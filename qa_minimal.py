 # -*- coding: utf-8 -*-
# 作者：zixiny-yee
# 创建时间：2026年5月
# 联系方式: yeziwquq@m.scnu.edu.cn
# 描述：中学计算机网络知识库 - 核心问答逻辑

import os
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from docx import Document
import fitz
import ollama

class MiniTeachingKB:
    def __init__(self, docs_folder="./docs"):
        # 直接加载本地已有模型，不走网络
        self.encoder = SentenceTransformer('local_model')
        self.docs = []
        self.doc_names = []
        self.embeddings = None

        for fname in os.listdir(docs_folder):
            file_path = os.path.join(docs_folder, fname)
            text = ""

            if fname.endswith('.txt'):
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read()
            elif fname.endswith('.docx'):
                doc = Document(file_path)
                text = "\n".join([p.text for p in doc.paragraphs])
            elif fname.endswith('.pdf'):
                pdf_doc = fitz.open(file_path)
                text = "\n".join([page.get_text() for page in pdf_doc])
                pdf_doc.close()
            else:
                continue

            if text.strip():
                self.docs.append(text)
                self.doc_names.append(fname)

        if self.docs:
            self.embeddings = self.encoder.encode(self.docs)

    def ask(self, question, top_k=3):
        q_emb = self.encoder.encode([question])
        similarities = cosine_similarity(q_emb, self.embeddings)[0]
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        context = "\n".join([self.docs[i][:1000] for i in top_indices])

        prompt = f"""你是一位经验丰富的中学信息技术教师，擅长用生动易懂的方式讲解计算机网络知识。

请根据以下教学资料回答学生的问题：
- 用通俗的语言解释，避免过于专业的术语
- 如果资料足以回答问题，请给出完整解答
- 如果资料不足以回答问题，请明确说明"资料中没有相关内容"，再结合你的知识补充

资料：
{context}

学生问题：{question}"""
        client = ollama.Client(host='http://127.0.0.1:11434')
        response = client.chat(model='qwen2:0.5b', messages=[{'role': 'user', 'content': prompt}])
        return response['message']['content']

if __name__ == "__main__":
    kb = MiniTeachingKB()
    print(kb.ask("如何解释TCP和UDP的区别？"))
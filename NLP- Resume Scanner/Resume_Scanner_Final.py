
import docx2txt
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
resume=docx2txt.process('Vatsal_CV.docx')
job_description=docx2txt.process('Dot Foods RD Intern Job Description.docx')

print(resume)
print(job_description)

content=[job_description,resume]



cv=CountVectorizer()
matrix=cv.fit_transform(content)

similarity_matrix=cosine_similarity(matrix)


print(similarity_matrix)

print("Resume Matches by:"+str(similarity_matrix[1][0]*100)+"%")

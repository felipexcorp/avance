# coding=utf-8
from backend.src.entities.entity import Session, engine, Base
from backend.src.entities.exam   import Exam

#from entities.entity import Session, engine, Base
#from entities.exam   import Exam
# generate database schema
Base.metadata.create_all(engine)

# start session
session = Session()

# check for existing data
exams = session.query(Exam).all()

if len(exams) == 0:
    # create and persist dummy exam
    python_exam = Exam("SQLAlchemy Exam", "Test your knowledge about SQLAlchemy.", "script")
    session.add(python_exam)
    session.commit()
    session.close()

    # reload exams
    exams = session.query(Exam).all()

# show existing exams
print('### Exams:')
for exam in exams :
    print(f'({exam.id}) {exam.title} - {exam.description} {exam.created_at} {exam.updated_at}')
git remote add origin https://github.com/felipexcorp/avance.git
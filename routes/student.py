from fastapi import APIRouter
from models.student import Student
from config.database import connection
from schemas.student import studentEntity, listOfStudentEntity

student_router = APIRouter()

#Get all students
@student_router.get('/students')
async def find_all_students():
    return listOfStudentEntity(connection.local.student.find())

#Creating a student
@student_router.post('/students')
async def create_student(student: Student):
    connection.local.student.insert_one(dict(student))
    return listOfStudentEntity(connection.local.student.find())
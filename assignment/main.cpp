#include <iostream>
#include <string>
#include <set>
using namespace std;

class Student {
public:
    int id;
    string firstName;
    string fatherName;
    int age;
    char sex;

    // Constructor
    Student(int _id, const string& _firstName, const string& _fatherName, int _age, char _sex)
        : id(_id), firstName(_firstName), fatherName(_fatherName), age(_age), sex(_sex) {}
};

class Course {
public:
    int courseNo;
    string courseTitle;
    int crh;

    // Constructor
    Course(int _courseNo, const string& _courseTitle, int _crh)
        : courseNo(_courseNo), courseTitle(_courseTitle), crh(_crh) {}
};

class TreeNode {
public:
    Student student;
    Course course;
    TreeNode* left;
    TreeNode* right;

    // Constructor
    TreeNode(const Student& _student, const Course& _course)
        : student(_student), course(_course), left(nullptr), right(nullptr) {}
};

class StudentRecordManager {
private:
    TreeNode* root;
    set<Course> availableCourses;
    set<Student> allStudents;

    TreeNode * addCourse(string courseTitle,int courseNo,int crh){
        Course  curr  = Course(courseNo,courseTitle,crh);
         auto foundCourse  = this->availableCourses.count(curr);
        if(foundCourse==0){
            cout<<"the course you are looking for is not currently available"<<endl;
            return nullptr; 
        }

        this->availableCourses.insert(curr);

    }

TreeNode* insert(TreeNode* node, const Student& student, const Course& course) {
    auto foundCourse = this->availableCourses.find(course);
    if (foundCourse == this->availableCourses.end()) {
        cout << "The course you are looking for is not currently available." << endl;
        return nullptr;
    }

    if (node == nullptr) {
        return new TreeNode(student, course);
    }

    if (student.id < node->student.id) {
        node->left = insert(node->left, student, course);
    } else if (student.id > node->student.id) {
        node->right = insert(node->right, student, course);
    }

    return node;
}
    void displayInOrder(TreeNode* node) const {
        if (node != nullptr) {
            displayInOrder(node->left);
            displayStudentAndCourse(node->student, node->course);
            displayInOrder(node->right);
        }
    }

    void displayStudentAndCourse(const Student& student, const Course& course) const {
        cout << "ID: " << student.id << ", Name: " << student.firstName << " " << student.fatherName
                  << ", Age: " << student.age << ", Sex: " << student.sex << "\n";
        cout << "Enrolled in Course - No: " << course.courseNo << ", Title: " << course.courseTitle << ", CRH: " << course.crh << "\n";
        cout << "-----------------------------------\n";
    }

public:
    StudentRecordManager() : root(nullptr) {}

    void registerStudent(const Student& student, const Course& course) {
        root = insert(root, student, course);
    }

    void displayAllStudents() const {
        displayInOrder(root);
    }
};

int main() {
    StudentRecordManager manager;

    // Register students and courses
    manager.registerStudent(Student(1, "John", "Doe", 20, 'M'), Course(101, "Math", 3));
    manager.registerStudent(Student(2, "Jane", "Smith", 22, 'F'), Course(102, "Physics", 4));

    // Display all students
    cout << "All Students:\n";
    manager.displayAllStudents();

    return 0;
}
#include <iostream>
#include <map>
#include <string>
#include <functional>

using namespace std;

//map<string, function<void()>> vtable;

// ID =  ParentsID ||MyID
class ParentClass1{
public:
    static const int ID = 1;
    string name = "ParentClass1";
    ParentClass1()= default;
};

class ParentClass2{
public:
    static const int ID = 2;
    string name = "ParentClass2";
    ParentClass2()= default;
};

class ChildClass1{
public:
    static const int ID = 13;
    string name = "ChildClass1";
    ChildClass1()= default;

    // constructor from parent class, because static_cast won't work otherwise
    ChildClass1(ParentClass1 p) {}
};

class ChildClass2{
public:
    static const int ID = 124;
    string name = "ChildClass2";
    ChildClass2()= default;
    ChildClass2(ParentClass1 p) {};
    ChildClass2(ParentClass2 p) {};
};

// casts for defined classes
#define MY_CLASSES_CASTS(C_id, from_obj) {\
    if(C_id = 1) \
        return static_cast<ParentClass1>(from_obj);\
    if(C_id =  13)\
        return static_cast<ChildClass1>(from_obj);    \
}

// down cast implementation
template <typename P, typename C>
C DYNAMIC_DOWN_CAST(int C_id, P from_obj){
    bool is_parent = false;

    int my_full_id = from_obj.ID;
    int other_id = C_id % 10;
    // check if type of @from_obj is parent to C type
    while(my_full_id > 0) {
        if(my_full_id % 10 == other_id) {
            is_parent = true;
            break;
        }
        my_full_id = my_full_id / 10;
    }
    if(is_parent)
        MY_CLASSES_CASTS(C_id, from_obj)
        //return static_cast<ChildClass1>(from_obj);//static_cast<C>(static_cast<ChildClass1>(from_obj));
}


/*Implementation of std::type_info
 * based on //https://en.cppreference.com/w/cpp/types/type_info */
template <typename T>
class type_info {
    public:
        bool operator=(T obj) = delete;  // can not be copy-assigned
        bool operator==(T obj) {return true;};
        int hash_code(T obj) {return obj.type_id;} // returns a value which is identical for the same types
        string name(T obj) {return obj.name;} // 	implementation defined name of the type
};

int main() {
    std::cout << "Create obj of classes"<< std::endl;
    ParentClass1 P1 =ParentClass1();
    ChildClass1 C1 = ChildClass1();

    std::cout << "Down Cast"<< std::endl;

    //down cast
    ChildClass1 P1_to_C1 = DYNAMIC_DOWN_CAST<ParentClass1, ChildClass1>(C1.ID, P1);

    std::cout << P1.name<<std::endl;
    std::cout << C1.name<<std::endl;
    std::cout << P1_to_C1.name<<std::endl;

}
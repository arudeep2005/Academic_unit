import re
import tkinter as tk
import pickle
from tkinter import messagebox,ttk
import tkinter.simpledialog

class Person:
    def __init__(self, user_id, password, role):
        self.user_id = user_id
        self.password = password
        self.role = role
        self.attempts = 0
        self.active = True


class Teacher(Person):
    def __init__(self, user_id, password, **user_details):
        super().__init__(user_id, password, role="Teacher")
        self.program = "Teacher"  
        self.name = user_details.get("name", "")
        self.department = user_details.get("department", "")
        self.city = user_details.get("city", "")
        self.college = user_details.get("college", "")
        self.courses_taught = user_details.get("courses_taught", "")  
        self.graduation_college = user_details.get("graduation_college", "")


class Student(Person):
    def __init__(self, user_id, password, role, program):
        super().__init__(user_id, password, role)
        self.program = program


class UGStudent(Student):
    def __init__(self, user_id, password, **user_details):
        super().__init__(user_id, password, role="UG", program="UG")
        self.name = user_details.get("name", "")
        self.department = user_details.get("department", "")
        self.city = user_details.get("city", "")
        self.college = user_details.get("college", "")
        self.cgpa = user_details.get("cgpa", 0.0)


class PGStudent(Student):
    def __init__(self, user_id, password, **user_details):
        super().__init__(user_id, password, role="PG", program="PG")
        self.name = user_details.get("name", "")
        self.department = user_details.get("department", "")
        self.city = user_details.get("city", "")
        self.college = user_details.get("college", "")
        self.specialisation = user_details.get("specialisation", "")
        self.phd_under = user_details.get("phd_under", "")

        
class UGStudentProfileGUI:
    def __init__(self, master, academic_unit, user_id):
        self.master = master
        self.master.title("UG Student Profile")
        self.master.geometry("1000x600")

        self.academic_unit = academic_unit
        self.user_id = user_id

        # Find the UGStudent instance based on user_id
        ug_student = next((user for user in academic_unit.users if isinstance(user, UGStudent) and user.user_id == user_id), None)

        if ug_student:
            self.display_profile(ug_student)
        else:
            messagebox.showerror("Error", "User not found or not a UG Student.")
            self.master.destroy()
            

    def display_profile(self, ug_student):
        # Display UG Student profile details
        title_style = ttk.Style()
        title_style.configure("Title.TLabel", font=("Times New Roman", 40, "bold", "underline"), background="#4CAF50", foreground="white")
        
        self.title_label = ttk.Label(self.master, text="UG Student Profile", style="Title.TLabel")
        self.title_label.pack(pady=40)
        self.label_name = tk.Label(self.master, text=f"Name   :   {ug_student.name}",font=("Times New Roman", 25, "bold"))
        self.label_name.pack()

        self.label_department = tk.Label(self.master, text=f"Department   :   {ug_student.department}",font=("Times New Roman", 25, "bold"))
        self.label_department.pack()

        self.label_city = tk.Label(self.master, text=f"City   :   {ug_student.city}",font=("Times New Roman", 25, "bold"))
        self.label_city.pack()

        self.label_college = tk.Label(self.master, text=f"College   :   {ug_student.college}",font=("Times New Roman", 25, "bold"))
        self.label_college.pack()

        self.label_cgpa = tk.Label(self.master, text=f"CGPA   :   {ug_student.cgpa}",font=("Times New Roman", 25, "bold"))
        self.label_cgpa.pack()


class PGStudentProfileGUI:
    def __init__(self, master, academic_unit, user_id):
        self.master = master
        self.master.title("PG Student Profile")
        self.master.geometry("1000x600")

        self.academic_unit = academic_unit
        self.user_id = user_id

        # Find the UGStudent instance based on user_id
        pg_student = next((user for user in academic_unit.users if isinstance(user, PGStudent) and user.user_id == user_id), None)

        if pg_student:
            self.display_profile(pg_student)
        else:
            messagebox.showerror("Error", "User not found or not a UG Student.")
            self.master.destroy()

    def display_profile(self, pg_student):
        # Display PG Student profile details
        title_style = ttk.Style()
        title_style.configure("Title.TLabel", font=("Times New Roman", 40, "bold", "underline"), background="#4CAF50", foreground="white")
        
        self.title_label = ttk.Label(self.master, text="PG Student Profile", style="Title.TLabel")
        self.title_label.pack(pady=40)
        self.label_name = tk.Label(self.master, text=f"Name   :  {pg_student.name}",font=("Times New Roman", 25, "bold"))
        self.label_name.pack()

        self.label_department = tk.Label(self.master, text=f"Department   :  {pg_student.department}",font=("Times New Roman", 25, "bold"))
        self.label_department.pack()

        self.label_city = tk.Label(self.master, text=f"City   :   {pg_student.city}",font=("Times New Roman", 25, "bold"))
        self.label_city.pack()

        self.label_college = tk.Label(self.master, text=f"College   :   {pg_student.college}",font=("Times New Roman", 25, "bold"))
        self.label_college.pack()

        self.label_specialisation = tk.Label(self.master, text=f"Specialisation   :   {pg_student.specialisation}",font=("Times New Roman", 25, "bold"))
        self.label_specialisation.pack()
        
        self.label_phd_under = tk.Label(self.master, text=f"PhD Under   :   {pg_student.phd_under}",font=("Times New Roman", 25, "bold"))
        self.label_phd_under.pack()
        
class TeacherProfileGUI:
    def __init__(self, master, academic_unit, user_id):
        self.master = master
        self.master.title("PG Student Profile")
        self.master.geometry("1000x600")

        self.academic_unit = academic_unit
        self.user_id = user_id

        # Find the UGStudent instance based on user_id
        teacher = next((user for user in academic_unit.users if isinstance(user, Teacher) and user.user_id == user_id), None)

        if teacher:
            self.display_profile(teacher)
        else:
            messagebox.showerror("Error", "User not found or not a Teacher.")
            self.master.destroy()

    def display_profile(self, teacher):
        # Display teacher profile details
        title_style = ttk.Style()
        title_style.configure("Title.TLabel", font=("Times New Roman", 40, "bold", "underline"), background="#4CAF50", foreground="white")
        
        self.title_label = ttk.Label(self.master, text="Teacher Profile", style="Title.TLabel")
        self.title_label.pack(pady=40)
        self.label_name = tk.Label(self.master, text=f"Name   :   {teacher.name}",font=("Times New Roman", 25, "bold"))
        self.label_name.pack()

        self.label_department = tk.Label(self.master, text=f"Department   :   {teacher.department}",font=("Times New Roman", 25, "bold"))
        self.label_department.pack()

        self.label_city = tk.Label(self.master, text=f"City   :   {teacher.city}",font=("Times New Roman", 25, "bold"))
        self.label_city.pack()

        self.label_college = tk.Label(self.master, text=f"College   :   {teacher.college}",font=("Times New Roman", 25, "bold"))
        self.label_college.pack()
        
        self.label_courses_taught = tk.Label(self.master, text=f"Courses Taught   :   {teacher.courses_taught}",font=("Times New Roman", 25, "bold"))
        self.label_courses_taught.pack()
        
        self.label_graduation_college = tk.Label(self.master, text=f"Graduation College   :   {teacher.graduation_college}",font=("Times New Roman", 25, "bold"))
        self.label_graduation_college.pack()
        
class UserProfileGUI:
    def __init__(self, master, academic_unit, user_id):
        self.master = master
        self.master.title("User Profile")
        self.master.geometry("1000x600")
        title_style = ttk.Style()
        title_style.configure("Title.TLabel", font=("Times New Roman", 40, "bold", "underline"), background="#4CAF50", foreground="white")
        
        self.title_label = ttk.Label(master, text="User Profile", style="Title.TLabel")
        self.title_label.pack(pady=40)

        self.academic_unit = academic_unit
        self.user_id = user_id

        self.user_details = self.get_user_details()

        for key, value in self.user_details.items():
            label = tk.Label(master, text=f"{key}: {value}",font=("Times New Roman", 25, "bold"))
            label.pack()

        # Edit Profile Button
        self.edit_profile_button = tk.Button(master, text="Edit Profile", command=self.edit_profile)
        self.edit_profile_button.pack()

    def get_user_details(self):
        for user in self.academic_unit.users:
            if user.user_id == self.user_id and user.active:
                user_details = {"User ID": user.user_id, "Role": user.role}

                if isinstance(user, UGStudent):
                    user_details.update({
                        "Program": user.program,
                        "Name": user.name,
                        "Department": user.department,
                        "City": user.city,
                        "College": user.college,
                        "CGPA": user.cgpa
                    })
                elif isinstance(user, PGStudent):
                    user_details.update({
                        "Program": user.program,
                        "Name": user.name,
                        "Department": user.department,
                        "City": user.city,
                        "College": user.college,
                        "Specialisation": user.specialisation,
                        "PhD Under": user.phd_under
                    })
                elif isinstance(user, Teacher):
                    user_details.update({
                        "Program": user.program,
                        "Name": user.name,
                        "Department": user.department,
                        "City": user.city,
                        "College": user.college,
                        "Courses Taught": user.courses_taught,
                        "Graduation College": user.graduation_college
                    })

                return user_details

        return {}

    def edit_profile(self):
        user = next((user for user in self.academic_unit.users if user.user_id == self.user_id and user.active), None)

        if user:
            edit_window = tk.Toplevel(self.master)
            edit_profile_gui = EditProfileGUI(edit_window, self.academic_unit, user)

class EditProfileGUI:
    def __init__(self, master, academic_unit, user):
        self.master = master
        self.master.title("Edit Profile")
        self.master.geometry("1000x600")
        title_style = ttk.Style()
        title_style.configure("Title.TLabel", font=("Times New Roman", 40, "bold", "underline"), background="#4CAF50", foreground="white")
        
        self.title_label = ttk.Label(master, text="Edit profile", style="Title.TLabel")
        self.title_label.pack(pady=40)

        self.academic_unit = academic_unit
        self.user = user

        self.edit_details = {}
        self.create_edit_fields()

        self.save_button = tk.Button(master, text="Save Changes", command=self.save_changes)
        self.save_button.pack()

    def create_edit_fields(self):
        for key, value in self.user.__dict__.items():
            if key not in ["user_id", "password", "role", "attempts", "active"]:
                frame = tk.Frame(self.master)
                frame.pack(fill="both", expand=True)
                label = tk.Label(frame, text=f"{key.capitalize()}:",font=("Times New Roman", 25, "bold"))
                label.pack(side="left")
                entry = tk.Entry(frame)
                entry.pack(side="right")
                entry.insert(0, str(value))
                self.edit_details[key] = entry

    def save_changes(self):
        for key, entry in self.edit_details.items():
            setattr(self.user, key, entry.get())
        self.academic_unit.save_data()
        messagebox.showinfo("Success", "Profile updated successfully.")
        self.master.destroy()  # Close the EditProfileGUI window after saving changes



class AcademicUnit:
    def __init__(self):
        self.users = []
        self.load_data()
        
    def load_data(self):
        try:
            with open("user_data.pkl", "rb") as file:
                self.users = pickle.load(file)
        except FileNotFoundError:
            # File does not exist (first run), initialize an empty list
            self.users = []
            
    def save_data(self):
        with open("user_data.pkl", "wb") as file:
            pickle.dump(self.users, file)

    def is_valid_password(self, password):
        # Password validation logic (same as before)
        if 8 <= len(password) <= 12 and re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) \
                and re.search(r'\d', password) and re.search(r'[!@#$%&*]', password) and ' ' not in password:
            return True
        else:
            return False

    def register_user(self, user_id, password, role, **user_details):
        valid_roles = ["Teacher", "UG Student", "PG Student"]
        if role not in valid_roles:
            messagebox.showwarning("Warning", "Invalid role. Allowed roles are: Teacher, UG Student, PG Student.")
            return

        if self.is_valid_password(password):
            if role == "Teacher":
                new_user = Teacher(user_id, password, **user_details)
            elif role == "UG Student":
                new_user = UGStudent(user_id, password, **user_details)
            elif role == "PG Student":
                new_user = PGStudent(user_id, password, **user_details)

            self.users.append(new_user)
            messagebox.showinfo("Success", f"User with ID {user_id} successfully registered as a {role}.")
        else:
            messagebox.showerror("Error", "Invalid password. Please check the password criteria.")
        self.save_data()

        
    def authenticate_user(self, user_id, password):
        for user in self.users:
            if user.user_id == user_id and user.active:
                if user.attempts < 2:
                    if user.password == password:
                        user.attempts = 0  # Reset attempts on successful login
                        return True
                    else:
                        user.attempts += 1
                        messagebox.showerror("Error", "Incorrect password. Please try again.")
                        return False
                else:
                    self.deregister_user(user_id)
                    messagebox.showinfo("Deregistered", "Too many unsuccesfull attempts\nAccount deregistered successfully.")

                    return False

        messagebox.showerror("Error", "User not found or account is inactive.")
        return False

    def update_profile(self, user_id, new_data):
        for user in self.users:
            if user.user_id == user_id and user.active:
                # Update user data (for simplicity, assuming new_data is a dictionary)
                for key, value in new_data.items():
                    setattr(user, key, value)
                messagebox.showinfo("Success", "User profile updated successfully.")
                return
        messagebox.showerror("Error", "User not found or account is inactive.")

    def deregister_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id and user.active:
                self.users.remove(user)
                messagebox.showinfo("Success", "Account successfully deregistered.")
                self.save_data()
                return

        messagebox.showerror("Error", "User not found or account is already inactive.")



class LoginGUI:
    def __init__(self, master, academic_unit):
        self.master = master
        self.master.title("User Login")
        self.master.geometry("1000x600")
        title_style = ttk.Style()
        title_style.configure("Title.TLabel", font=("Times New Roman", 40, "bold", "underline"), background="#4CAF50", foreground="white")
        
        self.title_label = ttk.Label(master, text="Login Window", style="Title.TLabel")
        self.title_label.pack(pady=40)

        self.label_email = tk.Label(master, text="Email / Username:", font=("Times New Roman", 25, "bold"))
        self.label_email.pack()

        self.entry_email = tk.Entry(master)
        self.entry_email.pack()

        self.label_password = tk.Label(master, text="Password:", font=("Times New Roman", 25, "bold"))
        self.label_password.pack()

        self.entry_password = tk.Entry(master, show="*")
        self.entry_password.pack()

        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.login_button.pack()

        self.academic_unit = academic_unit

    def login(self):
        user_id = self.entry_email.get()
        password = self.entry_password.get()

        if self.academic_unit.authenticate_user(user_id, password):
            messagebox.showinfo("Success", "Login successful.")

            # Open the user profile window
            profile_window = tk.Toplevel(self.master)
            profile_gui = UserProfileGUI(profile_window, self.academic_unit, user_id)

        #     self.master.destroy()
        else:
            self.master.destroy()


class RegistrationGUI:
    def __init__(self, master, academic_unit):
        self.master = master
        self.master.title("User Registration")
        self.master.geometry("1000x700")
        title_style = ttk.Style()
        title_style.configure("Title.TLabel", font=("Times New Roman", 40, "bold", "underline"), background="#4CAF50", foreground="white")
        
        self.title_label = ttk.Label(master, text="Register new account", style="Title.TLabel")
        self.title_label.pack(pady=20)

        self.academic_unit = academic_unit

        self.label_email = tk.Label(master, text="Email / Username:", font=("Times New Roman", 25, "bold"))
        self.label_email.pack()

        self.entry_email = tk.Entry(master)
        self.entry_email.pack()

        self.label_password = tk.Label(master, text="Password:", font=("Times New Roman", 25, "bold"))
        self.label_warning = tk.Label(master, text="(Password must be 8-12 characters long and contain at least one uppercase letter, one lowercase letter, one digit and one special character.)", font=("Times New Roman", 15, "bold"))                            

        self.label_password.pack()
        self.label_warning.pack()

        self.entry_password = tk.Entry(master, show="*")
        self.entry_password.pack()

        self.label_role = tk.Label(master, text="Role:", font=("Times New Roman", 25, "bold"))
        self.label_role.pack()

        self.role_var = tk.StringVar()
        self.role_var.set("Teacher")  # Default role is Teacher
        self.role_dropdown = ttk.Combobox(master, textvariable=self.role_var, values=["Teacher", "UG Student", "PG Student"])
        self.role_dropdown.pack()

        self.next_button = tk.Button(master, text="Next", command=self.validate_password)
        self.next_button.pack()

        # Additional details (hidden initially)
        self.label_name = tk.Label(master, text="Name:")
        self.entry_name = tk.Entry(master)

        self.label_department = tk.Label(master, text="Department:")
        self.entry_department = tk.Entry(master)

        self.label_city = tk.Label(master, text="City:")
        self.entry_city = tk.Entry(master)

        self.label_college = tk.Label(master, text="College:")
        self.entry_college = tk.Entry(master)

        self.label_cgpa = tk.Label(master, text="CGPA:")
        self.entry_cgpa = tk.Entry(master)

        self.label_specialisation = tk.Label(master, text="Specialisation:")
        self.entry_specialisation = tk.Entry(master)

        self.label_phd_under = tk.Label(master, text="PhD Under:")
        self.entry_phd_under = tk.Entry(master)
        
        self.label_courses_taught = tk.Label(master, text="Courses Taught:")
        self.entry_courses_taught = tk.Entry(master)
        
        self.label_graduation_college = tk.Label(master, text="Graduation College:")
        self.entry_graduation_college = tk.Entry(master)

        self.register_button = tk.Button(master, text="Register", command=self.register_user)

    def validate_password(self):
        user_id = self.entry_email.get()
        password = self.entry_password.get()

        # Check if the user is already registered
        for user in self.academic_unit.users:
            if user.user_id == user_id:
                if user.active:
                    messagebox.showerror("Error", "User is already registered.")
                    return

        # Check if the password is valid
        if not self.academic_unit.is_valid_password(password):
            messagebox.showerror("Error", "Invalid password. Please check the password criteria.")
            return
        #user.active = True

        # Proceed to collect additional details
        self.show_additional_details()

    def show_additional_details(self):
        # Hide the next button
        self.next_button.pack_forget()

        # Show additional details based on the selected role
        self.label_name.pack()
        self.entry_name.pack()

        self.label_department.pack()
        self.entry_department.pack()

        self.label_city.pack()
        self.entry_city.pack()

        self.label_college.pack()
        self.entry_college.pack()

        if self.role_var.get() == "UG Student":
            self.label_cgpa.pack()
            self.entry_cgpa.pack()
        elif self.role_var.get() == "PG Student":
            self.label_specialisation.pack()
            self.entry_specialisation.pack()

            self.label_phd_under.pack()
            self.entry_phd_under.pack()
        elif self.role_var.get() == "Teacher":
            self.label_courses_taught.pack()
            self.entry_courses_taught.pack()
            
            self.label_graduation_college.pack()
            self.entry_graduation_college.pack()

        # Show the register button
        self.register_button.pack()

    def register_user(self):
        user_id = self.entry_email.get()
        password = self.entry_password.get()
        role = self.role_var.get()

        # Collect user details based on role
        user_details = {
            "name": self.entry_name.get(),
            "department": self.entry_department.get(),
            "city": self.entry_city.get(),
            "college": self.entry_college.get(),
        }

        if role == "UG Student":
            user_details["cgpa"] = float(self.entry_cgpa.get())
        elif role == "PG Student":
            user_details["specialisation"] = self.entry_specialisation.get()
            user_details["phd_under"] = self.entry_phd_under.get()
        elif role == "Teacher":
            user_details["courses_taught"] = self.entry_courses_taught.get()
            user_details["graduation_college"] = self.entry_graduation_college.get()

        # Register the user
        self.academic_unit.register_user(user_id, password, role, **user_details)

        # Open profile window based on the selected role
        if role == "UG Student":
            ug_profile_window = tk.Toplevel(self.master)
            ug_profile_gui = UGStudentProfileGUI(ug_profile_window, self.academic_unit, user_id)
        elif role == "PG Student":
            pg_profile_window = tk.Toplevel(self.master)
            pg_profile_gui = PGStudentProfileGUI(pg_profile_window, self.academic_unit, user_id)
        elif role == "Teacher":
            teacher_profile_window = tk.Toplevel(self.master)
            teacher_profile_gui = TeacherProfileGUI(teacher_profile_window, self.academic_unit, user_id)

        # Optionally, you can close the registration window after successful registration
        # self.master.destroy()


class DeregistrationGUI:
    def __init__(self, master, academic_unit):
        self.master = master
        self.master.title("Deregister User")
        self.master.geometry("1000x600")
        title_style = ttk.Style()
        title_style.configure("Title.TLabel", font=("Times New Roman", 40, "bold", "underline"), background="#4CAF50", foreground="white")
        
        self.title_label = ttk.Label(master, text="Deregister account", style="Title.TLabel")
        self.title_label.pack(pady=40)

        self.label_email = tk.Label(master, text="Email / Username:",font=("Times New Roman", 25, "bold"))
        self.label_email.pack()

        self.entry_email = tk.Entry(master)
        self.entry_email.pack()

        self.label_password = tk.Label(master, text="Password:",font=("Times New Roman", 25, "bold"))
        self.label_password.pack()

        self.entry_password = tk.Entry(master, show="*")
        self.entry_password.pack()

        self.deregister_button = tk.Button(master, text="Deregister", command=self.deregister_user)
        self.deregister_button.pack()

        self.academic_unit = academic_unit

    def deregister_user(self):
        user_id = self.entry_email.get()
        password = self.entry_password.get()

        if self.academic_unit.authenticate_user(user_id, password):
            response = messagebox.askquestion("Confirmation", "Are you sure you want to deregister your account?")
            if response == 'yes':
                self.academic_unit.deregister_user(user_id)
                self.master.destroy()
            else:
                messagebox.showinfo("Cancelled", "Deregistration process cancelled.")
        else:
            messagebox.showerror("Error", "Incorrect password. Please try again.")


class MainApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Academic Unit Management")
        self.master.geometry("800x400")
        self.master.configure(bg="lightgrey")
        title_style = ttk.Style()
        title_style.configure("Title.TLabel", font=("Times New Roman", 40, "bold", "underline"), background="#4CAF50", foreground="white")

        # Title Label
        self.title_label = ttk.Label(master, text="Welcome to Academic Unit Management", style="Title.TLabel")
        self.title_label.pack(pady=20)

        self.academic_unit = AcademicUnit()

        self.login_button = tk.Button(master, text="Login", command=self.open_login_window)
        self.login_button.pack(pady=5)

        self.register_button = tk.Button(master, text="Register", command=self.open_registration_window)
        self.register_button.pack(pady=40)

        self.deregister_button = tk.Button(master, text="Deregister", command=self.open_deregistration_window)
        self.deregister_button.pack()

    def open_login_window(self):
        login_window = tk.Toplevel(self.master)
        login_gui = LoginGUI(login_window, self.academic_unit)

    def open_registration_window(self):
        registration_window = tk.Toplevel(self.master)
        registration_gui = RegistrationGUI(registration_window, self.academic_unit)

    def open_deregistration_window(self):
        deregistration_window = tk.Toplevel(self.master)
        deregistration_gui = DeregistrationGUI(deregistration_window, self.academic_unit)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()  
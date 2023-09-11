class Job:
    def __init__(self, profession):
        self.profession = profession
        self.vacancies = []

    def post_vacancy(self, company, salary, min_exp):
        vacancy = {
            'company': company,
            'salary': salary,
            'min_exp': min_exp
        }
        self.vacancies.append(vacancy)

    def close_vacancy(self, company):
        self.vacancies = [vacancy for vacancy in self.vacancies if vacancy['company'] != company]

    def update_salary(self, company, new_salary):
        for vacancy in self.vacancies:
            if vacancy['company'] == company:
                vacancy['salary'] = new_salary

    def update_exp(self, company, new_exp):
        for vacancy in self.vacancies:
            if vacancy['company'] == company:
                vacancy['min_expp'] = new_exp

    def show_vacancies(self):
        print(f"Вакансии по профессии '{self.profession}':")
        if not self.vacancies:
            print("Пока нет вакансий на данную профессию")
        else:
            for vacancy in self.vacancies:
                print(f"{vacancy['company']}: зарплата {vacancy['salary']} тыс, требуемый опыт {vacancy['min_exp']}")

    def find_best_vacancy(self, exp, profession, min_salary):
        if profession != self.profession:
            print(f"Кажется, вы ищете вакансии в разделе {self.profession}. Выберите другой раздел.")
            return
        best_vacancy = None
        for vacancy in self.vacancies:
            if vacancy['min_exp'] <= exp and vacancy['salary'] >= min_salary:
                if best_vacancy is None or vacancy['salary'] > best_vacancy['salary']:
                    best_vacancy = vacancy

        if best_vacancy is not None:
            print(
                f"Наилучшая вакансия для вас в компании"
                f" \"{best_vacancy['company']}\""
                f" с зарплатой {best_vacancy['salary']} тыс.")
            self.close_vacancy(best_vacancy['company'])
        else:
            print("Простите, для вас не нашлось вакансий.")

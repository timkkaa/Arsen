from datetime import datetime, timedelta


class TimeDisplayer:
    time = {
        'hours': 0,
        'minutes': 0,
        'seconds': 0
    }
    day_of_week = ""
    day = 0
    month = 0
    year = 0

    def __return_weekday(self, weekday):
        days = [
            "Понедельник",
            "Вторник",
            "Среда",
            "Четверг",
            "Пятница",
            "Суббота",
            "Воскресенье"
        ]

        return days[weekday]

    def set_datetime(self):
        current_time = datetime.now()

        self.time['hours'] = current_time.hour
        self.time['minutes'] = current_time.minute
        self.time['seconds'] = current_time.second

        self.day = current_time.day
        self.month = current_time.month
        self.year = current_time.year
        self.day_of_week = self.__return_weekday(current_time.weekday())

    def get_datetime(self):
        formatted_datetime = f"""
[=============================]

{f"{self.hours}:{self.minutes}:{self.seconds}".center(31, " ")}
{f"Сейчас {self.day_of_week}".center(31, " ")}
{f"{self.day}.{self.month}.{self.year}".center(31, " ")}

[=============================]
"""

        return formatted_datetime

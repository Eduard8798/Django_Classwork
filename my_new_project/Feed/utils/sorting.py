class Sorting:
    @staticmethod
    def sort_by_date(data):
        return sorted(data,key=lambda x: x['date'],reverse=True)
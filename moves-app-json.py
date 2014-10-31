import json

class MovesAppJson:

    def __init__(self, json_dir, daily = False, weekly = False, monthly = False, yearly = False, full = True):
        self.json_dir = json_dir
        self.json_dir_daily = None
        self.json_dir_weekly = None
        self.json_dir_monthly = None
        self.json_dir_yearly = None
        self.json_dir_full = None

        if daily:
            self.json_dir_daily = self.json_dir + '/daily'
        if weekly:
            self.json_dir_weekly = self.json_dir + '/weekly'
        if monthly:
            self.json_dir_monthly = self.json_dir + '/monthly'
        if yearly:
            self.json_dir_yearly = self.json_dir + '/yearly'
        if full:
            self.json_dir_full = self.json_dir + '/full'

        self._full_activities = []
        self._full_places = []
        self._full_storyline = []
        self._full_summary = []
        self.full = {'activities': [],
                     'places': [],
                     'storyline': [],
                     'summary': []}


    def _read_full_activities(self):
        """
        """

        full_activities_filename = self.json_dir_full + '/activities.json'

        with open(full_activities_filename) as jsonFileHandle:
            self._full_activities = json.load(jsonFileHandle)


    def get_full_activities(self):
        """
        """

        self._read_full_activities()

        return self._full_activities

    def _read_full_places(self):
        """
        """

        full_places_filename = self.json_dir_full + '/places.json'

        with open(full_places_filename) as jsonFileHandle:
            self._full_places = json.load(jsonFileHandle)


    def get_full_places(self):
        """
        """

        self._read_full_places()

        return self._full_places

    def _read_full_storyline(self):
        """
        """

        full_storyline_filename = self.json_dir_full + '/storyline.json'

        with open(full_storyline_filename) as jsonFileHandle:
            self._full_storyline = json.load(jsonFileHandle)

    def get_full_storyline(self):
        """
        """

        self._read_full_storyline()

        return self._full_storyline

    def _read_full_summary(self):
        """
        """

        full_summary_filename = self.json_dir_full + '/summary.json'

        with open(full_summary_filename) as jsonFileHandle:
            self._full_summary = json.load(jsonFileHandle)

    def get_full_summary(self):
        """
        """

        self._read_full_summary()

        return self._full_summary

    def get_full(self):
        """
        """

        self._read_full_activities()
        self._read_full_places()
        self._read_full_storyline()
        self._read_full_summary()

        self.full['activities'] = self._full_activities
        self.full['places'] = self._full_places
        self.full['storyline'] = self._full_storyline
        self.full['summary'] = self._full_summary

if __name__ == '__main__':

    m = MovesAppJson('json')

    m.get_full_activities()
    m.get_full_places()
    m.get_full_storyline()
    m.get_full_summary()

    m.get_full()

    print m.full


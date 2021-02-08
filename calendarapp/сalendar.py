class Calendar:

	def __init__(self, params):
		if 'person' in params:
			self.person = params['person']

	def currentWeek(self):
		testWeek = {
			'title': 'WEEK',
			'days' : [
				{ 'name': 'Monday' },
				{ 'name': 'Tuesday',
				  'events' : {
					120: { 'title': 'A', 'duration': 60 },
					720: { 'title': 'B', 'duration': 90 },
					}
				},
				{ 'name': 'Wednesday' },
				{ 'name': 'Thursday' },
				{ 'name': 'Friday' },
				{ 'name': 'Satturday' },
				{ 'name': 'Sunday' },
			]
		}
		return testWeek

class Person:

	def __init__(self, params):
		pass

	def getCalendar(self):
		return Calendar({ 'person': self })



def getPersonalCalendar(loginId):
	return Person({ 'loginId': loginId }).getCalendar()

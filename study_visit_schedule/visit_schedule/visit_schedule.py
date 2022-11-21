from edc_visit_schedule import VisitSchedule, site_visit_schedules
from .schedule import schedule

subject_visit_schedule = VisitSchedule(
    name='subject_visit_schedule',
    verbose_name='Study',
    offstudy_model='study_subject.subjectoffstudy',
    locator_model='study_subject.subject_locator'
)


subject_visit_schedule.add_schedule(schedule)


site_visit_schedules.register(subject_visit_schedule)
from edc_visit_schedule import VisitSchedule, site_visit_schedules
from .schedule import schedule_1

visit_schedule_1 = VisitSchedule(
    name='subject_visit_schedule',
    verbose_name='Study',
    offstudy_model='study_subject.subjectoffstudy',
    locator_model='study_subject.subject_locator',
    death_report_model='study_prn.death_report',
    previous_visit_schedule=None
)

visit_schedule_1.add_schedule(schedule_1)

site_visit_schedules.register(visit_schedule_1)

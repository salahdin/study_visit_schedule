from edc_visit_schedule import Schedule, Visit
from dateutil.relativedelta import relativedelta
from .requisitions import requisitions
from .crfs import crf

schedule = Schedule(name='subject_visit_schedule',
                    verbose_name='Visit Schedule',
                    onschedule_model='study_subject.onschedule',
                    offschedule_model='study_subject.offschedule',
                    appointment_model='edc_appointment.appointment',
                    consent_model='study_subject.subjectconsent')

# TODO: Add requisitions form and add offschedule model

# create visit with the 2 crfs for the initial visit
visit0 = Visit(
    code='1000',
    title='Visit 1000',
    timepoint=0,
    rbase=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(1))


visit1 = Visit(
    code='2000',
    title='Visit 2000',
    timepoint=0,
    rbase=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(2))


schedule.add_visit(visit0)
schedule.add_visit(visit1)

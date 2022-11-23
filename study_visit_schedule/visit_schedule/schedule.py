from edc_visit_schedule import Schedule, Visit
from dateutil.relativedelta import relativedelta
from .requisitions import requisitions
from .crfs import crf

schedule_1 = Schedule(name='subject_visit_schedule',
                      verbose_name='Visit Schedule',
                      onschedule_model='study_subject.onschedule',
                      offschedule_model='study_subject.offschedule',
                      appointment_model='edc_appointment.appointment',
                      consent_model='study_subject.subjectconsent')

# TODO: Add requisitions form and add offschedule model

# create visit with the 2 crfs for the initial visit
visit0 = Visit(
    code='1000',
    title='Visit 1',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(1),
    facility_name='clinic')

visit1 = Visit(
    code='2000',
    title='Visit 2',
    timepoint=1,
    rbase=relativedelta(days=2),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(2),
    facility_name='clinic')

schedule_1.add_visit(visit0)
schedule_1.add_visit(visit1)

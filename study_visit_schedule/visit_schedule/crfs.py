from edc_visit_schedule import FormsCollection, Crf

crf = {}

crf_1 = FormsCollection(
    Crf(show_order=1, model='study_subject.education'),
    name='fist visit'
)

crf.update({1: crf_1})

crf_2 = FormsCollection(
    Crf(show_order=2, model='study_subject.community_engagement'),
    name='second visit'
)
crf.update({2: crf_2})





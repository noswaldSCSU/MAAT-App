from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('participant_login/', views.participant_login, name='participant_login'),
    path('researcher_dashboard/', views.researcher_dashboard, name='researcher_dashboard'),
    path('experiment/create/step1/', views.create_experiment_step1, name='create_experiment_step1'),
    path('experiment/create/step2/<int:experiment_id>/', views.create_experiment_step2, name='create_experiment_step2'),
    path('experiment/create/step3/<int:experiment_id>/', views.create_experiment_step3, name='create_experiment_step3'),
    path('experiment/edit/<int:experiment_id>/', views.edit_experiment, name='edit_experiment'),
    path('experiment/delete/<int:experiment_id>/', views.delete_experiment, name='delete_experiment'),
    path('show_instructions/<int:participant_id>/<int:experiment_id>/', views.show_instructions, name='show_instructions'),
    path('start_experiment/<int:participant_id>/<int:experiment_id>/', views.start_experiment, name='start_experiment'),
    path('run_trial/', views.run_trial, name='run_trial'),
    path('save_response/', views.save_response, name='save_response'),
    path('experiment_complete/', views.experiment_complete, name='experiment_complete'),
    path('download_responses_csv/', views.download_responses_csv, name='download_responses_csv'),
    path('list_experiments/', views.list_experiments, name='list_experiments'),
    path('configure_experiment/<int:experiment_id>/', views.configure_experiment, name='configure_experiment'),
    path('manage_participants/', views.manage_participants, name='manage_participants'),
    path('register_participant/', views.register_participant, name='register_participant'),
    path('edit_participant/<int:participant_id>/', views.edit_participant, name='edit_participant'),
    path('delete_participant/<int:participant_id>/', views.delete_participant, name='delete_participant'),
    path('create_trial/', views.create_trial, name='create_trial'),
    path('edit_trial/<int:trial_id>/', views.edit_trial, name='edit_trial'),
    path('delete_trial/<int:trial_id>/', views.delete_trial, name='delete_trial'),
    path('export_csv/<int:experiment_id>/', views.export_csv, name='export_csv'),
]
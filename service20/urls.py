from django.urls import path
from service20.views import *
from . import views

app_name = 'service20'

urlpatterns = [
    
    #path('', views.stdApplyIns, name='stdApplyIns'),
    path('stdApplyStdView/', stdApplyStdView, name='detail'),
    path('Service20_01/', Service20_01_View, name='detail'),

    #멘토스쿨 리스트
    path('', Service20ListView.as_view(), name='Service20ListView'),

    path('authUserInfo/', post_user_info, name='post_user_info'),
    path('authUserInfoQuest/', post_user_info_Quest.as_view(), name='post_user_info_Quest'),


    path('msApply/', post_msApply, name='post_msApply'),
    path('mpmgListView/', mpmgListView.as_view(), name='mpmgListView'),
    path('mpmgListPersionView/', mpmgListPersionView.as_view(), name='mpmgListPersionView'),

    #멘토스쿨 콤보박스
    path('comboMpmgListView/', comboMpmgListView.as_view(), name='comboMpmgListView'),
    #멘토스쿨 콤보박스 Detail
    path('comboMpmgListViewDetail/', comboMpmgListViewDetail.as_view(), name='comboMpmgListViewDetail'),


    #멘토링 질문리스트
    path('post_mt_quest/', post_mt_quest, name='post_mt_Quest'),

]
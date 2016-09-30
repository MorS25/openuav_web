from django.shortcuts import render
from django.http import *
from django.template import loader
import subprocess
from .models import *

######

def index(request):
    template = loader.get_template('simulator/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def land(request):
    ls_output = subprocess.call("(rosrun mavros mavsys mode -c auto.land)",shell=True)
    return HttpResponse("landing...")

def takeoff(request):
    ls_output = subprocess.call("(rosrun mavros mavsys mode -c auto.takeoff)",shell=True)
    return HttpResponse("takeoff...")

def offboard(request):
    ls_output = subprocess.call("(rosrun mavros mavsys mode -c OFFBOARD)",shell=True)
    return HttpResponse("starting OFFBOARD mode...")

def mission(request):
    ls_output = subprocess.call("(rosrun mavros mavwp load /home/jdas/timpa-jd-updated.txt)",shell=True)
    ls_output = subprocess.call("(rosrun mavros mavwp setcur 0)",shell=True)
    ls_output = subprocess.call("(rosrun mavros mavsys mode -c auto.mission)",shell=True)
    ls_output = subprocess.call("(rosrun mavros mavsafety arm)", shell=True)
    return HttpResponse("starting mission mode...")

def arm(request):
    ls_output = subprocess.call("(rosrun mavros mavsafety arm)",shell=True)
    return HttpResponse("arming...")

def disarm(request):
    ls_output = subprocess.call("(rosrun mavros mavsafety disarm)",shell=True)
    return HttpResponse("disarming...")

def rtl(request):
    ls_output = subprocess.call("(rosrun mavros mavsys mode -c auto.rtl)",shell=True)
    return HttpResponse("rtl...")
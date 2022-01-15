import time       
import argparse
import ipaddress 


import subprocess
from colorama import init  
init()
from colorama import Fore
import threading           
from queue import Queue 

#-------------------------------------------------designings---------------------------------------------------------------------------

from colorama import init  # colors in text
init()



print( '\033[32m'+"""                                                                         
                                                                                 :#.               :#@@@@@@%%#+::                                         
                                                                              +%%+                  #@@@@@@@@@@@@*                                       
                                                                              =%%%-                   @@@@@@@@@@@@@@                                      
                                                                              %%%%:                   @@@@@@@@@@@@@@#                                     
                                                                              %%%%:                   %@@@@@@@@@@@@@@                                     
                                                                              %%%%-          *--- :   %@@@@@@@@@@@@@%                                     
                                                                              %%%%.#-       :         %@@@@@@@@@@@@%@.                                    
                                                                             .%%%%-: =.      :%%###*  *@@%::*%*#@@%@@:                                    
                                                                             .%%%%%%%-.     *%-    .+ +@=#@@@@@@@%@@@:                                    
                                                                             :%%  :%%%#    *%.        =-@@@#:. .:@@@@=                                    
                                                                             -%:    -%%    #          =@@%  .%@@# %@@*                                    
                                                                             +%      .%%              =@+ :@@@@@@@-@@#                                    
                                                                             *% *%%%*.*%=    -%%%%%   +# -@@@@@@@@@%@%                                    
                                                                             #@  -**:-%%#        .    + :@@@@@@@@@@@@%                                    
                                                                             *#      :%%#             +@@@@@@@@@@@@@@%                                    
                                                                             +#      :%%#             +@@@@@@%*#@@@@@%                                    
                                                                             =%      -%%+             *@@@-      %@@@%                                    
                                                                             :%.     #%%:             *@@@@%##@@@@@@@#                                    
                                                                             :%:     %%%              #@@@@@@@@@@@@@@#                                    
                                                                             .%:   .%*:#              %@@@@@@@@@@@@@@#                                    
                                                                              +   +%%+     +:    =++  %@@@@@@@@@@@@@@*                                    
                                                                              ==---**   ::+      #.%  %@@@@@@@@@@@@@@*                                    
                                                                              - +*+    #%*%+    #+ -  @@@@@@@@@@@@@@@+                                    
                                                                              ::%:#%##%%* *%%%%%# #  :@@@@@@@@@@@@@@@=                                    
                                                                               * % :*#%#    :-:  .:  *@@@@@@@@@@@@@@@-                                    
                                                                               .**%=.            =  .@@@@@@@@@@@@@@@@:                                    
                                                                                 :%%%%.         .   #@@*+@@@@@##++%@@:                                    
                                                                                ::-%%%% %**     .  .@@@@@@@@@@@ @=@@@:                                    
                                                                                  -*%%=  %-    -       %@@@@@@ -@.@@@.                                    
                                                                                   .%%: :%#   .     +=  #%@%#. @##@@@                                     
                                                                                    .%. %%%      .  @@=       @@-@@@+                                     
                                                                                   : -- @%%     : .@@@@@#***@@@%%@@@                                      
                                                                                    : = %%%    =%+=======+#@@@@=@@@#                                      
                                                                                     .  %%#    -@@@@@@@@@@@@@@*@@@@                                       
                                                                                      : =%-  :   %@@@@@@@@@@@@@@@%+                                       
                                                                                         .@+*    .@*-=-@@@@@@#@@@@                                        
                                                                                          =@#:   *@@. %@@@@@@@@@@.                                        
                                                                                           @%@   @@@  *@@@@@@@@@=                                         
                                                                                            @@* .@@@   @@@@@@@@#                                          
                                                                                            .@@:.@@#   @@@@@@@#                                           
                                                                                             .@@ @@*   @@@@@@%                                            
                                                                                              :@%*@*   @@@@@@                                             
                                                                                               =@*@%  :@@@@@                                              
                                                                                                =@@@  *%@@@                                               
                                                                                                 :@@  #@@+                                                
""")
print( '\033[91m'+"""\n
                                              #########-       .::.::                    @@@@@%      .   ..      .:::%@.                            @@@@@@@@@@#        
                                              ::::::::@=       %@@@@@       ######-      @::::%     *%   *%   :%%@@@#@=.    ######-     *=     *+   ::##::::::.        
                                                  @-   @=       %+  .@       @#***@=      @    %     +@:  #@   :@: @ .@:     @#****+@     %+     %*     #+               
                                                  @-   @=       %+  .@       @:   @=      @    %     -@:  #@   :@  @ .@:     @-    +@     %+     %*    .@                
                                               :**@#**=@=       %+  .@       @=@* @=      @    %     *@:  #@   :@  @ .@:     @-@*. +@     %+     %*    .@@@@@@@@         
                                               -##@%##+@=       %+  .@       @::%*@=      @    %     %#   #@   :@  @ .@:     @-.#@.+@     %+     %*           .@         
                                                  @-   @=      :@+  .@       @: ..@=      @    %     #@%:#@@   :@  @  @:     @-  . +@     %+     %*           .+         
                                                  @-   @=      -@=  .@       @+===@=     #+    % =+   *@@@%@   =@  @  #%     @*====+@     %#=====%*           ==         
                                                  @-   @+@    @@   .@  @    @@@@@@=    :@=    % =@       #@   @*  @  :@+    @@@@@@++@     *######@*           #-         
                                                  @-    @@  .@@-   .@*@@    @:   @=    %=     @*#.       #@  +@.  @   #%    @:    =#@            ::        ***@-         
                                                  @-    =#  :.#      =**=               +      ###       #@  ++   #    *                                 ###*          
                                                                                                              
                                                                                                                                  
""")
print('\033[32m'+"""
                                                                             %@@@@- %@ %@-  #@  .@@@=- @@@@@@ @@@@@:
                                                                            *@==+@:-@ +@@  .@ :@*-=@  @@==== @@==+@
                                                                            *@   @--@ +@@@ .@ @@      @@..*  @@  :@.
                                                                            *@@@@@ -@ +@ @@.@ @+  @@@ @@@@@  @@@@@*
                                                                            *@     -@ +@  @@@ @@    @ @@     @@ :@
                                                                            *@     -@ +@   @@  @@@@@@ @@@@@@ @@  %@""")

print('\033[32m'+"\nThis tool is developed by anon4mous. It is a pinging tool that can do all the stuffs normal ping command does along with those has a couple of handy features too. This tool is multi-threaded that is, it is faster than the normal ping command. Why waste your coffee and time out there finding live hosts, take a sip or two and your scan will be ready\n\n\nFor more information on the tool use '-h' for help of the tool\n\n")
print('\033[91m'+"Happy Hacking\n\n")
print(Fore.CYAN)
#-------------------------------------------end of designs----------------------------------------------------------------------------

#-----------------------------------------------------------parser coding(command line interaction)------------------------------------------

parser = argparse.ArgumentParser()
#adding message to help
msg = "This is a tool developed by Anon4mous, it basically pings websites/domains or ipaddress/iprange. We also could use ping command available by default but it is single threaded but the tool I developed is multi threaded hence saving your time. So you don't have to make coffee again and again, just get a sip or two and your sweep will be done by then. Good Luck and Happy Hunting"
 
# Initialize parser
parser = argparse.ArgumentParser(description = msg)

#adding argument for websites/domains pinging
parser.add_argument("-wp","--web-ping", help="Ping single websites/domains")

#list website/domain scan
parser.add_argument("-lwp","--list-web-ping", help="Ping websites/domains with list of websites/domains")

# adding argument for ipaddress/iprange pinging
parser.add_argument("-ip", "--ip-ping", help = "Ping ipaddress/iprange")

#list website/domain scan
parser.add_argument("-lip","--list-ip-ping", help="Ping ipaddress/iprange with list of ipaddress/iprange")

# Read arguments from command line
args = parser.parse_args()





#-------------------------------------------------------Functions------------------------------------------------------------------------


#--------------------------------------------ip ping funtions--------------------------------------------------------------------
def ip_ping_pingsweep(ip):
    
    # for windows:   -n is ping count, -w is wait (ms)
    # for linux: -c is ping count, -w is wait (ms)

    output = subprocess.Popen(['ping', '-n', '3', '-w', '50', str(all_hosts[ip])], stdout=subprocess.PIPE, startupinfo=info).communicate()[0]
    
    with thread_lock:
      
      # normalize colors to grey
      print('\033[93m', end='')

      # code logic if we have/don't have good response
      if "Reply" in output.decode('utf-8'):
         print(str(all_hosts[ip]), '\033[32m'+"is Online")
      elif "Destination host unreachable" in output.decode('utf-8'):
         #print(str(all_hosts[ip]), '\033[90m'+"is Offline (Unreachable)")
         pass
      elif "Request timed out" in output.decode('utf-8'):
         #print(str(all_hosts[ip]), '\033[90m'+"is Offline (Timeout)")
         pass
      else:
         # print colors in green if online
         pass

def ip_ping_threader():
   while True:
      worker = q.get()
      ip_ping_pingsweep(worker)
      q.task_done()

#-----------------------------------------------------ip list ping functions---------------------------------------------------------------


def ip_list_pingsweep(ip):
    

    output = subprocess.Popen(['ping', '-n', '3', '-w', '50', str(all_hosts[ip])], stdout=subprocess.PIPE, startupinfo=info).communicate()[0]
    
    with thread_lock:
      
      print('\033[93m', end='')

      if "Reply" in output.decode('utf-8'):
         print(str(all_hosts[ip]), '\033[32m'+"is Online")
      elif "Destination host unreachable" in output.decode('utf-8'):
         pass
      elif "Request timed out" in output.decode('utf-8'):
         pass
      else:

         pass

def ip_list_threader():
   while True:
      worker = q.get()
      ip_list_pingsweep(worker)
      q.task_done()


#----------------------------------------------------------web ping functions---------------------------------------------------------------

def web_pingsweep(ip):
    

    output = subprocess.Popen(['ping', '-n', '3', '-w', '50', str(web_file)], stdout=subprocess.PIPE, startupinfo=info).communicate()[0]
    
    with thread_lock:
      
      print('\033[93m', end='')
      if "Reply" in output.decode('utf-8'):
         print(str(web_file), '\033[32m'+"is Online")
      elif "Destination host unreachable" in output.decode('utf-8'):
         #print(str(all_hosts[ip]), '\033[90m'+"is Offline (Unreachable)")
         pass
      elif "Request timed out" in output.decode('utf-8'):
         #print(str(all_hosts[ip]), '\033[90m'+"is Offline (Timeout)")
         pass
      else:
         # print colors in green if online
         pass
def web_threader():
   while True:
      worker = q.get()
      web_pingsweep(worker)
      q.task_done()


#-----------------------------------------------------web list ping functions----------------------------------------------------------------

def web_list_pingsweep(ip):

    output = subprocess.Popen(['ping', '-n', '3', '-w', '50', str(web_list[ip])], stdout=subprocess.PIPE, startupinfo=info).communicate()[0]
    
    with thread_lock:
      
      # normalize colors to grey
      print('\033[93m', end='')

      # code logic if we have/don't have good response
      if "Reply" in output.decode('utf-8'):
         print(str(web_list[ip]), '\033[32m'+"is Online")
      elif "Destination host unreachable" in output.decode('utf-8'):
         #print(str(all_hosts[ip]), '\033[90m'+"is Offline (Unreachable)")
         pass
      elif "Request timed out" in output.decode('utf-8'):
         #print(str(all_hosts[ip]), '\033[90m'+"is Offline (Timeout)")
         pass
      else:
         # print colors in green if online
         pass

def web_list_threader():
   while True:
      worker = q.get()
      web_list_pingsweep(worker)
      q.task_done()



#----------------------------------------------------------end of functions------------------------------------------------------------------


#--------------------------------------------------------ip ping part-------------------------------------------------------------------------
if args.ip_ping:
    thread_lock = threading.Lock()
    net_addr = args.ip_ping

    startTime = time.time()

    ip_net = ipaddress.ip_network(net_addr)

    all_hosts = list(ip_net.hosts())

    info = subprocess.STARTUPINFO()
    info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    info.wShowWindow = subprocess.SW_HIDE
    print ('Sweeping Network with ICMP: ', net_addr)
    
    q = Queue()

    for x in range(100):
        t = threading.Thread(target = ip_ping_threader)
        t.daemon = True
        t.start()

    for worker in range(len(all_hosts)):
        q.put(worker)

    q.join()

    runtime = float("%0.2f" % (time.time() - startTime))
    print("Run Time: ", runtime, "seconds")

#---------------------------------------------------------End of ip ping part----------------------------------------------------------------

#---------------------------------------------------------ip list part-----------------------------------------------------------------------
if args.list_ip_ping:
    if ".txt" in args.list_ip_ping:
        thread_lock = threading.Lock()
        web_file = args.list_ip_ping

        # start time of scan
        startTime = time.time()

        with open("test_ip_list.txt") as ip_opened:
            lines = ip_opened.readlines()
            ip_list=[]
            for i in lines:
                ip_list.append(i.replace("\n",""))
        loop=len(ip_list)
        all_hosts=[]
        for i in range (0,loop-1):
            ip_net = ipaddress.ip_network(ip_list[i])
            all_hosts=all_hosts + list(ip_net.hosts())

        info = subprocess.STARTUPINFO()
        info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        info.wShowWindow = subprocess.SW_HIDE
        print ('Sweeping Websites/domains in the file with ICMP: ')

        q = Queue()

        for x in range(100):
            t = threading.Thread(target = ip_list_threader)
            t.daemon = True
            t.start()

        for worker in range(len(all_hosts)):
            q.put(worker)

        q.join()

        runtime = float("%0.2f" % (time.time() - startTime))
        print("Run Time: ", runtime, "seconds")
    
    
    else:
        print("Enter a valid text file name with the list ending with .txt (example.txt) ")

#----------------------------------------------------end of ip list part------------------------------------------------------------------

#----------------------------------------------------------web ping part------------------------------------------------------------------
if args.web_ping:
    thread_lock = threading.Lock()
    web_file = args.web_ping
    startTime = time.time()

    info = subprocess.STARTUPINFO()
    info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    info.wShowWindow = subprocess.SW_HIDE
    print ('Sweeping Websites/domains in the file with ICMP: ')
    q = Queue()

    for x in range(100):
        t = threading.Thread(target = web_threader)
        t.daemon = True
        t.start()

    for worker in range(0,1):
        q.put(worker)

    q.join()
    runtime = float("%0.2f" % (time.time() - startTime))
    print("Run Time: ", runtime, "seconds")

#------------------------------------------------------end of web ping part-----------------------------------------------------------------

#-----------------------------------------------------start of web list part----------------------------------------------------------------
if args.list_web_ping:
    if ".txt" in args.list_web_ping:
        thread_lock = threading.Lock()#makes it wait until the task is done

        # Prompt the user to input a file of websites
        web_file = args.list_web_ping

        # start time of scan
        startTime = time.time()

        with open(web_file) as web_opened:
            lines = web_opened.readlines()
            web_list=[]
            for i in lines:
                web_list.append(i.replace("\n",""))


        # Get all hosts on that network
        #all_hosts = list(ip_net.hosts())#list of all hosts available in the ip range

        # Configure subprocess to hide the console window
        info = subprocess.STARTUPINFO()
        info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        info.wShowWindow = subprocess.SW_HIDE#SW_HIDE will Hides the window. Another window will be activated.

        # signal that our scanning has started
        print ('Sweeping Websites/domains in the file with ICMP: ')

        q = Queue()

        # up to 100 threads, daemon for cleaner shutdown   
        # just spawns the threads and makes them daemon mode
        for x in range(100):
            t = threading.Thread(target = web_list_threader)
            t.daemon = True
            t.start()

        # loops over the last octet in our network object
        # passing it to q.put (entering it into queue)
        for worker in range(len(web_list)):
            q.put(worker)

        # queue management   
        q.join()

        # ok, give us a final time report
        runtime = float("%0.2f" % (time.time() - startTime))
        print("Run Time: ", runtime, "seconds")
    else:
        print("Enter a valid text file name with the list ending with .txt (example.txt) ")
#----------------------------------------------------------end of web list part--------------------------------------------------------------
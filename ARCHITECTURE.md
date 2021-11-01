

Spec
--------------------------
* discord controller
    * create event
    * allow users to opt in 
        * emotes/command
    * allow users to set notification settings?
    * allow attenders of the event to ping/notify other attenders 
* event controller
    * runs on loop
    * communicates db calls to user
    * notify users of upcoming events
* db for persistance/event backup in case bot goes down
* twilio/notification api
--------------------------

classes
--------------------------

* event
    * date-time
    * location
    * participants
* Person
    * discord ID
    * contact info
    * events participating in (?)
    * method to send msg on disc/txt (?)
--------------------------

# Postmortem: [June 1999, Ebay is down for 22 hours]

**Outage start time:** Thursday, June 11 1999 at 11:23 PM Eastern Standard Time
**Outage end time:** Friday, June 11 1999 at 9:23 PM Eastern Standard Time

  ***What was the impact? What were users experiencing?***
100% of the users that were actively bidding that day were met with an HTTP 505 Error code for almost 24 hours. Since the company launched a website redesign, several shutdowns were experienced for the last six days. As a result of the outage, the event drove the stock to close down $16.81 to $165.88 on the Nasdaq on Friday.
    

  

***What was the root cause?***
Technicians traced the main cause of the outage to a problem with the Sun Solaris operating system, which overwrote files and corrupted the Oracle database. The database, Version 7.3.2.2, recognized a data block in an incorrect format, and that caused the main hardware–a Sun E10000 server–to crash.
    

## Timeline

***When was the issue detected? How was the issue detected?***
A full database diagnosis concluded on Thursday, June 11 1999 at 2:00 AM Eastern Standard Time which helped to conclude the issue to the technicians.
    
***Actions taken (what parts of the system were investigated, what were the assumption on the root cause of the issue)***
Ebay stated it was due to a failure from Sun Microsystems that caused its service to go down, only to later find out that the system had not been upgraded with the latest available Solaris patch for months. Had the support team had the patches up to date, the outage wouldn’t have taken place.
    
***Which team/individuals was the incident escalated to?***
Ebay’s in-house server technical staff and Sun Microsystems Tech support
    


***How was the incident resolved?***
The latest Solaris patch was downloaded and installed. Also, a second server was deployed shortly after as a E10000 server running Oracle for backup.
    

  

## Root cause and resolution

***What was causing the issue?***
The incompatibility of not having the Solaris Operating system with the latest patch ended overwriting files incorrectly and corrupting the Oracle database.
    

***How the issue was fixed?***
After replacing all corrupted system files and then applied the latest Solaris patch, the servers were able to do a full reboot back to normal operating conditions
    

## Corrective and preventative measures

***What are the things that can be improved/fixed?***
    

-   Implementing a new policy for unscheduled outages of two hours or more, all auctions that would have ended during or one hour after the outage will be extended for 24 hours and will automatically refund all fees for those auctions
-   Mirror all the disks on the system
-   Put the database on hot standby mode and break the mirror to create a copy of the disks on the backup system that can't be contaminated in a crash.

---
title: RSVP Operates Only on Windows 2000
description: The RSVP Service will continue to run on hosts, but only as a conduit between applications and traffic control components.
ms.assetid: '7fd20179-8f88-4aa8-adf8-2ca6600f28d3'
---

# RSVP Operates Only on Windows 2000

> [!Note]  
> RSVP signaling is not supported on except on Windows 2000.

 

The RSVP Service will continue to run on hosts, but only as a conduit between applications and traffic control components. The impacts on QOS development for Windows versions later than Windows 2000 are enumerated in the following list:

-   Windows Sockets QOS semantics are fully operational and unchanged, but RSVP message exchange is not generated from any QOS function calls. As soon QOS settings and parameters are passed, application state is equivalent to RSVP signaling completing successfully. Outgoing packets are marked according to the service level specified in the requesting [**QOS**](qos.md) structure.
-   Parameters such as *Application-ID* and *Sub-Application-ID* are no longer useful; there is no signaling to carry them.
-   Notifications specific to QOS are no longer posted. For example, SIO\_GET\_QOS will never complete. Asynchronous SIO\_SET\_QOS will complete after the traffic control functionality has been completed, just as it does in Windows 2000. Applications that wait for QOS notifications will not receive them, and must be modified to operate properly.
-   IP\_TOS is deprecated as a way to mark packets by QOS. Developers should continue to use QOS to mark packets.
-   Received RSVP messages are absorbed; Windows does not respond with ICMP error messages.
-   Admission Control Service (ACS) is implemented only on Windows 2000; subsequent versions of Windows do not implement or support ACS.
-   The Traffic Control API is unaffected.

 

 





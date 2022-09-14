---
description: In Microsoft Telephony, telephony service providers execute in a separate process from telephony applications.
ms.assetid: ccc40d3c-6764-469a-baac-fa625d664ea7
title: The Telephony Service Provider UI DLL Interface
ms.topic: article
ms.date: 05/31/2018
---

# The Telephony Service Provider UI DLL Interface

In Microsoft Telephony, telephony service providers execute in a separate process from telephony applications. Service providers communicate with TAPISRV through the Telephony service provider interface (TSPI) and execute in its process; applications interface to TAPI, which are loaded in the application context.

The components of TAPI use various interprocess communications mechanisms to convey function requests and messages between applications and service providers. The applications and the service providers may be executing not only in separate processes, but on completely separate systems. Service providers therefore cannot display dialog boxes in the process or even on the computer on which they are executing; UI must be invoked from within the application context, on the computer on which the application is executing.

This section defines the mechanism by which service provider UI functions are loaded and invoked within the application context. A mechanism is also defined by which service providers can spontaneously open dialog boxes in the application context when they would not otherwise be expected by the application. An example of this latter case would be the **Talk/Hangup** dialog box that is displayed by a data modem service provider when the modem is being used as a dialer for interactive voice calls, and the user must be told to pick up the phone and inform the service provider when to place the modem onhook.

 

 




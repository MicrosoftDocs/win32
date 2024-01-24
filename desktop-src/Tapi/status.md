---
description: Most of the get and set operations deal with one component of information only. The phoneGetStatus function returns complete status information about a phone device to an application.
ms.assetid: 'ca38396c-6f97-4c1c-99fb-2bd64c74c626'
title: Status (Telephony API)
ms.topic: article
ms.date: 05/31/2018
---

# Status (Telephony API)

Most of the get and set operations deal with one component of information only. The [**phoneGetStatus**](/windows/desktop/api/Tapi/nf-tapi-phonegetstatus) function returns complete status information about a phone device to an application.

As mentioned earlier, whenever a status item changes on the phone device, a [**PHONE\_STATE**](phone-state.md) message is sent to the application function. This message's parameters include a handle to the phone device and an indication of the status item that changed.

An application can use [**phoneSetStatusMessages**](/windows/desktop/api/Tapi/nf-tapi-phonesetstatusmessages) to select the specific status changes for which it wants to be notified. Correspondingly, [**phoneGetStatusMessages**](/windows/desktop/api/Tapi/nf-tapi-phonegetstatusmessages) returns the status changes for which the application wants to be notified.

 

 




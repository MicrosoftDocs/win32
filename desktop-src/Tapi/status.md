---
Description: Most of the get and set operations deal with one component of information only. The phoneGetStatus function returns complete status information about a phone device to an application.
ms.assetid: 8d747aa5-05cc-4426-9d46-24bce6b4af26
title: Status
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Status

Most of the get and set operations deal with one component of information only. The [**phoneGetStatus**](/windows/desktop/api/Tapi/nf-tapi-phonegetstatus) function returns complete status information about a phone device to an application.

As mentioned earlier, whenever a status item changes on the phone device, a [**PHONE\_STATE**](phone-state.md) message is sent to the application function. This message's parameters include a handle to the phone device and an indication of the status item that changed.

An application can use [**phoneSetStatusMessages**](/windows/desktop/api/Tapi/nf-tapi-phonesetstatusmessages) to select the specific status changes for which it wants to be notified. Correspondingly, [**phoneGetStatusMessages**](/windows/desktop/api/Tapi/nf-tapi-phonegetstatusmessages) returns the status changes for which the application wants to be notified.

 

 




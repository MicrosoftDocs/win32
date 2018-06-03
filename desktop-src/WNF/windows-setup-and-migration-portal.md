---
Description: .
ms.assetid: 1f36cc9e-a903-4270-a6cb-8f042c5e41eb
title: Out-of-box experience (OOBE) APIs for setup state and notification
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Out-of-box experience (OOBE) APIs for setup state and notification

## Purpose

This section documents the functions (and function callback prototypes) used to detect and possibly repair an application after a setup or migration has occurred. These functions can also be used to suspend operations during the volatile setup or migration experience.

## In this section



| Topic                                                                                   | Description                                                                                                                                       |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| [**RegisterWaitUntilOOBECompleted**](/previous-versions/windows/desktop/api/Oobenotification/nf-oobenotification-registerwaituntiloobecompleted)<br/>     | Registers a callback to be called once OOBE (Windows Welcome) has been completed.<br/>                                                      |
| [*OOBE\_COMPLETED\_CALLBACK*](/previous-versions/windows/desktop/api/Oobenotification/nc-oobenotification-oobe_completed_callback)<br/>                   | Application-defined callback function used with the [**RegisterWaitUntilOOBECompleted**](/previous-versions/windows/desktop/api/Oobenotification/nf-oobenotification-registerwaituntiloobecompleted) function.<br/> |
| [**OOBEComplete**](/previous-versions/windows/desktop/api/Oobenotification/nf-oobenotification-oobecomplete)<br/>                                         | Determines whether OOBE (Windows Welcome) has been completed.<br/>                                                                          |
| [**UnregisterWaitUntilOOBECompleted**](/previous-versions/windows/desktop/api/Oobenotification/nf-oobenotification-unregisterwaituntiloobecompleted)<br/> | Unregisters the callback previously registered via [**RegisterWaitUntilOOBECompleted**](/previous-versions/windows/desktop/api/Oobenotification/nf-oobenotification-registerwaituntiloobecompleted).<br/>           |



 

 

 





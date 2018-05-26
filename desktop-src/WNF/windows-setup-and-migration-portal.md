---
Description: .
ms.assetid: 1f36cc9e-a903-4270-a6cb-8f042c5e41eb
title: Out-of-box experience (OOBE) APIs for setup state and notification
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Out-of-box experience (OOBE) APIs for setup state and notification

## Purpose

This section documents the functions (and function callback prototypes) used to detect and possibly repair an application after a setup or migration has occurred. These functions can also be used to suspend operations during the volatile setup or migration experience.

## In this section



| Topic                                                                                   | Description                                                                                                                                       |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| [**RegisterWaitUntilOOBECompleted**](/windows/previous-versions/Oobenotification/nf-oobenotification-registerwaituntiloobecompleted?branch=master)<br/>     | Registers a callback to be called once OOBE (Windows Welcome) has been completed.<br/>                                                      |
| [*OOBE\_COMPLETED\_CALLBACK*](/windows/previous-versions/Oobenotification/nc-oobenotification-oobe_completed_callback?branch=master)<br/>                   | Application-defined callback function used with the [**RegisterWaitUntilOOBECompleted**](/windows/previous-versions/Oobenotification/nf-oobenotification-registerwaituntiloobecompleted?branch=master) function.<br/> |
| [**OOBEComplete**](/windows/previous-versions/Oobenotification/nf-oobenotification-oobecomplete?branch=master)<br/>                                         | Determines whether OOBE (Windows Welcome) has been completed.<br/>                                                                          |
| [**UnregisterWaitUntilOOBECompleted**](/windows/previous-versions/Oobenotification/nf-oobenotification-unregisterwaituntiloobecompleted?branch=master)<br/> | Unregisters the callback previously registered via [**RegisterWaitUntilOOBECompleted**](/windows/previous-versions/Oobenotification/nf-oobenotification-registerwaituntiloobecompleted?branch=master).<br/>           |



 

 

 





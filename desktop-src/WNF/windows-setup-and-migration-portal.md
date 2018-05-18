---
Description: '.'
ms.assetid: '1f36cc9e-a903-4270-a6cb-8f042c5e41eb'
title: 'Out-of-box experience (OOBE) APIs for setup state and notification'
---

# Out-of-box experience (OOBE) APIs for setup state and notification

## Purpose

This section documents the functions (and function callback prototypes) used to detect and possibly repair an application after a setup or migration has occurred. These functions can also be used to suspend operations during the volatile setup or migration experience.

## In this section



| Topic                                                                                   | Description                                                                                                                                       |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| [**RegisterWaitUntilOOBECompleted**](registerwaituntiloobecompleted.md)<br/>     | Registers a callback to be called once OOBE (Windows Welcome) has been completed.<br/>                                                      |
| [*OOBE\_COMPLETED\_CALLBACK*](oobe-completed-callback.md)<br/>                   | Application-defined callback function used with the [**RegisterWaitUntilOOBECompleted**](registerwaituntiloobecompleted.md) function.<br/> |
| [**OOBEComplete**](oobecomplete.md)<br/>                                         | Determines whether OOBE (Windows Welcome) has been completed.<br/>                                                                          |
| [**UnregisterWaitUntilOOBECompleted**](unregisterwaituntiloobecompleted.md)<br/> | Unregisters the callback previously registered via [**RegisterWaitUntilOOBECompleted**](registerwaituntiloobecompleted.md).<br/>           |



 

 

 





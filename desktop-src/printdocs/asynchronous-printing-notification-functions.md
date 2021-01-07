---
description: The following interfaces are used in asynchronous communication between applications and components that are hosted by the print spooler, such as printer drivers and port monitors.
ms.assetid: 7e98e63f-616c-4cd1-a8aa-482d27529b8c
title: Asynchronous Printing Notification Functions
ms.topic: article
ms.date: 05/31/2018
---

# Asynchronous Printing Notification Functions

The following interfaces are used in asynchronous communication between applications and components that are hosted by the print spooler, such as printer drivers and port monitors.

## In this section



| Function                                                                                        | Description                                                                                                                                                                                              |
|-------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreatePrintAsyncNotifyChannel**](/windows/desktop/api/prnasnot/nf-prnasnot-createprintasyncnotifychannel)<br/>               | Creates a communication channel between a Print Spooler-hosted printing component, such as a print driver or port monitor, and an application that receives notifications from the component.<br/> |
| [**RegisterForPrintAsyncNotifications**](/windows/desktop/api/prnasnot/nf-prnasnot-registerforprintasyncnotifications)<br/>     | Enables an application to register for notifications from Print Spooler-hosted printing components such as printer drivers, print processors, and port monitors.<br/>                              |
| [**UnRegisterForPrintAsyncNotifications**](/windows/desktop/api/prnasnot/nf-prnasnot-unregisterforprintasyncnotifications)<br/> | Enables an application that has registered to receive notifications from Print Spooler-hosted printing components to unregister.<br/>                                                              |



 

 

 





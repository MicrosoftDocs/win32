---
description: The following interfaces are used in asynchronous communication between applications and components that are hosted by the print spooler, such as printer drivers and port monitors.
ms.assetid: e96c957f-3972-4afc-9d76-a4725b8688f8
title: Asynchronous Printing Notification Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Asynchronous Printing Notification Interfaces

The following interfaces are used in asynchronous communication between applications and components that are hosted by the print spooler, such as printer drivers and port monitors.

## In this section



| Interface                                                                     | Description                                                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IPrintAsyncNotifyCallback**](/windows/desktop/api/prnasnot/nn-prnasnot-iprintasyncnotifycallback)<br/>     | Creates and manages a communication channel used by applications and components that are hosted by the print spooler.<br/>                                                                                                                              |
| [**IPrintAsyncNotifyChannel**](/windows/desktop/api/prnasnot/nn-prnasnot-iprintasyncnotifychannel)<br/>       | Represents a communication channel that components that are hosted by the print spooler use to send notifications to applications. If the channel is bidirectional, applications can use the same channel to send responses back to the component.<br/> |
| [**IPrintAsyncNotifyDataObject**](/windows/desktop/api/prnasnot/nn-prnasnot-iprintasyncnotifydataobject)<br/> | Encapsulates the data sent in a notification channel. <br/>                                                                                                                                                                                             |



 

 

 





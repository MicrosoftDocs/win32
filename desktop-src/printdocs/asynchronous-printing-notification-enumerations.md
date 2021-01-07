---
description: The following enumerations are used in asynchronous communication between applications and components that are hosted by the print spooler, such as printer drivers and port monitors.
ms.assetid: 732a552b-caf9-45da-9a9e-a325c4f6341b
title: Asynchronous Printing Notification Enumerations
ms.topic: article
ms.date: 05/31/2018
---

# Asynchronous Printing Notification Enumerations

The following enumerations are used in asynchronous communication between applications and components that are hosted by the print spooler, such as printer drivers and port monitors.

## In this section



| Enumeration                                                                               | Description                                                                                                                                                                                                    |
|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PrintAsyncNotifyConversationStyle**](/windows/desktop/api/prnasnot/ne-prnasnot-printasyncnotifyconversationstyle)<br/> | Specifies whether communication is bidirectional or unidirectional between applications and Print Spooler-hosted components such as printer drivers, print processors, and port monitors.<br/>           |
| [**PrintAsyncNotifyError**](/windows/desktop/api/prnasnot/ne-prnasnot-printasyncnotifyerror)<br/>                         | Specifies the error code portion of the **HRESULT** returned after an asynchronous notification failure.<br/>                                                                                            |
| [**PrintAsyncNotifyUserFilter**](/windows/desktop/api/prnasnot/ne-prnasnot-printasyncnotifyuserfilter)<br/>               | Specifies whether notifications will go only to listening applications that are associated with the same user as the Print Spooler-hosted sender, or go to a broader set of listening applications.<br/> |



 

 

 





---
Description: Let you track cards within readers. These routines typically use the SCARD\_READERSTATE structure within an array.
ms.assetid: b26b26bf-85ff-435f-a679-7529f19b1c1b
title: Smart Card Tracking Functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Smart Card Tracking Functions

The following functions let you track cards within readers. These routines typically use the [**SCARD\_READERSTATE**](/windows/desktop/api/Winscard/ns-winscard-scard_readerstatea) structure within an array.



| Topic                                                | Description                                                                                                                            |
|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| [**SCardLocateCards**](/windows/desktop/api/Winscard/nf-winscard-scardlocatecardsa)         | Search for a card whose [*ATR string*](security.a_gly#-security-atr-string-gly) matches a supplied card name. |
| [**SCardGetStatusChange**](/windows/desktop/api/Winscard/nf-winscard-scardgetstatuschangea) | Block execution until the current availability of cards changes.                                                                       |
| [**SCardCancel**](/windows/desktop/api/Winscard/nf-winscard-scardcancel)                   | Terminate outstanding actions.                                                                                                         |



 

 

 




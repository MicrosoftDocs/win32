---
Description: Let you track cards within readers. These routines typically use the SCARD\_READERSTATE structure within an array.
ms.assetid: b26b26bf-85ff-435f-a679-7529f19b1c1b
title: Smart Card Tracking Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Smart Card Tracking Functions

The following functions let you track cards within readers. These routines typically use the [**SCARD\_READERSTATE**](/windows/win32/Winscard/ns-winscard-scard_readerstatea?branch=master) structure within an array.



| Topic                                                | Description                                                                                                                            |
|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| [**SCardLocateCards**](/windows/win32/Winscard/nf-winscard-scardlocatecardsa?branch=master)         | Search for a card whose [*ATR string*](security.a_gly#-security-atr-string-gly) matches a supplied card name. |
| [**SCardGetStatusChange**](/windows/win32/Winscard/nf-winscard-scardgetstatuschangea?branch=master) | Block execution until the current availability of cards changes.                                                                       |
| [**SCardCancel**](/windows/win32/Winscard/nf-winscard-scardcancel?branch=master)                   | Terminate outstanding actions.                                                                                                         |



 

 

 




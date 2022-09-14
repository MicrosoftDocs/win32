---
title: Messages Communicated through User Interfaces
description: This topic lists messages that a directory service can send from a user interface.
ms.assetid: c81a3c44-c01d-4029-8a7d-6e0911d4f5ab
ms.tgt_platform: multiple
keywords:
- Messages Communicated through User Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Messages Communicated through User Interfaces

This topic lists messages that a directory service can send from a user interface.

## Common Query Page Messages

The following messages are sent to a directory service query form extension page in the [**CQPageProc**](/windows/desktop/api/Cmnquery/nc-cmnquery-lpcqpageproc) callback function:

-   [**CQPM\_CLEARFORM**](cqpm-clearform.md)
-   [**CQPM\_ENABLE**](cqpm-enable.md)
-   [**CQPM\_GETPARAMETERS**](cqpm-getparameters.md)
-   [**CQPM\_HANDLERSPECIFIC**](cqpm-handlerspecific.md)
-   [**CQPM\_HELP**](cqpm-help.md)
-   [**CQPM\_INITIALIZE**](cqpm-initialize.md)
-   [**CQPM\_PERSIST**](cqpm-persist.md)
-   [**CQPM\_RELEASE**](cqpm-release.md)
-   [**CQPM\_SETDEFAULTPARAMETERS**](cqpm-setdefaultparameters.md)

## Miscellaneous Messages

The following table lists messages that a directory service can send.



| Message                  | Value                     | Description                                                                                                                                                                                                                                   |
|--------------------------|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DSPROP\_ATTRCHANGED\_MSG | "DsPropAttrChanged"       | A message sent for synchronizing property pages and the directory service administration tools, declared in Dsclient.h.                                                                                                                       |
| DSQPM\_GETCLASSLIST      | CQPM\_HANDLERSPECIFIC+0   | A page message sent to the form pages for retrieving a list of classes for query, used by the field selector and property well to build its list of display classes. wParam = flags and lParam = LPLPDSQUERYCLASSLIST, declared in Dsquery.h. |
| DSQPM\_HELPTOPICS        | (CQPM\_HANDLERSPECIFIC+1) | A page message sent to the form pages for handling the "Help Topics" request. wParam = 0, lParam = hWndParent, declared in Dsquery.h.                                                                                                         |



 

 

 





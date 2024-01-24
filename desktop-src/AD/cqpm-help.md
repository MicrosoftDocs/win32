---
title: CQPM_HELP message (Cmnquery.h)
description: Sent to the CQPageProc callback function of a query form extension page to allow the page extension to display context-sensitive help for the page.
ms.assetid: 07f5bd24-bca2-4d87-8e1e-acce552a3bf2
ms.tgt_platform: multiple
keywords:
- CQPM_HELP message Active Directory
topic_type:
- apiref
api_name:
- CQPM_HELP
api_location:
- Cmnquery.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CQPM\_HELP message

The **CQPM\_HELP** message is sent to the [**CQPageProc**](/windows/desktop/api/Cmnquery/nc-cmnquery-lpcqpageproc) callback function of a query form extension page to allow the page extension to display context-sensitive help for the page. If possible, the query page extension should display context-sensitive help in response to this event.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Not used.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**HELPINFO**](/windows/win32/api/winuser/ns-winuser-helpinfo) structure that contains additional data about the menu item, control, dialog box, or window for which context-sensitive help is requested.

</dd> </dl>

## Return value

The return value for this message is ignored.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>Cmnquery.h</dt> </dl> |



## See also

<dl> <dt>

[**CQPageProc**](/windows/desktop/api/Cmnquery/nc-cmnquery-lpcqpageproc)
</dt> <dt>

[**HELPINFO**](/windows/win32/api/winuser/ns-winuser-helpinfo)
</dt> </dl>

 


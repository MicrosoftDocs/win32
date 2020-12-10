---
title: RB_IDTOINDEX message (Commctrl.h)
description: Converts a band identifier to a band index in a rebar control.
ms.assetid: 'vs|controls|~\controls\rebar\messages\rb_idtoindex.htm'
keywords:
- RB_IDTOINDEX message Windows Controls
topic_type:
- apiref
api_name:
- RB_IDTOINDEX
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# RB\_IDTOINDEX message

Converts a band identifier to a band index in a rebar control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The application-defined identifier of the band in question. This is the value that was passed in the **wID** member of the [**REBARBANDINFO**](/windows/win32/api/commctrl/ns-commctrl-rebarbandinfoa) structure when the band was inserted.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the zero-based band index if successful, or -1 otherwise. If duplicate band identifiers exist, the first one is returned.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 






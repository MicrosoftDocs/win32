---
title: RB_GETBANDINFO message (Commctrl.h)
description: Retrieves information about a specified band in a rebar control.
ms.assetid: c2a76c91-7d44-4278-823d-bd263520e7a8
keywords:
- RB_GETBANDINFO message Windows Controls
topic_type:
- apiref
api_name:
- RB_GETBANDINFO
- RB_GETBANDINFOA
- RB_GETBANDINFOW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# RB\_GETBANDINFO message

Retrieves information about a specified band in a rebar control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Zero-based index of the band for which the information will be retrieved.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**REBARBANDINFO**](/windows/win32/api/commctrl/ns-commctrl-rebarbandinfoa) structure that will receive the requested band information. Before sending this message, you must set the **cbSize** member of this structure to the size of the **REBARBANDINFO** structure and set the **fMask** member to the items you want to retrieve. Additionally, you must set the **cch** member of the **REBARBANDINFO** structure to the size of the **lpText** buffer when RBBIM\_TEXT is specified.

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **RB\_GETBANDINFOW** (Unicode) and **RB\_GETBANDINFOA** (ANSI)<br/>             |



## See also

<dl> <dt>

[**RB\_SETBANDINFO**](rb-setbandinfo.md)
</dt> </dl>

 

 






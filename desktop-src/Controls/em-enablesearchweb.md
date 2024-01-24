---
title: EM_ENABLESEARCHWEB message (CommCtrl.h)
description: Enables or disables the "Search the web" feature and context menu entry.
ms.assetid: 9393f03e-0719-458b-8122-616df738c417
keywords:
- EM_ENABLESEARCHWEB message Windows Controls
topic_type:
- apiref
api_name:
- EM_ENABLESEARCHWEB
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_ENABLESEARCHWEB message

Enables or disables the "Search the web" feature and context menu entry.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A value of **TRUE** indicates the "Search the web" feature is enabled, and a value of **FALSE** indicates it is disabled.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

This message does not return a value.

## Remarks

If you disable "Search the web" using this message, the [**EM\_SEARCHWEB**](em-searchweb.md) message has no effect.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, 1809 \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2019 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>CommCtrl.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**EM\_SEARCHWEB**](em-searchweb.md)
</dt> </dl>

 

 






---
title: STM_SETICON message (Winuser.h)
description: An application sends the STM\_SETICON message to associate an icon with an icon control.
ms.assetid: 105b0667-8e23-47ed-9fb1-0792a22d7100
keywords:
- STM_SETICON message Windows Controls
topic_type:
- apiref
api_name:
- STM_SETICON
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# STM\_SETICON message

An application sends the **STM\_SETICON** message to associate an icon with an icon control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Handle to the icon to associate with the icon control.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

The return value is a handle to the icon previously associated with the icon control, or zero if an error occurs.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**STM\_GETICON**](stm-geticon.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**LoadIcon**](/windows/desktop/api/winuser/nf-winuser-loadicona)
</dt> </dl>

 


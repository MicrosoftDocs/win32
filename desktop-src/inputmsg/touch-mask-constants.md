---
title: Touch Mask
description: Values that can appear in the touchMask field of the POINTER_TOUCH_INFO structure.
ms.assetid: 23AD50C8-C769-48D6-9F27-DB2755C03D5C
topic_type:
- apiref
api_name:
- TOUCH_MASK_NONE
- TOUCH_MASK_CONTACTAREA
- TOUCH_MASK_ORIENTATION
- TOUCH_MASK_PRESSURE
api_location:
- winuser.h
api_type:
- HeaderDef
ms.topic: article
ms.date: 02/03/2020
---

# Touch Mask

Values that can appear in the **touchMask** field of the [**POINTER_TOUCH_INFO**](/windows/win32/api/winuser/ns-winuser-pointer_touch_info) structure.

<dl> <dt>

<span id="TOUCH_MASK_NONE_"></span><span id="touch_mask_none_"></span>**TOUCH_MASK_NONE** 
</dt> <dd> <dl> <dt>

0x00000000
</dt> <dt>



Default. None of the optional fields are valid.


</dt> </dl> </dd> <dt>

<span id="TOUCH_MASK_CONTACTAREA"></span><span id="touch_mask_contactarea"></span>**TOUCH_MASK_CONTACTAREA**
</dt> <dd> <dl> <dt>

0x00000001
</dt> <dt>



**rcContact** of the [**POINTER_TOUCH_INFO**](/windows/win32/api/winuser/ns-winuser-pointer_touch_info) structure is valid.


</dt> </dl> </dd> <dt>

<span id="TOUCH_MASK_ORIENTATION"></span><span id="touch_mask_orientation"></span>**TOUCH_MASK_ORIENTATION**
</dt> <dd> <dl> <dt>

0x00000002
</dt> <dt>



**orientation** of the [**POINTER_TOUCH_INFO**](/windows/win32/api/winuser/ns-winuser-pointer_touch_info) structure is valid.


</dt> </dl> </dd> <dt>

<span id="TOUCH_MASK_PRESSURE"></span><span id="touch_mask_pressure"></span>**TOUCH_MASK_PRESSURE**
</dt> <dd> <dl> <dt>

0x00000004
</dt> <dt>



**pressure** of the [**POINTER_TOUCH_INFO**](/windows/win32/api/winuser/ns-winuser-pointer_touch_info) structure is valid.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Winuser.h</dt> </dl> |



## See also

<dl> <dt>

[Constants](constants.md)
</dt> <dt>

[**POINTER_INFO**](/windows/win32/api/winuser/ns-winuser-pointer_info)
</dt> </dl>

 

 






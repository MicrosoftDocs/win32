---
title: Touch Mask
description: Values that can appear in the touchMask field of the POINTER\_TOUCH\_INFO structure.
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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Touch Mask

Values that can appear in the **touchMask** field of the [**POINTER\_TOUCH\_INFO**](/windows/win32/Winuser/ns-rimext-tagpointer_touch_info?branch=master) structure.

<dl> <dt>

<span id="TOUCH_MASK_NONE_"></span><span id="touch_mask_none_"></span>**TOUCH\_MASK\_NONE** 
</dt> <dd> <dl> <dt>

0x00000000
</dt> <dt>



Default. None of the optional fields are valid.


</dt> </dl> </dd> <dt>

<span id="TOUCH_MASK_CONTACTAREA"></span><span id="touch_mask_contactarea"></span>**TOUCH\_MASK\_CONTACTAREA**
</dt> <dd> <dl> <dt>

0x00000001
</dt> <dt>



**rcContact** of the [**POINTER\_TOUCH\_INFO**](/windows/win32/Winuser/ns-rimext-tagpointer_touch_info?branch=master) structure is valid.


</dt> </dl> </dd> <dt>

<span id="TOUCH_MASK_ORIENTATION"></span><span id="touch_mask_orientation"></span>**TOUCH\_MASK\_ORIENTATION**
</dt> <dd> <dl> <dt>

0x00000002
</dt> <dt>



**orientation** of the [**POINTER\_TOUCH\_INFO**](/windows/win32/Winuser/ns-rimext-tagpointer_touch_info?branch=master) structure is valid.


</dt> </dl> </dd> <dt>

<span id="TOUCH_MASK_PRESSURE"></span><span id="touch_mask_pressure"></span>**TOUCH\_MASK\_PRESSURE**
</dt> <dd> <dl> <dt>

0x00000004
</dt> <dt>



**pressure** of the [**POINTER\_TOUCH\_INFO**](/windows/win32/Winuser/ns-rimext-tagpointer_touch_info?branch=master) structure is valid.


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Winuser.h</dt> </dl> |



## See also

<dl> <dt>

[Constants](constants.md)
</dt> <dt>

[**POINTER\_INFO**](/windows/win32/Winuser/ns-rimext-tagpointer_info?branch=master)
</dt> </dl>

 

 






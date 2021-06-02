---
title: TBM_GETBUDDY message (Commctrl.h)
description: Retrieves the handle to a trackbar control buddy window at a given location. The specified location is relative to the control's orientation (horizontal or vertical).
ms.assetid: 69e4e467-150d-4505-b1c2-2ed9dd83f1a6
keywords:
- TBM_GETBUDDY message Windows Controls
topic_type:
- apiref
api_name:
- TBM_GETBUDDY
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TBM\_GETBUDDY message

Retrieves the handle to a trackbar control buddy window at a given location. The specified location is relative to the control's orientation (horizontal or vertical).

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Value indicating which buddy window handle will be retrieved, by relative location. This value can be one of the following:



| Value                                                                                                                                    | Meaning                                                                                                                                                                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TRUE"></span><span id="true"></span><dl> <dt>****TRUE****</dt> </dl>    | Retrieves the handle to the buddy to the left of the trackbar. If the trackbar control uses the [**TBS\_VERT**](trackbar-control-styles.md) style, the message will retrieve the buddy above the trackbar.<br/>  |
| <span id="FALSE"></span><span id="false"></span><dl> <dt>****FALSE****</dt> </dl> | Retrieves the handle to the buddy to the right of the trackbar. If the trackbar control uses the [**TBS\_VERT**](trackbar-control-styles.md) style, the message will retrieve the buddy below the trackbar.<br/> |



 

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the handle to the buddy window at the location specified by *wParam*, or **NULL** if no buddy window exists at that location.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 






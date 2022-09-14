---
title: TBM_SETTHUMBLENGTH message (Commctrl.h)
description: Sets the length of the slider in a trackbar. This message is ignored if the trackbar does not have the TBS\_FIXEDLENGTH style.
ms.assetid: 027fe341-a60a-4dbe-a48a-5ddaadef0b4a
keywords:
- TBM_SETTHUMBLENGTH message Windows Controls
topic_type:
- apiref
api_name:
- TBM_SETTHUMBLENGTH
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TBM\_SETTHUMBLENGTH message

Sets the length of the slider in a trackbar. This message is ignored if the trackbar does not have the [**TBS\_FIXEDLENGTH**](trackbar-control-styles.md) style.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Length, in pixels, of the slider.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

No return value.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TBM\_GETTHUMBLENGTH**](tbm-getthumblength.md)
</dt> </dl>

 

 






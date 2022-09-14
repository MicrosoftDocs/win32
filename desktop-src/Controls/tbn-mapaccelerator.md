---
title: TBN_MAPACCELERATOR notification code (Commctrl.h)
description: Requests the index of the button in the toolbar corresponding to the specified accelerator character. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 16d16560-62ef-4457-bf8c-bc6dddb520d7
keywords:
- TBN_MAPACCELERATOR notification code Windows Controls
topic_type:
- apiref
api_name:
- TBN_MAPACCELERATOR
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TBN\_MAPACCELERATOR notification code

Requests the index of the button in the toolbar corresponding to the specified accelerator character. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TBN_MAPACCELERATOR

    lpnmtb = (NMCHAR*) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMCHAR**](/windows/win32/api/commctrl/ns-commctrl-nmchar) structure that contains the accelerator key character and that receives the index of the corresponding button. The **dwItemNext** field is -1 if the accelerator does not correspond to a command.

</dd> </dl>

## Return value

TRUE if **NMCHAR.dwItemNext** is set to a value.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 






---
description: Notifies you that a change has taken place.
title: SMC_SHCHANGENOTIFY message (Shobjidl.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 8232f170-0dab-475a-ace0-67c04f01c777
api_name: 
 - SMC_SHCHANGENOTIFY
api_type: 
 - HeaderDef
api_location: 
 - Shobjidl.h
topic_type: 
 - APIRef
 - kbSyntax

---

# SMC\_SHCHANGENOTIFY message

Notifies you that a change has taken place.


```C++
SMC_SHCHANGENOTIFY
    lParam = (LPARAM) (PSMCSCHANGENOTIFYSTRUCT) psmc
            
```



## Parameters

<dl> <dt>

*psmc* 
</dt> <dd>

A pointer to an [**SMCSHCHANGENOTIFYSTRUCT**](/windows/win32/api/shobjidl_core/ns-shobjidl_core-smcshchangenotifystruct) structure with information on the change.

</dd> </dl>

## Return value

Return S\_OK.

## Remarks

This notification is received by the [**IShellMenuCallback::CallbackSM**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellmenucallback-callbacksm) method.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Shobjidl.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Shobjidl.idl</dt> </dl> |



 

 





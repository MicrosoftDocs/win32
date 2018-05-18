---
Description: 'Requests whether it is acceptable to drop a data object on the item specified by the accompanying SMDATA structure.'
ms.assetid: '777bbc7e-6b0f-4627-9d92-4aa8209082ca'
title: 'SMC\_SFDDRESTRICTED message'
---

# SMC\_SFDDRESTRICTED message

Requests whether it is acceptable to drop a data object on the item specified by the accompanying [**SMDATA**](smdata.md) structure.


```C++
SMC_SFDDRESTRICTED 
    wParam = (WPARAM) (void **) pDropTarget
            
```



## Parameters

<dl> <dt>

*pDropTarget* 
</dt> <dd>

The address of a void pointer that receives a pointer to your [**IDropTarget**](com.idroptarget) interface. Set this value to **NULL** if you do not want to accept the data object.

</dd> </dl>

## Return value

Return S\_OK.

## Remarks

This notification is received by the [**IShellMenuCallback::CallbackSM**](ishellmenucallback-callbacksm.md) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Shobjidl.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Shobjidl.idl</dt> </dl> |



 

 





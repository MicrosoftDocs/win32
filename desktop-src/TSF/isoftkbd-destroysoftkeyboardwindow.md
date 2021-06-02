---
title: ISoftKbd DestroySoftKeyboardWindow method (Softkbdc.h)
description: The ISoftKbd DestroySoftKeyboardWindow method destroys a soft keyboard window.
ms.assetid: 44030934-7b4a-46c1-95ea-709fc9004e43
keywords:
- DestroySoftKeyboardWindow method Text Services Framework
- DestroySoftKeyboardWindow method Text Services Framework , ISoftKbd interface
- ISoftKbd interface Text Services Framework , DestroySoftKeyboardWindow method
topic_type:
- apiref
api_name:
- ISoftKbd.DestroySoftKeyboardWindow
api_location:
- Softkbd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ISoftKbd::DestroySoftKeyboardWindow method

The **ISoftKbd::DestroySoftKeyboardWindow** method destroys a soft keyboard window.

## Syntax


```C++
HRESULT DestroySoftKeyboardWindow();
```



## Parameters

This method has no parameters.

## Return value

This method can return one of these values.



| Value                                                                                | Description                           |
|--------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method was successful.<br/> |



 

## Remarks

This method removes a soft keyboard window previously created with a call to [**ISoftKbd::CreateSoftKeyboardWindow**](isoftkbd-createsoftkeyboardwindow.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                        |
| Header<br/>                   | <dl> <dt>Softkbdc.h</dt> </dl>  |
| IDL<br/>                      | <dl> <dt>Softkbd.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Softkbd.dll</dt> </dl> |



## See also

<dl> <dt>

[**ISoftKbd**](isoftkbd.md)
</dt> <dt>

[**ISoftKbd::CreateSoftKeyboardWindow**](isoftkbd-createsoftkeyboardwindow.md)
</dt> </dl>

 

 






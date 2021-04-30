---
title: ISoftKbd SetSoftKeyboardTypeMode method (Softkbdc.h)
description: The ISoftKbd SetSoftKeyboardTypeMode method sets the type mode for a soft keyboard.
ms.assetid: 0b5b5056-59b3-41c7-bc43-70b5c3cd51c2
keywords:
- SetSoftKeyboardTypeMode method Text Services Framework
- SetSoftKeyboardTypeMode method Text Services Framework , ISoftKbd interface
- ISoftKbd interface Text Services Framework , SetSoftKeyboardTypeMode method
topic_type:
- apiref
api_name:
- ISoftKbd.SetSoftKeyboardTypeMode
api_location:
- Softkbd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ISoftKbd::SetSoftKeyboardTypeMode method

The **ISoftKbd::SetSoftKeyboardTypeMode** method sets the type mode for a soft keyboard.

## Syntax


```C++
HRESULT SetSoftKeyboardTypeMode(
  [in] TYPEMODE TypeMode
);
```



## Parameters

<dl> <dt>

*TypeMode* \[in\]
</dt> <dd>

The type mode. Possible values are defined for the [**TYPEMODE**](typemode.md) enumeration.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                        | Description                                     |
|----------------------------------------------------------------------------------------------|-------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The method was successful.<br/>           |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The *TypeMode* parameter is invalid.<br/> |



 

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

[**ISoftKbd::GetSoftKeyboardTypeMode**](isoftkbd-getsoftkeyboardtypemode.md)
</dt> <dt>

[**TYPEMODE**](typemode.md)
</dt> </dl>

 

 






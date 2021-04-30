---
title: ISoftKbd GetSoftKeyboardTypeMode method (Softkbdc.h)
description: The ISoftKbd GetSoftKeyboardTypeMode method retrieves the type mode for a soft keyboard.
ms.assetid: 77294652-b82e-4b69-bb55-5ebebc3c97c7
keywords:
- GetSoftKeyboardTypeMode method Text Services Framework
- GetSoftKeyboardTypeMode method Text Services Framework , ISoftKbd interface
- ISoftKbd interface Text Services Framework , GetSoftKeyboardTypeMode method
topic_type:
- apiref
api_name:
- ISoftKbd.GetSoftKeyboardTypeMode
api_location:
- Softkbd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ISoftKbd::GetSoftKeyboardTypeMode method

The **ISoftKbd::GetSoftKeyboardTypeMode** method retrieves the type mode for a soft keyboard.

## Syntax


```C++
HRESULT GetSoftKeyboardTypeMode(
  [out] TYPEMODE *lpTypeMode
);
```



## Parameters

<dl> <dt>

*lpTypeMode* \[out\]
</dt> <dd>

Pointer to a buffer in which this method retrieves the type mode. Possible values are defined for the [**TYPEMODE**](typemode.md) enumeration.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                        | Description                                       |
|----------------------------------------------------------------------------------------------|---------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The method was successful.<br/>             |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The *lpTypeMode* parameter is invalid.<br/> |



 

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

[**ISoftKbd::SetSoftKeyboardTypeMode**](isoftkbd-setsoftkeyboardtypemode.md)
</dt> <dt>

[**TYPEMODE**](typemode.md)
</dt> </dl>

 

 






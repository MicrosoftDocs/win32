---
title: ISoftKbd SelectSoftKeyboard method (Softkbdc.h)
description: The ISoftKbd SelectSoftKeyboard method selects the specified soft keyboard.
ms.assetid: 7e85d346-3741-457d-aadd-11d3a6710e85
keywords:
- SelectSoftKeyboard method Text Services Framework
- SelectSoftKeyboard method Text Services Framework , ISoftKbd interface
- ISoftKbd interface Text Services Framework , SelectSoftKeyboard method
topic_type:
- apiref
api_name:
- ISoftKbd.SelectSoftKeyboard
api_location:
- Softkbd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ISoftKbd::SelectSoftKeyboard method

The **ISoftKbd::SelectSoftKeyboard** method selects the specified soft keyboard.

## Syntax


```C++
HRESULT SelectSoftKeyboard(
  [in] DWORD dwKeyboardId
);
```



## Parameters

<dl> <dt>

*dwKeyboardId* \[in\]
</dt> <dd>

Identifier of the soft keyboard to select.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                        | Description                                         |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The method was successful.<br/>               |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The *dwKeyboardId* parameter is invalid.<br/> |



 

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
</dt> </dl>

 

 






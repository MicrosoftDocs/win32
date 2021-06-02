---
title: ISoftKbd EnumSoftKeyboard method (Softkbdc.h)
description: The ISoftKbd EnumSoftKeyboard method enumerates the possible soft keyboards that support the specified language.
ms.assetid: c71f99e5-c4c2-4b09-a58f-d3f4348d0c5d
keywords:
- EnumSoftKeyboard method Text Services Framework
- EnumSoftKeyboard method Text Services Framework , ISoftKbd interface
- ISoftKbd interface Text Services Framework , EnumSoftKeyboard method
topic_type:
- apiref
api_name:
- ISoftKbd.EnumSoftKeyboard
api_location:
- Softkbd.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ISoftKbd::EnumSoftKeyboard method

The **ISoftKbd::EnumSoftKeyboard** method enumerates the possible soft keyboards that support the specified language.

## Syntax


```C++
HRESULT EnumSoftKeyboard(
  [in]  LANGID langid,
  [out] DWORD  *lpdwKeyboard
);
```



## Parameters

<dl> <dt>

*langid* \[in\]
</dt> <dd>

Language identifier.

</dd> <dt>

*lpdwKeyboard* \[out\]
</dt> <dd>

Pointer to a buffer in which this method retrieves identifiers of the available soft keyboards.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                        | Description                                   |
|----------------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The method was successful.<br/>         |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The *langid* parameter is invalid.<br/> |



 

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

 

 






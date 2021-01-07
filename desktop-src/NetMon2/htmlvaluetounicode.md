---
description: The HTMLValueToUnicode function converts an HTML CP\_UTF8 string to a Unicode string.
ms.assetid: d175476e-9c84-48b8-9c89-00255b7cb638
title: HTMLValueToUnicode function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- HTMLValueToUnicode
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# HTMLValueToUnicode function

The **HTMLValueToUnicode** function converts an HTML CP\_UTF8 string to a Unicode string.

## Syntax


```C++
WCHAR* HTMLValueToUnicode(
  _Inout_ const char *pValue
);
```



## Parameters

<dl> <dt>

*pValue* \[in, out\]
</dt> <dd>

On input, pointer to the HTML string supplied by the MCSVC.

On output, pointer to the converted Unicode string.

</dd> </dl>

## Return value

The function returns the Unicode equivalent of the string.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 





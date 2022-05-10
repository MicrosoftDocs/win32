---
description: This ApiSetQueryApiSetPresence function is intended for internal use only and should not be used in your code.
ms.assetid: 836A7515-8C22-4032-9E99-F89B32C21685
title: ApiSetQueryApiSetPresence function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ApiSetQueryApiSetPresence
api_type: 
- DllExport
api_location: 
- api-ms-win-core-apiquery-l1-1-0.dll
- ntdll.dll
---

# ApiSetQueryApiSetPresence function

This API is intended for internal use only and should not be used in your code.

## Syntax


```C++
BOOL WINAPI ApiSetQueryApiSetPresence(
  _In_  PCUNICODE_STRING Namespace,
  _Out_ PBOOLEAN         Present
);
```



## Parameters

<dl> <dt>

*Namespace* \[in\]
</dt> <dd></dd> <dt>

*Present* \[out\]
</dt> <dd></dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                                                                                                                           |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                                                                                                                                  |
| Header<br/>                   | <dl> <dt>N/A</dt> </dl>                                                                                                                 |
| Library<br/>                  | <dl> <dt>Api-ms-win-core-apiquery-l1.lib; </dt> <dt>Api-ms-win-core-apiquery-l1-1-0.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Api-ms-win-core-apiquery-l1-1-0.dll</dt> </dl>                                                                                        |



 

 





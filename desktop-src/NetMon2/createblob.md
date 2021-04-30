---
description: The CreateBlob function creates an empty BLOB.
ms.assetid: fa31855b-af85-4ab5-b434-e54111731d8f
title: CreateBlob function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CreateBlob
api_type: 
- DllExport
api_location: 
- Npptools.dll
---

# CreateBlob function

The **CreateBlob** function creates an empty BLOB.

## Syntax


```C++
DWORD CreateBlob(
  _Out_ HBLOB *phBlob
);
```



## Parameters

<dl> <dt>

*phBlob* \[out\]
</dt> <dd>

Pointer to the variable where the pointer to the new BLOB is returned.

</dd> </dl>

## Return value

If the function is successful, the return value is NMERR\_SUCCESS.

If the function is unsuccessful, the return value is a NMERR value that describes the error.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Npptools.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Npptools.dll</dt> </dl> |



## See also

<dl> <dt>

[DestroyBlob](destroyblob.md)
</dt> </dl>

 

 





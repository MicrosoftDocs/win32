---
description: The DuplicateBlob function copies a specific BLOB.
ms.assetid: d2478f53-328c-4799-890c-7849ce1f22e9
title: DuplicateBlob function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DuplicateBlob
api_type: 
- DllExport
api_location: 
- Npptools.dll
---

# DuplicateBlob function

The **DuplicateBlob** function copies a specific BLOB.

## Syntax


```C++
DWORD DuplicateBlob(
  _In_  HBLOB hSrcBlob,
  _Out_ HBLOB *hBlobThatWillBeCreated
);
```



## Parameters

<dl> <dt>

*hSrcBlob* \[in\]
</dt> <dd>

Handle to the BLOB that is copied.

</dd> <dt>

*hBlobThatWillBeCreated* \[out\]
</dt> <dd>

Handle to the duplicate BLOB.

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

[CreateBlob](createblob.md)
</dt> <dt>

[DestroyBlob](destroyblob.md)
</dt> </dl>

 

 





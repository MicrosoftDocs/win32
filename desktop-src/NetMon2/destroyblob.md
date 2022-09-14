---
description: The DestroyBlob function frees all memory associated with the BLOB and then destroys the BLOB.
ms.assetid: 46cde0b7-1b59-426e-b19b-3c73af3d461a
title: DestroyBlob function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DestroyBlob
api_type: 
- DllExport
api_location: 
- Npptools.dll
---

# DestroyBlob function

The **DestroyBlob** function frees all memory associated with the BLOB and then destroys the BLOB.

## Syntax


```C++
DWORD DestroyBlob(
  _In_ HBLOB hBlob
);
```



## Parameters

<dl> <dt>

*hBlob* \[in\]
</dt> <dd>

Handle to the to the BLOB that is destroyed.

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
</dt> </dl>

 

 





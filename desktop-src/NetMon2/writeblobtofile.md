---
description: The WriteBlobToFile function writes a BLOB to a file.
ms.assetid: 0793dced-82c2-4553-90b2-acf594c6749e
title: WriteBlobToFile function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WriteBlobToFile
api_type: 
- DllExport
api_location: 
- Npptools.dll
---

# WriteBlobToFile function

The **WriteBlobToFile** function writes a BLOB to a file.

## Syntax


```C++
DWORD WriteBlobToFile(
  _In_       HBLOB hBlob,
  _In_ const char  *pFileName
);
```



## Parameters

<dl> <dt>

*hBlob* \[in\]
</dt> <dd>

Handle to the BLOB.

</dd> <dt>

*pFileName* \[in\]
</dt> <dd>

Pointer to the name of the file, in which the BLOB is saved.

</dd> </dl>

## Return value

If the function is successful, the return value is NMERR\_SUCCESS.

If the function is unsuccessful, the return value is a NMERR value that indicates the error.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Npptools.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Npptools.dll</dt> </dl> |



 

 





---
description: The ReadBlobFromFile function reads a BLOB in a file.
ms.assetid: c3d4a892-160b-48e9-8881-0ada3ebd49b0
title: ReadBlobFromFile function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ReadBlobFromFile
api_type: 
- DllExport
api_location: 
- Npptools.dll
---

# ReadBlobFromFile function

The **ReadBlobFromFile** function reads a BLOB in a file.

## Syntax


```C++
DWORD ReadBlobFromFile(
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

Pointer to the name of the file that contains the BLOB.

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



 

 





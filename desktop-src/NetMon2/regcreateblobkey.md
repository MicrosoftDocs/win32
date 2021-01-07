---
description: The RegCreateBlobKey function stores a BLOB at the given registry key.
ms.assetid: 14f3763e-aa04-4d51-b388-81ebf0d3952c
title: RegCreateBlobKey function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RegCreateBlobKey
api_type: 
- DllExport
api_location: 
- Npptools.dll
---

# RegCreateBlobKey function

The **RegCreateBlobKey** function stores a BLOB at the given registry key.

## Syntax


```C++
DWORD RegCreateBlobKey(
  _Out_       HKEY  hkey,
  _In_  const char  *szBlobName,
  _In_        HBLOB hBlob
);
```



## Parameters

<dl> <dt>

*hkey* \[out\]
</dt> <dd>

Handle to the registry key where the BLOB will be stored.

</dd> <dt>

*szBlobName* \[in\]
</dt> <dd>

Name (application defined) that represents the BLOB in the registry.

</dd> <dt>

*hBlob* \[in\]
</dt> <dd>

Handle to the BLOB that is saved.

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



## See also

<dl> <dt>

[RegOpenBlobKey](regopenblobkey.md)
</dt> </dl>

 

 





---
description: The RegOpenBlobKey function retrieves a BLOB stored at the given registry key.
ms.assetid: f6b16c07-c705-47f1-a21c-6155368551c7
title: RegOpenBlobKey function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RegOpenBlobKey
api_type: 
- DllExport
api_location: 
- Npptools.dll
---

# RegOpenBlobKey function

The **RegOpenBlobKey** function retrieves a BLOB stored at the given registry key.

## Syntax


```C++
DWORD RegOpenBlobKey(
  _In_        HKEY  hkey,
  _In_  const char  *szBlobName,
  _Out_       HBLOB *phBlob
);
```



## Parameters

<dl> <dt>

*hkey* \[in\]
</dt> <dd>

Handle to the registry key that contains the BLOB.

</dd> <dt>

*szBlobName* \[in\]
</dt> <dd>

Name that identifies the given BLOB in the registry.

</dd> <dt>

*phBlob* \[out\]
</dt> <dd>

Pointer to the BLOB that is retrieved.

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

[RegCreateBlobKey](regcreateblobkey.md)
</dt> </dl>

 

 





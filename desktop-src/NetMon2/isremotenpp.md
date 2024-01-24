---
description: The IsRemoteNPP function indicates whether the given BLOB specifies a remote NPP.
ms.assetid: 66ee0a9a-3199-479f-baec-da6ae6b46c65
title: IsRemoteNPP function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IsRemoteNPP
api_type: 
- DllExport
api_location: 
- Npptools.dll
---

# IsRemoteNPP function

The **IsRemoteNPP** function indicates whether the given BLOB specifies a remote NPP.

## Syntax


```C++
BOOL IsRemoteNPP(
  _In_ HBLOB hBlob
);
```



## Parameters

<dl> <dt>

*hBlob* \[in\]
</dt> <dd>

Handle to a BLOB.

</dd> </dl>

## Return value

If the function is successful, the return value is **TRUE**.

## Remarks

Use this function to test whether a remote category exists.

Make certain that the remote and local computer names are different.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Npptools.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Npptools.dll</dt> </dl> |



 

 





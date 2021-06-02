---
description: The MergeBlob function copies all of the entries from the source BLOB into a destination BLOB.
ms.assetid: 7521ce0c-fd02-4002-bdae-0d74a2e4a646
title: MergeBlob function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MergeBlob
api_type: 
- DllExport
api_location: 
- Npptools.dll
---

# MergeBlob function

The **MergeBlob** function copies all of the entries from the source BLOB into a destination BLOB.

## Syntax


```C++
DWORD MergeBlob(
  _Inout_ HBLOB hDstBlob,
  _In_    HBLOB hSrcBlob
);
```



## Parameters

<dl> <dt>

*hDstBlob* \[in, out\]
</dt> <dd>

Handle to the destination BLOB. On input, this BLOB contains its original information. On output, this BLOB contains its original information plus all the information of the source BLOB.

</dd> <dt>

*hSrcBlob* \[in\]
</dt> <dd>

Handle to the source BLOB.

</dd> </dl>

## Return value

If the function is successful, the return value is NMERR\_SUCCESS.

If the function is unsuccessful, the return value is a NMERR value that indicates the error.

## Remarks

Entries common to source and destination files will be overwritten with data from the source BLOB.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Npptools.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Npptools.dll</dt> </dl> |



 

 





---
description: The PdhVbGetCounterPathFromList function copies the counter path referenced by the Index parameter from a counter path list created by the user from the most recent call to the PdhVbCreateCounterPathList function.
ms.assetid: e77a022d-42f2-4c48-acb7-36cb013730dd
title: PdhVbGetCounterPathFromList function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PdhVbGetCounterPathFromList
api_type: 
- DllExport
api_location: 
- Pdh.dll
---

# PdhVbGetCounterPathFromList function

The **PdhVbGetCounterPathFromList** function copies the counter path referenced by the *Index* parameter from a counter path list created by the user from the most recent call to the [**PdhVbCreateCounterPathList**](pdhvbcreatecounterpathlist.md) function.

> [!IMPORTANT]
> The function that this topic describes may be altered or unavailable in the future. Instead, Microsoft recommends that you use the functions described in [Performance Counters Functions](performance-counters-functions.md).

Function PdhVbGetCounterPathFromList( \_ ByVal Index As Long, \_ ByVal Buffer As String, \_ ByVal BufferLength As Long \_ ) As Long

## Parameters

<dl> <dt>

*Index* 
</dt> <dd>

Index of the counter path to retrieve. This must be a value that is greater than or equal to 1, and less than or equal to the value returned by the [**PdhVbCreateCounterPathList**](pdhvbcreatecounterpathlist.md) function.

</dd> <dt>

*Buffer* 
</dt> <dd>

Dimensioned and initialized string that will receive the counter path that corresponds to the value of the Index parameter.

</dd> <dt>

*BufferLength* 
</dt> <dd>

Maximum number of characters that will fit in the string referenced by Buffer.

</dd> </dl>

## Return value

The function returns the number of characters copied to Buffer.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Library<br/>                  | <dl> <dt>Pdh.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Pdh.dll</dt> </dl> |



## See also

<dl> <dt>

[**PdhVbCreateCounterPathList**](pdhvbcreatecounterpathlist.md)
</dt> <dt>

[**PdhVbGetCounterPathElements**](pdhvbgetcounterpathelements.md)
</dt> <dt>

[**PdhVbGetOneCounterPath**](pdhvbgetonecounterpath.md)
</dt> </dl>

 

 





---
description: Retrieves the attribute data for the specified file.
ms.assetid: 899b4af3-8185-4ce5-8e81-05ec3a446e42
title: SdbGetFileAttributes function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SdbGetFileAttributes
api_type: 
- DllExport
api_location: 
- Apphelp.dll
---

# SdbGetFileAttributes function

Retrieves the attribute data for the specified file.

## Syntax


```C++
BOOL WINAPI SdbGetFileAttributes(
  _In_  LPCTSTR   lpwszFileName,
  _Out_ PATTRINFO *ppAttrInfo,
  _Out_ LPDWORD   lpdwAttrCount
);
```



## Parameters

<dl> <dt>

*lpwszFileName* \[in\]
</dt> <dd>

The path to the file.

</dd> <dt>

*ppAttrInfo* \[out\]
</dt> <dd>

An array of [**ATTRINFO**](attrinfo.md) structures that contain the attribute data.

</dd> <dt>

*lpdwAttrCount* \[out\]
</dt> <dd>

The number of attributes.

</dd> </dl>

## Return value

The function returns **TRUE** on success or **FALSE** on failure.

## Remarks

When you have finished with the data, free it using the [**SdbFreeFileAttributes**](sdbfreefileattributes.md) function.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Apphelp.dll</dt> </dl> |



## See also

<dl> <dt>

[**SdbFormatAttribute**](sdbformatattribute.md)
</dt> <dt>

[**SdbFreeFileAttributes**](sdbfreefileattributes.md)
</dt> </dl>

 

 





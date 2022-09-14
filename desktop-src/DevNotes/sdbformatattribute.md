---
description: Converts the specified attribute data to XML format.
ms.assetid: 7a75726d-f1ec-4137-89c1-eccb4a78fc22
title: SdbFormatAttribute function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SdbFormatAttribute
api_type: 
- DllExport
api_location: 
- Apphelp.dll
---

# SdbFormatAttribute function

Converts the specified attribute data to XML format.

## Syntax


```C++
BOOL WINAPI SdbFormatAttribute(
  _In_  PATTRINFO pAttrInfo,
  _Out_ LPTSTR    pchBuffer,
  _In_  DWORD     dwBufferSize
);
```



## Parameters

<dl> <dt>

*pAttrInfo* \[in\]
</dt> <dd>

An [**ATTRINFO**](attrinfo.md) structure.

</dd> <dt>

*pchBuffer* \[out\]
</dt> <dd>

The output buffer.

</dd> <dt>

*dwBufferSize* \[in\]
</dt> <dd>

The size of the *pchBuffer* buffer, in characters.

</dd> </dl>

## Return value

The function returns **TRUE** on success or **FALSE** if the buffer is too small or the attribute is not found.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Apphelp.dll</dt> </dl> |



## See also

<dl> <dt>

[**SdbGetFileAttributes**](sdbgetfileattributes.md)
</dt> </dl>

 

 





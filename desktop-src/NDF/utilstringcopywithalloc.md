---
title: UtilStringCopyWithAlloc function (Ndattributils.h)
description: Allocates and copies a source string.
ms.assetid: e1400ae1-0edd-4b59-af03-3da1b9d7073b
keywords:
- UtilStringCopyWithAlloc function NDF
topic_type:
- apiref
api_name:
- UtilStringCopyWithAlloc
api_location:
- ndattributils.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# UtilStringCopyWithAlloc function

The **UtilStringCopyWithAlloc** function allocates and copies a source string.

## Syntax


```C++
HRESULT UtilStringCopyWithAlloc(
  _Out_ LPWSTR  *Buffer,
  _In_  UINT    BufferMax,
  _In_  LPCWSTR Source
);
```



## Parameters

<dl> <dt>

*Buffer* \[out\]
</dt> <dd>

Type: **LPWSTR\***

The location where the pointer to the allocated memory is stored. When no longer needed, it must be released with [**CoTaskMemFree**](/windows/desktop/api/combaseapi/nf-combaseapi-cotaskmemfree). This buffer is always null-terminated.

</dd> <dt>

*BufferMax* \[in\]
</dt> <dd>

Type: **UINT**

The maximum number of characters to read from *Source*.

</dd> <dt>

*Source* \[in\]
</dt> <dd>

Type: **LPCWSTR**

The string to be copied.

</dd> </dl>

## Return value

Type: **HRESULT**

Possible return values include, but are not limited to, the following.



| Return code                                                                                  | Description                                                        |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The operation succeeded.<br/>                                |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | One or more parameters has not been provided correctly.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Ndattributils.h</dt> </dl> |



## See also

<dl> <dt>

[**CoTaskMemFree**](/windows/desktop/api/combaseapi/nf-combaseapi-cotaskmemfree)
</dt> <dt>

[**UtilAssembleStringsWithAlloc**](utilassemblestringswithalloc.md)
</dt> <dt>

[**UtilLoadStringWithAlloc**](utilloadstringwithalloc.md)
</dt> </dl>

 


---
title: UtilLoadStringWithAlloc function (Ndattributils.h)
description: Allocates and loads a string out of the resource table.
ms.assetid: 34bf0b93-2bec-49c3-9441-c83686c4abdb
keywords:
- UtilLoadStringWithAlloc function NDF
topic_type:
- apiref
api_name:
- UtilLoadStringWithAlloc
api_location:
- ndattributils.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# UtilLoadStringWithAlloc function

The **UtilLoadStringWithAlloc** function allocates and loads a string out of the resource table.

## Syntax


```C++
HRESULT UtilLoadStringWithAlloc(
  _In_  UINT   uID,
  _Out_ LPWSTR *ppwzBuffer,
  _In_  UINT   cchBufferMax
);
```



## Parameters

<dl> <dt>

*uID* \[in\]
</dt> <dd>

Type: **UINT**

Identifier of of the string to be loaded.

</dd> <dt>

*ppwzBuffer* \[out\]
</dt> <dd>

Type: **LPWSTR\***

The location where the newly allocated string will be placed. The string must be freed using [**CoTaskMemFree**](/windows/desktop/api/combaseapi/nf-combaseapi-cotaskmemfree) when it is no longer needed.

</dd> <dt>

*cchBufferMax* \[in\]
</dt> <dd>

Type: **UINT**

The maximum number of characters to load from the resource table. If the resource string is longer than the number of characters specified, it is truncated and null-terminated.

> [!Note]  
> This parameter may not be set to zero.

 

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

[**UtilStringCopyWithAlloc**](utilstringcopywithalloc.md)
</dt> <dt>

[**UtilAssembleStringsWithAlloc**](utilassemblestringswithalloc.md)
</dt> <dt>

[**CoTaskMemFree**](/windows/desktop/api/combaseapi/nf-combaseapi-cotaskmemfree)
</dt> </dl>

 


---
title: FreeUiInfo function (Ndattributils.h)
description: Deallocates the memory allocated internally to a UiInfo structure.
ms.assetid: 41d923fd-2fb3-406e-a5cf-f3ba475685f6
keywords:
- FreeUiInfo function NDF
topic_type:
- apiref
api_name:
- FreeUiInfo
api_location:
- ndattributils.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# FreeUiInfo function

The **FreeUiInfo** function deallocates the memory allocated internally to a [**UiInfo**](/windows/win32/api/ndattrib/ns-ndattrib-uiinfo) structure. This function calls [**CoTaskMemFree**](/windows/desktop/api/combaseapi/nf-combaseapi-cotaskmemfree) to deallocate memory.

## Syntax


```C++
VOID FreeUiInfo(
  _In_ UiInfo *pInfo
);
```



## Parameters

<dl> <dt>

*pInfo* \[in\]
</dt> <dd>

Type: **[**UiInfo**](/windows/win32/api/ndattrib/ns-ndattrib-uiinfo)\***

The structure. The allocated memory pointed to by this structure will be freed.

</dd> </dl>

## Return value

This function does not return a value.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Ndattributils.h</dt> </dl> |



## See also

<dl> <dt>

[**UiInfo**](/windows/win32/api/ndattrib/ns-ndattrib-uiinfo)
</dt> <dt>

[**CoTaskMemFree**](/windows/desktop/api/combaseapi/nf-combaseapi-cotaskmemfree)
</dt> </dl>

 


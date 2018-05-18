---
title: Issue GetCategories method
description: Returns the CategoryCollection of the Issue.
ms.assetid: '90ADE17F-0F82-4FE3-8DB1-8C6F6E828E97'
keywords: ["GetCategories method Access Execution Engine", "GetCategories method Access Execution Engine , Issue interface", "Issue interface Access Execution Engine , GetCategories method"]
topic_type:
- apiref
api_name:
- Issue.GetCategories
api_location:
- AxeCore.dll
api_type:
- COM
---

# Issue::GetCategories method

Returns the [**CategoryCollection**](categorycollection.md) of the **Issue**.

## Syntax


```C++
virtual HRESULT GetCategories(
  [out] CategoryCollection **categories
) = 0;
```



## Parameters

<dl> <dt>

*categories* \[out\]
</dt> <dd>

The **CategoryCollection**.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **Issue** objects hold data from **Iteration/Issues/Issue** elements.

The **CategoryCollection** holds data from element **Issue/Categories**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Issue**](issue-struct.md)
</dt> </dl>

 

 






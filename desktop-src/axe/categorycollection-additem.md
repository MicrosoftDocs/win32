---
title: CategoryCollection AddItem method
description: Creates and adds a category to the CategoryCollection.
ms.assetid: 'C814C47D-8F60-43C4-80A3-8D83B35E55F6'
keywords: ["AddItem method Access Execution Engine", "AddItem method Access Execution Engine , CategoryCollection interface", "CategoryCollection interface Access Execution Engine , AddItem method"]
topic_type:
- apiref
api_name:
- CategoryCollection.AddItem
api_location:
- AxeCore.dll
api_type:
- COM
---

# CategoryCollection::AddItem method

Creates and adds a category to the **CategoryCollection**.

## Syntax


```C++
virtual HRESULT AddItem(
  [in] LPCWSTR category
) = 0;
```



## Parameters

<dl> <dt>

*category* \[in\]
</dt> <dd>

The category.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

A **CategoryCollection** object holds data from element **Issue/Categories**.

A category is the value of an **Issue/Categories/Category** element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**CategoryCollection**](categorycollection.md)
</dt> </dl>

 

 






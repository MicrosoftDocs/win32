---
title: CategoryCollection GetItem method
description: Resturns a category from the CategoryCollection.
ms.assetid: '99B58148-16D0-46B9-8A5A-7B7DC6739F71'
keywords: ["GetItem method Access Execution Engine", "GetItem method Access Execution Engine , CategoryCollection interface", "CategoryCollection interface Access Execution Engine , GetItem method"]
topic_type:
- apiref
api_name:
- CategoryCollection.GetItem
api_location:
- AxeCore.dll
api_type:
- COM
---

# CategoryCollection::GetItem method

Resturns a category from the **CategoryCollection**.

## Syntax


```C++
virtual HRESULT GetItem(
  [in]  INT     index,
  [out] LPCWSTR *category
) = 0;
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

The category identifier.

</dd> <dt>

*category* \[out\]
</dt> <dd>

The category.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

*index* ranges from 0 to one less than the count of items in the collection.

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

 

 






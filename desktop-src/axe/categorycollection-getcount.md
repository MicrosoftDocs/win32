---
title: CategoryCollection GetCount method
description: Returns the count of categories in the CategoryCollection.
ms.assetid: 'A46EDAB3-3019-45FC-8F37-7F5D55063F0C'
keywords: ["GetCount method Access Execution Engine", "GetCount method Access Execution Engine , CategoryCollection interface", "CategoryCollection interface Access Execution Engine , GetCount method"]
topic_type:
- apiref
api_name:
- CategoryCollection.GetCount
api_location:
- AxeCore.dll
api_type:
- COM
---

# CategoryCollection::GetCount method

Returns the count of categories in the **CategoryCollection**.

## Syntax


```C++
virtual HRESULT GetCount(
  [out] INT *count
) const = 0;
```



## Parameters

<dl> <dt>

*count* \[out\]
</dt> <dd>

The count.

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

 

 






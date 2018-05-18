---
title: CategoryCollection Clear method
description: Deletes all categories from the CategoryCollection.
ms.assetid: '1B98A867-0CB0-4D70-AE57-818003447F5F'
keywords: ["Clear method Access Execution Engine", "Clear method Access Execution Engine , CategoryCollection interface", "CategoryCollection interface Access Execution Engine , Clear method"]
topic_type:
- apiref
api_name:
- CategoryCollection.Clear
api_location:
- AxeCore.dll
api_type:
- COM
---

# CategoryCollection::Clear method

Deletes all categories from the **CategoryCollection**.

## Syntax


```C++
virtual HRESULT Clear() = 0;
```



## Parameters

This method has no parameters.

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

 

 






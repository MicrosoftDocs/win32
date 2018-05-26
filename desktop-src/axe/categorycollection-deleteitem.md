---
title: CategoryCollection DeleteItem method
description: Deletes a category from the CategoryCollection.
ms.assetid: B7A63940-6885-4B76-870E-91EA4021B380
keywords:
- DeleteItem method Access Execution Engine
- DeleteItem method Access Execution Engine , CategoryCollection interface
- CategoryCollection interface Access Execution Engine , DeleteItem method
topic_type:
- apiref
api_name:
- CategoryCollection.DeleteItem
api_location:
- AxeCore.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CategoryCollection::DeleteItem method

Deletes a category from the **CategoryCollection**.

## Syntax


```C++
virtual HRESULT DeleteItem(
  [in] INT index
) = 0;
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

The category identifier.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

A **CategoryCollection** object holds data from element **Issue/Categories**.

A category is the value of an **Issue/Categories/Category** element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**CategoryCollection**](categorycollection.md)
</dt> </dl>

 

 






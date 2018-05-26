---
title: ParentCollection DeleteItem method
description: Deletes a parent from the ParentCollection.
ms.assetid: 271D8611-BB5D-40E6-804A-39D96C6C8638
keywords:
- DeleteItem method Access Execution Engine
- DeleteItem method Access Execution Engine , ParentCollection interface
- ParentCollection interface Access Execution Engine , DeleteItem method
topic_type:
- apiref
api_name:
- ParentCollection.DeleteItem
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

# ParentCollection::DeleteItem method

Deletes a parent from the **ParentCollection**.

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

The parent identifier.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

A **ParentCollection** holds data from a **TestCase/Parents** element.

A parent is the value of a **Parents/Parent** element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**ParentCollection**](parentcollection.md)
</dt> </dl>

 

 






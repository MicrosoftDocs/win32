---
title: ParentCollection AddItem method
description: Creates a parent and adds it to the ParentCollection.
ms.assetid: 55C1B444-290E-46AD-9EAC-4B1E2322AA7C
keywords:
- AddItem method Access Execution Engine
- AddItem method Access Execution Engine , ParentCollection interface
- ParentCollection interface Access Execution Engine , AddItem method
topic_type:
- apiref
api_name:
- ParentCollection.AddItem
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

# ParentCollection::AddItem method

Creates a parent and adds it to the **ParentCollection**.

## Syntax


```C++
virtual HRESULT AddItem(
  [in] LPCWSTR parent
) = 0;
```



## Parameters

<dl> <dt>

*parent* \[in\]
</dt> <dd>

The parent.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

A **ParentCollection** holds data from a **TestCase/Parents** element.

The parent is the value of a **Parents/Parent** element.

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

 

 






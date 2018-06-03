---
title: ParentCollection GetCount method
description: Returns the count of parents in the ParentCollection.
ms.assetid: BF7E9313-C6C2-4542-8A0B-C064189A01FD
keywords:
- GetCount method Access Execution Engine
- GetCount method Access Execution Engine , ParentCollection interface
- ParentCollection interface Access Execution Engine , GetCount method
topic_type:
- apiref
api_name:
- ParentCollection.GetCount
api_location:
- AxeCore.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ParentCollection::GetCount method

Returns the count of parents in the **ParentCollection**.

## Syntax


```C++
virtual HRESULT GetCount(
  [out] INT *count
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

 

 






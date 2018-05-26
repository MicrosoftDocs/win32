---
title: ReferenceCollection Clear method
description: Deletes all IssueReference objects from the ReferenceCollection.
ms.assetid: 38A5C0F6-DA52-4EC8-BE32-50F4033E1034
keywords:
- Clear method Access Execution Engine
- Clear method Access Execution Engine , ReferenceCollection interface
- ReferenceCollection interface Access Execution Engine , Clear method
topic_type:
- apiref
api_name:
- ReferenceCollection.Clear
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

# ReferenceCollection::Clear method

Deletes all [**IssueReference**](issuereference-struct.md) objects from the **ReferenceCollection**.

## Syntax


```C++
virtual HRESULT Clear() = 0;
```



## Parameters

This method has no parameters.

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

A **ReferenceCollection** holds data from an **Activity/References** element.

An **IssueReference** holds data from a **References/IssueReference** element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**ReferenceCollection**](referencecollection.md)
</dt> </dl>

 

 






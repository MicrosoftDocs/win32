---
title: ParentCollection Clear method
description: Deletes all parents from the ParentCollection.
ms.assetid: '76FFD3C7-09AD-4EF5-A960-8B6DDEAA61FA'
keywords: ["Clear method Access Execution Engine", "Clear method Access Execution Engine , ParentCollection interface", "ParentCollection interface Access Execution Engine , Clear method"]
topic_type:
- apiref
api_name:
- ParentCollection.Clear
api_location:
- AxeCore.dll
api_type:
- COM
---

# ParentCollection::Clear method

Deletes all parents from the **ParentCollection**.

## Syntax


```C++
virtual HRESULT Clear() = 0;
```



## Parameters

This method has no parameters.

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

A **ParentCollection** holds data from a **TestCase/Parents** element.

A parent is the value of a **Parents/Parent** element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**ParentCollection**](parentcollection.md)
</dt> </dl>

 

 






---
title: IssueCollection Clear method
description: Deletes all Issue objects from the IssueCollection.
ms.assetid: D7278046-CC4D-4683-9E25-451F79D0CA56
keywords:
- Clear method Access Execution Engine
- Clear method Access Execution Engine , IssueCollection interface
- IssueCollection interface Access Execution Engine , Clear method
topic_type:
- apiref
api_name:
- IssueCollection.Clear
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

# IssueCollection::Clear method

Deletes all [**Issue**](issue-struct.md) objects from the **IssueCollection**.

## Syntax


```C++
virtual HRESULT Clear() = 0;
```



## Parameters

This method has no parameters.

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The **IssueCollection** object holds information from the **Iteration/Issues** element.

The **Issue** objects hold data from **Issues/Issue** elements.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**IssueCollection**](issuecollection.md)
</dt> </dl>

 

 






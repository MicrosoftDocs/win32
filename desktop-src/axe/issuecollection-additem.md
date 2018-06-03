---
title: IssueCollection AddItem method
description: Creates and adds an Issue to the IssueCollection.
ms.assetid: 0BAABD15-974E-4A05-87CC-B6F6F200DD19
keywords:
- AddItem method Access Execution Engine
- AddItem method Access Execution Engine , IssueCollection interface
- IssueCollection interface Access Execution Engine , AddItem method
topic_type:
- apiref
api_name:
- IssueCollection.AddItem
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

# IssueCollection::AddItem method

Creates and adds an [**Issue**](issue-struct.md) to the **IssueCollection**.

## Syntax


```C++
virtual HRESULT AddItem(
  [out] Issue **issue
) = 0;
```



## Parameters

<dl> <dt>

*issue* \[out\]
</dt> <dd>

The **Issue** that this method creates.

</dd> </dl>

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

 

 






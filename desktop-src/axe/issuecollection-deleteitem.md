---
title: IssueCollection DeleteItem method
description: Deletes an Issue from the IssueCollection.
ms.assetid: 3D51EDBC-DBDC-4892-82A7-33865F46A8AB
keywords:
- DeleteItem method Access Execution Engine
- DeleteItem method Access Execution Engine , IssueCollection interface
- IssueCollection interface Access Execution Engine , DeleteItem method
topic_type:
- apiref
api_name:
- IssueCollection.DeleteItem
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

# IssueCollection::DeleteItem method

Deletes an [**Issue**](issue-struct.md) from the **IssueCollection**.

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

The issue identifier.

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

 

 






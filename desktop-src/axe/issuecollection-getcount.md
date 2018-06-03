---
title: IssueCollection GetCount method
description: Returns the count of Issue objects in the IssueCollection.
ms.assetid: 7343B3F3-0866-424A-9406-00A6DAF535C8
keywords:
- GetCount method Access Execution Engine
- GetCount method Access Execution Engine , IssueCollection interface
- IssueCollection interface Access Execution Engine , GetCount method
topic_type:
- apiref
api_name:
- IssueCollection.GetCount
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

# IssueCollection::GetCount method

Returns the count of [**Issue**](issue-struct.md) objects in the **IssueCollection**.

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

 

 






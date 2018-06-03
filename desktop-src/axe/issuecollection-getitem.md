---
title: IssueCollection GetItem method
description: Returns an Issue of the IssueCollection.
ms.assetid: E9893B47-5257-4B78-AFB7-8160878402A0
keywords:
- GetItem method Access Execution Engine
- GetItem method Access Execution Engine , IssueCollection interface
- IssueCollection interface Access Execution Engine , GetItem method
topic_type:
- apiref
api_name:
- IssueCollection.GetItem
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

# IssueCollection::GetItem method

Returns an [**Issue**](issue-struct.md) of the **IssueCollection**.

## Syntax


```C++
virtual HRESULT GetItem(
  [in]  INT   index,
  [out] Issue **issue
) = 0;
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

The issue identifier.

</dd> <dt>

*issue* \[out\]
</dt> <dd>

The **Issue**.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

*index* ranges from 0 to one less than the count of items in the collection.

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

 

 






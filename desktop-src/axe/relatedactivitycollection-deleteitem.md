---
title: RelatedActivityCollection DeleteItem method
description: Deletes an ActivityReference from the RelatedActivityCollection.
ms.assetid: F562F2B9-A157-475A-AB60-763845FD8514
keywords:
- DeleteItem method Access Execution Engine
- DeleteItem method Access Execution Engine , RelatedActivityCollection interface
- RelatedActivityCollection interface Access Execution Engine , DeleteItem method
topic_type:
- apiref
api_name:
- RelatedActivityCollection.DeleteItem
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

# RelatedActivityCollection::DeleteItem method

Deletes an [**ActivityReference**](activityreference-struct.md) from the **RelatedActivityCollection**.

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

The **ActivityReference** identifier.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

A **RelatedActivityCollection** holds data from an **Issue/Impact/RelatedActivities** element.

An **ActivityReference** holds data from a **RelatedActivities/ActivityReference** element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**RelatedActivityCollection**](relatedactivitycollection.md)
</dt> </dl>

 

 






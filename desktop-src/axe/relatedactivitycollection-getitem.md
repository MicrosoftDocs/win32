---
title: RelatedActivityCollection GetItem method
description: Returns an ActivityReference from the RelatedActivityCollection.
ms.assetid: E552BFA0-9173-4FEB-8623-EC5CB178B94E
keywords:
- GetItem method Access Execution Engine
- GetItem method Access Execution Engine , RelatedActivityCollection interface
- RelatedActivityCollection interface Access Execution Engine , GetItem method
topic_type:
- apiref
api_name:
- RelatedActivityCollection.GetItem
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

# RelatedActivityCollection::GetItem method

Returns an [**ActivityReference**](activityreference-struct.md) from the **RelatedActivityCollection**.

## Syntax


```C++
virtual HRESULT GetItem(
  [in]  INT               index,
  [out] ActivityReference **activityReference
) = 0;
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

The **ActivityReference** identifier.

</dd> <dt>

*activityReference* \[out\]
</dt> <dd>

The **ActivityReference**.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

*index* ranges from 0 to one less than the count of items in the collection.

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

 

 






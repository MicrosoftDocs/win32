---
title: RelatedActivityCollection GetCount method
description: Returns the count of ActivityReference objects in the RelatedActivityCollection.
ms.assetid: 'DBCFF2B5-5D60-4DB9-B1D9-92B297496CD8'
keywords: ["GetCount method Access Execution Engine", "GetCount method Access Execution Engine , RelatedActivityCollection interface", "RelatedActivityCollection interface Access Execution Engine , GetCount method"]
topic_type:
- apiref
api_name:
- RelatedActivityCollection.GetCount
api_location:
- AxeCore.dll
api_type:
- COM
---

# RelatedActivityCollection::GetCount method

Returns the count of [**ActivityReference**](activityreference-struct.md) objects in the **RelatedActivityCollection**.

## Syntax


```C++
virtual HRESULT GetCount(
  [out] INT *count
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

A **RelatedActivityCollection** holds data from an **Issue/Impact/RelatedActivities** element.

An **ActivityReference** holds data from a **RelatedActivities/ActivityReference** element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**RelatedActivityCollection**](relatedactivitycollection.md)
</dt> </dl>

 

 






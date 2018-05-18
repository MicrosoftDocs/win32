---
title: RelatedActivityCollection AddItem method
description: Creates an ActivityReference and adds it to the RelatedActivityCollection.
ms.assetid: '478DA66E-684B-434A-BE73-6194019ECFE9'
keywords: ["AddItem method Access Execution Engine", "AddItem method Access Execution Engine , RelatedActivityCollection interface", "RelatedActivityCollection interface Access Execution Engine , AddItem method"]
topic_type:
- apiref
api_name:
- RelatedActivityCollection.AddItem
api_location:
- AxeCore.dll
api_type:
- COM
---

# RelatedActivityCollection::AddItem method

Creates an [**ActivityReference**](activityreference-struct.md) and adds it to the **RelatedActivityCollection**.

## Syntax


```C++
virtual HRESULT AddItem(
  [in, optional]  LPCWSTR           attributeActivityID,
  [out, optional] ActivityReference **activityReference
) = 0;
```



## Parameters

<dl> <dt>

*attributeActivityID* \[in, optional\]
</dt> <dd>

The activity ID.

</dd> <dt>

*activityReference* \[out, optional\]
</dt> <dd>

The **ActivityReference** that this method creates.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

A **RelatedActivityCollection** holds data from an **Issue/Impact/RelatedActivities** element.

An **ActivityReference** holds data from a **RelatedActivities/ActivityReference** element.

The activity ID is the value of attribute **ActivityID** of element **ActivityReference**.

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

 

 






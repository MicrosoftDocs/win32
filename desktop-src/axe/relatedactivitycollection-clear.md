---
title: RelatedActivityCollection Clear method
description: Deletes all ActivityReference objects from the RelatedActivityCollection.
ms.assetid: 0FCDBACC-A8E6-4C22-B8AF-6E4746E1E894
keywords:
- Clear method Access Execution Engine
- Clear method Access Execution Engine , RelatedActivityCollection interface
- RelatedActivityCollection interface Access Execution Engine , Clear method
topic_type:
- apiref
api_name:
- RelatedActivityCollection.Clear
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

# RelatedActivityCollection::Clear method

Deletes all [**ActivityReference**](activityreference-struct.md) objects from the **RelatedActivityCollection**.

## Syntax


```C++
virtual HRESULT Clear() = 0;
```



## Parameters

This method has no parameters.

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

 

 






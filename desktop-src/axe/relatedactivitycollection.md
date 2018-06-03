---
title: RelatedActivityCollection class
description: This interface provides containers for ActivityReference objects.
ms.assetid: F0BD7953-2BC7-4D47-B6BD-00105D12CD69
keywords:
- RelatedActivityCollection class Access Execution Engine
- RelatedActivityCollection class Access Execution Engine , described
topic_type:
- apiref
api_name:
- RelatedActivityCollection
api_location:
- AxeCore.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# RelatedActivityCollection class

This interface provides containers for [**ActivityReference**](activityreference-struct.md) objects.

## When to implement

Never. This interface is implemented by Axe and provided to the assessment.

**RelatedActivityCollection** has these types of members:

-   [Methods](#methods)

### Methods

The **RelatedActivityCollection** class has these methods.



| Method                                                                                     | Description                                                                                                                         |
|:-------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------|
| [**~RelatedActivityCollection**](relatedactivitycollection--relatedactivitycollection.md) | Destructor method.<br/>                                                                                                       |
| [**AddItem**](relatedactivitycollection-additem.md)                                       | Creates an [**ActivityReference**](activityreference-struct.md) and adds it to the **RelatedActivityCollection**.<br/>       |
| [**Clear**](relatedactivitycollection-clear.md)                                           | Deletes all [**ActivityReference**](activityreference-struct.md) objects from the **RelatedActivityCollection**.<br/>        |
| [**DeleteItem**](relatedactivitycollection-deleteitem.md)                                 | Deletes an [**ActivityReference**](activityreference-struct.md) from the **RelatedActivityCollection**.<br/>                 |
| [**GetCount**](relatedactivitycollection-getcount.md)                                     | Returns the count of [**ActivityReference**](activityreference-struct.md) objects in the **RelatedActivityCollection**.<br/> |
| [**GetItem**](relatedactivitycollection-getitem.md)                                       | Returns an [**ActivityReference**](activityreference-struct.md) from the **RelatedActivityCollection**.<br/>                 |



 

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



 

 






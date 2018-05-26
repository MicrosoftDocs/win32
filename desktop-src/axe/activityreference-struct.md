---
title: ActivityReference class
description: This interface provides access to ActivityReference objects.
ms.assetid: 77989EEF-74F0-4097-B810-779234CF4104
keywords:
- ActivityReference class Access Execution Engine
- ActivityReference class Access Execution Engine , described
topic_type:
- apiref
api_name:
- ActivityReference
api_location:
- AxeCore.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ActivityReference class

This interface provides access to **ActivityReference** objects.

## When to implement

Never. This interface is implemented by Axe and provided to the assessment.

**ActivityReference** has these types of members:

-   [Methods](#methods)

### Methods

The **ActivityReference** class has these methods.



| Method                                                                     | Description                                                      |
|:---------------------------------------------------------------------------|:-----------------------------------------------------------------|
| [**~ActivityReference**](activityreference--activityreference.md)         | Destructor method.<br/>                                    |
| [**GetAttributeActivityID**](activityreference-getattributeactivityid.md) | Returns the activity ID of the **ActivityReference**.<br/> |
| [**SetAttributeActivityID**](activityreference-setattributeactivityid.md) | Sets the activity ID of the **ActivityReference**.<br/>    |



 

## Remarks

An **ActivityReference** holds data from an **Issue/Impact/RelatedActivities/ActivityReference** element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 






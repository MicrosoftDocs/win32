---
title: ActivityCollection class
description: This interface provides containers for Activity objects.
ms.assetid: A3B6F101-B239-4724-BA01-0B503AD0B935
keywords:
- ActivityCollection class Access Execution Engine
- ActivityCollection class Access Execution Engine , described
topic_type:
- apiref
api_name:
- ActivityCollection
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

# ActivityCollection class

This interface provides containers for [**Activity**](activity-struct.md) objects.

## When to implement

Never. This interface is implemented by Axe and provided to the assessment.

**ActivityCollection** has these types of members:

-   [Methods](#methods)

### Methods

The **ActivityCollection** class has these methods.



| Method                                                                | Description                                                                                                |
|:----------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------|
| [**~ActivityCollection**](activitycollection--activitycollection.md) | Destructor method.<br/>                                                                              |
| [**AddItem**](activitycollection-additem.md)                         | Creates an [**Activity**](activity-struct.md) and adds it to the **ActivityCollection**.<br/>       |
| [**Clear**](activitycollection-clear.md)                             | Deletes all [**Activity**](activity-struct.md) objects from the **ActivityCollection**.<br/>        |
| [**DeleteItem**](activitycollection-deleteitem.md)                   | Deletes an [**Activity**](activity-struct.md) from the **ActivityCollection**.<br/>                 |
| [**GetCount**](activitycollection-getcount.md)                       | Returns the count of [**Activity**](activity-struct.md) objects in the **ActivityCollection**.<br/> |
| [**GetItem**](activitycollection-getitem.md)                         | Returns an [**Activity**](activity-struct.md) from the **ActivityCollection**.<br/>                 |



 

## Remarks

The **ActivityCollection** holds data from element **Iteration/Activities**.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 






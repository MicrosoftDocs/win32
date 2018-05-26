---
title: AffectedMetricCollection class
description: This interface provides containers for the metric references of an Issue.
ms.assetid: B2D54F99-124A-447D-B1C4-9D1EF020C553
keywords:
- AffectedMetricCollection class Access Execution Engine
- AffectedMetricCollection class Access Execution Engine , described
topic_type:
- apiref
api_name:
- AffectedMetricCollection
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

# AffectedMetricCollection class

This interface provides containers for the metric references of an [**Issue**](issue-struct.md).

## When to implement

Never. This interface is implemented by Axe and provided to the assessment.

**AffectedMetricCollection** has these types of members:

-   [Methods](#methods)

### Methods

The **AffectedMetricCollection** class has these methods.



| Method                                                                                  | Description                                                                            |
|:----------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------|
| [**~AffectedMetricCollection**](affectedmetriccollection--affectedmetriccollection.md) | Destructor method.<br/>                                                          |
| [**AddItem**](affectedmetriccollection-additem.md)                                     | Creates and adds a metric reference to the **AffectedMetricCollection**.<br/>    |
| [**Clear**](affectedmetriccollection-clear.md)                                         | Deletes all metric references from the **AffectedMetricCollection**.<br/>        |
| [**DeleteItem**](affectedmetriccollection-deleteitem.md)                               | Deletes a metric reference from the **AffectedMetricCollection**.<br/>           |
| [**GetCount**](affectedmetriccollection-getcount.md)                                   | Returns the count of metric references in the **AffectedMetricCollection**.<br/> |
| [**GetItem**](affectedmetriccollection-getitem.md)                                     | Returns a metric reference from the **AffectedMetricCollection**.<br/>           |



 

## Remarks

An **AffectedMetricCollection** object holds data from element **Issue/AffectedMetrics**.

A metric reference is the value of an **Issue/AffectedMetrics/MetricReference** element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 






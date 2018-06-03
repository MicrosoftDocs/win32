---
title: MetricValue class
description: This interface provides access to MetricValue objects.
ms.assetid: 9494BD64-802C-46DD-9387-C78FAE3ADC80
keywords:
- MetricValue class Access Execution Engine
- MetricValue class Access Execution Engine , described
topic_type:
- apiref
api_name:
- MetricValue
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

# MetricValue class

This interface provides access to **MetricValue** objects.

## When to implement

Never. This interface is implemented by Axe and provided to the assessment.

**MetricValue** has these types of members:

-   [Methods](#methods)

### Methods

The **MetricValue** class has these methods.



| Method                                                         | Description                                                      |
|:---------------------------------------------------------------|:-----------------------------------------------------------------|
| [**~MetricValue**](metricvalue--metricvalue.md)               | Destructor method.<br/>                                    |
| [**GetProgrammaticName**](metricvalue-getprogrammaticname.md) | Returns the programmatic name of the **MetricValue**.<br/> |
| [**GetValue**](metricvalue-getvalue.md)                       | Overloaded. Returns the value of the **MetricValue**.<br/> |
| [**SetProgrammaticName**](metricvalue-setprogrammaticname.md) | Sets the programmatic name of the **MetricValue**.<br/>    |
| [**SetValue**](metricvalue-setvalue.md)                       | Overloaded. Sets the value of the **MetricValue**.<br/>    |



 

## Remarks

A **MetricValue** object holds data from an **Issue/MetricValues/MetricValue**, **Iteration/MetricValues/MetricValue**, or **TestCase/MetricValues/MetricValue** element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



 

 






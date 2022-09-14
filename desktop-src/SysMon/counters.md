---
title: Counters collection (Isysmon.h)
description: Use this class to manage the collection of CounterItem objects. To retrieve this object, call SystemMonitor.Counters.
ms.assetid: 01542569-3fee-440a-8722-db377380b73c
keywords:
- Counters collection SysMon
- Counters collection SysMon , described
topic_type:
- apiref
api_name:
- Counters
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Counters collection

Use this class to manage the collection of [**CounterItem**](counteritem.md) objects.

To retrieve this object, call [**SystemMonitor.Counters**](systemmonitor-counters.md).

## Members

The **Counters** collection has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Counters** collection has these methods.



| Method                            | Description                                                                           |
|:----------------------------------|:--------------------------------------------------------------------------------------|
| [**Add**](counters-add.md)       | Adds a [**CounterItem**](counteritem.md) instance to the collection.<br/>      |
| [**Remove**](counters-remove.md) | Removes a [**CounterItem**](counteritem.md) instance from the collection.<br/> |



 

### Properties

The **Counters** collection has these properties.



| Property                                   | Description                                                                                         |
|:-------------------------------------------|:----------------------------------------------------------------------------------------------------|
| [**Count**](counters-count.md)<br/> | Retrieves the number of [**CounterItem**](counteritem.md) instances in the collection.<br/>  |
| [**Item**](counters-item.md)<br/>   | Retrieves the specified [**CounterItem**](counteritem.md) instance from the collection.<br/> |



 

## Remarks

The **Counters** object is the default property of the [**SystemMonitor**](systemmonitor.md) object.

Add to this collection those counters that you want to graph. SYSMON retrieves the counter values either from the system or from a log file depending on the [**data source**](systemmonitor-datasourcetype.md) that you specify.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Isysmon.h</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



 

 






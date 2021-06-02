---
title: CounterItem object (Isysmon.h)
description: Use this class to retrieve the path and value of a counter and to specify the color used to graph the counter. To retrieve this object, call Counters.Item.
ms.assetid: 76b69395-efd8-4321-b7ed-63daa46e2636
keywords:
- CounterItem object SysMon
- CounterItem object SysMon , described
topic_type:
- apiref
api_name:
- CounterItem
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# CounterItem object

Use this class to retrieve the path and value of a counter and to specify the color used to graph the counter.

To retrieve this object, call [**Counters.Item**](counters-item.md).

## Members

The **CounterItem** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **CounterItem** object has these methods.



| Method                                             | Description                                                                    |
|:---------------------------------------------------|:-------------------------------------------------------------------------------|
| [**GetDataAt**](counteritem-getdataat.md)         | Retrieves the counter data from a specific point in the line graph.<br/> |
| [**GetStatistics**](counteritem-getstatistics.md) | Retrieves the average, maximum, and minimum values for the counter.<br/> |
| [**GetValue**](counteritem-getvalue.md)           | Retrieves the last value of the counter.<br/>                            |



 

### Properties

The **CounterItem** object has these properties.



| Property                                                  | Description                                                                     |
|:----------------------------------------------------------|:--------------------------------------------------------------------------------|
| [**Color**](counteritem-color.md)<br/>             | Retrieves or sets the color used to graph the counter value.<br/>         |
| [**LineStyle**](counteritem-linestyle.md)<br/>     | Retrieves or sets the line style used to graph the counter value.<br/>    |
| [**Path**](counteritem-path.md)<br/>               | Retrieves the path of the counter.<br/>                                   |
| [**ScaleFactor**](counteritem-scalefactor.md)<br/> | Retrieves or sets the scale factor used to graph the counter value.<br/>  |
| [**Selected**](counteritem-selected.md)<br/>       | Retrieves or sets a value that indicates if the counter is selected.<br/> |
| [**Value**](counteritem-value.md)<br/>             | Retrieves the current value of the counter.<br/>                          |
| [**Visible**](counteritem-visible.md)<br/>         | Retrieves or sets a value that indicates if the counter is graphed.<br/>  |
| [**Width**](counteritem-width.md)<br/>             | Retrieves or sets the line width used to graph the counter value.<br/>    |



 

## Remarks

[**Value**](counteritem-value.md) is the default property of **CounterItem**.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Isysmon.h</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



## See also

<dl> <dt>

[SYSMON Classes](sysmon-classes.md)
</dt> </dl>

 

 






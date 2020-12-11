---
title: Counters.Add method
description: Adds a CounterItem instance to the collection.
ms.assetid: 9daecfe6-c2a9-48af-8b59-4f81f0325535
keywords:
- Add method SysMon
- Add method SysMon , Counters class
- Counters class SysMon , Add method
topic_type:
- apiref
api_name:
- Counters.Add
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Counters.Add method

Adds a [**CounterItem**](counteritem.md) instance to the collection.

## Syntax


```VB
Counters.Add( _
  ByVal pathname As String _
) As CounterItem
```



## Parameters

<dl> <dt>

*pathname* \[in\]
</dt> <dd>

Path to the counter. The path can include a machine name, and must include a performance object name, an object instance name if the specified performance object supports multiple instances, and a counter name. This path specification is not case-sensitive.

For details on specifying a counter path, see [Specifying a Counter Path](/windows/desktop/PerfCtrs/specifying-a-counter-path).

</dd> </dl>

## Exceptions



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Exception type</th>
<th>Condition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>System.Runtime.InteropServices.COMException</strong></td>
<td>You can receive this exception for one of the following reasons:
<ul>
<li>The specified performance object was not found on the computer. The Err.Number value is 0xC0000BB8.</li>
<li>The specified counter could not be found. The Err.Number value is 0xC0000BB9.</li>
</ul></td>
</tr>
</tbody>
</table>



 

## Remarks

If you specify a wildcard counter in the *pathname* parameter, the **Add** method creates one [**CounterItem**](counteritem.md) object for each expanded path. The **Add** method then returns a pointer to the first added **CounterItem**.

If the wildcard would result in a duplicate counter, the error is not reported and no duplicate is created. If an error condition occurs before all counters are created, the error is reported and the remaining counters are not created.

There is no limit to the number of counters that you can add; however, SYSMON will graph only the first 1,024 counters in the collection. There is no limit on the number of counters that SYSMON will display in a report.

To receive notification when a counter is added, implement the [OnCounterAdded](systemmonitor-oncounteradded.md) event.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



## See also

<dl> <dt>

[**CounterItem**](counteritem.md)
</dt> <dt>

[**Counters**](counters.md)
</dt> <dt>

[**SystemMonitor.BrowseCounters**](systemmonitor-browsecounters.md)
</dt> </dl>

 


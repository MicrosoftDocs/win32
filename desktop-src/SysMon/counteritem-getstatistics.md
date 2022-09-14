---
title: CounterItem.GetStatistics method
description: Retrieves the average, maximum, and minimum values for the counter.
ms.assetid: fb55d68b-1dbe-48b1-88c8-51f33048ec24
keywords:
- GetStatistics method SysMon
- GetStatistics method SysMon , CounterItem class
- CounterItem class SysMon , GetStatistics method
topic_type:
- apiref
api_name:
- CounterItem.GetStatistics
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# CounterItem.GetStatistics method

Retrieves the average, maximum, and minimum values for the counter.

## Syntax


```VB
CounterItem.GetStatistics( _
  ByRef max As Double, _
  ByRef min As Double, _
  ByRef average As Double, _
  ByRef status As Long _
)
```



## Parameters

<dl> <dt>

*max* \[out\]
</dt> <dd>

Maximum value of the counter.

</dd> <dt>

*min* \[out\]
</dt> <dd>

Minimum value of the counter.

</dd> <dt>

*average* \[out\]
</dt> <dd>

Average value of the counter.

</dd> <dt>

*status* \[out\]
</dt> <dd>

Indicates if the values are valid.



| Value                                                                                              | Meaning                              |
|----------------------------------------------------------------------------------------------------|--------------------------------------|
| <dl> <dt>0</dt> </dl>                       | The values are valid.<br/>     |
| <dl> <dt>0xC0000BBA (3221228474)</dt> </dl> | The values are not valid.<br/> |



 

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Only those counter values that are visible in the graph window are used to calculate the statistical values.

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

[**CounterItem.GetDataAt**](counteritem-getdataat.md)
</dt> <dt>

[**CounterItem.GetValue**](counteritem-getvalue.md)
</dt> </dl>

 

 






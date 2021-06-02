---
title: CounterItem.GetValue method
description: Retrieves the last value of the counter.
ms.assetid: cf50d878-a119-42b0-bc59-b0e37ed15321
keywords:
- GetValue method SysMon
- GetValue method SysMon , CounterItem class
- CounterItem class SysMon , GetValue method
topic_type:
- apiref
api_name:
- CounterItem.GetValue
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# CounterItem.GetValue method

Retrieves the last value of the counter.

## Syntax


```VB
CounterItem.GetValue( _
  ByRef value As Double, _
  ByRef status As Long _
)
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Last sampled value of the counter.

</dd> <dt>

*status* \[out\]
</dt> <dd>

Indicates if the value is valid.



| Value                                                                                              | Meaning                            |
|----------------------------------------------------------------------------------------------------|------------------------------------|
| <dl> <dt>0</dt> </dl>                       | The value is valid.<br/>     |
| <dl> <dt>0xC0000BBA (3221228474)</dt> </dl> | The value is not valid.<br/> |



 

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

If the source of the counter data is from a log file, the value is the last counter value in the log file.

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

[**CounterItem.GetStatistics**](counteritem-getstatistics.md)
</dt> <dt>

[**CounterItem.Value**](counteritem-value.md)
</dt> </dl>

 

 






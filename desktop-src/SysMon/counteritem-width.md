---
title: CounterItem.Width property
description: Retrieves or sets the line width used to graph the counter value.
ms.assetid: 1f5c1e74-18d4-4005-b83f-bf7265d356cb
keywords:
- Width property SysMon
- Width property SysMon , CounterItem class
- CounterItem class SysMon , Width property
topic_type:
- apiref
api_name:
- CounterItem.Width
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# CounterItem.Width property

Retrieves or sets the line width used to graph the counter value.

This property is read/write.

## Syntax


```VB
Property Width As Long
```



## Property value

Line width used in a line graph. Valid values range from 1 to 3, where 1 (the default value) is the narrowest width.

**Prior to Windows Vista:** Valid values range from 1 to 9. Do not use a width value greater than 3 if your application will be run on Windows Vista.

## Exceptions



| Exception type               | Condition                              |
|------------------------------|----------------------------------------|
| **System.ArgumentException** | The specified line width is not valid. |



 

## Remarks

The default line width for the first sixteen counters that you add is 1. The default line width for the next sixteen counters (counters 17 - 32) that you add is 2. The default line width for the next sixteen counters (counters 33 - 48) that you add is 3. After that, SYSMON randomly chooses the line width. For details, see [**CounterItem.Color**](counteritem-color.md).

To specify a [**line style**](counteritem-linestyle.md) other than solid, the width must be 1. If you specify a value greater than 1 and specify a non-solid line style, SYSMON ignores the specified line width.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



## See also

<dl> <dt>

[**CounterItem**](counteritem.md)
</dt> </dl>

 

 






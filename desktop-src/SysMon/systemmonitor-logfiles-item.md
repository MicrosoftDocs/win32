---
title: LogFiles.Item property
description: Retrieves the specified LogFileItem instance from the collection.
ms.assetid: 518c1343-f659-4434-910c-958c09ffab6a
keywords:
- Item property SysMon
- Item property SysMon , LogFiles class
- LogFiles class SysMon , Item property
topic_type:
- apiref
api_name:
- LogFiles.Item
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# LogFiles.Item property

Retrieves the specified [**LogFileItem**](logfileitem.md) instance from the collection.

This property is read-only.

## Syntax


```VB
Property Item( _
  ByVal index As Object _
) As LogFileItem
```



## Property value

[**LogFileItem**](logfileitem.md) instance that corresponds to the specified index value.

## Remarks

This is the default property of the [**LogFiles**](systemmonitor-logfiles.md) object.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



## See also

<dl> <dt>

[LogFiles](logfiles.md)
</dt> <dt>

[**LogFileItem**](logfileitem.md)
</dt> <dt>

[**LogFiles**](systemmonitor-logfiles.md)
</dt> </dl>

 

 






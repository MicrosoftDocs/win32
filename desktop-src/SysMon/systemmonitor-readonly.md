---
title: SystemMonitor.ReadOnly property
description: Retrieves or sets a value that determines whether a user can modify the property values of the control.
ms.assetid: 6ecfd63a-09b1-46eb-803f-6cb05bdecc25
keywords:
- ReadOnly property SysMon
- ReadOnly property SysMon , SystemMonitor class
- SystemMonitor class SysMon , ReadOnly property
topic_type:
- apiref
api_name:
- SystemMonitor.ReadOnly
api_location:
- Sysmon.ocx
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SystemMonitor.ReadOnly property

Retrieves or sets a value that determines whether a user can modify the property values of the control.

This property is read-only.

## Syntax


```VB
Property ReadOnly As Boolean
```



## Property value

True if you do not want the user to modify the property values of the control; otherwise, false. The default value is false, meaning that users can modify the property values of the control.

## Remarks

When the value of this property is True, the following conditions are in effect:

-   The user cannot use the context menu.
-   The following toolbar buttons are disabled:
    -   New Counter Set
    -   View Current Activity
    -   View Log File Data
    -   Add
    -   Delete
    -   Paste Counter List
    -   Properties

Note that this property affects only the user's ability to modify property values through the user interface, it does not prevent you from programmatically modifying property values or counters.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Sysmon.ocx</dt> </dl> |



## See also

<dl> <dt>

[**SystemMonitor**](systemmonitor.md)
</dt> </dl>

 

 






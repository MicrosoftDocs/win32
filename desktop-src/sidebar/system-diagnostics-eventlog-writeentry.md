---
title: System.Diagnostics.EventLog.writeEntry method
description: Writes an Application event log entry.
ms.assetid: 'c412d92d-7def-4cb5-8285-a72bda110507'
keywords: ["writeEntry method Windows Sidebar", "writeEntry method Windows Sidebar , System.Diagnostics.EventLog object", "System.Diagnostics.EventLog object Windows Sidebar , writeEntry method"]
topic_type:
- apiref
api_name:
- System.Diagnostics.EventLog.writeEntry
api_location:
- Sidebar.Exe
api_type:
- COM
---

# System.Diagnostics.EventLog.writeEntry method

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Writes an **Application** event log entry.

## Syntax


```JScript
iRetVal = System.Diagnostics.EventLog.writeEntry(
  strEventLogEntry,
  [ intEventType = 3 ]
)
```



## Parameters

<dl> <dt>

*strEventLogEntry* \[in\]
</dt> <dd>

**String** to write to the event log.

</dd> <dt>

*intEventType* \[in, optional\]
</dt> <dd>

**Integer** that specifies the event type.

<dt>



 (0)


</dt> <dd>

Success.

</dd> <dt>



 (1)


</dt> <dd>

Error.

</dd> <dt>



 (2)


</dt> <dd>

Warning.

</dd> <dt>



 (3)


</dt> <dd>

Default. Information.

</dd> </dl> </dd> </dl>

## Remarks

The Windows Event Viewer with events logged using **writeEntry**.

![windows event viewer](images/reference/systemdiagnostics.png)

## Examples

The following example demonstrates how to write an event log entry.


```JScript
function PostEvent(event)
{
    System.Diagnostics.EventLog.writeEntry(
        window.event.srcElement.value, window.event.srcElement.id);
}
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 






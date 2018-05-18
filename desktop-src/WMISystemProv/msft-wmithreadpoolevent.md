---
title: MSFT\_WmiThreadPoolEvent class
description: Provides notification of thread events in the WMI Event SubSystem (ESS).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '284bd9cb-83bc-4686-99fb-b1c3d3b353ad'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_WmiThreadPoolEvent class", "MSFT_WmiThreadPoolEvent class, described"]
topic_type:
- apiref
api_name:
- MSFT_WmiThreadPoolEvent
- MSFT_WmiThreadPoolEvent.SECURITY_DESCRIPTOR
- MSFT_WmiThreadPoolEvent.ThreadID
- MSFT_WmiThreadPoolEvent.TIME_CREATED
api_location:
- WmiPrvSD.dll
api_type:
- DllExport
---

# MSFT\_WmiThreadPoolEvent class

The **MSFT\_WmiThreadPoolEvent** abstract [troubleshooting class](https://msdn.microsoft.com/library/aa394604) provides notification of thread events in the WMI Event SubSystem (ESS).

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
class MSFT_WmiThreadPoolEvent : MSFT_WmiEssEvent
{
  uint8  SECURITY_DESCRIPTOR[];
  uint32 ThreadID;
  uint64 TIME_CREATED;
};
```

## Members

The **MSFT\_WmiThreadPoolEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_WmiThreadPoolEvent** class has these properties.

<dl> <dt>

**SECURITY\_DESCRIPTOR**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Descriptor that the event provider uses to determine which users can receive the event. For more information, see [WMI Security Constants](https://msdn.microsoft.com/library/aa394576).

This property is inherited from [**\_\_Event**](https://msdn.microsoft.com/library/aa394634)

</dd> <dt>

**ThreadID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifier of the thread involved in the event.

</dd> <dt>

**TIME\_CREATED**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique value that indicates the time the event is generated. This is a 64-bit value that represents the number of 100-nanosecond intervals after January 1, 1601. The information is in the Coordinated Universal Time (UTC) format.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

This property is inherited from [**\_\_Event**](https://msdn.microsoft.com/library/aa394634)

</dd> </dl>

## Examples

The following VBScript code example reports thread creation and deletion events in the WMI event system. These events generate the classes derived from **MSFT\_WmiThreadPoolEvent**: [**MSFT\_WmiThreadPoolCreated**](msft-wmithreadpoolcreated.md) and [**MSFT\_WmiThreadPoolDeleted**](msft-wmithreadpooldeleted.md).


```VB
strComputer = "." 
Set objWMIService = GetObject("winmgmts:\\" _
    & strComputer & "\root\CIMV2") 
Set objEvents = objWMIService.ExecNotificationQuery _
("SELECT * FROM MSFT_WmiThreadPoolEvent WITHIN 5")

Do While True
    Set objReceivedEvent = objEvents.NextEvent
    Wscript.Echo "An event has occurred: Event class is " _
        & objReceivedEvent.Path_.Class & VBNewLine _
        & "ThreadID = " & objReceivedEvent.ThreadID
Loop

```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>System.mof</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>WmiPrvSD.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WmiEssEvent**](msft-wmiessevent.md)
</dt> <dt>

[WMI Service Event Troubleshooting Classes](https://msdn.microsoft.com/library/aa394578)
</dt> <dt>

[WMI Troubleshooting](https://msdn.microsoft.com/library/aa394603)
</dt> <dt>

WMI Troubleshooting
</dt> <dt>

[Monitoring Events](https://msdn.microsoft.com/library/aa392396)
</dt> <dt>

[Receiving a WMI Event](https://msdn.microsoft.com/library/aa393013)
</dt> </dl>

 

 






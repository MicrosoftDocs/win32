---
title: MSFT\_WmiSelfEvent class
description: Represents events occurring in the WMI service itself.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2bad2d0c-98d4-4fa3-8480-dfa86625fc5b
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_WmiSelfEvent class
- MSFT_WmiSelfEvent class, described
topic_type:
- apiref
api_name:
- MSFT_WmiSelfEvent
- MSFT_WmiSelfEvent.SECURITY_DESCRIPTOR
- MSFT_WmiSelfEvent.TIME_CREATED
api_location:
- WmiPrvSD.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_WmiSelfEvent class

The **MSFT\_WmiSelfEvent** abstract [troubleshooting class](https://msdn.microsoft.com/library/aa394604)represents events occurring in the WMI service itself. You can subscribe to this class to receive notifications of events derived from this class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[AMENDMENT]
class MSFT_WmiSelfEvent : __ExtrinsicEvent
{
  uint8  SECURITY_DESCRIPTOR[];
  uint64 TIME_CREATED;
};
```

## Members

The **MSFT\_WmiSelfEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_WmiSelfEvent** class has these properties.

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

## Remarks

You can subscribe to **MSFT\_WmiSelfEvent** by the following query:


```VB
Select * from MSFT_WmiSelfEvent
```



Derived events include:

-   [**MSFT\_WmiEssEvent**](msft-wmiessevent.md) and its derived classes
-   [**MSFT\_WmiProvider\_OperationEvent**](msft-wmiprovider-operationevent.md)

## Examples

The following VBScript code example polls for occurrences of **MSFT\_WmiSelfEvent** every 10 seconds. The received object, `objReceivedEvent`, represents an instance of an event class; for example, WMI may generate an instance of [**MSFT\_WmiProvider\_UnloadOperationEvent**](msft-wmiprovider-unloadoperationevent.md) when a cached provider is unloaded.

The call to [**SWbemServices.ExecNotificationQuery**](https://msdn.microsoft.com/library/aa393864) is [*semisynchronous*](https://msdn.microsoft.com/library/aa390836#wmi-gloss-semisynchronous) by default. This script runs and waits for events indefinitely. To stop script execution, use Task Manager to stop the process running Windows Script Host.


```VB
strComputer = "." 
Set objWMIService = GetObject("winmgmts:\\" & strComputer & "\root\CIMV2") 
Set objEvents = objWMIService.ExecNotificationQuery("SELECT * FROM MSFT_WmiselfEvent WITHIN 10")
Wscript.Echo "Waiting for MSFT_WmiselfEvent events"
Do While True
    Set objReceivedEvent = objEvents.NextEvent
    Wscript.Echo "Event has occurred: Event class is " & objReceivedEvent.Path_.Class
Loop
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>System.mof</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>WmiPrvSD.dll</dt> </dl> |



## See also

<dl> <dt>

[**\_\_ExtrinsicEvent**](https://msdn.microsoft.com/library/aa394646)
</dt> <dt>

[WMI Troubleshooting Classes](https://msdn.microsoft.com/library/aa394604)
</dt> <dt>

[Monitoring Events](https://msdn.microsoft.com/library/aa392396)
</dt> <dt>

[Receiving a WMI Event](https://msdn.microsoft.com/library/aa393013)
</dt> </dl>

 

 






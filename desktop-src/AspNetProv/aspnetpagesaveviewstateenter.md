---
Description: The event type class for the PageSaveViewstateEnter event.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 72590293-7428-42dc-a16f-5cb932f4d626
ms.prod: windows-server-dev
ms.technology:
- asp.net
- windows-management-instrumentation
ms.tgt_platform: multiple
title: AspNetPageSaveViewstateEnter class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AspNetPageSaveViewstateEnter class

The event type class for the **PageSaveViewstateEnter** event.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, EventType(38), EventLevel(5), EventTypeName("PageSaveViewstateEnter")]
class AspNetPageSaveViewstateEnter : AspNetTraceEvent
{
  uint16 EventSize;
  uint16 ReservedHeaderField;
  uint8  EventType;
  uint8  TraceLevel;
  uint16 TraceVersion;
  uint64 ThreadId;
  uint64 TimeStamp;
  uint8  EventGuid[];
  uint32 KernelTime;
  uint32 UserTime;
  uint32 InstanceId;
  uint8  ParentGuid[];
  uint32 ParentInstanceId;
  uint32 MofData;
  uint32 MofLength;
  uint32 Flags;
  uint32 Level;
  uint64 ConnID;
  object ContextId;
};
```

## Members

The **AspNetPageSaveViewstateEnter** class has these types of members:

-   [Properties](#properties)

### Properties

The **AspNetPageSaveViewstateEnter** class has these properties.

<dl> <dt>

**ConnID**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (1)
</dt> </dl>

The connection identifier

</dd> <dt>

**ContextId**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (2), **extension** ("Guid"), **ActivityID**
</dt> </dl>

The context identifier

</dd> <dt>

**EventGuid**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**WmiDataId**](https://msdn.microsoft.com/windows/desktop/3bc82074-05a7-411f-884f-5da1fd08112b) (8), **Max** (16)
</dt> </dl>

Event trace class GUID of this event.

</dd> <dt>

**EventSize**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**WmiDataId**](https://msdn.microsoft.com/windows/desktop/3bc82074-05a7-411f-884f-5da1fd08112b) (1)
</dt> </dl>

Total number of bytes of the event.

</dd> <dt>

**EventType**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**WmiDataId**](https://msdn.microsoft.com/windows/desktop/3bc82074-05a7-411f-884f-5da1fd08112b) (3)
</dt> </dl>

Provider-defined event type. Tells you which event type class to use to decipher the provider-defined event data (the data pointed to by **MofData**.

</dd> <dt>

**Flags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **ValueDescriptions** ("Infrastructure Events", "Pipeline Module Events", "Page Events", "Application Services Events"), **DefineValues** ("ETW\_ASPNET\_INFRASTRUCTURE", "ETW\_ASPNET\_MODULE", "ETW\_ASPNET\_PAGE", "ETW\_ASPNET\_APPSVC"), **Values** ("Infrastructure", "Module", "Page", "AppServices"), **ValueMap** ("0x0001", "0x0002", "0x0004", "0x0008")
</dt> </dl>

The classes of events that are enabled.

<dt>

<span id="Infrastructure"></span><span id="infrastructure"></span><span id="INFRASTRUCTURE"></span>

<span id="Infrastructure"></span><span id="infrastructure"></span><span id="INFRASTRUCTURE"></span>**Infrastructure** (1)


</dt> <dd>

Infrastructure Events

</dd> <dt>

<span id="Module"></span><span id="module"></span><span id="MODULE"></span>

<span id="Module"></span><span id="module"></span><span id="MODULE"></span>**Module** (2)


</dt> <dd>

Pipeline Module Events

</dd> <dt>

<span id="Page"></span><span id="page"></span><span id="PAGE"></span>

<span id="Page"></span><span id="page"></span><span id="PAGE"></span>**Page** (4)


</dt> <dd>

Page Events

</dd> <dt>

<span id="AppServices"></span><span id="appservices"></span><span id="APPSERVICES"></span>

<span id="AppServices"></span><span id="appservices"></span><span id="APPSERVICES"></span>**AppServices** (8)


</dt> <dd>

Application Services Events

</dd> </dl>

</dd> <dt>

**InstanceId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**WmiDataId**](https://msdn.microsoft.com/windows/desktop/3bc82074-05a7-411f-884f-5da1fd08112b) (11)
</dt> </dl>

Identifier of this event instance.

</dd> <dt>

**KernelTime**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**WmiDataId**](https://msdn.microsoft.com/windows/desktop/3bc82074-05a7-411f-884f-5da1fd08112b) (9)
</dt> </dl>

Elapsed execution time for kernel-mode instructions, in CPU ticks.

</dd> <dt>

**Level**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **ValueDescriptions** ("Abnormal exit or termination", "Severe errors", "Warnings", "Information", "Detailed information"), **DefineValues** ("TRACE\_LEVEL\_FATAL", "TRACE\_LEVEL\_ERROR", "TRACE\_LEVEL\_WARNING", "TRACE\_LEVEL\_INFORMATION", "TRACE\_LEVEL\_VERBOSE"), **Values** ("Fatal", "Error", "Warning", "Information", "Verbose"), **ValueMap** ("0x1", "0x2", "0x3", "0x4", "0x5"), **ValueType** ("index")
</dt> </dl>

The error level of the event.

<dt>

<span id="Fatal"></span><span id="fatal"></span><span id="FATAL"></span>

<span id="Fatal"></span><span id="fatal"></span><span id="FATAL"></span>**Fatal** (1)


</dt> <dd>

Abnormal exit or termination

</dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>**Error** (2)


</dt> <dd>

Severe errors

</dd> <dt>

<span id="Warning"></span><span id="warning"></span><span id="WARNING"></span>

<span id="Warning"></span><span id="warning"></span><span id="WARNING"></span>**Warning** (3)


</dt> <dd>

Warnings

</dd> <dt>

<span id="Information"></span><span id="information"></span><span id="INFORMATION"></span>

<span id="Information"></span><span id="information"></span><span id="INFORMATION"></span>**Information** (4)


</dt> <dd>

Information

</dd> <dt>

<span id="Verbose"></span><span id="verbose"></span><span id="VERBOSE"></span>

<span id="Verbose"></span><span id="verbose"></span><span id="VERBOSE"></span>**Verbose** (5)


</dt> <dd>

Detailed information

</dd> </dl>

</dd> <dt>

**MofData**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**WmiDataId**](https://msdn.microsoft.com/windows/desktop/3bc82074-05a7-411f-884f-5da1fd08112b) (14), **Pointer**
</dt> </dl>

Pointer to the provider-specific event data.

</dd> <dt>

**MofLength**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**WmiDataId**](https://msdn.microsoft.com/windows/desktop/3bc82074-05a7-411f-884f-5da1fd08112b) (15)
</dt> </dl>

Length of the provider-specific event data.

</dd> <dt>

**ParentGuid**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**WmiDataId**](https://msdn.microsoft.com/windows/desktop/3bc82074-05a7-411f-884f-5da1fd08112b) (12), **Max** (16)
</dt> </dl>

Event trace class GUID of the parent instance.

</dd> <dt>

**ParentInstanceId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**WmiDataId**](https://msdn.microsoft.com/windows/desktop/3bc82074-05a7-411f-884f-5da1fd08112b) (13)
</dt> </dl>

Identifier of the parent instance data.

</dd> <dt>

**ReservedHeaderField**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**WmiDataId**](https://msdn.microsoft.com/windows/desktop/3bc82074-05a7-411f-884f-5da1fd08112b) (2)
</dt> </dl>

Reserved.

</dd> <dt>

**ThreadId**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**WmiDataId**](https://msdn.microsoft.com/windows/desktop/3bc82074-05a7-411f-884f-5da1fd08112b) (6), **Pointer**
</dt> </dl>

Identifies the thread that generated the event.

</dd> <dt>

**TimeStamp**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**WmiDataId**](https://msdn.microsoft.com/windows/desktop/3bc82074-05a7-411f-884f-5da1fd08112b) (7)
</dt> </dl>

Contains the date and time when the event occurred.

</dd> <dt>

**TraceLevel**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**WmiDataId**](https://msdn.microsoft.com/windows/desktop/3bc82074-05a7-411f-884f-5da1fd08112b) (4)
</dt> </dl>

Provider-defined value that defines the severity level used to generate the event.

</dd> <dt>

**TraceVersion**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**WmiDataId**](https://msdn.microsoft.com/windows/desktop/3bc82074-05a7-411f-884f-5da1fd08112b) (5)
</dt> </dl>

Provider-defined version number of the event trace class used to generate the event.

</dd> <dt>

**UserTime**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**WmiDataId**](https://msdn.microsoft.com/windows/desktop/3bc82074-05a7-411f-884f-5da1fd08112b) (10)
</dt> </dl>

Elapsed execution time for user-mode instructions, in CPU ticks.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\WMI<br/>                                                                   |
| MOF<br/>                      | <dl> <dt>AspNet.mof</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>MSCoree.dll</dt> </dl> |



 

 





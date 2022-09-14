---
description: Indicates a Machine Check Architecture (MCA) invalid error. An invalid MCA error identifies an error format that does not conform to Windows specifications. This class is available only in 64-bit Windows systems.
ms.assetid: 476ea558-2e0e-480f-b4ba-8d73fdef3308
title: MSMCAEvent_InvalidError class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSMCAEvent_InvalidError
- MSMCAEvent_InvalidError.Active
- MSMCAEvent_InvalidError.AdditionalErrors
- MSMCAEvent_InvalidError.Cpu
- MSMCAEvent_InvalidError.ErrorSeverity
- MSMCAEvent_InvalidError.InstanceName
- MSMCAEvent_InvalidError.RawRecord
- MSMCAEvent_InvalidError.RecordId
- MSMCAEvent_InvalidError.Size
- MSMCAEvent_InvalidError.Type
- MSMCAEvent_InvalidError.LogToEventlog
api_type: 
- DllExport
api_location: 
- Wmiprov.dll
---

# MSMCAEvent\_InvalidError class

The **MSMCAEvent\_InvalidError** class indicates a Machine Check Architecture (MCA) invalid error. An invalid MCA error identifies an error format that does not conform to Windows specifications. This class is available only in 64-bit Windows systems.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
class MSMCAEvent_InvalidError : WMIEvent
{
  boolean Active;
  uint32  AdditionalErrors;
  uint32  Cpu;
  uint8   ErrorSeverity;
  string  InstanceName;
  uint8   RawRecord[];
  uint64  RecordId;
  uint32  Size;
  uint32  Type;
  uint32  LogToEventlog;
};
```

## Members

The **MSMCAEvent\_InvalidError** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSMCAEvent\_InvalidError** class has these properties.

<dl> <dt>

**Active**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**TRUE**, if this instance of the class is active; otherwise, **FALSE**.

</dd> <dt>

**AdditionalErrors**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of additional errors in the MCA record.

</dd> <dt>

**Cpu**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

CPU that reported the error. This property only applies to a multiprocessor system in which the first processor is assigned the number 0, the second processor is assigned the number 1, and so on.

</dd> <dt>

**ErrorSeverity**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Severity level of the error reported.



| Value                                                                                                | Meaning                |
|------------------------------------------------------------------------------------------------------|------------------------|
| <span id="0"></span><dl> <dt>**0**</dt> </dl> | Recoverable<br/> |
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | Fatal<br/>       |
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | Correctable<br/> |



 

</dd> <dt>

**InstanceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/standard-qualifiers)
</dt> </dl>

Unique identifier of this instance of the class.

</dd> <dt>

**LogToEventlog**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If 0 (zero) then this event is not logged to the system event log.

</dd> <dt>

**RawRecord**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Array of bytes that contains the raw error record as presented to Windows by the system abstraction layer (SAL). The number of elements in the array is specified by the **Size** property.

</dd> <dt>

**RecordId**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Record identifier of the error record for this error.

For more information about using **uint64** values in scripts, see [Scripting in WMI](/previous-versions//aa393262(v=vs.85)).

</dd> <dt>

**Size**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Size of the raw error record.

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Type of event log message. These messages correspond to the event log message codes used to insert event log messages by the Windows event log consumer provider when it receives one of the events.

</dd> </dl>

## Remarks

The **MSMCAEvent\_InvalidError** class is derived from [**WMIEvent**](wmievent.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                         |
| Namespace<br/>                | Root\\wmi<br/>                                                                   |
| MOF<br/>                      | <dl> <dt>Wmicore.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmiprov.dll</dt> </dl> |



## See also

<dl> <dt>

[MSMCA Classes](msmca-classes.md)
</dt> <dt>

[**WMIEvent**](wmievent.md)
</dt> </dl>

 


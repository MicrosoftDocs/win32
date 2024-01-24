---
description: Indicates that an Intelligent Platform Management Interface (IPMI) system event has occurred. The error is written to the SMBIOS System Event Log (SEL). This class is available only in 64-bit Windows systems.
ms.assetid: 1964f850-ac55-4639-9205-2eb0996dbaae
title: MSMCAEvent_SystemEventError class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSMCAEvent_SystemEventError
- MSMCAEvent_SystemEventError.Active
- MSMCAEvent_SystemEventError.AdditionalErrors
- MSMCAEvent_SystemEventError.Cpu
- MSMCAEvent_SystemEventError.ErrorSeverity
- MSMCAEvent_SystemEventError.InstanceName
- MSMCAEvent_SystemEventError.RawRecord
- MSMCAEvent_SystemEventError.RecordId
- MSMCAEvent_SystemEventError.SEL_DATA1
- MSMCAEvent_SystemEventError.SEL_DATA2
- MSMCAEvent_SystemEventError.SEL_DATA3
- MSMCAEvent_SystemEventError.SEL_EVENT_DIR_TYPE
- MSMCAEvent_SystemEventError.SEL_EVM_REV
- MSMCAEvent_SystemEventError.SEL_GENERATOR_ID
- MSMCAEvent_SystemEventError.SEL_RECORD_ID
- MSMCAEvent_SystemEventError.SEL_RECORD_TYPE
- MSMCAEvent_SystemEventError.SEL_SENSOR_NUM
- MSMCAEvent_SystemEventError.SEL_SENSOR_TYPE
- MSMCAEvent_SystemEventError.SEL_TIME_STAMP
- MSMCAEvent_SystemEventError.Size
- MSMCAEvent_SystemEventError.Type
- MSMCAEvent_SystemEventError.VALIDATION_BITS
- MSMCAEvent_SystemEventError.LogToEventlog
api_type: 
- DllExport
api_location: 
- Wmiprov.dll
---

# MSMCAEvent\_SystemEventError class

The **MSMCAEvent\_SystemEventError** class indicates that an Intelligent Platform Management Interface (IPMI) system event has occurred. The error is written to the SMBIOS System Event Log (SEL). This class is available only in 64-bit Windows systems.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
class MSMCAEvent_SystemEventError : WMIEvent
{
  boolean Active;
  uint32  AdditionalErrors;
  uint32  Cpu;
  uint8   ErrorSeverity;
  string  InstanceName;
  uint8   RawRecord[];
  uint64  RecordId;
  uint8   SEL_DATA1;
  uint8   SEL_DATA2;
  uint8   SEL_DATA3;
  uint8   SEL_EVENT_DIR_TYPE;
  uint8   SEL_EVM_REV;
  uint16  SEL_GENERATOR_ID;
  uint16  SEL_RECORD_ID;
  uint8   SEL_RECORD_TYPE;
  uint8   SEL_SENSOR_NUM;
  uint8   SEL_SENSOR_TYPE;
  uint64  SEL_TIME_STAMP;
  uint32  Size;
  uint32  Type;
  uint64  VALIDATION_BITS;
  uint32  LogToEventlog;
};
```

## Members

The **MSMCAEvent\_SystemEventError** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSMCAEvent\_SystemEventError** class has these properties.

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

Number of additional errors in the record.

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

Array of bytes that contains the raw error record. The number of elements in the array that the **Size** property specifies.

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

**SEL\_DATA1**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Event data field 1.

</dd> <dt>

**SEL\_DATA2**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Event data field 2.

</dd> <dt>

**SEL\_DATA3**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Event data field 3.

</dd> <dt>

**SEL\_EVENT\_DIR\_TYPE**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Event directory type.

</dd> <dt>

**SEL\_EVM\_REV**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Format version of the error message.

</dd> <dt>

**SEL\_GENERATOR\_ID**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Software identifier, if the event was software-generated.

</dd> <dt>

**SEL\_RECORD\_ID**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Record identifier used for SMBIOS system event log (SEL) access.

</dd> <dt>

**SEL\_RECORD\_TYPE**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Record type.

</dd> <dt>

**SEL\_SENSOR\_NUM**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Sensor number that generated the event.

</dd> <dt>

**SEL\_SENSOR\_TYPE**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Sensor type code of the sensor that generated the event.

</dd> <dt>

**SEL\_TIME\_STAMP**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Timestamp of the event log.

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

</dd> <dt>

**VALIDATION\_BITS**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Validation bits used to indicate the validity of the subsequent fields.



| Value                                                                                                                                            | Meaning                                     |
|--------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| <span id="1_0x1"></span><span id="1_0X1"></span><dl> <dt>**1 0x1**</dt> </dl>             | **SEL\_RECORD\_ID** is valid.<br/>    |
| <span id="2_0x2"></span><span id="2_0X2"></span><dl> <dt>**2 0x2**</dt> </dl>             | **SEL\_RECORD\_TYPE** is valid.<br/>  |
| <span id="4_0x4"></span><span id="4_0X4"></span><dl> <dt>**4 0x4**</dt> </dl>             | **SEL\_GENERATOR\_ID** is valid.<br/> |
| <span id="8_0x8"></span><span id="8_0X8"></span><dl> <dt>**8 0x8**</dt> </dl>             | **SEL\_EVM\_REV** is valid.<br/>      |
| <span id="16_0x10"></span><span id="16_0X10"></span><dl> <dt>**16 0x10**</dt> </dl>       | **SEL\_SENSOR\_TYPE** is valid.<br/>  |
| <span id="32_0x20"></span><span id="32_0X20"></span><dl> <dt>**32 0x20**</dt> </dl>       | **SEL\_SENSOR\_NUM** is valid.<br/>   |
| <span id="64_0x40"></span><span id="64_0X40"></span><dl> <dt>**64 0x40**</dt> </dl>       | **SEL\_EVENT\_DIR** is valid.<br/>    |
| <span id="128_0x80"></span><span id="128_0X80"></span><dl> <dt>**128 0x80**</dt> </dl>    | **SEL\_EVENT\_DATA1** is valid.<br/>  |
| <span id="256_0x100"></span><span id="256_0X100"></span><dl> <dt>**256 0x100**</dt> </dl> | **SEL\_EVENT\_DATA2** is valid.<br/>  |
| <span id="512_0x200"></span><span id="512_0X200"></span><dl> <dt>**512 0x200**</dt> </dl> | **SEL\_EVENT\_DATA3** is valid.<br/>  |



 

For more information about using **uint64** values in scripts, see [Scripting in WMI](/previous-versions//aa393262(v=vs.85)).

</dd> </dl>

## Remarks

The **MSMCAEvent\_SystemEventError** class is derived from [**WMIEvent**](wmievent.md).

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

 


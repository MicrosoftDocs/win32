---
description: Indicates a Machine Check Architecture (MCA) system BIOS error. This class is available only in 64-bit Windows systems.
ms.assetid: b451ca45-6208-4445-b9f1-b4e3174837a4
title: MSMCAEvent_SMBIOSError class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSMCAEvent_SMBIOSError
- MSMCAEvent_SMBIOSError.Active
- MSMCAEvent_SMBIOSError.AdditionalErrors
- MSMCAEvent_SMBIOSError.Cpu
- MSMCAEvent_SMBIOSError.ErrorSeverity
- MSMCAEvent_SMBIOSError.InstanceName
- MSMCAEvent_SMBIOSError.RawRecord
- MSMCAEvent_SMBIOSError.RecordId
- MSMCAEvent_SMBIOSError.Size
- MSMCAEvent_SMBIOSError.SMBIOS_EVENT_TYPE
- MSMCAEvent_SMBIOSError.Type
- MSMCAEvent_SMBIOSError.VALIDATION_BITS
- MSMCAEvent_SMBIOSError.LogToEventlog
api_type: 
- DllExport
api_location: 
- Wmiprov.dll
---

# MSMCAEvent\_SMBIOSError class

The **MSMCAEvent\_SMBIOSError** class indicates a Machine Check Architecture (MCA) system BIOS error. This class is available only in 64-bit Windows systems.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
class MSMCAEvent_SMBIOSError : WMIEvent
{
  boolean Active;
  uint32  AdditionalErrors;
  uint32  Cpu;
  uint8   ErrorSeverity;
  string  InstanceName;
  uint8   RawRecord[];
  uint64  RecordId;
  uint32  Size;
  uint8   SMBIOS_EVENT_TYPE;
  uint32  Type;
  uint64  VALIDATION_BITS;
  uint32  LogToEventlog;
};
```

## Members

The **MSMCAEvent\_SMBIOSError** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSMCAEvent\_SMBIOSError** class has these properties.

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

If 0 (zero), then this event is not logged to the system event log.

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

**Size**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Size of the raw error record.

</dd> <dt>

**SMBIOS\_EVENT\_TYPE**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Event type.



| Value                                                                                                  | Meaning                                                                                                                     |
|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| <span id="0"></span><dl> <dt>**0**</dt> </dl>   | Reserved.<br/>                                                                                                        |
| <span id="1"></span><dl> <dt>**1**</dt> </dl>   | Single bit ECC memory error.<br/>                                                                                     |
| <span id="2"></span><dl> <dt>**2**</dt> </dl>   | Multiple bit ECC memory error.<br/>                                                                                   |
| <span id="3"></span><dl> <dt>**3**</dt> </dl>   | Parity Memory error.<br/>                                                                                             |
| <span id="4"></span><dl> <dt>**4**</dt> </dl>   | Bus time out.<br/>                                                                                                    |
| <span id="5"></span><dl> <dt>**5**</dt> </dl>   | I/O Channel Check.<br/>                                                                                               |
| <span id="6"></span><dl> <dt>**6**</dt> </dl>   | Software NMI.<br/>                                                                                                    |
| <span id="7"></span><dl> <dt>**7**</dt> </dl>   | Post Memory Resize.<br/>                                                                                              |
| <span id="8"></span><dl> <dt>**8**</dt> </dl>   | POST Error.<br/>                                                                                                      |
| <span id="9"></span><dl> <dt>**9**</dt> </dl>   | PCI Parity Error.<br/>                                                                                                |
| <span id="10"></span><dl> <dt>**10**</dt> </dl> | PCI System Error.<br/>                                                                                                |
| <span id="11"></span><dl> <dt>**11**</dt> </dl> | CPU Failure.<br/>                                                                                                     |
| <span id="12"></span><dl> <dt>**12**</dt> </dl> | EISA Failsafe Timer time out.<br/>                                                                                    |
| <span id="13"></span><dl> <dt>**13**</dt> </dl> | Correctable memory log disabled.<br/>                                                                                 |
| <span id="14"></span><dl> <dt>**14**</dt> </dl> | Logging disabled for a specific event type. Too many errors of the same type received in a short amount of time.<br/> |
| <span id="15"></span><dl> <dt>**15**</dt> </dl> | Reserved.<br/>                                                                                                        |
| <span id="16"></span><dl> <dt>**16**</dt> </dl> | System limit exceeded (for example, voltage or temperature threshold exceeded).<br/>                                  |
| <span id="17"></span><dl> <dt>**17**</dt> </dl> | Asynchronous hardware timer expired and issued a system reset.<br/>                                                   |
| <span id="18"></span><dl> <dt>**18**</dt> </dl> | System configuration information.<br/>                                                                                |
| <span id="19"></span><dl> <dt>**19**</dt> </dl> | Hard disk information.<br/>                                                                                           |
| <span id="20"></span><dl> <dt>**20**</dt> </dl> | System reconfigured.<br/>                                                                                             |
| <span id="21"></span><dl> <dt>**21**</dt> </dl> | Uncorrectable CPU-complex error.<br/>                                                                                 |
| <span id="22"></span><dl> <dt>**22**</dt> </dl> | Log Area Reset or Cleared.<br/>                                                                                       |
| <span id="23"></span><dl> <dt>**23**</dt> </dl> | System boot. If implemented, this log entry is guaranteed to be the first one written on any system boot.<br/>        |



 

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

Validation bits used to indicate the validity of the subsequent fields. A value of 1 (0x1) means that the **SMBIOS\_EVENT** is valid.

For more information about using **uint64** values in scripts, see [Scripting in WMI](/previous-versions//aa393262(v=vs.85)).

</dd> </dl>

## Remarks

The **MSMCAEvent\_SMBIOSError** class is derived from [**WMIEvent**](wmievent.md).

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

 


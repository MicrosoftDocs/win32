---
description: Represents the capabilities and management of memory-related logical devices.
ms.assetid: 802c1c0e-7eab-4a17-9a29-6502ece6cb24
title: CIM_Memory class (Hyper-V management)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_Memory
- CIM_Memory.Volatile
- CIM_Memory.ErrorMethodology
- CIM_Memory.StartingAddress
- CIM_Memory.EndingAddress
- CIM_Memory.ErrorInfo
- CIM_Memory.OtherErrorDescription
- CIM_Memory.CorrectableError
- CIM_Memory.ErrorTime
- CIM_Memory.ErrorAccess
- CIM_Memory.ErrorTransferSize
- CIM_Memory.ErrorData
- CIM_Memory.ErrorDataOrder
- CIM_Memory.ErrorAddress
- CIM_Memory.SystemLevelAddress
- CIM_Memory.ErrorResolution
- CIM_Memory.AdditionalErrorData
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM_Memory class (Hyper-V management)

Represents the capabilities and management of memory-related logical devices.

## Syntax

``` syntax
[Abstract, Version("2.8.0"), UMLPackagePath("CIM::Device::Memory"), AMENDMENT]
class CIM_Memory : CIM_StorageExtent
{
  boolean  Volatile;
  string   ErrorMethodology;
  uint64   StartingAddress;
  uint64   EndingAddress;
  uint16   ErrorInfo;
  string   OtherErrorDescription;
  boolean  CorrectableError;
  datetime ErrorTime;
  uint16   ErrorAccess;
  uint32   ErrorTransferSize;
  uint8    ErrorData[];
  uint16   ErrorDataOrder;
  uint64   ErrorAddress;
  boolean  SystemLevelAddress;
  uint64   ErrorResolution;
  uint8    AdditionalErrorData[];
};
```

## Members

The **CIM\_Memory** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_Memory** class has these properties.

<dl> <dt>

**AdditionalErrorData**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](/windows/desktop/WmiSdk/standard-wmi-qualifiers) ("CIM\_MemoryError.AdditionalErrorData"), **OctetString**, [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Memory Device\|005.18", "MIF.DMTF\|Physical Memory Array\|001.13")
</dt> </dl>

An array of octets that contains additional error information. An example is ECC syndrome or the return of the check bits if a CRC-based error methodology is used. In the latter case, if a single bit error is recognized and the CRC algorithm is known, it is possible to determine the exact bit that failed.

If the **ErrorInfo** property contains "3" (OK), this property is not used.

</dd> <dt>

**CorrectableError**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](/windows/desktop/WmiSdk/standard-wmi-qualifiers) ("CIM\_MemoryError.CorrectableError"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Physical Memory Array\|001.8")
</dt> </dl>

**true** if the most recent error is correctable; otherwise, **false**. If the **ErrorInfo** property contains "3" (OK), this property is not used.

</dd> <dt>

**EndingAddress**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("KiloBytes"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Memory Array Mapped Addresses\|001.4", "MIF.DMTF\|Memory Device Mapped Addresses\|001.5"), **PUnit** ("byte \* 10^3")
</dt> </dl>

The ending address that is referenced by an application or operating system, and mapped by a memory controller for the memory object. The ending address is specified in kilobytes.

</dd> <dt>

**ErrorAccess**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](/windows/desktop/WmiSdk/standard-wmi-qualifiers) ("CIM\_MemoryError.ErrorAccess"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Physical Memory Array\|001.10")
</dt> </dl>

The memory access operation that caused the last error. If the **ErrorInfo** property contains "3" (OK), this property is not used.

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (2)


</dt> <dd></dd> <dt>

<span id="Read"></span><span id="read"></span><span id="READ"></span>

**Read** (3)


</dt> <dd></dd> <dt>

<span id="Write"></span><span id="write"></span><span id="WRITE"></span>

**Write** (4)


</dt> <dd></dd> <dt>

<span id="Partial_Write"></span><span id="partial_write"></span><span id="PARTIAL_WRITE"></span>

**Partial Write** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**ErrorAddress**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](/windows/desktop/WmiSdk/standard-wmi-qualifiers) ("CIM\_MemoryError.StartingAddress"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Memory Device\|005.19", "MIF.DMTF\|Physical Memory Array\|001.14")
</dt> </dl>

The address of the last memory error. The type of error is described by the **ErrorInfo** property. If the **ErrorInfo** property contains "3" (OK), this property is not used.

</dd> <dt>

**ErrorData**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](/windows/desktop/WmiSdk/standard-wmi-qualifiers) ("CIM\_MemoryError.ErrorData"), **OctetString**, [**ArrayType**](/windows/desktop/WmiSdk/standard-qualifiers) ("Indexed"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Physical Memory Array\|001.12")
</dt> </dl>

An array that contains data captured during the last erroneous memory access. The data occupies the first n octets of the array necessary to hold the number of bits specified by the **ErrorTransferSize** property.

If the **ErrorTransferSize** property contains "0" (OK), this property is not used.

</dd> <dt>

**ErrorDataOrder**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](/windows/desktop/WmiSdk/standard-wmi-qualifiers) ("CIM\_MemoryError.ErrorDataOrder")
</dt> </dl>

The ordering for data stored in the **ErrorData** property. "Least Significant Byte First" (value=1) or "Most Significant Byte First" (2) can be specified. If the **ErrorTransferSize** property contains "0" (OK), this property is not used.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Least_Significant_Byte_First"></span><span id="least_significant_byte_first"></span><span id="LEAST_SIGNIFICANT_BYTE_FIRST"></span>

**Least Significant Byte First** (1)


</dt> <dd></dd> <dt>

<span id="Most_Significant_Byte_First"></span><span id="most_significant_byte_first"></span><span id="MOST_SIGNIFICANT_BYTE_FIRST"></span>

**Most Significant Byte First** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**ErrorInfo**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](/windows/desktop/WmiSdk/standard-wmi-qualifiers) ("CIM\_MemoryError.ErrorInfo"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Memory Device\|005.12", "MIF.DMTF\|Physical Memory Array\|001.8"), [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_Memory**.**OtherErrorDescription**")
</dt> </dl>

The type of the last error to occur.

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (2)


</dt> <dd></dd> <dt>

<span id="OK"></span><span id="ok"></span>

**OK** (3)


</dt> <dd></dd> <dt>

<span id="Bad_Read"></span><span id="bad_read"></span><span id="BAD_READ"></span>

**Bad Read** (4)


</dt> <dd></dd> <dt>

<span id="Parity_Error"></span><span id="parity_error"></span><span id="PARITY_ERROR"></span>

**Parity Error** (5)


</dt> <dd></dd> <dt>

<span id="Single-Bit_Error"></span><span id="single-bit_error"></span><span id="SINGLE-BIT_ERROR"></span>

**Single-Bit Error** (6)


</dt> <dd></dd> <dt>

<span id="Double-Bit_Error"></span><span id="double-bit_error"></span><span id="DOUBLE-BIT_ERROR"></span>

**Double-Bit Error** (7)


</dt> <dd></dd> <dt>

<span id="Multi-Bit_Error"></span><span id="multi-bit_error"></span><span id="MULTI-BIT_ERROR"></span>

**Multi-Bit Error** (8)


</dt> <dd></dd> <dt>

<span id="Nibble_Error"></span><span id="nibble_error"></span><span id="NIBBLE_ERROR"></span>

**Nibble Error** (9)


</dt> <dd></dd> <dt>

<span id="Checksum_Error"></span><span id="checksum_error"></span><span id="CHECKSUM_ERROR"></span>

**Checksum Error** (10)


</dt> <dd></dd> <dt>

<span id="CRC_Error"></span><span id="crc_error"></span><span id="CRC_ERROR"></span>

**CRC Error** (11)


</dt> <dd></dd> <dt>

<span id="Undefined"></span><span id="undefined"></span><span id="UNDEFINED"></span>

**Undefined** (12)


</dt> <dd></dd> <dt>

<span id="Undefined"></span><span id="undefined"></span><span id="UNDEFINED"></span>

**Undefined** (13)


</dt> <dd></dd> <dt>

<span id="Undefined"></span><span id="undefined"></span><span id="UNDEFINED"></span>

**Undefined** (14)


</dt> <dd></dd> </dl>

</dd> <dt>

**ErrorMethodology**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("ErrorMethodology"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Physical Memory Array\|001.7")
</dt> </dl>

Indicates whether parity algorithms, CRC algorithms, ECC, or other mechanisms are used by the memory object. Details on the algorithm can also be supplied.

</dd> <dt>

**ErrorResolution**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](/windows/desktop/WmiSdk/standard-wmi-qualifiers) ("CIM\_MemoryError.ErrorResolution"), [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("Bytes"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Memory Device\|005.21", "MIF.DMTF\|Physical Memory Array\|001.15"), **PUnit** ("byte")
</dt> </dl>

The range, in bytes, in which the last error can be resolved. For example, if error addresses are resolved to bit 11, such as on a typical page basis; then the errors can be resolved to 4K boundaries, and this property is set to "4000". If the **ErrorInfo** property contains "3" (OK), this property is not used.

</dd> <dt>

**ErrorTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](/windows/desktop/WmiSdk/standard-wmi-qualifiers) ("CIM\_MemoryError.ErrorTime")
</dt> </dl>

The time when the last memory error occurred. If the **ErrorInfo** property contains "3" (OK), this property is not used.

</dd> <dt>

**ErrorTransferSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](/windows/desktop/WmiSdk/standard-wmi-qualifiers) ("CIM\_MemoryError.ErrorTransferSize"), [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("Bits"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Physical Memory Array\|001.11"), **PUnit** ("bit")
</dt> </dl>

The size of the data transfer, in bits, that caused the last error. "0" indicates no error. If the **ErrorInfo** property contains "3" (OK), this property is not used.

</dd> <dt>

**OtherErrorDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](/windows/desktop/WmiSdk/standard-wmi-qualifiers) ("CIM\_MemoryError.OtherErrorDescription"), [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_Memory**.**ErrorInfo**")
</dt> </dl>

A description of the error type, when the **ErrorType** property is set to "1" (other).

</dd> <dt>

**StartingAddress**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("KiloBytes"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Memory Array Mapped Addresses\|001.3", "MIF.DMTF\|Memory Device Mapped Addresses\|001.4"), **PUnit** ("byte \* 10^3")
</dt> </dl>

The starting address that is referenced by an application or operating system, and mapped by a memory controller for the memory object. The starting address is specified in kilobytes.

</dd> <dt>

**SystemLevelAddress**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Deprecated**](/windows/desktop/WmiSdk/standard-wmi-qualifiers) ("CIM\_MemoryError.SystemLevelAddress")
</dt> </dl>

**true** if the address information in the **ErrorAddress** property is a system-level address, **false** if it is a physical address.

</dd> <dt>

**Volatile**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if the memory is volatile; otherwise, **false**.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_StorageExtent**](cim-storageextent.md)
</dt> </dl>

 


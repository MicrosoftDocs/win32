---
description: Indicates an MCA, corrected machine check (CMC), or corrected platform error (CPE) information entry. This class is available only in 64-bit Windows systems.
ms.assetid: 4edbca20-2525-4e35-ab79-8cf421343144
title: MSMCAInfo_Entry class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSMCAInfo_Entry
- MSMCAInfo_Entry.Data
- MSMCAInfo_Entry.Length
api_type: 
- DllExport
api_location: 
- Wmiprov.dll
---

# MSMCAInfo\_Entry class

The **MSMCAInfo\_Entry** class indicates an MCA, corrected machine check (CMC), or corrected platform error (CPE) information entry. This class is available only in 64-bit Windows systems.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
class MSMCAInfo_Entry : MSMCAInfo
{
  uint8  Data[];
  uint32 Length;
};
```

## Members

The **MSMCAInfo\_Entry** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSMCAInfo\_Entry** class has these properties.

<dl> <dt>

**Data**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Integer array that contains a complete MCA error record as reported by the system abstraction layer (SAL). The SAL is code burned into ROM that the operating system calls to perform platform-dependent operations. It is similar to the BIOS on an x86 platform.

</dd> <dt>

**Length**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of bytes in the error record.

</dd> </dl>

## Remarks

The **MSMCAInfo\_Entry** class is derived from [**MSMCAInfo**](msmcainfo.md).

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

[**MSMCAInfo**](msmcainfo.md)
</dt> </dl>

 

 





---
title: MsftUal\_SystemId class
description: This is a class of property qualifiers that provides profile details of the local server and reflects changes if they are made.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ef28fe87-8f09-49cd-ae93-7040f5cc732e
ms.prod: windows-server-dev
ms.technology: user-access-logging
ms.tgt_platform: multiple
keywords:
- MsftUal_SystemId class User Access Logging
- MsftUal_SystemId class User Access Logging , described
topic_type:
- apiref
api_name:
- MsftUal_SystemId
- MsftUal_SystemId.CreationTime
- MsftUal_SystemId.SystemManufacturer
- MsftUal_SystemId.SystemProductName
- MsftUal_SystemId.PhysicalProcessorCount
- MsftUal_SystemId.CoresPerPhysicalProcessor
- MsftUal_SystemId.LogicalProcessorsPerPhysicalProcessor
- MsftUal_SystemId.MaximumMemory
- MsftUal_SystemId.SystemSMBIOSUUID
- MsftUal_SystemId.SystemSerialNumber
- MsftUal_SystemId.SystemDNSHostName
- MsftUal_SystemId.SystemDomainName
- MsftUal_SystemId.OSMajor
- MsftUal_SystemId.OSMinor
- MsftUal_SystemId.OSBuildNumber
- MsftUal_SystemId.OSPlatformId
- MsftUal_SystemId.OSSuiteMask
- MsftUal_SystemId.OSProductType
- MsftUal_SystemId.OSSerialNumber
- MsftUal_SystemId.OSCountryCode
- MsftUal_SystemId.OSCurrentTimeZone
- MsftUal_SystemId.OSDaylightInEffect
- MsftUal_SystemId.OSLastBootUpTime
- MsftUal_SystemId.ServicePackMajor
- MsftUal_SystemId.ServicePackMinor
api_location:
- UALProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MsftUal\_SystemId class

This is a class of property qualifiers that provides profile details of the local server and reflects changes if they are made.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Version("1"), dynamic, provider("UAL")]
class MsftUal_SystemId
{
  datetime CreationTime;
  string   SystemManufacturer;
  string   SystemProductName;
  uint32   PhysicalProcessorCount;
  uint32   CoresPerPhysicalProcessor;
  uint32   LogicalProcessorsPerPhysicalProcessor;
  uint64   MaximumMemory;
  string   SystemSMBIOSUUID;
  string   SystemSerialNumber;
  string   SystemDNSHostName;
  string   SystemDomainName;
  uint32   OSMajor;
  uint32   OSMinor;
  uint32   OSBuildNumber;
  uint32   OSPlatformId;
  uint32   OSSuiteMask;
  uint32   OSProductType;
  string   OSSerialNumber;
  string   OSCountryCode;
  sint16   OSCurrentTimeZone;
  boolean  OSDaylightInEffect;
  string   OSLastBootUpTime;
  uint32   ServicePackMajor;
  uint32   ServicePackMinor;
};
```

## Members

The **MsftUal\_SystemId** class has these types of members:

-   [Properties](#properties)

### Properties

The **MsftUal\_SystemId** class has these properties.

<dl> <dt>

**CoresPerPhysicalProcessor**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of cores for an instance of the physical processor in the system. For example, for a dual-core processor system, this property has a value of 2.

</dd> <dt>

**CreationTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date and time that the current operating system first became operational with this set of system identity properties. If the properties of a system change, then a new System Identity record is created.

</dd> <dt>

**LogicalProcessorsPerPhysicalProcessor**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of logical processors for an instance of a Hyper-Thread capable physical processor in the system. For example, in a Hyper-Thread quad-core processor system, this property has a value of 8.

</dd> <dt>

**MaximumMemory**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum system memory size (in bytes). For a virtual machine, this value represents what the hypervisor configured for the memory size of the virtual machine.

</dd> <dt>

**OSBuildNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The build number of the operating system.

</dd> <dt>

**OSCountryCode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The code for the country or region that an operating system uses. Values are based on international phone dialing prefixes.

</dd> <dt>

**OSCurrentTimeZone**
</dt> <dd> <dl> <dt>

Data type: **sint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number, in minutes, an operating system is offset from Greenwich mean time (GMT). The number is positive, negative, or zero.

</dd> <dt>

**OSDaylightInEffect**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If True, the daylight savings mode is ON.

</dd> <dt>

**OSLastBootUpTime**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The date and time the operating system was last restarted.

</dd> <dt>

**OSMajor**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The major portion of the version number of the operating system.

</dd> <dt>

**OSMinor**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The minor portion of the version number of the operating system.

</dd> <dt>

**OSPlatformId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An integer that represents the operating system platform. The possible values of the data property are "1" to indicate an unsupported Windows system and "2" to indicate a supported Windows system.

</dd> <dt>

**OSProductType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An enumeration type that identifies the operating system that you are running.

</dd> <dt>

**OSSerialNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The operating system product serial identification number.

</dd> <dt>

**OSSuiteMask**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The SuiteMask of the local system.

</dd> <dt>

**PhysicalProcessorCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of physical processors currently available on a system.

</dd> <dt>

**ServicePackMajor**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The major version number of the service pack.

</dd> <dt>

**ServicePackMinor**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The minor version number of the service pack.

</dd> <dt>

**SystemDNSHostName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The server name according to the domain name server (DNS).

</dd> <dt>

**SystemDomainName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the domain, or workgroup, to which the server belongs.

</dd> <dt>

**SystemManufacturer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the BIOS manufacturer.

</dd> <dt>

**SystemProductName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The product name specified in the system BIOS.

</dd> <dt>

**SystemSerialNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The unit identification for the local server.

</dd> <dt>

**SystemSMBIOSUUID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The SMBIOS reported universally unique identifier for this server unit.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\AccessLogging<br/>                                                         |
| MOF<br/>                      | <dl> <dt>Sum.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>UALProv.dll</dt> </dl> |



 

 






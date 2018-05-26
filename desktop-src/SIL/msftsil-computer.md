---
title: MsftSil\_Computer class
description: The MsftSil\_Computer WMI class retrieves system data about a server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 26fd08b3-5d2b-4571-bc14-1567be6755c0
ms.prod: windows-server-dev
ms.technology:
- software-inventory-logging
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MsftSil_Computer class Software Inventory Logging
- MsftSil_Computer class Software Inventory Logging , described
topic_type:
- apiref
api_name:
- MsftSil_Computer
- MsftSil_Computer.ChassisSerialNumber
- MsftSil_Computer.CollectedDateTime
- MsftSil_Computer.Model
- MsftSil_Computer.Name
- MsftSil_Computer.NumberOfCores
- MsftSil_Computer.NumberOfLogicalProcessors
- MsftSil_Computer.NumberOfProcessors
- MsftSil_Computer.OSName
- MsftSil_Computer.OSSku
- MsftSil_Computer.OSSuite
- MsftSil_Computer.OSSuiteMask
- MsftSil_Computer.OSVersion
- MsftSil_Computer.ProcessorFamily
- MsftSil_Computer.ProcessorManufacturer
- MsftSil_Computer.ProcessorName
- MsftSil_Computer.SystemManufacturer
- MsftSil_Computer.VmGuid
api_location:
- SILProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MsftSil\_Computer class

The **MsftSil\_Computer** WMI class retrieves system data about a server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.1"), dynamic, provider("silprovider"), AMENDMENT]
class MsftSil_Computer : MsftSil_Data
{
  string   ChassisSerialNumber;
  datetime CollectedDateTime;
  string   Model;
  string   Name;
  uint32   NumberOfCores;
  uint32   NumberOfLogicalProcessors;
  uint32   NumberOfProcessors;
  string   OSName;
  uint32   OSSku;
  uint32   OSSuite;
  uint32   OSSuiteMask;
  string   OSVersion;
  uint32   ProcessorFamily;
  string   ProcessorManufacturer;
  string   ProcessorName;
  string   SystemManufacturer;
  string   VmGuid;
};
```

## Members

The **MsftSil\_Computer** class has these types of members:

-   [Properties](#properties)

### Properties

The **MsftSil\_Computer** class has these properties.

<dl> <dt>

**ChassisSerialNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Retrieves the serial number on the chassis of the server.

</dd> <dt>

**CollectedDateTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Msft\_MiCompare\_IgnoreProperty**
</dt> </dl>

Retrieves the time and date the system data was collected.

</dd> <dt>

**Model**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Retrieves the model name of the server.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Retrieves the computer name that identifies the system.

</dd> <dt>

**NumberOfCores**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Retrieves the number of processor cores in the system.

</dd> <dt>

**NumberOfLogicalProcessors**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Retrieves the number of physical processors in the system.

</dd> <dt>

**NumberOfProcessors**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Retrieves the number of physical and virtual processors in the system.

</dd> <dt>

**OSName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Retrieves the name of the operating system (OS).

</dd> <dt>

**OSSku**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Retrieves the SKU of the OS.

</dd> <dt>

**OSSuite**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Retrieves the OS suite.

</dd> <dt>

**OSSuiteMask**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Retrieves the suite mask of the OS.

</dd> <dt>

**OSVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Retrieves the OS version.

</dd> <dt>

**ProcessorFamily**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Retrieves the name of the processor family.

</dd> <dt>

**ProcessorManufacturer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Retrieves the name of the manufacturer of the processor.

</dd> <dt>

**ProcessorName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Retrieves the name of the processor type.

</dd> <dt>

**SystemManufacturer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Retrieves the name of the server manufacturer.

</dd> <dt>

**VmGuid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property has been removed.

**Windows Server 2012 R2:** Retrieves the **GUID** of the virtual machine.

</dd> </dl>

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                          |
| Namespace<br/>                | Root\\InventoryLogging<br/>                                                          |
| MOF<br/>                      | <dl> <dt>SILProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SILProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MsftSil\_Data**](msftsil-data.md)
</dt> <dt>

[Software Inventory Logging WMI Data Provider Classes](software-inventory-logging-wmi-data-provider-classes.md)
</dt> </dl>

 

 






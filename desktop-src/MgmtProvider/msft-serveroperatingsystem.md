---
title: MSFT\_ServerOperatingSystem class
description: Represents the operating system of the server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 955414ea-7e66-4843-a15a-5687de067761
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_ServerOperatingSystem class
- MSFT_ServerOperatingSystem class, described
topic_type:
- apiref
api_name:
- MSFT_ServerOperatingSystem
- MSFT_ServerOperatingSystem.Name
- MSFT_ServerOperatingSystem.MajorVersion
- MSFT_ServerOperatingSystem.MinorVersion
- MSFT_ServerOperatingSystem.BuildNumber
- MSFT_ServerOperatingSystem.SPMajorVersion
- MSFT_ServerOperatingSystem.SPMinorVersion
- MSFT_ServerOperatingSystem.SKU
- MSFT_ServerOperatingSystem.Language
- MSFT_ServerOperatingSystem.Architecture
- MSFT_ServerOperatingSystem.SKUId
api_location:
- MgmtProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_ServerOperatingSystem class

Represents the operating system of the server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("mgmtprovider"), AMENDMENT]
class MSFT_ServerOperatingSystem
{
  string Name;
  uint32 MajorVersion;
  uint32 MinorVersion;
  uint32 BuildNumber;
  uint16 SPMajorVersion;
  uint16 SPMinorVersion;
  string SKU;
  string Language;
  uint8  Architecture;
  uint32 SKUId;
};
```

## Members

The **MSFT\_ServerOperatingSystem** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_ServerOperatingSystem** class has these properties.

<dl> <dt>

**Architecture**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The operating system's architecture.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="32-bit"></span><span id="32-BIT"></span>

**32-bit** (1)


</dt> <dd></dd> <dt>

<span id="64-bit"></span><span id="64-BIT"></span>

**64-bit** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**BuildNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The build number of the operating system.

</dd> <dt>

**Language**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The operating system locale name.

</dd> <dt>

**MajorVersion**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The major version number of the operating system.

</dd> <dt>

**MinorVersion**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The minor version number of the operating system.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The brand name of the operating system.

</dd> <dt>

**SKU**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Stock Keeping Unit name of the operating system.

</dd> <dt>

**SKUId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Stock Keeping Unit Id of the operating system.

</dd> <dt>

**SPMajorVersion**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The major version number of the operating system service pack installed.

</dd> <dt>

**SPMinorVersion**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The minor version number of the operating system service pack installed.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\Windows\\ServerManager<br/>                                                     |
| MOF<br/>                      | <dl> <dt>MgmtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MgmtProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**GetServerInventory method of MSFT\_ServerManagerTasks**](getserverinventory-msft-servermanagertasks.md)
</dt> </dl>

 

 






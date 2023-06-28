---
title: Win32\_InstalledStoreProgram class
description: The Win32\_InstalledStoreProgram class represents an installed Windows store application.
ms.assetid: 154c19c7-f2e5-48bd-b05b-3022e45f2aa4
keywords:
- Win32_InstalledStoreProgram class Application and Device Inventory Provider
- Win32_InstalledStoreProgram class Application and Device Inventory Provider , described
topic_type:
- apiref
api_name:
- Win32_InstalledStoreProgram
- Win32_InstalledStoreProgram.ProgramId
- Win32_InstalledStoreProgram.Name
- Win32_InstalledStoreProgram.Vendor
- Win32_InstalledStoreProgram.Version
- Win32_InstalledStoreProgram.Language
- Win32_InstalledStoreProgram.Architecture
api_location:
- Root\CIMv2
api_type:
- Schema
ms.technology: system-insights
ms.prod: windows-server
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# Win32\_InstalledStoreProgram class

The **Win32\_InstalledStoreProgram** class represents an installed Windows store application.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class Win32_InstalledStoreProgram
{
  string ProgramId;
  string Name;
  string Vendor;
  string Version;
  string Language;
  string Architecture;
};
```

## Members

The **Win32\_InstalledStoreProgram** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_InstalledStoreProgram** class has these properties.

<dl> <dt>

**Architecture**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The supported processor architectures for the Windows store application.

</dd> <dt>

**Language**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The supported languages for the Windows store application.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the Windows store application.

</dd> <dt>

**ProgramId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The unique identifier of the Windows store application.

</dd> <dt>

**Vendor**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The publisher of the Windows store application.

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The version of the Windows store application.

</dd> </dl>

## Requirements



|    Requirement                   |    Details                                 |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                 |
| Minimum supported server<br/> | None supported<br/>                                                            |
| Namespace<br/>                | Root\\CIMv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>Aeinv.mof</dt> </dl> |



 

 






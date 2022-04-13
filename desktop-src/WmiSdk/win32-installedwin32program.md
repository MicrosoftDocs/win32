---
title: Win32\_InstalledWin32Program class
description: The Win32\_InstalledWin32Program class represents an installed Win32 application.
ms.assetid: 2eef00da-8597-4852-b4fb-4276d05fd724
keywords:
- Win32_InstalledWin32Program class Application and Device Inventory Provider
- Win32_InstalledWin32Program class Application and Device Inventory Provider , described
topic_type:
- apiref
api_name:
- Win32_InstalledWin32Program
- Win32_InstalledWin32Program.ProgramId
- Win32_InstalledWin32Program.Name
- Win32_InstalledWin32Program.Vendor
- Win32_InstalledWin32Program.Version
- Win32_InstalledWin32Program.Language
- Win32_InstalledWin32Program.MsiPackageCode
- Win32_InstalledWin32Program.MsiProductCode
api_location:
- Root\CIMv2
api_type:
- Schema
ms.technology: system-insight
ms.prod: windows-server-dev
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# Win32\_InstalledWin32Program class

The **Win32\_InstalledWin32Program** class represents an installed Win32 application.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class Win32_InstalledWin32Program
{
  string ProgramId;
  string Name;
  string Vendor;
  string Version;
  string Language;
  string MsiPackageCode;
  string MsiProductCode;
};
```

## Members

The **Win32\_InstalledWin32Program** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_InstalledWin32Program** class has these properties.

<dl> <dt>

**Language**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The supported languages for the installed Win32 application.

</dd> <dt>

**MsiPackageCode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The MSI package code, if the Win32 application was installed using an MSI.

</dd> <dt>

**MsiProductCode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The MSI product code, if the Win32 application was installed using an MSI.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the installed Win32 application.

</dd> <dt>

**ProgramId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The unique identifier of the installed Win32 application. This value helps correlate **Win32\_InstalledWin32Program** with [**Win32\_InstalledProgramFramework**](win32-installedprogramframework.md).

</dd> <dt>

**Vendor**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The publisher of the installed Win32 application.

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The version of the installed Win32 application.

</dd> </dl>

## Requirements



|    Requirement           |  Details                    |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | None supported<br/>                                                            |
| Namespace<br/>                | Root\\CIMv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>Aeinv.mof</dt> </dl> |



 

 






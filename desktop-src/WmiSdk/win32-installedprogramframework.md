---
title: Win32\_InstalledProgramFramework class
description: The Win32\_InstalledProgramFramework class represents a technology framework that a Win32\_InstalledWin32Program instance is compiled against or uses at runtime.
ms.assetid: bb5c18c7-ec71-4579-8190-942de4fccd9e
keywords:
- Win32_InstalledProgramFramework class Application and Device Inventory Provider
- Win32_InstalledProgramFramework class Application and Device Inventory Provider , described
topic_type:
- apiref
api_name:
- Win32_InstalledProgramFramework
- Win32_InstalledProgramFramework.FrameworkName
- Win32_InstalledProgramFramework.FrameworkPublisher
- Win32_InstalledProgramFramework.FrameworkVersion
- Win32_InstalledProgramFramework.FrameworkVersionActual
- Win32_InstalledProgramFramework.ProgramId
- Win32_InstalledProgramFramework.IsPrivate
api_location:
- Root\CIMv2
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# Win32\_InstalledProgramFramework class

The **Win32\_InstalledProgramFramework** class represents a technology framework that a [**Win32\_InstalledWin32Program**](win32-installedwin32program.md) instance is compiled against or uses at runtime. Frameworks that this class can currently report are OpenSSL, Visual Basic, Visual C++ .Net, Visual C++, Java (only detects the java runtime binaries) and CLR.

> [!Note]  
> The set of frameworks that this class can detect may be updated over time.

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class Win32_InstalledProgramFramework
{
  string  FrameworkName;
  string  FrameworkPublisher;
  string  FrameworkVersion;
  string  FrameworkVersionActual;
  string  ProgramId;
  boolean IsPrivate;
};
```

## Members

The **Win32\_InstalledProgramFramework** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_InstalledProgramFramework** class has these properties.

<dl> <dt>

**FrameworkName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The name of the framework that the application identified by **ProgramId** depends on.

</dd> <dt>

**FrameworkPublisher**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The publisher of the framework.

</dd> <dt>

**FrameworkVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The version of the framework that the application has a dependency on.

</dd> <dt>

**FrameworkVersionActual**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The version of the framework that the application actually uses at runtime, if the framework can be detected.

</dd> <dt>

**IsPrivate**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

TRUE if the application bundles a private copy of the framework.

</dd> <dt>

**ProgramId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The unique identifier of the [**Win32\_InstalledWin32Program**](win32-installedwin32program.md) instance, with which the framework data is associated.

</dd> </dl>

## Requirements



|                Requirement                |      Details          |
|--------------------------------|----------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>    |
| Minimum supported server<br/> | None supported<br/>|
| Namespace<br/>                | Root\\CIMv2<br/    |
| MOF<br/>                      | <dl> <dt>Aeinv.mof</dt> </dl> |



 

 






---
title: Win32_RDMSPublishedApplication class
description: Manages a published application.
ms.assetid: 7a529f1d-1aaf-42fb-8469-92d38a7b0ffc
ms.tgt_platform: multiple
keywords:
- Win32_RDMSPublishedApplication class Remote Desktop Services
- Win32_RDMSPublishedApplication class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_RDMSPublishedApplication
- Win32_RDMSPublishedApplication.AppAlias
- Win32_RDMSPublishedApplication.PoolName
- Win32_RDMSPublishedApplication.DisplayName
- Win32_RDMSPublishedApplication.ShowInPortal
- Win32_RDMSPublishedApplication.SecurityDescriptor
- Win32_RDMSPublishedApplication.AppPath
- Win32_RDMSPublishedApplication.VirtualPath
- Win32_RDMSPublishedApplication.CommandLineSetting
- Win32_RDMSPublishedApplication.RequiredCommandLine
- Win32_RDMSPublishedApplication.Folder
- Win32_RDMSPublishedApplication.IconPath
- Win32_RDMSPublishedApplication.IconIndex
- Win32_RDMSPublishedApplication.IconContents
api_location:
- RDMS.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_RDMSPublishedApplication class

Manages a published application.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("Win32_RDManagement_Prov"), AMENDMENT]
class Win32_RDMSPublishedApplication
{
  string  AppAlias;
  string  PoolName;
  string  DisplayName;
  boolean ShowInPortal;
  string  SecurityDescriptor;
  string  AppPath;
  string  VirtualPath;
  uint32  CommandLineSetting;
  string  RequiredCommandLine;
  string  Folder;
  string  IconPath;
  sint32  IconIndex;
  uint8   IconContents[];
};
```

## Members

The **Win32\_RDMSPublishedApplication** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_RDMSPublishedApplication** class has these properties.

<dl> <dt>

**AppAlias**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Gets and sets the alias of the application.

</dd> <dt>

**AppPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets the path to the application.

</dd> <dt>

**CommandLineSetting**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets the command line setting for the application.

This property can be set to one of the following values:

<dt>

<span id="DoNotAllow"></span><span id="donotallow"></span><span id="DONOTALLOW"></span>

<span id="DoNotAllow"></span><span id="donotallow"></span><span id="DONOTALLOW"></span>**DoNotAllow** (0)


</dt> <dd>

Do not allow command line arguments.

</dd> <dt>

<span id="Allow"></span><span id="allow"></span><span id="ALLOW"></span>

<span id="Allow"></span><span id="allow"></span><span id="ALLOW"></span>**Allow** (1)


</dt> <dd>

Allow command line arguments.

</dd> <dt>

<span id="Require"></span><span id="require"></span><span id="REQUIRE"></span>

<span id="Require"></span><span id="require"></span><span id="REQUIRE"></span>**Require** (2)


</dt> <dd>

Require command line arguments.

</dd> </dl>

</dd> <dt>

**DisplayName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets the display name of the application.

</dd> <dt>

**Folder**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets the path to the application.

</dd> <dt>

**IconContents**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets an array that contains the application icon.

</dd> <dt>

**IconIndex**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets the index for the application icon.

</dd> <dt>

**IconPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets the path to the icon for this application.

</dd> <dt>

**PoolName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Gets and sets the name of the application pool of the application.

</dd> <dt>

**RequiredCommandLine**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets the command line arguments that are required for the application

</dd> <dt>

**SecurityDescriptor**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**optional**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

Gets and sets the security descriptor that controls access to the application, in security descriptor definition language (SDDL) format.

</dd> <dt>

**ShowInPortal**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether to display the application in Terminal Services Web Access (TS Web Access). **TRUE** to display the application in TS Web Access; otherwise, **FALSE**.

</dd> <dt>

**VirtualPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets the virtual path to the application.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\cimv2\\rdms<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>         |



## See also

<dl> <dt>

[Remote Desktop Management Services Provider](rdms-api-reference.md)
</dt> </dl>

 


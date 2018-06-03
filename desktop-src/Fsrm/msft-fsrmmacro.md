---
title: MSFT\_FSRMMacro class
description: Represents a FSRM macro object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6058e27f-2157-465e-9881-99c28b282cb6
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- MSFT_FSRMMacro class File Server Resource Manager
- MSFT_FSRMMacro class File Server Resource Manager , described
topic_type:
- apiref
api_name:
- MSFT_FSRMMacro
- MSFT_FSRMMacro.Type
- MSFT_FSRMMacro.Name
- MSFT_FSRMMacro.Description
api_location:
- SrmSvc.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_FSRMMacro class

Represents a FSRM macro object.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("FSRMWmiProvider")]
class MSFT_FSRMMacro
{
  uint32 Type;
  string Name;
  string Description;
};
```

## Members

The **MSFT\_FSRMMacro** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_FSRMMacro** class has these properties.

<dl> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Description of the macro.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Name of the macro.

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Represents the type of the object that this macro can use. Required.

<dt>

<span id="Quota"></span><span id="quota"></span><span id="QUOTA"></span>

<span id="Quota"></span><span id="quota"></span><span id="QUOTA"></span>**Quota** (1)


</dt> <dd>

The object is a quota or quota template object.

</dd> <dt>

<span id="FileScreen"></span><span id="filescreen"></span><span id="FILESCREEN"></span>

<span id="FileScreen"></span><span id="filescreen"></span><span id="FILESCREEN"></span>**FileScreen** (2)


</dt> <dd>

The object is a File Screen object.

</dd> <dt>

<span id="FileManagementJob"></span><span id="filemanagementjob"></span><span id="FILEMANAGEMENTJOB"></span>

<span id="FileManagementJob"></span><span id="filemanagementjob"></span><span id="FILEMANAGEMENTJOB"></span>**FileManagementJob** (3)


</dt> <dd>

The object is a File Management Job object.

</dd> <dt>

<span id="Adr"></span><span id="adr"></span><span id="ADR"></span>

<span id="Adr"></span><span id="adr"></span><span id="ADR"></span>**Adr** (4)


</dt> <dd>

The object is an Access Denied Remediation (ADR) object.

</dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\FSRM<br/>                                                 |
| MOF<br/>                      | <dl> <dt>MSFT\_FSRM.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SrmSvc.dll</dt> </dl>     |



## See also

<dl> <dt>

[FSRM WMI Classes](fsrm-wmi-classes.md)
</dt> </dl>

 

 






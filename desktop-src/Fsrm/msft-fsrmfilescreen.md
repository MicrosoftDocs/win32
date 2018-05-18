---
title: MSFT\_FSRMFileScreen class
description: Used to configure a file screen that blocks groups of files from being saved to the specified directory.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '86ee74e0-64d5-478a-8150-0f4b37e56694'
ms.prod: 'windows-server-dev'
ms.technology: 'file-server-resource-manager'
ms.tgt_platform: multiple
keywords: ["MSFT_FSRMFileScreen class File Server Resource Manager", "MSFT_FSRMFileScreen class File Server Resource Manager , described"]
topic_type:
- apiref
api_name:
- MSFT_FSRMFileScreen
- MSFT_FSRMFileScreen.Path
- MSFT_FSRMFileScreen.Description
- MSFT_FSRMFileScreen.IncludeGroup
- MSFT_FSRMFileScreen.Active
- MSFT_FSRMFileScreen.Notification
- MSFT_FSRMFileScreen.Template
- MSFT_FSRMFileScreen.MatchesTemplate
api_location:
- SrmSvc.dll
api_type:
- DllExport
---

# MSFT\_FSRMFileScreen class

Used to configure a file screen that blocks groups of files from being saved to the specified directory.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("FSRMWmiProvider")]
class MSFT_FSRMFileScreen
{
  string          Path;
  string          Description;
  string          IncludeGroup[];
  boolean         Active;
  MSFT_FSRMAction Notification[];
  string          Template;
  boolean         MatchesTemplate;
};
```

## Members

The **MSFT\_FSRMFileScreen** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_FSRMFileScreen** class has these methods.



| Method                                     | Description                                                                                                                              |
|:-------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------|
| [**Reset**](msft-fsrmfilescreen-reset.md) | The indicated file screen will have all its default settings for all parameters reset with those from the specified template.<br/> |



 

### Properties

The **MSFT\_FSRMFileScreen** class has these properties.

<dl> <dt>

**Active**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **True**, the server will fail any IO operation that violates the file screen. If **False**, the server will not fail violating IO operations but will still run any action associated with the file screen.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The description of the file screen.

</dd> <dt>

**IncludeGroup**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array of strings containing the names of the file groups that contain the file name patterns used to specify the files that are blocked by this screen.

</dd> <dt>

**MatchesTemplate**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, the property values of this file screen match those values of the template from which it was derived.

</dd> <dt>

**Notification**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_FSRMAction** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**MSFT\_FSRMAction**](msft-fsrmaction.md)")
</dt> </dl>

An array of instance of the [**MSFT\_FSRMAction**](msft-fsrmaction.md) class that represents the actions performed when the file screen is violated.

</dd> <dt>

**Path**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The path of the directory to which the file screen object applies.

</dd> <dt>

**Template**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of the file screen template that will be applied to this file screen. The string is limited to 4,000 characters.

</dd> </dl>

## Remarks

A file screen limits the types of files that the system or any user can store in a directory. When a restricted file is detected, the FSRM server performs the specified actions (see [**IFsrmFileScreenBase::CreateAction**](ifsrmfilescreenbase-createaction.md)).

The file screen applies to future files—the screen is not applied retroactively. To list the files in the directory that violate the screen, create a report job that lists files by type.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\FSRM<br/>                                                 |
| MOF<br/>                      | <dl> <dt>MSFT\_FSRM.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SrmSvc.dll</dt> </dl>     |



## See also

<dl> <dt>

[FSRM WMI Classes](fsrm-wmi-classes.md)
</dt> </dl>

 

 






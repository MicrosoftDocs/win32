---
title: MSFT\_FSRMFileScreenTemplate class
description: Used to configure templates from which new file screens can be derived.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: be4f3a6a-280f-4b0f-afdf-ce1ee7933018
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- MSFT_FSRMFileScreenTemplate class File Server Resource Manager
- MSFT_FSRMFileScreenTemplate class File Server Resource Manager , described
topic_type:
- apiref
api_name:
- MSFT_FSRMFileScreenTemplate
- MSFT_FSRMFileScreenTemplate.Name
- MSFT_FSRMFileScreenTemplate.Description
- MSFT_FSRMFileScreenTemplate.IncludeGroup
- MSFT_FSRMFileScreenTemplate.Active
- MSFT_FSRMFileScreenTemplate.Notification
- MSFT_FSRMFileScreenTemplate.UpdateDerived
- MSFT_FSRMFileScreenTemplate.UpdateDerivedMatching
api_location:
- SrmSvc.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_FSRMFileScreenTemplate class

Used to configure templates from which new file screens can be derived. Templates are identified by a name and are used to simplify configuration of file screens.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("FSRMWmiProvider")]
class MSFT_FSRMFileScreenTemplate
{
  string          Name;
  string          Description;
  string          IncludeGroup[];
  boolean         Active;
  MSFT_FSRMAction Notification[];
  boolean         UpdateDerived;
  boolean         UpdateDerivedMatching;
};
```

## Members

The **MSFT\_FSRMFileScreenTemplate** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_FSRMFileScreenTemplate** class has these properties.

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

A string up to 1KB in size. Optional. The default value is an empty string.

</dd> <dt>

**IncludeGroup**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array of strings containing the names of the file groups that contain the file name patterns used to specify the files that are blocked by this screen. The total combined length of the strings must be under 10KB. This parameter is required.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The name of the file screen template.

</dd> <dt>

**Notification**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_FSRMAction** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**MSFT\_FSRMAction**](msft-fsrmaction.md)")
</dt> </dl>

An array of instances of the [**MSFT\_FSRMAction**](msft-fsrmaction.md) class that represents the actions performed when the file screen is violated.

</dd> <dt>

**UpdateDerived**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Apply changes to all derived file screens, whether their properties match the templates or not.

</dd> <dt>

**UpdateDerivedMatching**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Applies changes to derived file screens only if the file screen's properties match the file screen template's properties.

Note that the comparison is made against the file screen template as it exists in the database, not a local copy that has not been committed.

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

 

 






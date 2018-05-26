---
title: MSFT\_FSRMFileGroup class
description: Used to define a group of files based on one or more file name patterns.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c090da1e-df74-4dba-aaa0-15defa85d604
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- MSFT_FSRMFileGroup class File Server Resource Manager
- MSFT_FSRMFileGroup class File Server Resource Manager , described
topic_type:
- apiref
api_name:
- MSFT_FSRMFileGroup
- MSFT_FSRMFileGroup.Name
- MSFT_FSRMFileGroup.Description
- MSFT_FSRMFileGroup.IncludePattern
- MSFT_FSRMFileGroup.ExcludePattern
api_location:
- SrmSvc.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_FSRMFileGroup class

Used to define a group of files based on one or more file name patterns. A file group is a logical collection of file name patterns identified by name that is used to define file screens and file screen exceptions. File group definitions may also be used for generating storage report jobs based on file type.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("FSRMWmiProvider")]
class MSFT_FSRMFileGroup
{
  string Name;
  string Description;
  string IncludePattern[];
  string ExcludePattern[];
};
```

## Members

The **MSFT\_FSRMFileGroup** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_FSRMFileGroup** class has these properties.

<dl> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Describes the file group. Can be up to 10KB in size. The default value is an empty string.

</dd> <dt>

**ExcludePattern**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array of pattern strings that may include '\*' and '?' as wildcard characters. The strings can be up to 1KB in size. This parameter is required.

</dd> <dt>

**IncludePattern**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array of pattern strings that may include '\*' and '?' as wildcard characters. The strings can be up to 1KB in size. This parameter is required.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The name of the file group. Can be up to 1KB in size. The value must be unique, and is required.

</dd> </dl>

## Remarks

A file group is formed by including all files that match the wildcard patterns in **IncludePattern** and then excluding all files that match the wildcard patterns in **ExcludePattern**. For example, to list all files except for "*examplename*", set **IncludePattern** to "\*.\*" and set **ExcludePattern** to "*examplename*".

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

 

 






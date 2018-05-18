---
title: MSFT\_FSRMFileScreenException class
description: Used to configure an exception that excludes the specified files from the file screening process.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1787aab2-b315-418c-81bf-1e42198c8780'
ms.prod: 'windows-server-dev'
ms.technology: 'file-server-resource-manager'
ms.tgt_platform: multiple
keywords: ["MSFT_FSRMFileScreenException class File Server Resource Manager", "MSFT_FSRMFileScreenException class File Server Resource Manager , described"]
topic_type:
- apiref
api_name:
- MSFT_FSRMFileScreenException
- MSFT_FSRMFileScreenException.Path
- MSFT_FSRMFileScreenException.Description
- MSFT_FSRMFileScreenException.IncludeGroup
api_location:
- SrmSvc.dll
api_type:
- DllExport
---

# MSFT\_FSRMFileScreenException class

Used to configure an exception that excludes the specified files from the file screening process. This allows the files of a file group to be saved in the directory when a file screen that applies to the directory would otherwise prevent the file from being saved in the directory.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("FSRMWmiProvider")]
class MSFT_FSRMFileScreenException
{
  string Path;
  string Description = "";
  string IncludeGroup[];
};
```

## Members

The **MSFT\_FSRMFileScreenException** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_FSRMFileScreenException** class has these properties.

<dl> <dt>

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

An array of strings, each containing the valid name of a file group. The total combined size must be under 10KB. This parameter is required.

</dd> <dt>

**Path**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The path that is associated with this file screen exception.

</dd> </dl>

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

 

 






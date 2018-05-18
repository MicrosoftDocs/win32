---
title: MSFT\_FSRMAutoQuota class
description: Creates a new AutoQuota on the server with the provided configuration and returns the FSRM quota object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '3941d07c-67e3-4763-8113-31fc156c9bd0'
ms.prod: 'windows-server-dev'
ms.technology: 'file-server-resource-manager'
ms.tgt_platform: multiple
keywords: ["MSFT_FSRMAutoQuota class File Server Resource Manager", "MSFT_FSRMAutoQuota class File Server Resource Manager , described"]
topic_type:
- apiref
api_name:
- MSFT_FSRMAutoQuota
- MSFT_FSRMAutoQuota.Path
- MSFT_FSRMAutoQuota.Size
- MSFT_FSRMAutoQuota.SoftLimit
- MSFT_FSRMAutoQuota.Disabled
- MSFT_FSRMAutoQuota.Template
- MSFT_FSRMAutoQuota.UpdateDerived
- MSFT_FSRMAutoQuota.UpdateDerivedMatching
- MSFT_FSRMAutoQuota.Threshold
api_location:
- SrmSvc.dll
api_type:
- DllExport
---

# MSFT\_FSRMAutoQuota class

Creates a new **AutoQuota** on the server with the provided configuration and returns the FSRM quota object.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("FSRMWmiProvider")]
class MSFT_FSRMAutoQuota
{
  string                  Path;
  uint64                  Size;
  boolean                 SoftLimit;
  boolean                 Disabled;
  string                  Template;
  boolean                 UpdateDerived;
  boolean                 UpdateDerivedMatching;
  MSFT_FSRMQuotaThreshold Threshold[];
};
```

## Members

The **MSFT\_FSRMAutoQuota** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_FSRMAutoQuota** class has these properties.

<dl> <dt>

**Disabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If set, the server will not track quota data for the quota and will not run any action associated with quota thresholds. The default value is false.

</dd> <dt>

**Path**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A required string that contains a valid local path to a folder. The value length cannot exceed the **MAX\_PATH** value.

</dd> <dt>

**Size**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Represents the quota limit, in bytes, for the auto quota. If the **Template** property is not provided then the **Size** property must be provided.

</dd> <dt>

**SoftLimit**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If this flag is set, the server will not fail violating IO operations but will still run any action associated with the quota thresholds. If this flag is not set, the server will fail an IO operation that causes the disk space usage to exceed the quota limit.

</dd> <dt>

**Template**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A quota template currently located on the server. Required. May not exceed 1KB.

</dd> <dt>

**Threshold**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_FSRMQuotaThreshold** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**MSFT\_FSRMQuotaThreshold**](msft-fsrmquotathreshold.md)")
</dt> </dl>

An instance of the [**MSFT\_FSRMQuotaThreshold**](msft-fsrmquotathreshold.md) class that represents the threshold.

</dd> <dt>

**UpdateDerived**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Apply changes to all derived objects, whether their properties match the template's or not.

</dd> <dt>

**UpdateDerivedMatching**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Applies changes to derived objects only if the object's properties match the template's properties.

Note that the comparison is made against the template as it exists in the database, not your local copy that has not been committed yet.

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
</dt> <dt>

[**IFsrmAutoApplyQuota**](ifsrmautoapplyquota.md)
</dt> </dl>

 

 






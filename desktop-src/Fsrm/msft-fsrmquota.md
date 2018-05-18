---
title: MSFT\_FSRMQuota class
description: Used to define a quota for a specified directory and to retrieve use statistics.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '9308f1de-ba8e-45f5-81ec-d8203839ee79'
ms.prod: 'windows-server-dev'
ms.technology: 'file-server-resource-manager'
ms.tgt_platform: multiple
keywords: ["MSFT_FSRMQuota class File Server Resource Manager", "MSFT_FSRMQuota class File Server Resource Manager , described"]
topic_type:
- apiref
api_name:
- MSFT_FSRMQuota
- MSFT_FSRMQuota.Path
- MSFT_FSRMQuota.Description
- MSFT_FSRMQuota.Size
- MSFT_FSRMQuota.SoftLimit
- MSFT_FSRMQuota.Disabled
- MSFT_FSRMQuota.Template
- MSFT_FSRMQuota.MatchesTemplate
- MSFT_FSRMQuota.Usage
- MSFT_FSRMQuota.PeakUsage
- MSFT_FSRMQuota.Threshold
api_location:
- SrmSvc.dll
api_type:
- DllExport
---

# MSFT\_FSRMQuota class

Used to define a quota for a specified directory and to retrieve use statistics.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("FSRMWmiProvider")]
class MSFT_FSRMQuota
{
  string                  Path;
  string                  Description = "";
  uint64                  Size;
  boolean                 SoftLimit = False;
  boolean                 Disabled = False;
  string                  Template;
  boolean                 MatchesTemplate;
  uint64                  Usage;
  uint64                  PeakUsage;
  MSFT_FSRMQuotaThreshold Threshold[] = {};
};
```

## Members

The **MSFT\_FSRMQuota** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_FSRMQuota** class has these methods.



| Method                                  | Description                                                                           |
|:----------------------------------------|:--------------------------------------------------------------------------------------|
| [**Reset**](msft-fsrmquota-reset.md)   | Applies the property values of the specified quota template to this quota.<br/> |
| [**Update**](msft-fsrmquota-update.md) | Starts a quota scan on the specified path.<br/>                                 |



 

### Properties

The **MSFT\_FSRMQuota** class has these properties.

<dl> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A string up to 1KB in size. Optional. The default value is an empty string.

</dd> <dt>

**Disabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **True**, the quota is disabled. The default value is **False**.

</dd> <dt>

**MatchesTemplate**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, the property values of this quota match those values of the template from which it was derived.

</dd> <dt>

**Path**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A string that represents a valid local path to a folder. Must not exceed the value of **MAX\_PATH**. Required.

</dd> <dt>

**PeakUsage**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The highest amount of disk space usage charged to this quota.

</dd> <dt>

**Size**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The size of the quota. If the **Template** property is not provided then the **Size** property must be provided.

</dd> <dt>

**SoftLimit**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **True**, the quota is a soft limit. If **False**, the quota is a hard limit. The default value is **False**. Optional.

</dd> <dt>

**Template**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A valid quota template name. Up to 1KB in size. Optional.

</dd> <dt>

**Threshold**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_FSRMQuotaThreshold** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**MSFT\_FSRMQuotaThreshold**](msft-fsrmquotathreshold.md)")
</dt> </dl>

A list of [**MSFT\_FSRMQuotaThreshold**](msft-fsrmquotathreshold.md) instances representing quota threshold objects with no more than 16 entries. The default value is an empty list.

</dd> <dt>

**Usage**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current amount of disk space usage charged to this quota.

</dd> </dl>

## Remarks

A quota limits the amount of data that the system or any user can store in a directory.

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

 

 






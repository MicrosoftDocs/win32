---
title: MSFT\_FSRMQuotaTemplate class
description: Used to configure templates from which new quota objects can be derived.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 59931c82-cba3-4b1b-aa8e-7c528db07755
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- MSFT_FSRMQuotaTemplate class File Server Resource Manager
- MSFT_FSRMQuotaTemplate class File Server Resource Manager , described
topic_type:
- apiref
api_name:
- MSFT_FSRMQuotaTemplate
- MSFT_FSRMQuotaTemplate.Name
- MSFT_FSRMQuotaTemplate.Description
- MSFT_FSRMQuotaTemplate.Size
- MSFT_FSRMQuotaTemplate.SoftLimit
- MSFT_FSRMQuotaTemplate.UpdateDerived
- MSFT_FSRMQuotaTemplate.UpdateDerivedMatching
- MSFT_FSRMQuotaTemplate.Threshold
api_location:
- SrmSvc.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_FSRMQuotaTemplate class

Used to configure templates from which new quota objects can be derived. Templates are identified by a name and are used to simplify the configuration of directory quotas.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("FSRMWmiProvider")]
class MSFT_FSRMQuotaTemplate
{
  string                  Name;
  string                  Description = "";
  uint64                  Size;
  boolean                 SoftLimit = False;
  boolean                 UpdateDerived;
  boolean                 UpdateDerivedMatching;
  MSFT_FSRMQuotaThreshold Threshold[] = {};
};
```

## Members

The **MSFT\_FSRMQuotaTemplate** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_FSRMQuotaTemplate** class has these properties.

<dl> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A string up to 1KB in size. Optional. The default value is an empty string.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A unique string that represents a quota template on the server. May be up to 1KB in size. Required.

</dd> <dt>

**Size**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The size of the quota. Required.

</dd> <dt>

**SoftLimit**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **True**, the quota is a soft limit. If **False**, the quota is a hard limit. The default value is **False**. Optional.

</dd> <dt>

**Threshold**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_FSRMQuotaThreshold** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**MSFT\_FSRMQuotaThreshold**](msft-fsrmquotathreshold.md)")
</dt> </dl>

A list of instance of the [**MSFT\_FSRMQuotaThreshold**](msft-fsrmquotathreshold.md) class representing quota threshold objects with no more than 16 entries. Optional. The default value is an empty list.

</dd> <dt>

**UpdateDerived**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Apply changes to all derived quotas, whether their properties match the templates or not.

</dd> <dt>

**UpdateDerivedMatching**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **True**, applies changes to derived quotas only if the quota's properties match the quota template's properties.

Note that the comparison is made against the quota template as it exists in the database, not a local copy that has not been committed.

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

 

 






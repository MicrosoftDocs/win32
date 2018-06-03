---
title: MSFT\_FSRMQuotaThreshold class
description: Represents a quota threshold and the actions that will be taken when the threshold is reached.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e5e98b6b-addc-4b38-8556-fca3423d23fd
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- MSFT_FSRMQuotaThreshold class File Server Resource Manager
- MSFT_FSRMQuotaThreshold class File Server Resource Manager , described
topic_type:
- apiref
api_name:
- MSFT_FSRMQuotaThreshold
- MSFT_FSRMQuotaThreshold.Percentage
- MSFT_FSRMQuotaThreshold.Action
api_location:
- SrmSvc.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_FSRMQuotaThreshold class

Represents a quota threshold and the actions that will be taken when the threshold is reached.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("FSRMWmiProvider")]
class MSFT_FSRMQuotaThreshold
{
  uint32          Percentage;
  MSFT_FSRMAction Action[];
};
```

## Members

The **MSFT\_FSRMQuotaThreshold** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_FSRMQuotaThreshold** class has these methods.



| Method                                                             | Description                                                                                           |
|:-------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------|
| [**CreateThreshold**](msft-fsrmquotathreshold-createthreshold.md) | Creates a **MSFT\_FSRMQuotaThreshold** instance representing a new quota threshold object.<br/> |



 

### Properties

The **MSFT\_FSRMQuotaThreshold** class has these properties.

<dl> <dt>

**Action**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_FSRMAction** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**MSFT\_FSRMAction**](msft-fsrmaction.md)")
</dt> </dl>

An array of instances of the [**MSFT\_FSRMAction**](msft-fsrmaction.md) class representing action types. Only one notification per type is allowed.

</dd> <dt>

**Percentage**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A number that represents of the percentage of used space from the available space that can be reached during a file operation.

Range: 1 250

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

 

 






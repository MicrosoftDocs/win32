---
title: MSFT\_FSRMMgmtPropertyValue class
description: Represents a FSRM management property name/value pair.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c2749616-6567-4c21-a64e-0847152629de
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- MSFT_FSRMMgmtPropertyValue class File Server Resource Manager
- MSFT_FSRMMgmtPropertyValue class File Server Resource Manager , described
topic_type:
- apiref
api_name:
- MSFT_FSRMMgmtPropertyValue
- MSFT_FSRMMgmtPropertyValue.Name
- MSFT_FSRMMgmtPropertyValue.Value
api_location:
- SrmSvc.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_FSRMMgmtPropertyValue class

Represents a FSRM management property name/value pair.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("FSRMWmiProvider")]
class MSFT_FSRMMgmtPropertyValue
{
  string Name;
  string Value;
};
```

## Members

The **MSFT\_FSRMMgmtPropertyValue** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_FSRMMgmtPropertyValue** class has these properties.

<dl> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the FSRM management property.

</dd> <dt>

**Value**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The value of the FSRM management property.

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

 

 






---
title: GetMgmtProperty method of the MSFT\_FSRMMgmtProperty class
description: Retrieves management properties that meet the specified criteria.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c944e50e-93d0-4f34-8230-45461b085b45
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- GetMgmtProperty method File Server Resource Manager
- GetMgmtProperty method File Server Resource Manager , MSFT_FSRMMgmtProperty class
- MSFT_FSRMMgmtProperty class File Server Resource Manager , GetMgmtProperty method
topic_type:
- apiref
api_name:
- MSFT_FSRMMgmtProperty.GetMgmtProperty
api_location:
- SrmSvc.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetMgmtProperty method of the MSFT\_FSRMMgmtProperty class

Retrieves management properties that meet the specified criteria.

## Syntax


```mof
uint64 GetMgmtProperty(
  [in]  string                Namespace,
  [in]  string                Name,
  [in]  boolean               Recurse,
  [in]  boolean               Effective,
  [out] MSFT_FSRMMgmtProperty Property[]
);
```



## Parameters

<dl> <dt>

*Namespace* \[in\]
</dt> <dd>

A string representing a local path to a folder or a folder of the format "&lt;Volume&gt;:\\path". Must not exceed the value of **MAX\_PATH**. Optional.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

A string up to 1KB in size. Optional.

</dd> <dt>

*Recurse* \[in\]
</dt> <dd>

If **True**, retrieves management properties for all folders containing management properties within the path. The default value is **False**. Optional.

</dd> <dt>

*Effective* \[in\]
</dt> <dd>

If **True**, retrieves the management property for the nearest folder with the requested property set. The default value is **False**. Optional.

</dd> <dt>

*Property* \[out\]
</dt> <dd>

Returns an array of [**MSFT\_FSRMMgmtProperty**](msft-fsrmmgmtproperty.md) instances representing the selected management properties.

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

[**MSFT\_FSRMMgmtProperty**](msft-fsrmmgmtproperty.md)
</dt> </dl>

 

 






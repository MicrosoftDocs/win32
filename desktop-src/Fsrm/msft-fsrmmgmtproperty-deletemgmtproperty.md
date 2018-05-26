---
title: DeleteMgmtProperty method of the MSFT\_FSRMMgmtProperty class
description: Deletes management properties.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e3d4ceb1-3078-4fb6-a1d9-94416cf043b1
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- DeleteMgmtProperty method File Server Resource Manager
- DeleteMgmtProperty method File Server Resource Manager , MSFT_FSRMMgmtProperty class
- MSFT_FSRMMgmtProperty class File Server Resource Manager , DeleteMgmtProperty method
topic_type:
- apiref
api_name:
- MSFT_FSRMMgmtProperty.DeleteMgmtProperty
api_location:
- SrmSvc.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DeleteMgmtProperty method of the MSFT\_FSRMMgmtProperty class

Deletes management properties.

## Syntax


```mof
uint64 DeleteMgmtProperty(
  [in] string  Namespace,
  [in] string  Name,
  [in] boolean Recurse
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

A string up to 1KB in size. Must be a valid name of a classification property marked for management on the server. Required.

</dd> <dt>

*Recurse* \[in\]
</dt> <dd>

If **True**, will remove the specified property from the folder specified in the *Namespace* parameter and all subdirectories of that folder. If **False**, will remove the specified property from the folder specified in the *Namespace* parameter and all subdirectories of that folder. If the *Namespace* parameter is not specified then the *Recurse* parameter is ignored and all of the named properties will be removed from the server..

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

 

 






---
title: SetMgmtProperty method of the MSFT\_FSRMMgmtProperty class
description: Sets management properties.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1bf0250a-4729-4034-b08b-096d74c6bfe8
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- SetMgmtProperty method File Server Resource Manager
- SetMgmtProperty method File Server Resource Manager , MSFT_FSRMMgmtProperty class
- MSFT_FSRMMgmtProperty class File Server Resource Manager , SetMgmtProperty method
topic_type:
- apiref
api_name:
- MSFT_FSRMMgmtProperty.SetMgmtProperty
api_location:
- SrmSvc.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetMgmtProperty method of the MSFT\_FSRMMgmtProperty class

Sets management properties.

## Syntax


```mof
uint64 SetMgmtProperty(
  [in]  string                Namespace,
  [in]  string                Name,
  [in]  string                Value,
  [out] MSFT_FSRMMgmtProperty Property[]
);
```



## Parameters

<dl> <dt>

*Namespace* \[in\]
</dt> <dd>

A string representing a local path to a folder. Must not exceed the value of **MAX\_PATH**. Required.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

A string up to 1KB in size. Must be a valid name of a classification property marked for management on the server. Required.

</dd> <dt>

*Value* \[in\]
</dt> <dd>

Value to assign to the classification property specified in the *Name* parameter.

</dd> <dt>

*Property* \[out\]
</dt> <dd>

Returns an array of instances of the [**MSFT\_FSRMMgmtProperty**](msft-fsrmmgmtproperty.md) class representing the affected management properties.

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

 

 






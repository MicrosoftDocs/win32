---
title: Reset method of the MSFT\_FSRMFileScreen class
description: Resets the default settings for all file screen parameters with those from the specified template.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: be9f0aae-a21b-4c68-8de6-16d412d0e672
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- Reset method File Server Resource Manager
- Reset method File Server Resource Manager , MSFT_FSRMFileScreen class
- MSFT_FSRMFileScreen class File Server Resource Manager , Reset method
topic_type:
- apiref
api_name:
- MSFT_FSRMFileScreen.Reset
api_location:
- SrmSvc.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Reset method of the MSFT\_FSRMFileScreen class

Resets the default settings for all file screen parameters with those from the specified template.

## Syntax


```mof
uint64 Reset(
  [in]  string              Template,
  [out] MSFT_FSRMFileScreen FileScreen
);
```



## Parameters

<dl> <dt>

*Template* \[in\]
</dt> <dd>

A valid local path to a folder. Must not exceed the value of **MAX\_PATH**. Required.

</dd> <dt>

*FileScreen* \[out\]
</dt> <dd>

The returns the [**MSFT\_FSRMFileScreen**](msft-fsrmfilescreen.md) instance that was reset.

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

[**MSFT\_FSRMFileScreen**](msft-fsrmfilescreen.md)
</dt> </dl>

 

 






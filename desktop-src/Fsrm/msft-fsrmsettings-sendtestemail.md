---
title: SendTestEmail method of the MSFT\_FSRMSettings class
description: Sends a test email to the specified email address.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a170c866-ccf8-4f5a-860b-cbd04360d970
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- SendTestEmail method File Server Resource Manager
- SendTestEmail method File Server Resource Manager , MSFT_FSRMSettings class
- MSFT_FSRMSettings class File Server Resource Manager , SendTestEmail method
topic_type:
- apiref
api_name:
- MSFT_FSRMSettings.SendTestEmail
api_location:
- SrmSvc.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SendTestEmail method of the MSFT\_FSRMSettings class

Sends a test email to the specified email address.

## Syntax


```mof
uint64 SendTestEmail(
  [in] string ToEmailAddress
);
```



## Parameters

<dl> <dt>

*ToEmailAddress* \[in\]
</dt> <dd>

A string containing a valid email address.

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

[**MSFT\_FSRMSettings**](msft-fsrmsettings.md)
</dt> </dl>

 

 






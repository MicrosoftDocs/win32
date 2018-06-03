---
title: SendRequestEmail method of the MSFT\_FSRMAdr class
description: Sends an email to request additional access to a file.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f9e33884-0361-43ae-a774-9575613c6c19
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- SendRequestEmail method File Server Resource Manager
- SendRequestEmail method File Server Resource Manager , MSFT_FSRMAdr class
- MSFT_FSRMAdr class File Server Resource Manager , SendRequestEmail method
topic_type:
- apiref
api_name:
- MSFT_FSRMAdr.SendRequestEmail
api_location:
- SrmSvc.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SendRequestEmail method of the MSFT\_FSRMAdr class

Sends an email to request additional access to a file.

## Syntax


```mof
uint64 SendRequestEmail(
  [in] string Path,
  [in] string ServerPath,
  [in] uint32 Event,
  [in] string UserMessage
);
```



## Parameters

<dl> <dt>

*Path* \[in\]
</dt> <dd>

A valid path on the server not longer than the **MAX\_PATH** value (260).

</dd> <dt>

*ServerPath* \[in\]
</dt> <dd>

A valid path on the server not longer than the **MAX\_PATH** value (260).

</dd> <dt>

*Event* \[in\]
</dt> <dd>

Describes the type of failure handled by ADR.

<dt>

<span id="AccessDenied"></span><span id="accessdenied"></span><span id="ACCESSDENIED"></span>

<span id="AccessDenied"></span><span id="accessdenied"></span><span id="ACCESSDENIED"></span>**AccessDenied** (1)


</dt> <dd>

The failure was an access denied error.

</dd> <dt>

<span id="FileNotFound"></span><span id="filenotfound"></span><span id="FILENOTFOUND"></span>

<span id="FileNotFound"></span><span id="filenotfound"></span><span id="FILENOTFOUND"></span>**FileNotFound** (2)


</dt> <dd>

The failure was an file not found error.

</dd> </dl> </dd> <dt>

*UserMessage* \[in\]
</dt> <dd>

A string to include in the request email, not to exceed 1KB.

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

[**MSFT\_FSRMAdr**](msft-fsrmadr.md)
</dt> </dl>

 

 






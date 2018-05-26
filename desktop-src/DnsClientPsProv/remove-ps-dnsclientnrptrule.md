---
title: Remove method of the PS\_DnsClientNrptRule class
description: Removes DNS client NRPT rule.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bf1d9369-d145-4459-9643-bfbb0e63f9fb
ms.prod: windows-server-dev
ms.technology:
- dns-client
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_DnsClientNrptRule class
- PS_DnsClientNrptRule class, Remove method
topic_type:
- apiref
api_name:
- PS_DnsClientNrptRule.Remove
api_location:
- DnsClientPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Remove method of the PS\_DnsClientNrptRule class

Removes DNS client NRPT rule.

## Syntax


```mof
uint32 Remove(
  [in]  string            GpoName,
  [in]  string            Name,
  [in]  boolean           PassThru,
  [in]  string            Server,
  [in]  boolean           Force,
  [out] DnsClientNrptRule cmdletOutput
);
```



## Parameters

<dl> <dt>

*GpoName* \[in\]
</dt> <dd>

Name of the GPO on which to operate.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Name which uniquely identifies a rule.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Specifies if result of the cmdlet should be displayed.

</dd> <dt>

*Server* \[in\]
</dt> <dd>

Name of the server containing the GPO.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Specifies not to issue a prompt.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

A [**DnsClientNrptRule**](ps-dnsclientnrptrule.md) object containing all the properties of DNS client NRPT rule.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsClientPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsClientNrptRule**](ps-dnsclientnrptrule.md)
</dt> </dl>

 

 






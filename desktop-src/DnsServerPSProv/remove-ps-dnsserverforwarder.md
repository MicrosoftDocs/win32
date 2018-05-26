---
title: Remove method of the PS\_DnsServerForwarder class
description: Remove the specified Forwarders.
audience: developer
ms.assetid: 6623fbb8-51a8-455b-bb78-6e7adcc8c849
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Remove method
- Remove method, PS_DnsServerForwarder class
- PS_DnsServerForwarder class, Remove method
topic_type:
- apiref
api_name:
- PS_DnsServerForwarder.Remove
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Remove method of the PS\_DnsServerForwarder class

Remove the specified Forwarders.

## Syntax


```mof
uint32 Remove(
  [in]  string             IPAddress[],
  [in]  string             ComputerName,
  [in]  boolean            PassThru,
  [in]  boolean            Force,
  [out] DnsServerForwarder cmdletOutput
);
```



## Parameters

<dl> <dt>

*IPAddress* \[in\]
</dt> <dd>

Specifies the forwarders that need to be removed.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If specified, returns the object or objects on which the operation was done.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

If specified, overrides the default confirmation before performing the operation.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains an embedded instance of the current object. This parameter returns a value only if *PassThru* is set to **true**.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerForwarder**](ps-dnsserverforwarder.md)
</dt> </dl>

 

 






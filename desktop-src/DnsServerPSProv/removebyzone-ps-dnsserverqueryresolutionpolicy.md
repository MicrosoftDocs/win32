---
title: RemoveByZone method of the PS\_DnsServerQueryResolutionPolicy class
description: Removes the name resolution policy from a DNS server by zone.
audience: developer
ms.assetid: eb57a7a6-66b0-4e73-bf00-442074f2cae1
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoveByZone method
- RemoveByZone method, PS_DnsServerQueryResolutionPolicy class
- PS_DnsServerQueryResolutionPolicy class, RemoveByZone method
topic_type:
- apiref
api_name:
- PS_DnsServerQueryResolutionPolicy.RemoveByZone
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoveByZone method of the PS\_DnsServerQueryResolutionPolicy class

Removes the name resolution policy from a DNS server by zone.

## Syntax


```mof
uint32 RemoveByZone(
  [in]  boolean         Force,
  [in]  string          ComputerName,
  [in]  boolean         PassThru,
  [in]  string          Name,
  [in]  string          ZoneName,
  [out] DnsServerPolicy cmdletOutput
);
```



## Parameters

<dl> <dt>

*Force* \[in\]
</dt> <dd>

**True** to not require user confirmation before continuing with the operation; **false** to require user confirmation. The default value is **false**.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional DNS server name.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the current instance in the *CmdletOutput* parameter. The default is **false**.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

The name of the policy.

</dd> <dt>

*ZoneName* \[in\]
</dt> <dd>

The name of the zone.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains a [**DnsServerPolicy**](dnsserverpolicy.md). This parameter returns a value only if *PassThru* is set to **true.**

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerQueryResolutionPolicy**](ps-dnsserverqueryresolutionpolicy.md)
</dt> </dl>

 

 






---
title: Disable method of the PS\_DnsServerSigningKeyRollover class
description: Disables key rollover on input key.
audience: developer
ms.assetid: a1d86b01-2a5e-4a5d-b1a9-2ca45d5d45e6
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Disable method
- Disable method, PS_DnsServerSigningKeyRollover class
- PS_DnsServerSigningKeyRollover class, Disable method
topic_type:
- apiref
api_name:
- PS_DnsServerSigningKeyRollover.Disable
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Disable method of the PS\_DnsServerSigningKeyRollover class

Disables key rollover on input key.

## Syntax


```mof
uint32 Disable(
  [in]  string              ZoneName,
  [in]  boolean             Force,
  [in]  string              KeyId,
  [in]  string              ComputerName,
  [in]  boolean             PassThru,
  [out] DnsServerSigningKey cmdletOutput
);
```



## Parameters

<dl> <dt>

*ZoneName* \[in\]
</dt> <dd>

Name of the zone on which DnsSec operations are performed.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

If specified, overrides the default confirmation before performing the operation.

</dd> <dt>

*KeyId* \[in\]
</dt> <dd>

Uniquely identifies the key.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional DNS server name.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If specified, returns the object or objects on which the operation was done.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains an embedded instance of a [**DnsServerSigningKeyRollover**](ps-dnsserversigningkeyrollover.md) class.

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

[**PS\_DnsServerSigningKeyRollover**](ps-dnsserversigningkeyrollover.md)
</dt> </dl>

 

 






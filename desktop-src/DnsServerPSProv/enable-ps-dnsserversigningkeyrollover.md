---
title: Enable method of the PS\_DnsServerSigningKeyRollover class
description: Enables rollover on the input key.
audience: developer
ms.assetid: 3c2843ed-bdc3-4fa1-8b90-29155df2254f
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Enable method
- Enable method, PS_DnsServerSigningKeyRollover class
- PS_DnsServerSigningKeyRollover class, Enable method
topic_type:
- apiref
api_name:
- PS_DnsServerSigningKeyRollover.Enable
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Enable method of the PS\_DnsServerSigningKeyRollover class

Enables rollover on the input key.

## Syntax


```mof
uint32 Enable(
  [in]  string              ComputerName,
  [in]  datetime            RolloverPeriod,
  [in]  datetime            InitialRolloverOffset,
  [in]  boolean             Force,
  [in]  string              ZoneName,
  [in]  string              KeyId,
  [in]  boolean             PassThru,
  [out] DnsServerSigningKey cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional DNS server name.

</dd> <dt>

*RolloverPeriod* \[in\]
</dt> <dd>

Amount of time between scheduled key rollovers.

</dd> <dt>

*InitialRolloverOffset* \[in\]
</dt> <dd>

Amount of time to delay the first scheduled key rollover. This allows for key rollovers to be staggered.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

If specified, overrides the default confirmation before performing the operation.

</dd> <dt>

*ZoneName* \[in\]
</dt> <dd>

Name of the zone on which DnsSec operations are performed.

</dd> <dt>

*KeyId* \[in\]
</dt> <dd>

Uniquely identifies the key.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If specified, returns the object or objects on which the operation was done.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains an embedded instance of the [**DnsServerSigningKeyRollover**](ps-dnsserversigningkeyrollover.md) class.

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

 

 






---
title: Invoke method of the PS\_DnsServerSigningKeyRollover class
description: Initiates rollover of input keys for the zone.
audience: developer
ms.assetid: 2731ac8d-d537-4c76-98ad-98f35baf595c
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Invoke method
- Invoke method, PS_DnsServerSigningKeyRollover class
- PS_DnsServerSigningKeyRollover class, Invoke method
topic_type:
- apiref
api_name:
- PS_DnsServerSigningKeyRollover.Invoke
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Invoke method of the PS\_DnsServerSigningKeyRollover class

Initiates rollover of input keys for the zone.

## Syntax


```mof
uint32 Invoke(
  [in]  string              ZoneName,
  [in]  string              KeyId[],
  [in]  string              ComputerName,
  [in]  boolean             Force,
  [in]  boolean             PassThru,
  [out] DnsServerSigningKey cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ZoneName* \[in\]
</dt> <dd>

The name of the zone in which DNS Security Extensions (DNSSEC) operations are performed.

</dd> <dt>

*KeyId* \[in\]
</dt> <dd>

One or more key identifiers.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional. A DNS server name. The acceptable values for this parameter are: an IP v4 address, an IP v6 address, or any other value that resolves to an IP address, such as a fully qualified domain name (FQDN), host name, or NETBIOS name.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Instructs the method to perform the operation without prompting for confirmation.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Returns an object representing the item with which you are working. By default, this method does not generate any output.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

One or more embedded instances of the [**DnsServerSigningKeyRollover**](ps-dnsserversigningkeyrollover.md) class.

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

 

 






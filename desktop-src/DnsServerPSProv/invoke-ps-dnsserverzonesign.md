---
title: Invoke method of the PS\_DnsServerZoneSign class
description: Initiates an operation to sign a zone.
audience: developer
ms.assetid: baf9db9e-1166-4a80-a397-18afef2f54a5
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Invoke method
- Invoke method, PS_DnsServerZoneSign class
- PS_DnsServerZoneSign class, Invoke method
topic_type:
- apiref
api_name:
- PS_DnsServerZoneSign.Invoke
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Invoke method of the PS\_DnsServerZoneSign class

Initiates an operation to sign a zone.

## Syntax


```mof
uint32 Invoke(
  [in]  string               ZoneName,
  [in]  boolean              SignWithDefault,
  [in]  boolean              DoResign,
  [in]  string               ComputerName,
  [in]  boolean              Force,
  [in]  boolean              PassThru,
  [out] DnsServerPrimaryZone cmdletOutput
);
```



## Parameters

<dl> <dt>

*ZoneName* \[in\]
</dt> <dd>

The name of the primary zone to sign.

</dd> <dt>

*SignWithDefault* \[in\]
</dt> <dd>

Signs a zone with default settings. If a zone is already signed, this parameter removes the existing key signing key (KSK) and zone signing key (ZSK) values for the zone and configures DNSSEC settings to default values. A new KSK and a new ZSK are used to re-sign the zone.

</dd> <dt>

*DoResign* \[in\]
</dt> <dd>

Re-signs a DNSSEC-signed zone.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional. A DNS server name. If you do not specify this parameter, the command runs on the local system. You can specify an IP address or any value that resolves to an IP address, such as a fully qualified domain name (FQDN), host name, or NETBIOS name.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Signs the DNS Server zone without prompting you for confirmation. By default, the cmdlet prompts you for confirmation before it proceeds.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Specifies whether the method returns an object that represents the item you are working. By default, this method does not generate any output.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DnsServerZoneSign**](dnsserverzonesigningmetadata.md) class.

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

[**PS\_DnsServerZoneSign**](ps-dnsserverzonesign.md)
</dt> </dl>

 

 






---
title: Invoke method of the PS\_DnsServerZoneUnsign class
description: Initiates unsigning on the zone.
audience: developer
ms.assetid: 83280aed-f0e0-4a25-8ebd-ea7a63318e01
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Invoke method
- Invoke method, PS_DnsServerZoneUnsign class
- PS_DnsServerZoneUnsign class, Invoke method
topic_type:
- apiref
api_name:
- PS_DnsServerZoneUnsign.Invoke
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Invoke method of the PS\_DnsServerZoneUnsign class

Initiates unsigning on the zone.

## Syntax


```mof
uint32 Invoke(
  [in]  string               ZoneName,
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

Name of the primary zone to be unsigned.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional DNS server name.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

If specified, overrides the default confirmation before performing the operation.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If specified, returns the object or objects on which the operation was done.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DnsServerZoneUnsign**](ps-dnsserverzoneunsign.md) class.

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

[**PS\_DnsServerZoneUnsign**](ps-dnsserverzoneunsign.md)
</dt> </dl>

 

 






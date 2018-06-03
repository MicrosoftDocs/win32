---
title: AddByInputObject method of the PS\_DnsServerZoneDelegation class
description: Adds a new delegated DNS zone to an existing zone.
audience: developer
ms.assetid: 019a95cb-6c6f-4afe-b2fc-5a6a7ea38c41
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddByInputObject method
- AddByInputObject method, PS_DnsServerZoneDelegation class
- PS_DnsServerZoneDelegation class, AddByInputObject method
topic_type:
- apiref
api_name:
- PS_DnsServerZoneDelegation.AddByInputObject
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddByInputObject method of the PS\_DnsServerZoneDelegation class

Adds a new delegated DNS zone to an existing zone.

## Syntax


```mof
uint32 AddByInputObject(
  [in]  string                  ComputerName,
  [in]  DnsServerZoneDelegation InputObject,
  [in]  string                  VirtualizationInstance,
  [in]  boolean                 PassThru,
  [in]  string                  ZoneScope,
  [out] DnsServerZoneDelegation cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies a DNS server. If you do not specify this parameter, the command runs on the local system. You can specify an IP address or any value that resolves to an IP address, such as a fully qualified domain name (FQDN), host name, or NETBIOS name.

</dd> <dt>

*InputObject* \[in\]
</dt> <dd>

This parameter takes an object of type [**DnsServerZoneDelegation**](dnsserverzonedelegation.md) as input.

</dd> <dt>

*VirtualizationInstance* \[in\]
</dt> <dd>

Unique identifier of the virtualization instance.

**Windows Server 2012 R2 and Windows Server 2012:** This parameter is unavailable prior to Windows Server 2016.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the object that was modified by the method. By default, this method does not generate any output.

</dd> <dt>

*ZoneScope* \[in\]
</dt> <dd>

Name of the zone scope.

**Windows Server 2012:** Not supported.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives an embedded instance of the [**DnsServerZoneDelegation**](dnsserverzonedelegation.md) class.

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

[**PS\_DnsServerZoneDelegation**](ps-dnsserverzonedelegation.md)
</dt> </dl>

 

 






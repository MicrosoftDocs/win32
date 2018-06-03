---
title: AddByInputObject method of the PS\_DnsServerResourceRecord class
description: Adds the resource record to a specified zone in a DNS server.
audience: developer
ms.assetid: a458de46-2720-40f4-a0c1-3be13fef5ad5
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddByInputObject method
- AddByInputObject method, PS_DnsServerResourceRecord class
- PS_DnsServerResourceRecord class, AddByInputObject method
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecord.AddByInputObject
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddByInputObject method of the PS\_DnsServerResourceRecord class

Adds the resource record to a specified zone in a DNS server.

## Syntax


```mof
uint32 AddByInputObject(
  [in]  DnsServerResourceRecord InputObject,
  [in]  string                  ZoneName,
  [in]  string                  ComputerName,
  [in]  boolean                 AllowUpdateAny,
  [in]  boolean                 PassThru,
  [in]  boolean                 Force,
  [in]  string                  ZoneScope,
  [in]  string                  VirtualizationInstance,
  [out] DnsServerResourceRecord cmdletOutput
);
```



## Parameters

<dl> <dt>

*InputObject* \[in\]
</dt> <dd>

Specifies the input to this method. This parameter takes an object of type Microsoft.Management.Infrastructure.CimInstance.DnsServerResourceRecord as input.

</dd> <dt>

*ZoneName* \[in\]
</dt> <dd>

Specifies the name of the DNS server zone.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies a DNS server. If you do not specify this parameter, the command runs on the local system. You can specify an IP address or any value that resolves to an IP address, such as a fully qualified domain name (FQDN), host name, or NETBIOS name.

</dd> <dt>

*AllowUpdateAny* \[in\]
</dt> <dd>

Allow any authenticated user to update DNS record with same owner name

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the object that was modified by the method. By default, this method does not generate any output.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Adds a resource record without prompting you for confirmation. By default, the method prompts you for confirmation before it proceeds.

</dd> <dt>

*ZoneScope* \[in\]
</dt> <dd>

Name of the zone scope.

**Windows Server 2012:** Not supported.

</dd> <dt>

*VirtualizationInstance* \[in\]
</dt> <dd>

Unique identifier of the virtualization instance.

**Windows Server 2012 R2 and Windows Server 2012:** This parameter is unavailable prior to Windows Server 2016.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives an embedded instance of the [**DnsServerResourceRecord**](dnsserverresourcerecord.md) class.

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

[**PS\_DnsServerResourceRecord**](ps-dnsserverresourcerecord.md)
</dt> </dl>

 

 






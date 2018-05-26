---
title: AddByInputObject method of the PS\_DnsServerQueryResolutionPolicy class
description: Adds a query resolution policy to the DNS server.
audience: developer
ms.assetid: 29fae9d8-ff1e-4894-81b1-406730f49a46
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- AddByInputObject method
- AddByInputObject method, PS_DnsServerQueryResolutionPolicy class
- PS_DnsServerQueryResolutionPolicy class, AddByInputObject method
topic_type:
- apiref
api_name:
- PS_DnsServerQueryResolutionPolicy.AddByInputObject
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddByInputObject method of the PS\_DnsServerQueryResolutionPolicy class

Adds a query resolution policy to the DNS server

## Syntax


```mof
uint32 AddByInputObject(
  [in]  boolean         PassThru,
  [in]  string          ComputerName,
  [in]  DnsServerPolicy InputObject,
  [in]  string          ZoneName,
  [out] DnsServerPolicy cmdletOutput
);
```



## Parameters

<dl> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the current instance in the *CmdletOutput* parameter. The default is **false**.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional DNS server name.

</dd> <dt>

*InputObject* \[in\]
</dt> <dd>

The input object on which to add.

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

 

 






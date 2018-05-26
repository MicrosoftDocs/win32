---
title: SetByInputObject method of the PS\_DnsServerQueryResolutionPolicy class
description: Sets the DNS server name resolution policy by input object.
audience: developer
ms.assetid: b19fa3d7-436f-46be-9669-2889530e89dd
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByInputObject method
- SetByInputObject method, PS_DnsServerQueryResolutionPolicy class
- PS_DnsServerQueryResolutionPolicy class, SetByInputObject method
topic_type:
- apiref
api_name:
- PS_DnsServerQueryResolutionPolicy.SetByInputObject
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetByInputObject method of the PS\_DnsServerQueryResolutionPolicy class

Sets the DNS server name resolution policy by input object.

## Syntax


```mof
uint32 SetByInputObject(
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

The input object to set.

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

 

 






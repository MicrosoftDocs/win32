---
title: Set method of the PS\_DnsServer class
description: Overwrites entire DNS server configuration.
audience: developer
ms.assetid: e7be6ec9-fd68-4084-a148-f08e0056dd05
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_DnsServer class
- PS_DnsServer class, Set method
topic_type:
- apiref
api_name:
- PS_DnsServer.Set
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Set method of the PS\_DnsServer class

Overwrites entire DNS server configuration.

## Syntax


```mof
uint32 Set(
  [in]  DnsServer InputObject,
  [in]  string    ComputerName,
  [in]  boolean   Force,
  [in]  boolean   CreateFileBackedPrimaryZones,
  [in]  boolean   PassThru,
  [out] DnsServer cmdletOutput
);
```



## Parameters

<dl> <dt>

*InputObject* \[in\]
</dt> <dd>

An embedded instance of the [**DnsServer**](dnsserver.md) class that specifies DNS server configuration that needs to be applied.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command

</dd> <dt>

*Force* \[in\]
</dt> <dd>

If specified, overrides the default confirmation before performing the operation.

</dd> <dt>

*CreateFileBackedPrimaryZones* \[in\]
</dt> <dd>

Specifies that new file backed primary zones need to be created on the server

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If specified, returns the object or objects on which the operation was done.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DnsServer**](dnsserver.md) class.

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

[**PS\_DnsServer**](ps-dnsserver.md)
</dt> </dl>

 

 






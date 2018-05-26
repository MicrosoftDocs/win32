---
title: Set method of the PS\_DnsServerSecondaryZone class
description: Overwrites settings of DNS server secondary zone.
audience: developer
ms.assetid: 1b65b34b-819d-4a5c-bb33-d4934c3ed966
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_DnsServerSecondaryZone class
- PS_DnsServerSecondaryZone class, Set method
topic_type:
- apiref
api_name:
- PS_DnsServerSecondaryZone.Set
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Set method of the PS\_DnsServerSecondaryZone class

Overwrites settings of DNS server secondary zone.

## Syntax


```mof
uint32 Set(
  [in]  string                 MasterServers[],
  [in]  string                 Name,
  [in]  string                 ComputerName,
  [in]  string                 ZoneFile,
  [in]  boolean                PassThru,
  [in]  boolean                IgnorePolicies,
  [out] DnsServerSecondaryZone cmdletOutput
);
```



## Parameters

<dl> <dt>

*MasterServers* \[in\]
</dt> <dd>

Specifies IP addresses of the master DNS servers for this zone.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the name of the zone.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

</dd> <dt>

*ZoneFile* \[in\]
</dt> <dd>

Specifies zone file path.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**True** to return the object that was modified by the method. By default, this method does not generate any output.

</dd> <dt>

*IgnorePolicies* \[in\]
</dt> <dd>

**true** if the policies of this zone are to be ignored; otherwise, **false**.

**Windows Server 2012 R2 and Windows Server 2012:** Not supported.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives and embedded instance of the [**DnsServerSecondaryZone**](dnsserversecondaryzone.md) class.

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

[**PS\_DnsServerSecondaryZone**](ps-dnsserversecondaryzone.md)
</dt> </dl>

 

 






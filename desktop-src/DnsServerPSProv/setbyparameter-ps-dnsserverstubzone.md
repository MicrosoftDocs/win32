---
title: SetByParameter method of the PS\_DnsServerStubZone class
description: Overwrites settings of DNS server stub zone. If none exists exit with terminating error.
audience: developer
ms.assetid: '940e01d8-a4c7-47da-a8de-2bbc4a1d5d4e'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetByParameter method", "SetByParameter method, PS_DnsServerStubZone class", "PS_DnsServerStubZone class, SetByParameter method"]
topic_type:
- apiref
api_name:
- PS_DnsServerStubZone.SetByParameter
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# SetByParameter method of the PS\_DnsServerStubZone class

Overwrites settings of DNS server stub zone. If none exists exit with terminating error.

## Syntax


```mof
uint32 SetByParameter(
  [in]  string            MasterServers[],
  [in]  string            Name,
  [in]  string            ComputerName,
  [in]  string            LocalMasters[],
  [in]  boolean           PassThru,
  [out] DnsServerStubZone cmdletOutput
);
```



## Parameters

<dl> <dt>

*MasterServers* \[in\]
</dt> <dd>

Specifies a list of master DNS servers stored in the Windows Registry on the local server. If it exists, this list overrides the list of master servers stored in Active Directory.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the name of the zone.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command

</dd> <dt>

*LocalMasters* \[in\]
</dt> <dd>

Local master name servers

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**True** to return the object that was modified by the method. By default, this method does not generate any output.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains an instance of the current object. This parameter returns a value only if *PassThru* is set to **true.**

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerStubZone**](ps-dnsserverstubzone.md)
</dt> </dl>

 

 






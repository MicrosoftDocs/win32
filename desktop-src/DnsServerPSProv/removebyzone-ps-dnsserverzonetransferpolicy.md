---
title: RemoveByZone method of the PS\_DnsServerZoneTransferPolicy class
description: Removes a zone transfer policy by zone.
audience: developer
ms.assetid: 'fd5e4251-d2f9-43b0-971e-19ec7fa38afd'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RemoveByZone method", "RemoveByZone method, PS_DnsServerZoneTransferPolicy class", "PS_DnsServerZoneTransferPolicy class, RemoveByZone method"]
topic_type:
- apiref
api_name:
- PS_DnsServerZoneTransferPolicy.RemoveByZone
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# RemoveByZone method of the PS\_DnsServerZoneTransferPolicy class

Removes a zone transfer policy by zone.

## Syntax


```mof
uint32 RemoveByZone(
  [in]  boolean         PassThru,
  [in]  string          Name,
  [in]  string          ComputerName,
  [in]  boolean         Force,
  [in]  string          ZoneName,
  [out] DnsServerPolicy cmdletOutput
);
```



## Parameters

<dl> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the current instance in the *CmdletOutput* parameter. The default is **false**.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Name of the policy to remove.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional computer name.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

**True** to not require user confirmation before continuing with the operation; **false** to require user confirmation. The default value is **false**.

</dd> <dt>

*ZoneName* \[in\]
</dt> <dd>

Name of the zone.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains a [**DnsServerPolicy**](dnsserverpolicy.md). This parameter returns a value only if *PassThru* is set to **true.**

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerZoneTransferPolicy**](ps-dnsserverzonetransferpolicy.md)
</dt> </dl>

 

 






---
title: Remove method of the PS\_DnsServerSigningKey class
description: Deletes one or more input keys from the zone.
audience: developer
ms.assetid: 'a34a310c-e7c0-4919-a0a7-36aac4e1c6c8'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Remove method", "Remove method, PS_DnsServerSigningKey class", "PS_DnsServerSigningKey class, Remove method"]
topic_type:
- apiref
api_name:
- PS_DnsServerSigningKey.Remove
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# Remove method of the PS\_DnsServerSigningKey class

Deletes one or more input keys from the zone.

## Syntax


```mof
uint32 Remove(
  [in]  string              ZoneName,
  [in]  boolean             PassThru,
  [in]  string              KeyId[],
  [in]  boolean             Force,
  [in]  string              ComputerName,
  [out] DnsServerSigningKey cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ZoneName* \[in\]
</dt> <dd>

Name of the zone on which DnsSec operations are performed.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If specified, returns the object or objects on which the operation was done.

</dd> <dt>

*KeyId* \[in\]
</dt> <dd>

Uniquely identifies the key.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

If specified, overrides the default confirmation before performing the operation.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional DNS server name.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains an embedded instance of the current object. This parameter returns a value only if *PassThru* is set to **true**.

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

[**PS\_DnsServerSigningKey**](ps-dnsserversigningkey.md)
</dt> </dl>

 

 






---
title: RemoveByName method of the PS\_DnsServerTrustAnchor class
description: Deletes the specified trust anchor.
audience: developer
ms.assetid: '2c44a53c-18d7-4f4a-9e37-422eea437d4c'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RemoveByName method", "RemoveByName method, PS_DnsServerTrustAnchor class", "PS_DnsServerTrustAnchor class, RemoveByName method"]
topic_type:
- apiref
api_name:
- PS_DnsServerTrustAnchor.RemoveByName
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# RemoveByName method of the PS\_DnsServerTrustAnchor class

Deletes the specified trust anchor.

## Syntax


```mof
uint32 RemoveByName(
  [in]  string               ComputerName,
  [in]  string               Name,
  [in]  string               Type,
  [in]  boolean              Force,
  [in]  boolean              PassThru,
  [out] DnsServerTrustAnchor cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional DNS server name.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Name of the zone whose trust anchor needs to be removed.

</dd> <dt>

*Type* \[in\]
</dt> <dd>

Trust Anchor Type

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

On return, contains an instance of the current object. This parameter returns a value only if *PassThru* is set to **true**.

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

[**PS\_DnsServerTrustAnchor**](ps-dnsservertrustanchor.md)
</dt> </dl>

 

 






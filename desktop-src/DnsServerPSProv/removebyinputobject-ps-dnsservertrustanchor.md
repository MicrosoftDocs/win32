---
title: RemoveByInputObject method of the PS\_DnsServerTrustAnchor class
description: Deletes the specified trust anchor.
audience: developer
ms.assetid: 'aa872de1-43b0-489f-a6ae-0ba690834c48'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RemoveByInputObject method", "RemoveByInputObject method, PS_DnsServerTrustAnchor class", "PS_DnsServerTrustAnchor class, RemoveByInputObject method"]
topic_type:
- apiref
api_name:
- PS_DnsServerTrustAnchor.RemoveByInputObject
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# RemoveByInputObject method of the PS\_DnsServerTrustAnchor class

Deletes the specified trust anchor.

## Syntax


```mof
uint32 RemoveByInputObject(
  [in]  string               ComputerName,
  [in]  boolean              Force,
  [in]  boolean              PassThru,
  [in]  DnsServerTrustAnchor InputObject[],
  [out] DnsServerTrustAnchor cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional DNS server name.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

If specified, overrides the default confirmation before performing the operation.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If specified, returns the object or objects on which the operation was done.

</dd> <dt>

*InputObject* \[in\]
</dt> <dd>

Specifies Trust Anchor object (retrieved from Get-DnsServerTrustAnchor) that needs to be removed

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains an embedded instance of [**DnsServerTrustAnchor**](dnsservertrustanchor.md). This parameter returns a value only if *PassThru* is set to **true**.

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

 

 






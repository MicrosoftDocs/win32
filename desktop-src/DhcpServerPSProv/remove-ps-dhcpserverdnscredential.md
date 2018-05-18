---
title: Remove method of the PS\_DhcpServerDnsCredential class
description: Removes DNS credentials to be used by the DHCP server for registering leases with the DNS server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '5b0e01f3-a58d-4f08-8a5c-cbff2eedab48'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Remove method", "Remove method, PS_DhcpServerDnsCredential class", "PS_DhcpServerDnsCredential class, Remove method"]
topic_type:
- apiref
api_name:
- PS_DhcpServerDnsCredential.Remove
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
---

# Remove method of the PS\_DhcpServerDnsCredential class

Removes DNS credentials to be used by the DHCP server for registering leases with the DNS server.

## Syntax


```mof
uint32 Remove(
  [in]  string                  ComputerName,
  [in]  boolean                 PassThru,
  [out] DhcpServerDnsCredential cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If specified, returns an output object for [**DhcpServerDnsCredential**](dhcpserverdnscredential.md)

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of a [**DhcpServerDnsCredential**](dhcpserverdnscredential.md) object.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DhcpServerDnsCredential**](ps-dhcpserverdnscredential.md)
</dt> </dl>

 

 






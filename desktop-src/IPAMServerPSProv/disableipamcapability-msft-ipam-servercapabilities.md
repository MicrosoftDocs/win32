---
Description: 'Disables an optional feature on an IPAM Server.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'ba76617f-3a3e-4f81-baf5-981da369baae'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'DisableIpamCapability method of the MSFT\_IPAM\_ServerCapabilities class'
---

# DisableIpamCapability method of the MSFT\_IPAM\_ServerCapabilities class

Disables an optional feature on an IPAM Server.

## Syntax


```mof
uint32 DisableIpamCapability(
  [in]  uint16                       Capability,
  [out] MSFT_IPAM_ServerCapabilities Output[]
);
```



## Parameters

<dl> <dt>

*Capability* \[in\]
</dt> <dd>

The name of the feature to disable.

The possible values are:

<dt>

1
</dt> <dd>

IpAddressTracking

</dd> </dl> </dd> <dt>

*Output* \[out\]
</dt> <dd>

When this method returns, this parameter contains an array that contains the updated IPAM server features.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_IPAM\_ServerCapabilities**](msft-ipam-servercapabilities.md)
</dt> </dl>

 

 





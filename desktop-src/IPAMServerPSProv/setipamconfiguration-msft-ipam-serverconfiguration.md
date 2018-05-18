---
Description: 'Updates the configuration for an IPAM server.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '32e14877-055f-4c3e-8eaf-5c01e8521fa0'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'SetIpamConfiguration method of the MSFT\_IPAM\_ServerConfiguration class'
---

# SetIpamConfiguration method of the MSFT\_IPAM\_ServerConfiguration class

Updates the configuration for an IPAM server.

## Syntax


```mof
uint32 SetIpamConfiguration(
  [in]  uint16                        Port,
  [in]  uint16                        ProvisioningMethod,
  [in]  string                        GpoPrefix,
  [in]  string                        HMACKey,
  [out] MSFT_IPAM_ServerConfiguration Output
);
```



## Parameters

<dl> <dt>

*Port* \[in\]
</dt> <dd>

The TCP port number used to provision the server.

</dd> <dt>

*ProvisioningMethod* \[in\]
</dt> <dd>

The provisioning method to configure on the server.

</dd> <dt>

*GpoPrefix* \[in\]
</dt> <dd>

The GPO prefix to use for Group Policy based provisioning.

</dd> <dt>

*HMACKey* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*Output* \[out\]
</dt> <dd>

When this method returns, this parameter contains a [**MSFT\_IPAM\_ServerConfiguration**](msft-ipam-serverconfiguration.md) containing the updated server configuration.

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

[**MSFT\_IPAM\_ServerConfiguration**](msft-ipam-serverconfiguration.md)
</dt> </dl>

 

 





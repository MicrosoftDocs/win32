---
Description: 'Updates the utilization thresholds for an IP address range, subnet mask, or block.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '6baee9ad-770e-44e8-bc1d-a0ae830fdb15'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'SetIpamAddressUtilizationThreshold method of the MSFT\_IPAM\_IPAddressUtilizationThreshold class'
---

# SetIpamAddressUtilizationThreshold method of the MSFT\_IPAM\_IPAddressUtilizationThreshold class

Updates the utilization thresholds for an IP address range, subnet mask, or block.

## Syntax


```mof
uint32 SetIpamAddressUtilizationThreshold(
  [in]  uint32                                  UnderUtilizationThreshold,
  [in]  uint32                                  OverUtilizationThreshold,
  [out] MSFT_IPAM_IPAddressUtilizationThreshold Output
);
```



## Parameters

<dl> <dt>

*UnderUtilizationThreshold* \[in\]
</dt> <dd>

The updated threshold percentage that indicates whether an IP address range, subnet, or block is underutilized.

</dd> <dt>

*OverUtilizationThreshold* \[in\]
</dt> <dd>

The updated threshold percentage that indicates whether an IP address range, subnet, or block is overutilized.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

When this method returns, this parameter contains the updated set of utilization thresholds.

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

[**MSFT\_IPAM\_IPAddressUtilizationThreshold**](msft-ipam-ipaddressutilizationthreshold.md)
</dt> </dl>

 

 





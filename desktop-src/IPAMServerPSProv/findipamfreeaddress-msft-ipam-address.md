---
Description: 'Retrieves an array of IP addresses from a range of IP addresses in IPAM that are not assigned to a device.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '5e98ec65-d251-4b9f-b5c6-3be522c7041b'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'FindIpamFreeAddress method of the MSFT\_IPAM\_Address class'
---

# FindIpamFreeAddress method of the MSFT\_IPAM\_Address class

Retrieves an array of IP addresses from a range of IP addresses in IPAM that are not assigned to a device.

## Syntax


```mof
uint32 FindIpamFreeAddress(
  [in]  MSFT_IPAM_Range       Range,
  [in]  uint32                NumAddress,
  [in]  boolean               TestReachability,
  [out] MSFT_IPAM_FreeAddress FreeIPAddresses[]
);
```



## Parameters

<dl> <dt>

*Range* \[in\]
</dt> <dd>

The IPAM range from which to retrieve the IP addresses.

</dd> <dt>

*NumAddress* \[in\]
</dt> <dd>

The number of IP addresses to retrieve.

</dd> <dt>

*TestReachability* \[in\]
</dt> <dd>

**True** to test the reachability of the IP addresses; otherwise, **false**.

</dd> <dt>

*FreeIPAddresses* \[out\]
</dt> <dd>

When this method returns, this parameter contains the array of retrieved IP addresses.

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

[**MSFT\_IPAM\_Address**](msft-ipam-address.md)
</dt> </dl>

 

 





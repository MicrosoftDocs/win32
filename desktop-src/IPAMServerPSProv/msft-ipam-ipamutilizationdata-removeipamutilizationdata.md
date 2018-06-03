---
Description: Deletes all utilization data in IPAM database on or before a specified date.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fbac4b97-89de-4aba-82e4-709e1b35cc0a
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: RemoveIpamUtilizationData method of the MSFT\_IPAM\_IpamUtilizationData class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemoveIpamUtilizationData method of the MSFT\_IPAM\_IpamUtilizationData class

Deletes all utilization data in IPAM database on or before a specified date.

## Syntax


```mof
uint32 RemoveIpamUtilizationData(
  [in]  datetime                      EndDate,
  [out] MSFT_IPAM_IpamUtilizationData Output[]
);
```



## Parameters

<dl> <dt>

*EndDate* \[in\]
</dt> <dd>

The end date.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

On success, returns an array of [**MSFT\_IPAM\_IpamUtilizationData**](msft-ipam-ipamutilizationdata.md) embedded instances.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_IPAM\_IpamUtilizationData**](msft-ipam-ipamutilizationdata.md)
</dt> </dl>

 

 





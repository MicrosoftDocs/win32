---
Description: Represents the utilization data in an IPAM database.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 711a98e9-361b-4818-b106-8fe922e87f83
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: MSFT\_IPAM\_IpamUtilizationData class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_IPAM\_IpamUtilizationData class

Represents the utilization data in an IPAM database.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("IPAMServerPSProvider"), AMENDMENT]
class MSFT_IPAM_IpamUtilizationData
{
};
```

## Members

The **MSFT\_IPAM\_IpamUtilizationData** class has these types of members:

-   [Methods](#methods)

### Methods

The **MSFT\_IPAM\_IpamUtilizationData** class has these methods.



| Method                                                                                       | Description                                                                             |
|:---------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------|
| [**RemoveIpamUtilizationData**](msft-ipam-ipamutilizationdata-removeipamutilizationdata.md) | Deletes all utilization data in IPAM database on or before a specified date.<br/> |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



 

 





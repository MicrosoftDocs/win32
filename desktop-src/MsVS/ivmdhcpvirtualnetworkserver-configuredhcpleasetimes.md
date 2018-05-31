---
title: IVMDHCPVirtualNetworkServer ConfigureDHCPLeaseTimes method
description: The ConfigureDHCPLeaseTimes method sets the lease time parameters for leases managed by the virtual DHCP server.
ms.assetid: b1dd4723-8ec8-4078-a91f-3cafb8143cc4
keywords:
- ConfigureDHCPLeaseTimes method Virtual Server
- ConfigureDHCPLeaseTimes method Virtual Server , IVMDHCPVirtualNetworkServer interface
- IVMDHCPVirtualNetworkServer interface Virtual Server , ConfigureDHCPLeaseTimes method
- ConfigureDHCPLeaseTimes method Virtual Server , VMDHCPVirtualNetworkServer interface
- VMDHCPVirtualNetworkServer interface Virtual Server , ConfigureDHCPLeaseTimes method
topic_type:
- apiref
api_name:
- IVMDHCPVirtualNetworkServer.ConfigureDHCPLeaseTimes
- VMDHCPVirtualNetworkServer.ConfigureDHCPLeaseTimes
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IVMDHCPVirtualNetworkServer::ConfigureDHCPLeaseTimes method

The **ConfigureDHCPLeaseTimes** method sets the lease time parameters for leases managed by the virtual DHCP server.

## Syntax


```C++
HRESULT ConfigureDHCPLeaseTimes(
  [in] VARIANT leaseTime,
  [in] VARIANT leaseRenewalTime,
  [in] VARIANT leaseRebindingTime
);
```



## Parameters

<dl> <dt>

*leaseTime* \[in\]
</dt> <dd>

The time in seconds after which leases granted by the virtual DHCP server expire. This number is passed as a VARIANT of type VT\_DECIMAL.

</dd> <dt>

*leaseRenewalTime* \[in\]
</dt> <dd>

The time, in seconds, after which the client virtual machine should renew its TCP/IP address lease. This number is passed as a VARIANT of type VT\_DECIMAL.

</dd> <dt>

*leaseRebindingTime* \[in\]
</dt> <dd>

The time in seconds after which the client virtual machine should rebind if the virtual DHCP server has not responded. This number is passed as a VARIANT of type VT\_DECIMAL.

</dd> </dl>

## Return value

This method can return one of these values.

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                         | Description                                                                                                                                   |
|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt> **S\_OK**</dt> </dl>               | The operation was successful.<br/>                                                                                                      |
| <dl> <dt> **E\_INVALIDARG**</dt> </dl>       | The calling parameters are invalid.<br/>                                                                                                |
| <dl> <dt> **DISP\_E\_BADVARTYPE**</dt> </dl> | One of the parameters could not be coerced into the correct data type.<br/>                                                             |
| <dl> <dt> **DISP\_E\_OVERFLOW**</dt> </dl>   | The value specified in one of the parameters was greater than the maximum allowed value. Other **HRESULT** values may be returned.<br/> |



 

## Remarks

*leaseRenewalTime* must be less than *leaseRebindingTime*. Likewise, *leaseRebindingTime* must be less than *leaseTime*. All must be in the range 1..2^32-1.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMDHCPVirtualNetworkServer**](ivmdhcpvirtualnetworkserver.md)
</dt> </dl>

 

 






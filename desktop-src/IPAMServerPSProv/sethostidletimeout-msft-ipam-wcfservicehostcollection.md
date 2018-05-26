---
Description: Updates the timeout duration of a WCF service host.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 038ae855-be04-439a-a5cc-dd82f31588ff
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: SetHostIdleTimeout method of the MSFT\_IPAM\_WCFServiceHostCollection class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetHostIdleTimeout method of the MSFT\_IPAM\_WCFServiceHostCollection class

Updates the timeout duration of a WCF service host.

## Syntax


```mof
uint32 SetHostIdleTimeout(
  [in] uint8 idleTimeoutInMinutes
);
```



## Parameters

<dl> <dt>

*idleTimeoutInMinutes* \[in\]
</dt> <dd>

The timeout duration of the service host, in minutes.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_IPAM\_WCFServiceHostCollection**](msft-ipam-wcfservicehostcollection.md)
</dt> </dl>

 

 





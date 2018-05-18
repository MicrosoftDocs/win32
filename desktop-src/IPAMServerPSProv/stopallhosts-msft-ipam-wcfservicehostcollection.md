---
Description: 'Closes all of the WCF service host endpoints in IPAM, and deletes them.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '04bd4402-598c-4ffe-922a-058c23c656b2'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'StopAllHosts method of the MSFT\_IPAM\_WCFServiceHostCollection class'
---

# StopAllHosts method of the MSFT\_IPAM\_WCFServiceHostCollection class

Closes all of the WCF service host endpoints in IPAM, and deletes them.

## Syntax


```mof
uint32 StopAllHosts();
```



## Parameters

This method has no parameters.

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

[**MSFT\_IPAM\_WCFServiceHostCollection**](msft-ipam-wcfservicehostcollection.md)
</dt> </dl>

 

 





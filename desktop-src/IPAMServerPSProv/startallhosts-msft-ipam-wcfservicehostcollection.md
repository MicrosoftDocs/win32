---
Description: 'Creates WCF service host endpoints, and opens them for communication.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '8c231c90-afc9-494c-8ab9-d193496ca362'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'StartAllHosts method of the MSFT\_IPAM\_WCFServiceHostCollection class'
---

# StartAllHosts method of the MSFT\_IPAM\_WCFServiceHostCollection class

Creates WCF service host endpoints, and opens them for communication.

## Syntax


```mof
uint32 StartAllHosts();
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

 

 





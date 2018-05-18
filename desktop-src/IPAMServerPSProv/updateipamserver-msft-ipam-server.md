---
Description: 'Updates an IPAM server following an operating system upgrade.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '1e69d1c4-9383-42d7-b113-56fdec4774c9'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'UpdateIpamServer method of the MSFT\_IPAM\_Server class'
---

# UpdateIpamServer method of the MSFT\_IPAM\_Server class

Updates an IPAM server following an operating system upgrade.

## Syntax


```mof
uint32 UpdateIpamServer(
  [in] boolean DeleteSystemCheckFailureRows
);
```



## Parameters

<dl> <dt>

*DeleteSystemCheckFailureRows* \[in\]
</dt> <dd>

**True** to delete error data for a failed IPAM database schema validation; otherwise **false**.

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

[**MSFT\_IPAM\_Server**](msft-ipam-server.md)
</dt> </dl>

 

 





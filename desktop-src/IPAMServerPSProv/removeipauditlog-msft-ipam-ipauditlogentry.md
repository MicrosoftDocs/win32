---
Description: 'Deletes IP address audit events that occurred before the specified date.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'ccc723ca-7d33-4d39-bda3-b3bf39562bf5'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'RemoveIpAuditLog method of the MSFT\_IPAM\_IpAuditLogEntry class'
---

# RemoveIpAuditLog method of the MSFT\_IPAM\_IpAuditLogEntry class

Deletes IP address audit events that occurred before the specified date.

## Syntax


```mof
uint32 RemoveIpAuditLog(
  [in]  datetime                  EndDate,
  [out] MSFT_IPAM_IpAuditLogEntry Output[]
);
```



## Parameters

<dl> <dt>

*EndDate* \[in\]
</dt> <dd>

The end date for deleting the events.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

When this method returns, this parameter contains an array of the deleted log entry objects.

</dd> </dl>

## Return value

Returns "0" on success, otherwise returns a WMI error code.

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

[**MSFT\_IPAM\_IpAuditLogEntry**](msft-ipam-ipauditlogentry.md)
</dt> </dl>

 

 





---
Description: 'Deletes all DHCP configuration events that occurred before the specified date.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '0a63d214-31aa-4854-8bf1-a2198087ae54'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'RemoveDhcpConfigurationEvent method of the MSFT\_IPAM\_DhcpConfigLogEntry class'
---

# RemoveDhcpConfigurationEvent method of the MSFT\_IPAM\_DhcpConfigLogEntry class

Deletes all DHCP configuration events that occurred before the specified date.

## Syntax


```mof
uint32 RemoveDhcpConfigurationEvent(
  [in]  datetime                     EndDate,
  [out] MSFT_IPAM_DhcpConfigLogEntry Output[]
);
```



## Parameters

<dl> <dt>

*EndDate* \[in\]
</dt> <dd>

The end date for deleting the configuration events.

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

[**MSFT\_IPAM\_DhcpConfigLogEntry**](msft-ipam-dhcpconfiglogentry.md)
</dt> </dl>

 

 





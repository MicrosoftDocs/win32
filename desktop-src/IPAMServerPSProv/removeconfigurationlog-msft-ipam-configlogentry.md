---
Description: 'Deletes all IPAM configuration events that occurred before the specified Date.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '4759a5d5-2a94-44ab-a41a-9d479e962b88'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'RemoveConfigurationLog method of the MSFT\_IPAM\_ConfigLogEntry class'
---

# RemoveConfigurationLog method of the MSFT\_IPAM\_ConfigLogEntry class

Deletes all IPAM configuration events that occurred before the specified Date.

## Syntax


```mof
uint32 RemoveConfigurationLog(
  [in]  datetime                 EndDate,
  [out] MSFT_IPAM_ConfigLogEntry Output[]
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

[**MSFT\_IPAM\_ConfigLogEntry**](msft-ipam-configlogentry.md)
</dt> </dl>

 

 





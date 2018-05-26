---
Description: Deletes an infrastructure server from the IPAM server inventory.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 05439188-4359-4274-84ca-480adc90daf5
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: RemoveIpamServerInventory method of the MSFT\_IPAM\_ServerInventory class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoveIpamServerInventory method of the MSFT\_IPAM\_ServerInventory class

Deletes an infrastructure server from the IPAM server inventory.

## Syntax


```mof
uint32 RemoveIpamServerInventory(
  [in]  string                    Name[],
  [out] MSFT_IPAM_ServerInventory Output[]
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the server remove.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

When this method returns, this parameter contains the updated server object.

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

[**MSFT\_IPAM\_ServerInventory**](msft-ipam-serverinventory.md)
</dt> </dl>

 

 





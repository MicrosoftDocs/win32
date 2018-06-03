---
title: GetByAll method of the PS\_VpnS2SInterfaceStatistics class
description: Retrieves statistics of an S2S interface for all connections.
audience: developer
ms.assetid: f41db730-6e85-4728-8423-a2992210900d
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetByAll method
- GetByAll method, PS_VpnS2SInterfaceStatistics class
- PS_VpnS2SInterfaceStatistics class, GetByAll method
topic_type:
- apiref
api_name:
- PS_VpnS2SInterfaceStatistics.GetByAll
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetByAll method of the PS\_VpnS2SInterfaceStatistics class

Retrieves statistics of an S2S interface for all connections.

## Syntax


```mof
uint32 GetByAll(
  [in]  boolean                   Clear,
  [in]  boolean                   Force,
  [out] VpnS2SInterfaceStatistics cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Clear* \[in\]
</dt> <dd>

Indicates whether to delete the statistics. **True** to delete the statistics; otherwise **false**.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Indicates whether this method displays the default confirmation prompt to the user. **True** to display the default confirmation prompt; otherwise **false**.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The [**VpnS2SInterfaceStatistics**](vpns2sinterfacestatistics.md) object that receives the statistics.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_VpnS2SInterfaceStatistics**](ps-vpns2sinterfacestatistics.md)
</dt> </dl>

 

 






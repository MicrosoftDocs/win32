---
title: Get method of the PS\_VpnS2SInterfaceStatistics class
description: Retrieves statistics of an S2S interface for the specified VPN connection.
audience: developer
ms.assetid: 1702a123-3762-4666-97e6-567df8f844ae
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_VpnS2SInterfaceStatistics class
- PS_VpnS2SInterfaceStatistics class, Get method
topic_type:
- apiref
api_name:
- PS_VpnS2SInterfaceStatistics.Get
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Get method of the PS\_VpnS2SInterfaceStatistics class

Retrieves statistics of an S2S interface for the specified VPN connection.

## Syntax


```mof
uint32 Get(
  [in]  string                    Name,
  [in]  boolean                   Clear,
  [in]  boolean                   Force,
  [out] VpnS2SInterfaceStatistics cmdletOutput
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

Specifies the name of the connection.

</dd> <dt>

*Clear* \[in\]
</dt> <dd>

Indicates whether to delete the statistics. **True** to delete the statistics; otherwise **false**.

**Windows Server 2012:** This parameter is not available before Windows Server 2012 R2.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Indicates whether this method displays the default confirmation prompt to the user. **True** to display the default confirmation prompt; otherwise **false**.

**Windows Server 2012:** This parameter is not available before Windows Server 2012 R2.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The cmdlet output.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_VpnS2SInterfaceStatistics**](ps-vpns2sinterfacestatistics.md)
</dt> </dl>

 

 






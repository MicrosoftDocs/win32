---
title: GetServerInventory method of the MSFT\_ServerManagerTasks class
description: Retrieves the basic inventory information of the server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '3444d7fa-f3f3-40a0-82bc-2f6f99939975'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetServerInventory method", "GetServerInventory method, MSFT_ServerManagerTasks class", "MSFT_ServerManagerTasks class, GetServerInventory method"]
topic_type:
- apiref
api_name:
- MSFT_ServerManagerTasks.GetServerInventory
api_location:
- MgmtProvider.dll
api_type:
- COM
---

# GetServerInventory method of the MSFT\_ServerManagerTasks class

Retrieves the basic inventory information of the server.

## Syntax


```mof
uint32 GetServerInventory(
  [in]  string                        SMServerId,
  [out] MSFT_ServerInventory          ServerInventory,
  [out] MSFT_ServerOperatingSystem    OperatingSystem,
  [out] MSFT_ServerClusterInformation ClusterInformation,
  [out] MSFT_ServerNetworkAdapter     NetworkAdapters[],
  [out] MSFT_ServerEventLog           EventLogs[]
);
```



## Parameters

<dl> <dt>

*SMServerId* \[in\]
</dt> <dd>

Optional parameter specifying the name used in the server manager to add the managed node.

</dd> <dt>

*ServerInventory* \[out\]
</dt> <dd>

An embedded instance of the [**MSFT\_ServerInventory**](msft-serverinventory.md) class that represents the miscellaneous inventory information of the server.

</dd> <dt>

*OperatingSystem* \[out\]
</dt> <dd>

An embedded instance of the [**MSFT\_ServerOperatingSystem**](msft-serveroperatingsystem.md) class that represents the operating system details of the server.

</dd> <dt>

*ClusterInformation* \[out\]
</dt> <dd>

An embedded instance of the [**MSFT\_ServerClusterInformation**](msft-serverclusterinformation.md) class that represents the cluster information of the server.

</dd> <dt>

*NetworkAdapters* \[out\]
</dt> <dd>

An array of embedded instances of the [**MSFT\_ServerNetworkAdapter**](msft-servernetworkadapter.md) class that represent the list of network adapters installed on the server.

</dd> <dt>

*EventLogs* \[out\]
</dt> <dd>

An array of embedded instances of the [**MSFT\_ServerEventLog**](msft-servereventlog.md) class that represent the list of event logs installed on the server.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\Windows\\ServerManager<br/>                                                     |
| MOF<br/>                      | <dl> <dt>MgmtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MgmtProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_ServerManagerTasks**](msft-servermanagertasks.md)
</dt> <dt>

[**MSFT\_ServerInventory**](msft-serverinventory.md)
</dt> <dt>

[**MSFT\_ServerOperatingSystem**](msft-serveroperatingsystem.md)
</dt> <dt>

[**MSFT\_ServerClusterInformation**](msft-serverclusterinformation.md)
</dt> <dt>

[**MSFT\_ServerNetworkAdapter**](msft-servernetworkadapter.md)
</dt> <dt>

[**MSFT\_ServerEventLog**](msft-servereventlog.md)
</dt> </dl>

 

 






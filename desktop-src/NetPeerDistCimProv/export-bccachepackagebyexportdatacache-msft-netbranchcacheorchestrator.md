---
Description: Exports a cache package.
ms.assetid: 107b5005-63b5-4dd0-9fcf-d5921a81db56
title: Export\_BCCachePackageByExportDataCache method of the MSFT\_NetBranchCacheOrchestrator class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Export\_BCCachePackageByExportDataCache method of the MSFT\_NetBranchCacheOrchestrator class

Exports a cache package

## Syntax


```mof
uint32 Export_BCCachePackageByExportDataCache(
  [in] boolean ExportDataCache,
  [in] string  Destination,
  [in] boolean Force
);
```



## Parameters

<dl> <dt>

*ExportDataCache* \[in\]
</dt> <dd>

Indicates the contents of the local data cache will be included in the package

</dd> <dt>

*Destination* \[in\]
</dt> <dd>

Specifies the path to the data package

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Indicates the operation should not prompt for confirmation

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>NetPeerDistCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetPeerDistCim.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_NetBranchCacheOrchestrator**](msft-netbranchcacheorchestrator.md)
</dt> </dl>

 

 





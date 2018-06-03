---
Description: Creates hashes for web content.
ms.assetid: 86ea8ba3-851b-4f4c-a2ac-64b4457d24a7
title: Publish\_BCWebHashes method of the MSFT\_NetBranchCacheOrchestrator class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Publish\_BCWebHashes method of the MSFT\_NetBranchCacheOrchestrator class

Creates hashes for web content.

## Syntax


```mof
uint32 Publish_BCWebHashes(
  [in] string               Path[],
  [in] uint32               UseVersion,
  [in] boolean              StageData,
  [in] string               StagingPath,
  [in] string ReferenceFile In,
  [in] boolean              Force
);
```



## Parameters

<dl> <dt>

*Path* \[in\]
</dt> <dd>

Specifies the file or folder to be hashed

</dd> <dt>

*UseVersion* \[in\]
</dt> <dd>

Specifies the version of the BranchCache hashing scheme to use

</dd> <dt>

*StageData* \[in\]
</dt> <dd>

Indicates the hashes should be saved to a staging area for future export

</dd> <dt>

*StagingPath* \[in\]
</dt> <dd>

Specifies a temporary folder to output staging data to

</dd> <dt>

*In* \[in\]
</dt> <dd>

Specifies a reference file from a previous execution

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

 

 





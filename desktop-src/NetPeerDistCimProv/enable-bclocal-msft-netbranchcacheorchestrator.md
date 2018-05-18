---
Description: 'Enables the BranchCache service in local caching mode.'
ms.assetid: '24b6f1d0-1fd6-4785-a879-482a5017949e'
title: 'Enable\_BCLocal method of the MSFT\_NetBranchCacheOrchestrator class'
---

# Enable\_BCLocal method of the MSFT\_NetBranchCacheOrchestrator class

Enables the BranchCache service in local caching mode.

## Syntax


```mof
uint32 Enable_BCLocal(
  [in] string  PolicyStore,
  [in] boolean Force
);
```



## Parameters

<dl> <dt>

*PolicyStore* \[in\]
</dt> <dd>

Path to the group policy object that should be modified by this cmdlet.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Indicates the operation should not prompt for confirmation

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>NetPeerDistCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetPeerDistCim.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_NetBranchCacheOrchestrator**](msft-netbranchcacheorchestrator.md)
</dt> </dl>

 

 





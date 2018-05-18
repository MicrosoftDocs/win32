---
Description: 'Resets BranchCache to a default configuration.'
ms.assetid: 'e11b37f7-648c-4bc0-91e5-c5876fcfb2d0'
title: 'Reset\_BC method of the MSFT\_NetBranchCacheOrchestrator class'
---

# Reset\_BC method of the MSFT\_NetBranchCacheOrchestrator class

Resets BranchCache to a default configuration.

## Syntax


```mof
uint32 Reset_BC(
  [in] boolean ResetFWRulesOnly,
  [in] boolean ResetPerfCountersOnly,
  [in] boolean Force
);
```



## Parameters

<dl> <dt>

*ResetFWRulesOnly* \[in\]
</dt> <dd>

If True, resets only the Windows firewall rules.

</dd> <dt>

*ResetPerfCountersOnly* \[in\]
</dt> <dd>

If True, resets only the Performance Counters.

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

 

 





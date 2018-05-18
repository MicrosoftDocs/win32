---
Description: 'Sets the cryptographic key used in the generation of segment secrets.'
ms.assetid: '18621201-3080-4316-9797-af0304542a08'
title: 'Set\_BCSecretKey method of the MSFT\_NetBranchCacheOrchestrator class'
---

# Set\_BCSecretKey method of the MSFT\_NetBranchCacheOrchestrator class

Sets the cryptographic key used in the generation of segment secrets.

## Syntax


```mof
uint32 Set_BCSecretKey(
  [in] string  Passphrase,
  [in] boolean Force
);
```



## Parameters

<dl> <dt>

*Passphrase* \[in\]
</dt> <dd>

Passphrase to use in the computation of the server secret key.

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

 

 





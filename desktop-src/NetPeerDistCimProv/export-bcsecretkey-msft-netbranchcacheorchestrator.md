---
Description: Exports a secret key to a file.
ms.assetid: 64563c44-0058-48ee-940e-2e47745e3d7f
title: Export\_BCSecretKey method of the MSFT\_NetBranchCacheOrchestrator class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Export\_BCSecretKey method of the MSFT\_NetBranchCacheOrchestrator class

Exports a secret key to a file.

## Syntax


```mof
uint32 Export_BCSecretKey(
  [in] string  Filename,
  [in] string  FilePassphrase,
  [in] boolean Force
);
```



## Parameters

<dl> <dt>

*Filename* \[in\]
</dt> <dd>

Path of the file that will contain the key information.

</dd> <dt>

*FilePassphrase* \[in\]
</dt> <dd>

Passphrase used to encrypt the file containing the key information.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Indicates the operation should not prompt for confirmation.

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

 

 





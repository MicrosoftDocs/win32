---
Description: Imports the cryptographic key used in the generation of segment secrets.
ms.assetid: 366eca8d-ce16-4f94-a43a-916c0be98b8b
title: Import\_BCSecretKey method of the MSFT\_NetBranchCacheOrchestrator class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Import\_BCSecretKey method of the MSFT\_NetBranchCacheOrchestrator class

Imports the cryptographic key used in the generation of segment secrets.

## Syntax


```mof
uint32 Import_BCSecretKey(
  [in] string  Filename,
  [in] string  FilePassphrase,
  [in] boolean Force
);
```



## Parameters

<dl> <dt>

*Filename* \[in\]
</dt> <dd>

Path of the file containing the key information to import.

</dd> <dt>

*FilePassphrase* \[in\]
</dt> <dd>

Passphrase for the file containing the key information.

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

 

 





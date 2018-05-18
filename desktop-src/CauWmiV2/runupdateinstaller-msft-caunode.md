---
title: RunUpdateInstaller method of the MSFT\_CAUNode class
description: Runs the update installer out of process on the node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f53bdbe4-9216-48e7-b671-2f73d2655a85'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-aware-patching'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RunUpdateInstaller method", "RunUpdateInstaller method, MSFT_CAUNode class", "MSFT_CAUNode class, RunUpdateInstaller method"]
topic_type:
- apiref
api_name:
- MSFT_CAUNode.RunUpdateInstaller
api_location:
- CauWmiV2.dll
api_type:
- COM
---

# RunUpdateInstaller method of the MSFT\_CAUNode class

Runs the update installer out of process on the node.

## Syntax


```mof
uint32 RunUpdateInstaller(
  [in]  string                           InstallerProgramPath,
  [in]  string                           Parameters,
  [in]  string                           UpdatePath,
  [in]  boolean                          RequireSmbEncryption,
  [out] MSFT_CAU_Update_Installer_Result Result
);
```



## Parameters

<dl> <dt>

*InstallerProgramPath* \[in\]
</dt> <dd>

The full path to the installer program. The path must be contained in quotation marks.

</dd> <dt>

*Parameters* \[in\]
</dt> <dd>

The parameters to the installer program.

</dd> <dt>

*UpdatePath* \[in\]
</dt> <dd>

The path to the update file.

</dd> <dt>

*RequireSmbEncryption* \[in\]
</dt> <dd>

**True** to require SMB Encryption to be enabled in a hotfix file share before installing the update; otherwise, **false**.

</dd> <dt>

*Result* \[out\]
</dt> <dd>

An embedded instance of [**MSFT\_CAU\_Update\_Installer\_Result**](msft-cau-update-installer-result.md) representing the result of the run installer.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\ClusterUpdate<br/>                                      |
| MOF<br/>                      | <dl> <dt>CAUWMIv2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CauWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_CAUNode**](msft-caunode.md)
</dt> </dl>

 

 






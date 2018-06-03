---
title: GetEffectiveNamespace method of the MSFT\_FSRMEffectiveNamespace class
description: Returns a list of paths that match the static namespaces in the input list and any namespaces that have a Folder Usage property set on them with a value in the input list.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 90de868b-5ab5-4397-90cf-d165af66dcfb
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- GetEffectiveNamespace method File Server Resource Manager
- GetEffectiveNamespace method File Server Resource Manager , MSFT_FSRMEffectiveNamespace class
- MSFT_FSRMEffectiveNamespace class File Server Resource Manager , GetEffectiveNamespace method
topic_type:
- apiref
api_name:
- MSFT_FSRMEffectiveNamespace.GetEffectiveNamespace
api_location:
- SrmSvc.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetEffectiveNamespace method of the MSFT\_FSRMEffectiveNamespace class

Returns a list of paths that match the static namespaces in the input list and any namespaces that have a Folder Usage property set on them with a value in the input list.

## Syntax


```mof
uint64 GetEffectiveNamespace(
  [in]  string Namespace[],
  [out] string EffectiveNamespace[]
);
```



## Parameters

<dl> <dt>

*Namespace* \[in\]
</dt> <dd>

An array of strings, each of which must be either a value of the **FolderUsage** property defined on the server (also called dynamic namespaces) or a static path (also called static namespaces). If providing **FolderUsage** properties, the format "\[FolderUsage\_MS=*value*\]" must be used. This parameter is required. The default value is an empty list.

</dd> <dt>

*EffectiveNamespace* \[out\]
</dt> <dd>

A list of all paths that the provided object considers in scope on the server. If the *Namespace* parameter was not empty, the list of all paths covered by the namespaces provided.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\FSRM<br/>                                                 |
| MOF<br/>                      | <dl> <dt>MSFT\_FSRM.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SrmSvc.dll</dt> </dl>     |



## See also

<dl> <dt>

[**MSFT\_FSRMEffectiveNamespace**](msft-fsrmeffectivenamespace.md)
</dt> </dl>

 

 






---
title: MSFT\_FSRMEffectiveNamespace class
description: A class that represents the namespaces in scope on the server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: cf33be57-ced8-41af-8caa-e1838ad67908
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- MSFT_FSRMEffectiveNamespace class File Server Resource Manager
- MSFT_FSRMEffectiveNamespace class File Server Resource Manager , described
topic_type:
- apiref
api_name:
- MSFT_FSRMEffectiveNamespace
api_location:
- SrmSvc.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_FSRMEffectiveNamespace class

A class that represents the namespaces in scope on the server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("FSRMWmiProvider")]
class MSFT_FSRMEffectiveNamespace
{
};
```

## Members

The **MSFT\_FSRMEffectiveNamespace** class has these types of members:

-   [Methods](#methods)

### Methods

The **MSFT\_FSRMEffectiveNamespace** class has these methods.



| Method                                                                             | Description                                                                                                                                                                            |
|:-----------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetEffectiveNamespace**](msft-fsrmeffectivenamespace-geteffectivenamespace.md) | Returns a list of paths that match the static namespaces in the input list and any namespaces that have a Folder Usage property set on them with a value in the input list.<br/> |



 

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

[FSRM WMI Classes](fsrm-wmi-classes.md)
</dt> </dl>

 

 






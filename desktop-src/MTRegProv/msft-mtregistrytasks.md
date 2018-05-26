---
title: MSFT\_MTRegistryTasks class
description: Encapsulates different tasks exposed by registry.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 74fe5a12-66f6-4e05-bb0f-aacde6783264
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_MTRegistryTasks class
- MSFT_MTRegistryTasks class, described
topic_type:
- apiref
api_name:
- MSFT_MTRegistryTasks
api_location:
- RegProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_MTRegistryTasks class

Encapsulates different tasks exposed by registry.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("regprov"), AMENDMENT]
class MSFT_MTRegistryTasks
{
};
```

## Members

The **MSFT\_MTRegistryTasks** class has these types of members:

-   [Methods](#methods)

### Methods

The **MSFT\_MTRegistryTasks** class has these methods.



| Method                                        | Description                                                                                     |
|:----------------------------------------------|:------------------------------------------------------------------------------------------------|
| [**Search**](search-msft-mtregistrytasks.md) | Searches the specified string in registry tree represented by the root registry key.<br/> |



 

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                         |
| Namespace<br/>                | Root\\Microsoft\\Windows\\ManagementTools<br/>                                   |
| MOF<br/>                      | <dl> <dt>RegProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RegProv.dll</dt> </dl> |



 

 






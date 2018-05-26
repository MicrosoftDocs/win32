---
title: PS\_BgpRouter class
description: Manages a Border Gateway Protocol (BGP) router.
audience: developer
ms.assetid: 422cd005-edd7-49f5-ba3b-6d01bb5d5394
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_BgpRouter class
- PS_BgpRouter class, described
topic_type:
- apiref
api_name:
- PS_BgpRouter
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_BgpRouter class

Manages a Border Gateway Protocol (BGP) router.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_BgpRouter
{
};
```

## Members

The **PS\_BgpRouter** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_BgpRouter** class has these methods.



| Method                                | Description                                                         |
|:--------------------------------------|:--------------------------------------------------------------------|
| [**Add**](add-ps-bgprouter.md)       | Adds a new BGP router to the specified tenant.<br/>           |
| [**Get**](get-ps-bgprouter.md)       | Retrieves the configuration information of a BGP router.<br/> |
| [**Remove**](remove-ps-bgprouter.md) | Removes a BGP router from the associated tenants.<br/>        |
| [**Set**](set-ps-bgprouter.md)       | Updates the configuration of a BGP router.<br/>               |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 






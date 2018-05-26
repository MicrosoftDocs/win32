---
title: PS\_DAMgmtServer class
description: Represents the Management Server configuration in a DirectAccess deployment.
audience: developer
ms.assetid: f35e6054-c7f6-4914-adc1-a4e5f1b402e1
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DAMgmtServer class
- PS_DAMgmtServer class, described
topic_type:
- apiref
api_name:
- PS_DAMgmtServer
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DAMgmtServer class

Represents the Management Server configuration in a DirectAccess deployment.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_DAMgmtServer
{
};
```

## Members

The **PS\_DAMgmtServer** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DAMgmtServer** class has these methods.



| Method                                   | Description                                                                                                                                                                  |
|:-----------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Add**](add-ps-damgmtserver.md)       | This cmdlet adds the specified Management servers to the DA deployment. Management server here refers to patch servers, Domain Controllers and other servers<br/>      |
| [**Get**](get-ps-damgmtserver.md)       | This cmdlet displays the configured Management servers. Management server here refers to patch servers, Domain Controllers and other servers<br/>                      |
| [**Remove**](remove-ps-damgmtserver.md) | This cmdlet removes the specified Management servers from the DA deployment. Management server here refers to patch servers, Domain Controllers and other servers<br/> |
| [**Update**](update-ps-damgmtserver.md) | This cmdlet updates the list of Management servers of the DA deployment. Management server here refers to patch servers, Domain Controllers and other servers<br/>     |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 






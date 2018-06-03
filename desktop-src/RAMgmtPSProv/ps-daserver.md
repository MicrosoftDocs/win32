---
title: PS\_DAServer class
description: Represents the configuration specific to the DirectAccess server.
audience: developer
ms.assetid: b105dfda-b568-4067-a095-126221c37932
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DAServer class
- PS_DAServer class, described
topic_type:
- apiref
api_name:
- PS_DAServer
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DAServer class

Represents the configuration specific to the DirectAccess server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("2.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_DAServer
{
};
```

## Members

The **PS\_DAServer** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DAServer** class has these methods.



| Method                                                                             | Description                                                          |
|:-----------------------------------------------------------------------------------|:---------------------------------------------------------------------|
| [**Get**](get-ps-daserver.md)                                                     | This cmdlet displays the properties of the DA Server<br/>      |
| [**SetByChangeDAInstallationType**](setbychangedainstallationtype-ps-daserver.md) | This cmdlet sets the properties specific to the DA server<br/> |
| [**SetByDisableComputerCertAuth**](setbydisablecomputercertauth-ps-daserver.md)   | This cmdlet sets the properties specific to the DA server<br/> |
| [**SetByEnableComputerCertAuth**](setbyenablecomputercertauth-ps-daserver.md)     | This cmdlet sets the properties specific to the DA server<br/> |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 






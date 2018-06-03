---
title: PS\_DAEntryPoint class
description: Describes a entry point which belongs to a multisite deployment.
audience: developer
ms.assetid: 67390648-c647-4b9b-b4a4-1f45efb76897
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DAEntryPoint class
- PS_DAEntryPoint class, described
topic_type:
- apiref
api_name:
- PS_DAEntryPoint
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DAEntryPoint class

Describes a entry point which belongs to a multisite deployment.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_DAEntryPoint
{
};
```

## Members

The **PS\_DAEntryPoint** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DAEntryPoint** class has these methods.



| Method                                   | Description                                                                                                                                                                 |
|:-----------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Add**](add-ps-daentrypoint.md)       | Adds an entry point to a multisite deployment. The cmdlet verifies DirectAccess prerequisites and adds the server as an entry point to the multisite deployment.<br/> |
| [**Get**](get-ps-daentrypoint.md)       | Displays the settings for an entry point.<br/>                                                                                                                        |
| [**Remove**](remove-ps-daentrypoint.md) | Removes an entry point from a multisite deployment.<br/>                                                                                                              |
| [**Set**](set-ps-daentrypoint.md)       | Configures settings for the entry point.<br/>                                                                                                                         |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 






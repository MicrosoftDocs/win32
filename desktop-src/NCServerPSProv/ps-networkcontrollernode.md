---
title: PS\_NetworkControllerNode class
description: Represents the Network Controller server provider functions for node level. The methods exposed by this class are performed for the local node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 95b8fbe1-1561-4774-b36e-8537bd40c7aa
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_NetworkControllerNode class
- PS_NetworkControllerNode class, described
topic_type:
- apiref
api_name:
- PS_NetworkControllerNode
api_location:
- NCServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_NetworkControllerNode class

Represents the Network Controller server provider functions for node level. The methods exposed by this class are performed for the local node.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("NcServerPSProvider"), AMENDMENT]
class PS_NetworkControllerNode
{
};
```

## Members

The **PS\_NetworkControllerNode** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_NetworkControllerNode** class has these methods.



| Method                                                                                      | Description                                                                                                    |
|:--------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------|
| [**Configure**](configure-ps-networkcontrollernode.md)                                     | Configures the node.<br/>                                                                                |
| [**GetManifestVersion**](getmanifestversion-ps-networkcontrollernode.md)                   | Returns the Network Controller cluster and application version defined in their template manifests.<br/> |
| [**GetServiceFabricVersion**](ps-networkcontrollernode-getservicefabricversion.md)         | Retrieves the service fabric version.<br/>                                                               |
| [**LogEvent**](logevent-ps-networkcontrollernode.md)                                       | Logs an event on the node.<br/>                                                                          |
| [**LogFailureEvent**](ps-networkcontrollernode-logfailureevent.md)                         | Logs failure event on the node.<br/>                                                                     |
| [**SyncNode**](ps-networkcontrollernode-syncnode.md)                                       | Syncs the node to install/uninstall any missing/extra updates.<br/>                                      |
| [**Unconfigure**](unconfigure-ps-networkcontrollernode.md)                                 | Unconfigures the node.<br/>                                                                              |
| [**UpdateConfigStoreForUpdates**](ps-networkcontrollernode-updateconfigstoreforupdates.md) | Updates the config store based on the update parameters.<br/>                                            |
| [**UpdateNodeConfiguration**](ps-networkcontrollernode-updatenodeconfiguration.md)         | Updates the Node configuration.<br/>                                                                     |
| [**Validate**](validate-ps-networkcontrollernode.md)                                       | Performs validations on the node.<br/>                                                                   |



 

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\NetworkController\\Server<br/>                                    |
| MOF<br/>                      | <dl> <dt>NCServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NCServerPSProvider.dll</dt> </dl> |



 

 






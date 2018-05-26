---
Description: Manages server components asynchronously.
audience: developer
ms.assetid: 40caa497-a3f4-43a7-97af-b03c25e9a44d
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: MSFT\_ServerManagerDeploymentTasks class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_ServerManagerDeploymentTasks class

Manages server components asynchronously.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("deploymentprovider")]
class MSFT_ServerManagerDeploymentTasks
{
};
```

## Members

The **MSFT\_ServerManagerDeploymentTasks** class has these types of members:

-   [Methods](#methods)

### Methods

The **MSFT\_ServerManagerDeploymentTasks** class has these methods.



| Method                                                                                                   | Description                                                                                                |
|:---------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------|
| [**AddServerComponentAsync**](addservercomponentasync-msft-servermanagerdeploymenttasks.md)             | Asynchronously installs a server component on a managed node.<br/>                                   |
| [**AddServerComponentVhdAsync**](addservercomponentvhdasync-msft-servermanagerdeploymenttasks.md)       | Asynchronously installs a server component on a VHD of a managed node.<br/>                          |
| [**GetAlterationRequestState**](getalterationrequeststate-msft-servermanagerdeploymenttasks.md)         | Retrieves the state of a deployment request.<br/>                                                    |
| [**GetEnumerationRequestState**](getenumerationrequeststate-msft-servermanagerdeploymenttasks.md)       | Updates the state of a deployment request.<br/>                                                      |
| [**GetServerComponentsAsync**](getservercomponentsasync-msft-servermanagerdeploymenttasks.md)           | Asynchronously retrieves the server components for the specified deployment request.<br/>            |
| [**GetServerComponentsVhdAsync**](getservercomponentsvhdasync-msft-servermanagerdeploymenttasks.md)     | Asynchronously retrieves the server components from a VHD for the specified deployment request.<br/> |
| [**RemoveServerComponentAsync**](removeservercomponentasync-msft-servermanagerdeploymenttasks.md)       | Asynchronously uninstalls a server component from a managed node.<br/>                               |
| [**RemoveServerComponentVhdAsync**](removeservercomponentvhdasync-msft-servermanagerdeploymenttasks.md) | Asynchronously uninstalls a server component from a VHD on a managed node.<br/>                      |



 

## Requirements



|                                     |                                                                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                                  |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                                                  |
| MOF<br/>                      | <dl> <dt>ServerManager.DeploymentProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ServerManager.DeploymentProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[ServerManager Deploymentprovider Provider Classes](server-manager-deployment.md)
</dt> </dl>

 

 





---
Description: Represents a system service that is managed by a server component.
audience: developer
ms.assetid: 8679f2ce-a7fe-48ec-a6b1-7741280c4b81
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: MSFT\_ServiceToMonitor class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_ServiceToMonitor class

Represents a system service that is managed by a server component.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("deploymentprovider")]
class MSFT_ServiceToMonitor
{
  String  Name;
  Boolean DefaultMonitoring;
};
```

## Members

The **MSFT\_ServiceToMonitor** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_ServiceToMonitor** class has these properties.

<dl> <dt>

**DefaultMonitoring**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether default monitoring of the system service is enabled by default. True to enable default monitoring by default; otherwise false.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the system service.

</dd> </dl>

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

 

 





---
Description: Represents a GUID that uniquely identifies a request.
audience: developer
ms.assetid: 30cd1c23-0a8f-437f-9b61-f50339a1848a
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: MSFT\_ServerManagerRequestGuid class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_ServerManagerRequestGuid class

Represents a **GUID** that uniquely identifies a request.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("deploymentprovider")]
class MSFT_ServerManagerRequestGuid
{
  uint64 HighHalf;
  uint64 LowHalf;
};
```

## Members

The **MSFT\_ServerManagerRequestGuid** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_ServerManagerRequestGuid** class has these properties.

<dl> <dt>

**HighHalf**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The first half of the **GUID**.

</dd> <dt>

**LowHalf**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The second half of the **GUID**.

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

 

 





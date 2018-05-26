---
title: MSFT\_CAU\_Update\_Installer\_Result class
description: A dynamic WMI class that contains the result and return codes for the update installer.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 214cb401-b722-4d68-b05e-98a5dbe4efd0
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-aware-patching
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_CAU_Update_Installer_Result class
- MSFT_CAU_Update_Installer_Result class, described
topic_type:
- apiref
api_name:
- MSFT_CAU_Update_Installer_Result
- MSFT_CAU_Update_Installer_Result.LaunchInstallerHResult
- MSFT_CAU_Update_Installer_Result.ReturnCode
api_location:
- CauWmiV2.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_CAU\_Update\_Installer\_Result class

A dynamic [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that contains the result and return codes for the update installer.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("CAUWMIV2"), AMENDMENT]
class MSFT_CAU_Update_Installer_Result
{
  uint32 LaunchInstallerHResult;
  SInt32 ReturnCode;
};
```

## Members

The **MSFT\_CAU\_Update\_Installer\_Result** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_CAU\_Update\_Installer\_Result** class has these properties.

<dl> <dt>

**LaunchInstallerHResult**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the result code returned from the attempt to launch the update installer.

</dd> <dt>

**ReturnCode**
</dt> <dd> <dl> <dt>

Data type: **SInt32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the return code from the update installer itself.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\Microsoft\\Windows\\ClusterUpdate<br/>                                      |
| MOF<br/>                      | <dl> <dt>CAUWMIv2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CauWmiV2.dll</dt> </dl> |



 

 






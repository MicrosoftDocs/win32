---
title: Win32_RDMSDeploymentSettings class
description: Manages deployment settings for a virtual desktop collection.
ms.assetid: c33563d5-a388-46d3-b23a-797aab9d472a
ms.tgt_platform: multiple
keywords:
- Win32_RDMSDeploymentSettings class Remote Desktop Services
- Win32_RDMSDeploymentSettings class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_RDMSDeploymentSettings
api_location:
- RDMS.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_RDMSDeploymentSettings class

Manages deployment settings for a virtual desktop collection.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("Win32_RDManagement_Prov"), AMENDMENT]
class Win32_RDMSDeploymentSettings
{
};
```

## Members

The **Win32\_RDMSDeploymentSettings** class has these types of members:

-   [Methods](#methods)

### Methods

The **Win32\_RDMSDeploymentSettings** class has these methods.



| Method                                                                                                  | Description                                                                                                                       |
|:--------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------|
| [**GetBaseVHDPath**](getbasevhdpath-win32-rdmsdeploymentsettings.md)                                   | Retrieves the base path to the directory to which VHDs of the virtual desktop collection are deployed.<br/>                 |
| [**GetConnectionString**](win32-rdmsdeploymentsettings-getconnectionstring.md)                         | Retrieves the deployment-level database connection string.<br/>                                                             |
| [**GetDiffVHDPath**](getdiffvhdpath-win32-rdmsdeploymentsettings.md)                                   | Retrieves the directory path to which the differencing disks are deployed for a virtual desktop collection.<br/>            |
| [**GetExportPath**](getexportpath-win32-rdmsdeploymentsettings.md)                                     | Retrieves the directory path to which virtual machines are deployed for a virtual desktop collection.<br/>                  |
| [**GetInt32Property**](getint32property-win32-rdmsdeploymentsettings.md)                               | Retrieves an integer property for the deployment settings of a virtual desktop collection.<br/>                             |
| [**GetSecondaryConnectionString**](win32-rdmsdeploymentsettings-getsecondaryconnectionstring.md)       | Retrieves the deployment-level database secondary connection string, which may be used to support password expiration.<br/> |
| [**GetSMBPath**](getsmbpath-win32-rdmsdeploymentsettings.md)                                           | Retrieves the UNC path to the SMB share to which virtual machines of the virtual desktop collection are deployed.<br/>      |
| [**GetStringArrayDeploymentSetting**](getstringarraydeploymentsetting-win32-rdmsdeploymentsettings.md) | Retrieves the deployment settings for a virtual desktop collection.<br/>                                                    |
| [**GetStringProperty**](getstringproperty-win32-rdmsdeploymentsettings.md)                             | Retrieves a string property for the deployment settings of a virtual desktop collection.<br/>                               |
| [**RemoveDeploymentSetting**](removedeploymentsetting-win32-rdmsdeploymentsettings.md)                 | Deletes the deployment settings for a virtual desktop collection.<br/>                                                      |
| [**SetBaseVHDPath**](setbasevhdpath-win32-rdmsdeploymentsettings.md)                                   | Retrieves the base path to the directory to which VHDs of the virtual desktop collection are deployed.<br/>                 |
| [**SetConnectionString**](win32-rdmsdeploymentsettings-setconnectionstring.md)                         | Sets the deployment-level database connection string.<br/>                                                                  |
| [**SetDiffVHDPath**](setdiffvhdpath-win32-rdmsdeploymentsettings.md)                                   | Updates the directory path to which the differencing disks are deployed for a virtual desktop collection.<br/>              |
| [**SetExportPath**](setexportpath-win32-rdmsdeploymentsettings.md)                                     | Updates the directory path to which virtual machines are deployed for a virtual desktop collection.<br/>                    |
| [**SetInt32Property**](setint32property-win32-rdmsdeploymentsettings.md)                               | Updates an integer property for the deployment settings of a virtual desktop collection.<br/>                               |
| [**SetSecondaryConnectionString**](win32-rdmsdeploymentsettings-setsecondaryconnectionstring.md)       | Sets the deployment-level database secondary connection string.<br/>                                                        |
| [**SetSMBPath**](setsmbpath-win32-rdmsdeploymentsettings.md)                                           | Updates the UNC path to the SMB share to which virtual machines of the virtual desktop collection are deployed.<br/>        |
| [**SetStringArrayDeploymentSetting**](setstringarraydeploymentsetting-win32-rdmsdeploymentsettings.md) | Updates the deployment settings for a virtual desktop collection.<br/>                                                      |
| [**SetStringProperty**](setstringproperty-win32-rdmsdeploymentsettings.md)                             | Updates a string property for the deployment settings of a virtual desktop collection.<br/>                                 |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\cimv2\\rdms<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>         |



## See also

<dl> <dt>

[Remote Desktop Management Services Provider](rdms-api-reference.md)
</dt> </dl>

 

 






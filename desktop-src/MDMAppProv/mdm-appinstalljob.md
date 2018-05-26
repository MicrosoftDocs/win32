---
title: MDM\_AppInstallJob class
description: Represents a job that manages the installation, upgrade, or uninstallation of an application on a device that is registered with the Mobile Device Management (MDM) service.
ms.assetid: 5ee99bd5-893e-4df9-9619-0dbd71eb888d
keywords:
- MDM_AppInstallJob class MDM App Management
- MDM_AppInstallJob class MDM App Management , described
topic_type:
- apiref
api_name:
- MDM_AppInstallJob
- MDM_AppInstallJob.JobID
- MDM_AppInstallJob.PackageFullName
- MDM_AppInstallJob.Status
- MDM_AppInstallJob.LastError
- MDM_AppInstallJob.Progress
- MDM_AppInstallJob.CreationTime
- MDM_AppInstallJob.DownloadUrlList
- MDM_AppInstallJob.Dependencies
- MDM_AppInstallJob.DependencyUrlLists
- MDM_AppInstallJob.LicenseXml
- MDM_AppInstallJob.ActionType
- MDM_AppInstallJob.JobType
- MDM_AppInstallJob.DeploymentOptions
api_location:
- MDMAppProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MDM\_AppInstallJob class

\[The MDM Application Provider is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use the [EnterpriseAppManagement Configuration Service Provider (CSP)](https://msdn.microsoft.com/library/windows/hardware/dn904955).\]

Represents a job that manages the installation, upgrade, or uninstallation of an application on a device that is registered with the Mobile Device Management (MDM) service.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), Deprecated("No value"), dynamic, provider("MDMAppProv"), AMENDMENT]
class MDM_AppInstallJob
{
  string   JobID;
  string   PackageFullName;
  uint32   Status;
  uint32   LastError;
  uint32   Progress;
  datetime CreationTime;
  string   DownloadUrlList[];
  string   Dependencies[];
  string   DependencyUrlLists[];
  string   LicenseXml;
  uint32   ActionType;
  uint32   JobType;
  uint32   DeploymentOptions;
};
```

## Members

The **MDM\_AppInstallJob** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MDM\_AppInstallJob** class has these methods.



| Method                                           | Description                                                                                                    |
|:-------------------------------------------------|:---------------------------------------------------------------------------------------------------------------|
| [**CreateJob**](createjob-mdm-appinstalljob.md) | Creates a job to manage the installation, upgrade, or uninstallation of an application on a device.<br/> |



 

### Properties

The **MDM\_AppInstallJob** class has these properties.

<dl> <dt>

**ActionType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the action type for the job, which specifies that the job is for an install, uninstall, or upgrade operation.

</dd> <dt>

**CreationTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Date and time that specifies when the job was created.

</dd> <dt>

**Dependencies**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Array of dependent frameworks for the application.

</dd> <dt>

**DependencyUrlLists**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Array of URLs used to download application framework data.

</dd> <dt>

**DeploymentOptions**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the deployment options for a Windows Store App.

</dd> <dt>

**DownloadUrlList**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Array of URLs used to download installation data.

</dd> <dt>

**JobID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Key that specifies the unique ID of the application installation, upgrade, or uninstallation.

</dd> <dt>

**JobType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the application type, which specifies that the job is for a Windows Store App, web application, or remote application.

**Windows 8:** This property is not supported before Windows 8.1.

</dd> <dt>

**LastError**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Last error code for the job.

</dd> <dt>

**LicenseXml**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The package license.

**Windows 8.1 and Windows 8:** This property is not supported before Windows 8.1 Update.

</dd> <dt>

**PackageFullName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Full name of the package that contains the application.

</dd> <dt>

**Progress**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Progress of the job.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Status of the job.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                      |
| Minimum supported server<br/> | None supported<br/>                                                                 |
| Namespace<br/>                | Root\\cimv2\\mdm<br/>                                                               |
| MOF<br/>                      | <dl> <dt>MDMAppProv.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MDMAppProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Mobile Device Management Application Provider Classes](https://msdn.microsoft.com/library/dn610374)
</dt> </dl>

 

 






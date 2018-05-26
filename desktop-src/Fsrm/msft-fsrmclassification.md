---
title: MSFT\_FSRMClassification class
description: Represents a classification task.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 79571ae1-726e-491b-b41e-6cd10cdf3936
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- MSFT_FSRMClassification class File Server Resource Manager
- MSFT_FSRMClassification class File Server Resource Manager , described
topic_type:
- apiref
api_name:
- MSFT_FSRMClassification
- MSFT_FSRMClassification.Server
- MSFT_FSRMClassification.LastError
- MSFT_FSRMClassification.Status
- MSFT_FSRMClassification.ExcludeNamespace
- MSFT_FSRMClassification.Schedule
- MSFT_FSRMClassification.Continuous
- MSFT_FSRMClassification.ContinuousLog
- MSFT_FSRMClassification.ContinuousLogSize
api_location:
- SrmSvc.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_FSRMClassification class

Represents a classification task.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("FSRMWmiProvider")]
class MSFT_FSRMClassification
{
  string                 Server;
  string                 LastError;
  uint32                 Status;
  string                 ExcludeNamespace[];
  MSFT_FSRMScheduledTask Schedule;
  boolean                Continuous;
  boolean                ContinuousLog;
  uint64                 ContinuousLogSize;
};
```

## Members

The **MSFT\_FSRMClassification** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_FSRMClassification** class has these methods.



| Method                                         | Description                                                                                     |
|:-----------------------------------------------|:------------------------------------------------------------------------------------------------|
| [**Start**](msft-fsrmclassification-start.md) | Starts a classification job.<br/>                                                         |
| [**Stop**](msft-fsrmclassification-stop.md)   | Stops the running instance of a classification job.<br/>                                  |
| [**Wait**](msft-fsrmclassification-wait.md)   | Waits for the specified period of time or until classification has finished running.<br/> |



 

### Properties

The **MSFT\_FSRMClassification** class has these properties.

<dl> <dt>

**Continuous**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **True** real time classification is enabled.

</dd> <dt>

**ContinuousLog**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **True** real time classification logs are enabled.

</dd> <dt>

**ContinuousLogSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Maximum size, in bytes, of the real time classification log. If 0 then there is no limit.

</dd> <dt>

**ExcludeNamespace**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array of strings containing the list of folders to not include in classification or file management. Each folder may include "\[AllVolumes\]" at the start of a path to indicate the namespace should be excluded on all volumes. Each namespace may have the string " /s" appended to it. In that case all folders and files within that namespace will be excluded. If it is not present, only the files within the specified folder will be excluded. If one string is "\[Default\]", then the default values are added to the exclude namespaces.

</dd> <dt>

**LastError**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The error message from the last time classification was run.

</dd> <dt>

**Schedule**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_FSRMScheduledTask**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**MSFT\_FSRMScheduledTask**](msft-fsrmscheduledtask.md)")
</dt> </dl>

An optional [**MSFT\_FSRMScheduledTask**](msft-fsrmscheduledtask.md) instance that represents the schedule for this classification task.

</dd> <dt>

**Server**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

This property is reserved.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The running status of classification.

<dt>

<span id="NotRunning"></span><span id="notrunning"></span><span id="NOTRUNNING"></span>

<span id="NotRunning"></span><span id="notrunning"></span><span id="NOTRUNNING"></span>**NotRunning** (1)


</dt> <dd>

The classification job is not running.

</dd> <dt>

<span id="Queued"></span><span id="queued"></span><span id="QUEUED"></span>

<span id="Queued"></span><span id="queued"></span><span id="QUEUED"></span>**Queued** (2)


</dt> <dd>

The classification job is queued to run but is not running.

</dd> <dt>

<span id="Running"></span><span id="running"></span><span id="RUNNING"></span>

<span id="Running"></span><span id="running"></span><span id="RUNNING"></span>**Running** (3)


</dt> <dd>

The classification job is running.

</dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\FSRM<br/>                                                 |
| MOF<br/>                      | <dl> <dt>MSFT\_FSRM.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SrmSvc.dll</dt> </dl>     |



## See also

<dl> <dt>

[FSRM WMI Classes](fsrm-wmi-classes.md)
</dt> </dl>

 

 






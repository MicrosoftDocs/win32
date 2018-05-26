---
title: FSRM WMI Classes
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1CE772FA-CE33-4900-A499-058175A7C37E
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
description: 
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# FSRM WMI Classes

The following WMI Classes are part of the File Server Resource Manager (FSRM) API:

## In this section

<dl> <dt>

[**MSFT\_FSRMAction**](msft-fsrmaction.md)
</dt> <dd>

Represents a FSRM action that can be triggered in response to a quota, file management job, or file screen event.

</dd> <dt>

[**MSFT\_FSRMAdr**](msft-fsrmadr.md)
</dt> <dd>

Provides interfaces to determine why access was denied to a file and to send a request for access according to policies defined on the file server.

</dd> <dt>

[**MSFT\_FSRMADRSettings**](msft-fsrmadrsettings.md)
</dt> <dd>

Returns an object containing event settings as supplied by the server.

</dd> <dt>

[**MSFT\_FSRMAutoQuota**](msft-fsrmautoquota.md)
</dt> <dd>

Creates a new **AutoQuota** on the server with the provided configuration and returns the FSRM quota object.

</dd> <dt>

[**MSFT\_FSRMClassification**](msft-fsrmclassification.md)
</dt> <dd>

Represents a classification task.

</dd> <dt>

[**MSFT\_FSRMClassificationPropertyDefinition**](msft-fsrmclassificationpropertydefinition.md)
</dt> <dd>

Represents a classification property definition.

</dd> <dt>

[**MSFT\_FSRMClassificationPropertyValue**](msft-fsrmclassificationpropertyvalue.md)
</dt> <dd>

Represents a classification property value.

</dd> <dt>

[**MSFT\_FSRMClassificationRule**](msft-fsrmclassificationrule.md)
</dt> <dd>

Defines a classification rule.

</dd> <dt>

[**MSFT\_FSRMEffectiveNamespace**](msft-fsrmeffectivenamespace.md)
</dt> <dd>

A class that represents the namespaces in scope on the server.

</dd> <dt>

[**MSFT\_FSRMFileGroup**](msft-fsrmfilegroup.md)
</dt> <dd>

Used to define a group of files based on one or more file name patterns.

</dd> <dt>

[**MSFT\_FSRMFileManagementJob**](msft-fsrmfilemanagementjob.md)
</dt> <dd>

Defines a file management job.

</dd> <dt>

[**MSFT\_FSRMFileScreen**](msft-fsrmfilescreen.md)
</dt> <dd>

Used to configure a file screen that blocks groups of files from being saved to the specified directory.

</dd> <dt>

[**MSFT\_FSRMFileScreenException**](msft-fsrmfilescreenexception.md)
</dt> <dd>

Used to configure an exception that excludes the specified files from the file screening process.

</dd> <dt>

[**MSFT\_FSRMFileScreenTemplate**](msft-fsrmfilescreentemplate.md)
</dt> <dd>

Used to configure templates from which new file screens can be derived.

</dd> <dt>

[**MSFT\_FSRMFMJAction**](msft-fsrmfmjaction.md)
</dt> <dd>

Represents a file management job action object.

</dd> <dt>

[**MSFT\_FSRMFMJCondition**](msft-fsrmfmjcondition.md)
</dt> <dd>

Represents the file management job conditions.

</dd> <dt>

[**MSFT\_FSRMFMJNotification**](msft-fsrmfmjnotification.md)
</dt> <dd>

Represents a file management job notification.

</dd> <dt>

[**MSFT\_FSRMFMJNotificationAction**](msft-fsrmfmjnotificationaction.md)
</dt> <dd>

Represents a new file management job notification action.

</dd> <dt>

[**MSFT\_FSRMMacro**](msft-fsrmmacro.md)
</dt> <dd>

Represents a FSRM macro object.

</dd> <dt>

[**MSFT\_FSRMMgmtProperty**](msft-fsrmmgmtproperty.md)
</dt> <dd>

Represents a FSRM management property which is a classification property that includes "Folders" (2) in its [**MSFT\_FSRMClassificationPropertyDefinition.AppliesTo**](msft-fsrmclassificationpropertydefinition.md) property and whose **MSFT\_FSRMClassificationPropertyDefinition.Flags** property does not include the "Secure" (4) value.

</dd> <dt>

[**MSFT\_FSRMMgmtPropertyValue**](msft-fsrmmgmtpropertyvalue.md)
</dt> <dd>

Represents a FSRM management property name/value pair.

</dd> <dt>

[**MSFT\_FSRMQuota**](msft-fsrmquota.md)
</dt> <dd>

Used to define a quota for a specified directory and to retrieve use statistics.

</dd> <dt>

[**MSFT\_FSRMQuotaTemplate**](msft-fsrmquotatemplate.md)
</dt> <dd>

Used to configure templates from which new quota objects can be derived.

</dd> <dt>

[**MSFT\_FSRMQuotaThreshold**](msft-fsrmquotathreshold.md)
</dt> <dd>

Represents a quota threshold and the actions that will be taken when the threshold is reached.

</dd> <dt>

[**MSFT\_FSRMScheduledTask**](msft-fsrmscheduledtask.md)
</dt> <dd>

Represents a FSRM scheduled task object

</dd> <dt>

[**MSFT\_FSRMSettings**](msft-fsrmsettings.md)
</dt> <dd>

Represents the FSRM settings.

</dd> <dt>

[**MSFT\_FSRMStorageReport**](msft-fsrmstoragereport.md)
</dt> <dd>

Represents a storage report.

</dd> </dl>

 

 





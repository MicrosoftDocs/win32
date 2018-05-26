---
title: FSRM Interfaces
description: The following interfaces are part of the File Server Resource Manager (FSRM) API.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bbd888d9-1005-4173-8e82-ced13e68c09e
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# FSRM Interfaces

The following interfaces are part of the File Server Resource Manager (FSRM) API.

## In this section

<dl> <dt>

[**DIFsrmClassificationEvents**](/windows/previous-versions/FsrmTlb/?branch=master)
</dt> <dd>

Handles events that are received while processing a [**ClassifyFiles**](/windows/previous-versions/FsrmPipeline/nf-fsrmpipeline-ifsrmclassificationmanager2-classifyfiles?branch=master) call.

</dd> <dt>

[**IFsrmAccessDeniedRemediationClient**](/windows/previous-versions/Fsrm/nn-fsrm-ifsrmaccessdeniedremediationclient?branch=master)
</dt> <dd>

Used to show the Access Denied Remediation (ADR) client user interface.

</dd> <dt>

[**IFsrmAction**](/windows/previous-versions/Fsrm/nn-fsrm-ifsrmaction?branch=master)
</dt> <dd>

The base class for all FSRM action interfaces.

</dd> <dt>

[**IFsrmActionCommand**](/windows/previous-versions/Fsrm/nn-fsrm-ifsrmactioncommand?branch=master)
</dt> <dd>

Used to run a command or script in response to a quota, file screen, or file management job event.

</dd> <dt>

[**IFsrmActionEmail**](/windows/previous-versions/Fsrm/nn-fsrm-ifsrmactionemail?branch=master)
</dt> <dd>

Used to send an email message in response to a quota or file screen event.

</dd> <dt>

[**IFsrmActionEmail2**](/windows/previous-versions/Fsrm/nn-fsrm-ifsrmactionemail2?branch=master)
</dt> <dd>

Used to limit the number of expired files listed in the email notification.

</dd> <dt>

[**IFsrmActionEventLog**](/windows/previous-versions/Fsrm/nn-fsrm-ifsrmactioneventlog?branch=master)
</dt> <dd>

Used to log an event to the Windows Application event log in response to a quota, file screen, or file management job event.

</dd> <dt>

[**IFsrmActionReport**](/windows/previous-versions/Fsrm/nn-fsrm-ifsrmactionreport?branch=master)
</dt> <dd>

Used to generate a report in response to a quota or file screen event.

</dd> <dt>

[**IFsrmAutoApplyQuota**](/windows/previous-versions/Fsrm/nn-fsrmquota-ifsrmautoapplyquota?branch=master)
</dt> <dd>

Used to automatically add the quota to new and existing subdirectories of the directory on which the automatic quota is applied.

</dd> <dt>

[**IFsrmClassificationManager**](/windows/previous-versions/FsrmPipeline/nn-fsrmpipeline-ifsrmclassificationmanager?branch=master)
</dt> <dd>

Manages file classification. Use this interface to define properties to use in classification, add classification rules for classifying files, define classification and storage modules, and enable classification reporting.

</dd> <dt>

[**IFsrmClassificationManager2**](/windows/previous-versions/FsrmPipeline/nn-fsrmpipeline-ifsrmclassificationmanager2?branch=master)
</dt> <dd>

Manages file classification. Use this interface to define properties to use in classification, add classification rules for classifying files, define classification and storage modules, and enable classification reporting.

</dd> <dt>

[**IFsrmClassificationRule**](/windows/previous-versions/Fsrm/nn-fsrmpipeline-ifsrmclassificationrule?branch=master)
</dt> <dd>

Defines a classification rule.

</dd> <dt>

[**IFsrmClassifierModuleDefinition**](/windows/previous-versions/Fsrm/nn-fsrmpipeline-ifsrmclassifiermoduledefinition?branch=master)
</dt> <dd>

Defines a classifier module.

</dd> <dt>

[**IFsrmClassifierModuleImplementation**](/windows/previous-versions/Fsrm/nn-fsrmpipeline-ifsrmclassifiermoduleimplementation?branch=master)
</dt> <dd>

Classifier modules implement this interface. FSRM calls the module's implementation when it runs classification.

</dd> <dt>

[**IFsrmCollection**](/windows/previous-versions/Fsrm/nn-fsrm-ifsrmcollection?branch=master)
</dt> <dd>

Defines a collection of FSRM objects.

</dd> <dt>

[**IFsrmCommittableCollection**](/windows/previous-versions/Fsrm/nn-fsrm-ifsrmcommittablecollection?branch=master)
</dt> <dd>

Defines a collection of FSRM objects that can have the same type of objects added to or removed from the collection. All objects in the collection can also be committed in a single batch operation.

</dd> <dt>

[**IFsrmDerivedObjectsResult**](/windows/previous-versions/Fsrm/nn-fsrm-ifsrmderivedobjectsresult?branch=master)
</dt> <dd>

Used to access the results when the source template calls the **CommitAndUpdateDerived** method.

</dd> <dt>

[**IFsrmExportImport**](/windows/previous-versions/Fsrm/nn-fsrm-ifsrmexportimport?branch=master)
</dt> <dd>

Used to export and import FSRM objects.

</dd> <dt>

[**IFsrmFileConditionProperty**](/windows/previous-versions/FsrmReports/nn-fsrmreports-ifsrmfileconditionproperty?branch=master)
</dt> <dd>

Defines a file condition property.

</dd> <dt>

[**IFsrmFileGroup**](/windows/previous-versions/Fsrm/nn-fsrmscreen-ifsrmfilegroup?branch=master)
</dt> <dd>

Used to define a group of files based on one or more file name patterns.

</dd> <dt>

[**IFsrmFileGroupImported**](/windows/previous-versions/Fsrm/nn-fsrmscreen-ifsrmfilegroupimported?branch=master)
</dt> <dd>

Used to configure imported file group objects.

</dd> <dt>

[**IFsrmFileGroupManager**](/windows/previous-versions/FsrmScreen/nn-fsrmscreen-ifsrmfilegroupmanager?branch=master)
</dt> <dd>

Used to manage file group objects.

</dd> <dt>

[**IFsrmFileManagementJob**](/windows/previous-versions/Fsrm/nn-fsrmreports-ifsrmfilemanagementjob?branch=master)
</dt> <dd>

Defines a file management job.

</dd> <dt>

[**IFsrmFileManagementJobManager**](/windows/previous-versions/Fsrm/nn-fsrmreports-ifsrmfilemanagementjobmanager?branch=master)
</dt> <dd>

Used to manage file management jobs.

</dd> <dt>

[**IFsrmFileScreen**](/windows/previous-versions/FsrmScreen/nn-fsrmscreen-ifsrmfilescreen?branch=master)
</dt> <dd>

Used to configure a file screen that blocks groups of files from being saved to the specified directory.

</dd> <dt>

[**IFsrmFileScreenBase**](/windows/previous-versions/FsrmScreen/nn-fsrmscreen-ifsrmfilescreenbase?branch=master)
</dt> <dd>

Base class for all file screen interfaces.

</dd> <dt>

[**IFsrmFileScreenException**](/windows/previous-versions/FsrmScreen/nn-fsrmscreen-ifsrmfilescreenexception?branch=master)
</dt> <dd>

Used to configure an exception that excludes the specified files from the file screening process.

</dd> <dt>

[**IFsrmFileScreenManager**](/windows/previous-versions/FsrmScreen/nn-fsrmscreen-ifsrmfilescreenmanager?branch=master)
</dt> <dd>

Used to manage file screen objects.

</dd> <dt>

[**IFsrmFileScreenTemplate**](/windows/previous-versions/FsrmScreen/nn-fsrmscreen-ifsrmfilescreentemplate?branch=master)
</dt> <dd>

Used to configure templates from which new file screens can be derived.

</dd> <dt>

[**IFsrmFileScreenTemplateImported**](/windows/previous-versions/Fsrm/nn-fsrmscreen-ifsrmfilescreentemplateimported?branch=master)
</dt> <dd>

Used to save imported file screen templates.

</dd> <dt>

[**IFsrmFileScreenTemplateManager**](/windows/previous-versions/FsrmScreen/nn-fsrmscreen-ifsrmfilescreentemplatemanager?branch=master)
</dt> <dd>

Used to manage file screen templates.

</dd> <dt>

[**IFsrmMutableCollection**](/windows/previous-versions/Fsrm/nn-fsrm-ifsrmmutablecollection?branch=master)
</dt> <dd>

Used to manage a collection of FSRM objects that can have objects added to or removed from the collection.

</dd> <dt>

[**IFsrmObject**](/windows/previous-versions/Fsrm/nn-fsrm-ifsrmobject?branch=master)
</dt> <dd>

Base class for all FSRM objects.

</dd> <dt>

[**IFsrmPathMapper**](/windows/previous-versions/Fsrm/nn-fsrm-ifsrmpathmapper?branch=master)
</dt> <dd>

Used to retrieve the network share paths that are mapped to a local path.

</dd> <dt>

[**IFsrmPipelineModuleConnector**](/windows/previous-versions/FsrmPipeline/nn-fsrmpipeline-ifsrmpipelinemoduleconnector?branch=master)
</dt> <dd>

Creates the communication channel between FSRM and your pipeline module implementation.

</dd> <dt>

[**IFsrmPipelineModuleDefinition**](/windows/previous-versions/Fsrm/nn-fsrmpipeline-ifsrmpipelinemoduledefinition?branch=master)
</dt> <dd>

Defines a module that is used to classify files or store and retrieve properties from files.

</dd> <dt>

[**IFsrmPipelineModuleImplementation**](/windows/previous-versions/Fsrm/nn-fsrmpipeline-ifsrmpipelinemoduleimplementation?branch=master)
</dt> <dd>

Abstract interface for [**IFsrmClassifierModuleImplementation**](/windows/previous-versions/Fsrm/nn-fsrmpipeline-ifsrmclassifiermoduleimplementation?branch=master) and [**IFsrmStorageModuleImplementation**](/windows/previous-versions/Fsrm/nn-fsrmpipeline-ifsrmstoragemoduleimplementation?branch=master).

</dd> <dt>

[**IFsrmProperty**](/windows/previous-versions/Fsrm/nn-fsrmpipeline-ifsrmproperty?branch=master)
</dt> <dd>

Defines an instance of a property.

</dd> <dt>

[**IFsrmPropertyBag**](/windows/previous-versions/Fsrm/nn-fsrmpipeline-ifsrmpropertybag?branch=master)
</dt> <dd>

Contains the classification properties for a file.

</dd> <dt>

[**IFsrmPropertyBag2**](/windows/previous-versions/FsrmPipeline/nn-fsrmpipeline-ifsrmpropertybag2?branch=master)
</dt> <dd>

IFsrmPropertyBag2 Interface

</dd> <dt>

[**IFsrmPropertyCondition**](/windows/previous-versions/Fsrm/nn-fsrmreports-ifsrmpropertycondition?branch=master)
</dt> <dd>

Defines a property condition that the file management job uses to determine if the file is expired.

</dd> <dt>

[**IFsrmPropertyDefinition**](/windows/previous-versions/Fsrm/nn-fsrmpipeline-ifsrmpropertydefinition?branch=master)
</dt> <dd>

Defines a property that you want to use to classify files.

</dd> <dt>

[**IFsrmPropertyDefinition2**](/windows/previous-versions/FsrmPipeline/nn-fsrmpipeline-ifsrmpropertydefinition2?branch=master)
</dt> <dd>

Defines a property that you want to use to classify files.

</dd> <dt>

[**IFsrmPropertyDefinitionValue**](/windows/previous-versions/FsrmPipeline/nn-fsrmpipeline-ifsrmpropertydefinitionvalue?branch=master)
</dt> <dd>

Contains properties that describe a classification property definition value.

</dd> <dt>

[**IFsrmQuota**](/windows/previous-versions/Fsrm/nn-fsrmquota-ifsrmquota?branch=master)
</dt> <dd>

Used to define a quota for a specified directory and to retrieve use statistics.

</dd> <dt>

[**IFsrmQuotaBase**](/windows/previous-versions/Fsrm/nn-fsrmquota-ifsrmquotabase?branch=master)
</dt> <dd>

Base interface for all quota interfaces.

</dd> <dt>

[**IFsrmQuotaManager**](/windows/previous-versions/FsrmQuota/nn-fsrmquota-ifsrmquotamanager?branch=master)
</dt> <dd>

Used to manage quotas.

</dd> <dt>

[**IFsrmQuotaManagerEx**](/windows/previous-versions/Fsrm/nn-fsrmquota-ifsrmquotamanagerex?branch=master)
</dt> <dd>

Used to manage quotas, extended version.

</dd> <dt>

[**IFsrmQuotaObject**](/windows/previous-versions/Fsrm/nn-fsrmquota-ifsrmquotaobject?branch=master)
</dt> <dd>

Base class for the quota and automatic quota interfaces.

</dd> <dt>

[**IFsrmQuotaTemplate**](/windows/previous-versions/Fsrm/nn-fsrmquota-ifsrmquotatemplate?branch=master)
</dt> <dd>

Used to configure templates from which new quota objects can be derived.

</dd> <dt>

[**IFsrmQuotaTemplateImported**](/windows/previous-versions/Fsrm/nn-fsrmquota-ifsrmquotatemplateimported?branch=master)
</dt> <dd>

Used to modify and save imported quota templates.

</dd> <dt>

[**IFsrmQuotaTemplateManager**](/windows/previous-versions/FsrmQuota/nn-fsrmquota-ifsrmquotatemplatemanager?branch=master)
</dt> <dd>

Used to manage quota templates.

</dd> <dt>

[**IFsrmReport**](/windows/previous-versions/Fsrm/nn-fsrmreports-ifsrmreport?branch=master)
</dt> <dd>

Used to configure the description and filters for a single report.

</dd> <dt>

[**IFsrmReportJob**](/windows/previous-versions/Fsrm/nn-fsrmreports-ifsrmreportjob?branch=master)
</dt> <dd>

Used to configure a report job.

</dd> <dt>

[**IFsrmReportManager**](/windows/previous-versions/FsrmReports/nn-fsrmreports-ifsrmreportmanager?branch=master)
</dt> <dd>

Used to manage report jobs.

</dd> <dt>

[**IFsrmReportScheduler**](/windows/previous-versions/FsrmReports/nn-fsrmreports-ifsrmreportscheduler?branch=master)
</dt> <dd>

Used to manage scheduled tasks for report jobs and file management jobs.

</dd> <dt>

[**IFsrmRule**](/windows/previous-versions/Fsrm/nn-fsrmpipeline-ifsrmrule?branch=master)
</dt> <dd>

Defines a rule.

</dd> <dt>

[**IFsrmSetting**](/windows/previous-versions/Fsrm/nn-fsrm-ifsrmsetting?branch=master)
</dt> <dd>

Used to configure FSRM.

</dd> <dt>

[**IFsrmStorageModuleDefinition**](/windows/previous-versions/Fsrm/nn-fsrmpipeline-ifsrmstoragemoduledefinition?branch=master)
</dt> <dd>

Defines a local storage module that is used to read and write property values.

</dd> <dt>

[**IFsrmStorageModuleImplementation**](/windows/previous-versions/Fsrm/nn-fsrmpipeline-ifsrmstoragemoduleimplementation?branch=master)
</dt> <dd>

Storage modules implement this interface.

</dd> </dl>

 

 





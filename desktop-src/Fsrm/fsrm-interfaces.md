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
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FSRM Interfaces

The following interfaces are part of the File Server Resource Manager (FSRM) API.

## In this section

<dl> <dt>

[**DIFsrmClassificationEvents**](/previous-versions/windows/desktop/api/FsrmTlb/)
</dt> <dd>

Handles events that are received while processing a [**ClassifyFiles**](/previous-versions/windows/desktop/api/FsrmPipeline/nf-fsrmpipeline-ifsrmclassificationmanager2-classifyfiles) call.

</dd> <dt>

[**IFsrmAccessDeniedRemediationClient**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrm-ifsrmaccessdeniedremediationclient)
</dt> <dd>

Used to show the Access Denied Remediation (ADR) client user interface.

</dd> <dt>

[**IFsrmAction**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrm-ifsrmaction)
</dt> <dd>

The base class for all FSRM action interfaces.

</dd> <dt>

[**IFsrmActionCommand**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrm-ifsrmactioncommand)
</dt> <dd>

Used to run a command or script in response to a quota, file screen, or file management job event.

</dd> <dt>

[**IFsrmActionEmail**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrm-ifsrmactionemail)
</dt> <dd>

Used to send an email message in response to a quota or file screen event.

</dd> <dt>

[**IFsrmActionEmail2**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrm-ifsrmactionemail2)
</dt> <dd>

Used to limit the number of expired files listed in the email notification.

</dd> <dt>

[**IFsrmActionEventLog**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrm-ifsrmactioneventlog)
</dt> <dd>

Used to log an event to the Windows Application event log in response to a quota, file screen, or file management job event.

</dd> <dt>

[**IFsrmActionReport**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrm-ifsrmactionreport)
</dt> <dd>

Used to generate a report in response to a quota or file screen event.

</dd> <dt>

[**IFsrmAutoApplyQuota**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmquota-ifsrmautoapplyquota)
</dt> <dd>

Used to automatically add the quota to new and existing subdirectories of the directory on which the automatic quota is applied.

</dd> <dt>

[**IFsrmClassificationManager**](/previous-versions/windows/desktop/api/FsrmPipeline/nn-fsrmpipeline-ifsrmclassificationmanager)
</dt> <dd>

Manages file classification. Use this interface to define properties to use in classification, add classification rules for classifying files, define classification and storage modules, and enable classification reporting.

</dd> <dt>

[**IFsrmClassificationManager2**](/previous-versions/windows/desktop/api/FsrmPipeline/nn-fsrmpipeline-ifsrmclassificationmanager2)
</dt> <dd>

Manages file classification. Use this interface to define properties to use in classification, add classification rules for classifying files, define classification and storage modules, and enable classification reporting.

</dd> <dt>

[**IFsrmClassificationRule**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmpipeline-ifsrmclassificationrule)
</dt> <dd>

Defines a classification rule.

</dd> <dt>

[**IFsrmClassifierModuleDefinition**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmpipeline-ifsrmclassifiermoduledefinition)
</dt> <dd>

Defines a classifier module.

</dd> <dt>

[**IFsrmClassifierModuleImplementation**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmpipeline-ifsrmclassifiermoduleimplementation)
</dt> <dd>

Classifier modules implement this interface. FSRM calls the module's implementation when it runs classification.

</dd> <dt>

[**IFsrmCollection**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrm-ifsrmcollection)
</dt> <dd>

Defines a collection of FSRM objects.

</dd> <dt>

[**IFsrmCommittableCollection**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrm-ifsrmcommittablecollection)
</dt> <dd>

Defines a collection of FSRM objects that can have the same type of objects added to or removed from the collection. All objects in the collection can also be committed in a single batch operation.

</dd> <dt>

[**IFsrmDerivedObjectsResult**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrm-ifsrmderivedobjectsresult)
</dt> <dd>

Used to access the results when the source template calls the **CommitAndUpdateDerived** method.

</dd> <dt>

[**IFsrmExportImport**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrm-ifsrmexportimport)
</dt> <dd>

Used to export and import FSRM objects.

</dd> <dt>

[**IFsrmFileConditionProperty**](/previous-versions/windows/desktop/api/FsrmReports/nn-fsrmreports-ifsrmfileconditionproperty)
</dt> <dd>

Defines a file condition property.

</dd> <dt>

[**IFsrmFileGroup**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmscreen-ifsrmfilegroup)
</dt> <dd>

Used to define a group of files based on one or more file name patterns.

</dd> <dt>

[**IFsrmFileGroupImported**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmscreen-ifsrmfilegroupimported)
</dt> <dd>

Used to configure imported file group objects.

</dd> <dt>

[**IFsrmFileGroupManager**](/previous-versions/windows/desktop/api/FsrmScreen/nn-fsrmscreen-ifsrmfilegroupmanager)
</dt> <dd>

Used to manage file group objects.

</dd> <dt>

[**IFsrmFileManagementJob**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmreports-ifsrmfilemanagementjob)
</dt> <dd>

Defines a file management job.

</dd> <dt>

[**IFsrmFileManagementJobManager**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmreports-ifsrmfilemanagementjobmanager)
</dt> <dd>

Used to manage file management jobs.

</dd> <dt>

[**IFsrmFileScreen**](/previous-versions/windows/desktop/api/FsrmScreen/nn-fsrmscreen-ifsrmfilescreen)
</dt> <dd>

Used to configure a file screen that blocks groups of files from being saved to the specified directory.

</dd> <dt>

[**IFsrmFileScreenBase**](/previous-versions/windows/desktop/api/FsrmScreen/nn-fsrmscreen-ifsrmfilescreenbase)
</dt> <dd>

Base class for all file screen interfaces.

</dd> <dt>

[**IFsrmFileScreenException**](/previous-versions/windows/desktop/api/FsrmScreen/nn-fsrmscreen-ifsrmfilescreenexception)
</dt> <dd>

Used to configure an exception that excludes the specified files from the file screening process.

</dd> <dt>

[**IFsrmFileScreenManager**](/previous-versions/windows/desktop/api/FsrmScreen/nn-fsrmscreen-ifsrmfilescreenmanager)
</dt> <dd>

Used to manage file screen objects.

</dd> <dt>

[**IFsrmFileScreenTemplate**](/previous-versions/windows/desktop/api/FsrmScreen/nn-fsrmscreen-ifsrmfilescreentemplate)
</dt> <dd>

Used to configure templates from which new file screens can be derived.

</dd> <dt>

[**IFsrmFileScreenTemplateImported**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmscreen-ifsrmfilescreentemplateimported)
</dt> <dd>

Used to save imported file screen templates.

</dd> <dt>

[**IFsrmFileScreenTemplateManager**](/previous-versions/windows/desktop/api/FsrmScreen/nn-fsrmscreen-ifsrmfilescreentemplatemanager)
</dt> <dd>

Used to manage file screen templates.

</dd> <dt>

[**IFsrmMutableCollection**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrm-ifsrmmutablecollection)
</dt> <dd>

Used to manage a collection of FSRM objects that can have objects added to or removed from the collection.

</dd> <dt>

[**IFsrmObject**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrm-ifsrmobject)
</dt> <dd>

Base class for all FSRM objects.

</dd> <dt>

[**IFsrmPathMapper**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrm-ifsrmpathmapper)
</dt> <dd>

Used to retrieve the network share paths that are mapped to a local path.

</dd> <dt>

[**IFsrmPipelineModuleConnector**](/previous-versions/windows/desktop/api/FsrmPipeline/nn-fsrmpipeline-ifsrmpipelinemoduleconnector)
</dt> <dd>

Creates the communication channel between FSRM and your pipeline module implementation.

</dd> <dt>

[**IFsrmPipelineModuleDefinition**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmpipeline-ifsrmpipelinemoduledefinition)
</dt> <dd>

Defines a module that is used to classify files or store and retrieve properties from files.

</dd> <dt>

[**IFsrmPipelineModuleImplementation**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmpipeline-ifsrmpipelinemoduleimplementation)
</dt> <dd>

Abstract interface for [**IFsrmClassifierModuleImplementation**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmpipeline-ifsrmclassifiermoduleimplementation) and [**IFsrmStorageModuleImplementation**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmpipeline-ifsrmstoragemoduleimplementation).

</dd> <dt>

[**IFsrmProperty**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmpipeline-ifsrmproperty)
</dt> <dd>

Defines an instance of a property.

</dd> <dt>

[**IFsrmPropertyBag**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmpipeline-ifsrmpropertybag)
</dt> <dd>

Contains the classification properties for a file.

</dd> <dt>

[**IFsrmPropertyBag2**](/previous-versions/windows/desktop/api/FsrmPipeline/nn-fsrmpipeline-ifsrmpropertybag2)
</dt> <dd>

IFsrmPropertyBag2 Interface

</dd> <dt>

[**IFsrmPropertyCondition**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmreports-ifsrmpropertycondition)
</dt> <dd>

Defines a property condition that the file management job uses to determine if the file is expired.

</dd> <dt>

[**IFsrmPropertyDefinition**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmpipeline-ifsrmpropertydefinition)
</dt> <dd>

Defines a property that you want to use to classify files.

</dd> <dt>

[**IFsrmPropertyDefinition2**](/previous-versions/windows/desktop/api/FsrmPipeline/nn-fsrmpipeline-ifsrmpropertydefinition2)
</dt> <dd>

Defines a property that you want to use to classify files.

</dd> <dt>

[**IFsrmPropertyDefinitionValue**](/previous-versions/windows/desktop/api/FsrmPipeline/nn-fsrmpipeline-ifsrmpropertydefinitionvalue)
</dt> <dd>

Contains properties that describe a classification property definition value.

</dd> <dt>

[**IFsrmQuota**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmquota-ifsrmquota)
</dt> <dd>

Used to define a quota for a specified directory and to retrieve use statistics.

</dd> <dt>

[**IFsrmQuotaBase**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmquota-ifsrmquotabase)
</dt> <dd>

Base interface for all quota interfaces.

</dd> <dt>

[**IFsrmQuotaManager**](/previous-versions/windows/desktop/api/FsrmQuota/nn-fsrmquota-ifsrmquotamanager)
</dt> <dd>

Used to manage quotas.

</dd> <dt>

[**IFsrmQuotaManagerEx**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmquota-ifsrmquotamanagerex)
</dt> <dd>

Used to manage quotas, extended version.

</dd> <dt>

[**IFsrmQuotaObject**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmquota-ifsrmquotaobject)
</dt> <dd>

Base class for the quota and automatic quota interfaces.

</dd> <dt>

[**IFsrmQuotaTemplate**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmquota-ifsrmquotatemplate)
</dt> <dd>

Used to configure templates from which new quota objects can be derived.

</dd> <dt>

[**IFsrmQuotaTemplateImported**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmquota-ifsrmquotatemplateimported)
</dt> <dd>

Used to modify and save imported quota templates.

</dd> <dt>

[**IFsrmQuotaTemplateManager**](/previous-versions/windows/desktop/api/FsrmQuota/nn-fsrmquota-ifsrmquotatemplatemanager)
</dt> <dd>

Used to manage quota templates.

</dd> <dt>

[**IFsrmReport**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmreports-ifsrmreport)
</dt> <dd>

Used to configure the description and filters for a single report.

</dd> <dt>

[**IFsrmReportJob**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmreports-ifsrmreportjob)
</dt> <dd>

Used to configure a report job.

</dd> <dt>

[**IFsrmReportManager**](/previous-versions/windows/desktop/api/FsrmReports/nn-fsrmreports-ifsrmreportmanager)
</dt> <dd>

Used to manage report jobs.

</dd> <dt>

[**IFsrmReportScheduler**](/previous-versions/windows/desktop/api/FsrmReports/nn-fsrmreports-ifsrmreportscheduler)
</dt> <dd>

Used to manage scheduled tasks for report jobs and file management jobs.

</dd> <dt>

[**IFsrmRule**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmpipeline-ifsrmrule)
</dt> <dd>

Defines a rule.

</dd> <dt>

[**IFsrmSetting**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrm-ifsrmsetting)
</dt> <dd>

Used to configure FSRM.

</dd> <dt>

[**IFsrmStorageModuleDefinition**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmpipeline-ifsrmstoragemoduledefinition)
</dt> <dd>

Defines a local storage module that is used to read and write property values.

</dd> <dt>

[**IFsrmStorageModuleImplementation**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmpipeline-ifsrmstoragemoduleimplementation)
</dt> <dd>

Storage modules implement this interface.

</dd> </dl>

 

 





---
title: FSRM Interfaces
description: The following interfaces are part of the File Server Resource Manager (FSRM) API.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'bbd888d9-1005-4173-8e82-ced13e68c09e'
ms.prod: 'windows-server-dev'
ms.technology: 'file-server-resource-manager'
ms.tgt_platform: multiple
---

# FSRM Interfaces

The following interfaces are part of the File Server Resource Manager (FSRM) API.

## In this section

<dl> <dt>

[**DIFsrmClassificationEvents**](difsrmclassificationevents.md)
</dt> <dd>

Handles events that are received while processing a [**ClassifyFiles**](ifsrmclassificationmanager2-classifyfiles.md) call.

</dd> <dt>

[**IFsrmAccessDeniedRemediationClient**](ifsrmaccessdeniedremediationclient.md)
</dt> <dd>

Used to show the Access Denied Remediation (ADR) client user interface.

</dd> <dt>

[**IFsrmAction**](ifsrmaction.md)
</dt> <dd>

The base class for all FSRM action interfaces.

</dd> <dt>

[**IFsrmActionCommand**](ifsrmactioncommand.md)
</dt> <dd>

Used to run a command or script in response to a quota, file screen, or file management job event.

</dd> <dt>

[**IFsrmActionEmail**](ifsrmactionemail.md)
</dt> <dd>

Used to send an email message in response to a quota or file screen event.

</dd> <dt>

[**IFsrmActionEmail2**](ifsrmactionemail2.md)
</dt> <dd>

Used to limit the number of expired files listed in the email notification.

</dd> <dt>

[**IFsrmActionEventLog**](ifsrmactioneventlog.md)
</dt> <dd>

Used to log an event to the Windows Application event log in response to a quota, file screen, or file management job event.

</dd> <dt>

[**IFsrmActionReport**](ifsrmactionreport.md)
</dt> <dd>

Used to generate a report in response to a quota or file screen event.

</dd> <dt>

[**IFsrmAutoApplyQuota**](ifsrmautoapplyquota.md)
</dt> <dd>

Used to automatically add the quota to new and existing subdirectories of the directory on which the automatic quota is applied.

</dd> <dt>

[**IFsrmClassificationManager**](ifsrmclassificationmanager.md)
</dt> <dd>

Manages file classification. Use this interface to define properties to use in classification, add classification rules for classifying files, define classification and storage modules, and enable classification reporting.

</dd> <dt>

[**IFsrmClassificationManager2**](ifsrmclassificationmanager2.md)
</dt> <dd>

Manages file classification. Use this interface to define properties to use in classification, add classification rules for classifying files, define classification and storage modules, and enable classification reporting.

</dd> <dt>

[**IFsrmClassificationRule**](ifsrmclassificationrule.md)
</dt> <dd>

Defines a classification rule.

</dd> <dt>

[**IFsrmClassifierModuleDefinition**](ifsrmclassifiermoduledefinition.md)
</dt> <dd>

Defines a classifier module.

</dd> <dt>

[**IFsrmClassifierModuleImplementation**](ifsrmclassifiermoduleimplementation.md)
</dt> <dd>

Classifier modules implement this interface. FSRM calls the module's implementation when it runs classification.

</dd> <dt>

[**IFsrmCollection**](ifsrmcollection.md)
</dt> <dd>

Defines a collection of FSRM objects.

</dd> <dt>

[**IFsrmCommittableCollection**](ifsrmcommittablecollection.md)
</dt> <dd>

Defines a collection of FSRM objects that can have the same type of objects added to or removed from the collection. All objects in the collection can also be committed in a single batch operation.

</dd> <dt>

[**IFsrmDerivedObjectsResult**](ifsrmderivedobjectsresult.md)
</dt> <dd>

Used to access the results when the source template calls the **CommitAndUpdateDerived** method.

</dd> <dt>

[**IFsrmExportImport**](ifsrmexportimport.md)
</dt> <dd>

Used to export and import FSRM objects.

</dd> <dt>

[**IFsrmFileConditionProperty**](ifsrmfileconditionproperty.md)
</dt> <dd>

Defines a file condition property.

</dd> <dt>

[**IFsrmFileGroup**](ifsrmfilegroup.md)
</dt> <dd>

Used to define a group of files based on one or more file name patterns.

</dd> <dt>

[**IFsrmFileGroupImported**](ifsrmfilegroupimported.md)
</dt> <dd>

Used to configure imported file group objects.

</dd> <dt>

[**IFsrmFileGroupManager**](ifsrmfilegroupmanager.md)
</dt> <dd>

Used to manage file group objects.

</dd> <dt>

[**IFsrmFileManagementJob**](ifsrmfilemanagementjob.md)
</dt> <dd>

Defines a file management job.

</dd> <dt>

[**IFsrmFileManagementJobManager**](ifsrmfilemanagementjobmanager.md)
</dt> <dd>

Used to manage file management jobs.

</dd> <dt>

[**IFsrmFileScreen**](ifsrmfilescreen.md)
</dt> <dd>

Used to configure a file screen that blocks groups of files from being saved to the specified directory.

</dd> <dt>

[**IFsrmFileScreenBase**](ifsrmfilescreenbase.md)
</dt> <dd>

Base class for all file screen interfaces.

</dd> <dt>

[**IFsrmFileScreenException**](ifsrmfilescreenexception.md)
</dt> <dd>

Used to configure an exception that excludes the specified files from the file screening process.

</dd> <dt>

[**IFsrmFileScreenManager**](ifsrmfilescreenmanager.md)
</dt> <dd>

Used to manage file screen objects.

</dd> <dt>

[**IFsrmFileScreenTemplate**](ifsrmfilescreentemplate.md)
</dt> <dd>

Used to configure templates from which new file screens can be derived.

</dd> <dt>

[**IFsrmFileScreenTemplateImported**](ifsrmfilescreentemplateimported.md)
</dt> <dd>

Used to save imported file screen templates.

</dd> <dt>

[**IFsrmFileScreenTemplateManager**](ifsrmfilescreentemplatemanager.md)
</dt> <dd>

Used to manage file screen templates.

</dd> <dt>

[**IFsrmMutableCollection**](ifsrmmutablecollection.md)
</dt> <dd>

Used to manage a collection of FSRM objects that can have objects added to or removed from the collection.

</dd> <dt>

[**IFsrmObject**](ifsrmobject.md)
</dt> <dd>

Base class for all FSRM objects.

</dd> <dt>

[**IFsrmPathMapper**](ifsrmpathmapper.md)
</dt> <dd>

Used to retrieve the network share paths that are mapped to a local path.

</dd> <dt>

[**IFsrmPipelineModuleConnector**](ifsrmpipelinemoduleconnector.md)
</dt> <dd>

Creates the communication channel between FSRM and your pipeline module implementation.

</dd> <dt>

[**IFsrmPipelineModuleDefinition**](ifsrmpipelinemoduledefinition.md)
</dt> <dd>

Defines a module that is used to classify files or store and retrieve properties from files.

</dd> <dt>

[**IFsrmPipelineModuleImplementation**](ifsrmpipelinemoduleimplementation.md)
</dt> <dd>

Abstract interface for [**IFsrmClassifierModuleImplementation**](ifsrmclassifiermoduleimplementation.md) and [**IFsrmStorageModuleImplementation**](ifsrmstoragemoduleimplementation.md).

</dd> <dt>

[**IFsrmProperty**](ifsrmproperty.md)
</dt> <dd>

Defines an instance of a property.

</dd> <dt>

[**IFsrmPropertyBag**](ifsrmpropertybag.md)
</dt> <dd>

Contains the classification properties for a file.

</dd> <dt>

[**IFsrmPropertyBag2**](ifsrmpropertybag2.md)
</dt> <dd>

IFsrmPropertyBag2 Interface

</dd> <dt>

[**IFsrmPropertyCondition**](ifsrmpropertycondition.md)
</dt> <dd>

Defines a property condition that the file management job uses to determine if the file is expired.

</dd> <dt>

[**IFsrmPropertyDefinition**](ifsrmpropertydefinition.md)
</dt> <dd>

Defines a property that you want to use to classify files.

</dd> <dt>

[**IFsrmPropertyDefinition2**](ifsrmpropertydefinition2.md)
</dt> <dd>

Defines a property that you want to use to classify files.

</dd> <dt>

[**IFsrmPropertyDefinitionValue**](ifsrmpropertydefinitionvalue.md)
</dt> <dd>

Contains properties that describe a classification property definition value.

</dd> <dt>

[**IFsrmQuota**](ifsrmquota.md)
</dt> <dd>

Used to define a quota for a specified directory and to retrieve use statistics.

</dd> <dt>

[**IFsrmQuotaBase**](ifsrmquotabase.md)
</dt> <dd>

Base interface for all quota interfaces.

</dd> <dt>

[**IFsrmQuotaManager**](ifsrmquotamanager.md)
</dt> <dd>

Used to manage quotas.

</dd> <dt>

[**IFsrmQuotaManagerEx**](ifsrmquotamanagerex.md)
</dt> <dd>

Used to manage quotas, extended version.

</dd> <dt>

[**IFsrmQuotaObject**](ifsrmquotaobject.md)
</dt> <dd>

Base class for the quota and automatic quota interfaces.

</dd> <dt>

[**IFsrmQuotaTemplate**](ifsrmquotatemplate.md)
</dt> <dd>

Used to configure templates from which new quota objects can be derived.

</dd> <dt>

[**IFsrmQuotaTemplateImported**](ifsrmquotatemplateimported.md)
</dt> <dd>

Used to modify and save imported quota templates.

</dd> <dt>

[**IFsrmQuotaTemplateManager**](ifsrmquotatemplatemanager.md)
</dt> <dd>

Used to manage quota templates.

</dd> <dt>

[**IFsrmReport**](ifsrmreport.md)
</dt> <dd>

Used to configure the description and filters for a single report.

</dd> <dt>

[**IFsrmReportJob**](ifsrmreportjob.md)
</dt> <dd>

Used to configure a report job.

</dd> <dt>

[**IFsrmReportManager**](ifsrmreportmanager.md)
</dt> <dd>

Used to manage report jobs.

</dd> <dt>

[**IFsrmReportScheduler**](ifsrmreportscheduler.md)
</dt> <dd>

Used to manage scheduled tasks for report jobs and file management jobs.

</dd> <dt>

[**IFsrmRule**](ifsrmrule.md)
</dt> <dd>

Defines a rule.

</dd> <dt>

[**IFsrmSetting**](ifsrmsetting.md)
</dt> <dd>

Used to configure FSRM.

</dd> <dt>

[**IFsrmStorageModuleDefinition**](ifsrmstoragemoduledefinition.md)
</dt> <dd>

Defines a local storage module that is used to read and write property values.

</dd> <dt>

[**IFsrmStorageModuleImplementation**](ifsrmstoragemoduleimplementation.md)
</dt> <dd>

Storage modules implement this interface.

</dd> </dl>

 

 





---
title: What's New in FSRM in Windows Server 2008 R2
description: The following table identifies what is new for File Server Resource Manager (FSRM) in Windows Server 2008 R2.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '323ca14b-1cee-44b7-9625-2a892a8a1371'
ms.prod: 'windows-server-dev'
ms.technology: 'file-server-resource-manager'
ms.tgt_platform: multiple
keywords: ["File Server Resource Manager File Server Resource Manager , what's new in Windows ServerÂ 2008Â R2"]
---

# What's New in FSRM in Windows Server 2008 R2

The following table identifies what is new for File Server Resource Manager (FSRM) in Windows Server 2008 R2.



| Release                           | Description of features                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Windows Server 2008 R2<br/> | Adds the ability to classify files based on rules (see [**IFsrmClassificationManager**](ifsrmclassificationmanager.md)). A rule associates a property with a file if the rule is met. File management jobs (see [**IFsrmFileManagementJobManager**](ifsrmfilemanagementjobmanager.md)) can then consume the file's properties and perform actions based whether the property values set by the classifier meet the specified file management property conditions. The primary action is to expire the file (move the file to an expired files folder) and send notification that the file was expired.<br/> You can use the built-in folder classifier or you can implement your own classifier.<br/> Adds support for classification reporting.<br/> |



 

## Windows Server 2008 R2

Windows Server 2008 R2 added the following interfaces:

-   [**IFsrmActionEmail2**](ifsrmactionemail2.md)
-   [**IFsrmClassificationManager**](ifsrmclassificationmanager.md)
-   [**IFsrmClassificationRule**](ifsrmclassificationrule.md)
-   [**IFsrmClassifierModuleDefinition**](ifsrmclassifiermoduledefinition.md)
-   [**IFsrmClassifierModuleImplementation**](ifsrmclassifiermoduleimplementation.md)
-   [**IFsrmFileManagementJob**](ifsrmfilemanagementjob.md)
-   [**IFsrmFileManagementJobManager**](ifsrmfilemanagementjobmanager.md)
-   [**IFsrmPipelineModuleConnector**](ifsrmpipelinemoduleconnector.md)
-   [**IFsrmPipelineModuleDefinition**](ifsrmpipelinemoduledefinition.md)
-   [**IFsrmPipelineModuleImplementation**](ifsrmpipelinemoduleimplementation.md)
-   [**IFsrmProperty**](ifsrmproperty.md)
-   [**IFsrmPropertyBag**](ifsrmpropertybag.md)
-   [**IFsrmPropertyCondition**](ifsrmpropertycondition.md)
-   [**IFsrmPropertyDefinition**](ifsrmpropertydefinition.md)
-   [**IFsrmRule**](ifsrmrule.md)
-   [**IFsrmStorageModuleDefinition**](ifsrmstoragemoduledefinition.md)
-   [**IFsrmStorageModuleImplementation**](ifsrmstoragemoduleimplementation.md)

Windows Server 2008 R2 added the following enumerations:

-   [**FsrmClassificationLoggingFlags**](fsrmclassificationloggingflags.md)
-   [**FsrmExecutionOption**](fsrmexecutionoption.md)
-   [**FsrmFileManagementLoggingFlags**](fsrmfilemanagementloggingflags.md)
-   [**FsrmFileManagementType**](fsrmfilemanagementtype.md)
-   [**FsrmFileStreamingInterfaceType**](fsrmfilestreaminginterfacetype.md)
-   [**FsrmFileStreamingMode**](fsrmfilestreamingmode.md)
-   [**FsrmGetFilePropertyOptions**](fsrmgetfilepropertyoptions.md)
-   [**FsrmPipelineModuleType**](fsrmpipelinemoduletype.md)
-   [**FsrmPropertyBagFlags**](fsrmpropertybagflags.md)
-   [**FsrmPropertyConditionType**](fsrmpropertyconditiontype.md)
-   [**FsrmPropertyDefinitionType**](fsrmpropertydefinitiontype.md)
-   [**FsrmPropertyFlags**](fsrmpropertyflags.md)
-   [**FsrmRuleFlags**](fsrmruleflags.md)
-   [**FsrmRuleType**](fsrmruletype.md)
-   [**FsrmStorageModuleCaps**](fsrmstoragemodulecaps.md)
-   [**FsrmStorageModuleType**](fsrmstoragemoduletype.md)

Windows Server 2008 R2 changed the following enumerations:

-   [**FsrmAccountType**](fsrmaccounttype.md)
-   [**FsrmReportFilter**](fsrmreportfilter.md)
-   [**FsrmReportLimit**](fsrmreportlimit.md)
-   [**FsrmReportType**](fsrmreporttype.md)

 

 






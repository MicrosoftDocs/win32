---
title: What's New in FSRM in Windows Server 2008 R2
description: The following table identifies what is new for File Server Resource Manager (FSRM) in Windows Server 2008 R2.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 323ca14b-1cee-44b7-9625-2a892a8a1371
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- File Server Resource Manager File Server Resource Manager , what's new in Windows Server 2008 R2
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# What's New in FSRM in Windows Server 2008 R2

The following table identifies what is new for File Server Resource Manager (FSRM) in Windows Server 2008 R2.



| Release                           | Description of features                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Windows Server 2008 R2<br/> | Adds the ability to classify files based on rules (see [**IFsrmClassificationManager**](/previous-versions/windows/desktop/api/FsrmPipeline/nn-fsrmpipeline-ifsrmclassificationmanager)). A rule associates a property with a file if the rule is met. File management jobs (see [**IFsrmFileManagementJobManager**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmreports-ifsrmfilemanagementjobmanager)) can then consume the file's properties and perform actions based whether the property values set by the classifier meet the specified file management property conditions. The primary action is to expire the file (move the file to an expired files folder) and send notification that the file was expired.<br/> You can use the built-in folder classifier or you can implement your own classifier.<br/> Adds support for classification reporting.<br/> |



 

## Windows Server 2008 R2

Windows Server 2008 R2 added the following interfaces:

-   [**IFsrmActionEmail2**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrm-ifsrmactionemail2)
-   [**IFsrmClassificationManager**](/previous-versions/windows/desktop/api/FsrmPipeline/nn-fsrmpipeline-ifsrmclassificationmanager)
-   [**IFsrmClassificationRule**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmpipeline-ifsrmclassificationrule)
-   [**IFsrmClassifierModuleDefinition**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmpipeline-ifsrmclassifiermoduledefinition)
-   [**IFsrmClassifierModuleImplementation**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmpipeline-ifsrmclassifiermoduleimplementation)
-   [**IFsrmFileManagementJob**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmreports-ifsrmfilemanagementjob)
-   [**IFsrmFileManagementJobManager**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmreports-ifsrmfilemanagementjobmanager)
-   [**IFsrmPipelineModuleConnector**](/previous-versions/windows/desktop/api/FsrmPipeline/nn-fsrmpipeline-ifsrmpipelinemoduleconnector)
-   [**IFsrmPipelineModuleDefinition**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmpipeline-ifsrmpipelinemoduledefinition)
-   [**IFsrmPipelineModuleImplementation**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmpipeline-ifsrmpipelinemoduleimplementation)
-   [**IFsrmProperty**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmpipeline-ifsrmproperty)
-   [**IFsrmPropertyBag**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmpipeline-ifsrmpropertybag)
-   [**IFsrmPropertyCondition**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmreports-ifsrmpropertycondition)
-   [**IFsrmPropertyDefinition**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmpipeline-ifsrmpropertydefinition)
-   [**IFsrmRule**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmpipeline-ifsrmrule)
-   [**IFsrmStorageModuleDefinition**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmpipeline-ifsrmstoragemoduledefinition)
-   [**IFsrmStorageModuleImplementation**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrmpipeline-ifsrmstoragemoduleimplementation)

Windows Server 2008 R2 added the following enumerations:

-   [**FsrmClassificationLoggingFlags**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmclassificationloggingflags)
-   [**FsrmExecutionOption**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmexecutionoption)
-   [**FsrmFileManagementLoggingFlags**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmfilemanagementloggingflags)
-   [**FsrmFileManagementType**](/previous-versions/windows/desktop/api/Fsrm/ne-fsrmenums-_fsrmfilemanagementtype)
-   [**FsrmFileStreamingInterfaceType**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmfilestreaminginterfacetype)
-   [**FsrmFileStreamingMode**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmfilestreamingmode)
-   [**FsrmGetFilePropertyOptions**](/previous-versions/windows/desktop/api/Fsrm/ne-fsrmenums-_fsrmgetfilepropertyoptions)
-   [**FsrmPipelineModuleType**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmpipelinemoduletype)
-   [**FsrmPropertyBagFlags**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmpropertybagflags)
-   [**FsrmPropertyConditionType**](/previous-versions/windows/desktop/api/Fsrm/ne-fsrmenums-_fsrmpropertyconditiontype)
-   [**FsrmPropertyDefinitionType**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmpropertydefinitiontype)
-   [**FsrmPropertyFlags**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmpropertyflags)
-   [**FsrmRuleFlags**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmruleflags)
-   [**FsrmRuleType**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmruletype)
-   [**FsrmStorageModuleCaps**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmstoragemodulecaps)
-   [**FsrmStorageModuleType**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmstoragemoduletype)

Windows Server 2008 R2 changed the following enumerations:

-   [**FsrmAccountType**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmaccounttype)
-   [**FsrmReportFilter**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmreportfilter)
-   [**FsrmReportLimit**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmreportlimit)
-   [**FsrmReportType**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmreporttype)

 

 






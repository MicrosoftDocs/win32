---
title: Whats New in FSRM in Windows Server 2008 R2
description: The following table identifies what is new for File Server Resource Manager (FSRM) in Windows Server 2008 R2.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 323ca14b-1cee-44b7-9625-2a892a8a1371
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- File Server Resource Manager File Server Resource Manager , whats new in Windows Server 2008 R2
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# What's New in FSRM in Windows Server 2008 R2

The following table identifies what is new for File Server Resource Manager (FSRM) in Windows Server 2008 R2.



| Release                           | Description of features                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Windows Server 2008 R2<br/> | Adds the ability to classify files based on rules (see [**IFsrmClassificationManager**](/windows/previous-versions/FsrmPipeline/nn-fsrmpipeline-ifsrmclassificationmanager?branch=master)). A rule associates a property with a file if the rule is met. File management jobs (see [**IFsrmFileManagementJobManager**](/windows/previous-versions/Fsrm/nn-fsrmreports-ifsrmfilemanagementjobmanager?branch=master)) can then consume the file's properties and perform actions based whether the property values set by the classifier meet the specified file management property conditions. The primary action is to expire the file (move the file to an expired files folder) and send notification that the file was expired.<br/> You can use the built-in folder classifier or you can implement your own classifier.<br/> Adds support for classification reporting.<br/> |



 

## Windows Server 2008 R2

Windows Server 2008 R2 added the following interfaces:

-   [**IFsrmActionEmail2**](/windows/previous-versions/Fsrm/nn-fsrm-ifsrmactionemail2?branch=master)
-   [**IFsrmClassificationManager**](/windows/previous-versions/FsrmPipeline/nn-fsrmpipeline-ifsrmclassificationmanager?branch=master)
-   [**IFsrmClassificationRule**](/windows/previous-versions/Fsrm/nn-fsrmpipeline-ifsrmclassificationrule?branch=master)
-   [**IFsrmClassifierModuleDefinition**](/windows/previous-versions/Fsrm/nn-fsrmpipeline-ifsrmclassifiermoduledefinition?branch=master)
-   [**IFsrmClassifierModuleImplementation**](/windows/previous-versions/Fsrm/nn-fsrmpipeline-ifsrmclassifiermoduleimplementation?branch=master)
-   [**IFsrmFileManagementJob**](/windows/previous-versions/Fsrm/nn-fsrmreports-ifsrmfilemanagementjob?branch=master)
-   [**IFsrmFileManagementJobManager**](/windows/previous-versions/Fsrm/nn-fsrmreports-ifsrmfilemanagementjobmanager?branch=master)
-   [**IFsrmPipelineModuleConnector**](/windows/previous-versions/FsrmPipeline/nn-fsrmpipeline-ifsrmpipelinemoduleconnector?branch=master)
-   [**IFsrmPipelineModuleDefinition**](/windows/previous-versions/Fsrm/nn-fsrmpipeline-ifsrmpipelinemoduledefinition?branch=master)
-   [**IFsrmPipelineModuleImplementation**](/windows/previous-versions/Fsrm/nn-fsrmpipeline-ifsrmpipelinemoduleimplementation?branch=master)
-   [**IFsrmProperty**](/windows/previous-versions/Fsrm/nn-fsrmpipeline-ifsrmproperty?branch=master)
-   [**IFsrmPropertyBag**](/windows/previous-versions/Fsrm/nn-fsrmpipeline-ifsrmpropertybag?branch=master)
-   [**IFsrmPropertyCondition**](/windows/previous-versions/Fsrm/nn-fsrmreports-ifsrmpropertycondition?branch=master)
-   [**IFsrmPropertyDefinition**](/windows/previous-versions/Fsrm/nn-fsrmpipeline-ifsrmpropertydefinition?branch=master)
-   [**IFsrmRule**](/windows/previous-versions/Fsrm/nn-fsrmpipeline-ifsrmrule?branch=master)
-   [**IFsrmStorageModuleDefinition**](/windows/previous-versions/Fsrm/nn-fsrmpipeline-ifsrmstoragemoduledefinition?branch=master)
-   [**IFsrmStorageModuleImplementation**](/windows/previous-versions/Fsrm/nn-fsrmpipeline-ifsrmstoragemoduleimplementation?branch=master)

Windows Server 2008 R2 added the following enumerations:

-   [**FsrmClassificationLoggingFlags**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmclassificationloggingflags?branch=master)
-   [**FsrmExecutionOption**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmexecutionoption?branch=master)
-   [**FsrmFileManagementLoggingFlags**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmfilemanagementloggingflags?branch=master)
-   [**FsrmFileManagementType**](/windows/previous-versions/Fsrm/ne-fsrmenums-_fsrmfilemanagementtype?branch=master)
-   [**FsrmFileStreamingInterfaceType**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmfilestreaminginterfacetype?branch=master)
-   [**FsrmFileStreamingMode**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmfilestreamingmode?branch=master)
-   [**FsrmGetFilePropertyOptions**](/windows/previous-versions/Fsrm/ne-fsrmenums-_fsrmgetfilepropertyoptions?branch=master)
-   [**FsrmPipelineModuleType**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmpipelinemoduletype?branch=master)
-   [**FsrmPropertyBagFlags**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmpropertybagflags?branch=master)
-   [**FsrmPropertyConditionType**](/windows/previous-versions/Fsrm/ne-fsrmenums-_fsrmpropertyconditiontype?branch=master)
-   [**FsrmPropertyDefinitionType**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmpropertydefinitiontype?branch=master)
-   [**FsrmPropertyFlags**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmpropertyflags?branch=master)
-   [**FsrmRuleFlags**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmruleflags?branch=master)
-   [**FsrmRuleType**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmruletype?branch=master)
-   [**FsrmStorageModuleCaps**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmstoragemodulecaps?branch=master)
-   [**FsrmStorageModuleType**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmstoragemoduletype?branch=master)

Windows Server 2008 R2 changed the following enumerations:

-   [**FsrmAccountType**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmaccounttype?branch=master)
-   [**FsrmReportFilter**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmreportfilter?branch=master)
-   [**FsrmReportLimit**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmreportlimit?branch=master)
-   [**FsrmReportType**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmreporttype?branch=master)

 

 






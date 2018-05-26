---
title: Whats New in FSRM in Windows Server 2012
description: The following table identifies what is new or changed for File Server Resource Manager (FSRM).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9c058c3e-d6b0-4a7e-8160-b5518129dedc
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- File Server Resource Manager File Server Resource Manager , whats new in Windows Server 2012
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# What's New in FSRM in Windows Server 2012

The following table identifies what is new or changed for File Server Resource Manager (FSRM).



| Area                                                                 | Windows Server 2008 R2        | Windows Server 2012/Windows 8                                                                                                                                                              |
|----------------------------------------------------------------------|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Extensibility mechanism<br/>                                   | COM<br/>                | COM, WMI, and PowerShell<br/>                                                                                                                                                        |
| Access Denied Remediation<br/>                                 | Not supported<br/>      | Supported<br/>                                                                                                                                                                       |
| Property definition<br/>                                       | Local<br/>              | Global to the forest (including default recommended definitions)<br/>                                                                                                                |
| Who can classify files<br/>                                    | Administrator only<br/> | Administrators, Business owners and users<br/>                                                                                                                                       |
| Manual classification<br/>                                     | No UI<br/>              | Classification UI added in explorer<br/>                                                                                                                                             |
| What can be classified<br/>                                    | Files<br/>              | Folders and Files<br/>                                                                                                                                                               |
| When is the classification and file management tasks done<br/> | Schedule<br/>           | Schedule and Continuous<br/>                                                                                                                                                         |
| In box classification mechanisms<br/>                          | Content, location<br/>  | Content (improved), location, PowerShell<br/>                                                                                                                                        |
| In box file management tasks<br/>                              | Expiration, custom<br/> | Expiration, custom, RMS<br/>                                                                                                                                                         |
| Security based on classification<br/>                          | None<br/>               | Access control based on classification including central access control (Dynamic Access Control)<br/> Audit access based on classification including central audit policy<br/> |



 

## Windows Server 2012

Windows Server 2012 added the following interfaces:

-   [**IFsrmAccessDeniedRemediationClient**](/windows/previous-versions/Fsrm/nn-fsrm-ifsrmaccessdeniedremediationclient?branch=master)
-   [**IFsrmClassificationManager2**](/windows/previous-versions/FsrmPipeline/nn-fsrmpipeline-ifsrmclassificationmanager2?branch=master)
-   [**IFsrmFileConditionProperty**](/windows/previous-versions/FsrmReports/nn-fsrmreports-ifsrmfileconditionproperty?branch=master)
-   [**IFsrmPropertyBag2**](/windows/previous-versions/FsrmPipeline/nn-fsrmpipeline-ifsrmpropertybag2?branch=master)
-   [**IFsrmPropertyDefinition2**](/windows/previous-versions/FsrmPipeline/nn-fsrmpipeline-ifsrmpropertydefinition2?branch=master)
-   [**IFsrmPropertyDefinitionValue**](/windows/previous-versions/FsrmPipeline/nn-fsrmpipeline-ifsrmpropertydefinitionvalue?branch=master)

Windows Server 2012 added the following enumerations:

-   [**AdrClientDisplayFlags**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_adrclientdisplayflags?branch=master)
-   [**AdrClientErrorType**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_adrclienterrortype?branch=master)
-   [**AdrClientFlags**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_adrclientflags?branch=master)
-   [**AdrEmailFlags**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_adremailflags?branch=master)
-   [**FsrmFileSystemPropertyId**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmfilesystempropertyid?branch=master)
-   [**FsrmPropertyBagField**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmpropertybagfield?branch=master)
-   [**FsrmPropertyDefinitionAppliesTo**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmpropertydefinitionappliesto?branch=master)
-   [**FsrmPropertyDefinitionFlags**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmpropertydefinitionflags?branch=master)
-   [**FsrmPropertyValueType**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmpropertyvaluetype?branch=master)

Windows Server 2012 added the following classes:

-   [**FsrmClassificationManager**](/windows/previous-versions/FsrmTlb/?branch=master)
-   [**FsrmExportImport**](/windows/previous-versions/FsrmTlb/?branch=master)
-   [**FsrmFileGroupManager**](/windows/previous-versions/FsrmTlb/?branch=master)
-   [**FsrmFileManagementJobManager**](/windows/previous-versions/FsrmTlb/?branch=master)
-   [**FsrmFileScreenManager**](/windows/previous-versions/FsrmTlb/?branch=master)
-   [**FsrmFileScreenTemplateManager**](/windows/previous-versions/FsrmTlb/?branch=master)
-   [**FsrmPathMapper**](/windows/previous-versions/FsrmTlb/?branch=master)
-   [**FsrmPipelineModuleConnector**](/windows/previous-versions/FsrmTlb/?branch=master)
-   [**FsrmQuotaManager**](/windows/previous-versions/FsrmTlb/?branch=master)
-   [**FsrmQuotaTemplateManager**](/windows/previous-versions/FsrmTlb/?branch=master)
-   [**FsrmReportManager**](/windows/previous-versions/FsrmTlb/?branch=master)
-   [**FsrmReportScheduler**](/windows/previous-versions/FsrmTlb/?branch=master)
-   [**FsrmSetting**](/windows/previous-versions/FsrmTlb/?branch=master)

Windows Server 2012 added the following WMI classes:

-   [**MSFT\_FSRMAction**](msft-fsrmaction.md)
-   [**MSFT\_FSRMAdr**](msft-fsrmadr.md)
-   [**MSFT\_FSRMADRSettings**](msft-fsrmadrsettings.md)
-   [**MSFT\_FSRMAutoQuota**](msft-fsrmautoquota.md)
-   [**MSFT\_FSRMClassification**](msft-fsrmclassification.md)
-   [**MSFT\_FSRMClassificationPropertyDefinition**](msft-fsrmclassificationpropertydefinition.md)
-   [**MSFT\_FSRMClassificationPropertyValue**](msft-fsrmclassificationpropertyvalue.md)
-   [**MSFT\_FSRMClassificationRule**](msft-fsrmclassificationrule.md)
-   [**MSFT\_FSRMEffectiveNamespace**](msft-fsrmeffectivenamespace.md)
-   [**MSFT\_FSRMFileGroup**](msft-fsrmfilegroup.md)
-   [**MSFT\_FSRMFileManagementJob**](msft-fsrmfilemanagementjob.md)
-   [**MSFT\_FSRMFileScreen**](msft-fsrmfilescreen.md)
-   [**MSFT\_FSRMFileScreenException**](msft-fsrmfilescreenexception.md)
-   [**MSFT\_FSRMFileScreenTemplate**](msft-fsrmfilescreentemplate.md)
-   [**MSFT\_FSRMFMJAction**](msft-fsrmfmjaction.md)
-   [**MSFT\_FSRMFMJCondition**](msft-fsrmfmjcondition.md)
-   [**MSFT\_FSRMFMJNotification**](msft-fsrmfmjnotification.md)
-   [**MSFT\_FSRMFMJNotificationAction**](msft-fsrmfmjnotificationaction.md)
-   [**MSFT\_FSRMMacro**](msft-fsrmmacro.md)
-   [**MSFT\_FSRMMgmtProperty**](msft-fsrmmgmtproperty.md)
-   [**MSFT\_FSRMMgmtPropertyValue**](msft-fsrmmgmtpropertyvalue.md)
-   [**MSFT\_FSRMQuota**](msft-fsrmquota.md)
-   [**MSFT\_FSRMQuotaTemplate**](msft-fsrmquotatemplate.md)
-   [**MSFT\_FSRMQuotaThreshold**](msft-fsrmquotathreshold.md)
-   [**MSFT\_FSRMScheduledTask**](msft-fsrmscheduledtask.md)
-   [**MSFT\_FSRMSettings**](msft-fsrmsettings.md)
-   [**MSFT\_FSRMStorageReport**](msft-fsrmstoragereport.md)

Windows Server 2012 changed the following enumerations:

-   [**FsrmAccountType**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmaccounttype?branch=master)
-   [**FsrmEnumOptions**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmenumoptions?branch=master)
-   [**FsrmFileManagementType**](/windows/previous-versions/Fsrm/ne-fsrmenums-_fsrmfilemanagementtype?branch=master)
-   [**FsrmGetFilePropertyOptions**](/windows/previous-versions/Fsrm/ne-fsrmenums-_fsrmgetfilepropertyoptions?branch=master)
-   [**FsrmPropertyConditionType**](/windows/previous-versions/Fsrm/ne-fsrmenums-_fsrmpropertyconditiontype?branch=master)
-   [**FsrmPropertyDefinitionType**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmpropertydefinitiontype?branch=master)
-   [**FsrmPropertyFlags**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmpropertyflags?branch=master)
-   [**FsrmReportLimit**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmreportlimit?branch=master)
-   [**FsrmReportType**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmreporttype?branch=master)
-   [**FsrmStorageModuleCaps**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmstoragemodulecaps?branch=master)
-   [**FsrmStorageModuleType**](/windows/previous-versions/FsrmEnums/ne-fsrmenums-_fsrmstoragemoduletype?branch=master)

Windows Server 2012 removed support for the following interface:

-   [**IFsrmReportScheduler**](/windows/previous-versions/FsrmReports/nn-fsrmreports-ifsrmreportscheduler?branch=master)

 

 






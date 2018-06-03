---
title: What's New in FSRM in Windows Server 2012
description: The following table identifies what is new or changed for File Server Resource Manager (FSRM).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9c058c3e-d6b0-4a7e-8160-b5518129dedc
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- File Server Resource Manager File Server Resource Manager , what's new in Windows Server 2012
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

-   [**IFsrmAccessDeniedRemediationClient**](/previous-versions/windows/desktop/api/Fsrm/nn-fsrm-ifsrmaccessdeniedremediationclient)
-   [**IFsrmClassificationManager2**](/previous-versions/windows/desktop/api/FsrmPipeline/nn-fsrmpipeline-ifsrmclassificationmanager2)
-   [**IFsrmFileConditionProperty**](/previous-versions/windows/desktop/api/FsrmReports/nn-fsrmreports-ifsrmfileconditionproperty)
-   [**IFsrmPropertyBag2**](/previous-versions/windows/desktop/api/FsrmPipeline/nn-fsrmpipeline-ifsrmpropertybag2)
-   [**IFsrmPropertyDefinition2**](/previous-versions/windows/desktop/api/FsrmPipeline/nn-fsrmpipeline-ifsrmpropertydefinition2)
-   [**IFsrmPropertyDefinitionValue**](/previous-versions/windows/desktop/api/FsrmPipeline/nn-fsrmpipeline-ifsrmpropertydefinitionvalue)

Windows Server 2012 added the following enumerations:

-   [**AdrClientDisplayFlags**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_adrclientdisplayflags)
-   [**AdrClientErrorType**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_adrclienterrortype)
-   [**AdrClientFlags**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_adrclientflags)
-   [**AdrEmailFlags**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_adremailflags)
-   [**FsrmFileSystemPropertyId**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmfilesystempropertyid)
-   [**FsrmPropertyBagField**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmpropertybagfield)
-   [**FsrmPropertyDefinitionAppliesTo**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmpropertydefinitionappliesto)
-   [**FsrmPropertyDefinitionFlags**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmpropertydefinitionflags)
-   [**FsrmPropertyValueType**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmpropertyvaluetype)

Windows Server 2012 added the following classes:

-   [**FsrmClassificationManager**](/previous-versions/windows/desktop/api/FsrmTlb/)
-   [**FsrmExportImport**](/previous-versions/windows/desktop/api/FsrmTlb/)
-   [**FsrmFileGroupManager**](/previous-versions/windows/desktop/api/FsrmTlb/)
-   [**FsrmFileManagementJobManager**](/previous-versions/windows/desktop/api/FsrmTlb/)
-   [**FsrmFileScreenManager**](/previous-versions/windows/desktop/api/FsrmTlb/)
-   [**FsrmFileScreenTemplateManager**](/previous-versions/windows/desktop/api/FsrmTlb/)
-   [**FsrmPathMapper**](/previous-versions/windows/desktop/api/FsrmTlb/)
-   [**FsrmPipelineModuleConnector**](/previous-versions/windows/desktop/api/FsrmTlb/)
-   [**FsrmQuotaManager**](/previous-versions/windows/desktop/api/FsrmTlb/)
-   [**FsrmQuotaTemplateManager**](/previous-versions/windows/desktop/api/FsrmTlb/)
-   [**FsrmReportManager**](/previous-versions/windows/desktop/api/FsrmTlb/)
-   [**FsrmReportScheduler**](/previous-versions/windows/desktop/api/FsrmTlb/)
-   [**FsrmSetting**](/previous-versions/windows/desktop/api/FsrmTlb/)

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

-   [**FsrmAccountType**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmaccounttype)
-   [**FsrmEnumOptions**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmenumoptions)
-   [**FsrmFileManagementType**](/previous-versions/windows/desktop/api/Fsrm/ne-fsrmenums-_fsrmfilemanagementtype)
-   [**FsrmGetFilePropertyOptions**](/previous-versions/windows/desktop/api/Fsrm/ne-fsrmenums-_fsrmgetfilepropertyoptions)
-   [**FsrmPropertyConditionType**](/previous-versions/windows/desktop/api/Fsrm/ne-fsrmenums-_fsrmpropertyconditiontype)
-   [**FsrmPropertyDefinitionType**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmpropertydefinitiontype)
-   [**FsrmPropertyFlags**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmpropertyflags)
-   [**FsrmReportLimit**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmreportlimit)
-   [**FsrmReportType**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmreporttype)
-   [**FsrmStorageModuleCaps**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmstoragemodulecaps)
-   [**FsrmStorageModuleType**](/previous-versions/windows/desktop/api/FsrmEnums/ne-fsrmenums-_fsrmstoragemoduletype)

Windows Server 2012 removed support for the following interface:

-   [**IFsrmReportScheduler**](/previous-versions/windows/desktop/api/FsrmReports/nn-fsrmreports-ifsrmreportscheduler)

 

 






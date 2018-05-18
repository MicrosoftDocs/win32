---
title: What's New in FSRM in Windows Server 2012
description: The following table identifies what is new or changed for File Server Resource Manager (FSRM).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '9c058c3e-d6b0-4a7e-8160-b5518129dedc'
ms.prod: 'windows-server-dev'
ms.technology: 'file-server-resource-manager'
ms.tgt_platform: multiple
keywords: ["File Server Resource Manager File Server Resource Manager , what's new in Windows ServerÂ 2012"]
---

# What's New in FSRM in Windows Server 2012

The following table identifies what is new or changed for File Server Resource Manager (FSRM).



| Area                                                                 | Windows Server 2008 R2        | Windows Server 2012/Windows 8                                                                                                                                                              |
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

Windows Server 2012 added the following interfaces:

-   [**IFsrmAccessDeniedRemediationClient**](ifsrmaccessdeniedremediationclient.md)
-   [**IFsrmClassificationManager2**](ifsrmclassificationmanager2.md)
-   [**IFsrmFileConditionProperty**](ifsrmfileconditionproperty.md)
-   [**IFsrmPropertyBag2**](ifsrmpropertybag2.md)
-   [**IFsrmPropertyDefinition2**](ifsrmpropertydefinition2.md)
-   [**IFsrmPropertyDefinitionValue**](ifsrmpropertydefinitionvalue.md)

Windows Server 2012 added the following enumerations:

-   [**AdrClientDisplayFlags**](adrclientdisplayflags.md)
-   [**AdrClientErrorType**](adrclienterrortype.md)
-   [**AdrClientFlags**](adrclientflags.md)
-   [**AdrEmailFlags**](adremailflags.md)
-   [**FsrmFileSystemPropertyId**](fsrmfilesystempropertyid.md)
-   [**FsrmPropertyBagField**](fsrmpropertybagfield.md)
-   [**FsrmPropertyDefinitionAppliesTo**](fsrmpropertydefinitionappliesto.md)
-   [**FsrmPropertyDefinitionFlags**](fsrmpropertydefinitionflags.md)
-   [**FsrmPropertyValueType**](fsrmpropertyvaluetype.md)

Windows Server 2012 added the following classes:

-   [**FsrmClassificationManager**](fsrmclassificationmanager.md)
-   [**FsrmExportImport**](fsrmexportimport.md)
-   [**FsrmFileGroupManager**](fsrmfilegroupmanager.md)
-   [**FsrmFileManagementJobManager**](fsrmfilemanagementjobmanager.md)
-   [**FsrmFileScreenManager**](fsrmfilescreenmanager.md)
-   [**FsrmFileScreenTemplateManager**](fsrmfilescreentemplatemanager.md)
-   [**FsrmPathMapper**](fsrmpathmapper.md)
-   [**FsrmPipelineModuleConnector**](fsrmpipelinemoduleconnector.md)
-   [**FsrmQuotaManager**](fsrmquotamanager.md)
-   [**FsrmQuotaTemplateManager**](fsrmquotatemplatemanager.md)
-   [**FsrmReportManager**](fsrmreportmanager.md)
-   [**FsrmReportScheduler**](fsrmreportscheduler.md)
-   [**FsrmSetting**](fsrmsetting.md)

Windows Server 2012 added the following WMI classes:

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

Windows Server 2012 changed the following enumerations:

-   [**FsrmAccountType**](fsrmaccounttype.md)
-   [**FsrmEnumOptions**](fsrmenumoptions.md)
-   [**FsrmFileManagementType**](fsrmfilemanagementtype.md)
-   [**FsrmGetFilePropertyOptions**](fsrmgetfilepropertyoptions.md)
-   [**FsrmPropertyConditionType**](fsrmpropertyconditiontype.md)
-   [**FsrmPropertyDefinitionType**](fsrmpropertydefinitiontype.md)
-   [**FsrmPropertyFlags**](fsrmpropertyflags.md)
-   [**FsrmReportLimit**](fsrmreportlimit.md)
-   [**FsrmReportType**](fsrmreporttype.md)
-   [**FsrmStorageModuleCaps**](fsrmstoragemodulecaps.md)
-   [**FsrmStorageModuleType**](fsrmstoragemoduletype.md)

Windows Server 2012 removed support for the following interface:

-   [**IFsrmReportScheduler**](ifsrmreportscheduler.md)

 

 






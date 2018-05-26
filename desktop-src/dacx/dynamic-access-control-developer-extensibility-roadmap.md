---
title: Dynamic Access Control developer extensibility
description: The Dynamic Access Control (DAC) scenario, as delivered in Windows Server 2012, has a variety of developer extensibility points that add customization potential for your applications development.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: EDE95808-D6E0-4F03-9BBC-4CD76F159481
ms.prod: windows-server-dev
ms.technology: dynamic-access-control
ms.tgt_platform: multiple
keywords:
- Dynamic Access Control developer extensibility DACx
- Dynamic Access Control developer extensibility DACx , home page
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Dynamic Access Control developer extensibility

[The Dynamic Access Control (DAC) scenario](https://technet.microsoft.com/library/hh831717.aspx), as delivered in Windows Server 2012, has a variety of developer extensibility points that add customization potential for your applications development. Many of these extensibility points are outlined in this topic, some with additional information and others to be further developed.

-   [Introduction](#introduction)
-   [Managing Central Access Policies](#managing-central-access-policies)
-   [User claim provisioning to Active Directory](#user-claim-provisioning-to-active-directory)
-   [Creating DAC compatible file classification properties](#creating-dac-compatible-file-classification-properties)
-   [Classification-aware applications](#classification-aware-applications)
-   [Audit event analysis for compliance reporting and forensic analysis](#audit-event-analysis-for-compliance-reporting-and-forensic-analysis)
-   [Integrating DAC access and audit policies into applications](#integrating-dac-access-and-audit-policies-into-applications)
-   [Constructing a plug-in for the File Classification Infrastructure](#constructing-a-plug-in-for-the-file-classification-infrastructure)
-   [Data management for file servers](#data-management-for-file-servers)
-   [DAC How-to topics](#dac-how-to-topics)
-   [Additional resources](#additional-resources)
-   [Related topics](#related-topics)

## Introduction

The DAC developer extensibility areas are organized by types of extensibility. These are outlined in the set of tables that follow. These extensibility points, or programmatic customization points, are intended for experienced programmers.

## Managing Central Access Policies

Creating Central Access Policies (CAP) for files allow organizations to centrally deploy and manage authorization policies that include conditional expressions using security groups, user claims, device claims, and resource properties. These polices are based on compliance and business regulatory requirements. These policies are created and hosted in Active Directory (AD), therefore making it easier to manage and deploy.

Some aspects of CAP management can be further configured programmatically through AD and are outlined as follows.

For more information on CAPs, see [Dynamic Access Control Scenario: Central Access Policy](https://technet.microsoft.com/library/hh831425.aspx) on TechNet or [Centralized Authorization Policy](https://msdn.microsoft.com/library/windows/desktop/jj662749) on MSDN.



| Scenario                                                                                                                                                                                                                             | Guidance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A partner that develops policy management and modeling solutions integrates with the DAC access and audit policy so that the policies can be configured through the policy management solution that the partner provides.<br/> | [How to use central access policies for DAC](how-to-use-central-access-policies-for-dynamic-access-control.md)<br/> Active directory configuration for DAC objects: [How to set up a claim type](how-to-set-up-a-claim-type.md), [Dynamic Access Control objects in Active Directory](dynamic-access-control-containers-in-active-directory.md)<br/> [How to read DAC objects using LDAP](how-to-enumerate-active-directory-definitions-for-user-and-device-claims-and-resource-properties.md)<br/> |



 

## User claim provisioning to Active Directory

In Windows Server 2012, the AD Domain Server maintains a *claims dictionary* in each forest and all claim types in use within the forest are defined at the AD forest level.

Custom user claims provisioning can be effected programmatically.



| Scenario                                                                                                                                                                                                                                                         | Guidance                                                                                                                                                                                                                                                                                                                                                                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A partner develops a product that allows organizations to manage user claims in AD so that organizations can source the claims from multiple repositories as well as delegate the assignment of specific claims and specific values for these claims.<br/> | [How to use central access policies](how-to-use-central-access-policies-for-dynamic-access-control.md)<br/> [How to set up a claim type](how-to-set-up-a-claim-type.md)<br/> [Dynamic Access Control containers in Active Directory](dynamic-access-control-containers-in-active-directory.md)<br/> [How to set up a resource property](how-to-set-up-a-resource-property.md)<br/> |



 

## Creating DAC compatible file classification properties

By creating file classification properties on files in a manner compatible with DAC, Central Access Policies are correctly applied to files that are stored or move to a Windows Server 2012 share.



| Scenario                                                                                                                                                                                                                | Guidance                                                                                                                                                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Providing automatic and manual classification of files on Windows and non-Windows based machines. When those files are moved to a DAC enabled workload, the corresponding Central Access Policy is enforced.<br/> | [Accessing Classification Properties](https://msdn.microsoft.com/library/jj635208)<br/> [\[MS-FCIADS\]: File Classification Infrastructure Alternate Data Stream (ADS) File Format](Http://Go.Microsoft.Com/FWLink/p/?LinkID=265469)<br/> |



 

## Classification-aware applications

Classification-aware applications are applications that create or consume file classification properties on files. These applications range from a Line of Business type application that classify files they create based on the value of the data, for example **Impact=High**, to Information Worker applications such as a data entry application that allows the user to determine the classification of the information they are creating.



| Scenario                                                                                                                                                 | Guidance                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Users saving a picture in a paint application are asked to determine the classification of the file before they are allowed to save the file.<br/> | Applications can read the classification information on files they are manipulating and display it so that users can view how the file is classified. They can also allow users to change the classification properties, updating them using the classification APIs. For more information see [Accessing Classification Properties](https://msdn.microsoft.com/library/jj635208)<br/>                                                                                              |
| Users are manually classifying many files on client and server.<br/>                                                                               | Bulk file classification: The classification manager interfaces (see the [File Server Resource Manager (FSRM) Interfaces](https://msdn.microsoft.com/library/bb625488) topic) provides clear, enumerate, get, and set capability for classification properties on files. It also provides a Classifying Files API to efficiently classify files as a bulk operation through call-backs within FCI for each individual file. For more information, see [Classifying Files](https://msdn.microsoft.com/library/jj218761).<br/> |
| A Data Leakage Protection (DLP) solution sees the classification and acts on it.<br/>                                                              | A data leakage protection solution can read classification information stored on the file then apply a policy such as alerting users that are trying to store sensitive information on a USB device or a user is sending sensitive documents through email. For more information see [Accessing Classification Properties](https://msdn.microsoft.com/library/jj635208).<br/>                                                                                                       |
| An application moving data from one repository to another can classify the data based on its knowledge of the data.<br/>                           | When a line of business application moves data from a repository, such as a database, and stores it on a file server (e.g.: as an Excel spreadsheet) it can also classify the file according to the business needs (e.g.: PII=Yes, Impact=High). For more information see [Accessing Classification Properties](https://msdn.microsoft.com/library/jj635208).<br/>                                                                                                                  |



 

## Audit event analysis for compliance reporting and forensic analysis

Security auditing is not new to Windows, it has been around since Windows NT. In Windows Server 2012 and Windows 8 we have made significant improvements to auditing by:

-   Reducing audit volume by introducing expression-based audit policies that help target relevant data
-   Improving consumption of audit events by adding more metadata to the events which in turn can be consumed by audit analysis tools to enable users get to the most relevant events quickly
-   Making it possible to test changes to CAPs directly in the production environment through *Staging*

Developers of audit event reporting and analysis tools can leverage these improvements to enhance their products with better audit reports that help users answer questions such as "Who access my finance information in the last three months?" or "How will this proposed change in access policy impact my users?".



| Scenario                                                                                                                                                                                                                       | Guidance                                                                                                                        |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| The developer of an audit event analysis and reporting solution wants to enhance his product with new reports that help users understand file access in their Enterprise and helps them deploy changes to the CAPs.<br/> | [How to enrich audit reporting](enrich-audit-reporting.md) covers these events: file access, user logon and staging<br/> |



 

## Integrating DAC access and audit policies into applications

Integrating DAC access and audit policies into applications enables those applications to use the new authorization capabilities in Windows Server 2012 so that they can implement scenarios such as centrally managed access control that spans across the application and other data repositories or access control based on conditional expressions and user/device claims.



| Scenario                                                                                                        | Guidance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Integrating claims, resource properties and conditional expressions into custom resource managers.<br/>   | Understanding Windows Access Control - see [How AccessCheck Works](https://msdn.microsoft.com/library/windows/desktop/aa446683)<br/> Performing runtime authorization in resource manager applications [Using AuthZ API](https://msdn.microsoft.com/library/windows/desktop/ff394773) section - see [Effective access rights for files sample](https://Code.MSDN.Microsoft.Com/windowsdesktop/Effective-access-rights-dd5b13a8)<br/> How to integrate the ACL-UI into an application - see [Authentication and authorization DACL editor sample](https://Code.MSDN.Microsoft.Com/windowsdesktop/Authentication-and-b9166266)<br/> Programmatically manage access control policy: [AddConditionalAce](https://msdn.microsoft.com/library/windows/desktop/dd401511.aspx), [AddResourceAttributeAce](https://msdn.microsoft.com/library/windows/desktop/hh448447.aspx)<br/> [How to author SDDL based on SDDL reference content](https://msdn.microsoft.com/library/windows/desktop/aa379570) - see [Authentication and authorization DACL editor sample](https://Code.MSDN.Microsoft.Com/windowsdesktop/Authentication-and-b9166266) and [\[MS-DTYP\]: Security Descriptor Description Language](https://msdn.microsoft.com/library/cc230368(PROT.10).aspx)<br/> |
| Use Central Access Policies (CAP) on resource manager applications such as non-Windows file servers.<br/> | Reading CAP definitions from AD - see [How to enumerate Active Directory definitions for user and device claims and resource properties](how-to-enumerate-active-directory-definitions-for-user-and-device-claims-and-resource-properties.md) and [**AddScopedPolicyIDAce**](https://msdn.microsoft.com/library/windows/desktop/hh448448)<br/> Setting resource attributes and central access control - see [Setting central access control and resource attributes sample](https://Code.MSDN.Microsoft.Com/windowsdesktop/Resource-attributes-sample-da837a61)<br/> [Deploy a Central Access Policy using PowerShell](https://technet.microsoft.com/library/hh846167.aspx) - see [Central access policy ID lookup sample](https://Code.MSDN.Microsoft.Com/windowsdesktop/Central-access-policy-ID-3836c4a5)<br/> [Deploy a Central Access Policy (Demonstration Steps)](https://technet.microsoft.com/library/hh846167.aspx)<br/>                                                                                                                                                                                                                                                                                                                       |



 

## Constructing a plug-in for the File Classification Infrastructure

Constructing a plug-in for the File Classification Infrastructure (FCI) is enables Data Leakage Prevention (DLP) solutions to plug into the new DAC capabilities so that customers can control access, audit and encryption based on the DLP solution's analysis engine.



| Scenario                                                                                                                                            | Guidance                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| Advanced classification used to apply access, audit, encryption, and data life-cycle management policies to information on file servers.<br/> | [Developing FCI Pipeline Modules](https://msdn.microsoft.com/library/ee126210)<br/> |



 

## Data management for file servers

Data management for file servers provides solutions to manage the vast amount of fast growing unstructured data on file servers. Using the FCI capabilities, developers can enhance their product to enable data management based on the business value (classification properties) of the files so that organizations can define data management policies across their unstructured repositories.



| Scenario                                                                                                                | Guidance                                                                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A partner product implements data life-cycle management on file servers based on classification of the data.<br/> | For examples see [Accessing Classification Properties](https://msdn.microsoft.com/library/jj635208) and [Classifying Files](https://msdn.microsoft.com/library/jj218761).<br/> |



 

## DAC How-to topics

[How to configure a file management task](how-to-configure-a-file-management-task.md)

[How to create a custom storage plug-in](how-to-create-a-custom-storage-plug-in.md)

[How to enrich audit reporting](enrich-audit-reporting.md)

[How to read Dynamic Access Control objects using LDAP](how-to-enumerate-active-directory-definitions-for-user-and-device-claims-and-resource-properties.md)

[How to use custom file classification](how-to-use-custom-file-classification.md)

[How to use central access policies for dynamic access control](how-to-use-central-access-policies-for-dynamic-access-control.md)

[Dynamic Access Control containers in Active Directory](dynamic-access-control-containers-in-active-directory.md)

[How to set up a claim type](how-to-set-up-a-claim-type.md)

[How to set up a resource property](how-to-set-up-a-resource-property.md)

[How to setup a central access rule](how-to-setup-a-central-access-rule.md)

[How to setup a central access policy](how-to-setup-a-central-access-policy.md)

## Additional resources

[Deploy a Central Access Policy (Demonstration Steps) \[TechNet\]](https://technet.microsoft.com/library/hh846167.aspx)

[Dynamic Access Control: Scenario Overview \[TechNet\]](https://technet.microsoft.com/library/hh831717.aspx)

[Extensible File Classification Infrastructure](https://msdn.microsoft.com/windowsserver2008r2trainingcourse_fileclassifictioninfrastructure_unit)

[Working with File Classification](https://technet.microsoft.com/library/dd758765.aspx)

[Automatically uploading files from File Server to SharePoint using the File Classification Infrastructure (FCI)](http://blogs.technet.com/b/filecab/archive/2009/12/14/automatically-upload-files-from-file-server-to-sharepoint-using-the-file-classification-infrastructure-fci.aspx)

## Related topics

[Create a Custom File Management Task](https://technet.microsoft.com/library/dd759180.aspx)


[Developing FCI Pipeline Modules](https://msdn.microsoft.com/library/ee126210)


[Using FSRM](https://msdn.microsoft.com/library/bb870628)


[FSRM Interfaces](https://msdn.microsoft.com/library/bb625488)


[What's New in FSRM in Windows Server 2012](https://msdn.microsoft.com/library/dd392499)


[Authorization](https://msdn.microsoft.com/library/windows/desktop/aa375769)


[Central Access Policy](https://technet.microsoft.com/library/hh831425.aspx)


[How AccessCheck Works](https://msdn.microsoft.com/library/windows/desktop/aa446683)


 

 






---
title: Group Policy Management Console Scripting Samples
description: The following information describes the Group Policy Management Console (GPMC) scripting samples.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5996edda-f42c-4345-9912-0fcb1c784d11
ms.prod: windows-server-dev
ms.technology: group-policy
ms.tgt_platform: multiple
keywords:
- scripting examples
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Group Policy Management Console Scripting Samples

The following information describes the Group Policy Management Console (GPMC) scripting samples. These samples were originally found in the "%programfiles%\\Gpmc\\Scripts" directory after you installed the GPMC, and now can be found on the [TechNet Code Gallery](https://gallery.technet.microsoft.com/Group-Policy-Management-17a5f840). You can execute the scripts at the command prompt. The scripts send output to the Command Prompt window. Run the scripts using the CScript.exe application.

The following script samples address administrative tasks:

-   [Backing up an Individual GPO](#backing-up-an-individual-gpo)
-   [Backing up the GPOs in a Domain](#backing-up-the-gpos-in-a-domain)
-   [Creating a Copy of a GPO](#creating-a-copy-of-a-gpo)
-   [Creating a New GPO](#creating-a-new-gpo)
-   [Creating a Policy Environment Using an XML File](#creating-a-policy-environment-using-an-xml-file)
-   [Creating an XML File that Represents a Policy Environment](#creating-an-xml-file-that-represents-a-policy-environment)
-   [Create Migration Table](#deleting-a-gpo)
-   [Deleting a GPO](#deleting-a-gpo)
-   [Grant Permissions for all GPOs in a Domain](#grant-permissions-for-all-gpos-in-a-domain)
-   [Importing a GPO](#importing-a-gpo)
-   [Importing Multiple GPOs into a Domain](#importing-multiple-gpos-into-a-domain)
-   [Restoring a GPO](#restoring-a-gpo)
-   [Restoring All GPOs in a Domain](#restoring-all-gpos-in-a-domain)
-   [Setting GPO Permissions](#setting-gpo-permissions)
-   [Setting Permissions for all GPOs Linked to a Scope of Management](#setting-permissions-for-all-gpos-linked-to-a-scope-of-management)
-   [Setting Permissions to Create GPOs](#setting-permissions-to-create-gpos)
-   [Setting Policy-related Permissions on a SOM](#setting-policy-related-permissions-on-a-som)

There are also script samples that perform the following queries:

-   [Listing All GPOs in a Domain](#listing-all-gpos-in-a-domain)
-   [Listing Disabled GPOs](#listing-disabled-gpos)
-   [Listing GPO Information](#listing-gpo-information)
-   [Listing GPOs at a Backup Location](#listing-gpos-at-a-backup-location)
-   [Listing GPOs by Policy Extension](#listing-gpos-by-policy-extension)
-   [Listing GPOs by Security Group](#listing-gpos-by-security-group)
-   [Listing GPOs Orphaned in SYSVOL](#listing-gpos-orphaned-in-sysvol)
-   [Listing GPOs With Duplicate Names](#listing-gpos-with-duplicate-names)
-   [Listing GPOs Without Security Filtering](#listing-gpos-without-security-filtering)
-   [Listing SOM Information](#listing-som-information)
-   [Listing SOMs With Links to GPOs in External Domains](#listing-soms-with-links-to-gpos-in-external-domains)
-   [Listing Unlinked GPOs in a Domain](#listing-unlinked-gpos-in-a-domain)
-   [Printing the SOM Policy Tree](#printing-the-som-policy-tree)
-   [Generate Reports for all GPOs](#printing-the-som-policy-tree)
-   [Generate Reports for a GPO](#printing-the-som-policy-tree)

## Backing Up an Individual GPO

The BackupGPO.wsf sample backs up a Group Policy object (GPO) to a specified backup directory. You can specify the GPO either by its name or by its GPO ID. The backup directory and the GPO must already exist. You can use the *Comment* parameter to specify an optional comment for the backup.

**Usage:  BackupGPO.wsf &lt;GPO Name&gt; &lt;BackupLocation&gt; \[/Comment:&lt;Comment&gt;\] \[/Domain:&lt;DNSDomainName&gt;\]**

**Example:  BackupGPO.wsf TestPolicyGPO \\\\server\\share\\GPOBackups /Comment: "Weekly backup" /Domain:example.microsoft.com**

## Backing Up the GPOs in a Domain

The BackupAllGPOs.wsf sample backs up all the GPOs in a domain to the specified backup directory. The backup directory must exist. You can use the *Comment* parameter to specify an optional comment for the backup.

**Usage:  BackupAllGPOs.wsf &lt;BackupLocation&gt; \[/Comment:&lt;Comment&gt;\] \[/Domain:&lt;DNSDomain&gt;\]**

**Example:  BackupAllGPOs.wsf \\\\server\\share\\GPOBackups /Comment:"Weekly backup" /Domain:example.microsoft.com**

## Creating a Copy of a GPO

The CopyGPO.wsf sample creates a new GPO and copies the settings from a source GPO into the new destination GPO. You specify the source GPO either by its name or its GPO ID. You specify the new destination GPO by name. Use the **MigrationTable** switch to map security principals and paths across domains. Use the **CopyACL** switch to copy the access control list (ACL) on the source GPO to the destination GPO. To create a migration table, see the [Create Migration Table](#create-migration-table) script sample.

**Usage:  CopyGPO.wsf &lt;SourceGPO&gt; &lt;TargetGPO&gt; \[/SourceDomain:&lt;DNSDomainName&gt;\] \[/TargetDomain:&lt;DNSDomainName&gt;\] \[/SourceDC:&lt;DomainController&gt;\] \[/TargetDC&lt;DomainController&gt;\] \[/MigrationTable&lt;MigrationTable&gt;\] \[/CopyACL\]**

**Example:  CopyGPO.wsf TestPolicyGPO NewProductionGPO /SourceDomain:example.microsoft.com /TargetDomain:example.microsoft.com**

## Creating a New GPO

The CreateGPO.wsf sample creates a GPO with the specified name in the specified domain.

**Usage:  CreateGPO.wsf &lt;GPOName&gt; \[/Domain:&lt;DNSDomainName&gt;\]**

**Example:  CreateGPO.wsf MyGPO /Domain:example.microsoft.com**

## Creating a Policy Environment Using an XML File

The CreateEnvironmentFromXML.wsf sample reads an XML file that specifies a policy environment, such as an organizational unit (OU) or a GPO.

The script can perform operations such as the following:

-   Create GPOs and OUs
-   Link GPOs
-   Import settings into GPOs
-   Set security on GPOs
-   Create security groups and users

Using the **Undo** switch deletes the environment. Specify the **ExcludeSettings** switch to ignore the GPO templates specified in the XML. Specify the **ExcludePermissions** switch to ignore the permissions on scopes of management (SOMs) and on GPOs. Default permissions will be used instead. To use a migration table when you import GPOs, specify the **MigrationTable** switch and the path of the migration table file. Use the **MigrationTable** switch to map security principals and paths across domains. For more information about how to create a migration table, see the CreateMigrationTable.wsf script sample. Specify the **Q** switch to enable quiet mode, which suppresses all the confirmation warnings.

**Usage:  CreateEnvironmentFromXML.wsf /xml:&lt;XmlFile&gt; \[/undo\] \[/Domain:&lt;DNSDomainName&gt;\] \[/dc:&lt;DomainControllerName&gt;\] \[/ExcludeSettings\] \[/ExcludePermissions\] \[/MigrationTable:&lt;FilePath&gt;\]**

**Example:  CreateEnvironmentFromXML.wsf /xml:TestDomain.xml /Domain:/example.microsoft.com /dc:testdomaindc-1 /MigrationTable:TestMigrationTable.xml**

## Creating an XML File that Represents a Policy Environment

The CreateXMLFromEnvironment.wsf sample reads an existing policy environment; for example, OUs, GPOs, and GPO links. The sample script creates an XML file that represents that environment. You can use this script in conjunction with the CreateEnvironmentFromXML.wsf script. If you do not specify a domain, the domain of the computer is the default.

Multiple switches are available for this script. Use the **ExcludePermissions** switch so that policy-related permissions are not recorded. Use the **StartingOU** switch to specify the Lightweight Directory Access Protocol (LDAP) path of an OU from which the XML should be built, rather than parsing the entire domain. Specify the **IncludeUsers** switch to include user accounts. Use the **IncludeAllGroups** switch to include groups from the Users container and from the domain root. If you do not specify the **IncludeAllGroups** switch, the script adds only the groups defined in the OUs to the XML file. If you specify a template path, the GPOs are exported to the specified location. Use the **/TemplatePath** switch to specify the location in which you want to store the backups of the GPO templates that contain the policy settings.

**Usage:  CreateXMLFromEnvironment.wsf &lt;OutputFile&gt; \[/Domain:&lt;DNSDomainName&gt;\] \[/dc:&lt;DomainControllerName&gt;\] \[/TemplatePath:&lt;Path&gt;\] \[/StartingOU:&lt;LDAPPath&gt;\] \[/ExcludePermissions\] \[/IncludeAllGroups\] \[/IncludeUsers\]**

**Example:  CreateXMLFromEnvironment.wsf TestDomain.xml /Domain:example.microsoft.com**

**Example:  CreateXMLFromEnvironment.wsf TestDomain.xml /StartingOU:OU=marketing,DC=MyDomain,DC=COM**

**Example:  CreateXMLFromEnvironment.wsf TestDomain.xml /templatepath:\\backups**

## Create Migration Table

The CreateMigrationTable.wsf sample creates a file that contains the XML representation of the paths and the security principals for the specified GPO source.

You can specify one of the following GPO sources:

-   An individual GPO
-   A backup location
-   All the GPOs in a domain

Then, you can use the resulting XML when you perform GPO import and copy operations, which are typically performed across domains.

You can use the following switches:

-   Use the **GPO** switch to use a single GPO source when you build the XML migration table.
-   Use the **BackupLocation** switch to use GPO backups as a source when you build the XML migration table.
-   Use the **AllGPOs** switch to use all the GPOs in the domain as a source to build the XML migration table.
-   Use the **Overwrite** switch to overwrite an existing XML file instead of appending to it.
-   Use the **MapByName** switch to specify a corresponding account with the same name as the original in the destination domain.

**Usage:  CreateMigrationTable.wsf &lt;TableName&gt; \[/GPO:&lt;GPO Name&gt;\] \[/BackupLocation:&lt;FilePath&gt;\] \[/AllGPOs\] \[/Overwrite\] \[/MapByName\] \[/Domain:&lt;DNSDomainName&gt;\]**

**Example:  CreateMigrationTable.wsf SampleTable.xml /BackupLocation:c:\\GPOBackups /OverWrite /MapByName**

**Example:  CreateMigrationTable.wsf SampleTable.xml /GPO:TestGPO**

**Example:  CreateMigrationTable.wsf SampleTable.xml /AllGPOs /Overwrite /Domain:example.microsoft.com**

## Deleting a GPO

The DeleteGPO.wsf sample deletes a GPO. You can specify the GPO by name or by its GPO ID. If you do not specify the *KeepLinks* parameter, all the links to the GPO in the specified domain and in any sites are deleted.

**Usage:  DeleteGPO.wsf &lt;GPOName&gt; \[/KeepLinks\] \[/Domain:&lt;DNSDomainName&gt;\]**

**Example:  DeleteGPO.wsf MyGPO**

## Grant Permissions for all GPOs in a Domain

The GrantPermissionOnAllGPOs.wsf sample takes a particular domain and then grants a user or a group the specified level of permission for all the GPOs in that domain. This sample grants the specified level of permission regardless of whether those GPOs are linked to an OU or not. Use the **Permission** switch to specify a permission level of Read, Apply, Edit, FullEdit, or None for the security principal specified in the *GroupName* parameter. Use the **Replace** switch to remove existing permissions for the group or user before you make the change. If a group or a user is already granted a permission level that is higher than the new permission level, and you do not specify the **Replace** switch, no change is made.

Consider the following example:

-   The new permission level is Edit
-   The user already has Full Edit permission

In this example, if you do not use the **Replace** switch, the user retains the Full Edit permission because the change is not applied

**Usage:  GrantPermissionOnAllGPOs.wsf &lt;Group Name&gt; /Permission: &lt;Permission Level&gt; \[/Replace\] \[/Domain:&lt;DNSDomainName&gt;\]**

**Example:  GrantPermissionOnAllGPOs.wsf "Marketing Group Administrators"/Permission:FullEdit /Replace**

**Example:  GrantPermissionOnAllGPOs.wsf TestUser /Permission:Read**

## Importing a GPO

The ImportGPO.wsf sample imports the settings from a backup GPO to another GPO that you specify. Use the *BackupLocation* parameter to specify the location of the backup. Then, use the *BackupID* parameter to specify the GPO name or backup ID (GUID) of the backup to use. If you do not specify a GPO, the name of the GPO that was backed up will be used.

If you specify a GPO name or a GPO ID for the *BackupID* parameter, the script imports the most recent backup. To import an earlier version of a GPO backup, specify the unique backup ID for the backup. The unique backup ID is the string that uniquely identifies the backup within its backup directory. To retrieve the unique backup IDs for all the GPOs in a specific backup location, run the QueryBackupLocation.wsf script.

Specify the GPO to which you are importing the setting by using the *TargetGPO* parameter. Use the optional **MigrationTable** switch when you import a GPO to map security principals and paths across domains. If the specified GPO does not exist, use the **CreateIfNeeded** switch to create a new GPO.

**Usage:  ImportGPO.wsf &lt;BackupLocation&gt; &lt;BackupID&gt; \[TargetGPO\] \[/MigrationTable:&lt;FilePath&gt;\] \[/CreateIfNeeded\] \[/Domain:&lt;DNSDomainName&gt;\]**

**Example:  ImportGPO.wsf f:\\backup TestGPO NewGPO /CreateIfNeeded**

**Example:  ImportGPO.wsf f:\\backup {73624CC9-E8F2-4F05-88D2-193FAE8773CE} NewGPO /CreateIfNeeded**

## Importing Multiple GPOs into a Domain

The ImportAllGPOs.wsf sample creates new GPOs in a specified domain and imports settings into these new GPOs from a specified backup location. The script creates a new GPO and imports settings for the latest version of each backed-up GPO in the backup location. The names of the GPOs that were backed up are used for the new GPOs. The new GPOs are derived from a previous GPO backup. Therefore, if the previous GPOs still exist in the domain, they will be overwritten by the new GPOs. Any GPO settings that have been changed since the backup will be lost.

**Usage:  ImportAllGPOs.wsf &lt;BackupLocation&gt; \[/MigrationTable:&lt;FilePath&gt;\] \[Domain:&lt;DNSDomainName&gt;\]**

**Example:  ImportAllGPOs.wsf f:\\backup /MigrationTable:f:\\Table1.xml**

## Restoring a GPO

The RestoreGPO.wsf sample restores a backup GPO to the original domain from which it was saved. If the original domain is unavailable, the RestoreGPO.wsf sample fails. Use the *BackupLocation* parameter to specify the location of the backup. Then, use the *BackupID* parameter to specify the GPO name or the backup ID (GUID) of the backup to use.

If you specify a GPO name or a GPO ID for the *Backup* parameter, the script restores the most recent backup. To restore an earlier version of a GPO backup, specify the unique backup ID for the backup. The unique backup ID is the string that uniquely identifies the backup in its backup directory. To retrieve the unique backup IDs for all the GPOs in a backup location, run the QueryBackupLocation.wsf script.

**Usage:  RestoreGPO.wsf &lt;BackupLocation&gt; &lt;BackupID&gt; \[/Domain:&lt;Domain&gt;\] \[/DC:&lt;DomainController&gt;\]**

**Examples:  RestoreGPO.wsf f:\\backup BackUpGPO**

**RestoreGPO.wsf f:\\backup {73624CC9-E8F2-4F05-88D2-193FAE8773CE}**

## Restoring all GPOs in a Domain

The RestoreAllGPOs.wsf sample restores the most recent backup of each GPO that is backed up to Active Directory in a specified backup location.

**Usage:  RestoreAllGPOs.wsf &lt;BackupLocation&gt; \[/Domain:&lt;DNSDomainName&gt;\]**

**Examples:  RestoreAllGPOs.wsf f:\\backup /Domain:example.microsoft.com**

## Setting GPO Permissions

The SetGPOPermissions.wsf sample takes a GPO name or GPO ID, group or user name, and permission level and grants that level of permission on the GPO. Use the **Permission** switch to specify a permission level of Read, Apply, Edit, FullEdit, or None for the security principal that is specified in the *GroupName* parameter. Use the **Replace** switch to remove the existing permissions for the group or user before you make the change. Otherwise, the script ensures that the group or user has at least the specified permission level.

**Usage:  SetGPOPermissions.wsf:&lt;GPOName&gt;&lt;GroupName&gt; /Permission:&lt;PermissionLevel&gt; \[/Replace\] \[/Domain:&lt;DNSDomainName&gt;\]**

**Example:  SetGPOPermissions.wsf TestGPO TestGroup /Permission:Edit**

**Example:  SetGPOPermissions.wsf TestGPO TestGroup /Permission:Edit**

**Example:  SetGPOPermission.wsf {73624CC9-E8F2-4F05-88D2-193FAE8773CE}TestUser /Permission:FullEdit /Replace /Domain:example.microsoft.com**

## Setting Permissions for All GPOs Linked to a Scope of Management

The SetGPOPermissionsBySOM.wsf sample grants a user or group a specified permission level for all the GPOs that are linked to a specified SOM (a site, a domain, or an OU). Use the **Permission** switch to specify a permission level of Read, Apply, Edit, FullEdit, or None for the security principal that is specified in the *GroupName* parameter. Use the **Replace** switch to remove existing permissions for the group or user before you make the change. If a group or a user has a permission level that is higher than the new permission level, and you do not specify the **Replace** switch, no change is made.

Consider the following example:

-   The new permission level is Edit
-   The user already has Full Edit permission

In this example, if you do not use the **Replace** switch, the user retains the Full Edit permission because the change is not applied. Use the **Recursive** switch to apply the change to all the child OUs of the specified SOM.

**Usage:  SetGPOPermissionsBySOM.wsf &lt;SOM Name&gt; &lt;Group Name&gt; /Permission: &lt;PermissionLevel&gt; \[/Recursive\] \[/Replace\] \[/Domain:&lt;DNSDomainName&gt;\]**

**Example:  SetGPOPermissionsBySOM.wsf "Marketing Group Administrators" "Marketing Group" /Permission:FullEdit /Recursive**

**Example:** SetGPOPermissionsBySOM.wsf MarketingOU TestUser /Permission:Read /Replace

## Setting Permissions to Create GPOs

The SetGPOCreationPermissions.wsf sample grants or removes the permissions that let a user or security group create GPOs in a domain.

**Usage:  SetGPOCreationPermissions.wsf &lt;GroupName&gt; \[Remove\] \[/Domain:&lt;DNSDomainName&gt;\]**

**Example:  SetGPOCreationPermissions.wsf "Policy Administrators"**

**Example:  SetGPOCreationPermissions.wsf TestUser /remove**

## Setting Policy-related Permissions on a SOM

The SetSOMPermissions.wsf sample grants a user or group the specified level of permission on a specified SOM (a site, a domain, or an OU). Use the **Permission** switch to specify a permission level of LinkGPOs, RSoPLogging, RSoPPlanning, All, or None for the SOM. You can specify either the display name or the full LDAP path of the SOM for the SOM Name parameter. The **Inherit** switch causes all child containers to inherit the setting. RSoP planning mode requires, at least, a Windows Server domain controller to perform the query, and is not applicable to sites.

**Usage:  SetSOMPermissions.wsf &lt;SOM Name&gt; &lt;Group Name&gt; /Permission:&lt;PermissionLevel&gt; \[/Inherit\] \[/Domain:&lt;DNSDomainName&gt;\]**

**Example:  SetSOMPermissions.wsf "Test Marketing OU" "Marketing Admin Group" /Permission:All /Inherit**

**Example:  SetSOMPermission.wsf MarketingOU TestUser /Permission:LinkGPOs**

## Listing All GPOs in a Domain

The ListAllGPOs.wsf sample prints a list of all the GPOs in the specified domain.

> [!Note]  
> Using the **/v** switch creates detailed or verbose output for each GPO.

 

**Usage:  ListAllGPOs.wsf \[/v\] \[/Domain:&lt;DNSDomainName&gt;\]**

**Example:  ListAllGPOs.wsf /v /Domain:example.microsoft.com**

## Listing Disabled GPOs

The FindDisabledGPOs.wsf sample prints a list of all the GPOs that are disabled or partially disabled in the specified domain. This script enumerates both fully and partially disabled GPOs. The results are grouped accordingly.

**Usage:  FindDisabledGPOs.wsf \[/Domain:&lt;DNSDomainName&gt;\]**

**Example:  FindDisabledGPOs.wsf /Domain:example.microsoft.com**

## Listing GPO Information

The DumpGPOInfo.wsf sample prints information for a specified GPO. You can specify the GPO by its name or its GPO ID.

**Usage:  DumpGPOInfo.wsf GPOName \[/Domain:&lt;DNSDomainName&gt;\]**

**Example:  DumpGPOInfo.wsf MyGPO /Domain:example.microsoft.com**

## Listing GPOs at a Backup Location

The QueryBackupLocation.wsf sample prints a list of the GPOs that have been backed up to a specified file system location. For each backed-up GPO, the **Verbose** switch displays detailed information, such as the ID, the backup time, and any comments.

**Usage:  QueryBackupLocation.wsf &lt;path&gt; \[/Verbose\]**

**Example:  QueryBackupLocation.wsf \\\\server\\share\\GPOBackups /Verbose**

## Listing GPOs by Policy Extension

The FindGPOsByPolicyExtension.wsf sample prints a list of all the GPOs in the specified domain for which a specific policy extension is configured. For example, the script prints all the GPOs in the domain for which the Software Installation or Folder Redirection policy extensions are configured. You can specify either the GUID or the display name of the client-side extension. To determine which client-side extensions are registered locally, use the **PrintCSE** switch.

**Usage:  FindGPOsByPolicyExtension.wsf &lt;ExtensionID&gt; \[/PrintCSE\] \[/Domain:&lt;DNSDomainName&gt;\]**

**Example:  FindGPOsByPolicyExtension.wsf "Software Installation"**

This example lists all the GPOs that define policy settings for the 'Software Installation' policy extension.

**Example:  FindGPOsByPolicyExtension.wsf /PrintCSE**

This example lists all CSEs that are installed locally.

## Listing GPOs by Security Group

The FindGPOsBySecurityGroup.wsf sample prints a list of all the GPOs on which a security principal has the specified permission level. Use the **Permission** switch to specify the permission level (Read, Apply, Edit, or Full Edit) for the security principal that you want to find. If no permission is specified, the script queries for all the GPOs that have the Apply permission level. Use the **Effective** switch to display the GPOs with a specific set of permissions, whether the permissions are explicitly set or derived as a result of group membership. Use the **None** switch to display the GPOs that do not have the specified permission for the specified group or user.

**Usage:  FindGPOsBySecurityGroup.wsf &lt;GroupName&gt; /Permission:&lt;PermissionLevel&gt; \[/Effective\] \[/Domain:&lt;DNSDomainName&gt;\] \[/None\]**

**Example:  FindGPOsBySecurityGroup.wsf "Domain Administrators" /Permission:Edit /Effective**

## Listing GPOs orphaned in SYSVOL

The FindOrphanGPOsInSYSVOL.wsf sample finds and then prints all the GPOs in SYSVOL that do not have a corresponding Active Directory source. These GPOs are usually referred to as *orphaned* GPOs.

Usually, a GPO becomes orphaned through one of the following ways:

-   The GPO was deleted directly through ADSI Edit.
-   The GPO was deleted by someone who had permissions to delete the GPO in Active Directory, but not in the SYSVOL directory.

In these cases, the Active Directory portion of the GPO is deleted, but the SYSVOL portion of the GPO remains. Use the **Domain** switch to specify a domain to search for orphaned GPOs.

**Usage:  FindOrphanGPOsInSYSVOL.wsf \[/Domain:&lt;DNSDomainName&gt;\]**

**Example:  FindOrphanGPOsInSYSVOL.wsf /Domain:example.microsoft.com**

## Listing GPOs with Duplicate Names

The FindDuplicateNamedGPOs.wsf sample prints a list of all the GPOs in the specified domain that have duplicate names.

**Usage:  FindDuplicateNamedGPOs.wsf \[/Domain:&lt;DNSDomainName&gt;\]**

**Example:  FindDuplicateNamedGPOs.wsf /domain:example.microsoft.com**

## Listing GPOs Without Security Filtering

The FindGPOsWithNoSecurityFiltering.wsf sample prints a list of all the GPOs for which apply permissions are not set. These GPOs exist, but they are not applied to any computers or users.

**Usage:  FindGPOsWithNoSecurityFiltering.wsf \[/Domain:&lt;DNSDomainName&gt;\]**

**Example:  FindGPOsWithNoSecurityFiltering.wsf /Domain:example.microsoft.com**

## Listing SOM Information

The DumpSOMInfo.wsf sample prints policy information about a specified SOM (a site, a domain, or an OU). The information that is printed includes information about the GPOs that are linked to the SOM and information about the policy permission on that SOM. Use the **ShowInheritedLinks** switch to show the inherited GPO links for the SOM.

**Usage:  DumpSOMInfo.wsf &lt;SOM Name&gt; \[/ShowInherited\] \[/Domain:&lt;DNSDomainName&gt;\]**

**Example:  DumpSOMInfo.wsf "Test OU" /ShowInherited /Domain:example.microsoft.com**

## Listing SOMs With Links to GPOs in External Domains

The FindSOMsWithExternalGPOLinks.wsf sample prints a list of all the SOMs in the specified domain that link to a GPO in a different domain.

**Usage:  FindsSOMsWithExternalGPOLinks.wsf \[/Domain:&lt;DNSDomainName&gt;\]**

**Example:  FindsSOMsWithExternalGPOLinks.wsf /Domain:example.microsoft.com**

## Listing Unlinked GPOs in a Domain

The FindUnlinkedGPOs.wsf sample prints a list of all the GPOs in the specified domain that have no links. Links outside the domain, including site links, are not included in the list.

**Usage:  FindUnlinkedGPOs.wsf \[/Domain:&lt;DNSDomainName&gt;\]**

**Example:  FindUnlinkedGPOs.wsf /Domain:example.microsoft.com**

## Printing the SOM Policy Tree

The ListSOMPolicyTree.wsf sample prints a list of all the SOMs (all of the sites, domains, and OUs) in the specified domain. For each SOM in the list, a list of the GPOs that are linked to it is printed.

**Usage:  ListSOMPolicyTree.wsf \[/Domain:&lt;DNSDomainName&gt;\]**

**Example:  ListSOMPolicyTree.wsf /Domain:example.microsoft.com**

## Generate Reports for all GPOs

The GetReportsForAllGPOs.wsf sample generates two files for each GPO in the domain. The first file is an XML file that contains information such as details, links, security filtering, WMI filtering, delegation, computer, and user configurations for the GPO. The second file is an HTML representation of the GPO data. Use the *ReportLocation* parameter to specify the location in which you want to generate the files. Use the **Domain** switch to specify the domain that you want to run the report against.

**Usage:  GetReportsForAllGPOs.wsf &lt;ReportLocation&gt; \[/Domain:&lt;DNSDomainName&gt;\]**

**Example:  GetReportsForAllGPOs.wsf c:\\reports**

## Generate Reports for a GPO

The GetReportsForGPO.wsf sample generates two files for a specified GPO or GPO ID in the domain. The first file is an XML file that contains information such as details, links, security filtering, WMI filtering, delegation, computer and user configurations for the GPO. The second file is an HTML representation of the GPO data. Use the *ReportLocation* parameter to specify the location in which you want to generate the files. Use the **Domain** switch to specify the domain that you want to run the report against.

**Usage:  GetReportsForGPO.wsf &lt;GPOName&gt; &lt;ReportLocation&gt; \[/Domain:&lt;DNSDomainName&gt;\]**

**Example:  GetReportsForGPO.wsf TestGPO c:\\reports /Domain:test.microsoft.com**

**Example:  GetReportsForGPO.wsf {73624CC9-E8F2-4F05-88D2-193FAE8773CE} c:\\reports**

 

 





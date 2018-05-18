---
title: GPMC Interfaces
description: The following table lists the Group Policy Management Console (GPMC) interfaces.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a02e9261-8bf5-4e1e-ae3f-64a763f93751'
ms.prod: 'windows-server-dev'
ms.technology: 'group-policy'
ms.tgt_platform: multiple
---

# GPMC Interfaces

The following table lists the Group Policy Management Console (GPMC) interfaces.



| Interface                                                  | Description                                                                                                                                                                                                                                                                                         |
|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IGPM**](igpm.md)                                       | Accesses GPMC interfaces to retrieve GPMC information and to create objects. Manages and queries Group Policy Objects (GPOs) and GPO links. Queries scope of management (SOM) objects.                                                                                                              |
| [**IGPMAsyncCancel**](igpmasynccancel.md)                 | Cancels an asynchronous GPMC operation, such as a backup, restore, import, copy, or report generation. The GPMC function called by the client asynchronously returns a pointer to the [**IGPMAsyncCancel**](igpmasynccancel.md) interface. **IGPMAsyncCancel** is not available through scripting. |
| [**IGPMAsyncProgress**](igpmasyncprogress.md)             | Enables client notification about the progress of an operation. Implemented by the client, and passed as a parameter to GPMC methods that can run asynchronously. [**IGPMAsyncProgress**](igpmasyncprogress.md) is not available through scripting.                                                |
| [**IGPMBackup**](igpmbackup.md)                           | Retrieves the properties of [**GPMBackup**](igpmbackup.md) objects. Deletes **GPMBackup** objects.                                                                                                                                                                                                 |
| [**IGPMBackupCollection**](igpmbackupcollection.md)       | Accesses a collection of GPO backups.                                                                                                                                                                                                                                                               |
| [**IGPMBackupDir**](igpmbackupdir.md)                     | Queries GPO backups and GPO backup collections.                                                                                                                                                                                                                                                     |
| [**IGPMClientSideExtension**](igpmclientsideextension.md) | Queries client-side extension properties such as the ID and the display name.                                                                                                                                                                                                                       |
| [**IGPMConstants**](igpmconstants.md)                     | Retrieves the values of GPMC constants.                                                                                                                                                                                                                                                             |
| [**IGPMCSECollection**](igpmcsecollection.md)             | Accesses a collection of client-side extension objects.                                                                                                                                                                                                                                             |
| [**IGPMDomain**](igpmdomain.md)                           | Queries SOM objects. Creates, restores, and queries GPOs. Creates and queries WMI filters. WMI filter queries use WMI Query Language (WQL).                                                                                                                                                         |
| [**IGPMGPO**](igpmgpo.md)                                 | Manages an individual GPO. Deletes, copies, imports, or backs up a GPO. Enables or disables user and computer configuration options. Sets security information. Retrieves multiple GPO properties for a given GPO, and generates reports of the settings in the GPO.                                |
| [**IGPMGPOCollection**](igpmgpocollection.md)             | Accesses a collection of GPOs.                                                                                                                                                                                                                                                                      |
| [**IGPMGPOLink**](igpmgpolink.md)                         | Manages a GPO link from a SOM. Sets and retrieves the properties of GPO links, such as the link order or whether a link is enabled or enforced.                                                                                                                                                     |
| [**IGPMGPOLinksCollection**](igpmgpolinkscollection.md)   | Accesses a collection of GPO links.                                                                                                                                                                                                                                                                 |
| [**IGPMPermission**](igpmpermission.md)                   | Retrieves permission properties.                                                                                                                                                                                                                                                                    |
| [**IGPMResult**](igpmresult.md)                           | Retrieves status message information while performing GPMC operations on GPOs, such as restore, import, backup, and copy operations.                                                                                                                                                                |
| [**IGPMRSOP**](igpmrsop.md)                               | Queries Resultant Set of Policy (RSoP) in logging or planning mode. Generates RSoP reports.                                                                                                                                                                                                         |
| [**IGPMSearchCriteria**](igpmsearchcriteria.md)           | Defines the criteria for search operations.                                                                                                                                                                                                                                                         |
| [**IGPMSecurityInfo**](igpmsecurityinfo.md)               | Defines the set of permissions that exist on a SOM, GPO, or WMI filter. Removes or adds permissions.                                                                                                                                                                                                |
| [**IGPMSitesContainer**](igpmsitescontainer.md)           | Queries SOM objects for particular sites in a forest.                                                                                                                                                                                                                                               |
| [**IGPMSOM**](igpmsom.md)                                 | Creates and retrieves GPO links for a SOM. Sets and retrieves security attributes and properties for a SOM.                                                                                                                                                                                         |
| [**IGPMSOMCollection**](igpmsomcollection.md)             | Accesses a collection of SOMs.                                                                                                                                                                                                                                                                      |
| [**IGPMStatusMessage**](igpmstatusmessage.md)             | Retrieves the properties of the status messages of GPO operations.                                                                                                                                                                                                                                  |
| [**IGPMStatusMsgCollection**](igpmstatusmsgcollection.md) | Accesses a collection of status messages.                                                                                                                                                                                                                                                           |
| [**IGPMTrustee**](igpmtrustee.md)                         | Retrieves information about a trustee that is a user, group, or computer in the domain.                                                                                                                                                                                                             |
| [**IGPMWMIFilter**](igpmwmifilter.md)                     | Sets or retrieves the security attributes and properties of a WMI filter.                                                                                                                                                                                                                           |
| [**IGPMWMIFilterCollection**](igpmwmifiltercollection.md) | Accesses a collection of WMI filters.                                                                                                                                                                                                                                                               |
| [**IGPMMapEntry**](igpmmapentry.md)                       | Retrieves map entries.                                                                                                                                                                                                                                                                              |
| [**IGPMMapEntryCollection**](igpmmapentrycollection.md)   | Accesses a collection of map entries.                                                                                                                                                                                                                                                               |
| [**IGPMigrationTable**](igpmmigrationtable.md)            | Accesses a migration table.                                                                                                                                                                                                                                                                         |



 

 

 





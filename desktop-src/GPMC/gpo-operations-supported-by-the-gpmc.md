---
title: GPO Operations Supported by the GPMC
description: The Group Policy Management Console (GPMC) supports the following Group Policy object (GPO) operations. You can access these operations through the GPMC user interface and through the GPMC COM interfaces.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '3d2b71e6-6015-4314-90c5-4624e44625cf'
ms.prod: 'windows-server-dev'
ms.technology: 'group-policy'
ms.tgt_platform: multiple
keywords: ["GPO operations"]
---

# GPO Operations Supported by the GPMC

The Group Policy Management Console (GPMC) supports the following Group Policy object (GPO) operations. You can access these operations through the GPMC user interface and through the [GPMC COM interfaces](gpmc-interfaces.md).

The following list describes these GPO operations:

-   **Backup**. Transfers the contents of a GPO from Active Directory to the file system. The contents include policy settings and core information about the GPO, such as the GPO ID GUID, the version information, the status, and the [access control lists (ACLs)](https://msdn.microsoft.com/library/windows/desktop/aa374872) associated with the GPO. A GPO that has been backed-up (also called exported) can be restored to Active Directory by calling the [**IGPMDomain::RestoreGPO**](igpmdomain-restoregpo.md) method. A GPO that has been backed-up can be imported into Active Directory using the [**IGPMGPO::Import**](igpmgpo-import.md) method. For more information about backup operations, see [**IGPMGPO::Backup**](igpmgpo-backup.md).

    > [!Note]  
    > No separate export operation or method exists. The backup operation serves as the mechanism for exporting GPOs.

     

-   **Restore**. Returns a GPO to the state the GPO was in when it was backed-up. For more information, see [**IGPMDomain::RestoreGPO**](igpmdomain-restoregpo.md).

    > [!Note]  
    > A restore operation can restore a GPO only to the original domain in which the GPO was created because the restore operation restores the original GPO ID, policy settings, and ACLs.

     

    > [!Note]  
    > A restore operation cannot modify links to the GPO because links are attributes of the scope of management (SOM), which is a site, domain, or organizational unit (OU).

     

-   **Import**. Transfers the policy settings from a backed-up GPO in the file system to a GPO in Active Directory. The source GPO can be any backed-up GPO in the file system. The destination GPO must be an existing GPO in Active Directory. The import operation only transfers policy settings. The operation erases previous policy settings in the destination GPO. An import operation does not modify the GPO ID or the ACLs on the destination GPO, nor does an import operation modify links that point to the destination GPO or to an associated WMI filter. For more information, see [**IGPMGPO::Import**](igpmgpo-import.md).
-   **Copy**. Transfers the policy settings from an existing GPO in Active Directory to a new GPO in Active Directory. The copy operation creates a new GPO with a new GPO ID. The copy operation also copies the policy settings from the source GPO to the new GPO. During the copy operation, the user can choose to copy ACLs from the source GPO to the destination GPO. Or, the user can keep the default ACLs for the GPOs on the new GPO. The new GPO created by the copy operation is unlinked because a copy operation does not transfer links. For more information, see [**IGPMGPO::CopyTo**](igpmgpo-copyto.md).

    > [!Note]  
    > Import and copy operations are similar but different. In a copy operation, the source GPO must be in Active Directory. The copy operation creates a new GPO with a new GPO ID. In an import operation, the source GPO must be in the file system. And, the destination GPO must be an existing GPO in Active Directory.

     

-   **Advanced options for import and copy operations**. To facilitate import and copy operations across domains and forests, the GPMC enables administrators to map certain policy settings to new values. This can be useful if you maintain separate test and production environments. For more information, see [Copying and Importing GPOs Across Domains](copying-and-importing-gpos-across-domains.md).

 

 





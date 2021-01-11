---
description: Services configuration enables the Windows Installer to customize the services on a computer.
ms.assetid: 164280b2-1c75-49d2-ac04-c3654be84134
title: Using Services Configuration
ms.topic: article
ms.date: 05/31/2018
---

# Using Services Configuration

Services configuration enables the Windows Installer to customize the [services](../services/services.md) on a computer. Developers can author a Windows Installer package to install, stop, start and delete services during an installation by using the [ServiceControl](servicecontrol-table.md) and [ServiceInstall](serviceinstall-table.md) tables and the [InstallServices](installservices-action.md), [StopServices](stopservices-action.md) and [DeleteServices](deleteservices-action.md) actions.

Beginning with packages written for Windows Installer 5.0, developers can also use the [MsiConfigureServices](msiconfigureservices-action.md) standard action and the [MsiServiceConfig table](msiserviceconfig-table.md) to configure the extended service customization options available with Windows 7 and Windows Server 2008 R2 and Windows Vista and Windows Server 2008. Existing installation packages written for versions of the Windows Installer that did not include the MsiServiceConfig table can be still be installed using Windows Installer 5.0. The services configuration feature of the Windows Installer cannot configure network service accounts, install shared service host (svchost) processes, or restart services stopped as part of the installation.

**Windows XP and Windows Server 2003 or earlier:** Not supported. The service configuration tables and standard actions are available beginning with Windows Installer 5.0 running on Windows 7 and Windows Server 2008 R2 and Windows Installer 4.5 running on Windows Vista and Windows Server 2008.

You must include the [MsiConfigureServices](msiconfigureservices-action.md) action in the [InstallExecuteSequence](installexecutesequence-table.md) table to request the service configurations that you specify in the [MsiServiceConfig table](msiserviceconfig-table.md). The Windows Installer uses the information in the MsiServiceConfig table only when the MsiConfigureServices standard action is included in a sequence table. The MsiConfigureServices standard action also uses information in the [ServiceControl](servicecontrol-table.md) and [ServiceInstall](serviceinstall-table.md) tables.

To request that the system give only required privileges to a particular service, specify the service and the **SERVICE\_CONFIG\_REQUIRED\_PRIVILEGES\_INFO** configuration option in the [MsiServiceConfig table](msiserviceconfig-table.md). Remove the unneeded privileges from the service's process token. This option can be used to configure services run in the security context of the LocalSystem, LocalService, or NetworkService [service user accounts](../services/service-user-accounts.md).

To request that the system delay the automatic start of a service for a time after the start of all other auto-start services, specify the service and the **SERVICE\_CONFIG\_DELAYED\_AUTO\_START** option in the [MsiServiceConfig table](msiserviceconfig-table.md). The service being delayed must be installed by the current package with SERVICE\_AUTO\_START specified in the [ServiceInstall](serviceinstall-table.md) table or the service must already be installed as an auto-start service.

To request that the system reserve a resource for the exclusive use of a particular service, specify the service, the service SID type, and the **SERVICE\_CONFIG\_SERVICE\_SID\_INFO** configuration option in the [MsiServiceConfig table](msiserviceconfig-table.md). Add the service's SID to the resource's Access Control List (ACL) for the resource.

To request that the [Service Control Manager](../services/service-control-manager.md) (SCM) wait after sending the **SERVICE\_CONTROL\_PRESHUTDOWN** notification to a service, do the following. Specify the service, the length of time the SCM should wait, and the **SERVICE\_CONFIG\_PRESHUTDOWN\_INFO** configuration option in the [MsiServiceConfig table](msiserviceconfig-table.md).

To configure when the system should run actions after the failure of a service, specify the service and the **SERVICE\_CONFIG\_FAILURE\_ACTIONS\_FLAG** option in the [MsiServiceConfig table](msiserviceconfig-table.md). Add the actions to be run to the [MsiServiceConfigFailureActions table](msiserviceconfigfailureactions-table.md).

For more about the extended service customization capabilities introduced with the Windows Vista and Windows Server 2008 operating systems, see [Service Changes for Windows Vista](../services/service-changes-for-windows-vista.md).

 

 

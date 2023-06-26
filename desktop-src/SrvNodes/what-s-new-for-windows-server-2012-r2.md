---
description: The following list describes new and updated feature areas for Windows Server 2012 and Windows Server 2012 R2. For more information on new Windows 8 and Windows 8.1 technologies, see Windows 8 and Windows 8.1 Technologies.
ms.assetid: bd8b4dd8-e0b7-4340-a6bd-1baa42d9a1dd
title: "What's New: Windows Server 2012 R2 & Windows Server 2012"
ms.topic: article
ms.date: 05/31/2018
---

# What's New: Windows Server 2012 R2 & Windows Server 2012

The following list describes new and updated feature areas for Windows Server 2012 and Windows Server 2012 R2. For more information on new Windows 8 and Windows 8.1 technologies, see [Windows 8 and Windows 8.1 Technologies](/previous-versions/windows/desktop/whatsnew/windows-8-technologies).

## What's New for Windows Server 2012 R2

-   [Data Deduplication](/previous-versions/windows/desktop/dedup/data-deduplication-api-portal)

    Data deduplication finds and removes duplication within data on a volume while ensuring that the data remains correct and complete. This makes it possible to store more file data in less space on the volume. For Windows Server 2012 R2, a number of parameters and error codes were activated, and the [**MSFT\_DedupFileMetadata**](/previous-versions/windows/desktop/dedup/msft-dedupfilemetadata) class was added.

-   [Software Inventory Logging](/previous-versions/windows/desktop/sil/software-inventory-logging-portal)

    **New!** Software Inventory Logging collects licensing data about software installed on a Windows Server, and provides remote access to the data so it can be aggregated easily by a datacenter.

-   [iSCSI Target Server](/previous-versions/windows/desktop/iscsitarg/iscsi-software-target-api-portal)

    The iSCSI Target Server API provides Windows Management Instrumentation (WMI) providers for managing the Microsoft iSCSI Target Server, such as creating virtual disks, and for presenting them to the client. A number of new features were added for Windows Server 2012 R2.

-   [Mobile Device Management Registration](../mdmreg/mobile-device-management-registration-portal.md)

    **New!** An industry trend has been developing in which employees connect their personal mobile computing devices to the corporate network and resources (either on premise or through the cloud) to perform workplace tasks. This trend requires support for easy configuration of the network and resources, such that employees can register personal devices with the company for work-related purposes. Applications and technology to support easy configuration must also enable IT professionals to manage the risk associated with having uncontrolled devices connected to the corporate network. The Mobile Device Management (MDM) registration enrolls a device into a management service.

-   [Windows PowerShell](/powershell/scripting/overview)

    Windows PowerShell is a task-based command-line shell and scripting language designed especially for system administration. New in Windows Server 2012 R2, Windows PowerShell v4 supports Desired State Configuration, which is a new management platform in Windows PowerShell that enables deploying and managing configuration data for software services and managing the environment in which these services run.

## What's New for Windows Server 2012

-   [Windows Clustering](/previous-versions/windows/desktop/mscs/windows-clustering)

    Windows Clustering allows you to manage both network load-balanced clusters as well as failover clusters. A number of new features were added in this release, including new Group management features, common properties, and integration with WMI.

-   [User Access Logging](/previous-versions/windows/desktop/ual/user-access-logging)

    **New!** User Access Logging (UAL) is a common framework for Windows Server roles to report their respective consumption metrics. This UAL framework is a foundational and critical component of the larger licensing management solution.

-   [Windows Remote Management](../winrm/portal.md)

    Windows Remote Management (WinRM) is the Microsoft implementation of WS-Management Protocol, a standard Simple Object Access Protocol (SOAP)-based, firewall-friendly protocol that allows hardware and operating systems, from different vendors, to interoperate. Windows Server 2012 includes a number of Connection API's that focus on interacting with running instances and shells.

-   [Windows Management Infrastructure](/previous-versions/windows/desktop/wmi_v2/what-s-new-in-mi)

    **New!** The Windows Management Infrastructure (MI) features represent the latest version of the Windows Management Instrumentation (WMI) technologies, which are based on the CIM standard from DMTF (Distributed Management Task Force). MI is fully compatible with previous versions of WMI and provides a host of features and benefits that make designing and developing providers and clients easier than ever.

-   [Data Deduplication](/previous-versions/windows/desktop/dedup/data-deduplication-api-portal)

    **New!** Data deduplication finds and removes duplication within data on a volume while ensuring that the data remains correct and complete. This makes it possible to store more file data in less space on the volume.

-   [iSCSI Target Server](/previous-versions/windows/desktop/iscsitarg/iscsi-software-target-api-portal)

    **New!** The iSCSI Target Server API provides Windows Management Instrumentation (WMI) providers for managing the Microsoft iSCSI Target Server, such as creating virtual disks, and for presenting them to the client.

-   [NFS Provider for WMI](/previous-versions/windows/desktop/nfswmi/wmi-provider-for-nfs-portal)

    **New!** The NFS WMI provider provides a means of managing NFS server and client settings, file shares, netgroups, and client groups.

-   [Offline Files](../devnotes/offline-files.md)

    The Offline Files API allows applications to control and monitor the behavior of Offline Files programmatically. Windows Server 2012 adds the [**OfflineFilesQueryStatusEx**](/previous-versions/windows/desktop/api/cscapi/nf-cscapi-offlinefilesquerystatusex), [**OfflineFilesStart**](/previous-versions/windows/desktop/api/cscapi/nf-cscapi-offlinefilesstart) and [**RenameItem**](/previous-versions/windows/desktop/offlinefiles/win32-offlinefilescache-renameitem) functions.

-   [SMB Management](/previous-versions/windows/desktop/smb/smb-management-api-portal)

    **New!** The SMB Management API provides WMI classes and methods to manage shares and share access.

-   [Server Core](/previous-versions/windows/desktop/legacy/hh846323(v=vs.85))

    Windows Server provides minimal server installation options for computers running on the Windows Server 2008 operating system or later. Windows Server 2012 offers Server Core as both a configuration as well as an installation options.

-   [Windows Server Backup](/previous-versions/windows/desktop/wsb/windows-server-backup-portal)

    The Windows Server Backup feature automatically backs up and restores application data. Windows Server 2012 includes the Cloud Backup Provider API.

-   [Windows Desktop Sharing](/previous-versions/windows/desktop/rdp/rdp-portal)

    Windows Desktop Sharing is a multiple-party screen-sharing technology. Windows Server 2012 implements this technology using the Windows Duplication API.

-   [Remote Desktop Services](../termserv/terminal-services-portal.md)

    Windows Desktop Sharing allows the user to remotely access an instance of the operating system. Windows Server 2012 includes a number of new features, including Child sessions, RemoteFX Media redirection, and the Remote Desktop Broker client.

-   [Windows PowerShell](/powershell/scripting/overview)

    Windows PowerShell is a task-based command-line shell and scripting language designed especially for system administration. New in Windows Server 2012, Windows PowerShell v3 supports Windows PowerShell Workflow, which leverages the benefits of Windows Workflow Foundation to allow the automation of long-running tasks.

-   [Management OData](/powershell/scripting/windows-powershell/wmf/overview)

    **New!** Also known as Windows PowerShell Web Services, Management OData, new in Windows PowerShell v3, allows the creation of an ASP.NET web service end point that exposes management data, acessed through Windows PowerShell commands, as OData web service entities.

## Related topics

<dl> <dt>

[Windows Server 2012 R2 on TechNet](/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/hh801901(v=ws.11))
</dt> <dt>

[Windows Server 2012 R2 and Windows Server 2012 on TechNet Library](/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/hh801901(v=ws.11))
</dt> <dt>

[Windows Server 2012 R2 on Microsoft.Com](https://www.microsoft.com/evalcenter/evaluate-windows-server-2012-r2-essentials)
</dt> </dl>

 

 

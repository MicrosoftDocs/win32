---
description: Describes how to find the correct WMI class and procedures to use in scripts and applications that perform common computer and network administration tasks.
ms.assetid: fe15b67c-8ae6-4360-a2ee-1eda292dd05a
ms.tgt_platform: multiple
title: WMI Tasks for Scripts and Applications
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# WMI Tasks for Scripts and Applications

The following sections describe various computer and network administration tasks and provide links to the WMI class or classes used to perform those tasks. For more information, see [Creating a WMI Application or Script](creating-a-wmi-application-or-script.md). For more information about using WMI, see [Further Information](further-information.md). For more information about using WMI, see [TechNet ScriptCenter](https://www.microsoft.com/technet/scriptcenter/default.mspx). (These resources may not be available in every language or country/region.)

For more information about how to provide data to WMI, see [Using WMI](using-wmi.md), which will reference topics about writing a WMI [*provider*](gloss-p.md).

The operations shown in script examples can be performed by applications in C++ or Visual Basic. For more information, see [Creating a WMI Application Using C++](creating-a-wmi-application-using-c-.md) and [WMI C++ Application Examples](wmi-c---application-examples.md).

The following table lists the categories of tasks.



| Task Categories                                                               | Description                                                                                                                                                                                                                                                                                                                                               |
|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Accounts and Domains](wmi-tasks--accounts-and-domains.md)                   | Obtain information such as the computer domain or the currently logged-on user. Many domain- or account-related tasks are best performed with [ADSI](/windows/desktop/ADSI/active-directory-service-interfaces-adsi) scripts. For examples, see the TechNet ScriptCenter at [https://www.microsoft.com/technet](https://technet.microsoft.com/default.aspx). |
| [Computer Hardware](wmi-tasks--computer-hardware.md)                         | Obtain information about the presence, state, or properties of hardware components. For example, you can determine whether a computer is a desktop or laptop.                                                                                                                                                                                             |
| [Computer Software](wmi-tasks--computer-software.md)                         | Obtain information such as which software is installed by the Windows Installer (MSI) and software versions.                                                                                                                                                                                                                                              |
| [Connecting to the WMI Service](wmi-tasks--connecting-to-the-wmi-service.md) | To get data from WMI, either on the local computer or from a remote computer, you must connect to the WMI service by connecting to a specific [*namespace*](gloss-n.md). In most cases, use either the shorthand [moniker](creating-a-wmi-script.md) connection or the [**Locator**](swbemlocator-connectserver.md) connection.    |
| [Dates and Times](wmi-tasks--dates-and-times.md)                             | There are WMI classes and a scripting object to parse or convert the [CIM datetime](date-and-time-format.md) format.                                                                                                                                                                                                                                     |
| [Desktop Management](wmi-tasks--desktop-management.md)                       | Obtain data from or control remote desktops. For example, you can determine whether or not the screensaver requires a password. WMI also gives you the ability shut down a remote computer.                                                                                                                                                               |
| [Disks and File Systems](wmi-tasks--disks-and-file-systems.md)               | Obtain information about disk drive hardware state, logical volumes.                                                                                                                                                                                                                                                                                      |
| [Event Logs](wmi-tasks--event-logs.md)                                       | Obtain event data from NT Event log files and perform operations like backing up or clearing log files.                                                                                                                                                                                                                                                   |
| [Files and Folders](wmi-tasks--files-and-folders.md)                         | Change file or folder properties through WMI, including creating a share or renaming a file.                                                                                                                                                                                                                                                              |
| [Networking](wmi-tasks--networking.md)                                       | Manage and obtain information about connections and IP or MAC addresses.                                                                                                                                                                                                                                                                                  |
| [Operating Systems](wmi-tasks--operating-systems.md)                         | Obtain information about the operating system such as version, whether it is activated, or which hotfixes are installed.                                                                                                                                                                                                                                  |
| [Performance Monitoring](wmi-tasks--performance-monitoring.md)               | Use the WMI classes that obtain data from performance counters to access and refresh data about computer performance.                                                                                                                                                                                                                                     |
| [Processes](wmi-tasks--processes.md)                                         | Obtain information such as the account under which a process is running. You can perform actions like creating processes.                                                                                                                                                                                                                                 |
| [Printers and Printing](wmi-tasks--printers-and-printing.md)                 | Manage and obtain data about printers, such as finding or setting the default printer.                                                                                                                                                                                                                                                                    |
| [Registry](wmi-tasks--registry.md)                                           | Create and modify registry keys and values.                                                                                                                                                                                                                                                                                                               |
| [Scheduled Tasks](wmi-tasks--scheduled-tasks.md)                             | Create and get information about scheduled tasks.                                                                                                                                                                                                                                                                                                         |
| [Services](wmi-tasks--services.md)                                           | Obtain information about services, including dependent or antecedent services.                                                                                                                                                                                                                                                                            |



 

 

 

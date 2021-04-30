---
description: The Operating System category groups classes that represent operating system related objects.
ms.assetid: D0756D8C-A3D3-4C75-96A3-8C7F05300B39
ms.tgt_platform: multiple
title: Operating System Classes
ms.topic: article
ms.date: 05/31/2018
---

# Operating System Classes

The Operating System category groups classes that represent operating system related objects. They denote the various configurations and settings that define a computing environment. Examples include: the boot configuration, Component Object Model (COM) settings, desktop environment settings, drivers, security settings, user settings, and registry settings.

The Operating System category is grouped into the following subcategories:

-   [COM](#com)
-   [Desktop](#desktop)
-   [Drivers](#drivers)
-   [Event log](#windows-event-log)
-   [File system](#file-system)
-   [Job objects](#job-objects)
-   [Memory and page files](#memory-and-page-files)
-   [Multimedia audio or visual](#multimedia-audio-or-visual)
-   [Networking](#networking)
-   [Operating system events](#operating-system-events)
-   [Operating system settings](#operating-system-settings)
-   [Processes](#processes)
-   [Registry](#registry)
-   [Scheduler jobs](#scheduler-jobs)
-   [Security](#security)
-   [Services](#services)
-   [Shares](#shares)
-   [Start menu](#start-menu)
-   [Storage](#storage)
-   [Users](#users)
-   [Windows product activation](#windows-product-activation)

## COM

The COM subcategory groups classes that represent COM and DCOM settings, classes, and client application settings.



| Class                                                                                           | Description                                                                                                                                                                          |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Win32\_ClassicCOMApplicationClasses**](win32-classiccomapplicationclasses.md)               | Association class<br/> Relates a DCOM application and a COM component grouped under it.<br/>                                                                             |
| [**Win32\_ClassicCOMClass**](win32-classiccomclass.md)                                         | Instance class<br/> Represents the properties of a COM component.<br/>                                                                                                   |
| [**Win32\_ClassicCOMClassSettings**](win32-classiccomclasssettings.md)                         | Association class<br/> Relates a COM class and the settings used to configure instances of the COM class.<br/>                                                           |
| [**Win32\_ClientApplicationSetting**](win32-clientapplicationsetting.md)                       | Association class<br/> Relates an executable and a DCOM application that contains the DCOM configuration options for the executable file.<br/>                           |
| [**Win32\_COMApplication**](win32-comapplication.md)                                           | Instance class<br/> Represents a COM application.<br/>                                                                                                                   |
| [**Win32\_COMApplicationClasses**](win32-comapplicationclasses.md)                             | Association class<br/> Relates a COM component and the COM application where it resides.<br/>                                                                            |
| [**Win32\_COMApplicationSettings**](win32-comapplicationsettings.md)                           | Association class<br/> Relates a DCOM application and its configuration settings.<br/>                                                                                   |
| [**Win32\_COMClass**](win32-comclass.md)                                                       | Instance class<br/> Represents the properties of a COM component.<br/>                                                                                                   |
| [**Win32\_ComClassAutoEmulator**](win32-comclassautoemulator.md)                               | Association class<br/> Relates a COM class and another COM class that it automatically emulates.<br/>                                                                    |
| [**Win32\_ComClassEmulator**](win32-comclassemulator.md)                                       | Association class<br/> Relates two versions of a COM class.<br/>                                                                                                         |
| [**Win32\_ComponentCategory**](win32-componentcategory.md)                                     | Instance class<br/> Represents a component category.<br/>                                                                                                                |
| [**Win32\_COMSetting**](win32-comsetting.md)                                                   | Instance class<br/> Represents the settings associated with a COM component or COM application.<br/>                                                                     |
| [**Win32\_DCOMApplication**](win32-dcomapplication.md)                                         | Instance class<br/> Represents the properties of a DCOM application.<br/>                                                                                                |
| [**Win32\_DCOMApplicationAccessAllowedSetting**](/previous-versions/windows/desktop/secrcw32prov/win32-dcomapplicationaccessallowedsetting) | Association class<br/> Relates the [**Win32\_DCOMApplication**](win32-dcomapplication.md) instance and the user security identifications (SID) that can access it.<br/> |
| [**Win32\_DCOMApplicationLaunchAllowedSetting**](/previous-versions/windows/desktop/secrcw32prov/win32-dcomapplicationlaunchallowedsetting) | Association class<br/> Relates the [**Win32\_DCOMApplication**](win32-dcomapplication.md) instance and the user SIDs that can launch it.<br/>                           |
| [**Win32\_DCOMApplicationSetting**](win32-dcomapplicationsetting.md)                           | Instance class<br/> Represents the settings of a DCOM application.<br/>                                                                                                  |
| [**Win32\_ImplementedCategory**](win32-implementedcategory.md)                                 | Association class<br/> Relates a component category and the COM class using its interfaces.<br/>                                                                         |



 

## Desktop

The Desktop subcategory groups classes that represent objects that define a specific desktop configuration.



| Class                                           | Description                                                                                                                        |
|-------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| [**Win32\_Desktop**](win32-desktop.md)         | Instance class<br/> Represents the common characteristics of a user's desktop.<br/>                                    |
| [**Win32\_Environment**](win32-environment.md) | Instance class<br/> Represents an environment or system environment setting on a computer system running Windows.<br/> |
| [**Win32\_TimeZone**](win32-timezone.md)       | Instance class<br/> Represents the time zone information for a computer system running Windows.<br/>                   |
| [**Win32\_UserDesktop**](win32-userdesktop.md) | Association class<br/> Relates a user account and the desktop settings that are specific to it.<br/>                   |



 

## Drivers

The Drivers subcategory groups classes that represent virtual device drivers and system drivers for base services.



| Class                                             | Description                                                                           |
|---------------------------------------------------|---------------------------------------------------------------------------------------|
| [**Win32\_SystemDriver**](win32-systemdriver.md) | Instance class<br/> Represents the system driver for a base service.<br/> |



 

## File System

The File System subcategory groups classes that represent the way a hard disk is logically arranged. This includes the type of file system used, the directory structure, and way the disk is partitioned.



| Class                                                                               | Description                                                                                                                                                                          |
|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Win32\_CIMLogicalDeviceCIMDataFile**](win32-cimlogicaldevicecimdatafile.md)     | Association class<br/> Relates logical devices and data files, indicating the driver files used by the device.<br/>                                                      |
| [**Win32\_Directory**](win32-directory.md)                                         | Instance class<br/> Represents a directory entry on a computer system running Windows.<br/>                                                                              |
| [**Win32\_DirectorySpecification**](/previous-versions/windows/desktop/msiprov/win32-directoryspecification)               | Instance class<br/> Represents the directory layout for the product.<br/>                                                                                                |
| [**Win32\_DiskDriveToDiskPartition**](win32-diskdrivetodiskpartition.md)           | Association class<br/> Relates a disk drive and a partition existing on it.<br/>                                                                                         |
| [**Win32\_DiskPartition**](win32-diskpartition.md)                                 | Instance class<br/> Represents the capabilities and management capacity of a partitioned area of a physical disk on a computer system running Windows.<br/>              |
| [**Win32\_DiskQuota**](/previous-versions/windows/desktop/wmipdskq/win32-diskquota)                                    | Association class<br/> Tracks disk space usage for NTFS file system volumes.<br/>                                                                                        |
| [**Win32\_LogicalDisk**](win32-logicaldisk.md)                                     | Represents a data source that resolves to an actual local storage device on a computer system running Windows.<br/>                                                            |
| [**Win32\_LogicalDiskRootDirectory**](win32-logicaldiskrootdirectory.md)           | Association class<br/> Relates a logical disk and its directory structure.<br/>                                                                                          |
| [**Win32\_LogicalDiskToPartition**](win32-logicaldisktopartition.md)               | Association class<br/> Relates a logical disk drive and the disk partition it resides on.<br/>                                                                           |
| [**Win32\_MappedLogicalDisk**](win32-mappedlogicaldisk.md)                         | Represents network storage devices that are mapped as logical disks on the computer system running Windows.<br/>                                                               |
| [**Win32\_OperatingSystemAutochkSetting**](/previous-versions//aa394240(v=vs.85)) | Association class<br/> Represents the association between a [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md) instance and the settings defined for it.<br/> |
| [**Win32\_QuotaSetting**](/previous-versions/windows/desktop/wmipdskq/win32-quotasetting)                              | Instance class<br/> Contains setting information for disk quotas on a volume.<br/>                                                                                       |
| [**Win32\_ShortcutFile**](win32-shortcutfile.md)                                   | Instance class<br/> Represents files that are shortcuts to other files, directories, and commands.<br/>                                                                  |
| [**Win32\_SubDirectory**](win32-subdirectory.md)                                   | Association class<br/> Relates a directory (folder) and one of its subdirectories (subfolders).<br/>                                                                     |
| [**Win32\_SystemPartitions**](win32-systempartitions.md)                           | Association class<br/> Relates a computer system and a disk partition on that system.<br/>                                                                               |
| [**Win32\_Volume**](/previous-versions/windows/desktop/legacy/aa394515(v=vs.85))                                               | Instance class<br/> Represents an area of storage on a hard disk.<br/>                                                                                                   |
| [**Win32\_VolumeQuota**](/previous-versions/windows/desktop/vdswmi/win32-volumequota)                                     | Association class<br/> Relates a volume to the per volume quota settings.<br/>                                                                                           |
| [**Win32\_VolumeQuotaSetting**](/previous-versions/windows/desktop/wmipdskq/win32-volumequotasetting)                  | Association class<br/> Relates disk quota settings with a specific disk volume.<br/>                                                                                     |
| [**Win32\_VolumeUserQuota**](/previous-versions/windows/desktop/vdswmi/win32-volumeuserquota)                             | Association class<br/> Relates per user quotas to quota-enabled volumes.<br/>                                                                                            |



 

## Job Objects

The Job Objects subcategory groups classes that represent classes that provide the means of instrumenting named job objects. An unnamed job object cannot be instrumented.



| Class                                                                               | Description                                                                                                                                                                                |
|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Win32\_CollectionStatistics**](/previous-versions/windows/desktop/cimwin32a/win32-collectionstatistics)                   | Association class<br/> Relates a managed system element collection and the class representing statistical information about the collection.<br/>                               |
| [**Win32\_LUID**](/previous-versions/windows/desktop/wmipjobobjprov/win32-luid)                                                   | Instance class<br/> Represents a locally unique identifier (LUID)<br/>                                                                                                         |
| [**Win32\_LUIDandAttributes**](/previous-versions/windows/desktop/wmipjobobjprov/win32-luidandattributes)                         | Instance class<br/> Represents a LUID and its attributes.<br/>                                                                                                                 |
| [**Win32\_NamedJobObject**](/previous-versions/windows/desktop/wmipjobobjprov/win32-namedjobobject)                               | Instance class<br/> Represents a kernel object that is used to group processes for the sake of controlling the life and resources of the processes within the job object.<br/> |
| [**Win32\_NamedJobObjectActgInfo**](/previous-versions/windows/desktop/wmipjobobjprov/win32-namedjobobjectactginfo)               | Instance class<br/> Represents the I/O accounting information for a job object.<br/>                                                                                           |
| [**Win32\_NamedJobObjectLimit**](/previous-versions/windows/desktop/wmipjobobjprov/win32-namedjobobjectlimit)                     | Instance class<br/> Represents an association between a job object and the job object limit settings.<br/>                                                                     |
| [**Win32\_NamedJobObjectLimitSetting**](/previous-versions/windows/desktop/wmipjobobjprov/win32-namedjobobjectlimitsetting)       | Instance class<br/> Represents the limit settings for a job object.<br/>                                                                                                       |
| [**Win32\_NamedJobObjectProcess**](/previous-versions/windows/desktop/wmipjobobjprov/win32-namedjobobjectprocess)                 | Instance class<br/> Relates a job object and the process contained in the job object.<br/>                                                                                     |
| [**Win32\_NamedJobObjectSecLimit**](/previous-versions/windows/desktop/wmipjobobjprov/win32-namedjobobjectseclimit)               | Instance class<br/> Relates a job object and the job object security limit settings.<br/>                                                                                      |
| [**Win32\_NamedJobObjectSecLimitSetting**](/previous-versions/windows/desktop/wmipjobobjprov/win32-namedjobobjectseclimitsetting) | Instance class<br/> Represents the security limit settings for a job object.<br/>                                                                                              |
| [**Win32\_NamedJobObjectStatistics**](/previous-versions/windows/desktop/wmipjobobjprov/win32-namedjobobjectstatistics)           | Instance class<br/> Represents an association between a job object and the job object I/O accounting information class.<br/>                                                   |
| [**Win32\_SIDandAttributes**](/previous-versions/windows/desktop/wmipjobobjprov/win32-sidandattributes)                           | Instance class<br/> Represents a security identifier (SID) and its attributes.<br/>                                                                                            |
| [**Win32\_TokenGroups**](/previous-versions/windows/desktop/wmipjobobjprov/win32-tokengroups)                                     | Event class<br/> Represents information about the group SIDs in an access token.<br/>                                                                                          |
| [**Win32\_TokenPrivileges**](/previous-versions/windows/desktop/wmipjobobjprov/win32-tokenprivileges)                             | Event class<br/> Represents information about a set of privileges for an access token.<br/>                                                                                    |



 

## Memory and Page Files

The Memory and Page files subcategory groups classes that represent page file configuration settings.



| Class                                                                 | Description                                                                                                                                   |
|-----------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| [**Win32\_PageFile**](win32-pagefile.md)                             | Instance class<br/> Represents the file used for handling virtual memory file swapping on a Windows system.<br/>                  |
| [**Win32\_PageFileElementSetting**](win32-pagefileelementsetting.md) | Association class<br/> Relates the initial settings of a page file and the state of those settings during normal use.<br/>        |
| [**Win32\_PageFileSetting**](win32-pagefilesetting.md)               | Instance class<br/> Represents the settings of a page file.<br/>                                                                  |
| [**Win32\_PageFileUsage**](win32-pagefileusage.md)                   | Instance class<br/> Represents the file used for handling virtual memory file swapping on a computer system running Windows.<br/> |



 

## Multimedia Audio or Visual

The class in the Multimedia Audio or Visual subcategory represents properties of the audio or video codec installed on the computer system.



| Class                                       | Description                                                                                                |
|---------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [**Win32\_CodecFile**](win32-codecfile.md) | Instance class<br/> Represents the audio or video codec installed on the computer system.<br/> |



 

## Networking

The Networking subcategory groups classes that represent network connections, network clients, and network connection settings such as the protocol used.



| Class                                                                            | Description                                                                                                                      |
|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [**Win32\_ActiveRoute**](/previous-versions/windows/desktop/wmiiprouteprov/win32-activeroute)                       | Association class<br/> Relates the current IP4 route to the persisted IP route table.<br/>                           |
| [**Win32\_IP4PersistedRouteTable**](/previous-versions/windows/desktop/wmiiprouteprov/win32-ip4persistedroutetable) | Instance class<br/> Represents persisted IP routes.<br/>                                                             |
| [**Win32\_IP4RouteTable**](/previous-versions/windows/desktop/wmiiprouteprov/win32-ip4routetable)                   | Instance class<br/> Represents information that governs the routing of network data packets.<br/>                    |
| [**Win32\_IP4RouteTableEvent**](/previous-versions/windows/desktop/wmiiprouteprov/win32-ip4routetableevent)         | Event class<br/> Represents IP route change events.<br/>                                                             |
| [**Win32\_NetworkClient**](win32-networkclient.md)                              | Instance class<br/> Represents a network client on a computer system running Windows.<br/>                           |
| [**Win32\_NetworkConnection**](win32-networkconnection.md)                      | Instance class<br/> Represents an active network connection in a Windows environment.<br/>                           |
| [**Win32\_NetworkProtocol**](win32-networkprotocol.md)                          | Instance class<br/> Represents a protocol and its network characteristics on a computer system running Windows.<br/> |
| [**Win32\_NTDomain**](/previous-versions/windows/desktop/cimwin32a/win32-ntdomain)                                        | Instance class<br/> Represents a Windows NT domain.<br/>                                                             |
| [**Win32\_PingStatus**](/previous-versions/windows/desktop/wmipicmp/win32-pingstatus)                               | Instance class<br/> Represents the values returned by the standard **ping** command.<br/>                            |
| [**Win32\_ProtocolBinding**](win32-protocolbinding.md)                          | Association class<br/> Relates a system-level driver, network protocol, and network adapter.<br/>                    |



 

## Operating System Events

The Operating System Events subcategory groups classes that represent events in the operating system related to processes, threads, and system shutdown.



| Class                                                                                 | Description                                                                                                                                                              |
|---------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Win32\_ComputerShutdownEvent**](/previous-versions/windows/desktop/cimwin32a/win32-computershutdownevent)                   | Event class<br/> Represents computer shutdown events.<br/>                                                                                                   |
| [**Win32\_ComputerSystemEvent**](/previous-versions/windows/desktop/cimwin32a/win32-computersystemevent)                       | Event class<br/> Represents events related to a computer system.<br/>                                                                                        |
| [**Win32\_DeviceChangeEvent**](win32-devicechangeevent.md)                           | Event class<br/> Represents device change events resulting from the addition, removal, or modification of devices on the computer system.<br/>               |
| [**Win32\_ModuleLoadTrace**](/previous-versions/windows/desktop/krnlprov/win32-moduleloadtrace)                               | Event class<br/> Indicates that a process has loaded a new module.<br/>                                                                                      |
| [**Win32\_ModuleTrace**](/previous-versions/windows/desktop/krnlprov/win32-moduletrace)                                       | Event class<br/> Base event for module events.<br/>                                                                                                          |
| [**Win32\_ProcessStartTrace**](/previous-versions/windows/desktop/krnlprov/win32-processstarttrace)                           | Event class<br/> Indicates that a new process has started.<br/>                                                                                              |
| [**Win32\_ProcessStopTrace**](/previous-versions/windows/desktop/krnlprov/win32-processstoptrace)                             | Event class<br/> Indicates that a process has terminated.<br/>                                                                                               |
| [**Win32\_ProcessTrace**](/previous-versions/windows/desktop/krnlprov/win32-processtrace)                                     | Event class<br/> Base event for process events.<br/>                                                                                                         |
| [**Win32\_SystemConfigurationChangeEvent**](win32-systemconfigurationchangeevent.md) | Event class<br/> Indicates that the device list on the system has been refreshed (a device has been added or removed, or the configuration changed).<br/>    |
| [**Win32\_SystemTrace**](/previous-versions/windows/desktop/krnlprov/win32-systemtrace)                                       | Event class<br/> Base class for all system trace events, including module, process, and thread traces.<br/>                                                  |
| [**Win32\_ThreadStartTrace**](/previous-versions/windows/desktop/krnlprov/win32-threadstarttrace)                             | Event class<br/> Indicates a new thread has started.<br/>                                                                                                    |
| [**Win32\_ThreadStopTrace**](/previous-versions/windows/desktop/krnlprov/win32-threadstoptrace)                               | Event class<br/> Indicates that a thread has stopped.<br/>                                                                                                   |
| [**Win32\_ThreadTrace**](/previous-versions/windows/desktop/krnlprov/win32-threadtrace)                                       | Event class<br/> Base event class for thread events.<br/>                                                                                                    |
| [**Win32\_VolumeChangeEvent**](win32-volumechangeevent.md)                           | Event class<br/> Represents a network-mapped drive event resulting from the addition of a network drive letter or mounted drive on the computer system.<br/> |



 

## Operating System Settings

The Operating System Settings subcategory groups classes that represent the Operating System and its settings.



| Class                                                                                       | Description                                                                                                                                                                        |
|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Win32\_BootConfiguration**](win32-bootconfiguration.md)                                 | Instance class<br/> Represents the boot configuration of a computer system running Windows.<br/>                                                                       |
| [**Win32\_ComputerSystem**](win32-computersystem.md)                                       | Instance class<br/> Represents a computer system operating in a Windows environment.<br/>                                                                              |
| [**Win32\_ComputerSystemProcessor**](win32-computersystemprocessor.md)                     | Association class<br/> Relates a computer system and a processor running on that system.<br/>                                                                          |
| [**Win32\_ComputerSystemProduct**](win32-computersystemproduct.md)                         | Instance class<br/> Represents a product.<br/>                                                                                                                         |
| [**Win32\_DependentService**](win32-dependentservice.md)                                   | Association class<br/> Relates two interdependent base services.<br/>                                                                                                  |
| [**Win32\_LoadOrderGroup**](win32-loadordergroup.md)                                       | Instance class<br/> Represents a group of system services that define execution dependencies.<br/>                                                                     |
| [**Win32\_LoadOrderGroupServiceDependencies**](win32-loadordergroupservicedependencies.md) | Instance class<br/> Represents an association between a base service and a load order group that the service depends on to start running.<br/>                         |
| [**Win32\_LoadOrderGroupServiceMembers**](win32-loadordergroupservicemembers.md)           | Association class<br/> Relates a load order group and a base service.<br/>                                                                                             |
| [**Win32\_OperatingSystem**](win32-operatingsystem.md)                                     | Instance class<br/> Represents an operating system installed on a computer system running Windows.<br/>                                                                |
| [**Win32\_OperatingSystemQFE**](win32-operatingsystemqfe.md)                               | Association class<br/> Relates an operating system and product updates applied as represented in [**Win32\_QuickFixEngineering**](win32-quickfixengineering.md).<br/> |
| [**Win32\_OSRecoveryConfiguration**](win32-osrecoveryconfiguration.md)                     | Instance class<br/> Represents the types of information that will be gathered from memory when the operating system fails.<br/>                                        |
| [**Win32\_QuickFixEngineering**](win32-quickfixengineering.md)                             | Instance class<br/> Represents system-wide Quick Fix Engineering (QFE) or updates that have been applied to the current operating system.<br/>                         |
| [**Win32\_StartupCommand**](win32-startupcommand.md)                                       | Instance class<br/> Represents a command that runs automatically when a user logs onto the computer system.<br/>                                                       |
| [**Win32\_SystemBootConfiguration**](win32-systembootconfiguration.md)                     | Association class<br/> Relates a computer system and its boot configuration.<br/>                                                                                      |
| [**Win32\_SystemDesktop**](win32-systemdesktop.md)                                         | Association class<br/> Relates a computer system and its desktop configuration.<br/>                                                                                   |
| [**Win32\_SystemDevices**](win32-systemdevices.md)                                         | Association class<br/> Relates a computer system and a logical device installed on that system.<br/>                                                                   |
| [**Win32\_SystemLoadOrderGroups**](win32-systemloadordergroups.md)                         | Association class<br/> Relates a computer system and a load order group.<br/>                                                                                          |
| [**Win32\_SystemNetworkConnections**](win32-systemnetworkconnections.md)                   | Association class<br/> Relates a network connection and the computer system on which it resides.<br/>                                                                  |
| [**Win32\_SystemOperatingSystem**](win32-systemoperatingsystem.md)                         | Association class<br/> Relates a computer system and its operating system.<br/>                                                                                        |
| [**Win32\_SystemProcesses**](win32-systemprocesses.md)                                     | Association class <br/> Relates a computer system and a process running on that system.<br/>                                                                           |
| [**Win32\_SystemProgramGroups**](win32-systemprogramgroups.md)                             | Association class<br/> Relates a computer system and a logical program group.<br/>                                                                                     |
| [**Win32\_SystemResources**](win32-systemresources.md)                                     | Association class<br/> Relates a system resource and the computer system it resides on.<br/>                                                                           |
| [**Win32\_SystemServices**](win32-systemservices.md)                                       | Association class<br/> Relates a computer system and a service program that exists on the system.<br/>                                                                 |
| [**Win32\_SystemSetting**](win32-systemsetting.md)                                         | Association class<br/> Relates a computer system and a general setting on that system.<br/>                                                                            |
| [**Win32\_SystemSystemDriver**](win32-systemsystemdriver.md)                               | Association class<br/> Relates a computer system and a system driver running on that computer system.<br/>                                                             |
| [**Win32\_SystemTimeZone**](win32-systemtimezone.md)                                       | Association class<br/> Relates a computer system and a time zone.<br/>                                                                                                 |
| [**Win32\_SystemUsers**](win32-systemusers.md)                                             | Association class<br/> Relates a computer system and a user account on that system.<br/>                                                                               |



 

## Processes

The Processes subcategory groups classes that represent system processes and threads.



| Class                                                 | Description                                                                                                     |
|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| [**Win32\_Process**](win32-process.md)               | Instance class<br/> Represents a sequence of events on a computer system running Windows.<br/>      |
| [**Win32\_ProcessStartup**](win32-processstartup.md) | Instance class<br/> Represents the startup configuration of a computer system running Windows.<br/> |
| [**Win32\_Thread**](win32-thread.md)                 | Instance class<br/> Represents a thread of execution.<br/>                                          |



 

## Registry

The class in the Registry subcategory represents the contents of the Windows registry.



| Class                                     | Description                                                                                               |
|-------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [**Win32\_Registry**](win32-registry.md) | Instance class<br/> Represents the system registry on a computer system running Windows.<br/> |



 

## Scheduler Jobs

The Scheduler Jobs subcategory groups classes that represent scheduled job settings.



| Class                                                | Description                                                                                                                                                                                                                                                           |
|------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Win32\_CurrentTime**](/previous-versions/windows/desktop/wmitimepprov/win32-currenttime) | Abstract class<br/> Represents an instance in time as component seconds, minutes, day of the week, and so on.<br/>                                                                                                                                        |
| [**Win32\_ScheduledJob**](win32-scheduledjob.md)    | Instance class<br/> Represents a job scheduled using the Windows schedule service.<br/>                                                                                                                                                                   |
| [**Win32\_LocalTime**](/previous-versions/windows/desktop/wmitimepprov/win32-localtime)     | Instance class<br/> Represents a point in time returned as [**Win32\_LocalTime**](/previous-versions/windows/desktop/wmitimepprov/win32-localtime) objects that result from a query. The **Hour** property is returned as the local time in a 24-hour clock.<br/>                                |
| [**Win32\_UTCTime**](/previous-versions/windows/desktop/wmitimepprov/win32-utctime)         | Instance class<br/> Represents a point in time that is returned as [**Win32\_UTCTime**](/previous-versions/windows/desktop/wmitimepprov/win32-utctime) objects that result from a query. The **Hour** property is returned as the coordinated universal time (UTC) time in a 24 hour clock.<br/> |



 

## Security

The Security subcategory groups classes that represent system security settings.



| Class                                                                               | Description                                                                                                                                                  |
|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Win32\_AccountSID**](/previous-versions/windows/desktop/secrcw32prov/win32-accountsid)                                       | Association class<br/> Relates a security account instance with a security descriptor instance.<br/>                                             |
| [**Win32\_ACE**](/previous-versions/windows/desktop/secrcw32prov/win32-ace)                                                     | Instance class<br/> Represents an access control entry (ACE).<br/>                                                                               |
| [**Win32\_LogicalFileAccess**](/previous-versions/windows/desktop/secrcw32prov/win32-logicalfileaccess)                         | Association class<br/> Relates the security settings of a file or directory and one member of its discretionary access control list (DACL).<br/> |
| [**Win32\_LogicalFileAuditing**](/previous-versions/windows/desktop/secrcw32prov/win32-logicalfileauditing)                     | Association class<br/> Relates the security settings of a file or directory one member of its system access control list (SACL).<br/>            |
| [**Win32\_LogicalFileGroup**](/previous-versions/windows/desktop/secrcw32prov/win32-logicalfilegroup)                           | Association class<br/> Relates the security settings of a file or directory and its group.<br/>                                                  |
| [**Win32\_LogicalFileOwner**](/previous-versions/windows/desktop/secrcw32prov/win32-logicalfileowner)                           | Association class<br/> Relates the security settings of a file or directory and its owner.<br/>                                                  |
| [**Win32\_LogicalFileSecuritySetting**](/previous-versions/windows/desktop/secrcw32prov/win32-logicalfilesecuritysetting)       | Instance class<br/> Represents security settings for a logical file.<br/>                                                                        |
| [**Win32\_LogicalShareAccess**](/previous-versions/windows/desktop/secrcw32prov/win32-logicalshareaccess)                       | Association class<br/> Relates the security settings of a share and one member of its DACL.<br/>                                                 |
| [**Win32\_LogicalShareAuditing**](/previous-versions/windows/desktop/secrcw32prov/win32-logicalshareauditing)                   | Association class<br/> Relates the security settings of a share and one member of its SACL.<br/>                                                 |
| [**Win32\_LogicalShareSecuritySetting**](/previous-versions/windows/desktop/secrcw32prov/win32-logicalsharesecuritysetting)     | Instance class<br/> Represents security settings for a logical file.<br/>                                                                        |
| [**Win32\_PrivilegesStatus**](win32-privilegesstatus.md)                           | Instance class<br/> Represents information about the privileges required to complete an operation.<br/>                                          |
| [**Win32\_SecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptor)                       | Instance class<br/> Represents a structural representation of a [**SECURITY\_DESCRIPTOR**](/windows/desktop/api/winnt/ns-winnt-security_descriptor).<br/>                   |
| [**Win32\_SecuritySetting**](/previous-versions/windows/desktop/secrcw32prov/win32-securitysetting)                             | Instance class<br/> Represents security settings for a managed element.<br/>                                                                     |
| [**Win32\_SecuritySettingAccess**](/previous-versions/windows/desktop/secrcw32prov/win32-securitysettingaccess)                 | Instance class<br/> Represents the rights granted and denied to a trustee for a given object.<br/>                                               |
| [**Win32\_SecuritySettingAuditing**](/previous-versions/windows/desktop/secrcw32prov/win32-securitysettingauditing)             | Instance class<br/> Represents the auditing for a given trustee on a given object.<br/>                                                          |
| [**Win32\_SecuritySettingGroup**](/previous-versions/windows/desktop/secrcw32prov/win32-securitysettinggroup)                   | Association class<br/> Relates the security of an object and its group.<br/>                                                                     |
| [**Win32\_SecuritySettingOfLogicalFile**](/previous-versions/windows/desktop/secrcw32prov/win32-securitysettingoflogicalfile)   | Instance class<br/> Represents security settings of a file or directory object.<br/>                                                             |
| [**Win32\_SecuritySettingOfLogicalShare**](/previous-versions/windows/desktop/secrcw32prov/win32-securitysettingoflogicalshare) | Instance class<br/> Represents security settings of a shared object.<br/>                                                                        |
| [**Win32\_SecuritySettingOfObject**](/previous-versions/windows/desktop/secrcw32prov/win32-securitysettingofobject)             | Association class<br/> Relates an object to its security settings.<br/>                                                                          |
| [**Win32\_SecuritySettingOwner**](/previous-versions/windows/desktop/secrcw32prov/win32-securitysettingowner)                   | Association class<br/> Relates the security settings of an object and its owner.<br/>                                                            |
| [**Win32\_SID**](/previous-versions/windows/desktop/secrcw32prov/win32-sid)                                                     | Instance class<br/> Represents an arbitrary SID.<br/>                                                                                            |
| [**Win32\_Trustee**](/previous-versions/windows/desktop/secrcw32prov/win32-trustee)                                             | Instance class<br/> Represents a trustee.<br/>                                                                                                   |



 

## Services

The Services subcategory groups classes that represent services and base services.



| Class                                           | Description                                                                                                                                             |
|-------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Win32\_BaseService**](win32-baseservice.md) | Instance class<br/> Represents executable objects that are installed in a registry database maintained by the Service Control Manager.<br/> |
| [**Win32\_Service**](win32-service.md)         | Instance class<br/> Represents a service on a computer system running Windows.<br/>                                                         |



 

## Shares

The Shares subcategory groups classes that represent details of shared resources, such as printers and folders.



| Class                                                       | Description                                                                                                                                                                                          |
|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Win32\_DFSNode**](/previous-versions/windows/desktop/wmipdfs/win32-dfsnode)                     | Association class<br/> Represents a root or junction node of a domain-based or stand-alone distributed file system (DFS).<br/>                                                           |
| [**Win32\_DFSNodeTarget**](/previous-versions/windows/desktop/wmipdfs/win32-dfsnodetarget)         | Association class<br/> Represents the relationship of a DFS node to one of its targets.<br/>                                                                                             |
| [**Win32\_DFSTarget**](/previous-versions/windows/desktop/wmipdfs/win32-dfstarget)                 | Association class<br/> Represents the target of a DFS node.<br/>                                                                                                                         |
| [**Win32\_ServerConnection**](/previous-versions/windows/desktop/wmipsess/win32-serverconnection)   | Instance class<br/> Represents the connections made from a remote computer to a shared resource on the local computer.<br/>                                                              |
| [**Win32\_ServerSession**](/previous-versions/windows/desktop/wmipsess/win32-serversession)         | Instance class<br/> Represents the sessions that are established with the local computer by users on a remote computer.<br/>                                                             |
| [**Win32\_ConnectionShare**](/previous-versions/windows/desktop/wmipsess/win32-connectionshare)     | Association class<br/> Relates a shared resource on the computer and the connection made to the shared resource.<br/>                                                                    |
| [**Win32\_PrinterShare**](win32-printershare.md)           | Association class<br/> Relates a local printer and the share that represents it as it is viewed over a network.<br/>                                                                     |
| [**Win32\_SessionConnection**](/previous-versions/windows/desktop/wmipsess/win32-sessionconnection) | Association class<br/> Represents an association between a session established with the local server by a user on a remote machine, and the connections that depend on the session.<br/> |
| [**Win32\_SessionProcess**](win32-sessionprocess.md)       | Association class<br/> Represents an association between a logon session and the processes associated with that session.<br/>                                                            |
| [**Win32\_ShareToDirectory**](win32-sharetodirectory.md)   | Association class<br/> Relates a shared resource on the computer system and the directory to which it is mapped.<br/>                                                                    |
| [**Win32\_Share**](win32-share.md)                         | Instance class<br/> Represents a shared resource on a computer system running Windows.<br/>                                                                                              |



 

## Start Menu

The Start Menu subcategory groups classes that represent program groups.



| Class                                                                                   | Description                                                                                                                                                              |
|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Win32\_LogicalProgramGroup**](win32-logicalprogramgroup.md)                         | Instance class<br/> Represents a program group in a computer system running Windows.<br/>                                                                    |
| [**Win32\_LogicalProgramGroupDirectory**](win32-logicalprogramgroupdirectory.md)       | Association class<br/> Relates logical program groups (groupings in the Start menu), and the file directories in which they are stored.<br/>                 |
| [**Win32\_LogicalProgramGroupItem**](win32-logicalprogramgroupitem.md)                 | Instance class<br/> Represents an element contained by a **Win32\_ProgramGroup** instance, that is not itself another **Win32\_ProgramGroup** instance.<br/> |
| [**Win32\_LogicalProgramGroupItemDataFile**](win32-logicalprogramgroupitemdatafile.md) | Association class<br/> Relates the program group items of the Start menu, and the files in which they are stored.<br/>                                       |
| [**Win32\_ProgramGroupContents**](win32-programgroupcontents.md)                       | Association class<br/> Relates a program group order and an individual program group or item contained in it.<br/>                                           |
| [**Win32\_ProgramGroupOrItem**](win32-programgrouporitem.md)                           | Instance class<br/> Represents a logical grouping of programs on the user's **Start**\|**Programs** menu.<br/>                                               |



 

## Storage

The Users subcategory groups classes that represent storage information.



| Class                                                                   | Description                                                                                                                                  |
|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| [**Win32\_ShadowBy**](/previous-versions/windows/desktop/vsswmi/win32-shadowby)                               | Association class<br/> Represents the association between a shadow copy and the provider that creates the shadow copy.<br/>      |
| [**Win32\_ShadowContext**](/previous-versions/windows/desktop/vsswmi/win32-shadowcontext)                     | Association class<br/> Specifies how a shadow copy is to be created, queried, or deleted.<br/>                                   |
| [**Win32\_ShadowCopy**](/previous-versions/windows/desktop/legacy/aa394428(v=vs.85))                           | Instance class<br/> Represents a duplicate copy of the original volume at a previous time.<br/>                                  |
| [**Win32\_ShadowDiffVolumeSupport**](/previous-versions/windows/desktop/vsswmi/win32-shadowdiffvolumesupport) | Association class<br/> Represents an association between a shadow copy provider and a storage volume.<br/>                       |
| [**Win32\_ShadowFor**](/previous-versions/windows/desktop/vsswmi/win32-shadowfor)                             | Association class<br/> Represents an association between a shadow copy and the volume for which the shadow copy is created.<br/> |
| [**Win32\_ShadowOn**](/previous-versions/windows/desktop/vsswmi/win32-shadowon)                               | Association class<br/> Represents an association between a shadow copy and where the differential data is written.<br/>          |
| [**Win32\_ShadowProvider**](/previous-versions/windows/desktop/vsswmi/win32-shadowprovider)                   | Association class<br/> Represents a component that creates and represents volume shadow copies.<br/>                             |
| [**Win32\_ShadowStorage**](/previous-versions/windows/desktop/legacy/aa394433(v=vs.85))                     | Association class<br/> Represents an association between a shadow copy and where the differential data is written.<br/>          |
| [**Win32\_ShadowVolumeSupport**](/previous-versions/windows/desktop/vsswmi/win32-shadowvolumesupport)         | Association class<br/> Represents an association between a shadow copy provider with a supported volume.<br/>                    |
| [**Win32\_Volume**](/previous-versions/windows/desktop/legacy/aa394515(v=vs.85))                                   | Instance class<br/> Represents an area of storage on a hard disk.<br/>                                                           |
| [**Win32\_VolumeUserQuota**](/previous-versions/windows/desktop/vdswmi/win32-volumeuserquota)                 | Association class<br/> Represents a volume to the per volume quota settings.<br/>                                                |



 

## Users

The Users subcategory groups classes that represent user account information, such as group membership details.



| Class                                                                 | Description                                                                                                                                      |
|-----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Win32\_Account**](win32-account.md)                               | Instance class<br/> Represents information about user accounts and group accounts known to the computer system running Windows.<br/> |
| [**Win32\_Group**](win32-group.md)                                   | Instance class<br/> Represents data about a group account.<br/>                                                                      |
| [**Win32\_GroupInDomain**](/previous-versions/windows/desktop/cimwin32a/win32-groupindomain)                   | Association class<br/> Identifies the group accounts associated with a Windows NT domain.<br/>                                       |
| [**Win32\_GroupUser**](win32-groupuser.md)                           | Association class<br/> Relates a group and an account that is a member of that group.<br/>                                           |
| [**Win32\_LogonSession**](win32-logonsession.md)                     | Instance class<br/> Describes the logon session or sessions associated with a user logged on to Windows.<br/>                        |
| [**Win32\_LogonSessionMappedDisk**](/windows/desktop/CIMWin32Prov/win32-logonsessionmappeddisk) | Instance class<br/> Represents the mapped logical disks associated with the session.<br/>                                            |
| [**Win32\_NetworkLoginProfile**](win32-networkloginprofile.md)       | Instance class<br/> Represents the network login information of a specific user on a computer system running Windows.<br/>           |
| [**Win32\_SystemAccount**](win32-systemaccount.md)                   | Instance class<br/> Represents a system account.<br/>                                                                                |
| [**Win32\_UserAccount**](win32-useraccount.md)                       | Instance class<br/> Represents information about a user account on a computer system running Windows.<br/>                           |
| [**Win32\_UserInDomain**](/previous-versions/windows/desktop/cimwin32a/win32-userindomain)                     | Association class<br/> Relates a user account and a Windows NT domain.<br/>                                                          |



 

## Windows Event Log

The Windows Event Log subcategory groups classes that represent events, event log entries, event log configuration settings, and so on.



| Class                                                         | Description                                                                                                                                                                   |
|---------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Win32\_NTEventlogFile**](/previous-versions/windows/desktop/legacy/aa394225(v=vs.85))         | Instance class<br/> Represents data stored in a Windows Event log file.<br/>                                                                                      |
| [**Win32\_NTLogEvent**](/previous-versions/windows/desktop/eventlogprov/win32-ntlogevent)                 | Instance class<br/> Represents Windows events.<br/>                                                                                                               |
| [**Win32\_NTLogEventComputer**](/previous-versions/windows/desktop/eventlogprov/win32-ntlogeventcomputer) | Association class<br/> Relates instances of [**Win32\_NTLogEvent**](/previous-versions/windows/desktop/eventlogprov/win32-ntlogevent) and [**Win32\_ComputerSystem**](win32-computersystem.md).<br/>         |
| [**Win32\_NTLogEventLog**](/previous-versions/windows/desktop/eventlogprov/win32-ntlogeventlog)           | Association class<br/> Relates instances of [**Win32\_NTLogEvent**](/previous-versions/windows/desktop/eventlogprov/win32-ntlogevent) and [**Win32\_NTEventlogFile**](/previous-versions/windows/desktop/legacy/aa394225(v=vs.85)) classes.<br/> |
| [**Win32\_NTLogEventUser**](/previous-versions/windows/desktop/eventlogprov/win32-ntlogeventuser)         | Association class<br/> Relates instances of [**Win32\_NTLogEvent**](/previous-versions/windows/desktop/eventlogprov/win32-ntlogevent) and [**Win32\_UserAccount**](win32-useraccount.md).<br/>               |



 

## Windows Product Activation

Windows Product Activation (WPA) is an antipiracy technology to reduce the casual copying of software.



| Class                                                                                                               | Description                                                                                                                                                                                       |
|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Win32\_ComputerSystemWindowsProductActivationSetting**](/previous-versions/windows/desktop/licwmiprov/win32-computersystemwindowsproductactivationsetting) | Association class<br/> Relates instances of [**Win32\_ComputerSystem**](win32-computersystem.md) and [**Win32\_WindowsProductActivation**](/previous-versions/windows/desktop/legacy/aa394520(v=vs.85)).<br/> |
| [**Win32\_Proxy**](/previous-versions/windows/desktop/legacy/aa394389(v=vs.85))                                                                                 | Instance class<br/> Contains properties and methods to query and configure an Internet connection related to WPA.<br/>                                                                |
| [**Win32\_WindowsProductActivation**](/previous-versions/windows/desktop/legacy/aa394520(v=vs.85))                                           | Instance class<br/> Contains properties and methods related to WPA.<br/>                                                                                                              |



 

## Related topics

<dl> <dt>

[Win32 Classes](/previous-versions//aa394084(v=vs.85))
</dt> </dl>

 


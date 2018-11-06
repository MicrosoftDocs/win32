---
Description: Starting with Windows Vista, WMI contains many new features based upon requests by WMI users.
ms.assetid: 604a86d2-9a8e-4266-93b8-13676f768b29
ms.tgt_platform: multiple
title: Whats New in Windows Vista
ms.topic: article
ms.date: 05/31/2018
---

# What's New in Windows Vista

Starting with Windows Vista, WMI contains many new features based upon requests by WMI users.

-   [New Troubleshooting Tool](#new-troubleshooting-tool)
-   [New Security Features in Windows Vista](#new-security-features-in-windows-vista)
-   [Other New Features in Windows Vista](#other-new-features-in-windows-vista)
-   [Related topics](#related-topics)

## New Troubleshooting Tool

A new troubleshooting tool is available for download.

<dl> <dt>

<span id="WMI_Diagnosis_Utility"></span><span id="wmi_diagnosis_utility"></span><span id="WMI_DIAGNOSIS_UTILITY"></span>WMI Diagnosis Utility
</dt> <dd>

This utility examines the current state of the WMI service and related components, DCOM settings, and registry settings on the local computer. The utility reports problems and offers suggestions for repair. For more information and to download the utility, see [WMI Diagnosis Utility](Http://go.microsoft.com/fwlink/p/?linkid=84435).

</dd> </dl>

## New Security Features in Windows Vista

The following list lists the new WMI security features that are available in Windows Vista.

<dl> <dt>

<span id="Tracing_and_logging_events"></span><span id="tracing_and_logging_events"></span><span id="TRACING_AND_LOGGING_EVENTS"></span>Tracing and logging events
</dt> <dd>

WMI service no longer uses most of the [WMI Log Files](wmi-log-files.md). Instead it uses [Event Tracing](https://msdn.microsoft.com/library/windows/desktop/bb968803) (ETW) and events are available through the **Event Viewer** UI or the Wevtutil command line tool. For more information, see [Tracing WMI Activity](tracing-wmi-activity.md).

</dd> <dt>

<span id="Setting_WMI_namespace_security_in_the_MOF_file"></span><span id="setting_wmi_namespace_security_in_the_mof_file"></span><span id="SETTING_WMI_NAMESPACE_SECURITY_IN_THE_MOF_FILE"></span>Setting WMI namespace security in the MOF file
</dt> <dd>

The **NamespaceSecuritySDDL** qualifier can be used to secure any namespace. For more information, see [Setting Namespace Security When the Namespace is Created](setting-namespace-security-when-the-namespace-is-created.md).

</dd> <dt>

<span id="Security_Auditing_of_WMI_namespaces"></span><span id="security_auditing_of_wmi_namespaces"></span><span id="SECURITY_AUDITING_OF_WMI_NAMESPACES"></span>Security Auditing of WMI namespaces
</dt> <dd>

WMI uses the namespace system access control lists (SACL) to audit namespace activity and report events to the Security event log. For more information, see [Access to WMI Namespaces](access-to-wmi-namespaces.md) and [Setting Namespace Security Descriptors](setting-namespace-security-descriptors.md).

</dd> <dt>

<span id="Get_and_Set_security_descriptor_methods_for_securable_objects"></span><span id="get_and_set_security_descriptor_methods_for_securable_objects"></span><span id="GET_AND_SET_SECURITY_DESCRIPTOR_METHODS_FOR_SECURABLE_OBJECTS"></span>Get and Set security descriptor methods for securable objects
</dt> <dd>

New scriptable methods to get and set security descriptors have been added to [**Win32\_Printer**](https://msdn.microsoft.com/library/aa394363), [**Win32\_Service**](https://msdn.microsoft.com/library/aa394418), [**StdRegProv**](https://msdn.microsoft.com/library/aa393664), [**Win32\_DCOMApplicationSetting**](https://msdn.microsoft.com/library/aa394118), and [**\_\_SystemSecurity**](--systemsecurity.md). For more information, see [Changing Access Security on Securable Objects](changing-access-security-on-securable-objects.md).

</dd> <dt>

<span id="Manipulate_Security_Descriptors_in_scripts"></span><span id="manipulate_security_descriptors_in_scripts"></span><span id="MANIPULATE_SECURITY_DESCRIPTORS_IN_SCRIPTS"></span>Manipulate Security Descriptors in scripts
</dt> <dd>

The [**Win32\_SecurityDescriptorHelper**](https://msdn.microsoft.com/library/aa394403) class has methods that allow scripts to convert binary security descriptors on securable objects to [**Win32\_SecurityDescriptor**](https://msdn.microsoft.com/library/aa394402) objects or [Security Descriptor Definition Language](https://msdn.microsoft.com/library/windows/desktop/aa379567) strings. For more information, see [Changing Access Security on Securable Objects](changing-access-security-on-securable-objects.md).

</dd> <dt>

<span id="User_Account_Control"></span><span id="user_account_control"></span><span id="USER_ACCOUNT_CONTROL"></span>User Account Control
</dt> <dd>

User Account Control (UAC) affects what WMI data is returned, remote access, and how scripts must be run. For more information, see [User Account Control and WMI](user-account-control-and-wmi.md). For more information about UAC, see [Getting Started with User Account Control on Windows Vista](Http://go.microsoft.com/fwlink/p/?linkid=84438).

</dd> </dl>

## Other New Features in Windows Vista

The following list lists new WMI features that are available in Windows Vista.

<dl> <dt>

<span id="New_performance_counter_data_providers"></span><span id="new_performance_counter_data_providers"></span><span id="NEW_PERFORMANCE_COUNTER_DATA_PROVIDERS"></span>New performance counter data providers
</dt> <dd>

The AutoDiscovery/AutoPurge (ADAP) process no longer transfers performance counter objects into WMI performance classes in the WMI repository. For more information, see [Performance Libraries and WMI](performance-libraries-and-wmi.md). The [WMIPerfClass Provider](wmiperfclass-provider.md) creates the WMI Performance Counter Classes. Data is dynamically supplied to these WMI performance classes by the [WMIPerfInst Provider](wmiperfinst-provider.md).

</dd> <dt>

<span id="Indexer_for_collections"></span><span id="indexer_for_collections"></span><span id="INDEXER_FOR_COLLECTIONS"></span>Indexer for collections
</dt> <dd>

The [**SWbemObject.ItemIndex**](swbemobjectset-itemindex.md) method returns the object associated with a specified index into a collection.

</dd> <dt>

<span id="Support_for_IPv6_and_IPv4"></span><span id="support_for_ipv6_and_ipv4"></span><span id="SUPPORT_FOR_IPV6_AND_IPV4"></span>Support for IPv6 and IPv4
</dt> <dd>

WMI [IP Route Provider](https://msdn.microsoft.com/library/aa391405) and network classes supply data for IPv4 addresses. Starting with Windows Vista, WMI also provides limited support for IPv6 network capabilities. For more information, see [IPv6 and IPv4 Support in WMI](ipv6-and-ipv4-support-in-wmi.md).

</dd> <dt>

<span id="Changes_to_remote_connections"></span><span id="changes_to_remote_connections"></span><span id="CHANGES_TO_REMOTE_CONNECTIONS"></span>Changes to remote connections
</dt> <dd>

Connecting to a WMI namespace on a remote computer running Windows Vista may require changes to settings for [Windows Firewall](Http://go.microsoft.com/fwlink/p/?linkid=84428), [User Account Control](Http://go.microsoft.com/fwlink/p/?linkid=84439), or DCOM. For more information, see [Connecting to WMI Remotely Starting with Vista](connecting-to-wmi-remotely-starting-with-vista.md).

</dd> <dt>

<span id="Changes_to_________Win32_QuickFixEngineering"></span><span id="changes_to_________win32_quickfixengineering"></span><span id="CHANGES_TO_________WIN32_QUICKFIXENGINEERING"></span>Changes to [**Win32\_QuickFixEngineering**](https://msdn.microsoft.com/library/aa394391)
</dt> <dd>

For systems running on the Windows Vista and later operating system, this class returns only the updates supplied by Component Based Servicing (CBS). These updates are not listed in the registry. Updates supplied by Windows Installer (MSI) or the [Windows Update](http://go.microsoft.com/fwlink/p/?linkid=33483) are not returned by [**Win32\_QuickFixEngineering**](https://msdn.microsoft.com/library/aa394391).

</dd> <dt>

<span id="Enabling_and_disabling_a_NIC"></span><span id="enabling_and_disabling_a_nic"></span><span id="ENABLING_AND_DISABLING_A_NIC"></span>Enabling and disabling a NIC
</dt> <dd>

[**Win32\_NetworkAdapter**](https://msdn.microsoft.com/library/aa394216) has new methods to enable and disable the network adapter.

</dd> <dt>

<span id="Windows_Installer_Provider_changes"></span><span id="windows_installer_provider_changes"></span><span id="WINDOWS_INSTALLER_PROVIDER_CHANGES"></span>Windows Installer Provider changes
</dt> <dd>

[**Win32\_Product**](https://msdn.microsoft.com/library/aa394378) has new properties and methods to provide more data about the product.

</dd> <dt>

<span id="New_display_monitor_classes"></span><span id="new_display_monitor_classes"></span><span id="NEW_DISPLAY_MONITOR_CLASSES"></span>New display monitor classes
</dt> <dd>

[Monitor Display Classes](https://msdn.microsoft.com/library/windows/desktop/dn622981) contain data supplied by the [WDM Provider](https://msdn.microsoft.com/library/windows/desktop/aa394052) that provides data about display monitors.

</dd> <dt>

<span id="Intelligent_Platform_Management_Interface_provider"></span><span id="intelligent_platform_management_interface_provider"></span><span id="INTELLIGENT_PLATFORM_MANAGEMENT_INTERFACE_PROVIDER"></span>Intelligent Platform Management Interface provider
</dt> <dd>

The WMI [IPMI Provider](https://msdn.microsoft.com/library/aa391402) supplies data from baseboard management controller (BMC) operations to the operating system. The provider supplies information to the Intelligent Platform Management Information Classes, which provide sensors data and BMC System Event Log (SEL) message data.

</dd> <dt>

<span id="Detecting_hyperthreading_and_multicore_processors"></span><span id="detecting_hyperthreading_and_multicore_processors"></span><span id="DETECTING_HYPERTHREADING_AND_MULTICORE_PROCESSORS"></span>Detecting hyperthreading and multicore processors
</dt> <dd>

[**Win32\_ComputerSystem**](https://msdn.microsoft.com/library/aa394102) and [**Win32\_Processor**](https://msdn.microsoft.com/library/aa394373) have new properties that enable you to write scripts to determine whether the computer system has multicore or hyperthreading processors.

</dd> <dt>

<span id="Event_messages"></span><span id="event_messages"></span><span id="EVENT_MESSAGES"></span>Event messages
</dt> <dd>

Windows Vista has new event messages. For more information, see [WMI Events](wmi-events.md).

</dd> <dt>

<span id="Inventory_improvements"></span><span id="inventory_improvements"></span><span id="INVENTORY_IMPROVEMENTS"></span>Inventory improvements
</dt> <dd>

Many hardware classes have had changes to improve hardware inventory. For example, a serial number property was added to [**Win32\_CDROMDrive**](https://msdn.microsoft.com/library/aa394081) and [**Win32\_DiskDrive**](https://msdn.microsoft.com/library/aa394132).

</dd> <dt>

<span id="New_provider_hosting_models"></span><span id="new_provider_hosting_models"></span><span id="NEW_PROVIDER_HOSTING_MODELS"></span>New provider hosting models
</dt> <dd>

New provider hosting models have been added for Windows Vista. For more information, see [Provider Hosting and Security](provider-hosting-and-security.md).

</dd> </dl>

## Related topics

<dl> <dt>

[About WMI](about-wmi.md)
</dt> </dl>

 

 




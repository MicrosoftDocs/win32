---
Description: 'Windows Management Infrastructure (WMI), Management Instrumentation (MI) and Open Management Infrastructure (OMI) all use Management Object Format (MOF) files to describe the information made available through their respective providers.'
ms.assetid: '5ec3c6a2-df23-446d-a4da-b8e207eeb6f6'
title: 'WMI/MI/OMI Providers'
---

# WMI/MI/OMI Providers

Windows Management Infrastructure (WMI), Management Instrumentation (MI) and Open Management Infrastructure (OMI) all use Management Object Format (MOF) files to describe the information made available through their respective providers.

<dl> <dt>

<span id="Active_Directory"></span><span id="active_directory"></span><span id="ACTIVE_DIRECTORY"></span>[Active Directory](https://msdn.microsoft.com/library/aa384753)
</dt> <dd>

The Active Directory provider, also known as the Directory Services (DS) provider, maps Active Directory objects to WMI. By accessing the Lightweight Directory Access Protocol (LDAP) namespace in WMI, you can reference or make an object an alias in the Active Directory.

</dd> <dt>

<span id="Application_Inventory"></span><span id="application_inventory"></span><span id="APPLICATION_INVENTORY"></span>[Application Inventory](https://msdn.microsoft.com/library/dn894019)
</dt> <dd>

The WMI classes for Application Inventory enable discovery of the installed Win32 applications and Windows store applications on a Windows system.

</dd> <dt>

<span id="Application_Proxy"></span><span id="application_proxy"></span><span id="APPLICATION_PROXY"></span>[Application Proxy](https://msdn.microsoft.com/library/dn765511)
</dt> <dd>

Application Proxy WMI Provider enables developers to access the Web Application Proxy service so administrators can publish applications for external access. Web Application Proxy is a reverse proxy for Active Directory Federation Services (AD FS).

</dd> <dt>

<span id="BitLocker_Drive_Encryption__BDE_"></span><span id="bitlocker_drive_encryption__bde_"></span><span id="BITLOCKER_DRIVE_ENCRYPTION__BDE_"></span>[BitLocker Drive Encryption (BDE)](https://msdn.microsoft.com/library/windows/desktop/aa376409)
</dt> <dd>

Provides configuration and management for an area of storage on a hard disk drive, represented by an instance of [**Win32\_EncryptableVolume**](https://msdn.microsoft.com/library/windows/desktop/aa376483), that can be protected by using encryption.

</dd> <dt>

<span id="BITS"></span><span id="bits"></span>[BITS](https://msdn.microsoft.com/library/dd904506)
</dt> <dd>

The Background Intelligent Transfer Service (BITS) Compact Server with BITS Remote Management allows authenticated administrators or controller applications to create, modify and manage BITS transfer jobs remotely without using the Internet Information Services (IIS) service.

</dd> <dt>

<span id="BizTalk"></span><span id="biztalk"></span><span id="BIZTALK"></span>[BizTalk](Http://go.microsoft.com/fwlink/p/?linkid=84305)
</dt> <dd>

Supplies access to the BizTalk administration objects represented by WMI classes.

</dd> <dt>

<span id="Boot_Configuration_Data"></span><span id="boot_configuration_data"></span><span id="BOOT_CONFIGURATION_DATA"></span>[Boot Configuration Data](https://msdn.microsoft.com/library/windows/desktop/bb986746)
</dt> <dd>

The Boot Configuration Data (BCD) provider provides a store that is used to describe boot applications and boot application settings.

</dd> <dt>

<span id="Boot_Event_Collector"></span><span id="boot_event_collector"></span><span id="BOOT_EVENT_COLLECTOR"></span>[Boot Event Collector](https://msdn.microsoft.com/library/mt164560)
</dt> <dd>

The Boot Event Collector WMI provider provides access to connection and configuration information for the Setup and Boot Event Collection feature on Windows Server.

</dd> <dt>

<span id="CIMWin32__Win32__Power_Management_Events"></span><span id="cimwin32__win32__power_management_events"></span><span id="CIMWIN32__WIN32__POWER_MANAGEMENT_EVENTS"></span>[CIMWin32, Win32, Power Management Events](https://msdn.microsoft.com/library/dn792179)
</dt> <dd>

The CIMWin32 providers support the classes implemented in CimWin32.dll, and consist of the core CIM classes, the Win32 implementation of those classes, and power management events.

</dd> <dt>

<span id="CIMWin32a"></span><span id="cimwin32a"></span><span id="CIMWIN32A"></span>[CIMWin32a](https://msdn.microsoft.com/library/dn605981)
</dt> <dd>

The CIMWin32a provider extends the classes available in the [CIMWin32](https://msdn.microsoft.com/library/dn792179).

</dd> <dt>

<span id="DcbQosCim"></span><span id="dcbqoscim"></span><span id="DCBQOSCIM"></span>[DcbQosCim](https://msdn.microsoft.com/library/hh872258)
</dt> <dd>

The DcbQosCim provider supports classes that describe Network QOS setting data, control setting data, and traffic class setting data.

</dd> <dt>

<span id="Distributed_File_System__DFS_"></span><span id="distributed_file_system__dfs_"></span><span id="DISTRIBUTED_FILE_SYSTEM__DFS_"></span>[Distributed File System (DFS)](https://msdn.microsoft.com/library/aa390360)
</dt> <dd>

The DFS provider supplies scriptable DFS functions through WMI.

</dd> <dt>

<span id="Distributed_File_System_Replication__DFSR_"></span><span id="distributed_file_system_replication__dfsr_"></span><span id="DISTRIBUTED_FILE_SYSTEM_REPLICATION__DFSR_"></span>[Distributed File System Replication (DFSR)](https://msdn.microsoft.com/library/bb540031)
</dt> <dd>

Creates tools for configuring and monitoring the [Distributed File System (DFS)](https://msdn.microsoft.com/library/bb524800) service. For more information, see [DFSR WMI Classes](https://msdn.microsoft.com/library/bb540028).

</dd> <dt>

<span id="Dfsncimprov"></span><span id="dfsncimprov"></span><span id="DFSNCIMPROV"></span>[Dfsncimprov](https://msdn.microsoft.com/library/jj152336)
</dt> <dd>

The [Dfsncimprov](https://msdn.microsoft.com/library/jj152336) provider supports classes that implement DFS namespace access.

</dd> <dt>

<span id="DhcpServerPSProvider"></span><span id="dhcpserverpsprovider"></span><span id="DHCPSERVERPSPROVIDER"></span>[DhcpServerPSProvider](https://msdn.microsoft.com/library/hh832732)
</dt> <dd>

The [DhcpServerPSProvider](https://msdn.microsoft.com/library/hh832732) provider supports classes that interact with a dynamic host configuration protocol (DHCP) server.

</dd> <dt>

<span id="Disk_Quota"></span><span id="disk_quota"></span><span id="DISK_QUOTA"></span>[Disk Quota](https://msdn.microsoft.com/library/aa390365)
</dt> <dd>

The Windows Disk Quota provider allows administrators to control the amount of data that each user stores on an NTFS file system.

</dd> <dt>

<span id="Distributed_Transaction_Coordinator__DTC_"></span><span id="distributed_transaction_coordinator__dtc_"></span><span id="DISTRIBUTED_TRANSACTION_COORDINATOR__DTC_"></span>[Distributed Transaction Coordinator (DTC)](https://msdn.microsoft.com/library/dn948295)
</dt> <dd>

The DTC provider enables management of the DTC.

</dd> <dt>

<span id="DNS"></span><span id="dns"></span>[DNS](https://msdn.microsoft.com/library/windows/desktop/ms682125)
</dt> <dd>

Enables administrators and programmers to configure Domain Name System (DNS) resource records (RRs) and DNS Servers using WMI.

</dd> <dt>

<span id="Dnsclientcim_Provider_Classes"></span><span id="dnsclientcim_provider_classes"></span><span id="DNSCLIENTCIM_PROVIDER_CLASSES"></span>[Dnsclientcim Provider Classes](https://msdn.microsoft.com/library/hh872280)
</dt> <dd>

The Dnsclientcim provider supports classes that interact with a Domain Name System (DNS) client.

</dd> <dt>

<span id="DnsClientPSProvider"></span><span id="dnsclientpsprovider"></span><span id="DNSCLIENTPSPROVIDER"></span>[DnsClientPSProvider](https://msdn.microsoft.com/library/hh832825)
</dt> <dd>

The [DnsClientPSProvider](https://msdn.microsoft.com/library/hh832825) provider supports WMI classes that interact with a DNS client.

</dd> <dt>

<span id="DnsServerPSProvider"></span><span id="dnsserverpsprovider"></span><span id="DNSSERVERPSPROVIDER"></span>[DnsServerPSProvider](https://msdn.microsoft.com/library/hh832826)
</dt> <dd>

The [DnsServerPSProvider](https://msdn.microsoft.com/library/hh832826) provider supports WMI classes that interact with a DNS server.

</dd> <dt>

<span id="Event_Log"></span><span id="event_log"></span><span id="EVENT_LOG"></span>[Event Log](https://msdn.microsoft.com/library/aa390413)
</dt> <dd>

The [Event Log](https://msdn.microsoft.com/library/aa390413) provider supplies access to data from the event log service, and notification of events.

</dd> <dt>

<span id="Event_Tracing_Management"></span><span id="event_tracing_management"></span><span id="EVENT_TRACING_MANAGEMENT"></span>[Event Tracing Management](https://msdn.microsoft.com/library/dn919682)
</dt> <dd>

The Event Tracing Management provider provides access to Event Tracing for Windows (ETW) autologger session configurations and trace events.

</dd> <dt>

<span id="Failover_Cluster-Aware_Updating"></span><span id="failover_cluster-aware_updating"></span><span id="FAILOVER_CLUSTER-AWARE_UPDATING"></span>[Failover Cluster-Aware Updating](https://msdn.microsoft.com/library/mt164586)
</dt> <dd>

The Failover Cluster-Aware Updating (CAU) provider supports coordination with and management of CAU.

</dd> <dt>

<span id="Failover_Clustering_Hyper-V"></span><span id="failover_clustering_hyper-v"></span><span id="FAILOVER_CLUSTERING_HYPER-V"></span>[Failover Clustering Hyper-V](https://msdn.microsoft.com/library/mt167750)
</dt> <dd>

The Failover Clustering Hyper-V provider provides management and reporting of Hyper-V in a clustering environment.

</dd> <dt>

<span id="Failover_Clustering_Storage_QoS"></span><span id="failover_clustering_storage_qos"></span><span id="FAILOVER_CLUSTERING_STORAGE_QOS"></span>[Failover Clustering Storage QoS](https://msdn.microsoft.com/library/mt164590)
</dt> <dd>

The Failover Clustering Storage Quality of Service (QoS) provider provides management and reporting of the clustering storage QoS policies.

</dd> <dt>

<span id="Failover_Cluster_V1_Provider"></span><span id="failover_cluster_v1_provider"></span><span id="FAILOVER_CLUSTER_V1_PROVIDER"></span>[Failover Cluster V1 Provider](https://msdn.microsoft.com/library/mt164664)
</dt> <dd>

The Failover Cluster V1 provider provides management of a failover cluster.

</dd> <dt>

<span id="Failover_Cluster_V1_Extensions"></span><span id="failover_cluster_v1_extensions"></span><span id="FAILOVER_CLUSTER_V1_EXTENSIONS"></span>[Failover Cluster V1 Extensions](https://msdn.microsoft.com/library/mt164601)
</dt> <dd>

The Failover Cluster Extensions provider provides additional management of a failover cluster.

</dd> <dt>

<span id="Gateway_Health_Monitor"></span><span id="gateway_health_monitor"></span><span id="GATEWAY_HEALTH_MONITOR"></span>[Gateway Health Monitor](https://msdn.microsoft.com/library/mt164603)
</dt> <dd>

The Gateway Health Monitor provider manages gateway health monitoring events and information.

</dd> <dt>

<span id="Group_Policy_API"></span><span id="group_policy_api"></span><span id="GROUP_POLICY_API"></span>[Group Policy API](https://msdn.microsoft.com/library/aa374177)
</dt> <dd>

The Group Policy provider enables policy-based administration using Microsoft Active Directory (AD) directory services.

</dd> <dt>

<span id="Host_Guardian_Service"></span><span id="host_guardian_service"></span><span id="HOST_GUARDIAN_SERVICE"></span>[Host Guardian Service](https://msdn.microsoft.com/library/dn958267)
</dt> <dd>

The Host Guardian Service provider provides management of the Host Guardian Service for shielded VMs.

</dd> <dt>

<span id="Hyper-V"></span><span id="hyper-v"></span><span id="HYPER-V"></span>[Hyper-V](https://msdn.microsoft.com/library/cc136992)
</dt> <dd>

The Hyper-V provider allows you to manage and retrieve information about virtual machines.

</dd> <dt>

<span id="Hyper-V__V2_"></span><span id="hyper-v__v2_"></span><span id="HYPER-V__V2_"></span>[Hyper-V (V2)](https://msdn.microsoft.com/library/windows/desktop/hh850319)
</dt> <dd>

The Hyper-V (V2) provider extends the [Hyper-V](https://msdn.microsoft.com/library/cc136992) provider.

</dd> <dt>

<span id="Internet_Information_Services__IIS_"></span><span id="internet_information_services__iis_"></span><span id="INTERNET_INFORMATION_SERVICES__IIS_"></span>[Internet Information Services (IIS)](Http://go.microsoft.com/fwlink/p/?linkid=84317)
</dt> <dd>

Exposes programming interfaces that can be used to query and configure the IIS metabase.

</dd> <dt>

<span id="Internet_Protocol_Address_Management__IPAM__Server"></span><span id="internet_protocol_address_management__ipam__server"></span><span id="INTERNET_PROTOCOL_ADDRESS_MANAGEMENT__IPAM__SERVER"></span>[Internet Protocol Address Management (IPAM) Server](https://msdn.microsoft.com/library/dn765570)
</dt> <dd>

The IPAM Server Provider enables developers to manage IPAM through WMI.

</dd> <dt>

<span id="IP_Route_Provider"></span><span id="ip_route_provider"></span><span id="IP_ROUTE_PROVIDER"></span>[IP Route Provider](https://msdn.microsoft.com/library/aa391405)
</dt> <dd>

The preinstalled IP Route provider supplies IPV4 network routing information, including (but not limited to) the information available through the **route print** command.

</dd> <dt>

<span id="Intelligent_Platform_Management_Interface__IPMI_"></span><span id="intelligent_platform_management_interface__ipmi_"></span><span id="INTELLIGENT_PLATFORM_MANAGEMENT_INTERFACE__IPMI_"></span>[Intelligent Platform Management Interface (IPMI)](https://msdn.microsoft.com/library/aa391402)
</dt> <dd>

Supplies IPMI data from Baseboard Management Controller (BMC) operations.

</dd> <dt>

<span id="iSCSI_Target_Server"></span><span id="iscsi_target_server"></span><span id="ISCSI_TARGET_SERVER"></span>[iSCSI Target Server](https://msdn.microsoft.com/library/hh830439)
</dt> <dd>

The iSCSI Target Server provider supports a WMI interface for managing the Microsoft iSCSI Target Server, such as creating virtual disks, and for presenting them to the client.

</dd> <dt>

<span id="Job_Object"></span><span id="job_object"></span><span id="JOB_OBJECT"></span>[Job Object](https://msdn.microsoft.com/library/aa392151)
</dt> <dd>

The Job Object provider supports access to data about named kernel job objects.

</dd> <dt>

<span id="Kernel_Trace"></span><span id="kernel_trace"></span><span id="KERNEL_TRACE"></span>[Kernel Trace](https://msdn.microsoft.com/library/aa392155)
</dt> <dd>

The preinstalled Kernel Trace event provider allows you to see kernel trace events on Process creation, Process termination, Thread creation, Thread termination and module load.

</dd> <dt>

<span id="Live_Communications_Server_2003"></span><span id="live_communications_server_2003"></span><span id="LIVE_COMMUNICATIONS_SERVER_2003"></span>[Live Communications Server 2003](Http://go.microsoft.com/fwlink/p/?linkid=84360)
</dt> <dd>

Provides classes that create, register, configure, manage custom Session Initiation Protocol (SIP) applications with the [Live Communications Server 2003](Http://go.microsoft.com/fwlink/p/?linkid=84359).

</dd> <dt>

<span id="Management_Tools_Registry"></span><span id="management_tools_registry"></span><span id="MANAGEMENT_TOOLS_REGISTRY"></span>[Management Tools Registry](https://msdn.microsoft.com/library/dn958288)
</dt> <dd>

The Management Tools Registry provider provides remote access to the registry.

</dd> <dt>

<span id="Management_Tools_Task_Manager"></span><span id="management_tools_task_manager"></span><span id="MANAGEMENT_TOOLS_TASK_MANAGER"></span>[Management Tools Task Manager](https://msdn.microsoft.com/library/dn958299)
</dt> <dd>

The Management Tools Task Manager provider provides access and management of the Task Manager data.

</dd> <dt>

<span id="MDM_Application"></span><span id="mdm_application"></span><span id="MDM_APPLICATION"></span>[MDM Application](https://msdn.microsoft.com/library/dn610375)
</dt> <dd>

The Mobile Device Management (MDM) application provider manages applications on devices that are subscribed to the MDM service.

</dd> <dt>

<span id="MDM_Bridge"></span><span id="mdm_bridge"></span><span id="MDM_BRIDGE"></span>[MDM Bridge](https://msdn.microsoft.com/library/windows/desktop/dn905224)
</dt> <dd>

The MDM Bridge provider enables MDM management of a network bridge.

</dd> <dt>

<span id="MDM_Settings"></span><span id="mdm_settings"></span><span id="MDM_SETTINGS"></span>[MDM Settings](https://msdn.microsoft.com/library/dn610402)
</dt> <dd>

The MDM Settings Provider enables management of settings on devices enrolled with a MDM service.

</dd> <dt>

<span id="MSFT_PCSVDevice"></span><span id="msft_pcsvdevice"></span><span id="MSFT_PCSVDEVICE"></span>[MSFT\_PCSVDevice](https://msdn.microsoft.com/library/dn375992)
</dt> <dd>

The [MSFT\_PCSVDevice](https://msdn.microsoft.com/library/dn375992) provider exposes a class that defines a view class for a physical computer system.

</dd> <dt>

<span id="MsNetImPlatform"></span><span id="msnetimplatform"></span><span id="MSNETIMPLATFORM"></span>[MsNetImPlatform](https://msdn.microsoft.com/library/hh873046)
</dt> <dd>

The [MsNetImPlatform](https://msdn.microsoft.com/library/hh873046) provider section provides reference information for MsNetImPlatform provider classes implemented in NdisIMPlatCim.dll.

</dd> <dt>

<span id="NetAdapterCim"></span><span id="netadaptercim"></span><span id="NETADAPTERCIM"></span>[NetAdapterCim](https://msdn.microsoft.com/library/hh872472)
</dt> <dd>

The [NetAdapterCim](https://msdn.microsoft.com/library/hh872472) provider supports classes that access network adapters.

</dd> <dt>

<span id="NetDaCim"></span><span id="netdacim"></span><span id="NETDACIM"></span>[NetDaCim](https://msdn.microsoft.com/library/hh872259)
</dt> <dd>

This section provides reference information for [NetDaCim](https://msdn.microsoft.com/library/hh872259) Provider classes.

</dd> <dt>

<span id="NetNcCim"></span><span id="netnccim"></span><span id="NETNCCIM"></span>[NetNcCim](https://msdn.microsoft.com/library/hh872473)
</dt> <dd>

Provides reference information for [NetNcCim](https://msdn.microsoft.com/library/hh872473) provider classes.

</dd> <dt>

<span id="NetPeerDist"></span><span id="netpeerdist"></span><span id="NETPEERDIST"></span>[NetPeerDist](https://msdn.microsoft.com/library/hh872251)
</dt> <dd>

The [NetPeerDist](https://msdn.microsoft.com/library/hh872251) provider supports classes that interact with the Branch Cache infrastructure.

</dd> <dt>

<span id="NetQosCim"></span><span id="netqoscim"></span><span id="NETQOSCIM"></span>[NetQosCim](https://msdn.microsoft.com/library/hh872475)
</dt> <dd>

The [NetQosCim](https://msdn.microsoft.com/library/hh872475) provider supplies data for network quality of service (QoS) and QoS setting data.

</dd> <dt>

<span id="NetSwitchTeam"></span><span id="netswitchteam"></span><span id="NETSWITCHTEAM"></span>[NetSwitchTeam](https://msdn.microsoft.com/library/jj676899)
</dt> <dd>

This section provides reference information for NetSwitchTeam provider classes declared in NetSwitchTeam.mof and implemented in NetSwitchTeamCim.dll.

</dd> <dt>

<span id="NetTCPIP"></span><span id="nettcpip"></span><span id="NETTCPIP"></span>[NetTCPIP](https://msdn.microsoft.com/library/hh872476)
</dt> <dd>

The NetTCPIP provider supports classes that interact with TCPIP connections.

</dd> <dt>

<span id="NetTtCim"></span><span id="netttcim"></span><span id="NETTTCIM"></span>[NetTtCim](https://msdn.microsoft.com/library/hh872474)
</dt> <dd>

This section provides reference information for NetTtCim provider classes defined in NetTtCim.mof and implemented in NetTtCim.dll.

</dd> <dt>

<span id="NetWNV"></span><span id="netwnv"></span><span id="NETWNV"></span>[NetWNV](https://msdn.microsoft.com/library/hh872477)
</dt> <dd>

The NetWNV provider supports classes that interact with net virtualization technologies.

</dd> <dt>

<span id="Network_Access_Protection"></span><span id="network_access_protection"></span><span id="NETWORK_ACCESS_PROTECTION"></span>[Network Access Protection](https://msdn.microsoft.com/library/windows/desktop/dn744309)
</dt> <dd>

The Network Access Protection provider exposes a platform for protected access to private networks.

</dd> <dt>

<span id="Network_Load_Balancing"></span><span id="network_load_balancing"></span><span id="NETWORK_LOAD_BALANCING"></span>[Network Load Balancing](https://msdn.microsoft.com/library/cc296105)
</dt> <dd>

The Network Load Balancing (NLB) Provider enables management of a NLB cluster.

</dd> <dt>

<span id="NetworkController_Server"></span><span id="networkcontroller_server"></span><span id="NETWORKCONTROLLER_SERVER"></span>[NetworkController Server](https://msdn.microsoft.com/library/mt164705)
</dt> <dd>

The provider enables management of a network controller server.

</dd> <dt>

<span id="NFS"></span><span id="nfs"></span>[NFS](https://msdn.microsoft.com/library/ff706658)
</dt> <dd>

The provider for NFS allows you to create tools and scripts for configuring and monitoring the Windows Network File System.

</dd> <dt>

<span id="Ping"></span><span id="ping"></span><span id="PING"></span>[Ping](https://msdn.microsoft.com/library/aa392743)
</dt> <dd>

The Ping provider supplies access to the status information provided by the standard ping command.

</dd> <dt>

<span id="Policy"></span><span id="policy"></span><span id="POLICY"></span>[Policy](https://msdn.microsoft.com/library/aa392744)
</dt> <dd>

Provides extensions to group policy, and permits refinements in the application of policy.

</dd> <dt>

<span id="Power_Meter"></span><span id="power_meter"></span><span id="POWER_METER"></span>[Power Meter](https://msdn.microsoft.com/library/dn622954)
</dt> <dd>

The Power Meter provider supports the Power Metering and Budgeting (PMB) interface. These classes are the primary interface for the query of Power Meter Interface (PMI) information from underlying power meters on the system.

</dd> <dt>

<span id="Power_Policy"></span><span id="power_policy"></span><span id="POWER_POLICY"></span>[Power Policy](https://msdn.microsoft.com/library/dn622955)
</dt> <dd>

The Power Policy provider provides classes the ability to remotely manage all the power policy infrastructure.

</dd> <dt>

<span id="RAMgmtPSProvider"></span><span id="ramgmtpsprovider"></span><span id="RAMGMTPSPROVIDER"></span>[RAMgmtPSProvider](https://msdn.microsoft.com/library/hh872484)
</dt> <dd>

The [RAMgmtPSProvider](https://msdn.microsoft.com/library/hh872484) provider provides classes to manage Remote Access.

</dd> <dt>

<span id="RAServerPSProvider"></span><span id="raserverpsprovider"></span><span id="RASERVERPSPROVIDER"></span>[RAServerPSProvider](https://msdn.microsoft.com/library/hh872485)
</dt> <dd>

The [RAServerPSProvider](https://msdn.microsoft.com/library/hh872485) provider provides classes to manage the Remote Access Server.

</dd> <dt>

<span id="ReliabilityMetricsProvider"></span><span id="reliabilitymetricsprovider"></span><span id="RELIABILITYMETRICSPROVIDER"></span>[ReliabilityMetricsProvider](https://msdn.microsoft.com/library/dn622965)
</dt> <dd>

The [ReliabilityMetricsProvider](https://msdn.microsoft.com/library/dn622965) provider exposes system and Windows Event Log reliability metrics.

</dd> <dt>

<span id="Remote_Desktop_Services"></span><span id="remote_desktop_services"></span><span id="REMOTE_DESKTOP_SERVICES"></span>[Remote Desktop Services](https://msdn.microsoft.com/library/aa383511)
</dt> <dd>

Enables consistent server administration in a Remote Desktop Services environment.

</dd> <dt>

<span id="Reporting_Services"></span><span id="reporting_services"></span><span id="REPORTING_SERVICES"></span>[Reporting Services](Http://go.microsoft.com/fwlink/p/?linkid=84358)
</dt> <dd>

Defines classes that allow you to write scripts and code to modify the settings of the report server and the Report Manager.

</dd> <dt>

<span id="Resultant_Set_of_Policy__RSoP_"></span><span id="resultant_set_of_policy__rsop_"></span><span id="RESULTANT_SET_OF_POLICY__RSOP_"></span>[Resultant Set of Policy (RSoP)](https://msdn.microsoft.com/library/aa374408)
</dt> <dd>

Supplies methods to plan and debug policy settings in a what-if situation. These methods allow administrators to determine easily the combination of policy settings that apply to, or will apply to, a user or computer. This is known as the Resultant Set of Policy (RSoP). For more information, see [About the RSoP WMI Method Provider](https://msdn.microsoft.com/library/aa372119) and [RSoP WMI Classes](https://msdn.microsoft.com/library/aa375082).

</dd> <dt>

<span id="Security"></span><span id="security"></span><span id="SECURITY"></span>[Security](https://msdn.microsoft.com/library/aa393274)
</dt> <dd>

Retrieves or changes security settings that control ownership, auditing, and access rights to files, directories, and shares.

</dd> <dt>

<span id="ServerManager.DeploymentProvider"></span><span id="servermanager.deploymentprovider"></span><span id="SERVERMANAGER.DEPLOYMENTPROVIDER"></span>[ServerManager.DeploymentProvider](https://msdn.microsoft.com/library/hh872518)
</dt> <dd>

The [ServerManager.DeploymentProvider](https://msdn.microsoft.com/library/hh872518) exposes deployment functionality.

</dd> <dt>

<span id="Session"></span><span id="session"></span><span id="SESSION"></span>[Session](https://msdn.microsoft.com/library/aa393282)
</dt> <dd>

Manages network sessions and connections.

</dd> <dt>

<span id="Shadow_Copy"></span><span id="shadow_copy"></span><span id="SHADOW_COPY"></span>[Shadow Copy](https://msdn.microsoft.com/library/aa393625)
</dt> <dd>

Supplies management functions for the Shadow Copies of the Shared Folders feature.

</dd> <dt>

<span id="Shielded_VM_Provisioning"></span><span id="shielded_vm_provisioning"></span><span id="SHIELDED_VM_PROVISIONING"></span>[Shielded VM Provisioning](https://msdn.microsoft.com/library/mt130276)
</dt> <dd>

The Shielded VM Provisioning provider enables a fabric controller to start the secure provisioning of a shielded VM on a Hyper-V host.

</dd> <dt>

<span id="Shielded_VM_Provisioning_Service"></span><span id="shielded_vm_provisioning_service"></span><span id="SHIELDED_VM_PROVISIONING_SERVICE"></span>[Shielded VM Provisioning Service](https://msdn.microsoft.com/library/mt164700)
</dt> <dd>

The provider enables provisioning of a shielded virtual machine.

</dd> <dt>

<span id="SMB_Management"></span><span id="smb_management"></span><span id="SMB_MANAGEMENT"></span>[SMB Management](https://msdn.microsoft.com/library/hh830479)
</dt> <dd>

The SMB Management API provides classes and methods to manage shares and share access.

</dd> <dt>

<span id="SNMP"></span><span id="snmp"></span>[SNMP](https://msdn.microsoft.com/library/aa393635)
</dt> <dd>

Maps Simple Network Management Protocol (SNMP) objects that are defined in Management Information Base (MIB) schema objects to classes. For more information, see [Setting up the WMI SNMP Environment](https://msdn.microsoft.com/library/aa393621).

</dd> <dt>

<span id="Software_Inventory_Logging"></span><span id="software_inventory_logging"></span><span id="SOFTWARE_INVENTORY_LOGGING"></span>[Software Inventory Logging](https://msdn.microsoft.com/library/dn440662)
</dt> <dd>

The Software Inventory Logging provider collects licensing data about software installed on a Windows Server, and provides remote access to the data so it can be aggregated easily by a datacenter.

</dd> <dt>

<span id="Software_Licensing_for_"></span><span id="software_licensing_for_"></span><span id="SOFTWARE_LICENSING_FOR_"></span>[Software Licensing for Windows Vista](https://msdn.microsoft.com/library/ee957720)
</dt> <dd>

[Software Licensing Classes](https://msdn.microsoft.com/library/dn622972) used for Windows Vista.

</dd> <dt>

<span id="Software_License"></span><span id="software_license"></span><span id="SOFTWARE_LICENSE"></span>[Software License](https://msdn.microsoft.com/library/dn622972)
</dt> <dd>

The Software Licensing provider retrieves software licensing data.

</dd> <dt>

<span id="Storage_Volume"></span><span id="storage_volume"></span><span id="STORAGE_VOLUME"></span>[Storage Volume](https://msdn.microsoft.com/library/aa393675)
</dt> <dd>

The Storage Volume provider supplies volume management functions.

</dd> <dt>

<span id="Storage_Replica"></span><span id="storage_replica"></span><span id="STORAGE_REPLICA"></span>[Storage Replica](https://msdn.microsoft.com/library/mt127177)
</dt> <dd>

The provider enables management of a storage replica.

</dd> <dt>

<span id="System_Registry"></span><span id="system_registry"></span><span id="SYSTEM_REGISTRY"></span>[System Registry](https://msdn.microsoft.com/library/aa393886)
</dt> <dd>

The System Registry provider enables management applications to retrieve and modify data in the system registry, and receive notifications when changes occur.

</dd> <dt>

<span id="System_Restore"></span><span id="system_restore"></span><span id="SYSTEM_RESTORE"></span>[System Restore](https://msdn.microsoft.com/library/windows/desktop/dd408121)
</dt> <dd>

Supplies classes that configure and use System Restore functionality. For more information, see [Configuring System Restore](https://msdn.microsoft.com/library/windows/desktop/aa378835) and the [System Restore WMI Classes](https://msdn.microsoft.com/library/windows/desktop/aa378986).

</dd> <dt>

<span id="Trusted_Platform_Module"></span><span id="trusted_platform_module"></span><span id="TRUSTED_PLATFORM_MODULE"></span>[Trusted Platform Module](https://msdn.microsoft.com/library/windows/desktop/aa376480)
</dt> <dd>

Provides access to data about a security device, represented by an instance of [**Win32\_TPM**](https://msdn.microsoft.com/library/windows/desktop/aa376484), that is the root of trust for a Microsoft Windows trusted platform computer system.

</dd> <dt>

<span id="Trustmon"></span><span id="trustmon"></span><span id="TRUSTMON"></span>[Trustmon](https://msdn.microsoft.com/library/aa393921)
</dt> <dd>

The [Trustmon](https://msdn.microsoft.com/library/aa393921) provider is an instance provider that creates classes with information about the trust relationships between domains.

</dd> <dt>

<span id="User_Access_Logging"></span><span id="user_access_logging"></span><span id="USER_ACCESS_LOGGING"></span>[User Access Logging](https://msdn.microsoft.com/library/hh437528)
</dt> <dd>

User Access Logging (UAL) is a common framework for Windows Server roles to report their respective consumption metrics.

</dd> <dt>

<span id="UserProfileProvider"></span><span id="userprofileprovider"></span><span id="USERPROFILEPROVIDER"></span>[UserProfileProvider](https://msdn.microsoft.com/library/dn622974)
</dt> <dd>

The [UserProfileProvider](https://msdn.microsoft.com/library/dn622974) provider exposes classes that provide information about a user profile on a Windows system, as well as the health status of a redirected user folder.

</dd> <dt>

<span id="User_State_Management"></span><span id="user_state_management"></span><span id="USER_STATE_MANAGEMENT"></span>[User State Management](https://msdn.microsoft.com/library/windows/desktop/hh830616)
</dt> <dd>

The User State Management provider exposes a management and reporting API for enterprise scenarios.

</dd> <dt>

<span id="View"></span><span id="view"></span><span id="VIEW"></span>[View](https://msdn.microsoft.com/library/aa393970)
</dt> <dd>

Creates new instances and methods based on instances of other classes. Two versions of the View provider are available on 64-bit platforms.

</dd> <dt>

<span id="VPNClientPSProvider"></span><span id="vpnclientpsprovider"></span><span id="VPNCLIENTPSPROVIDER"></span>[VPNClientPSProvider](https://msdn.microsoft.com/library/jj206654)
</dt> <dd>

The [VPNClientPSProvider](https://msdn.microsoft.com/library/jj206654) provider exposes a platform for automating connectivity to a virtual private network client.

</dd> <dt>

<span id="WDM"></span><span id="wdm"></span>[WDM](https://msdn.microsoft.com/library/windows/desktop/aa394052)
</dt> <dd>

Provides access to the classes, instances, methods, and events of hardware drivers that conform to the Windows Driver Model (WDM).

</dd> <dt>

<span id="WFasCim"></span><span id="wfascim"></span><span id="WFASCIM"></span>[WFasCim](https://msdn.microsoft.com/library/jj676898)
</dt> <dd>

The [WFasCim](https://msdn.microsoft.com/library/jj676898) provider exposes network security and filtering features.

</dd> <dt>

<span id="WhqlProvider"></span><span id="whqlprovider"></span><span id="WHQLPROVIDER"></span>[WhqlProvider](https://msdn.microsoft.com/library/dn622975)
</dt> <dd>

The [WhqlProvider](https://msdn.microsoft.com/library/dn622975) provider exposes digital signature information about drivers.

</dd> <dt>

<span id="Win32ClockProvider"></span><span id="win32clockprovider"></span><span id="WIN32CLOCKPROVIDER"></span>[Win32ClockProvider](https://msdn.microsoft.com/library/dn622976)
</dt> <dd>

The [Win32ClockProvider](https://msdn.microsoft.com/library/dn622976) provider exposes the current, local, and UTC-based timestamps on a computer system.

</dd> <dt>

<span id="Windows_Data_Access_Components__WDAC_"></span><span id="windows_data_access_components__wdac_"></span><span id="WINDOWS_DATA_ACCESS_COMPONENTS__WDAC_"></span>[Windows Data Access Components (WDAC)](https://msdn.microsoft.com/library/dn806533)
</dt> <dd>

Provides management of WDAC.

</dd> <dt>

<span id="Windows_Defender"></span><span id="windows_defender"></span><span id="WINDOWS_DEFENDER"></span>[Windows Defender](https://msdn.microsoft.com/library/windows/desktop/dn439477)
</dt> <dd>

The Windows Defender provider exposes Windows Defender security features.

</dd> <dt>

<span id="Windows_Installer"></span><span id="windows_installer"></span><span id="WINDOWS_INSTALLER"></span>[Windows Installer](https://msdn.microsoft.com/library/aa394523)
</dt> <dd>

The Windows Installer provider, also known as the MSI provider allows applications to access information collected from Windows Installer compliant applications.

</dd> <dt>

<span id="Windows_Product_Activation"></span><span id="windows_product_activation"></span><span id="WINDOWS_PRODUCT_ACTIVATION"></span>[Windows Product Activation](https://msdn.microsoft.com/library/aa394524)
</dt> <dd>

The Windows Product Activation (WPA) provider is an anti-piracy technology aimed at reducing the casual copying of software.

</dd> <dt>

<span id="Windows_Server_Manager"></span><span id="windows_server_manager"></span><span id="WINDOWS_SERVER_MANAGER"></span>[Windows Server Manager](https://msdn.microsoft.com/library/mt164645)
</dt> <dd>

The provider enables access to and management of the configuration controlled by the Server Manager application.

</dd> <dt>

<span id="Windows_Server_Storage_Management__MsftStrgMan_"></span><span id="windows_server_storage_management__msftstrgman_"></span><span id="WINDOWS_SERVER_STORAGE_MANAGEMENT__MSFTSTRGMAN_"></span>[Windows Server Storage Management (MsftStrgMan)](https://msdn.microsoft.com/library/mt127223)
</dt> <dd>

The MsftStrgMan provider provides management for storage systems on Windows Server products.

</dd> <dt>

<span id="Windows_Storage_Management__StrgMgmt_"></span><span id="windows_storage_management__strgmgmt_"></span><span id="WINDOWS_STORAGE_MANAGEMENT__STRGMGMT_"></span>[Windows Storage Management (StrgMgmt)](https://msdn.microsoft.com/library/windows/desktop/hh830613)
</dt> <dd>

The StrgMgmt provider can be used to manage a wide range of storage configurations, from tablets to external storage arrays on servers.

</dd> <dt>

<span id="Windows_System_Assessment_Tool"></span><span id="windows_system_assessment_tool"></span><span id="WINDOWS_SYSTEM_ASSESSMENT_TOOL"></span>[Windows System Assessment Tool](https://msdn.microsoft.com/library/windows/desktop/aa969208)
</dt> <dd>

The Windows System Assessment Tool (WinSAT) exposes a number of classes that assesses the performance characteristics and capabilities of a computer.

</dd> <dt>

<span id="WMI_Core"></span><span id="wmi_core"></span><span id="WMI_CORE"></span>[WMI Core](https://msdn.microsoft.com/library/windows/desktop/dn622981)
</dt> <dd>

The WMI Core provider defines classes that compose the core functionality of WMI.

</dd> <dt>

<span id="Msft_ProviderSubSystem"></span><span id="msft_providersubsystem"></span><span id="MSFT_PROVIDERSUBSYSTEM"></span>[Msft\_ProviderSubSystem](https://msdn.microsoft.com/library/dn622939)
</dt> <dd>

The [Msft\_ProviderSubSystem](https://msdn.microsoft.com/library/dn622939) provider supports providers.

</dd> <dt>

<span id="Win32_Perf"></span><span id="win32_perf"></span><span id="WIN32_PERF"></span>[Win32\_Perf](https://msdn.microsoft.com/library/dn622979)
</dt> <dd>

The [**Win32\_Perf**](https://msdn.microsoft.com/library/dn622979) abstract class is the base class for the performance counter classes [**Win32\_PerfRawData**](https://msdn.microsoft.com/library/dn622978) and [**Win32\_PerfFormattedData**](https://msdn.microsoft.com/library/dn622977). It defines the required timestamp and frequency properties used in the CounterType algorithms for the performance counter classes.

</dd> <dt>

<span id="Win32_PerfFormattedData"></span><span id="win32_perfformatteddata"></span><span id="WIN32_PERFFORMATTEDDATA"></span>[**Win32\_PerfFormattedData**](https://msdn.microsoft.com/library/dn622977)
</dt> <dd>

An abstract base class for the pre-installed, calculated data classes.

</dd> <dt>

<span id="Win32_PerfRawData"></span><span id="win32_perfrawdata"></span><span id="WIN32_PERFRAWDATA"></span>[**Win32\_PerfRawData**](https://msdn.microsoft.com/library/dn622978)
</dt> <dd>

The performance counter class [**Win32\_PerfRawData**](https://msdn.microsoft.com/library/dn622978) is the abstract base class for all concrete raw performance counter classes. To appear in System Monitor, performance counter classes must be added to the "Root\\CIMv2" namespace and derived from **Win32\_PerfRawData**.

</dd> <dt>

<span id="WMIPerfClass"></span><span id="wmiperfclass"></span><span id="WMIPERFCLASS"></span>[WMIPerfClass](https://msdn.microsoft.com/library/aa394546)
</dt> <dd>

Creates the WMI [Performance Counter Classes](https://msdn.microsoft.com/library/aa392738). Data is dynamically supplied to these performance classes by the WMIPerfInst provider.

</dd> <dt>

<span id="WmiPerfInst"></span><span id="wmiperfinst"></span><span id="WMIPERFINST"></span>[WmiPerfInst](https://msdn.microsoft.com/library/aa394547)
</dt> <dd>

Supplies raw and formatted performance counter data dynamically from [Performance Counter Class](https://msdn.microsoft.com/library/aa392738) definitions.

</dd> <dt>

<span id="Work_Folders"></span><span id="work_folders"></span><span id="WORK_FOLDERS"></span>[Work Folders](https://msdn.microsoft.com/library/dn632596)
</dt> <dd>

Work Folders is used to synchronize files with multiple PCs and mobile devices.

</dd> </dl>

 

 




---
Description: 'A list of the reference content for the Windows API.'
ms.assetid: '9CA123F9-92F1-4761-9468-266DA422F70E'
title: Windows API Index
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Windows API Index

The following is a list of the reference content for the Windows application programming interface (API) for desktop and server applications.

Using the Windows API, you can develop applications that run successfully on all versions of Windows while taking advantage of the features and capabilities unique to each version. (Note that this was formerly called the Win32 API. The name Windows API more accurately reflects its roots in 16-bit Windows and its support on 64-bit Windows.)

## User Interface

The Windows UI API create and use windows to display output, prompt for user input, and carry out the other tasks that support interaction with the user. Most applications create at least one window.

-   [Accessibility](winauto.windows_accessibility_features_reference)
-   [Desktop Window Manager (DWM)](dwm.reference)
-   [Globalization Services](intl.globalization_services)
-   [High DPI](hidpi.high_dpi_reference)
-   [Multilingual User Interface (MUI)](intl.multilingual_user_interface_reference)
-   [National Language Support (NLS)](intl.national_language_support_reference)
-   [User Interface elements](winprog.user_interface):

    -   [Buttons](controls.bumper_button_button_control_reference)
    -   [Carets](menurc.caret_functions)
    -   [Combo Boxes](controls.bumper_combobox_combobox_control_reference)
    -   [Common Dialog Boxes](dlgbox.common_dialog_box_reference)
    -   [Common Controls](controls._win32_Individual_Control_Info)
    -   [Cursors](menurc.cursor_reference)
    -   [Dialog Boxes](dlgbox.dialog_box_reference)
    -   [Edit Controls](controls.bumper_edit_control_edit_control_reference)
    -   [Header Controls](controls.bumper_header_control_header_control_reference)
    -   [Icons](menurc.icon_reference)
    -   [Keyboard Accelerators](menurc.keyboard_accelerator_reference)
    -   [List Boxes](controls.bumper_list_box_list_box_control_reference)
    -   [List-View Controls](controls.bumper_list_view_list-view_control_reference)
    -   [Menus](menurc.menu_reference)
    -   [Progress Bars](controls.bumper_progress_bar_progress_bar_control_reference)
    -   [Property Sheets](controls.bumper_property_sheet_property_sheets_reference)
    -   [Rich Edit Controls](controls.bumper_rich_edit_rich_edit_control_reference)
    -   [Scroll Bars](controls.bumper_scroll_bar_scroll_bars_reference)
    -   [Static Controls](controls.bumper_static_control_static_control_reference)
    -   [Strings](menurc.string_reference)
    -   [Toolbars](controls.bumper_toolbar_toolbar_control_reference)
    -   [Tooltips](controls.bumper_tooltip_tooltip_control_reference)
    -   [Trackbars](controls.bumper_trackbar_trackbar_control_reference)
    -   [Tree-View Controls](controls.bumper_tree_view_tree-view_control_reference)

-   [Windows Animation Manager](uianimation.windows_animation_reference)
-   [Windows Ribbon Framework](windowsribbon.windowsribbon_reference_entry)

## Windows Environment (Shell)

-   [Windows Property System](properties.property_system_reference)
-   [Windows Shell](shell.shell_reference_bumper)
-   [Windows Search](search._search_Reference_Entry_Page)
-   [Consoles](base.console_reference)

## User Input and Messaging

-   [User Interaction](nodepage.user_interaction)
    -   [Direct Manipulation](directmanipulation.direct_manipulation_portal)
    -   [Ink input](input_ink.input_ink_portal)
    -   [Input Feedback Configuration](input_feedback.input_feedback_configuration_portal)
    -   [Interaction Context](input_intcontext.interaction_context_portal)
    -   [Pointer Device Input Stack](input_pointerdevice.pointer_device_stack_portal)
    -   [Pointer Input Messages and Notifications](inputmsg.messages_and_notifications)
    -   [Radial controller input](Input_Radial.radialcontroller_portal)
    -   [Text Services Framework](tsf.text_services_framework)
    -   [Touch Hit Testing](input_touchhittest.touch_hit_testing_portal)
    -   [Touch Injection](input_touchinjection.touch_injection_portal)
-   [Legacy User Interaction](nodepage.legacy_user_interaction_features)
    -   [Touch Input](wintouch.windows_touch_portal)
    -   [Keyboard Input](inputdev.keyboard_input)
    -   [Mouse Input](inputdev.mouse_input)
    -   [Raw Input](inputdev.raw_input)
-   [Windows and Messages](winmsg.windowing):

    -   [Messages and Message Queues](winmsg.message_and_message_queue_reference)
    -   [Windows](winmsg.window_reference)
    -   [Window Classes](winmsg.window_class_reference)
    -   [Window Procedures](winmsg.window_procedure_reference)
    -   [Timers](winmsg.timer_reference)
    -   [Window Properties](winmsg.window_property_reference)
    -   [Hooks](winmsg.hook_reference)

## Data access and storage

-   [Background Intelligent Transfer Service (BITS)](bits.bits_reference)
-   [Data Backup](nodepage.backup)
    -   [Backup](backup.backup_reference)
    -   [Data Deduplication](dedup.data_deduplication_api_reference)
    -   [Volume Shadow Copy](base.volume_shadow_copy_reference)
    -   [Windows Server Backup](wsb.windows_server_backup_api_interfaces)
-   [Data Exchange](dataxchg.data_exchange):

    -   [Clipboard](dataxchg.clipboard_reference)
    -   [Dynamic Data Exchange (DDE)](dataxchg.dynamic_data_exchange_reference)
    -   [Dynamic Data Exchange Management (DDEML)](dataxchg.dynamic_data_exchange_management_library_reference)

-   [Directory Management](fs.directory_management_reference)
-   [Disk Management](fs.disk_management_reference)
-   [Distributed File System (DFS)](dfs.distributed_file_system_reference)
-   [Distributed File System Replication](dfsr.dfsr_wmi_classes)
-   [Extensible Storage Engine](5033f53b-72f1-4a28-926e-242461863071)
-   [Files and I/O (Local file system)](fs.file_management_reference)
-   [iSCSI Discovery Library API](iscsidisc.iscsi_discovery_library_reference)
-   [Offline Files](of.offline_files_reference)
-   [Packaging](opc.packaging_programming_reference)
-   [Remote Differential Compression](rdc.remote_differential_compression_reference)
-   [Transactional NTFS](fs.transactional_ntfs_reference)
-   [Volume Management](fs.volume_management_reference)
-   [Virtual Hard Disk (VHD)](vhd.vhd_reference)
-   [Windows Storage Management](stormgmt.windows_storage_management_api_portal)
-   [Windows Data Access Components](dedd0762-f224-4736-9894-32bd8313ea61)
    -   [Microsoft Open Database Connectivity (ODBC)](1ba0f6cc-dfa7-4fe8-8bc2-f862b386156d)
    -   [Microsoft OLE DB](9441cd79-c5cd-4d28-9897-389e7264ea95)
    -   [Microsoft ActiveX Data Objects (ADO)](6dc27c85-84e1-472a-b057-d1854b8c98a3)

## Diagnostics

The [Diagnostics](winprog.diagnostics) API enable you to troubleshoot application or system problems and monitor performance.

-   [Application Recovery and Restart](recovery.application_recovery_and_restart_reference)
-   [Debugging](base.debugging_reference)
-   [Error Handling](base.error_handling_reference)
-   [Event Logging](base.event_logging_reference)
-   [Event Tracing](etw.event_tracing_reference)
-   [Hardware Counter Profiling (HCP)](hcp.hcp_reference)
-   [Network Diagnostics Framework (NDF)](ndf.ndf_reference)
-   [Network Monitor](netmon.reference)
-   [Performance Counters](perf.performance_counters_reference)
-   [Performance Logs and Alerts (PLA)](pla.performance_logs_and_alerts_reference)
-   [Process Snapshotting](proc_snap.process_snapshotting_reference)
-   [Process Status (PSAPI)](base.psapi_reference)
-   [Structured Exception Handling](base.structured_exception_handling_reference)
-   [System Monitor](sysmon.system_monitor_reference)
-   [Wait Chain Traversal](base.wait_chain_traversal)
-   [Windows Error Reporting (WER)](wer.wer_reference)
-   [Windows Event Log](wes.windows_event_log_reference)
-   [Windows Troubleshooting Platform](wintt.windows_troubleshooting_reference)

## Graphics and Multimedia

The [Graphics, multimedia,](winprog.graphics_and_multimedia) [audio, and video](nodepage.audio_and_video) APIs enable applications to incorporate formatted text, graphics, audio, and video.

-   [Core Audio](coreaudio.programming_reference)
-   [Direct2D](direct2d.reference)
-   [DirectComposition](directcomp.reference)
-   [DirectShow](dshow.directshow_reference)
-   [DirectWrite](directwrite.reference)
-   [DirectX](nodepage.directx_sdk__august_2009_)
-   [Media Streaming](mediastreaming.media_streaming_api_portal)
-   [Microsoft Media Foundation](mf.media_foundation_programming_reference)
-   [Microsoft TV Technologies](mstv.microsoft_tv_technologies_application_interface)
-   [Windows Imaging Component (WIC)](wic._wic_codec_reference)
-   [Windows Media Audio and Video Codec and DSP](codecapi.codecprogrammingreference)
-   [Windows Media Center](ProgrammingReference)
-   [Windows Media Format](wmformat.programming_reference)
-   [Windows Media Library Sharing Services](wmlss.WindowsMediaLibrarySharingServicesPortal)
-   [Windows Media Player](wmp.windows_media_player_object_model_reference)
-   [Windows Media Services](fc740e87-575b-4da2-89fb-40a6c39f9017)
-   [Windows Movie Maker](wmmdvdm.windows_movie_maker_apis)

## Devices

-   [AllJoyn](alljoyn.alljoyn_api_portal)
-   [Communications Resources](base.communications_reference)
-   [Device Access](deviceaccess.device_access_api_c___programming_reference)
-   [Device Management](base.device_management_reference)
-   [Enhanced Storage](enstor.enhanced_storage_reference)
-   [Function Discovery](ncd.function_discovery_reference)
-   [Image Mastering](imapi.imapi_reference)
-   [Location](winlocation.windows_location_programming_reference)
-   [PnP-X Association Database](ncd.pnp-x_association_database_reference)
-   [Printing](print.introduction_to_printing)
    -   [Print Spooler](gdi.printing_and_print_spooler_reference)
    -   [Print Document Package](xps.tailored_app_printing_api)
    -   [Print Schema Specification](http://go.microsoft.com/?linkid=7141496)
    -   [Print Ticket](gdi.print_ticket_api)
    -   [XPS Print](gdi.xpsprint_api)
-   [Sensors](winsensors.sensor_api_programming_reference)
-   [System Event Notification Service (SENS)](sens.sens_reference)
-   [Tool Help](base.tool_help_reference)
-   [UPnP](upnp.universal_plug_and_play_start_page)
-   [Web Services on Devices](ncd.web_services_for_devices_reference)
-   [Windows Image Acquisition (WIA)](wia._wia_reference)
-   [Windows Media Device Manager](wmdm.programming_reference)
-   [Windows Portable Devices](wpdsdk.programming_reference)

## System Services

The [System Services](winprog.system_services) APIs give applications access to the resources of the computer and the features of the underlying operating system, such as memory, file systems, devices, processes, and threads.

-   [COM](com.reference)
-   [COM+](cos.com__reference)
-   [Compression API](cmpapi._compression_portal)
-   [Distributed Transaction Coordinator (DTC)](c0f7d3dd-4da1-45df-8516-d0d2ec1b0ca6)
-   [Dynamic-Link Libraries (DLLs)](base.dynamic_link_library_functions)
-   [Help API](helpapi.help_api_reference)
-   [Interprocess Communications](base.interprocess_communications):
    -   [Mailslots](base.mailslot_functions)
    -   [Pipes](base.pipe_functions)
-   [Kernel Transaction Manager (KTM)](fs.ktm_reference)
-   [Memory Management](base.memory_management_reference)
-   [Operation Recorder](oprec._operation_portal)
-   [Power Management](base.power_management_reference)
-   [Remote Desktop Services](termserv.terminal_services_reference)
-   [Processes](base.process_and_thread_reference)
-   [Services](base.service_reference)
-   [Synchronization](base.synchronization_reference)
-   [Threads](base.process_and_thread_reference)
-   [Windows Desktop Sharing](rdp.windows_desktop_sharing_reference)
-   [Windows System Information](base.windows_system_information)
    -   [Handle and Objects](base.handle_and_object_functions)
    -   [Registry](base.registry_reference)
    -   [Time](base.time_reference)
    -   [Time Provider](base.time_provider_reference)

## Security and Identity

The [Security and Identity](winprog.security) APIs enable password authentication at logon, discretionary protection for all sharable system objects, privileged access control, rights management, and security auditing.

-   [Authentication](security.authentication_reference)
-   [Authorization](security.authorization_reference)
-   [Certificate Enrollment](security.certificate_enrollment_api_reference)
-   [Cryptography](security.cryptography_reference)
-   [Cryptographic Next Generation (CNG)](security.cng_reference)
-   [Directory Services](dsportal.directory_services_portal)
    -   [Active Directory Domain Services](ad.active_directory_domain_services_reference)
    -   [Active Directory Service Interfaces (ADSI)](adsi.adsi_reference)
-   [Extensible Authentication Protocol (EAP)](eap.extensible_authentication_protocol_reference)
-   [Extensible Authentication Protocol Host (EAPHost)](eaphost.eaphost_api_reference)
-   [MS-CHAP Password Management](mschap.ms-chap_password_management_reference)
-   [Network Access Protection (NAP)](nap.nap_reference)
-   [Network Policy Server Extensions (NPS)](nps.IAS_internet_authentication_service_reference)
-   [Parental Controls](parcon.parental_controls_reference)
-   [Security WMI Providers](security.security_wmi_providers_reference)
-   [TPM Base Services (TBS)](tbs.tbs_reference)
-   [Windows Biometric Framework](secbiomet.biometric_service_api_reference)

## Application Installation and Servicing

-   [Games Explorer](a85389a3-d349-4914-ebc4-0b849ecc99e5)
-   [Side-by-side Assemblies](setup.side_by_side_assemblies_reference)
-   [Windows Store app Packaging and Desployment](appxpkg.api_reference)
-   [Developer License](devlic.developer_license_apis)
-   [Restart Manager](rstmgr.restart_manager_reference)
-   [Windows Installer](setup.windows_installer_portal)

## System Admin and Management

The [System administration](nodepage.system_administration) interfaces enable you to install, configure, and service applications or systems.

-   [Boot Configuration Data WMI Provider](bcd.bcd_reference)
-   [Failover Clusters](mscs.failover_cluster_apis_portal)
-   [File Server Resource Manager (FSRM)](fsrm.fsrm_reference)
-   [Group Policy](policy.group_policy_reference)
-   [Microsoft Management Console (MMC) 2.0](mmc.mmc_reference)
-   [NetShell](netshell.netshell_reference)
-   [Settings Management Infrastructure](smi.settings_management_infrastructure__smi_)
-   [Software Inventory Logging](sil.software_inventory_logging_reference)
-   [Software Licensing](security.software_licensing_api_reference)
-   [Restart Manager](rstmgr.restart_manager_portal)
-   [Settings Management Infrastructure](smi.settings_management_infrastructure__smi_)
-   [System Restore](sr.system_restore_start_page)
-   [System Shutdown](base.system_shutdown)
-   [Task Scheduler](taskschd.task_scheduler_start_page)
-   [User Access Logging](ual.user_access_logging_reference)
-   [Windows Virtual PC](vpc.virtual_pc_reference)
-   [Microsoft Virtual Server](msvs.microsoft_virtual_server_reference)
-   [Network Load Balancing Provider](mscs.network_load_balancing_provider_reference)
-   [Windows Defender WMI v2](defender.windows_defender_wmiv2_apis_portal)
-   [Windows Deployment Services](wds.portal)
-   [Windows Genuine Advantage](wingen.windows_genuine_advantage_api_functions)
-   [Windows Management Infrastructure](wmi_v2.wmi_reference)
-   [Windows Management Instrumentation (WMI)](wmi.wmi_reference)
-   [Windows Remote Management](winrm.portal)
-   [Windows Resource Protection](setup.windows_resource_protection_portal)
-   [Windows Server Update Services](995e4afc-4bf5-413a-9bd4-a7abbd7f55b1)
-   [Windows System Assessment Tool](winsat.winsat_reference)
-   [Windows Update Agent](wua.portal_client)

## Networking and Internet

The [Networking](winprog.networking) APIs enable communication between applications over a network. You can also create and manage access to shared resources, such as directories and network printers.

-   [Domain Name System (DNS)](dns.dns_reference)
-   [Dynamic Host Configuration Protocol (DHCP)](dhcp.dhcp_start_page)
-   [Fax Service](fax._mfax_fax_service_reference)
-   [Get Connected Wizard](get_connected.get_connected_wizard_api_reference)
-   [HTTP Server](http.http_server_api_reference)
-   [Internet Connection Sharing and Firewall](ics.internet_connection_sharing_and_internet_connection_firewall_reference)
-   [IP Helper](iphlp.ip_helper_function_reference)
-   [IPv6 Internet Connection Firewall](ics.ipv6_firewall_configuration_reference)
-   [Management Information Base](mib.management_information_base_reference)
-   [Message Queuing (MSMQ)](1746e651-19ca-4e21-b3b6-e1cc19389bb5)
-   [Multicast Address Dynamic Client Allocation Protocol (MADCAP)](madcap.madcap_reference)
-   [Network Address Translation (NAT)](ics.network_address_translation_traversal_reference)
-   [Network List Manager (NLM)](nla.network_list_manager_api_reference)
-   [Network Management](netmgmt.network_management_reference)
-   [Network Share Management](fs.network_share_management_reference)
-   [Peer-to-Peer](p2p.portal)
-   [Quality of Service (QOS)](qos.qos_reference)
-   [Remote Procedure Call](rpc.reference)
-   [Routing and Remote Access Service (RAS)](rras.portal)
-   [Simple Network Management Protocol (SNMP)](snmp.snmp_reference)
-   [SMB Management](smb.smb_management_api_portal)
-   [Telephony Application Programming Interfaces (TAPI)](tapi3.telephony_application_programming_interfaces)
-   [WebDAV](webdav.webdav_api_reference)
-   [WebSocket Protocol Component](websock.web_socket_protocol_component_api_portal)
-   Wireless networking:
    -   [Bluetooth](bluetooth.bluetooth_reference)
    -   [IrDA](irda.irda_and_windows_sockets_reference)
    -   [Mobile Broadband](mbn.mobile_broadband_networks_api_reference)
    -   [Native Wifi](nwifi.native_wifi_reference)
    -   [Windows Connect Now](wcn.windows_connect_now_reference)
    -   [Windows Connection Manager](wcm.windows_connection_manager_reference)
-   [Windows Filtering Platform](fwp.fwp_reference)
-   [Windows Firewall with Advanced Security](ics.windows_firewall_with_advanced_security_reference)
-   [Windows HTTP Services (WinHTTP)](http.winhttp_reference)
-   [Windows Internet (WinINet)](wininet.wininet_reference)
-   [Windows Networking (WNet)](wnet.windows_networking_reference)
-   [Windows Network Virtualization](wnv.windows_network_virtualization_portal)
-   [Windows RSS Platform](rss_ref_entry)
-   [Windows Sockets (Winsock)](winsock.winsock_reference)
-   [Windows Web Services](wsw.windows_web_services_reference)
-   [XML HTTP Extended Request](ixhr2.ixmlhttprequest2_portal)

## Deprecated or legacy APIs

The following are technologies and APIs that are outdated or have been replaced or deprecated from the Windows client and server operating systems.

-   [DirectMusic](DirectMusicCCReference_9)
-   [DirectSound](O:Microsoft.directx_sdk.reference.dx9_directsound_reference)
-   [Graphics Device Interface (GDI)](gdi.windows_gdi): Use [Direct2D](direct2d.reference) instead.
-   [GDI+](gdiplus._gdiplus_CLASS_GDI_Reference): Use [Direct2D](direct2d.reference) instead.
-   [Microsoft UDDI SDK](ac915f15-6640-47f3-ae64-1a31e7220552) is now included with [Microsoft BizTalk Server](http://go.microsoft.com/fwlink/p/?LinkID=122067).
-   [Monitor Configuration](monitor.monitor_configuration_reference)
-   [Multiple Display Monitors](gdi.multiple_display_monitors_reference)
-   [Network Dynamic Data Exchange (DDE)](base.network_dde_reference)
-   [OpenGL](opengl.opengl_reference)
-   [Picture Acquisition](picacq.programming_reference)
-   [Remote Installation Service](c62e5951-5eb9-42f1-95ae-490e5d7a5551): Use [Windows Deployment Services](wds.windows_deployment_services_portal) instead.
-   [Virtual Disk Service (VDS)](base.vds_reference): Use [Windows Storage Management](stormgmt.windows_storage_management_api_portal) instead.
-   Terminal Services: Use [Remote Desktop Services](termserv.terminal_services_reference).
-   [Windows Color System](wcs.reference)
-   [Windows Media Rights Manager](http://msdn.microsoft.com/en-us/library/windows/desktop/bb614742.aspx)
-   [Windows Messaging (MAPI)](mapi.mapi_stub_library_and_simple_mapi): Use [Office MAPI](3d980b86-7001-4869-9780-121c6bfc7275) instead.
-   [Windows Multimedia](multimedia.multimedia_reference)
-   [Windows Gadget Platform](gadgetplatform.windows_gadget_platform_portal): Create Windows Store apps instead.
-   [Windows Sidebar](sidebar._sidebar_ref_entry): Create Windows Store apps instead.
-   [Windows SideShow](9f2d2769-c07a-4609-aac5-e14545dc02f5): No replacement.
-   [WPF Bitmap Effects](wibe._wibe_about_bitmapeffects)

 

 




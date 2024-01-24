---
description: The following list lists events supported by WMI logs in Windows Vista and later operating systems.
ms.assetid: ad8891cc-0b76-404d-81fc-961bcdbfae32
ms.tgt_platform: multiple
title: WMI Event Messages
ms.topic: reference
ms.date: 05/31/2018
---

# WMI Event Messages

The following list lists events supported by WMI logs in Windows Vista and later operating systems.

> [!Note]  
> The following documentation is designed for developers and IT administrators. If you are attempting to resolve a WMI error message on your home system, please refer to the [Microsoft Support](https://support.microsoft.com/) website.

 

<dl> <dt>

<span id="WBEM_MC_REPOSITORY_INCONSISTENT"></span><span id="wbem_mc_repository_inconsistent"></span>**WBEM\_MC\_REPOSITORY\_INCONSISTENT**
</dt> <dd> <dl> <dt>

1073747424 (0x400015E0)
</dt> <dt>



The Windows Management Instrumentation Service detected an inconsistency with the WMI repository in the directory *%windir%\\system32\\wbem\\repository* and was not able to recover it. The WMI repository will now be deleted, A new repository will be created based on the auto-recovery mechanism.


</dt> </dl> </dd> <dt>

<span id="WBEM_MC_PROVIDER_SUBSYSTEM_LOCALSYSTEM_PROVIDER_LOAD"></span><span id="wbem_mc_provider_subsystem_localsystem_provider_load"></span>**WBEM\_MC\_PROVIDER\_SUBSYSTEM\_LOCALSYSTEM\_PROVIDER\_LOAD**
</dt> <dd> <dl> <dt>

2147483711 (0x8000003F)
</dt> <dt>



A provider, %1, has been registered in the Windows Management Instrumentation namespace %2 to use the LocalSystem account. This account is privileged and the provider may cause a security violation if it does not correctly impersonate user requests.


</dt> </dl> </dd> <dt>

<span id="WBEM_MC_MOF_NOT_LOADED_AT_RECOVERY"></span><span id="wbem_mc_mof_not_loaded_at_recovery"></span>**WBEM\_MC\_MOF\_NOT\_LOADED\_AT\_RECOVERY**
</dt> <dd> <dl> <dt>

3221225476 (0xC0000004)
</dt> <dt>



Error %1 encountered when trying to load MOF %2 while recovering .MOF file marked with autorecover.


</dt> </dl> </dd> <dt>

<span id="WBEM_MC_CANNOT_ACTIVATE_FILTER"></span><span id="wbem_mc_cannot_activate_filter"></span>**WBEM\_MC\_CANNOT\_ACTIVATE\_FILTER**
</dt> <dd> <dl> <dt>

3221225482 (0xC000000A)
</dt> <dt>



Event filter with query "%2" could not be reactivated in namespace "%1" because of error %3. Events cannot be delivered through this filter until the problem is corrected.


</dt> </dl> </dd> <dt>

<span id="WBEM_MC_INVALID_EVENT_PROVIDER_QUERY"></span><span id="wbem_mc_invalid_event_provider_query"></span>**WBEM\_MC\_INVALID\_EVENT\_PROVIDER\_QUERY**
</dt> <dd> <dl> <dt>

3221225493 (0xC0000015)
</dt> <dt>



Event provider %1 attempted to register a syntactically invalid query "%2". The query will be ignored. The query can be corrected by examining the WMI repository with CIM studio and updating the permanent subscriptions for the listed provider and query. If the permanent subscription is created with MOF file coming with an installed product, the application vendor must be contacted to correct the faulty registration.


</dt> </dl> </dd> <dt>

<span id="WBEM_MC_INVALID_EVENT_PROVIDER_INTRINSIC_QUERY"></span><span id="wbem_mc_invalid_event_provider_intrinsic_query"></span>**WBEM\_MC\_INVALID\_EVENT\_PROVIDER\_INTRINSIC\_QUERY**
</dt> <dd> <dl> <dt>

3221225494 (0xC0000016)
</dt> <dt>



Event provider %1 attempted to register an intrinsic event query "%2" in %3 namespace for which the set of target object classes could not be determined. The query will be ignored.


</dt> </dl> </dd> <dt>

<span id="WBEM_MC_EVENT_PROVIDER_QUERY_TOO_BROAD"></span><span id="wbem_mc_event_provider_query_too_broad"></span>**WBEM\_MC\_EVENT\_PROVIDER\_QUERY\_TOO\_BROAD**
</dt> <dd> <dl> <dt>

3221225495 (0xC0000017)
</dt> <dt>



Event provider %1 attempted to register query "%2" in %3 namespace which is too broad. Event providers cannot provide events that are provided by the system. The query will be ignored. Contact the application vendor.


</dt> </dl> </dd> <dt>

<span id="WBEM_MC_EVENT_PROVIDER_QUERY_NOT_FOUND"></span><span id="wbem_mc_event_provider_query_not_found"></span>**WBEM\_MC\_EVENT\_PROVIDER\_QUERY\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

3221225496 (0xC0000018)
</dt> <dt>



Event provider %1 attempted to register query "%2" whose target class "%3" in %4 namespace does not exist. The query will be ignored.


</dt> </dl> </dd> <dt>

<span id="WBEM_MC_EVENT_PROVIDER_QUERY_NOT_EVENT"></span><span id="wbem_mc_event_provider_query_not_event"></span>**WBEM\_MC\_EVENT\_PROVIDER\_QUERY\_NOT\_EVENT**
</dt> <dd> <dl> <dt>

3221225497 (0xC0000019)
</dt> <dt>



Event provider %1 attempted to register query &quot;%2&quot; whose target class &quot;%3&quot; is not an event class. The query will be ignored. Contact the application vendor.


</dt> </dl> </dd> <dt>

<span id="WBEM_MC_WBEM_CORE_FAILURE"></span><span id="wbem_mc_wbem_core_failure"></span>**WBEM\_MC\_WBEM\_CORE\_FAILURE**
</dt> <dd> <dl> <dt>

3221225500 (0xC000001C)
</dt> <dt>



Failed to Initialize WMI Core or Provider SubSystem or Event SubSystem with error number %1. This could be due to a badly installed version of WMI, WMI repository upgrade failure, insufficient disk space or insufficient memory.


</dt> </dl> </dd> <dt>

<span id="WBEM_MC_ADAP_CONNECTION_FAILURE"></span><span id="wbem_mc_adap_connection_failure"></span>**WBEM\_MC\_ADAP\_CONNECTION\_FAILURE**
</dt> <dd> <dl> <dt>

3221225515 (0xC000002B)
</dt> <dt>



Windows Management Instrumentation ADAP failed to connect to namespace %1 with the following error %2.


</dt> </dl> </dd> <dt>

<span id="WBEM_MC_ADAP_PERFLIB_PUTCLASS_FAILURE"></span><span id="wbem_mc_adap_perflib_putclass_failure"></span>**WBEM\_MC\_ADAP\_PERFLIB\_PUTCLASS\_FAILURE**
</dt> <dd> <dl> <dt>

3221225520 (0xC0000030)
</dt> <dt>



Windows Management Instrumentation ADAP was unable to save object %1 in namespace %2 because of the following error %3.


</dt> </dl> </dd> <dt>

<span id="WBEM_MC_ADAP_UNABLE_TO_ADD_WIN32PERF"></span><span id="wbem_mc_adap_unable_to_add_win32perf"></span>**WBEM\_MC\_ADAP\_UNABLE\_TO\_ADD\_WIN32PERF**
</dt> <dd> <dl> <dt>

3221225530 (0xC000003A)
</dt> <dt>



Windows Management Instrumentation ADAP was unable to create the Win32\_Perf base class in %1:Result=%2.


</dt> </dl> </dd> <dt>

<span id="WBEM_MC_ADAP_UNABLE_TO_ADD_WIN32PERFRAWDATA"></span><span id="wbem_mc_adap_unable_to_add_win32perfrawdata"></span>**WBEM\_MC\_ADAP\_UNABLE\_TO\_ADD\_WIN32PERFRAWDATA**
</dt> <dd> <dl> <dt>

3221225531 (0xC000003B)
</dt> <dt>



Windows Management Instrumentation ADAP was unable to create the Win32\_PerfRawData base class %1.


</dt> </dl> </dd> <dt>

<span id="WBEM_MC_REPOSITORY_FAILED_TO_START"></span><span id="wbem_mc_repository_failed_to_start"></span>**WBEM\_MC\_REPOSITORY\_FAILED\_TO\_START**
</dt> <dd> <dl> <dt>

3221231073 (0xC00015E1)
</dt> <dt>



The Windows Management Instrumentation Service failed to load the repository files under the directory *%windir%\\system32\\wbem\\repository*. This can be caused by a corruption in the repository files, security settings on this directory, lack of disk space, or other system resource issues such as lack of memory. If this error occurs each time the computer is restarted then the administrator on this computer may need to stop WMI Service, review the security setting on this folder and files under this folder, and run WMIDiag to validate the health of Windows Management Instrumentation.


</dt> </dl> </dd> <dt>

<span id="WBEM_MC_WBEM_REQUIRES_ENCRYPTION_DENIED"></span><span id="wbem_mc_wbem_requires_encryption_denied"></span>**WBEM\_MC\_WBEM\_REQUIRES\_ENCRYPTION\_DENIED**
</dt> <dd> <dl> <dt>

3221231077 (0xC00015E5)
</dt> <dt>



Access to the %1 namespace was denied because the namespace is marked with RequiresEncryption but the script or application attempted to connect to this namespace with an authentication level below **Pkt\_Privacy**. Change the authentication level to **Pkt\_Privacy** and run the script or application again.


</dt> </dl> </dd> <dt>

<span id="WBEM_MC_WBEM_REQUIRES_ENCRYPTION_ASYNC_DENIED"></span><span id="wbem_mc_wbem_requires_encryption_async_denied"></span>**WBEM\_MC\_WBEM\_REQUIRES\_ENCRYPTION\_ASYNC\_DENIED**
</dt> <dd> <dl> <dt>

3221231078 (0xC00015E6)
</dt> <dt>



Windows Management Instrumentation Service could not deliver results asynchronously for %1 namespace. The namespace is marked with RequiresEncryption but WinMgmt could not establish a secure connection back to the client computer. Ensure there is a trust relationship between the client and server computers so that the client recognizes the server computer account.


</dt> </dl> </dd> <dt>

<span id="WBEM_MC_WBEM_HOST_KILLED"></span><span id="wbem_mc_wbem_host_killed"></span>**WBEM\_MC\_WBEM\_HOST\_KILLED**
</dt> <dd> <dl> <dt>

3221231084 (0xC00015EC)
</dt> <dt>



Windows Management Instrumentation has stopped WMIPRVSE.EXE because a quota reached a warning value. Quota: %1 Value: %2 Maximum value: %3 WMIPRVSE PID: %4.


</dt> </dl> </dd> <dt>

<span id="WBEM_MC_WBEM_REPFILESNOTFOUND"></span><span id="wbem_mc_wbem_repfilesnotfound"></span>**WBEM\_MC\_WBEM\_REPFILESNOTFOUND**
</dt> <dd> <dl> <dt>

3221231086 (0xC00015EE)
</dt> <dt>



During the service startup, the Windows Management Instrumentation service was unable to locate the repository files. A new repository will be created based on the auto-recovery mechanism.


</dt> </dl> </dd> <dt>

<span id="WBEM_MC_WBEM_STARTED_SUCESSFULLY"></span><span id="wbem_mc_wbem_started_sucessfully"></span>**WBEM\_MC\_WBEM\_STARTED\_SUCESSFULLY**
</dt> <dd> <dl> <dt>

3221231087 (0xC00015EF)
</dt> <dt>



Windows Management Instrumentation Service started successfully.


</dt> </dl> </dd> <dt>

<span id="WBEM_MC_WBEM_CORE_PSS_ESS_INITIALIZED"></span><span id="wbem_mc_wbem_core_pss_ess_initialized"></span>**WBEM\_MC\_WBEM\_CORE\_PSS\_ESS\_INITIALIZED**
</dt> <dd> <dl> <dt>

3221231089 (0xC00015F1)
</dt> <dt>



Windows Management Instrumentation Service subsystems initialized successfully.


</dt> </dl> </dd> <dt>

<span id="WBEM_MC_WBEM_SERVICE_INIT_FAILURE"></span><span id="wbem_mc_wbem_service_init_failure"></span>**WBEM\_MC\_WBEM\_SERVICE\_INIT\_FAILURE**
</dt> <dd> <dl> <dt>

3221225501 (0xC000001D)
</dt> <dt>



Error number %1 was returned in trying to initialize Windows Management Instrumentation Service. This could be due to a badly installed version of WMI, WMI repository upgrade failure, insufficient disk space or insufficient memory.


</dt> </dl> </dd> <dt>

<span id="WBEM_MC_WBEM_REPOSITORY_RECREATED"></span><span id="wbem_mc_wbem_repository_recreated"></span>**WBEM\_MC\_WBEM\_REPOSITORY\_RECREATED**
</dt> <dd> <dl> <dt>

3221231088 (0xC00015F0)
</dt> <dt>



Windows Management Instrumentation Repository successfully recreated using Autorecovery mechanism.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



## See also

<dl> <dt>

[WMI Events](wmi-events.md)
</dt> <dt>

[WMI Troubleshooting](wmi-troubleshooting.md)
</dt> </dl>

 

 





---
description: Describes error codes 1000-1299 defined in the WinError.h header file and is intended for developers.
ms.assetid: 0061feb6-e1a0-4fcd-8f80-954087c799d7
title: System Error Codes (1000-1299) (WinError.h)
ms.topic: reference
ms.date: 07/15/2024
---

# System Error Codes (1000-1299)

The following list describes [system error codes](system-error-codes.md) for errors 1000 to 1299. They are returned by the [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) function when many functions fail. To retrieve the description text for the error in your application, use the [**FormatMessage**](/windows/desktop/api/WinBase/nf-winbase-formatmessage) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag.

> [!NOTE]
> This information is intended for developers debugging system errors. For other errors, such as issues with Windows Update, see the list of resources on the [Error codes](system-error-codes.md) page.

 

<span id="ERROR_STACK_OVERFLOW"></span><span id="error_stack_overflow"></span>**ERROR\_STACK\_OVERFLOW**
   

1001 (0x3E9)
 



Recursion too deep; the stack overflowed.


   

<span id="ERROR_INVALID_MESSAGE"></span><span id="error_invalid_message"></span>**ERROR\_INVALID\_MESSAGE**
   

1002 (0x3EA)
 



The window cannot act on the sent message.


   

<span id="ERROR_CAN_NOT_COMPLETE"></span><span id="error_can_not_complete"></span>**ERROR\_CAN\_NOT\_COMPLETE**
   

1003 (0x3EB)
 



Cannot complete this function.


   

<span id="ERROR_INVALID_FLAGS"></span><span id="error_invalid_flags"></span>**ERROR\_INVALID\_FLAGS**
   

1004 (0x3EC)
 



Invalid flags.


   

<span id="ERROR_UNRECOGNIZED_VOLUME"></span><span id="error_unrecognized_volume"></span>**ERROR\_UNRECOGNIZED\_VOLUME**
   

1005 (0x3ED)
 



The volume does not contain a recognized file system. Please make sure that all required file system drivers are loaded and that the volume is not corrupted.


   

<span id="ERROR_FILE_INVALID"></span><span id="error_file_invalid"></span>**ERROR\_FILE\_INVALID**
   

1006 (0x3EE)
 



The volume for a file has been externally altered so that the opened file is no longer valid.


   

<span id="ERROR_FULLSCREEN_MODE"></span><span id="error_fullscreen_mode"></span>**ERROR\_FULLSCREEN\_MODE**
   

1007 (0x3EF)
 



The requested operation cannot be performed in full-screen mode.


   

<span id="ERROR_NO_TOKEN"></span><span id="error_no_token"></span>**ERROR\_NO\_TOKEN**
   

1008 (0x3F0)
 



An attempt was made to reference a token that does not exist.


   

<span id="ERROR_BADDB"></span><span id="error_baddb"></span>**ERROR\_BADDB**
   

1009 (0x3F1)
 



The configuration registry database is corrupt.


   

<span id="ERROR_BADKEY"></span><span id="error_badkey"></span>**ERROR\_BADKEY**
   

1010 (0x3F2)
 



The configuration registry key is invalid.


   

<span id="ERROR_CANTOPEN"></span><span id="error_cantopen"></span>**ERROR\_CANTOPEN**
   

1011 (0x3F3)
 



The configuration registry key could not be opened.


   

<span id="ERROR_CANTREAD"></span><span id="error_cantread"></span>**ERROR\_CANTREAD**
   

1012 (0x3F4)
 



The configuration registry key could not be read.


   

<span id="ERROR_CANTWRITE"></span><span id="error_cantwrite"></span>**ERROR\_CANTWRITE**
   

1013 (0x3F5)
 



The configuration registry key could not be written.


   

<span id="ERROR_REGISTRY_RECOVERED"></span><span id="error_registry_recovered"></span>**ERROR\_REGISTRY\_RECOVERED**
   

1014 (0x3F6)
 



One of the files in the registry database had to be recovered by use of a log or alternate copy. The recovery was successful.


   

<span id="ERROR_REGISTRY_CORRUPT"></span><span id="error_registry_corrupt"></span>**ERROR\_REGISTRY\_CORRUPT**
   

1015 (0x3F7)
 



The registry is corrupted. The structure of one of the files containing registry data is corrupted, or the system's memory image of the file is corrupted, or the file could not be recovered because the alternate copy or log was absent or corrupted.


   

<span id="ERROR_REGISTRY_IO_FAILED"></span><span id="error_registry_io_failed"></span>**ERROR\_REGISTRY\_IO\_FAILED**
   

1016 (0x3F8)
 



An I/O operation initiated by the registry failed unrecoverably. The registry could not read in, or write out, or flush, one of the files that contain the system's image of the registry.


   

<span id="ERROR_NOT_REGISTRY_FILE"></span><span id="error_not_registry_file"></span>**ERROR\_NOT\_REGISTRY\_FILE**
   

1017 (0x3F9)
 



The system has attempted to load or restore a file into the registry, but the specified file is not in a registry file format.


   

<span id="ERROR_KEY_DELETED"></span><span id="error_key_deleted"></span>**ERROR\_KEY\_DELETED**
   

1018 (0x3FA)
 



Illegal operation attempted on a registry key that has been marked for deletion.


   

<span id="ERROR_NO_LOG_SPACE"></span><span id="error_no_log_space"></span>**ERROR\_NO\_LOG\_SPACE**
   

1019 (0x3FB)
 



System could not allocate the required space in a registry log.


   

<span id="ERROR_KEY_HAS_CHILDREN"></span><span id="error_key_has_children"></span>**ERROR\_KEY\_HAS\_CHILDREN**
   

1020 (0x3FC)
 



Cannot create a symbolic link in a registry key that already has subkeys or values.


   

<span id="ERROR_CHILD_MUST_BE_VOLATILE"></span><span id="error_child_must_be_volatile"></span>**ERROR\_CHILD\_MUST\_BE\_VOLATILE**
   

1021 (0x3FD)
 



Cannot create a stable subkey under a volatile parent key.


   

<span id="ERROR_NOTIFY_ENUM_DIR"></span><span id="error_notify_enum_dir"></span>**ERROR\_NOTIFY\_ENUM\_DIR**
   

1022 (0x3FE)
 



A notify change request is being completed and the information is not being returned in the caller's buffer. The caller now needs to enumerate the files to find the changes.


   

<span id="ERROR_DEPENDENT_SERVICES_RUNNING"></span><span id="error_dependent_services_running"></span>**ERROR\_DEPENDENT\_SERVICES\_RUNNING**
   

1051 (0x41B)
 



A stop control has been sent to a service that other running services are dependent on.


   

<span id="ERROR_INVALID_SERVICE_CONTROL"></span><span id="error_invalid_service_control"></span>**ERROR\_INVALID\_SERVICE\_CONTROL**
   

1052 (0x41C)
 



The requested control is not valid for this service.


   

<span id="ERROR_SERVICE_REQUEST_TIMEOUT"></span><span id="error_service_request_timeout"></span>**ERROR\_SERVICE\_REQUEST\_TIMEOUT**
   

1053 (0x41D)
 



The service did not respond to the start or control request in a timely fashion.


   

<span id="ERROR_SERVICE_NO_THREAD"></span><span id="error_service_no_thread"></span>**ERROR\_SERVICE\_NO\_THREAD**
   

1054 (0x41E)
 



A thread could not be created for the service.


   

<span id="ERROR_SERVICE_DATABASE_LOCKED"></span><span id="error_service_database_locked"></span>**ERROR\_SERVICE\_DATABASE\_LOCKED**
   

1055 (0x41F)
 



The service database is locked.


   

<span id="ERROR_SERVICE_ALREADY_RUNNING"></span><span id="error_service_already_running"></span>**ERROR\_SERVICE\_ALREADY\_RUNNING**
   

1056 (0x420)
 



An instance of the service is already running.


   

<span id="ERROR_INVALID_SERVICE_ACCOUNT"></span><span id="error_invalid_service_account"></span>**ERROR\_INVALID\_SERVICE\_ACCOUNT**
   

1057 (0x421)
 



The account name is invalid or does not exist, or the password is invalid for the account name specified.


   

<span id="ERROR_SERVICE_DISABLED"></span><span id="error_service_disabled"></span>**ERROR\_SERVICE\_DISABLED**
   

1058 (0x422)
 



The service cannot be started, either because it is disabled or because it has no enabled devices associated with it.


   

<span id="ERROR_CIRCULAR_DEPENDENCY"></span><span id="error_circular_dependency"></span>**ERROR\_CIRCULAR\_DEPENDENCY**
   

1059 (0x423)
 



Circular service dependency was specified.


   

<span id="ERROR_SERVICE_DOES_NOT_EXIST"></span><span id="error_service_does_not_exist"></span>**ERROR\_SERVICE\_DOES\_NOT\_EXIST**
   

1060 (0x424)
 



The specified service does not exist as an installed service.


   

<span id="ERROR_SERVICE_CANNOT_ACCEPT_CTRL"></span><span id="error_service_cannot_accept_ctrl"></span>**ERROR\_SERVICE\_CANNOT\_ACCEPT\_CTRL**
   

1061 (0x425)
 



The service cannot accept control messages at this time.


   

<span id="ERROR_SERVICE_NOT_ACTIVE"></span><span id="error_service_not_active"></span>**ERROR\_SERVICE\_NOT\_ACTIVE**
   

1062 (0x426)
 



The service has not been started.


   

<span id="ERROR_FAILED_SERVICE_CONTROLLER_CONNECT"></span><span id="error_failed_service_controller_connect"></span>**ERROR\_FAILED\_SERVICE\_CONTROLLER\_CONNECT**
   

1063 (0x427)
 



The service process could not connect to the service controller.


   

<span id="ERROR_EXCEPTION_IN_SERVICE"></span><span id="error_exception_in_service"></span>**ERROR\_EXCEPTION\_IN\_SERVICE**
   

1064 (0x428)
 



An exception occurred in the service when handling the control request.


   

<span id="ERROR_DATABASE_DOES_NOT_EXIST"></span><span id="error_database_does_not_exist"></span>**ERROR\_DATABASE\_DOES\_NOT\_EXIST**
   

1065 (0x429)
 



The database specified does not exist.


   

<span id="ERROR_SERVICE_SPECIFIC_ERROR"></span><span id="error_service_specific_error"></span>**ERROR\_SERVICE\_SPECIFIC\_ERROR**
   

1066 (0x42A)
 



The service has returned a service-specific error code.


   

<span id="ERROR_PROCESS_ABORTED"></span><span id="error_process_aborted"></span>**ERROR\_PROCESS\_ABORTED**
   

1067 (0x42B)
 



The process terminated unexpectedly.


   

<span id="ERROR_SERVICE_DEPENDENCY_FAIL"></span><span id="error_service_dependency_fail"></span>**ERROR\_SERVICE\_DEPENDENCY\_FAIL**
   

1068 (0x42C)
 



The dependency service or group failed to start.


   

<span id="ERROR_SERVICE_LOGON_FAILED"></span><span id="error_service_logon_failed"></span>**ERROR\_SERVICE\_LOGON\_FAILED**
   

1069 (0x42D)
 



The service did not start due to a logon failure.


   

<span id="ERROR_SERVICE_START_HANG"></span><span id="error_service_start_hang"></span>**ERROR\_SERVICE\_START\_HANG**
   

1070 (0x42E)
 



After starting, the service hung in a start-pending state.


   

<span id="ERROR_INVALID_SERVICE_LOCK"></span><span id="error_invalid_service_lock"></span>**ERROR\_INVALID\_SERVICE\_LOCK**
   

1071 (0x42F)
 



The specified service database lock is invalid.


   

<span id="ERROR_SERVICE_MARKED_FOR_DELETE"></span><span id="error_service_marked_for_delete"></span>**ERROR\_SERVICE\_MARKED\_FOR\_DELETE**
   

1072 (0x430)
 



The specified service has been marked for deletion.


   

<span id="ERROR_SERVICE_EXISTS"></span><span id="error_service_exists"></span>**ERROR\_SERVICE\_EXISTS**
   

1073 (0x431)
 



The specified service already exists.


   

<span id="ERROR_ALREADY_RUNNING_LKG"></span><span id="error_already_running_lkg"></span>**ERROR\_ALREADY\_RUNNING\_LKG**
   

1074 (0x432)
 



The system is currently running with the last-known-good configuration.


   

<span id="ERROR_SERVICE_DEPENDENCY_DELETED"></span><span id="error_service_dependency_deleted"></span>**ERROR\_SERVICE\_DEPENDENCY\_DELETED**
   

1075 (0x433)
 



The dependency service does not exist or has been marked for deletion.


   

<span id="ERROR_BOOT_ALREADY_ACCEPTED"></span><span id="error_boot_already_accepted"></span>**ERROR\_BOOT\_ALREADY\_ACCEPTED**
   

1076 (0x434)
 



The current boot has already been accepted for use as the last-known-good control set.


   

<span id="ERROR_SERVICE_NEVER_STARTED"></span><span id="error_service_never_started"></span>**ERROR\_SERVICE\_NEVER\_STARTED**
   

1077 (0x435)
 



No attempts to start the service have been made since the last boot.


   

<span id="ERROR_DUPLICATE_SERVICE_NAME"></span><span id="error_duplicate_service_name"></span>**ERROR\_DUPLICATE\_SERVICE\_NAME**
   

1078 (0x436)
 



The name is already in use as either a service name or a service display name.


   

<span id="ERROR_DIFFERENT_SERVICE_ACCOUNT"></span><span id="error_different_service_account"></span>**ERROR\_DIFFERENT\_SERVICE\_ACCOUNT**
   

1079 (0x437)
 



The account specified for this service is different from the account specified for other services running in the same process.


   

<span id="ERROR_CANNOT_DETECT_DRIVER_FAILURE"></span><span id="error_cannot_detect_driver_failure"></span>**ERROR\_CANNOT\_DETECT\_DRIVER\_FAILURE**
   

1080 (0x438)
 



Failure actions can only be set for Win32 services, not for drivers.


   

<span id="ERROR_CANNOT_DETECT_PROCESS_ABORT"></span><span id="error_cannot_detect_process_abort"></span>**ERROR\_CANNOT\_DETECT\_PROCESS\_ABORT**
   

1081 (0x439)
 



This service runs in the same process as the service control manager. Therefore, the service control manager cannot take action if this service's process terminates unexpectedly.


   

<span id="ERROR_NO_RECOVERY_PROGRAM"></span><span id="error_no_recovery_program"></span>**ERROR\_NO\_RECOVERY\_PROGRAM**
   

1082 (0x43A)
 



No recovery program has been configured for this service.


   

<span id="ERROR_SERVICE_NOT_IN_EXE"></span><span id="error_service_not_in_exe"></span>**ERROR\_SERVICE\_NOT\_IN\_EXE**
   

1083 (0x43B)
 



The executable program that this service is configured to run in does not implement the service.


   

<span id="ERROR_NOT_SAFEBOOT_SERVICE"></span><span id="error_not_safeboot_service"></span>**ERROR\_NOT\_SAFEBOOT\_SERVICE**
   

1084 (0x43C)
 



This service cannot be started in Safe Mode.


   

<span id="ERROR_END_OF_MEDIA"></span><span id="error_end_of_media"></span>**ERROR\_END\_OF\_MEDIA**
   

1100 (0x44C)
 



The physical end of the tape has been reached.


   

<span id="ERROR_FILEMARK_DETECTED"></span><span id="error_filemark_detected"></span>**ERROR\_FILEMARK\_DETECTED**
   

1101 (0x44D)
 



A tape access reached a filemark.


   

<span id="ERROR_BEGINNING_OF_MEDIA"></span><span id="error_beginning_of_media"></span>**ERROR\_BEGINNING\_OF\_MEDIA**
   

1102 (0x44E)
 



The beginning of the tape or a partition was encountered.


   

<span id="ERROR_SETMARK_DETECTED"></span><span id="error_setmark_detected"></span>**ERROR\_SETMARK\_DETECTED**
   

1103 (0x44F)
 



A tape access reached the end of a set of files.


   

<span id="ERROR_NO_DATA_DETECTED"></span><span id="error_no_data_detected"></span>**ERROR\_NO\_DATA\_DETECTED**
   

1104 (0x450)
 



No more data is on the tape.


   

<span id="ERROR_PARTITION_FAILURE"></span><span id="error_partition_failure"></span>**ERROR\_PARTITION\_FAILURE**
   

1105 (0x451)
 



Tape could not be partitioned.


   

<span id="ERROR_INVALID_BLOCK_LENGTH"></span><span id="error_invalid_block_length"></span>**ERROR\_INVALID\_BLOCK\_LENGTH**
   

1106 (0x452)
 



When accessing a new tape of a multivolume partition, the current block size is incorrect.


   

<span id="ERROR_DEVICE_NOT_PARTITIONED"></span><span id="error_device_not_partitioned"></span>**ERROR\_DEVICE\_NOT\_PARTITIONED**
   

1107 (0x453)
 



Tape partition information could not be found when loading a tape.


   

<span id="ERROR_UNABLE_TO_LOCK_MEDIA"></span><span id="error_unable_to_lock_media"></span>**ERROR\_UNABLE\_TO\_LOCK\_MEDIA**
   

1108 (0x454)
 



Unable to lock the media eject mechanism.


   

<span id="ERROR_UNABLE_TO_UNLOAD_MEDIA"></span><span id="error_unable_to_unload_media"></span>**ERROR\_UNABLE\_TO\_UNLOAD\_MEDIA**
   

1109 (0x455)
 



Unable to unload the media.


   

<span id="ERROR_MEDIA_CHANGED"></span><span id="error_media_changed"></span>**ERROR\_MEDIA\_CHANGED**
   

1110 (0x456)
 



The media in the drive may have changed.


   

<span id="ERROR_BUS_RESET"></span><span id="error_bus_reset"></span>**ERROR\_BUS\_RESET**
   

1111 (0x457)
 



The I/O bus was reset.


   

<span id="ERROR_NO_MEDIA_IN_DRIVE"></span><span id="error_no_media_in_drive"></span>**ERROR\_NO\_MEDIA\_IN\_DRIVE**
   

1112 (0x458)
 



No media in drive.


   

<span id="ERROR_NO_UNICODE_TRANSLATION"></span><span id="error_no_unicode_translation"></span>**ERROR\_NO\_UNICODE\_TRANSLATION**
   

1113 (0x459)
 



No mapping for the Unicode character exists in the target multi-byte code page.


   

<span id="ERROR_DLL_INIT_FAILED"></span><span id="error_dll_init_failed"></span>**ERROR\_DLL\_INIT\_FAILED**
   

1114 (0x45A)
 



A dynamic link library (DLL) initialization routine failed.


   

<span id="ERROR_SHUTDOWN_IN_PROGRESS"></span><span id="error_shutdown_in_progress"></span>**ERROR\_SHUTDOWN\_IN\_PROGRESS**
   

1115 (0x45B)
 



A system shutdown is in progress.


   

<span id="ERROR_NO_SHUTDOWN_IN_PROGRESS"></span><span id="error_no_shutdown_in_progress"></span>**ERROR\_NO\_SHUTDOWN\_IN\_PROGRESS**
   

1116 (0x45C)
 



Unable to abort the system shutdown because no shutdown was in progress.


   

<span id="ERROR_IO_DEVICE"></span><span id="error_io_device"></span>**ERROR\_IO\_DEVICE**
   

1117 (0x45D)
 



The request could not be performed because of an I/O device error.


   

<span id="ERROR_SERIAL_NO_DEVICE"></span><span id="error_serial_no_device"></span>**ERROR\_SERIAL\_NO\_DEVICE**
   

1118 (0x45E)
 



No serial device was successfully initialized. The serial driver will unload.


   

<span id="ERROR_IRQ_BUSY"></span><span id="error_irq_busy"></span>**ERROR\_IRQ\_BUSY**
   

1119 (0x45F)
 



Unable to open a device that was sharing an interrupt request (IRQ) with other devices. At least one other device that uses that IRQ was already opened.


   

<span id="ERROR_MORE_WRITES"></span><span id="error_more_writes"></span>**ERROR\_MORE\_WRITES**
   

1120 (0x460)
 



A serial I/O operation was completed by another write to the serial port. The IOCTL\_SERIAL\_XOFF\_COUNTER reached zero.)


   

<span id="ERROR_COUNTER_TIMEOUT"></span><span id="error_counter_timeout"></span>**ERROR\_COUNTER\_TIMEOUT**
   

1121 (0x461)
 



A serial I/O operation completed because the timeout period expired. The IOCTL\_SERIAL\_XOFF\_COUNTER did not reach zero.)


   

<span id="ERROR_FLOPPY_ID_MARK_NOT_FOUND"></span><span id="error_floppy_id_mark_not_found"></span>**ERROR\_FLOPPY\_ID\_MARK\_NOT\_FOUND**
   

1122 (0x462)
 



No ID address mark was found on the floppy disk.


   

<span id="ERROR_FLOPPY_WRONG_CYLINDER"></span><span id="error_floppy_wrong_cylinder"></span>**ERROR\_FLOPPY\_WRONG\_CYLINDER**
   

1123 (0x463)
 



Mismatch between the floppy disk sector ID field and the floppy disk controller track address.


   

<span id="ERROR_FLOPPY_UNKNOWN_ERROR"></span><span id="error_floppy_unknown_error"></span>**ERROR\_FLOPPY\_UNKNOWN\_ERROR**
   

1124 (0x464)
 



The floppy disk controller reported an error that is not recognized by the floppy disk driver.


   

<span id="ERROR_FLOPPY_BAD_REGISTERS"></span><span id="error_floppy_bad_registers"></span>**ERROR\_FLOPPY\_BAD\_REGISTERS**
   

1125 (0x465)
 



The floppy disk controller returned inconsistent results in its registers.


   

<span id="ERROR_DISK_RECALIBRATE_FAILED"></span><span id="error_disk_recalibrate_failed"></span>**ERROR\_DISK\_RECALIBRATE\_FAILED**
   

1126 (0x466)
 



While accessing the hard disk, a recalibrate operation failed, even after retries.


   

<span id="ERROR_DISK_OPERATION_FAILED"></span><span id="error_disk_operation_failed"></span>**ERROR\_DISK\_OPERATION\_FAILED**
   

1127 (0x467)
 



While accessing the hard disk, a disk operation failed even after retries.


   

<span id="ERROR_DISK_RESET_FAILED"></span><span id="error_disk_reset_failed"></span>**ERROR\_DISK\_RESET\_FAILED**
   

1128 (0x468)
 



While accessing the hard disk, a disk controller reset was needed, but even that failed.


   

<span id="ERROR_EOM_OVERFLOW"></span><span id="error_eom_overflow"></span>**ERROR\_EOM\_OVERFLOW**
   

1129 (0x469)
 



Physical end of tape encountered.


   

<span id="ERROR_NOT_ENOUGH_SERVER_MEMORY"></span><span id="error_not_enough_server_memory"></span>**ERROR\_NOT\_ENOUGH\_SERVER\_MEMORY**
   

1130 (0x46A)
 



Not enough server storage is available to process this command.


   

<span id="ERROR_POSSIBLE_DEADLOCK"></span><span id="error_possible_deadlock"></span>**ERROR\_POSSIBLE\_DEADLOCK**
   

1131 (0x46B)
 



A potential deadlock condition has been detected.


   

<span id="ERROR_MAPPED_ALIGNMENT"></span><span id="error_mapped_alignment"></span>**ERROR\_MAPPED\_ALIGNMENT**
   

1132 (0x46C)
 



The base address or the file offset specified does not have the proper alignment.


   

<span id="ERROR_SET_POWER_STATE_VETOED"></span><span id="error_set_power_state_vetoed"></span>**ERROR\_SET\_POWER\_STATE\_VETOED**
   

1140 (0x474)
 



An attempt to change the system power state was vetoed by another application or driver.


   

<span id="ERROR_SET_POWER_STATE_FAILED"></span><span id="error_set_power_state_failed"></span>**ERROR\_SET\_POWER\_STATE\_FAILED**
   

1141 (0x475)
 



The system BIOS failed an attempt to change the system power state.


   

<span id="ERROR_TOO_MANY_LINKS"></span><span id="error_too_many_links"></span>**ERROR\_TOO\_MANY\_LINKS**
   

1142 (0x476)
 



An attempt was made to create more links on a file than the file system supports.


   

<span id="ERROR_OLD_WIN_VERSION"></span><span id="error_old_win_version"></span>**ERROR\_OLD\_WIN\_VERSION**
   

1150 (0x47E)
 



The specified program requires a newer version of Windows.


   

<span id="ERROR_APP_WRONG_OS"></span><span id="error_app_wrong_os"></span>**ERROR\_APP\_WRONG\_OS**
   

1151 (0x47F)
 



The specified program is not a Windows or MS-DOS program.


   

<span id="ERROR_SINGLE_INSTANCE_APP"></span><span id="error_single_instance_app"></span>**ERROR\_SINGLE\_INSTANCE\_APP**
   

1152 (0x480)
 



Cannot start more than one instance of the specified program.


   

<span id="ERROR_RMODE_APP"></span><span id="error_rmode_app"></span>**ERROR\_RMODE\_APP**
   

1153 (0x481)
 



The specified program was written for an earlier version of Windows.


   

<span id="ERROR_INVALID_DLL"></span><span id="error_invalid_dll"></span>**ERROR\_INVALID\_DLL**
   

1154 (0x482)
 



One of the library files needed to run this application is damaged.


   

<span id="ERROR_NO_ASSOCIATION"></span><span id="error_no_association"></span>**ERROR\_NO\_ASSOCIATION**
   

1155 (0x483)
 



No application is associated with the specified file for this operation.


   

<span id="ERROR_DDE_FAIL"></span><span id="error_dde_fail"></span>**ERROR\_DDE\_FAIL**
   

1156 (0x484)
 



An error occurred in sending the command to the application.


   

<span id="ERROR_DLL_NOT_FOUND"></span><span id="error_dll_not_found"></span>**ERROR\_DLL\_NOT\_FOUND**
   

1157 (0x485)
 



One of the library files needed to run this application cannot be found.


   

<span id="ERROR_NO_MORE_USER_HANDLES"></span><span id="error_no_more_user_handles"></span>**ERROR\_NO\_MORE\_USER\_HANDLES**
   

1158 (0x486)
 



The current process has used all of its system allowance of handles for Window Manager objects.


   

<span id="ERROR_MESSAGE_SYNC_ONLY"></span><span id="error_message_sync_only"></span>**ERROR\_MESSAGE\_SYNC\_ONLY**
   

1159 (0x487)
 



The message can be used only with synchronous operations.


   

<span id="ERROR_SOURCE_ELEMENT_EMPTY"></span><span id="error_source_element_empty"></span>**ERROR\_SOURCE\_ELEMENT\_EMPTY**
   

1160 (0x488)
 



The indicated source element has no media.


   

<span id="ERROR_DESTINATION_ELEMENT_FULL"></span><span id="error_destination_element_full"></span>**ERROR\_DESTINATION\_ELEMENT\_FULL**
   

1161 (0x489)
 



The indicated destination element already contains media.


   

<span id="ERROR_ILLEGAL_ELEMENT_ADDRESS"></span><span id="error_illegal_element_address"></span>**ERROR\_ILLEGAL\_ELEMENT\_ADDRESS**
   

1162 (0x48A)
 



The indicated element does not exist.


   

<span id="ERROR_MAGAZINE_NOT_PRESENT"></span><span id="error_magazine_not_present"></span>**ERROR\_MAGAZINE\_NOT\_PRESENT**
   

1163 (0x48B)
 



The indicated element is part of a magazine that is not present.


   

<span id="ERROR_DEVICE_REINITIALIZATION_NEEDED"></span><span id="error_device_reinitialization_needed"></span>**ERROR\_DEVICE\_REINITIALIZATION\_NEEDED**
   

1164 (0x48C)
 



The indicated device requires reinitialization due to hardware errors.


   

<span id="ERROR_DEVICE_REQUIRES_CLEANING"></span><span id="error_device_requires_cleaning"></span>**ERROR\_DEVICE\_REQUIRES\_CLEANING**
   

1165 (0x48D)
 



The device has indicated that cleaning is required before further operations are attempted.


   

<span id="ERROR_DEVICE_DOOR_OPEN"></span><span id="error_device_door_open"></span>**ERROR\_DEVICE\_DOOR\_OPEN**
   

1166 (0x48E)
 



The device has indicated that its door is open.


   

<span id="ERROR_DEVICE_NOT_CONNECTED"></span><span id="error_device_not_connected"></span>**ERROR\_DEVICE\_NOT\_CONNECTED**
   

1167 (0x48F)
 



The device is not connected.


   

<span id="ERROR_NOT_FOUND"></span><span id="error_not_found"></span>**ERROR\_NOT\_FOUND**
   

1168 (0x490)
 



Element not found.


   

<span id="ERROR_NO_MATCH"></span><span id="error_no_match"></span>**ERROR\_NO\_MATCH**
   

1169 (0x491)
 



There was no match for the specified key in the index.


   

<span id="ERROR_SET_NOT_FOUND"></span><span id="error_set_not_found"></span>**ERROR\_SET\_NOT\_FOUND**
   

1170 (0x492)
 



The property set specified does not exist on the object.


   

<span id="ERROR_POINT_NOT_FOUND"></span><span id="error_point_not_found"></span>**ERROR\_POINT\_NOT\_FOUND**
   

1171 (0x493)
 



The point passed to GetMouseMovePoints is not in the buffer.


   

<span id="ERROR_NO_TRACKING_SERVICE"></span><span id="error_no_tracking_service"></span>**ERROR\_NO\_TRACKING\_SERVICE**
   

1172 (0x494)
 



The tracking (workstation) service is not running.


   

<span id="ERROR_NO_VOLUME_ID"></span><span id="error_no_volume_id"></span>**ERROR\_NO\_VOLUME\_ID**
   

1173 (0x495)
 



The Volume ID could not be found.


   

<span id="ERROR_UNABLE_TO_REMOVE_REPLACED"></span><span id="error_unable_to_remove_replaced"></span>**ERROR\_UNABLE\_TO\_REMOVE\_REPLACED**
   

1175 (0x497)
 



Unable to remove the file to be replaced.


   

<span id="ERROR_UNABLE_TO_MOVE_REPLACEMENT"></span><span id="error_unable_to_move_replacement"></span>**ERROR\_UNABLE\_TO\_MOVE\_REPLACEMENT**
   

1176 (0x498)
 



Unable to move the replacement file to the file to be replaced. The file to be replaced has retained its original name.


   

<span id="ERROR_UNABLE_TO_MOVE_REPLACEMENT_2"></span><span id="error_unable_to_move_replacement_2"></span>**ERROR\_UNABLE\_TO\_MOVE\_REPLACEMENT\_2**
   

1177 (0x499)
 



Unable to move the replacement file to the file to be replaced. The file to be replaced has been renamed using the backup name.


   

<span id="ERROR_JOURNAL_DELETE_IN_PROGRESS"></span><span id="error_journal_delete_in_progress"></span>**ERROR\_JOURNAL\_DELETE\_IN\_PROGRESS**
   

1178 (0x49A)
 



The volume change journal is being deleted.


   

<span id="ERROR_JOURNAL_NOT_ACTIVE"></span><span id="error_journal_not_active"></span>**ERROR\_JOURNAL\_NOT\_ACTIVE**
   

1179 (0x49B)
 



The volume change journal is not active.


   

<span id="ERROR_POTENTIAL_FILE_FOUND"></span><span id="error_potential_file_found"></span>**ERROR\_POTENTIAL\_FILE\_FOUND**
   

1180 (0x49C)
 



A file was found, but it may not be the correct file.


   

<span id="ERROR_JOURNAL_ENTRY_DELETED"></span><span id="error_journal_entry_deleted"></span>**ERROR\_JOURNAL\_ENTRY\_DELETED**
   

1181 (0x49D)
 



The journal entry has been deleted from the journal.


   

<span id="ERROR_SHUTDOWN_IS_SCHEDULED"></span><span id="error_shutdown_is_scheduled"></span>**ERROR\_SHUTDOWN\_IS\_SCHEDULED**
   

1190 (0x4A6)
 



A system shutdown has already been scheduled.


   

<span id="ERROR_SHUTDOWN_USERS_LOGGED_ON"></span><span id="error_shutdown_users_logged_on"></span>**ERROR\_SHUTDOWN\_USERS\_LOGGED\_ON**
   

1191 (0x4A7)
 



The system shutdown cannot be initiated because there are other users logged on to the computer.


   

<span id="ERROR_BAD_DEVICE"></span><span id="error_bad_device"></span>**ERROR\_BAD\_DEVICE**
   

1200 (0x4B0)
 



The specified device name is invalid.


   

<span id="ERROR_CONNECTION_UNAVAIL"></span><span id="error_connection_unavail"></span>**ERROR\_CONNECTION\_UNAVAIL**
   

1201 (0x4B1)
 



The device is not currently connected but it is a remembered connection.


   

<span id="ERROR_DEVICE_ALREADY_REMEMBERED"></span><span id="error_device_already_remembered"></span>**ERROR\_DEVICE\_ALREADY\_REMEMBERED**
   

1202 (0x4B2)
 



The local device name has a remembered connection to another network resource.


   

<span id="ERROR_NO_NET_OR_BAD_PATH"></span><span id="error_no_net_or_bad_path"></span>**ERROR\_NO\_NET\_OR\_BAD\_PATH**
   

1203 (0x4B3)
 



The network path was either typed incorrectly, does not exist, or the network provider is not currently available. Please try retyping the path or contact your network administrator.


   

<span id="ERROR_BAD_PROVIDER"></span><span id="error_bad_provider"></span>**ERROR\_BAD\_PROVIDER**
   

1204 (0x4B4)
 



The specified network provider name is invalid.


   

<span id="ERROR_CANNOT_OPEN_PROFILE"></span><span id="error_cannot_open_profile"></span>**ERROR\_CANNOT\_OPEN\_PROFILE**
   

1205 (0x4B5)
 



Unable to open the network connection profile.


   

<span id="ERROR_BAD_PROFILE"></span><span id="error_bad_profile"></span>**ERROR\_BAD\_PROFILE**
   

1206 (0x4B6)
 



The network connection profile is corrupted.


   

<span id="ERROR_NOT_CONTAINER"></span><span id="error_not_container"></span>**ERROR\_NOT\_CONTAINER**
   

1207 (0x4B7)
 



Cannot enumerate a noncontainer.


   

<span id="ERROR_EXTENDED_ERROR"></span><span id="error_extended_error"></span>**ERROR\_EXTENDED\_ERROR**
   

1208 (0x4B8)
 



An extended error has occurred.


   

<span id="ERROR_INVALID_GROUPNAME"></span><span id="error_invalid_groupname"></span>**ERROR\_INVALID\_GROUPNAME**
   

1209 (0x4B9)
 



The format of the specified group name is invalid.


   

<span id="ERROR_INVALID_COMPUTERNAME"></span><span id="error_invalid_computername"></span>**ERROR\_INVALID\_COMPUTERNAME**
   

1210 (0x4BA)
 



The format of the specified computer name is invalid.


   

<span id="ERROR_INVALID_EVENTNAME"></span><span id="error_invalid_eventname"></span>**ERROR\_INVALID\_EVENTNAME**
   

1211 (0x4BB)
 



The format of the specified event name is invalid.


   

<span id="ERROR_INVALID_DOMAINNAME"></span><span id="error_invalid_domainname"></span>**ERROR\_INVALID\_DOMAINNAME**
   

1212 (0x4BC)
 



The format of the specified domain name is invalid.


   

<span id="ERROR_INVALID_SERVICENAME"></span><span id="error_invalid_servicename"></span>**ERROR\_INVALID\_SERVICENAME**
   

1213 (0x4BD)
 



The format of the specified service name is invalid.


   

<span id="ERROR_INVALID_NETNAME"></span><span id="error_invalid_netname"></span>**ERROR\_INVALID\_NETNAME**
   

1214 (0x4BE)
 



The format of the specified network name is invalid.


   

<span id="ERROR_INVALID_SHARENAME"></span><span id="error_invalid_sharename"></span>**ERROR\_INVALID\_SHARENAME**
   

1215 (0x4BF)
 



The format of the specified share name is invalid.


   

<span id="ERROR_INVALID_PASSWORDNAME"></span><span id="error_invalid_passwordname"></span>**ERROR\_INVALID\_PASSWORDNAME**
   

1216 (0x4C0)
 



The format of the specified password is invalid.


   

<span id="ERROR_INVALID_MESSAGENAME"></span><span id="error_invalid_messagename"></span>**ERROR\_INVALID\_MESSAGENAME**
   

1217 (0x4C1)
 



The format of the specified message name is invalid.


   

<span id="ERROR_INVALID_MESSAGEDEST"></span><span id="error_invalid_messagedest"></span>**ERROR\_INVALID\_MESSAGEDEST**
   

1218 (0x4C2)
 



The format of the specified message destination is invalid.


   

<span id="ERROR_SESSION_CREDENTIAL_CONFLICT"></span><span id="error_session_credential_conflict"></span>**ERROR\_SESSION\_CREDENTIAL\_CONFLICT**
   

1219 (0x4C3)
 



Multiple connections to a server or shared resource by the same user, using more than one user name, are not allowed. Disconnect all previous connections to the server or shared resource and try again.


   

<span id="ERROR_REMOTE_SESSION_LIMIT_EXCEEDED"></span><span id="error_remote_session_limit_exceeded"></span>**ERROR\_REMOTE\_SESSION\_LIMIT\_EXCEEDED**
   

1220 (0x4C4)
 



An attempt was made to establish a session to a network server, but there are already too many sessions established to that server.


   

<span id="ERROR_DUP_DOMAINNAME"></span><span id="error_dup_domainname"></span>**ERROR\_DUP\_DOMAINNAME**
   

1221 (0x4C5)
 



The workgroup or domain name is already in use by another computer on the network.


   

<span id="ERROR_NO_NETWORK"></span><span id="error_no_network"></span>**ERROR\_NO\_NETWORK**
   

1222 (0x4C6)
 



The network is not present or not started.


   

<span id="ERROR_CANCELLED"></span><span id="error_cancelled"></span>**ERROR\_CANCELLED**
   

1223 (0x4C7)
 



The operation was canceled by the user.


   

<span id="ERROR_USER_MAPPED_FILE"></span><span id="error_user_mapped_file"></span>**ERROR\_USER\_MAPPED\_FILE**
   

1224 (0x4C8)
 



The requested operation cannot be performed on a file with a user-mapped section open.


   

<span id="ERROR_CONNECTION_REFUSED"></span><span id="error_connection_refused"></span>**ERROR\_CONNECTION\_REFUSED**
   

1225 (0x4C9)
 



The remote computer refused the network connection.


   

<span id="ERROR_GRACEFUL_DISCONNECT"></span><span id="error_graceful_disconnect"></span>**ERROR\_GRACEFUL\_DISCONNECT**
   

1226 (0x4CA)
 



The network connection was gracefully closed.


   

<span id="ERROR_ADDRESS_ALREADY_ASSOCIATED"></span><span id="error_address_already_associated"></span>**ERROR\_ADDRESS\_ALREADY\_ASSOCIATED**
   

1227 (0x4CB)
 



The network transport endpoint already has an address associated with it.


   

<span id="ERROR_ADDRESS_NOT_ASSOCIATED"></span><span id="error_address_not_associated"></span>**ERROR\_ADDRESS\_NOT\_ASSOCIATED**
   

1228 (0x4CC)
 



An address has not yet been associated with the network endpoint.


   

<span id="ERROR_CONNECTION_INVALID"></span><span id="error_connection_invalid"></span>**ERROR\_CONNECTION\_INVALID**
   

1229 (0x4CD)
 



An operation was attempted on a nonexistent network connection.


   

<span id="ERROR_CONNECTION_ACTIVE"></span><span id="error_connection_active"></span>**ERROR\_CONNECTION\_ACTIVE**
   

1230 (0x4CE)
 



An invalid operation was attempted on an active network connection.


   

<span id="ERROR_NETWORK_UNREACHABLE"></span><span id="error_network_unreachable"></span>**ERROR\_NETWORK\_UNREACHABLE**
   

1231 (0x4CF)
 



The network location cannot be reached. For information about network troubleshooting, see Windows Help.


   

<span id="ERROR_HOST_UNREACHABLE"></span><span id="error_host_unreachable"></span>**ERROR\_HOST\_UNREACHABLE**
   

1232 (0x4D0)
 



The network location cannot be reached. For information about network troubleshooting, see Windows Help.


   

<span id="ERROR_PROTOCOL_UNREACHABLE"></span><span id="error_protocol_unreachable"></span>**ERROR\_PROTOCOL\_UNREACHABLE**
   

1233 (0x4D1)
 



The network location cannot be reached. For information about network troubleshooting, see Windows Help.


   

<span id="ERROR_PORT_UNREACHABLE"></span><span id="error_port_unreachable"></span>**ERROR\_PORT\_UNREACHABLE**
   

1234 (0x4D2)
 



No service is operating at the destination network endpoint on the remote system.


   

<span id="ERROR_REQUEST_ABORTED"></span><span id="error_request_aborted"></span>**ERROR\_REQUEST\_ABORTED**
   

1235 (0x4D3)
 



The request was aborted.


   

<span id="ERROR_CONNECTION_ABORTED"></span><span id="error_connection_aborted"></span>**ERROR\_CONNECTION\_ABORTED**
   

1236 (0x4D4)
 



The network connection was aborted by the local system.


   

<span id="ERROR_RETRY"></span><span id="error_retry"></span>**ERROR\_RETRY**
   

1237 (0x4D5)
 



The operation could not be completed. A retry should be performed.


   

<span id="ERROR_CONNECTION_COUNT_LIMIT"></span><span id="error_connection_count_limit"></span>**ERROR\_CONNECTION\_COUNT\_LIMIT**
   

1238 (0x4D6)
 



A connection to the server could not be made because the limit on the number of concurrent connections for this account has been reached.


   

<span id="ERROR_LOGIN_TIME_RESTRICTION"></span><span id="error_login_time_restriction"></span>**ERROR\_LOGIN\_TIME\_RESTRICTION**
   

1239 (0x4D7)
 



Attempting to log in during an unauthorized time of day for this account.


   

<span id="ERROR_LOGIN_WKSTA_RESTRICTION"></span><span id="error_login_wksta_restriction"></span>**ERROR\_LOGIN\_WKSTA\_RESTRICTION**
   

1240 (0x4D8)
 



The account is not authorized to log in from this station.


   

<span id="ERROR_INCORRECT_ADDRESS"></span><span id="error_incorrect_address"></span>**ERROR\_INCORRECT\_ADDRESS**
   

1241 (0x4D9)
 



The network address could not be used for the operation requested.


   

<span id="ERROR_ALREADY_REGISTERED"></span><span id="error_already_registered"></span>**ERROR\_ALREADY\_REGISTERED**
   

1242 (0x4DA)
 



The service is already registered.


   

<span id="ERROR_SERVICE_NOT_FOUND"></span><span id="error_service_not_found"></span>**ERROR\_SERVICE\_NOT\_FOUND**
   

1243 (0x4DB)
 



The specified service does not exist.


   

<span id="ERROR_NOT_AUTHENTICATED"></span><span id="error_not_authenticated"></span>**ERROR\_NOT\_AUTHENTICATED**
   

1244 (0x4DC)
 



The operation being requested was not performed because the user has not been authenticated.


   

<span id="ERROR_NOT_LOGGED_ON"></span><span id="error_not_logged_on"></span>**ERROR\_NOT\_LOGGED\_ON**
   

1245 (0x4DD)
 



The operation being requested was not performed because the user has not logged on to the network. The specified service does not exist.


   

<span id="ERROR_CONTINUE"></span><span id="error_continue"></span>**ERROR\_CONTINUE**
   

1246 (0x4DE)
 



Continue with work in progress.


   

<span id="ERROR_ALREADY_INITIALIZED"></span><span id="error_already_initialized"></span>**ERROR\_ALREADY\_INITIALIZED**
   

1247 (0x4DF)
 



An attempt was made to perform an initialization operation when initialization has already been completed.


   

<span id="ERROR_NO_MORE_DEVICES"></span><span id="error_no_more_devices"></span>**ERROR\_NO\_MORE\_DEVICES**
   

1248 (0x4E0)
 



No more local devices.


   

<span id="ERROR_NO_SUCH_SITE"></span><span id="error_no_such_site"></span>**ERROR\_NO\_SUCH\_SITE**
   

1249 (0x4E1)
 



The specified site does not exist.


   

<span id="ERROR_DOMAIN_CONTROLLER_EXISTS"></span><span id="error_domain_controller_exists"></span>**ERROR\_DOMAIN\_CONTROLLER\_EXISTS**
   

1250 (0x4E2)
 



A domain controller with the specified name already exists.


   

<span id="ERROR_ONLY_IF_CONNECTED"></span><span id="error_only_if_connected"></span>**ERROR\_ONLY\_IF\_CONNECTED**
   

1251 (0x4E3)
 



This operation is supported only when you are connected to the server.


   

<span id="ERROR_OVERRIDE_NOCHANGES"></span><span id="error_override_nochanges"></span>**ERROR\_OVERRIDE\_NOCHANGES**
   

1252 (0x4E4)
 



The group policy framework should call the extension even if there are no changes.


   

<span id="ERROR_BAD_USER_PROFILE"></span><span id="error_bad_user_profile"></span>**ERROR\_BAD\_USER\_PROFILE**
   

1253 (0x4E5)
 



The specified user does not have a valid profile.


   

<span id="ERROR_NOT_SUPPORTED_ON_SBS"></span><span id="error_not_supported_on_sbs"></span>**ERROR\_NOT\_SUPPORTED\_ON\_SBS**
   

1254 (0x4E6)
 



This operation is not supported on a computer running Windows Server 2003 for Small Business Server.


   

<span id="ERROR_SERVER_SHUTDOWN_IN_PROGRESS"></span><span id="error_server_shutdown_in_progress"></span>**ERROR\_SERVER\_SHUTDOWN\_IN\_PROGRESS**
   

1255 (0x4E7)
 



The server machine is shutting down.


   

<span id="ERROR_HOST_DOWN"></span><span id="error_host_down"></span>**ERROR\_HOST\_DOWN**
   

1256 (0x4E8)
 



The remote system is not available. For information about network troubleshooting, see Windows Help.


   

<span id="ERROR_NON_ACCOUNT_SID"></span><span id="error_non_account_sid"></span>**ERROR\_NON\_ACCOUNT\_SID**
   

1257 (0x4E9)
 



The security identifier provided is not from an account domain.


   

<span id="ERROR_NON_DOMAIN_SID"></span><span id="error_non_domain_sid"></span>**ERROR\_NON\_DOMAIN\_SID**
   

1258 (0x4EA)
 



The security identifier provided does not have a domain component.


   

<span id="ERROR_APPHELP_BLOCK"></span><span id="error_apphelp_block"></span>**ERROR\_APPHELP\_BLOCK**
   

1259 (0x4EB)
 



AppHelp dialog canceled thus preventing the application from starting.


   

<span id="ERROR_ACCESS_DISABLED_BY_POLICY"></span><span id="error_access_disabled_by_policy"></span>**ERROR\_ACCESS\_DISABLED\_BY\_POLICY**
   

1260 (0x4EC)
 



This program is blocked by group policy. For more information, contact your system administrator.


   

<span id="ERROR_REG_NAT_CONSUMPTION"></span><span id="error_reg_nat_consumption"></span>**ERROR\_REG\_NAT\_CONSUMPTION**
   

1261 (0x4ED)
 



A program attempt to use an invalid register value. Normally caused by an uninitialized register. This error is Itanium specific.


   

<span id="ERROR_CSCSHARE_OFFLINE"></span><span id="error_cscshare_offline"></span>**ERROR\_CSCSHARE\_OFFLINE**
   

1262 (0x4EE)
 



The share is currently offline or does not exist.


   

<span id="ERROR_PKINIT_FAILURE"></span><span id="error_pkinit_failure"></span>**ERROR\_PKINIT\_FAILURE**
   

1263 (0x4EF)
 



The Kerberos protocol encountered an error while validating the KDC certificate during smartcard logon. There is more information in the system event log.


   

<span id="ERROR_SMARTCARD_SUBSYSTEM_FAILURE"></span><span id="error_smartcard_subsystem_failure"></span>**ERROR\_SMARTCARD\_SUBSYSTEM\_FAILURE**
   

1264 (0x4F0)
 



The Kerberos protocol encountered an error while attempting to utilize the smartcard subsystem.


   

<span id="ERROR_DOWNGRADE_DETECTED"></span><span id="error_downgrade_detected"></span>**ERROR\_DOWNGRADE\_DETECTED**
   

1265 (0x4F1)
 



The system cannot contact a domain controller to service the authentication request. Please try again later.


   

<span id="ERROR_MACHINE_LOCKED"></span><span id="error_machine_locked"></span>**ERROR\_MACHINE\_LOCKED**
   

1271 (0x4F7)
 



The machine is locked and cannot be shut down without the force option.


   

<span id="ERROR_CALLBACK_SUPPLIED_INVALID_DATA"></span><span id="error_callback_supplied_invalid_data"></span>**ERROR\_CALLBACK\_SUPPLIED\_INVALID\_DATA**
   

1273 (0x4F9)
 



An application-defined callback gave invalid data when called.


   

<span id="ERROR_SYNC_FOREGROUND_REFRESH_REQUIRED"></span><span id="error_sync_foreground_refresh_required"></span>**ERROR\_SYNC\_FOREGROUND\_REFRESH\_REQUIRED**
   

1274 (0x4FA)
 



The group policy framework should call the extension in the synchronous foreground policy refresh.


   

<span id="ERROR_DRIVER_BLOCKED"></span><span id="error_driver_blocked"></span>**ERROR\_DRIVER\_BLOCKED**
   

1275 (0x4FB)
 



This driver has been blocked from loading.


   

<span id="ERROR_INVALID_IMPORT_OF_NON_DLL"></span><span id="error_invalid_import_of_non_dll"></span>**ERROR\_INVALID\_IMPORT\_OF\_NON\_DLL**
   

1276 (0x4FC)
 



A dynamic link library (DLL) referenced a module that was neither a DLL nor the process's executable image.


   

<span id="ERROR_ACCESS_DISABLED_WEBBLADE"></span><span id="error_access_disabled_webblade"></span>**ERROR\_ACCESS\_DISABLED\_WEBBLADE**
   

1277 (0x4FD)
 



Windows cannot open this program since it has been disabled.


   

<span id="ERROR_ACCESS_DISABLED_WEBBLADE_TAMPER"></span><span id="error_access_disabled_webblade_tamper"></span>**ERROR\_ACCESS\_DISABLED\_WEBBLADE\_TAMPER**
   

1278 (0x4FE)
 



Windows cannot open this program because the license enforcement system has been tampered with or become corrupted.


   

<span id="ERROR_RECOVERY_FAILURE"></span><span id="error_recovery_failure"></span>**ERROR\_RECOVERY\_FAILURE**
   

1279 (0x4FF)
 



A transaction recover failed.


   

<span id="ERROR_ALREADY_FIBER"></span><span id="error_already_fiber"></span>**ERROR\_ALREADY\_FIBER**
   

1280 (0x500)
 



The current thread has already been converted to a fiber.


   

<span id="ERROR_ALREADY_THREAD"></span><span id="error_already_thread"></span>**ERROR\_ALREADY\_THREAD**
   

1281 (0x501)
 



The current thread has already been converted from a fiber.


   

<span id="ERROR_STACK_BUFFER_OVERRUN"></span><span id="error_stack_buffer_overrun"></span>**ERROR\_STACK\_BUFFER\_OVERRUN**
   

1282 (0x502)
 



The system detected an overrun of a stack-based buffer in this application. This overrun could potentially allow a malicious user to gain control of this application.


   

<span id="ERROR_PARAMETER_QUOTA_EXCEEDED"></span><span id="error_parameter_quota_exceeded"></span>**ERROR\_PARAMETER\_QUOTA\_EXCEEDED**
   

1283 (0x503)
 



Data present in one of the parameters is more than the function can operate on.


   

<span id="ERROR_DEBUGGER_INACTIVE"></span><span id="error_debugger_inactive"></span>**ERROR\_DEBUGGER\_INACTIVE**
   

1284 (0x504)
 



An attempt to do an operation on a debug object failed because the object is in the process of being deleted.


   

<span id="ERROR_DELAY_LOAD_FAILED"></span><span id="error_delay_load_failed"></span>**ERROR\_DELAY\_LOAD\_FAILED**
   

1285 (0x505)
 



An attempt to delay-load a .dll or get a function address in a delay-loaded .dll failed.


   

<span id="ERROR_VDM_DISALLOWED"></span><span id="error_vdm_disallowed"></span>**ERROR\_VDM\_DISALLOWED**
   

1286 (0x506)
 



%1 is a 16-bit application. You do not have permissions to execute 16-bit applications. Check your permissions with your system administrator.


   

<span id="ERROR_UNIDENTIFIED_ERROR"></span><span id="error_unidentified_error"></span>**ERROR\_UNIDENTIFIED\_ERROR**
   

1287 (0x507)
 



Insufficient information exists to identify the cause of failure.


   

<span id="ERROR_INVALID_CRUNTIME_PARAMETER"></span><span id="error_invalid_cruntime_parameter"></span>**ERROR\_INVALID\_CRUNTIME\_PARAMETER**
   

1288 (0x508)
 



The parameter passed to a C runtime function is incorrect.


   

<span id="ERROR_BEYOND_VDL"></span><span id="error_beyond_vdl"></span>**ERROR\_BEYOND\_VDL**
   

1289 (0x509)
 



The operation occurred beyond the valid data length of the file.


   

<span id="ERROR_INCOMPATIBLE_SERVICE_SID_TYPE"></span><span id="error_incompatible_service_sid_type"></span>**ERROR\_INCOMPATIBLE\_SERVICE\_SID\_TYPE**
   

1290 (0x50A)
 



The service start failed since one or more services in the same process have an incompatible service SID type setting. A service with restricted service SID type can only coexist in the same process with other services with a restricted SID type. If the service SID type for this service was just configured, the hosting process must be restarted in order to start this service.

On Windows Server 2003 and Windows XP, an unrestricted service cannot coexist in the same process with other services. The service with the unrestricted service SID type must be moved to an owned process in order to start this service.


   

<span id="ERROR_DRIVER_PROCESS_TERMINATED"></span><span id="error_driver_process_terminated"></span>**ERROR\_DRIVER\_PROCESS\_TERMINATED**
   

1291 (0x50B)
 



The process hosting the driver for this device has been terminated.


   

<span id="ERROR_IMPLEMENTATION_LIMIT"></span><span id="error_implementation_limit"></span>**ERROR\_IMPLEMENTATION\_LIMIT**
   

1292 (0x50C)
 



An operation attempted to exceed an implementation-defined limit.


   

<span id="ERROR_PROCESS_IS_PROTECTED"></span><span id="error_process_is_protected"></span>**ERROR\_PROCESS\_IS\_PROTECTED**
   

1293 (0x50D)
 



Either the target process, or the target thread's containing process, is a protected process.


   

<span id="ERROR_SERVICE_NOTIFY_CLIENT_LAGGING"></span><span id="error_service_notify_client_lagging"></span>**ERROR\_SERVICE\_NOTIFY\_CLIENT\_LAGGING**
   

1294 (0x50E)
 



The service notification client is lagging too far behind the current state of services in the machine.


   

<span id="ERROR_DISK_QUOTA_EXCEEDED"></span><span id="error_disk_quota_exceeded"></span>**ERROR\_DISK\_QUOTA\_EXCEEDED**
   

1295 (0x50F)
 



The requested file operation failed because the storage quota was exceeded. To free up disk space, move files to a different location or delete unnecessary files. For more information, contact your system administrator.


   

<span id="ERROR_CONTENT_BLOCKED"></span><span id="error_content_blocked"></span>**ERROR\_CONTENT\_BLOCKED**
   

1296 (0x510)
 



The requested file operation failed because the storage policy blocks that type of file. For more information, contact your system administrator.


   

<span id="ERROR_INCOMPATIBLE_SERVICE_PRIVILEGE"></span><span id="error_incompatible_service_privilege"></span>**ERROR\_INCOMPATIBLE\_SERVICE\_PRIVILEGE**
   

1297 (0x511)
 



A privilege that the service requires to function properly does not exist in the service account configuration. You may use the Services Microsoft Management Console (MMC) snap-in (services.msc) and the Local Security Settings MMC snap-in (secpol.msc) to view the service configuration and the account configuration.


   

<span id="ERROR_APP_HANG"></span><span id="error_app_hang"></span>**ERROR\_APP\_HANG**
   

1298 (0x512)
 



A thread involved in this operation appears to be unresponsive.


   

<span id="ERROR_INVALID_LABEL"></span><span id="error_invalid_label"></span>**ERROR\_INVALID\_LABEL**
   

1299 (0x513)
 



Indicates a particular Security ID may not be assigned as the label of an object.


   


## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   |  WinError.h  |



## See also

 

[System Error Codes](system-error-codes.md)
 

 

 





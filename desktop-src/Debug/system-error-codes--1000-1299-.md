---
description: Describes error codes 1000-1299 defined in the WinError.h header file and is intended for developers.
ms.assetid: 0061feb6-e1a0-4fcd-8f80-954087c799d7
title: System Error Codes (1000-1299) (WinError.h)
ms.topic: reference
ms.date: 07/18/2019
---

# System Error Codes (1000-1299)

> [!NOTE]
> This information is intended for developers debugging system errors. For other errors, such as issues with Windows Update, there is a list of resources on the [Error codes](system-error-codes.md) page.

The following list describes [system error codes](system-error-codes.md) for errors 1000 to 1299. They are returned by the [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) function when many functions fail. To retrieve the description text for the error in your application, use the [**FormatMessage**](/windows/desktop/api/WinBase/nf-winbase-formatmessage) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag.

<dl> <dt>

<span id="ERROR_STACK_OVERFLOW"></span><span id="error_stack_overflow"></span>**ERROR\_STACK\_OVERFLOW**
</dt> <dd> <dl> <dt>

1001 (0x3E9)
</dt> <dt>



Recursion too deep; the stack overflowed.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_MESSAGE"></span><span id="error_invalid_message"></span>**ERROR\_INVALID\_MESSAGE**
</dt> <dd> <dl> <dt>

1002 (0x3EA)
</dt> <dt>



The window cannot act on the sent message.


</dt> </dl> </dd> <dt>

<span id="ERROR_CAN_NOT_COMPLETE"></span><span id="error_can_not_complete"></span>**ERROR\_CAN\_NOT\_COMPLETE**
</dt> <dd> <dl> <dt>

1003 (0x3EB)
</dt> <dt>



Cannot complete this function.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_FLAGS"></span><span id="error_invalid_flags"></span>**ERROR\_INVALID\_FLAGS**
</dt> <dd> <dl> <dt>

1004 (0x3EC)
</dt> <dt>



Invalid flags.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNRECOGNIZED_VOLUME"></span><span id="error_unrecognized_volume"></span>**ERROR\_UNRECOGNIZED\_VOLUME**
</dt> <dd> <dl> <dt>

1005 (0x3ED)
</dt> <dt>



The volume does not contain a recognized file system. Please make sure that all required file system drivers are loaded and that the volume is not corrupted.


</dt> </dl> </dd> <dt>

<span id="ERROR_FILE_INVALID"></span><span id="error_file_invalid"></span>**ERROR\_FILE\_INVALID**
</dt> <dd> <dl> <dt>

1006 (0x3EE)
</dt> <dt>



The volume for a file has been externally altered so that the opened file is no longer valid.


</dt> </dl> </dd> <dt>

<span id="ERROR_FULLSCREEN_MODE"></span><span id="error_fullscreen_mode"></span>**ERROR\_FULLSCREEN\_MODE**
</dt> <dd> <dl> <dt>

1007 (0x3EF)
</dt> <dt>



The requested operation cannot be performed in full-screen mode.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_TOKEN"></span><span id="error_no_token"></span>**ERROR\_NO\_TOKEN**
</dt> <dd> <dl> <dt>

1008 (0x3F0)
</dt> <dt>



An attempt was made to reference a token that does not exist.


</dt> </dl> </dd> <dt>

<span id="ERROR_BADDB"></span><span id="error_baddb"></span>**ERROR\_BADDB**
</dt> <dd> <dl> <dt>

1009 (0x3F1)
</dt> <dt>



The configuration registry database is corrupt.


</dt> </dl> </dd> <dt>

<span id="ERROR_BADKEY"></span><span id="error_badkey"></span>**ERROR\_BADKEY**
</dt> <dd> <dl> <dt>

1010 (0x3F2)
</dt> <dt>



The configuration registry key is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_CANTOPEN"></span><span id="error_cantopen"></span>**ERROR\_CANTOPEN**
</dt> <dd> <dl> <dt>

1011 (0x3F3)
</dt> <dt>



The configuration registry key could not be opened.


</dt> </dl> </dd> <dt>

<span id="ERROR_CANTREAD"></span><span id="error_cantread"></span>**ERROR\_CANTREAD**
</dt> <dd> <dl> <dt>

1012 (0x3F4)
</dt> <dt>



The configuration registry key could not be read.


</dt> </dl> </dd> <dt>

<span id="ERROR_CANTWRITE"></span><span id="error_cantwrite"></span>**ERROR\_CANTWRITE**
</dt> <dd> <dl> <dt>

1013 (0x3F5)
</dt> <dt>



The configuration registry key could not be written.


</dt> </dl> </dd> <dt>

<span id="ERROR_REGISTRY_RECOVERED"></span><span id="error_registry_recovered"></span>**ERROR\_REGISTRY\_RECOVERED**
</dt> <dd> <dl> <dt>

1014 (0x3F6)
</dt> <dt>



One of the files in the registry database had to be recovered by use of a log or alternate copy. The recovery was successful.


</dt> </dl> </dd> <dt>

<span id="ERROR_REGISTRY_CORRUPT"></span><span id="error_registry_corrupt"></span>**ERROR\_REGISTRY\_CORRUPT**
</dt> <dd> <dl> <dt>

1015 (0x3F7)
</dt> <dt>



The registry is corrupted. The structure of one of the files containing registry data is corrupted, or the system's memory image of the file is corrupted, or the file could not be recovered because the alternate copy or log was absent or corrupted.


</dt> </dl> </dd> <dt>

<span id="ERROR_REGISTRY_IO_FAILED"></span><span id="error_registry_io_failed"></span>**ERROR\_REGISTRY\_IO\_FAILED**
</dt> <dd> <dl> <dt>

1016 (0x3F8)
</dt> <dt>



An I/O operation initiated by the registry failed unrecoverably. The registry could not read in, or write out, or flush, one of the files that contain the system's image of the registry.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_REGISTRY_FILE"></span><span id="error_not_registry_file"></span>**ERROR\_NOT\_REGISTRY\_FILE**
</dt> <dd> <dl> <dt>

1017 (0x3F9)
</dt> <dt>



The system has attempted to load or restore a file into the registry, but the specified file is not in a registry file format.


</dt> </dl> </dd> <dt>

<span id="ERROR_KEY_DELETED"></span><span id="error_key_deleted"></span>**ERROR\_KEY\_DELETED**
</dt> <dd> <dl> <dt>

1018 (0x3FA)
</dt> <dt>



Illegal operation attempted on a registry key that has been marked for deletion.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_LOG_SPACE"></span><span id="error_no_log_space"></span>**ERROR\_NO\_LOG\_SPACE**
</dt> <dd> <dl> <dt>

1019 (0x3FB)
</dt> <dt>



System could not allocate the required space in a registry log.


</dt> </dl> </dd> <dt>

<span id="ERROR_KEY_HAS_CHILDREN"></span><span id="error_key_has_children"></span>**ERROR\_KEY\_HAS\_CHILDREN**
</dt> <dd> <dl> <dt>

1020 (0x3FC)
</dt> <dt>



Cannot create a symbolic link in a registry key that already has subkeys or values.


</dt> </dl> </dd> <dt>

<span id="ERROR_CHILD_MUST_BE_VOLATILE"></span><span id="error_child_must_be_volatile"></span>**ERROR\_CHILD\_MUST\_BE\_VOLATILE**
</dt> <dd> <dl> <dt>

1021 (0x3FD)
</dt> <dt>



Cannot create a stable subkey under a volatile parent key.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOTIFY_ENUM_DIR"></span><span id="error_notify_enum_dir"></span>**ERROR\_NOTIFY\_ENUM\_DIR**
</dt> <dd> <dl> <dt>

1022 (0x3FE)
</dt> <dt>



A notify change request is being completed and the information is not being returned in the caller's buffer. The caller now needs to enumerate the files to find the changes.


</dt> </dl> </dd> <dt>

<span id="ERROR_DEPENDENT_SERVICES_RUNNING"></span><span id="error_dependent_services_running"></span>**ERROR\_DEPENDENT\_SERVICES\_RUNNING**
</dt> <dd> <dl> <dt>

1051 (0x41B)
</dt> <dt>



A stop control has been sent to a service that other running services are dependent on.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_SERVICE_CONTROL"></span><span id="error_invalid_service_control"></span>**ERROR\_INVALID\_SERVICE\_CONTROL**
</dt> <dd> <dl> <dt>

1052 (0x41C)
</dt> <dt>



The requested control is not valid for this service.


</dt> </dl> </dd> <dt>

<span id="ERROR_SERVICE_REQUEST_TIMEOUT"></span><span id="error_service_request_timeout"></span>**ERROR\_SERVICE\_REQUEST\_TIMEOUT**
</dt> <dd> <dl> <dt>

1053 (0x41D)
</dt> <dt>



The service did not respond to the start or control request in a timely fashion.


</dt> </dl> </dd> <dt>

<span id="ERROR_SERVICE_NO_THREAD"></span><span id="error_service_no_thread"></span>**ERROR\_SERVICE\_NO\_THREAD**
</dt> <dd> <dl> <dt>

1054 (0x41E)
</dt> <dt>



A thread could not be created for the service.


</dt> </dl> </dd> <dt>

<span id="ERROR_SERVICE_DATABASE_LOCKED"></span><span id="error_service_database_locked"></span>**ERROR\_SERVICE\_DATABASE\_LOCKED**
</dt> <dd> <dl> <dt>

1055 (0x41F)
</dt> <dt>



The service database is locked.


</dt> </dl> </dd> <dt>

<span id="ERROR_SERVICE_ALREADY_RUNNING"></span><span id="error_service_already_running"></span>**ERROR\_SERVICE\_ALREADY\_RUNNING**
</dt> <dd> <dl> <dt>

1056 (0x420)
</dt> <dt>



An instance of the service is already running.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_SERVICE_ACCOUNT"></span><span id="error_invalid_service_account"></span>**ERROR\_INVALID\_SERVICE\_ACCOUNT**
</dt> <dd> <dl> <dt>

1057 (0x421)
</dt> <dt>



The account name is invalid or does not exist, or the password is invalid for the account name specified.


</dt> </dl> </dd> <dt>

<span id="ERROR_SERVICE_DISABLED"></span><span id="error_service_disabled"></span>**ERROR\_SERVICE\_DISABLED**
</dt> <dd> <dl> <dt>

1058 (0x422)
</dt> <dt>



The service cannot be started, either because it is disabled or because it has no enabled devices associated with it.


</dt> </dl> </dd> <dt>

<span id="ERROR_CIRCULAR_DEPENDENCY"></span><span id="error_circular_dependency"></span>**ERROR\_CIRCULAR\_DEPENDENCY**
</dt> <dd> <dl> <dt>

1059 (0x423)
</dt> <dt>



Circular service dependency was specified.


</dt> </dl> </dd> <dt>

<span id="ERROR_SERVICE_DOES_NOT_EXIST"></span><span id="error_service_does_not_exist"></span>**ERROR\_SERVICE\_DOES\_NOT\_EXIST**
</dt> <dd> <dl> <dt>

1060 (0x424)
</dt> <dt>



The specified service does not exist as an installed service.


</dt> </dl> </dd> <dt>

<span id="ERROR_SERVICE_CANNOT_ACCEPT_CTRL"></span><span id="error_service_cannot_accept_ctrl"></span>**ERROR\_SERVICE\_CANNOT\_ACCEPT\_CTRL**
</dt> <dd> <dl> <dt>

1061 (0x425)
</dt> <dt>



The service cannot accept control messages at this time.


</dt> </dl> </dd> <dt>

<span id="ERROR_SERVICE_NOT_ACTIVE"></span><span id="error_service_not_active"></span>**ERROR\_SERVICE\_NOT\_ACTIVE**
</dt> <dd> <dl> <dt>

1062 (0x426)
</dt> <dt>



The service has not been started.


</dt> </dl> </dd> <dt>

<span id="ERROR_FAILED_SERVICE_CONTROLLER_CONNECT"></span><span id="error_failed_service_controller_connect"></span>**ERROR\_FAILED\_SERVICE\_CONTROLLER\_CONNECT**
</dt> <dd> <dl> <dt>

1063 (0x427)
</dt> <dt>



The service process could not connect to the service controller.


</dt> </dl> </dd> <dt>

<span id="ERROR_EXCEPTION_IN_SERVICE"></span><span id="error_exception_in_service"></span>**ERROR\_EXCEPTION\_IN\_SERVICE**
</dt> <dd> <dl> <dt>

1064 (0x428)
</dt> <dt>



An exception occurred in the service when handling the control request.


</dt> </dl> </dd> <dt>

<span id="ERROR_DATABASE_DOES_NOT_EXIST"></span><span id="error_database_does_not_exist"></span>**ERROR\_DATABASE\_DOES\_NOT\_EXIST**
</dt> <dd> <dl> <dt>

1065 (0x429)
</dt> <dt>



The database specified does not exist.


</dt> </dl> </dd> <dt>

<span id="ERROR_SERVICE_SPECIFIC_ERROR"></span><span id="error_service_specific_error"></span>**ERROR\_SERVICE\_SPECIFIC\_ERROR**
</dt> <dd> <dl> <dt>

1066 (0x42A)
</dt> <dt>



The service has returned a service-specific error code.


</dt> </dl> </dd> <dt>

<span id="ERROR_PROCESS_ABORTED"></span><span id="error_process_aborted"></span>**ERROR\_PROCESS\_ABORTED**
</dt> <dd> <dl> <dt>

1067 (0x42B)
</dt> <dt>



The process terminated unexpectedly.


</dt> </dl> </dd> <dt>

<span id="ERROR_SERVICE_DEPENDENCY_FAIL"></span><span id="error_service_dependency_fail"></span>**ERROR\_SERVICE\_DEPENDENCY\_FAIL**
</dt> <dd> <dl> <dt>

1068 (0x42C)
</dt> <dt>



The dependency service or group failed to start.


</dt> </dl> </dd> <dt>

<span id="ERROR_SERVICE_LOGON_FAILED"></span><span id="error_service_logon_failed"></span>**ERROR\_SERVICE\_LOGON\_FAILED**
</dt> <dd> <dl> <dt>

1069 (0x42D)
</dt> <dt>



The service did not start due to a logon failure.


</dt> </dl> </dd> <dt>

<span id="ERROR_SERVICE_START_HANG"></span><span id="error_service_start_hang"></span>**ERROR\_SERVICE\_START\_HANG**
</dt> <dd> <dl> <dt>

1070 (0x42E)
</dt> <dt>



After starting, the service hung in a start-pending state.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_SERVICE_LOCK"></span><span id="error_invalid_service_lock"></span>**ERROR\_INVALID\_SERVICE\_LOCK**
</dt> <dd> <dl> <dt>

1071 (0x42F)
</dt> <dt>



The specified service database lock is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_SERVICE_MARKED_FOR_DELETE"></span><span id="error_service_marked_for_delete"></span>**ERROR\_SERVICE\_MARKED\_FOR\_DELETE**
</dt> <dd> <dl> <dt>

1072 (0x430)
</dt> <dt>



The specified service has been marked for deletion.


</dt> </dl> </dd> <dt>

<span id="ERROR_SERVICE_EXISTS"></span><span id="error_service_exists"></span>**ERROR\_SERVICE\_EXISTS**
</dt> <dd> <dl> <dt>

1073 (0x431)
</dt> <dt>



The specified service already exists.


</dt> </dl> </dd> <dt>

<span id="ERROR_ALREADY_RUNNING_LKG"></span><span id="error_already_running_lkg"></span>**ERROR\_ALREADY\_RUNNING\_LKG**
</dt> <dd> <dl> <dt>

1074 (0x432)
</dt> <dt>



The system is currently running with the last-known-good configuration.


</dt> </dl> </dd> <dt>

<span id="ERROR_SERVICE_DEPENDENCY_DELETED"></span><span id="error_service_dependency_deleted"></span>**ERROR\_SERVICE\_DEPENDENCY\_DELETED**
</dt> <dd> <dl> <dt>

1075 (0x433)
</dt> <dt>



The dependency service does not exist or has been marked for deletion.


</dt> </dl> </dd> <dt>

<span id="ERROR_BOOT_ALREADY_ACCEPTED"></span><span id="error_boot_already_accepted"></span>**ERROR\_BOOT\_ALREADY\_ACCEPTED**
</dt> <dd> <dl> <dt>

1076 (0x434)
</dt> <dt>



The current boot has already been accepted for use as the last-known-good control set.


</dt> </dl> </dd> <dt>

<span id="ERROR_SERVICE_NEVER_STARTED"></span><span id="error_service_never_started"></span>**ERROR\_SERVICE\_NEVER\_STARTED**
</dt> <dd> <dl> <dt>

1077 (0x435)
</dt> <dt>



No attempts to start the service have been made since the last boot.


</dt> </dl> </dd> <dt>

<span id="ERROR_DUPLICATE_SERVICE_NAME"></span><span id="error_duplicate_service_name"></span>**ERROR\_DUPLICATE\_SERVICE\_NAME**
</dt> <dd> <dl> <dt>

1078 (0x436)
</dt> <dt>



The name is already in use as either a service name or a service display name.


</dt> </dl> </dd> <dt>

<span id="ERROR_DIFFERENT_SERVICE_ACCOUNT"></span><span id="error_different_service_account"></span>**ERROR\_DIFFERENT\_SERVICE\_ACCOUNT**
</dt> <dd> <dl> <dt>

1079 (0x437)
</dt> <dt>



The account specified for this service is different from the account specified for other services running in the same process.


</dt> </dl> </dd> <dt>

<span id="ERROR_CANNOT_DETECT_DRIVER_FAILURE"></span><span id="error_cannot_detect_driver_failure"></span>**ERROR\_CANNOT\_DETECT\_DRIVER\_FAILURE**
</dt> <dd> <dl> <dt>

1080 (0x438)
</dt> <dt>



Failure actions can only be set for Win32 services, not for drivers.


</dt> </dl> </dd> <dt>

<span id="ERROR_CANNOT_DETECT_PROCESS_ABORT"></span><span id="error_cannot_detect_process_abort"></span>**ERROR\_CANNOT\_DETECT\_PROCESS\_ABORT**
</dt> <dd> <dl> <dt>

1081 (0x439)
</dt> <dt>



This service runs in the same process as the service control manager. Therefore, the service control manager cannot take action if this service's process terminates unexpectedly.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_RECOVERY_PROGRAM"></span><span id="error_no_recovery_program"></span>**ERROR\_NO\_RECOVERY\_PROGRAM**
</dt> <dd> <dl> <dt>

1082 (0x43A)
</dt> <dt>



No recovery program has been configured for this service.


</dt> </dl> </dd> <dt>

<span id="ERROR_SERVICE_NOT_IN_EXE"></span><span id="error_service_not_in_exe"></span>**ERROR\_SERVICE\_NOT\_IN\_EXE**
</dt> <dd> <dl> <dt>

1083 (0x43B)
</dt> <dt>



The executable program that this service is configured to run in does not implement the service.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_SAFEBOOT_SERVICE"></span><span id="error_not_safeboot_service"></span>**ERROR\_NOT\_SAFEBOOT\_SERVICE**
</dt> <dd> <dl> <dt>

1084 (0x43C)
</dt> <dt>



This service cannot be started in Safe Mode.


</dt> </dl> </dd> <dt>

<span id="ERROR_END_OF_MEDIA"></span><span id="error_end_of_media"></span>**ERROR\_END\_OF\_MEDIA**
</dt> <dd> <dl> <dt>

1100 (0x44C)
</dt> <dt>



The physical end of the tape has been reached.


</dt> </dl> </dd> <dt>

<span id="ERROR_FILEMARK_DETECTED"></span><span id="error_filemark_detected"></span>**ERROR\_FILEMARK\_DETECTED**
</dt> <dd> <dl> <dt>

1101 (0x44D)
</dt> <dt>



A tape access reached a filemark.


</dt> </dl> </dd> <dt>

<span id="ERROR_BEGINNING_OF_MEDIA"></span><span id="error_beginning_of_media"></span>**ERROR\_BEGINNING\_OF\_MEDIA**
</dt> <dd> <dl> <dt>

1102 (0x44E)
</dt> <dt>



The beginning of the tape or a partition was encountered.


</dt> </dl> </dd> <dt>

<span id="ERROR_SETMARK_DETECTED"></span><span id="error_setmark_detected"></span>**ERROR\_SETMARK\_DETECTED**
</dt> <dd> <dl> <dt>

1103 (0x44F)
</dt> <dt>



A tape access reached the end of a set of files.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_DATA_DETECTED"></span><span id="error_no_data_detected"></span>**ERROR\_NO\_DATA\_DETECTED**
</dt> <dd> <dl> <dt>

1104 (0x450)
</dt> <dt>



No more data is on the tape.


</dt> </dl> </dd> <dt>

<span id="ERROR_PARTITION_FAILURE"></span><span id="error_partition_failure"></span>**ERROR\_PARTITION\_FAILURE**
</dt> <dd> <dl> <dt>

1105 (0x451)
</dt> <dt>



Tape could not be partitioned.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_BLOCK_LENGTH"></span><span id="error_invalid_block_length"></span>**ERROR\_INVALID\_BLOCK\_LENGTH**
</dt> <dd> <dl> <dt>

1106 (0x452)
</dt> <dt>



When accessing a new tape of a multivolume partition, the current block size is incorrect.


</dt> </dl> </dd> <dt>

<span id="ERROR_DEVICE_NOT_PARTITIONED"></span><span id="error_device_not_partitioned"></span>**ERROR\_DEVICE\_NOT\_PARTITIONED**
</dt> <dd> <dl> <dt>

1107 (0x453)
</dt> <dt>



Tape partition information could not be found when loading a tape.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNABLE_TO_LOCK_MEDIA"></span><span id="error_unable_to_lock_media"></span>**ERROR\_UNABLE\_TO\_LOCK\_MEDIA**
</dt> <dd> <dl> <dt>

1108 (0x454)
</dt> <dt>



Unable to lock the media eject mechanism.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNABLE_TO_UNLOAD_MEDIA"></span><span id="error_unable_to_unload_media"></span>**ERROR\_UNABLE\_TO\_UNLOAD\_MEDIA**
</dt> <dd> <dl> <dt>

1109 (0x455)
</dt> <dt>



Unable to unload the media.


</dt> </dl> </dd> <dt>

<span id="ERROR_MEDIA_CHANGED"></span><span id="error_media_changed"></span>**ERROR\_MEDIA\_CHANGED**
</dt> <dd> <dl> <dt>

1110 (0x456)
</dt> <dt>



The media in the drive may have changed.


</dt> </dl> </dd> <dt>

<span id="ERROR_BUS_RESET"></span><span id="error_bus_reset"></span>**ERROR\_BUS\_RESET**
</dt> <dd> <dl> <dt>

1111 (0x457)
</dt> <dt>



The I/O bus was reset.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_MEDIA_IN_DRIVE"></span><span id="error_no_media_in_drive"></span>**ERROR\_NO\_MEDIA\_IN\_DRIVE**
</dt> <dd> <dl> <dt>

1112 (0x458)
</dt> <dt>



No media in drive.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_UNICODE_TRANSLATION"></span><span id="error_no_unicode_translation"></span>**ERROR\_NO\_UNICODE\_TRANSLATION**
</dt> <dd> <dl> <dt>

1113 (0x459)
</dt> <dt>



No mapping for the Unicode character exists in the target multi-byte code page.


</dt> </dl> </dd> <dt>

<span id="ERROR_DLL_INIT_FAILED"></span><span id="error_dll_init_failed"></span>**ERROR\_DLL\_INIT\_FAILED**
</dt> <dd> <dl> <dt>

1114 (0x45A)
</dt> <dt>



A dynamic link library (DLL) initialization routine failed.


</dt> </dl> </dd> <dt>

<span id="ERROR_SHUTDOWN_IN_PROGRESS"></span><span id="error_shutdown_in_progress"></span>**ERROR\_SHUTDOWN\_IN\_PROGRESS**
</dt> <dd> <dl> <dt>

1115 (0x45B)
</dt> <dt>



A system shutdown is in progress.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_SHUTDOWN_IN_PROGRESS"></span><span id="error_no_shutdown_in_progress"></span>**ERROR\_NO\_SHUTDOWN\_IN\_PROGRESS**
</dt> <dd> <dl> <dt>

1116 (0x45C)
</dt> <dt>



Unable to abort the system shutdown because no shutdown was in progress.


</dt> </dl> </dd> <dt>

<span id="ERROR_IO_DEVICE"></span><span id="error_io_device"></span>**ERROR\_IO\_DEVICE**
</dt> <dd> <dl> <dt>

1117 (0x45D)
</dt> <dt>



The request could not be performed because of an I/O device error.


</dt> </dl> </dd> <dt>

<span id="ERROR_SERIAL_NO_DEVICE"></span><span id="error_serial_no_device"></span>**ERROR\_SERIAL\_NO\_DEVICE**
</dt> <dd> <dl> <dt>

1118 (0x45E)
</dt> <dt>



No serial device was successfully initialized. The serial driver will unload.


</dt> </dl> </dd> <dt>

<span id="ERROR_IRQ_BUSY"></span><span id="error_irq_busy"></span>**ERROR\_IRQ\_BUSY**
</dt> <dd> <dl> <dt>

1119 (0x45F)
</dt> <dt>



Unable to open a device that was sharing an interrupt request (IRQ) with other devices. At least one other device that uses that IRQ was already opened.


</dt> </dl> </dd> <dt>

<span id="ERROR_MORE_WRITES"></span><span id="error_more_writes"></span>**ERROR\_MORE\_WRITES**
</dt> <dd> <dl> <dt>

1120 (0x460)
</dt> <dt>



A serial I/O operation was completed by another write to the serial port. The IOCTL\_SERIAL\_XOFF\_COUNTER reached zero.)


</dt> </dl> </dd> <dt>

<span id="ERROR_COUNTER_TIMEOUT"></span><span id="error_counter_timeout"></span>**ERROR\_COUNTER\_TIMEOUT**
</dt> <dd> <dl> <dt>

1121 (0x461)
</dt> <dt>



A serial I/O operation completed because the timeout period expired. The IOCTL\_SERIAL\_XOFF\_COUNTER did not reach zero.)


</dt> </dl> </dd> <dt>

<span id="ERROR_FLOPPY_ID_MARK_NOT_FOUND"></span><span id="error_floppy_id_mark_not_found"></span>**ERROR\_FLOPPY\_ID\_MARK\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

1122 (0x462)
</dt> <dt>



No ID address mark was found on the floppy disk.


</dt> </dl> </dd> <dt>

<span id="ERROR_FLOPPY_WRONG_CYLINDER"></span><span id="error_floppy_wrong_cylinder"></span>**ERROR\_FLOPPY\_WRONG\_CYLINDER**
</dt> <dd> <dl> <dt>

1123 (0x463)
</dt> <dt>



Mismatch between the floppy disk sector ID field and the floppy disk controller track address.


</dt> </dl> </dd> <dt>

<span id="ERROR_FLOPPY_UNKNOWN_ERROR"></span><span id="error_floppy_unknown_error"></span>**ERROR\_FLOPPY\_UNKNOWN\_ERROR**
</dt> <dd> <dl> <dt>

1124 (0x464)
</dt> <dt>



The floppy disk controller reported an error that is not recognized by the floppy disk driver.


</dt> </dl> </dd> <dt>

<span id="ERROR_FLOPPY_BAD_REGISTERS"></span><span id="error_floppy_bad_registers"></span>**ERROR\_FLOPPY\_BAD\_REGISTERS**
</dt> <dd> <dl> <dt>

1125 (0x465)
</dt> <dt>



The floppy disk controller returned inconsistent results in its registers.


</dt> </dl> </dd> <dt>

<span id="ERROR_DISK_RECALIBRATE_FAILED"></span><span id="error_disk_recalibrate_failed"></span>**ERROR\_DISK\_RECALIBRATE\_FAILED**
</dt> <dd> <dl> <dt>

1126 (0x466)
</dt> <dt>



While accessing the hard disk, a recalibrate operation failed, even after retries.


</dt> </dl> </dd> <dt>

<span id="ERROR_DISK_OPERATION_FAILED"></span><span id="error_disk_operation_failed"></span>**ERROR\_DISK\_OPERATION\_FAILED**
</dt> <dd> <dl> <dt>

1127 (0x467)
</dt> <dt>



While accessing the hard disk, a disk operation failed even after retries.


</dt> </dl> </dd> <dt>

<span id="ERROR_DISK_RESET_FAILED"></span><span id="error_disk_reset_failed"></span>**ERROR\_DISK\_RESET\_FAILED**
</dt> <dd> <dl> <dt>

1128 (0x468)
</dt> <dt>



While accessing the hard disk, a disk controller reset was needed, but even that failed.


</dt> </dl> </dd> <dt>

<span id="ERROR_EOM_OVERFLOW"></span><span id="error_eom_overflow"></span>**ERROR\_EOM\_OVERFLOW**
</dt> <dd> <dl> <dt>

1129 (0x469)
</dt> <dt>



Physical end of tape encountered.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_ENOUGH_SERVER_MEMORY"></span><span id="error_not_enough_server_memory"></span>**ERROR\_NOT\_ENOUGH\_SERVER\_MEMORY**
</dt> <dd> <dl> <dt>

1130 (0x46A)
</dt> <dt>



Not enough server storage is available to process this command.


</dt> </dl> </dd> <dt>

<span id="ERROR_POSSIBLE_DEADLOCK"></span><span id="error_possible_deadlock"></span>**ERROR\_POSSIBLE\_DEADLOCK**
</dt> <dd> <dl> <dt>

1131 (0x46B)
</dt> <dt>



A potential deadlock condition has been detected.


</dt> </dl> </dd> <dt>

<span id="ERROR_MAPPED_ALIGNMENT"></span><span id="error_mapped_alignment"></span>**ERROR\_MAPPED\_ALIGNMENT**
</dt> <dd> <dl> <dt>

1132 (0x46C)
</dt> <dt>



The base address or the file offset specified does not have the proper alignment.


</dt> </dl> </dd> <dt>

<span id="ERROR_SET_POWER_STATE_VETOED"></span><span id="error_set_power_state_vetoed"></span>**ERROR\_SET\_POWER\_STATE\_VETOED**
</dt> <dd> <dl> <dt>

1140 (0x474)
</dt> <dt>



An attempt to change the system power state was vetoed by another application or driver.


</dt> </dl> </dd> <dt>

<span id="ERROR_SET_POWER_STATE_FAILED"></span><span id="error_set_power_state_failed"></span>**ERROR\_SET\_POWER\_STATE\_FAILED**
</dt> <dd> <dl> <dt>

1141 (0x475)
</dt> <dt>



The system BIOS failed an attempt to change the system power state.


</dt> </dl> </dd> <dt>

<span id="ERROR_TOO_MANY_LINKS"></span><span id="error_too_many_links"></span>**ERROR\_TOO\_MANY\_LINKS**
</dt> <dd> <dl> <dt>

1142 (0x476)
</dt> <dt>



An attempt was made to create more links on a file than the file system supports.


</dt> </dl> </dd> <dt>

<span id="ERROR_OLD_WIN_VERSION"></span><span id="error_old_win_version"></span>**ERROR\_OLD\_WIN\_VERSION**
</dt> <dd> <dl> <dt>

1150 (0x47E)
</dt> <dt>



The specified program requires a newer version of Windows.


</dt> </dl> </dd> <dt>

<span id="ERROR_APP_WRONG_OS"></span><span id="error_app_wrong_os"></span>**ERROR\_APP\_WRONG\_OS**
</dt> <dd> <dl> <dt>

1151 (0x47F)
</dt> <dt>



The specified program is not a Windows or MS-DOS program.


</dt> </dl> </dd> <dt>

<span id="ERROR_SINGLE_INSTANCE_APP"></span><span id="error_single_instance_app"></span>**ERROR\_SINGLE\_INSTANCE\_APP**
</dt> <dd> <dl> <dt>

1152 (0x480)
</dt> <dt>



Cannot start more than one instance of the specified program.


</dt> </dl> </dd> <dt>

<span id="ERROR_RMODE_APP"></span><span id="error_rmode_app"></span>**ERROR\_RMODE\_APP**
</dt> <dd> <dl> <dt>

1153 (0x481)
</dt> <dt>



The specified program was written for an earlier version of Windows.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_DLL"></span><span id="error_invalid_dll"></span>**ERROR\_INVALID\_DLL**
</dt> <dd> <dl> <dt>

1154 (0x482)
</dt> <dt>



One of the library files needed to run this application is damaged.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_ASSOCIATION"></span><span id="error_no_association"></span>**ERROR\_NO\_ASSOCIATION**
</dt> <dd> <dl> <dt>

1155 (0x483)
</dt> <dt>



No application is associated with the specified file for this operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_DDE_FAIL"></span><span id="error_dde_fail"></span>**ERROR\_DDE\_FAIL**
</dt> <dd> <dl> <dt>

1156 (0x484)
</dt> <dt>



An error occurred in sending the command to the application.


</dt> </dl> </dd> <dt>

<span id="ERROR_DLL_NOT_FOUND"></span><span id="error_dll_not_found"></span>**ERROR\_DLL\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

1157 (0x485)
</dt> <dt>



One of the library files needed to run this application cannot be found.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_MORE_USER_HANDLES"></span><span id="error_no_more_user_handles"></span>**ERROR\_NO\_MORE\_USER\_HANDLES**
</dt> <dd> <dl> <dt>

1158 (0x486)
</dt> <dt>



The current process has used all of its system allowance of handles for Window Manager objects.


</dt> </dl> </dd> <dt>

<span id="ERROR_MESSAGE_SYNC_ONLY"></span><span id="error_message_sync_only"></span>**ERROR\_MESSAGE\_SYNC\_ONLY**
</dt> <dd> <dl> <dt>

1159 (0x487)
</dt> <dt>



The message can be used only with synchronous operations.


</dt> </dl> </dd> <dt>

<span id="ERROR_SOURCE_ELEMENT_EMPTY"></span><span id="error_source_element_empty"></span>**ERROR\_SOURCE\_ELEMENT\_EMPTY**
</dt> <dd> <dl> <dt>

1160 (0x488)
</dt> <dt>



The indicated source element has no media.


</dt> </dl> </dd> <dt>

<span id="ERROR_DESTINATION_ELEMENT_FULL"></span><span id="error_destination_element_full"></span>**ERROR\_DESTINATION\_ELEMENT\_FULL**
</dt> <dd> <dl> <dt>

1161 (0x489)
</dt> <dt>



The indicated destination element already contains media.


</dt> </dl> </dd> <dt>

<span id="ERROR_ILLEGAL_ELEMENT_ADDRESS"></span><span id="error_illegal_element_address"></span>**ERROR\_ILLEGAL\_ELEMENT\_ADDRESS**
</dt> <dd> <dl> <dt>

1162 (0x48A)
</dt> <dt>



The indicated element does not exist.


</dt> </dl> </dd> <dt>

<span id="ERROR_MAGAZINE_NOT_PRESENT"></span><span id="error_magazine_not_present"></span>**ERROR\_MAGAZINE\_NOT\_PRESENT**
</dt> <dd> <dl> <dt>

1163 (0x48B)
</dt> <dt>



The indicated element is part of a magazine that is not present.


</dt> </dl> </dd> <dt>

<span id="ERROR_DEVICE_REINITIALIZATION_NEEDED"></span><span id="error_device_reinitialization_needed"></span>**ERROR\_DEVICE\_REINITIALIZATION\_NEEDED**
</dt> <dd> <dl> <dt>

1164 (0x48C)
</dt> <dt>



The indicated device requires reinitialization due to hardware errors.


</dt> </dl> </dd> <dt>

<span id="ERROR_DEVICE_REQUIRES_CLEANING"></span><span id="error_device_requires_cleaning"></span>**ERROR\_DEVICE\_REQUIRES\_CLEANING**
</dt> <dd> <dl> <dt>

1165 (0x48D)
</dt> <dt>



The device has indicated that cleaning is required before further operations are attempted.


</dt> </dl> </dd> <dt>

<span id="ERROR_DEVICE_DOOR_OPEN"></span><span id="error_device_door_open"></span>**ERROR\_DEVICE\_DOOR\_OPEN**
</dt> <dd> <dl> <dt>

1166 (0x48E)
</dt> <dt>



The device has indicated that its door is open.


</dt> </dl> </dd> <dt>

<span id="ERROR_DEVICE_NOT_CONNECTED"></span><span id="error_device_not_connected"></span>**ERROR\_DEVICE\_NOT\_CONNECTED**
</dt> <dd> <dl> <dt>

1167 (0x48F)
</dt> <dt>



The device is not connected.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_FOUND"></span><span id="error_not_found"></span>**ERROR\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

1168 (0x490)
</dt> <dt>



Element not found.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_MATCH"></span><span id="error_no_match"></span>**ERROR\_NO\_MATCH**
</dt> <dd> <dl> <dt>

1169 (0x491)
</dt> <dt>



There was no match for the specified key in the index.


</dt> </dl> </dd> <dt>

<span id="ERROR_SET_NOT_FOUND"></span><span id="error_set_not_found"></span>**ERROR\_SET\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

1170 (0x492)
</dt> <dt>



The property set specified does not exist on the object.


</dt> </dl> </dd> <dt>

<span id="ERROR_POINT_NOT_FOUND"></span><span id="error_point_not_found"></span>**ERROR\_POINT\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

1171 (0x493)
</dt> <dt>



The point passed to GetMouseMovePoints is not in the buffer.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_TRACKING_SERVICE"></span><span id="error_no_tracking_service"></span>**ERROR\_NO\_TRACKING\_SERVICE**
</dt> <dd> <dl> <dt>

1172 (0x494)
</dt> <dt>



The tracking (workstation) service is not running.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_VOLUME_ID"></span><span id="error_no_volume_id"></span>**ERROR\_NO\_VOLUME\_ID**
</dt> <dd> <dl> <dt>

1173 (0x495)
</dt> <dt>



The Volume ID could not be found.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNABLE_TO_REMOVE_REPLACED"></span><span id="error_unable_to_remove_replaced"></span>**ERROR\_UNABLE\_TO\_REMOVE\_REPLACED**
</dt> <dd> <dl> <dt>

1175 (0x497)
</dt> <dt>



Unable to remove the file to be replaced.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNABLE_TO_MOVE_REPLACEMENT"></span><span id="error_unable_to_move_replacement"></span>**ERROR\_UNABLE\_TO\_MOVE\_REPLACEMENT**
</dt> <dd> <dl> <dt>

1176 (0x498)
</dt> <dt>



Unable to move the replacement file to the file to be replaced. The file to be replaced has retained its original name.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNABLE_TO_MOVE_REPLACEMENT_2"></span><span id="error_unable_to_move_replacement_2"></span>**ERROR\_UNABLE\_TO\_MOVE\_REPLACEMENT\_2**
</dt> <dd> <dl> <dt>

1177 (0x499)
</dt> <dt>



Unable to move the replacement file to the file to be replaced. The file to be replaced has been renamed using the backup name.


</dt> </dl> </dd> <dt>

<span id="ERROR_JOURNAL_DELETE_IN_PROGRESS"></span><span id="error_journal_delete_in_progress"></span>**ERROR\_JOURNAL\_DELETE\_IN\_PROGRESS**
</dt> <dd> <dl> <dt>

1178 (0x49A)
</dt> <dt>



The volume change journal is being deleted.


</dt> </dl> </dd> <dt>

<span id="ERROR_JOURNAL_NOT_ACTIVE"></span><span id="error_journal_not_active"></span>**ERROR\_JOURNAL\_NOT\_ACTIVE**
</dt> <dd> <dl> <dt>

1179 (0x49B)
</dt> <dt>



The volume change journal is not active.


</dt> </dl> </dd> <dt>

<span id="ERROR_POTENTIAL_FILE_FOUND"></span><span id="error_potential_file_found"></span>**ERROR\_POTENTIAL\_FILE\_FOUND**
</dt> <dd> <dl> <dt>

1180 (0x49C)
</dt> <dt>



A file was found, but it may not be the correct file.


</dt> </dl> </dd> <dt>

<span id="ERROR_JOURNAL_ENTRY_DELETED"></span><span id="error_journal_entry_deleted"></span>**ERROR\_JOURNAL\_ENTRY\_DELETED**
</dt> <dd> <dl> <dt>

1181 (0x49D)
</dt> <dt>



The journal entry has been deleted from the journal.


</dt> </dl> </dd> <dt>

<span id="ERROR_SHUTDOWN_IS_SCHEDULED"></span><span id="error_shutdown_is_scheduled"></span>**ERROR\_SHUTDOWN\_IS\_SCHEDULED**
</dt> <dd> <dl> <dt>

1190 (0x4A6)
</dt> <dt>



A system shutdown has already been scheduled.


</dt> </dl> </dd> <dt>

<span id="ERROR_SHUTDOWN_USERS_LOGGED_ON"></span><span id="error_shutdown_users_logged_on"></span>**ERROR\_SHUTDOWN\_USERS\_LOGGED\_ON**
</dt> <dd> <dl> <dt>

1191 (0x4A7)
</dt> <dt>



The system shutdown cannot be initiated because there are other users logged on to the computer.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_DEVICE"></span><span id="error_bad_device"></span>**ERROR\_BAD\_DEVICE**
</dt> <dd> <dl> <dt>

1200 (0x4B0)
</dt> <dt>



The specified device name is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_CONNECTION_UNAVAIL"></span><span id="error_connection_unavail"></span>**ERROR\_CONNECTION\_UNAVAIL**
</dt> <dd> <dl> <dt>

1201 (0x4B1)
</dt> <dt>



The device is not currently connected but it is a remembered connection.


</dt> </dl> </dd> <dt>

<span id="ERROR_DEVICE_ALREADY_REMEMBERED"></span><span id="error_device_already_remembered"></span>**ERROR\_DEVICE\_ALREADY\_REMEMBERED**
</dt> <dd> <dl> <dt>

1202 (0x4B2)
</dt> <dt>



The local device name has a remembered connection to another network resource.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_NET_OR_BAD_PATH"></span><span id="error_no_net_or_bad_path"></span>**ERROR\_NO\_NET\_OR\_BAD\_PATH**
</dt> <dd> <dl> <dt>

1203 (0x4B3)
</dt> <dt>



The network path was either typed incorrectly, does not exist, or the network provider is not currently available. Please try retyping the path or contact your network administrator.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_PROVIDER"></span><span id="error_bad_provider"></span>**ERROR\_BAD\_PROVIDER**
</dt> <dd> <dl> <dt>

1204 (0x4B4)
</dt> <dt>



The specified network provider name is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_CANNOT_OPEN_PROFILE"></span><span id="error_cannot_open_profile"></span>**ERROR\_CANNOT\_OPEN\_PROFILE**
</dt> <dd> <dl> <dt>

1205 (0x4B5)
</dt> <dt>



Unable to open the network connection profile.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_PROFILE"></span><span id="error_bad_profile"></span>**ERROR\_BAD\_PROFILE**
</dt> <dd> <dl> <dt>

1206 (0x4B6)
</dt> <dt>



The network connection profile is corrupted.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_CONTAINER"></span><span id="error_not_container"></span>**ERROR\_NOT\_CONTAINER**
</dt> <dd> <dl> <dt>

1207 (0x4B7)
</dt> <dt>



Cannot enumerate a noncontainer.


</dt> </dl> </dd> <dt>

<span id="ERROR_EXTENDED_ERROR"></span><span id="error_extended_error"></span>**ERROR\_EXTENDED\_ERROR**
</dt> <dd> <dl> <dt>

1208 (0x4B8)
</dt> <dt>



An extended error has occurred.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_GROUPNAME"></span><span id="error_invalid_groupname"></span>**ERROR\_INVALID\_GROUPNAME**
</dt> <dd> <dl> <dt>

1209 (0x4B9)
</dt> <dt>



The format of the specified group name is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_COMPUTERNAME"></span><span id="error_invalid_computername"></span>**ERROR\_INVALID\_COMPUTERNAME**
</dt> <dd> <dl> <dt>

1210 (0x4BA)
</dt> <dt>



The format of the specified computer name is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_EVENTNAME"></span><span id="error_invalid_eventname"></span>**ERROR\_INVALID\_EVENTNAME**
</dt> <dd> <dl> <dt>

1211 (0x4BB)
</dt> <dt>



The format of the specified event name is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_DOMAINNAME"></span><span id="error_invalid_domainname"></span>**ERROR\_INVALID\_DOMAINNAME**
</dt> <dd> <dl> <dt>

1212 (0x4BC)
</dt> <dt>



The format of the specified domain name is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_SERVICENAME"></span><span id="error_invalid_servicename"></span>**ERROR\_INVALID\_SERVICENAME**
</dt> <dd> <dl> <dt>

1213 (0x4BD)
</dt> <dt>



The format of the specified service name is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_NETNAME"></span><span id="error_invalid_netname"></span>**ERROR\_INVALID\_NETNAME**
</dt> <dd> <dl> <dt>

1214 (0x4BE)
</dt> <dt>



The format of the specified network name is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_SHARENAME"></span><span id="error_invalid_sharename"></span>**ERROR\_INVALID\_SHARENAME**
</dt> <dd> <dl> <dt>

1215 (0x4BF)
</dt> <dt>



The format of the specified share name is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_PASSWORDNAME"></span><span id="error_invalid_passwordname"></span>**ERROR\_INVALID\_PASSWORDNAME**
</dt> <dd> <dl> <dt>

1216 (0x4C0)
</dt> <dt>



The format of the specified password is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_MESSAGENAME"></span><span id="error_invalid_messagename"></span>**ERROR\_INVALID\_MESSAGENAME**
</dt> <dd> <dl> <dt>

1217 (0x4C1)
</dt> <dt>



The format of the specified message name is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_MESSAGEDEST"></span><span id="error_invalid_messagedest"></span>**ERROR\_INVALID\_MESSAGEDEST**
</dt> <dd> <dl> <dt>

1218 (0x4C2)
</dt> <dt>



The format of the specified message destination is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_SESSION_CREDENTIAL_CONFLICT"></span><span id="error_session_credential_conflict"></span>**ERROR\_SESSION\_CREDENTIAL\_CONFLICT**
</dt> <dd> <dl> <dt>

1219 (0x4C3)
</dt> <dt>



Multiple connections to a server or shared resource by the same user, using more than one user name, are not allowed. Disconnect all previous connections to the server or shared resource and try again.


</dt> </dl> </dd> <dt>

<span id="ERROR_REMOTE_SESSION_LIMIT_EXCEEDED"></span><span id="error_remote_session_limit_exceeded"></span>**ERROR\_REMOTE\_SESSION\_LIMIT\_EXCEEDED**
</dt> <dd> <dl> <dt>

1220 (0x4C4)
</dt> <dt>



An attempt was made to establish a session to a network server, but there are already too many sessions established to that server.


</dt> </dl> </dd> <dt>

<span id="ERROR_DUP_DOMAINNAME"></span><span id="error_dup_domainname"></span>**ERROR\_DUP\_DOMAINNAME**
</dt> <dd> <dl> <dt>

1221 (0x4C5)
</dt> <dt>



The workgroup or domain name is already in use by another computer on the network.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_NETWORK"></span><span id="error_no_network"></span>**ERROR\_NO\_NETWORK**
</dt> <dd> <dl> <dt>

1222 (0x4C6)
</dt> <dt>



The network is not present or not started.


</dt> </dl> </dd> <dt>

<span id="ERROR_CANCELLED"></span><span id="error_cancelled"></span>**ERROR\_CANCELLED**
</dt> <dd> <dl> <dt>

1223 (0x4C7)
</dt> <dt>



The operation was canceled by the user.


</dt> </dl> </dd> <dt>

<span id="ERROR_USER_MAPPED_FILE"></span><span id="error_user_mapped_file"></span>**ERROR\_USER\_MAPPED\_FILE**
</dt> <dd> <dl> <dt>

1224 (0x4C8)
</dt> <dt>



The requested operation cannot be performed on a file with a user-mapped section open.


</dt> </dl> </dd> <dt>

<span id="ERROR_CONNECTION_REFUSED"></span><span id="error_connection_refused"></span>**ERROR\_CONNECTION\_REFUSED**
</dt> <dd> <dl> <dt>

1225 (0x4C9)
</dt> <dt>



The remote computer refused the network connection.


</dt> </dl> </dd> <dt>

<span id="ERROR_GRACEFUL_DISCONNECT"></span><span id="error_graceful_disconnect"></span>**ERROR\_GRACEFUL\_DISCONNECT**
</dt> <dd> <dl> <dt>

1226 (0x4CA)
</dt> <dt>



The network connection was gracefully closed.


</dt> </dl> </dd> <dt>

<span id="ERROR_ADDRESS_ALREADY_ASSOCIATED"></span><span id="error_address_already_associated"></span>**ERROR\_ADDRESS\_ALREADY\_ASSOCIATED**
</dt> <dd> <dl> <dt>

1227 (0x4CB)
</dt> <dt>



The network transport endpoint already has an address associated with it.


</dt> </dl> </dd> <dt>

<span id="ERROR_ADDRESS_NOT_ASSOCIATED"></span><span id="error_address_not_associated"></span>**ERROR\_ADDRESS\_NOT\_ASSOCIATED**
</dt> <dd> <dl> <dt>

1228 (0x4CC)
</dt> <dt>



An address has not yet been associated with the network endpoint.


</dt> </dl> </dd> <dt>

<span id="ERROR_CONNECTION_INVALID"></span><span id="error_connection_invalid"></span>**ERROR\_CONNECTION\_INVALID**
</dt> <dd> <dl> <dt>

1229 (0x4CD)
</dt> <dt>



An operation was attempted on a nonexistent network connection.


</dt> </dl> </dd> <dt>

<span id="ERROR_CONNECTION_ACTIVE"></span><span id="error_connection_active"></span>**ERROR\_CONNECTION\_ACTIVE**
</dt> <dd> <dl> <dt>

1230 (0x4CE)
</dt> <dt>



An invalid operation was attempted on an active network connection.


</dt> </dl> </dd> <dt>

<span id="ERROR_NETWORK_UNREACHABLE"></span><span id="error_network_unreachable"></span>**ERROR\_NETWORK\_UNREACHABLE**
</dt> <dd> <dl> <dt>

1231 (0x4CF)
</dt> <dt>



The network location cannot be reached. For information about network troubleshooting, see Windows Help.


</dt> </dl> </dd> <dt>

<span id="ERROR_HOST_UNREACHABLE"></span><span id="error_host_unreachable"></span>**ERROR\_HOST\_UNREACHABLE**
</dt> <dd> <dl> <dt>

1232 (0x4D0)
</dt> <dt>



The network location cannot be reached. For information about network troubleshooting, see Windows Help.


</dt> </dl> </dd> <dt>

<span id="ERROR_PROTOCOL_UNREACHABLE"></span><span id="error_protocol_unreachable"></span>**ERROR\_PROTOCOL\_UNREACHABLE**
</dt> <dd> <dl> <dt>

1233 (0x4D1)
</dt> <dt>



The network location cannot be reached. For information about network troubleshooting, see Windows Help.


</dt> </dl> </dd> <dt>

<span id="ERROR_PORT_UNREACHABLE"></span><span id="error_port_unreachable"></span>**ERROR\_PORT\_UNREACHABLE**
</dt> <dd> <dl> <dt>

1234 (0x4D2)
</dt> <dt>



No service is operating at the destination network endpoint on the remote system.


</dt> </dl> </dd> <dt>

<span id="ERROR_REQUEST_ABORTED"></span><span id="error_request_aborted"></span>**ERROR\_REQUEST\_ABORTED**
</dt> <dd> <dl> <dt>

1235 (0x4D3)
</dt> <dt>



The request was aborted.


</dt> </dl> </dd> <dt>

<span id="ERROR_CONNECTION_ABORTED"></span><span id="error_connection_aborted"></span>**ERROR\_CONNECTION\_ABORTED**
</dt> <dd> <dl> <dt>

1236 (0x4D4)
</dt> <dt>



The network connection was aborted by the local system.


</dt> </dl> </dd> <dt>

<span id="ERROR_RETRY"></span><span id="error_retry"></span>**ERROR\_RETRY**
</dt> <dd> <dl> <dt>

1237 (0x4D5)
</dt> <dt>



The operation could not be completed. A retry should be performed.


</dt> </dl> </dd> <dt>

<span id="ERROR_CONNECTION_COUNT_LIMIT"></span><span id="error_connection_count_limit"></span>**ERROR\_CONNECTION\_COUNT\_LIMIT**
</dt> <dd> <dl> <dt>

1238 (0x4D6)
</dt> <dt>



A connection to the server could not be made because the limit on the number of concurrent connections for this account has been reached.


</dt> </dl> </dd> <dt>

<span id="ERROR_LOGIN_TIME_RESTRICTION"></span><span id="error_login_time_restriction"></span>**ERROR\_LOGIN\_TIME\_RESTRICTION**
</dt> <dd> <dl> <dt>

1239 (0x4D7)
</dt> <dt>



Attempting to log in during an unauthorized time of day for this account.


</dt> </dl> </dd> <dt>

<span id="ERROR_LOGIN_WKSTA_RESTRICTION"></span><span id="error_login_wksta_restriction"></span>**ERROR\_LOGIN\_WKSTA\_RESTRICTION**
</dt> <dd> <dl> <dt>

1240 (0x4D8)
</dt> <dt>



The account is not authorized to log in from this station.


</dt> </dl> </dd> <dt>

<span id="ERROR_INCORRECT_ADDRESS"></span><span id="error_incorrect_address"></span>**ERROR\_INCORRECT\_ADDRESS**
</dt> <dd> <dl> <dt>

1241 (0x4D9)
</dt> <dt>



The network address could not be used for the operation requested.


</dt> </dl> </dd> <dt>

<span id="ERROR_ALREADY_REGISTERED"></span><span id="error_already_registered"></span>**ERROR\_ALREADY\_REGISTERED**
</dt> <dd> <dl> <dt>

1242 (0x4DA)
</dt> <dt>



The service is already registered.


</dt> </dl> </dd> <dt>

<span id="ERROR_SERVICE_NOT_FOUND"></span><span id="error_service_not_found"></span>**ERROR\_SERVICE\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

1243 (0x4DB)
</dt> <dt>



The specified service does not exist.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_AUTHENTICATED"></span><span id="error_not_authenticated"></span>**ERROR\_NOT\_AUTHENTICATED**
</dt> <dd> <dl> <dt>

1244 (0x4DC)
</dt> <dt>



The operation being requested was not performed because the user has not been authenticated.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_LOGGED_ON"></span><span id="error_not_logged_on"></span>**ERROR\_NOT\_LOGGED\_ON**
</dt> <dd> <dl> <dt>

1245 (0x4DD)
</dt> <dt>



The operation being requested was not performed because the user has not logged on to the network. The specified service does not exist.


</dt> </dl> </dd> <dt>

<span id="ERROR_CONTINUE"></span><span id="error_continue"></span>**ERROR\_CONTINUE**
</dt> <dd> <dl> <dt>

1246 (0x4DE)
</dt> <dt>



Continue with work in progress.


</dt> </dl> </dd> <dt>

<span id="ERROR_ALREADY_INITIALIZED"></span><span id="error_already_initialized"></span>**ERROR\_ALREADY\_INITIALIZED**
</dt> <dd> <dl> <dt>

1247 (0x4DF)
</dt> <dt>



An attempt was made to perform an initialization operation when initialization has already been completed.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_MORE_DEVICES"></span><span id="error_no_more_devices"></span>**ERROR\_NO\_MORE\_DEVICES**
</dt> <dd> <dl> <dt>

1248 (0x4E0)
</dt> <dt>



No more local devices.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_SUCH_SITE"></span><span id="error_no_such_site"></span>**ERROR\_NO\_SUCH\_SITE**
</dt> <dd> <dl> <dt>

1249 (0x4E1)
</dt> <dt>



The specified site does not exist.


</dt> </dl> </dd> <dt>

<span id="ERROR_DOMAIN_CONTROLLER_EXISTS"></span><span id="error_domain_controller_exists"></span>**ERROR\_DOMAIN\_CONTROLLER\_EXISTS**
</dt> <dd> <dl> <dt>

1250 (0x4E2)
</dt> <dt>



A domain controller with the specified name already exists.


</dt> </dl> </dd> <dt>

<span id="ERROR_ONLY_IF_CONNECTED"></span><span id="error_only_if_connected"></span>**ERROR\_ONLY\_IF\_CONNECTED**
</dt> <dd> <dl> <dt>

1251 (0x4E3)
</dt> <dt>



This operation is supported only when you are connected to the server.


</dt> </dl> </dd> <dt>

<span id="ERROR_OVERRIDE_NOCHANGES"></span><span id="error_override_nochanges"></span>**ERROR\_OVERRIDE\_NOCHANGES**
</dt> <dd> <dl> <dt>

1252 (0x4E4)
</dt> <dt>



The group policy framework should call the extension even if there are no changes.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_USER_PROFILE"></span><span id="error_bad_user_profile"></span>**ERROR\_BAD\_USER\_PROFILE**
</dt> <dd> <dl> <dt>

1253 (0x4E5)
</dt> <dt>



The specified user does not have a valid profile.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_SUPPORTED_ON_SBS"></span><span id="error_not_supported_on_sbs"></span>**ERROR\_NOT\_SUPPORTED\_ON\_SBS**
</dt> <dd> <dl> <dt>

1254 (0x4E6)
</dt> <dt>



This operation is not supported on a computer running Windows Server 2003 for Small Business Server.


</dt> </dl> </dd> <dt>

<span id="ERROR_SERVER_SHUTDOWN_IN_PROGRESS"></span><span id="error_server_shutdown_in_progress"></span>**ERROR\_SERVER\_SHUTDOWN\_IN\_PROGRESS**
</dt> <dd> <dl> <dt>

1255 (0x4E7)
</dt> <dt>



The server machine is shutting down.


</dt> </dl> </dd> <dt>

<span id="ERROR_HOST_DOWN"></span><span id="error_host_down"></span>**ERROR\_HOST\_DOWN**
</dt> <dd> <dl> <dt>

1256 (0x4E8)
</dt> <dt>



The remote system is not available. For information about network troubleshooting, see Windows Help.


</dt> </dl> </dd> <dt>

<span id="ERROR_NON_ACCOUNT_SID"></span><span id="error_non_account_sid"></span>**ERROR\_NON\_ACCOUNT\_SID**
</dt> <dd> <dl> <dt>

1257 (0x4E9)
</dt> <dt>



The security identifier provided is not from an account domain.


</dt> </dl> </dd> <dt>

<span id="ERROR_NON_DOMAIN_SID"></span><span id="error_non_domain_sid"></span>**ERROR\_NON\_DOMAIN\_SID**
</dt> <dd> <dl> <dt>

1258 (0x4EA)
</dt> <dt>



The security identifier provided does not have a domain component.


</dt> </dl> </dd> <dt>

<span id="ERROR_APPHELP_BLOCK"></span><span id="error_apphelp_block"></span>**ERROR\_APPHELP\_BLOCK**
</dt> <dd> <dl> <dt>

1259 (0x4EB)
</dt> <dt>



AppHelp dialog canceled thus preventing the application from starting.


</dt> </dl> </dd> <dt>

<span id="ERROR_ACCESS_DISABLED_BY_POLICY"></span><span id="error_access_disabled_by_policy"></span>**ERROR\_ACCESS\_DISABLED\_BY\_POLICY**
</dt> <dd> <dl> <dt>

1260 (0x4EC)
</dt> <dt>



This program is blocked by group policy. For more information, contact your system administrator.


</dt> </dl> </dd> <dt>

<span id="ERROR_REG_NAT_CONSUMPTION"></span><span id="error_reg_nat_consumption"></span>**ERROR\_REG\_NAT\_CONSUMPTION**
</dt> <dd> <dl> <dt>

1261 (0x4ED)
</dt> <dt>



A program attempt to use an invalid register value. Normally caused by an uninitialized register. This error is Itanium specific.


</dt> </dl> </dd> <dt>

<span id="ERROR_CSCSHARE_OFFLINE"></span><span id="error_cscshare_offline"></span>**ERROR\_CSCSHARE\_OFFLINE**
</dt> <dd> <dl> <dt>

1262 (0x4EE)
</dt> <dt>



The share is currently offline or does not exist.


</dt> </dl> </dd> <dt>

<span id="ERROR_PKINIT_FAILURE"></span><span id="error_pkinit_failure"></span>**ERROR\_PKINIT\_FAILURE**
</dt> <dd> <dl> <dt>

1263 (0x4EF)
</dt> <dt>



The Kerberos protocol encountered an error while validating the KDC certificate during smartcard logon. There is more information in the system event log.


</dt> </dl> </dd> <dt>

<span id="ERROR_SMARTCARD_SUBSYSTEM_FAILURE"></span><span id="error_smartcard_subsystem_failure"></span>**ERROR\_SMARTCARD\_SUBSYSTEM\_FAILURE**
</dt> <dd> <dl> <dt>

1264 (0x4F0)
</dt> <dt>



The Kerberos protocol encountered an error while attempting to utilize the smartcard subsystem.


</dt> </dl> </dd> <dt>

<span id="ERROR_DOWNGRADE_DETECTED"></span><span id="error_downgrade_detected"></span>**ERROR\_DOWNGRADE\_DETECTED**
</dt> <dd> <dl> <dt>

1265 (0x4F1)
</dt> <dt>



The system cannot contact a domain controller to service the authentication request. Please try again later.


</dt> </dl> </dd> <dt>

<span id="ERROR_MACHINE_LOCKED"></span><span id="error_machine_locked"></span>**ERROR\_MACHINE\_LOCKED**
</dt> <dd> <dl> <dt>

1271 (0x4F7)
</dt> <dt>



The machine is locked and cannot be shut down without the force option.


</dt> </dl> </dd> <dt>

<span id="ERROR_CALLBACK_SUPPLIED_INVALID_DATA"></span><span id="error_callback_supplied_invalid_data"></span>**ERROR\_CALLBACK\_SUPPLIED\_INVALID\_DATA**
</dt> <dd> <dl> <dt>

1273 (0x4F9)
</dt> <dt>



An application-defined callback gave invalid data when called.


</dt> </dl> </dd> <dt>

<span id="ERROR_SYNC_FOREGROUND_REFRESH_REQUIRED"></span><span id="error_sync_foreground_refresh_required"></span>**ERROR\_SYNC\_FOREGROUND\_REFRESH\_REQUIRED**
</dt> <dd> <dl> <dt>

1274 (0x4FA)
</dt> <dt>



The group policy framework should call the extension in the synchronous foreground policy refresh.


</dt> </dl> </dd> <dt>

<span id="ERROR_DRIVER_BLOCKED"></span><span id="error_driver_blocked"></span>**ERROR\_DRIVER\_BLOCKED**
</dt> <dd> <dl> <dt>

1275 (0x4FB)
</dt> <dt>



This driver has been blocked from loading.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_IMPORT_OF_NON_DLL"></span><span id="error_invalid_import_of_non_dll"></span>**ERROR\_INVALID\_IMPORT\_OF\_NON\_DLL**
</dt> <dd> <dl> <dt>

1276 (0x4FC)
</dt> <dt>



A dynamic link library (DLL) referenced a module that was neither a DLL nor the process's executable image.


</dt> </dl> </dd> <dt>

<span id="ERROR_ACCESS_DISABLED_WEBBLADE"></span><span id="error_access_disabled_webblade"></span>**ERROR\_ACCESS\_DISABLED\_WEBBLADE**
</dt> <dd> <dl> <dt>

1277 (0x4FD)
</dt> <dt>



Windows cannot open this program since it has been disabled.


</dt> </dl> </dd> <dt>

<span id="ERROR_ACCESS_DISABLED_WEBBLADE_TAMPER"></span><span id="error_access_disabled_webblade_tamper"></span>**ERROR\_ACCESS\_DISABLED\_WEBBLADE\_TAMPER**
</dt> <dd> <dl> <dt>

1278 (0x4FE)
</dt> <dt>



Windows cannot open this program because the license enforcement system has been tampered with or become corrupted.


</dt> </dl> </dd> <dt>

<span id="ERROR_RECOVERY_FAILURE"></span><span id="error_recovery_failure"></span>**ERROR\_RECOVERY\_FAILURE**
</dt> <dd> <dl> <dt>

1279 (0x4FF)
</dt> <dt>



A transaction recover failed.


</dt> </dl> </dd> <dt>

<span id="ERROR_ALREADY_FIBER"></span><span id="error_already_fiber"></span>**ERROR\_ALREADY\_FIBER**
</dt> <dd> <dl> <dt>

1280 (0x500)
</dt> <dt>



The current thread has already been converted to a fiber.


</dt> </dl> </dd> <dt>

<span id="ERROR_ALREADY_THREAD"></span><span id="error_already_thread"></span>**ERROR\_ALREADY\_THREAD**
</dt> <dd> <dl> <dt>

1281 (0x501)
</dt> <dt>



The current thread has already been converted from a fiber.


</dt> </dl> </dd> <dt>

<span id="ERROR_STACK_BUFFER_OVERRUN"></span><span id="error_stack_buffer_overrun"></span>**ERROR\_STACK\_BUFFER\_OVERRUN**
</dt> <dd> <dl> <dt>

1282 (0x502)
</dt> <dt>



The system detected an overrun of a stack-based buffer in this application. This overrun could potentially allow a malicious user to gain control of this application.


</dt> </dl> </dd> <dt>

<span id="ERROR_PARAMETER_QUOTA_EXCEEDED"></span><span id="error_parameter_quota_exceeded"></span>**ERROR\_PARAMETER\_QUOTA\_EXCEEDED**
</dt> <dd> <dl> <dt>

1283 (0x503)
</dt> <dt>



Data present in one of the parameters is more than the function can operate on.


</dt> </dl> </dd> <dt>

<span id="ERROR_DEBUGGER_INACTIVE"></span><span id="error_debugger_inactive"></span>**ERROR\_DEBUGGER\_INACTIVE**
</dt> <dd> <dl> <dt>

1284 (0x504)
</dt> <dt>



An attempt to do an operation on a debug object failed because the object is in the process of being deleted.


</dt> </dl> </dd> <dt>

<span id="ERROR_DELAY_LOAD_FAILED"></span><span id="error_delay_load_failed"></span>**ERROR\_DELAY\_LOAD\_FAILED**
</dt> <dd> <dl> <dt>

1285 (0x505)
</dt> <dt>



An attempt to delay-load a .dll or get a function address in a delay-loaded .dll failed.


</dt> </dl> </dd> <dt>

<span id="ERROR_VDM_DISALLOWED"></span><span id="error_vdm_disallowed"></span>**ERROR\_VDM\_DISALLOWED**
</dt> <dd> <dl> <dt>

1286 (0x506)
</dt> <dt>



%1 is a 16-bit application. You do not have permissions to execute 16-bit applications. Check your permissions with your system administrator.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNIDENTIFIED_ERROR"></span><span id="error_unidentified_error"></span>**ERROR\_UNIDENTIFIED\_ERROR**
</dt> <dd> <dl> <dt>

1287 (0x507)
</dt> <dt>



Insufficient information exists to identify the cause of failure.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_CRUNTIME_PARAMETER"></span><span id="error_invalid_cruntime_parameter"></span>**ERROR\_INVALID\_CRUNTIME\_PARAMETER**
</dt> <dd> <dl> <dt>

1288 (0x508)
</dt> <dt>



The parameter passed to a C runtime function is incorrect.


</dt> </dl> </dd> <dt>

<span id="ERROR_BEYOND_VDL"></span><span id="error_beyond_vdl"></span>**ERROR\_BEYOND\_VDL**
</dt> <dd> <dl> <dt>

1289 (0x509)
</dt> <dt>



The operation occurred beyond the valid data length of the file.


</dt> </dl> </dd> <dt>

<span id="ERROR_INCOMPATIBLE_SERVICE_SID_TYPE"></span><span id="error_incompatible_service_sid_type"></span>**ERROR\_INCOMPATIBLE\_SERVICE\_SID\_TYPE**
</dt> <dd> <dl> <dt>

1290 (0x50A)
</dt> <dt>



The service start failed since one or more services in the same process have an incompatible service SID type setting. A service with restricted service SID type can only coexist in the same process with other services with a restricted SID type. If the service SID type for this service was just configured, the hosting process must be restarted in order to start this service.

On Windows Server 2003 and Windows XP, an unrestricted service cannot coexist in the same process with other services. The service with the unrestricted service SID type must be moved to an owned process in order to start this service.


</dt> </dl> </dd> <dt>

<span id="ERROR_DRIVER_PROCESS_TERMINATED"></span><span id="error_driver_process_terminated"></span>**ERROR\_DRIVER\_PROCESS\_TERMINATED**
</dt> <dd> <dl> <dt>

1291 (0x50B)
</dt> <dt>



The process hosting the driver for this device has been terminated.


</dt> </dl> </dd> <dt>

<span id="ERROR_IMPLEMENTATION_LIMIT"></span><span id="error_implementation_limit"></span>**ERROR\_IMPLEMENTATION\_LIMIT**
</dt> <dd> <dl> <dt>

1292 (0x50C)
</dt> <dt>



An operation attempted to exceed an implementation-defined limit.


</dt> </dl> </dd> <dt>

<span id="ERROR_PROCESS_IS_PROTECTED"></span><span id="error_process_is_protected"></span>**ERROR\_PROCESS\_IS\_PROTECTED**
</dt> <dd> <dl> <dt>

1293 (0x50D)
</dt> <dt>



Either the target process, or the target thread's containing process, is a protected process.


</dt> </dl> </dd> <dt>

<span id="ERROR_SERVICE_NOTIFY_CLIENT_LAGGING"></span><span id="error_service_notify_client_lagging"></span>**ERROR\_SERVICE\_NOTIFY\_CLIENT\_LAGGING**
</dt> <dd> <dl> <dt>

1294 (0x50E)
</dt> <dt>



The service notification client is lagging too far behind the current state of services in the machine.


</dt> </dl> </dd> <dt>

<span id="ERROR_DISK_QUOTA_EXCEEDED"></span><span id="error_disk_quota_exceeded"></span>**ERROR\_DISK\_QUOTA\_EXCEEDED**
</dt> <dd> <dl> <dt>

1295 (0x50F)
</dt> <dt>



The requested file operation failed because the storage quota was exceeded. To free up disk space, move files to a different location or delete unnecessary files. For more information, contact your system administrator.


</dt> </dl> </dd> <dt>

<span id="ERROR_CONTENT_BLOCKED"></span><span id="error_content_blocked"></span>**ERROR\_CONTENT\_BLOCKED**
</dt> <dd> <dl> <dt>

1296 (0x510)
</dt> <dt>



The requested file operation failed because the storage policy blocks that type of file. For more information, contact your system administrator.


</dt> </dl> </dd> <dt>

<span id="ERROR_INCOMPATIBLE_SERVICE_PRIVILEGE"></span><span id="error_incompatible_service_privilege"></span>**ERROR\_INCOMPATIBLE\_SERVICE\_PRIVILEGE**
</dt> <dd> <dl> <dt>

1297 (0x511)
</dt> <dt>



A privilege that the service requires to function properly does not exist in the service account configuration. You may use the Services Microsoft Management Console (MMC) snap-in (services.msc) and the Local Security Settings MMC snap-in (secpol.msc) to view the service configuration and the account configuration.


</dt> </dl> </dd> <dt>

<span id="ERROR_APP_HANG"></span><span id="error_app_hang"></span>**ERROR\_APP\_HANG**
</dt> <dd> <dl> <dt>

1298 (0x512)
</dt> <dt>



A thread involved in this operation appears to be unresponsive.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_LABEL"></span><span id="error_invalid_label"></span>**ERROR\_INVALID\_LABEL**
</dt> <dd> <dl> <dt>

1299 (0x513)
</dt> <dt>



Indicates a particular Security ID may not be assigned as the label of an object.


</dt> </dl> </dd> </dl>


## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>WinError.h</dt> </dl> |



## See also

<dl> <dt>

[System Error Codes](system-error-codes.md)
</dt> </dl>

 

 





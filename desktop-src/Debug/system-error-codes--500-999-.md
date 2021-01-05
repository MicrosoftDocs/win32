---
description: Describes error codes 500-999 defined in the WinError.h header file and is intended for developers.
ms.assetid: 8d8b427b-b761-4023-a834-a6eff96d6ba1
title: System Error Codes (500-999) (WinError.h)
ms.topic: reference
ms.date: 07/18/2019
---

# System Error Codes (500-999)

> [!NOTE]
> This information is intended for developers debugging system errors. For other errors, such as issues with Windows Update, there is a list of resources on the [Error codes](system-error-codes.md) page.

The following list describes [system error codes](system-error-codes.md) (errors 500 to 999). They are returned by the [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) function when many functions fail. To retrieve the description text for the error in your application, use the [**FormatMessage**](/windows/desktop/api/WinBase/nf-winbase-formatmessage) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag.

<dl> <dt>

<span id="ERROR_USER_PROFILE_LOAD"></span><span id="error_user_profile_load"></span>**ERROR\_USER\_PROFILE\_LOAD**
</dt> <dd> <dl> <dt>

500 (0x1F4)
</dt> <dt>



User profile cannot be loaded.


</dt> </dl> </dd> <dt>

<span id="ERROR_ARITHMETIC_OVERFLOW"></span><span id="error_arithmetic_overflow"></span>**ERROR\_ARITHMETIC\_OVERFLOW**
</dt> <dd> <dl> <dt>

534 (0x216)
</dt> <dt>



Arithmetic result exceeded 32 bits.


</dt> </dl> </dd> <dt>

<span id="ERROR_PIPE_CONNECTED"></span><span id="error_pipe_connected"></span>**ERROR\_PIPE\_CONNECTED**
</dt> <dd> <dl> <dt>

535 (0x217)
</dt> <dt>



There is a process on other end of the pipe.


</dt> </dl> </dd> <dt>

<span id="ERROR_PIPE_LISTENING"></span><span id="error_pipe_listening"></span>**ERROR\_PIPE\_LISTENING**
</dt> <dd> <dl> <dt>

536 (0x218)
</dt> <dt>



Waiting for a process to open the other end of the pipe.


</dt> </dl> </dd> <dt>

<span id="ERROR_VERIFIER_STOP"></span><span id="error_verifier_stop"></span>**ERROR\_VERIFIER\_STOP**
</dt> <dd> <dl> <dt>

537 (0x219)
</dt> <dt>



Application verifier has found an error in the current process.


</dt> </dl> </dd> <dt>

<span id="ERROR_ABIOS_ERROR"></span><span id="error_abios_error"></span>**ERROR\_ABIOS\_ERROR**
</dt> <dd> <dl> <dt>

538 (0x21A)
</dt> <dt>



An error occurred in the ABIOS subsystem.


</dt> </dl> </dd> <dt>

<span id="ERROR_WX86_WARNING"></span><span id="error_wx86_warning"></span>**ERROR\_WX86\_WARNING**
</dt> <dd> <dl> <dt>

539 (0x21B)
</dt> <dt>



A warning occurred in the WX86 subsystem.


</dt> </dl> </dd> <dt>

<span id="ERROR_WX86_ERROR"></span><span id="error_wx86_error"></span>**ERROR\_WX86\_ERROR**
</dt> <dd> <dl> <dt>

540 (0x21C)
</dt> <dt>



An error occurred in the WX86 subsystem.


</dt> </dl> </dd> <dt>

<span id="ERROR_TIMER_NOT_CANCELED"></span><span id="error_timer_not_canceled"></span>**ERROR\_TIMER\_NOT\_CANCELED**
</dt> <dd> <dl> <dt>

541 (0x21D)
</dt> <dt>



An attempt was made to cancel or set a timer that has an associated APC and the subject thread is not the thread that originally set the timer with an associated APC routine.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNWIND"></span><span id="error_unwind"></span>**ERROR\_UNWIND**
</dt> <dd> <dl> <dt>

542 (0x21E)
</dt> <dt>



Unwind exception code.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_STACK"></span><span id="error_bad_stack"></span>**ERROR\_BAD\_STACK**
</dt> <dd> <dl> <dt>

543 (0x21F)
</dt> <dt>



An invalid or unaligned stack was encountered during an unwind operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_UNWIND_TARGET"></span><span id="error_invalid_unwind_target"></span>**ERROR\_INVALID\_UNWIND\_TARGET**
</dt> <dd> <dl> <dt>

544 (0x220)
</dt> <dt>



An invalid unwind target was encountered during an unwind operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_PORT_ATTRIBUTES"></span><span id="error_invalid_port_attributes"></span>**ERROR\_INVALID\_PORT\_ATTRIBUTES**
</dt> <dd> <dl> <dt>

545 (0x221)
</dt> <dt>



Invalid Object Attributes specified to NtCreatePort or invalid Port Attributes specified to NtConnectPort


</dt> </dl> </dd> <dt>

<span id="ERROR_PORT_MESSAGE_TOO_LONG"></span><span id="error_port_message_too_long"></span>**ERROR\_PORT\_MESSAGE\_TOO\_LONG**
</dt> <dd> <dl> <dt>

546 (0x222)
</dt> <dt>



Length of message passed to NtRequestPort or NtRequestWaitReplyPort was longer than the maximum message allowed by the port.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_QUOTA_LOWER"></span><span id="error_invalid_quota_lower"></span>**ERROR\_INVALID\_QUOTA\_LOWER**
</dt> <dd> <dl> <dt>

547 (0x223)
</dt> <dt>



An attempt was made to lower a quota limit below the current usage.


</dt> </dl> </dd> <dt>

<span id="ERROR_DEVICE_ALREADY_ATTACHED"></span><span id="error_device_already_attached"></span>**ERROR\_DEVICE\_ALREADY\_ATTACHED**
</dt> <dd> <dl> <dt>

548 (0x224)
</dt> <dt>



An attempt was made to attach to a device that was already attached to another device.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSTRUCTION_MISALIGNMENT"></span><span id="error_instruction_misalignment"></span>**ERROR\_INSTRUCTION\_MISALIGNMENT**
</dt> <dd> <dl> <dt>

549 (0x225)
</dt> <dt>



An attempt was made to execute an instruction at an unaligned address and the host system does not support unaligned instruction references.


</dt> </dl> </dd> <dt>

<span id="ERROR_PROFILING_NOT_STARTED"></span><span id="error_profiling_not_started"></span>**ERROR\_PROFILING\_NOT\_STARTED**
</dt> <dd> <dl> <dt>

550 (0x226)
</dt> <dt>



Profiling not started.


</dt> </dl> </dd> <dt>

<span id="ERROR_PROFILING_NOT_STOPPED"></span><span id="error_profiling_not_stopped"></span>**ERROR\_PROFILING\_NOT\_STOPPED**
</dt> <dd> <dl> <dt>

551 (0x227)
</dt> <dt>



Profiling not stopped.


</dt> </dl> </dd> <dt>

<span id="ERROR_COULD_NOT_INTERPRET"></span><span id="error_could_not_interpret"></span>**ERROR\_COULD\_NOT\_INTERPRET**
</dt> <dd> <dl> <dt>

552 (0x228)
</dt> <dt>



The passed ACL did not contain the minimum required information.


</dt> </dl> </dd> <dt>

<span id="ERROR_PROFILING_AT_LIMIT"></span><span id="error_profiling_at_limit"></span>**ERROR\_PROFILING\_AT\_LIMIT**
</dt> <dd> <dl> <dt>

553 (0x229)
</dt> <dt>



The number of active profiling objects is at the maximum and no more may be started.


</dt> </dl> </dd> <dt>

<span id="ERROR_CANT_WAIT"></span><span id="error_cant_wait"></span>**ERROR\_CANT\_WAIT**
</dt> <dd> <dl> <dt>

554 (0x22A)
</dt> <dt>



Used to indicate that an operation cannot continue without blocking for I/O.


</dt> </dl> </dd> <dt>

<span id="ERROR_CANT_TERMINATE_SELF"></span><span id="error_cant_terminate_self"></span>**ERROR\_CANT\_TERMINATE\_SELF**
</dt> <dd> <dl> <dt>

555 (0x22B)
</dt> <dt>



Indicates that a thread attempted to terminate itself by default (called NtTerminateThread with **NULL**) and it was the last thread in the current process.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNEXPECTED_MM_CREATE_ERR"></span><span id="error_unexpected_mm_create_err"></span>**ERROR\_UNEXPECTED\_MM\_CREATE\_ERR**
</dt> <dd> <dl> <dt>

556 (0x22C)
</dt> <dt>



If an MM error is returned which is not defined in the standard FsRtl filter, it is converted to one of the following errors which is guaranteed to be in the filter. In this case information is lost, however, the filter correctly handles the exception.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNEXPECTED_MM_MAP_ERROR"></span><span id="error_unexpected_mm_map_error"></span>**ERROR\_UNEXPECTED\_MM\_MAP\_ERROR**
</dt> <dd> <dl> <dt>

557 (0x22D)
</dt> <dt>



If an MM error is returned which is not defined in the standard FsRtl filter, it is converted to one of the following errors which is guaranteed to be in the filter. In this case information is lost, however, the filter correctly handles the exception.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNEXPECTED_MM_EXTEND_ERR"></span><span id="error_unexpected_mm_extend_err"></span>**ERROR\_UNEXPECTED\_MM\_EXTEND\_ERR**
</dt> <dd> <dl> <dt>

558 (0x22E)
</dt> <dt>



If an MM error is returned which is not defined in the standard FsRtl filter, it is converted to one of the following errors which is guaranteed to be in the filter. In this case information is lost, however, the filter correctly handles the exception.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_FUNCTION_TABLE"></span><span id="error_bad_function_table"></span>**ERROR\_BAD\_FUNCTION\_TABLE**
</dt> <dd> <dl> <dt>

559 (0x22F)
</dt> <dt>



A malformed function table was encountered during an unwind operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_GUID_TRANSLATION"></span><span id="error_no_guid_translation"></span>**ERROR\_NO\_GUID\_TRANSLATION**
</dt> <dd> <dl> <dt>

560 (0x230)
</dt> <dt>



Indicates that an attempt was made to assign protection to a file system file or directory and one of the SIDs in the security descriptor could not be translated into a GUID that could be stored by the file system. This causes the protection attempt to fail, which may cause a file creation attempt to fail.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_LDT_SIZE"></span><span id="error_invalid_ldt_size"></span>**ERROR\_INVALID\_LDT\_SIZE**
</dt> <dd> <dl> <dt>

561 (0x231)
</dt> <dt>



Indicates that an attempt was made to grow an LDT by setting its size, or that the size was not an even number of selectors.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_LDT_OFFSET"></span><span id="error_invalid_ldt_offset"></span>**ERROR\_INVALID\_LDT\_OFFSET**
</dt> <dd> <dl> <dt>

563 (0x233)
</dt> <dt>



Indicates that the starting value for the LDT information was not an integral multiple of the selector size.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_LDT_DESCRIPTOR"></span><span id="error_invalid_ldt_descriptor"></span>**ERROR\_INVALID\_LDT\_DESCRIPTOR**
</dt> <dd> <dl> <dt>

564 (0x234)
</dt> <dt>



Indicates that the user supplied an invalid descriptor when trying to set up Ldt descriptors.


</dt> </dl> </dd> <dt>

<span id="ERROR_TOO_MANY_THREADS"></span><span id="error_too_many_threads"></span>**ERROR\_TOO\_MANY\_THREADS**
</dt> <dd> <dl> <dt>

565 (0x235)
</dt> <dt>



Indicates a process has too many threads to perform the requested action. For example, assignment of a primary token may only be performed when a process has zero or one threads.


</dt> </dl> </dd> <dt>

<span id="ERROR_THREAD_NOT_IN_PROCESS"></span><span id="error_thread_not_in_process"></span>**ERROR\_THREAD\_NOT\_IN\_PROCESS**
</dt> <dd> <dl> <dt>

566 (0x236)
</dt> <dt>



An attempt was made to operate on a thread within a specific process, but the thread specified is not in the process specified.


</dt> </dl> </dd> <dt>

<span id="ERROR_PAGEFILE_QUOTA_EXCEEDED"></span><span id="error_pagefile_quota_exceeded"></span>**ERROR\_PAGEFILE\_QUOTA\_EXCEEDED**
</dt> <dd> <dl> <dt>

567 (0x237)
</dt> <dt>



Page file quota was exceeded.


</dt> </dl> </dd> <dt>

<span id="ERROR_LOGON_SERVER_CONFLICT"></span><span id="error_logon_server_conflict"></span>**ERROR\_LOGON\_SERVER\_CONFLICT**
</dt> <dd> <dl> <dt>

568 (0x238)
</dt> <dt>



The Netlogon service cannot start because another Netlogon service running in the domain conflicts with the specified role.


</dt> </dl> </dd> <dt>

<span id="ERROR_SYNCHRONIZATION_REQUIRED"></span><span id="error_synchronization_required"></span>**ERROR\_SYNCHRONIZATION\_REQUIRED**
</dt> <dd> <dl> <dt>

569 (0x239)
</dt> <dt>



The SAM database on a Windows Server is significantly out of synchronization with the copy on the Domain Controller. A complete synchronization is required.


</dt> </dl> </dd> <dt>

<span id="ERROR_NET_OPEN_FAILED"></span><span id="error_net_open_failed"></span>**ERROR\_NET\_OPEN\_FAILED**
</dt> <dd> <dl> <dt>

570 (0x23A)
</dt> <dt>



The NtCreateFile API failed. This error should never be returned to an application, it is a place holder for the Windows Lan Manager Redirector to use in its internal error mapping routines.


</dt> </dl> </dd> <dt>

<span id="ERROR_IO_PRIVILEGE_FAILED"></span><span id="error_io_privilege_failed"></span>**ERROR\_IO\_PRIVILEGE\_FAILED**
</dt> <dd> <dl> <dt>

571 (0x23B)
</dt> <dt>



{Privilege Failed} The I/O permissions for the process could not be changed.


</dt> </dl> </dd> <dt>

<span id="ERROR_CONTROL_C_EXIT"></span><span id="error_control_c_exit"></span>**ERROR\_CONTROL\_C\_EXIT**
</dt> <dd> <dl> <dt>

572 (0x23C)
</dt> <dt>



{Application Exit by CTRL+C} The application terminated as a result of a CTRL+C.


</dt> </dl> </dd> <dt>

<span id="ERROR_MISSING_SYSTEMFILE"></span><span id="error_missing_systemfile"></span>**ERROR\_MISSING\_SYSTEMFILE**
</dt> <dd> <dl> <dt>

573 (0x23D)
</dt> <dt>



{Missing System File} The required system file %hs is bad or missing.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNHANDLED_EXCEPTION"></span><span id="error_unhandled_exception"></span>**ERROR\_UNHANDLED\_EXCEPTION**
</dt> <dd> <dl> <dt>

574 (0x23E)
</dt> <dt>



{Application Error} The exception %s (0x%08lx) occurred in the application at location 0x%08lx.


</dt> </dl> </dd> <dt>

<span id="ERROR_APP_INIT_FAILURE"></span><span id="error_app_init_failure"></span>**ERROR\_APP\_INIT\_FAILURE**
</dt> <dd> <dl> <dt>

575 (0x23F)
</dt> <dt>



{Application Error} The application was unable to start correctly (0x%lx). Click OK to close the application.


</dt> </dl> </dd> <dt>

<span id="ERROR_PAGEFILE_CREATE_FAILED"></span><span id="error_pagefile_create_failed"></span>**ERROR\_PAGEFILE\_CREATE\_FAILED**
</dt> <dd> <dl> <dt>

576 (0x240)
</dt> <dt>



{Unable to Create Paging File} The creation of the paging file %hs failed (%lx). The requested size was %ld.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_IMAGE_HASH"></span><span id="error_invalid_image_hash"></span>**ERROR\_INVALID\_IMAGE\_HASH**
</dt> <dd> <dl> <dt>

577 (0x241)
</dt> <dt>



Windows cannot verify the digital signature for this file. A recent hardware or software change might have installed a file that is signed incorrectly or damaged, or that might be malicious software from an unknown source.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_PAGEFILE"></span><span id="error_no_pagefile"></span>**ERROR\_NO\_PAGEFILE**
</dt> <dd> <dl> <dt>

578 (0x242)
</dt> <dt>



{No Paging File Specified} No paging file was specified in the system configuration.


</dt> </dl> </dd> <dt>

<span id="ERROR_ILLEGAL_FLOAT_CONTEXT"></span><span id="error_illegal_float_context"></span>**ERROR\_ILLEGAL\_FLOAT\_CONTEXT**
</dt> <dd> <dl> <dt>

579 (0x243)
</dt> <dt>



{EXCEPTION} A real-mode application issued a floating-point instruction and floating-point hardware is not present.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_EVENT_PAIR"></span><span id="error_no_event_pair"></span>**ERROR\_NO\_EVENT\_PAIR**
</dt> <dd> <dl> <dt>

580 (0x244)
</dt> <dt>



An event pair synchronization operation was performed using the thread specific client/server event pair object, but no event pair object was associated with the thread.


</dt> </dl> </dd> <dt>

<span id="ERROR_DOMAIN_CTRLR_CONFIG_ERROR"></span><span id="error_domain_ctrlr_config_error"></span>**ERROR\_DOMAIN\_CTRLR\_CONFIG\_ERROR**
</dt> <dd> <dl> <dt>

581 (0x245)
</dt> <dt>



A Windows Server has an incorrect configuration.


</dt> </dl> </dd> <dt>

<span id="ERROR_ILLEGAL_CHARACTER"></span><span id="error_illegal_character"></span>**ERROR\_ILLEGAL\_CHARACTER**
</dt> <dd> <dl> <dt>

582 (0x246)
</dt> <dt>



An illegal character was encountered. For a multi-byte character set this includes a lead byte without a succeeding trail byte. For the Unicode character set this includes the characters 0xFFFF and 0xFFFE.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNDEFINED_CHARACTER"></span><span id="error_undefined_character"></span>**ERROR\_UNDEFINED\_CHARACTER**
</dt> <dd> <dl> <dt>

583 (0x247)
</dt> <dt>



The Unicode character is not defined in the Unicode character set installed on the system.


</dt> </dl> </dd> <dt>

<span id="ERROR_FLOPPY_VOLUME"></span><span id="error_floppy_volume"></span>**ERROR\_FLOPPY\_VOLUME**
</dt> <dd> <dl> <dt>

584 (0x248)
</dt> <dt>



The paging file cannot be created on a floppy diskette.


</dt> </dl> </dd> <dt>

<span id="ERROR_BIOS_FAILED_TO_CONNECT_INTERRUPT"></span><span id="error_bios_failed_to_connect_interrupt"></span>**ERROR\_BIOS\_FAILED\_TO\_CONNECT\_INTERRUPT**
</dt> <dd> <dl> <dt>

585 (0x249)
</dt> <dt>



The system BIOS failed to connect a system interrupt to the device or bus for which the device is connected.


</dt> </dl> </dd> <dt>

<span id="ERROR_BACKUP_CONTROLLER"></span><span id="error_backup_controller"></span>**ERROR\_BACKUP\_CONTROLLER**
</dt> <dd> <dl> <dt>

586 (0x24A)
</dt> <dt>



This operation is only allowed for the Primary Domain Controller of the domain.


</dt> </dl> </dd> <dt>

<span id="ERROR_MUTANT_LIMIT_EXCEEDED"></span><span id="error_mutant_limit_exceeded"></span>**ERROR\_MUTANT\_LIMIT\_EXCEEDED**
</dt> <dd> <dl> <dt>

587 (0x24B)
</dt> <dt>



An attempt was made to acquire a mutant such that its maximum count would have been exceeded.


</dt> </dl> </dd> <dt>

<span id="ERROR_FS_DRIVER_REQUIRED"></span><span id="error_fs_driver_required"></span>**ERROR\_FS\_DRIVER\_REQUIRED**
</dt> <dd> <dl> <dt>

588 (0x24C)
</dt> <dt>



A volume has been accessed for which a file system driver is required that has not yet been loaded.


</dt> </dl> </dd> <dt>

<span id="ERROR_CANNOT_LOAD_REGISTRY_FILE"></span><span id="error_cannot_load_registry_file"></span>**ERROR\_CANNOT\_LOAD\_REGISTRY\_FILE**
</dt> <dd> <dl> <dt>

589 (0x24D)
</dt> <dt>



{Registry File Failure} The registry cannot load the hive (file): %hs or its log or alternate. It is corrupt, absent, or not writable.


</dt> </dl> </dd> <dt>

<span id="ERROR_DEBUG_ATTACH_FAILED"></span><span id="error_debug_attach_failed"></span>**ERROR\_DEBUG\_ATTACH\_FAILED**
</dt> <dd> <dl> <dt>

590 (0x24E)
</dt> <dt>



{Unexpected Failure in [**DebugActiveProcess**](/windows/win32/api/debugapi/nf-debugapi-debugactiveprocess)} An unexpected failure occurred while processing a **DebugActiveProcess** API request. You may choose OK to terminate the process, or Cancel to ignore the error.


</dt> </dl> </dd> <dt>

<span id="ERROR_SYSTEM_PROCESS_TERMINATED"></span><span id="error_system_process_terminated"></span>**ERROR\_SYSTEM\_PROCESS\_TERMINATED**
</dt> <dd> <dl> <dt>

591 (0x24F)
</dt> <dt>



{Fatal System Error} The %hs system process terminated unexpectedly with a status of 0x%08x (0x%08x 0x%08x). The system has been shut down.


</dt> </dl> </dd> <dt>

<span id="ERROR_DATA_NOT_ACCEPTED"></span><span id="error_data_not_accepted"></span>**ERROR\_DATA\_NOT\_ACCEPTED**
</dt> <dd> <dl> <dt>

592 (0x250)
</dt> <dt>



{Data Not Accepted} The TDI client could not handle the data received during an indication.


</dt> </dl> </dd> <dt>

<span id="ERROR_VDM_HARD_ERROR"></span><span id="error_vdm_hard_error"></span>**ERROR\_VDM\_HARD\_ERROR**
</dt> <dd> <dl> <dt>

593 (0x251)
</dt> <dt>



NTVDM encountered a hard error.


</dt> </dl> </dd> <dt>

<span id="ERROR_DRIVER_CANCEL_TIMEOUT"></span><span id="error_driver_cancel_timeout"></span>**ERROR\_DRIVER\_CANCEL\_TIMEOUT**
</dt> <dd> <dl> <dt>

594 (0x252)
</dt> <dt>



{Cancel Timeout} The driver %hs failed to complete a cancelled I/O request in the allotted time.


</dt> </dl> </dd> <dt>

<span id="ERROR_REPLY_MESSAGE_MISMATCH"></span><span id="error_reply_message_mismatch"></span>**ERROR\_REPLY\_MESSAGE\_MISMATCH**
</dt> <dd> <dl> <dt>

595 (0x253)
</dt> <dt>



{Reply Message Mismatch} An attempt was made to reply to an LPC message, but the thread specified by the client ID in the message was not waiting on that message.


</dt> </dl> </dd> <dt>

<span id="ERROR_LOST_WRITEBEHIND_DATA"></span><span id="error_lost_writebehind_data"></span>**ERROR\_LOST\_WRITEBEHIND\_DATA**
</dt> <dd> <dl> <dt>

596 (0x254)
</dt> <dt>



{Delayed Write Failed} Windows was unable to save all the data for the file %hs. The data has been lost. This error may be caused by a failure of your computer hardware or network connection. Please try to save this file elsewhere.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLIENT_SERVER_PARAMETERS_INVALID"></span><span id="error_client_server_parameters_invalid"></span>**ERROR\_CLIENT\_SERVER\_PARAMETERS\_INVALID**
</dt> <dd> <dl> <dt>

597 (0x255)
</dt> <dt>



The parameter(s) passed to the server in the client/server shared memory window were invalid. Too much data may have been put in the shared memory window.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_TINY_STREAM"></span><span id="error_not_tiny_stream"></span>**ERROR\_NOT\_TINY\_STREAM**
</dt> <dd> <dl> <dt>

598 (0x256)
</dt> <dt>



The stream is not a tiny stream.


</dt> </dl> </dd> <dt>

<span id="ERROR_STACK_OVERFLOW_READ"></span><span id="error_stack_overflow_read"></span>**ERROR\_STACK\_OVERFLOW\_READ**
</dt> <dd> <dl> <dt>

599 (0x257)
</dt> <dt>



The request must be handled by the stack overflow code.


</dt> </dl> </dd> <dt>

<span id="ERROR_CONVERT_TO_LARGE"></span><span id="error_convert_to_large"></span>**ERROR\_CONVERT\_TO\_LARGE**
</dt> <dd> <dl> <dt>

600 (0x258)
</dt> <dt>



Internal OFS status codes indicating how an allocation operation is handled. Either it is retried after the containing onode is moved or the extent stream is converted to a large stream.


</dt> </dl> </dd> <dt>

<span id="ERROR_FOUND_OUT_OF_SCOPE"></span><span id="error_found_out_of_scope"></span>**ERROR\_FOUND\_OUT\_OF\_SCOPE**
</dt> <dd> <dl> <dt>

601 (0x259)
</dt> <dt>



The attempt to find the object found an object matching by ID on the volume but it is out of the scope of the handle used for the operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_ALLOCATE_BUCKET"></span><span id="error_allocate_bucket"></span>**ERROR\_ALLOCATE\_BUCKET**
</dt> <dd> <dl> <dt>

602 (0x25A)
</dt> <dt>



The bucket array must be grown. Retry transaction after doing so.


</dt> </dl> </dd> <dt>

<span id="ERROR_MARSHALL_OVERFLOW"></span><span id="error_marshall_overflow"></span>**ERROR\_MARSHALL\_OVERFLOW**
</dt> <dd> <dl> <dt>

603 (0x25B)
</dt> <dt>



The user/kernel marshalling buffer has overflowed.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_VARIANT"></span><span id="error_invalid_variant"></span>**ERROR\_INVALID\_VARIANT**
</dt> <dd> <dl> <dt>

604 (0x25C)
</dt> <dt>



The supplied variant structure contains invalid data.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_COMPRESSION_BUFFER"></span><span id="error_bad_compression_buffer"></span>**ERROR\_BAD\_COMPRESSION\_BUFFER**
</dt> <dd> <dl> <dt>

605 (0x25D)
</dt> <dt>



The specified buffer contains ill-formed data.


</dt> </dl> </dd> <dt>

<span id="ERROR_AUDIT_FAILED"></span><span id="error_audit_failed"></span>**ERROR\_AUDIT\_FAILED**
</dt> <dd> <dl> <dt>

606 (0x25E)
</dt> <dt>



{Audit Failed} An attempt to generate a security audit failed.


</dt> </dl> </dd> <dt>

<span id="ERROR_TIMER_RESOLUTION_NOT_SET"></span><span id="error_timer_resolution_not_set"></span>**ERROR\_TIMER\_RESOLUTION\_NOT\_SET**
</dt> <dd> <dl> <dt>

607 (0x25F)
</dt> <dt>



The timer resolution was not previously set by the current process.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSUFFICIENT_LOGON_INFO"></span><span id="error_insufficient_logon_info"></span>**ERROR\_INSUFFICIENT\_LOGON\_INFO**
</dt> <dd> <dl> <dt>

608 (0x260)
</dt> <dt>



There is insufficient account information to log you on.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_DLL_ENTRYPOINT"></span><span id="error_bad_dll_entrypoint"></span>**ERROR\_BAD\_DLL\_ENTRYPOINT**
</dt> <dd> <dl> <dt>

609 (0x261)
</dt> <dt>



{Invalid DLL Entrypoint} The dynamic link library %hs is not written correctly. The stack pointer has been left in an inconsistent state. The entrypoint should be declared as WINAPI or STDCALL. Select YES to fail the DLL load. Select NO to continue execution. Selecting NO may cause the application to operate incorrectly.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_SERVICE_ENTRYPOINT"></span><span id="error_bad_service_entrypoint"></span>**ERROR\_BAD\_SERVICE\_ENTRYPOINT**
</dt> <dd> <dl> <dt>

610 (0x262)
</dt> <dt>



{Invalid Service Callback Entrypoint} The %hs service is not written correctly. The stack pointer has been left in an inconsistent state. The callback entrypoint should be declared as WINAPI or STDCALL. Selecting OK will cause the service to continue operation. However, the service process may operate incorrectly.


</dt> </dl> </dd> <dt>

<span id="ERROR_IP_ADDRESS_CONFLICT1"></span><span id="error_ip_address_conflict1"></span>**ERROR\_IP\_ADDRESS\_CONFLICT1**
</dt> <dd> <dl> <dt>

611 (0x263)
</dt> <dt>



There is an IP address conflict with another system on the network.


</dt> </dl> </dd> <dt>

<span id="ERROR_IP_ADDRESS_CONFLICT2"></span><span id="error_ip_address_conflict2"></span>**ERROR\_IP\_ADDRESS\_CONFLICT2**
</dt> <dd> <dl> <dt>

612 (0x264)
</dt> <dt>



There is an IP address conflict with another system on the network.


</dt> </dl> </dd> <dt>

<span id="ERROR_REGISTRY_QUOTA_LIMIT"></span><span id="error_registry_quota_limit"></span>**ERROR\_REGISTRY\_QUOTA\_LIMIT**
</dt> <dd> <dl> <dt>

613 (0x265)
</dt> <dt>



{Low On Registry Space} The system has reached the maximum size allowed for the system part of the registry. Additional storage requests will be ignored.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_CALLBACK_ACTIVE"></span><span id="error_no_callback_active"></span>**ERROR\_NO\_CALLBACK\_ACTIVE**
</dt> <dd> <dl> <dt>

614 (0x266)
</dt> <dt>



A callback return system service cannot be executed when no callback is active.


</dt> </dl> </dd> <dt>

<span id="ERROR_PWD_TOO_SHORT"></span><span id="error_pwd_too_short"></span>**ERROR\_PWD\_TOO\_SHORT**
</dt> <dd> <dl> <dt>

615 (0x267)
</dt> <dt>



The password provided is too short to meet the policy of your user account. Please choose a longer password.


</dt> </dl> </dd> <dt>

<span id="ERROR_PWD_TOO_RECENT"></span><span id="error_pwd_too_recent"></span>**ERROR\_PWD\_TOO\_RECENT**
</dt> <dd> <dl> <dt>

616 (0x268)
</dt> <dt>



The policy of your user account does not allow you to change passwords too frequently. This is done to prevent users from changing back to a familiar, but potentially discovered, password. If you feel your password has been compromised then please contact your administrator immediately to have a new one assigned.


</dt> </dl> </dd> <dt>

<span id="ERROR_PWD_HISTORY_CONFLICT"></span><span id="error_pwd_history_conflict"></span>**ERROR\_PWD\_HISTORY\_CONFLICT**
</dt> <dd> <dl> <dt>

617 (0x269)
</dt> <dt>



You have attempted to change your password to one that you have used in the past. The policy of your user account does not allow this. Please select a password that you have not previously used.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNSUPPORTED_COMPRESSION"></span><span id="error_unsupported_compression"></span>**ERROR\_UNSUPPORTED\_COMPRESSION**
</dt> <dd> <dl> <dt>

618 (0x26A)
</dt> <dt>



The specified compression format is unsupported.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_HW_PROFILE"></span><span id="error_invalid_hw_profile"></span>**ERROR\_INVALID\_HW\_PROFILE**
</dt> <dd> <dl> <dt>

619 (0x26B)
</dt> <dt>



The specified hardware profile configuration is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_PLUGPLAY_DEVICE_PATH"></span><span id="error_invalid_plugplay_device_path"></span>**ERROR\_INVALID\_PLUGPLAY\_DEVICE\_PATH**
</dt> <dd> <dl> <dt>

620 (0x26C)
</dt> <dt>



The specified Plug and Play registry device path is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_QUOTA_LIST_INCONSISTENT"></span><span id="error_quota_list_inconsistent"></span>**ERROR\_QUOTA\_LIST\_INCONSISTENT**
</dt> <dd> <dl> <dt>

621 (0x26D)
</dt> <dt>



The specified quota list is internally inconsistent with its descriptor.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVALUATION_EXPIRATION"></span><span id="error_evaluation_expiration"></span>**ERROR\_EVALUATION\_EXPIRATION**
</dt> <dd> <dl> <dt>

622 (0x26E)
</dt> <dt>



{Windows Evaluation Notification} The evaluation period for this installation of Windows has expired. This system will shutdown in 1 hour. To restore access to this installation of Windows, please upgrade this installation using a licensed distribution of this product.


</dt> </dl> </dd> <dt>

<span id="ERROR_ILLEGAL_DLL_RELOCATION"></span><span id="error_illegal_dll_relocation"></span>**ERROR\_ILLEGAL\_DLL\_RELOCATION**
</dt> <dd> <dl> <dt>

623 (0x26F)
</dt> <dt>



{Illegal System DLL Relocation} The system DLL %hs was relocated in memory. The application will not run properly. The relocation occurred because the DLL %hs occupied an address range reserved for Windows system DLLs. The vendor supplying the DLL should be contacted for a new DLL.


</dt> </dl> </dd> <dt>

<span id="ERROR_DLL_INIT_FAILED_LOGOFF"></span><span id="error_dll_init_failed_logoff"></span>**ERROR\_DLL\_INIT\_FAILED\_LOGOFF**
</dt> <dd> <dl> <dt>

624 (0x270)
</dt> <dt>



{DLL Initialization Failed} The application failed to initialize because the window station is shutting down.


</dt> </dl> </dd> <dt>

<span id="ERROR_VALIDATE_CONTINUE"></span><span id="error_validate_continue"></span>**ERROR\_VALIDATE\_CONTINUE**
</dt> <dd> <dl> <dt>

625 (0x271)
</dt> <dt>



The validation process needs to continue on to the next step.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_MORE_MATCHES"></span><span id="error_no_more_matches"></span>**ERROR\_NO\_MORE\_MATCHES**
</dt> <dd> <dl> <dt>

626 (0x272)
</dt> <dt>



There are no more matches for the current index enumeration.


</dt> </dl> </dd> <dt>

<span id="ERROR_RANGE_LIST_CONFLICT"></span><span id="error_range_list_conflict"></span>**ERROR\_RANGE\_LIST\_CONFLICT**
</dt> <dd> <dl> <dt>

627 (0x273)
</dt> <dt>



The range could not be added to the range list because of a conflict.


</dt> </dl> </dd> <dt>

<span id="ERROR_SERVER_SID_MISMATCH"></span><span id="error_server_sid_mismatch"></span>**ERROR\_SERVER\_SID\_MISMATCH**
</dt> <dd> <dl> <dt>

628 (0x274)
</dt> <dt>



The server process is running under a SID different than that required by client.


</dt> </dl> </dd> <dt>

<span id="ERROR_CANT_ENABLE_DENY_ONLY"></span><span id="error_cant_enable_deny_only"></span>**ERROR\_CANT\_ENABLE\_DENY\_ONLY**
</dt> <dd> <dl> <dt>

629 (0x275)
</dt> <dt>



A group marked use for deny only cannot be enabled.


</dt> </dl> </dd> <dt>

<span id="ERROR_FLOAT_MULTIPLE_FAULTS"></span><span id="error_float_multiple_faults"></span>**ERROR\_FLOAT\_MULTIPLE\_FAULTS**
</dt> <dd> <dl> <dt>

630 (0x276)
</dt> <dt>



{EXCEPTION} Multiple floating point faults.


</dt> </dl> </dd> <dt>

<span id="ERROR_FLOAT_MULTIPLE_TRAPS"></span><span id="error_float_multiple_traps"></span>**ERROR\_FLOAT\_MULTIPLE\_TRAPS**
</dt> <dd> <dl> <dt>

631 (0x277)
</dt> <dt>



{EXCEPTION} Multiple floating point traps.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOINTERFACE"></span><span id="error_nointerface"></span>**ERROR\_NOINTERFACE**
</dt> <dd> <dl> <dt>

632 (0x278)
</dt> <dt>



The requested interface is not supported.


</dt> </dl> </dd> <dt>

<span id="ERROR_DRIVER_FAILED_SLEEP"></span><span id="error_driver_failed_sleep"></span>**ERROR\_DRIVER\_FAILED\_SLEEP**
</dt> <dd> <dl> <dt>

633 (0x279)
</dt> <dt>



{System Standby Failed} The driver %hs does not support standby mode. Updating this driver may allow the system to go to standby mode.


</dt> </dl> </dd> <dt>

<span id="ERROR_CORRUPT_SYSTEM_FILE"></span><span id="error_corrupt_system_file"></span>**ERROR\_CORRUPT\_SYSTEM\_FILE**
</dt> <dd> <dl> <dt>

634 (0x27A)
</dt> <dt>



The system file %1 has become corrupt and has been replaced.


</dt> </dl> </dd> <dt>

<span id="ERROR_COMMITMENT_MINIMUM"></span><span id="error_commitment_minimum"></span>**ERROR\_COMMITMENT\_MINIMUM**
</dt> <dd> <dl> <dt>

635 (0x27B)
</dt> <dt>



{Virtual Memory Minimum Too Low} Your system is low on virtual memory. Windows is increasing the size of your virtual memory paging file. During this process, memory requests for some applications may be denied. For more information, see Help.


</dt> </dl> </dd> <dt>

<span id="ERROR_PNP_RESTART_ENUMERATION"></span><span id="error_pnp_restart_enumeration"></span>**ERROR\_PNP\_RESTART\_ENUMERATION**
</dt> <dd> <dl> <dt>

636 (0x27C)
</dt> <dt>



A device was removed so enumeration must be restarted.


</dt> </dl> </dd> <dt>

<span id="ERROR_SYSTEM_IMAGE_BAD_SIGNATURE"></span><span id="error_system_image_bad_signature"></span>**ERROR\_SYSTEM\_IMAGE\_BAD\_SIGNATURE**
</dt> <dd> <dl> <dt>

637 (0x27D)
</dt> <dt>



{Fatal System Error} The system image %s is not properly signed. The file has been replaced with the signed file. The system has been shut down.


</dt> </dl> </dd> <dt>

<span id="ERROR_PNP_REBOOT_REQUIRED"></span><span id="error_pnp_reboot_required"></span>**ERROR\_PNP\_REBOOT\_REQUIRED**
</dt> <dd> <dl> <dt>

638 (0x27E)
</dt> <dt>



Device will not start without a reboot.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSUFFICIENT_POWER"></span><span id="error_insufficient_power"></span>**ERROR\_INSUFFICIENT\_POWER**
</dt> <dd> <dl> <dt>

639 (0x27F)
</dt> <dt>



There is not enough power to complete the requested operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_MULTIPLE_FAULT_VIOLATION"></span><span id="error_multiple_fault_violation"></span>**ERROR\_MULTIPLE\_FAULT\_VIOLATION**
</dt> <dd> <dl> <dt>

640 (0x280)
</dt> <dt>



ERROR\_MULTIPLE\_FAULT\_VIOLATION


</dt> </dl> </dd> <dt>

<span id="ERROR_SYSTEM_SHUTDOWN"></span><span id="error_system_shutdown"></span>**ERROR\_SYSTEM\_SHUTDOWN**
</dt> <dd> <dl> <dt>

641 (0x281)
</dt> <dt>



The system is in the process of shutting down.


</dt> </dl> </dd> <dt>

<span id="ERROR_PORT_NOT_SET"></span><span id="error_port_not_set"></span>**ERROR\_PORT\_NOT\_SET**
</dt> <dd> <dl> <dt>

642 (0x282)
</dt> <dt>



An attempt to remove a processes DebugPort was made, but a port was not already associated with the process.


</dt> </dl> </dd> <dt>

<span id="ERROR_DS_VERSION_CHECK_FAILURE"></span><span id="error_ds_version_check_failure"></span>**ERROR\_DS\_VERSION\_CHECK\_FAILURE**
</dt> <dd> <dl> <dt>

643 (0x283)
</dt> <dt>



This version of Windows is not compatible with the behavior version of directory forest, domain or domain controller.


</dt> </dl> </dd> <dt>

<span id="ERROR_RANGE_NOT_FOUND"></span><span id="error_range_not_found"></span>**ERROR\_RANGE\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

644 (0x284)
</dt> <dt>



The specified range could not be found in the range list.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_SAFE_MODE_DRIVER"></span><span id="error_not_safe_mode_driver"></span>**ERROR\_NOT\_SAFE\_MODE\_DRIVER**
</dt> <dd> <dl> <dt>

646 (0x286)
</dt> <dt>



The driver was not loaded because the system is booting into safe mode.


</dt> </dl> </dd> <dt>

<span id="ERROR_FAILED_DRIVER_ENTRY"></span><span id="error_failed_driver_entry"></span>**ERROR\_FAILED\_DRIVER\_ENTRY**
</dt> <dd> <dl> <dt>

647 (0x287)
</dt> <dt>



The driver was not loaded because it failed its initialization call.


</dt> </dl> </dd> <dt>

<span id="ERROR_DEVICE_ENUMERATION_ERROR"></span><span id="error_device_enumeration_error"></span>**ERROR\_DEVICE\_ENUMERATION\_ERROR**
</dt> <dd> <dl> <dt>

648 (0x288)
</dt> <dt>



The "%hs" encountered an error while applying power or reading the device configuration. This may be caused by a failure of your hardware or by a poor connection.


</dt> </dl> </dd> <dt>

<span id="ERROR_MOUNT_POINT_NOT_RESOLVED"></span><span id="error_mount_point_not_resolved"></span>**ERROR\_MOUNT\_POINT\_NOT\_RESOLVED**
</dt> <dd> <dl> <dt>

649 (0x289)
</dt> <dt>



The create operation failed because the name contained at least one mount point which resolves to a volume to which the specified device object is not attached.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_DEVICE_OBJECT_PARAMETER"></span><span id="error_invalid_device_object_parameter"></span>**ERROR\_INVALID\_DEVICE\_OBJECT\_PARAMETER**
</dt> <dd> <dl> <dt>

650 (0x28A)
</dt> <dt>



The device object parameter is either not a valid device object or is not attached to the volume specified by the file name.


</dt> </dl> </dd> <dt>

<span id="ERROR_MCA_OCCURED"></span><span id="error_mca_occured"></span>**ERROR\_MCA\_OCCURED**
</dt> <dd> <dl> <dt>

651 (0x28B)
</dt> <dt>



A Machine Check Error has occurred. Please check the system eventlog for additional information.


</dt> </dl> </dd> <dt>

<span id="ERROR_DRIVER_DATABASE_ERROR"></span><span id="error_driver_database_error"></span>**ERROR\_DRIVER\_DATABASE\_ERROR**
</dt> <dd> <dl> <dt>

652 (0x28C)
</dt> <dt>



There was error \[%2\] processing the driver database.


</dt> </dl> </dd> <dt>

<span id="ERROR_SYSTEM_HIVE_TOO_LARGE"></span><span id="error_system_hive_too_large"></span>**ERROR\_SYSTEM\_HIVE\_TOO\_LARGE**
</dt> <dd> <dl> <dt>

653 (0x28D)
</dt> <dt>



System hive size has exceeded its limit.


</dt> </dl> </dd> <dt>

<span id="ERROR_DRIVER_FAILED_PRIOR_UNLOAD"></span><span id="error_driver_failed_prior_unload"></span>**ERROR\_DRIVER\_FAILED\_PRIOR\_UNLOAD**
</dt> <dd> <dl> <dt>

654 (0x28E)
</dt> <dt>



The driver could not be loaded because a previous version of the driver is still in memory.


</dt> </dl> </dd> <dt>

<span id="ERROR_VOLSNAP_PREPARE_HIBERNATE"></span><span id="error_volsnap_prepare_hibernate"></span>**ERROR\_VOLSNAP\_PREPARE\_HIBERNATE**
</dt> <dd> <dl> <dt>

655 (0x28F)
</dt> <dt>



{Volume Shadow Copy Service} Please wait while the Volume Shadow Copy Service prepares volume %hs for hibernation.


</dt> </dl> </dd> <dt>

<span id="ERROR_HIBERNATION_FAILURE"></span><span id="error_hibernation_failure"></span>**ERROR\_HIBERNATION\_FAILURE**
</dt> <dd> <dl> <dt>

656 (0x290)
</dt> <dt>



The system has failed to hibernate (The error code is %hs). Hibernation will be disabled until the system is restarted.


</dt> </dl> </dd> <dt>

<span id="ERROR_PWD_TOO_LONG"></span><span id="error_pwd_too_long"></span>**ERROR\_PWD\_TOO\_LONG**
</dt> <dd> <dl> <dt>

657 (0x291)
</dt> <dt>



The password provided is too long to meet the policy of your user account. Please choose a shorter password.


</dt> </dl> </dd> <dt>

<span id="ERROR_FILE_SYSTEM_LIMITATION"></span><span id="error_file_system_limitation"></span>**ERROR\_FILE\_SYSTEM\_LIMITATION**
</dt> <dd> <dl> <dt>

665 (0x299)
</dt> <dt>



The requested operation could not be completed due to a file system limitation.


</dt> </dl> </dd> <dt>

<span id="ERROR_ASSERTION_FAILURE"></span><span id="error_assertion_failure"></span>**ERROR\_ASSERTION\_FAILURE**
</dt> <dd> <dl> <dt>

668 (0x29C)
</dt> <dt>



An assertion failure has occurred.


</dt> </dl> </dd> <dt>

<span id="ERROR_ACPI_ERROR"></span><span id="error_acpi_error"></span>**ERROR\_ACPI\_ERROR**
</dt> <dd> <dl> <dt>

669 (0x29D)
</dt> <dt>



An error occurred in the ACPI subsystem.


</dt> </dl> </dd> <dt>

<span id="ERROR_WOW_ASSERTION"></span><span id="error_wow_assertion"></span>**ERROR\_WOW\_ASSERTION**
</dt> <dd> <dl> <dt>

670 (0x29E)
</dt> <dt>



WOW Assertion Error.


</dt> </dl> </dd> <dt>

<span id="ERROR_PNP_BAD_MPS_TABLE"></span><span id="error_pnp_bad_mps_table"></span>**ERROR\_PNP\_BAD\_MPS\_TABLE**
</dt> <dd> <dl> <dt>

671 (0x29F)
</dt> <dt>



A device is missing in the system BIOS MPS table. This device will not be used. Please contact your system vendor for system BIOS update.


</dt> </dl> </dd> <dt>

<span id="ERROR_PNP_TRANSLATION_FAILED"></span><span id="error_pnp_translation_failed"></span>**ERROR\_PNP\_TRANSLATION\_FAILED**
</dt> <dd> <dl> <dt>

672 (0x2A0)
</dt> <dt>



A translator failed to translate resources.


</dt> </dl> </dd> <dt>

<span id="ERROR_PNP_IRQ_TRANSLATION_FAILED"></span><span id="error_pnp_irq_translation_failed"></span>**ERROR\_PNP\_IRQ\_TRANSLATION\_FAILED**
</dt> <dd> <dl> <dt>

673 (0x2A1)
</dt> <dt>



A IRQ translator failed to translate resources.


</dt> </dl> </dd> <dt>

<span id="ERROR_PNP_INVALID_ID"></span><span id="error_pnp_invalid_id"></span>**ERROR\_PNP\_INVALID\_ID**
</dt> <dd> <dl> <dt>

674 (0x2A2)
</dt> <dt>



Driver %2 returned invalid ID for a child device (%3).


</dt> </dl> </dd> <dt>

<span id="ERROR_WAKE_SYSTEM_DEBUGGER"></span><span id="error_wake_system_debugger"></span>**ERROR\_WAKE\_SYSTEM\_DEBUGGER**
</dt> <dd> <dl> <dt>

675 (0x2A3)
</dt> <dt>



{Kernel Debugger Awakened} the system debugger was awakened by an interrupt.


</dt> </dl> </dd> <dt>

<span id="ERROR_HANDLES_CLOSED"></span><span id="error_handles_closed"></span>**ERROR\_HANDLES\_CLOSED**
</dt> <dd> <dl> <dt>

676 (0x2A4)
</dt> <dt>



{Handles Closed} Handles to objects have been automatically closed as a result of the requested operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_EXTRANEOUS_INFORMATION"></span><span id="error_extraneous_information"></span>**ERROR\_EXTRANEOUS\_INFORMATION**
</dt> <dd> <dl> <dt>

677 (0x2A5)
</dt> <dt>



{Too Much Information} The specified access control list (ACL) contained more information than was expected.


</dt> </dl> </dd> <dt>

<span id="ERROR_RXACT_COMMIT_NECESSARY"></span><span id="error_rxact_commit_necessary"></span>**ERROR\_RXACT\_COMMIT\_NECESSARY**
</dt> <dd> <dl> <dt>

678 (0x2A6)
</dt> <dt>



This warning level status indicates that the transaction state already exists for the registry sub-tree, but that a transaction commit was previously aborted. The commit has NOT been completed, but has not been rolled back either (so it may still be committed if desired).


</dt> </dl> </dd> <dt>

<span id="ERROR_MEDIA_CHECK"></span><span id="error_media_check"></span>**ERROR\_MEDIA\_CHECK**
</dt> <dd> <dl> <dt>

679 (0x2A7)
</dt> <dt>



{Media Changed} The media may have changed.


</dt> </dl> </dd> <dt>

<span id="ERROR_GUID_SUBSTITUTION_MADE"></span><span id="error_guid_substitution_made"></span>**ERROR\_GUID\_SUBSTITUTION\_MADE**
</dt> <dd> <dl> <dt>

680 (0x2A8)
</dt> <dt>



{GUID Substitution} During the translation of a global identifier (GUID) to a Windows security ID (SID), no administratively-defined GUID prefix was found. A substitute prefix was used, which will not compromise system security. However, this may provide a more restrictive access than intended.


</dt> </dl> </dd> <dt>

<span id="ERROR_STOPPED_ON_SYMLINK"></span><span id="error_stopped_on_symlink"></span>**ERROR\_STOPPED\_ON\_SYMLINK**
</dt> <dd> <dl> <dt>

681 (0x2A9)
</dt> <dt>



The create operation stopped after reaching a symbolic link.


</dt> </dl> </dd> <dt>

<span id="ERROR_LONGJUMP"></span><span id="error_longjump"></span>**ERROR\_LONGJUMP**
</dt> <dd> <dl> <dt>

682 (0x2AA)
</dt> <dt>



A long jump has been executed.


</dt> </dl> </dd> <dt>

<span id="ERROR_PLUGPLAY_QUERY_VETOED"></span><span id="error_plugplay_query_vetoed"></span>**ERROR\_PLUGPLAY\_QUERY\_VETOED**
</dt> <dd> <dl> <dt>

683 (0x2AB)
</dt> <dt>



The Plug and Play query operation was not successful.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNWIND_CONSOLIDATE"></span><span id="error_unwind_consolidate"></span>**ERROR\_UNWIND\_CONSOLIDATE**
</dt> <dd> <dl> <dt>

684 (0x2AC)
</dt> <dt>



A frame consolidation has been executed.


</dt> </dl> </dd> <dt>

<span id="ERROR_REGISTRY_HIVE_RECOVERED"></span><span id="error_registry_hive_recovered"></span>**ERROR\_REGISTRY\_HIVE\_RECOVERED**
</dt> <dd> <dl> <dt>

685 (0x2AD)
</dt> <dt>



{Registry Hive Recovered} Registry hive (file): %hs was corrupted and it has been recovered. Some data might have been lost.


</dt> </dl> </dd> <dt>

<span id="ERROR_DLL_MIGHT_BE_INSECURE"></span><span id="error_dll_might_be_insecure"></span>**ERROR\_DLL\_MIGHT\_BE\_INSECURE**
</dt> <dd> <dl> <dt>

686 (0x2AE)
</dt> <dt>



The application is attempting to run executable code from the module %hs. This may be insecure. An alternative, %hs, is available. Should the application use the secure module %hs?


</dt> </dl> </dd> <dt>

<span id="ERROR_DLL_MIGHT_BE_INCOMPATIBLE"></span><span id="error_dll_might_be_incompatible"></span>**ERROR\_DLL\_MIGHT\_BE\_INCOMPATIBLE**
</dt> <dd> <dl> <dt>

687 (0x2AF)
</dt> <dt>



The application is loading executable code from the module %hs. This is secure, but may be incompatible with previous releases of the operating system. An alternative, %hs, is available. Should the application use the secure module %hs?


</dt> </dl> </dd> <dt>

<span id="ERROR_DBG_EXCEPTION_NOT_HANDLED"></span><span id="error_dbg_exception_not_handled"></span>**ERROR\_DBG\_EXCEPTION\_NOT\_HANDLED**
</dt> <dd> <dl> <dt>

688 (0x2B0)
</dt> <dt>



Debugger did not handle the exception.


</dt> </dl> </dd> <dt>

<span id="ERROR_DBG_REPLY_LATER"></span><span id="error_dbg_reply_later"></span>**ERROR\_DBG\_REPLY\_LATER**
</dt> <dd> <dl> <dt>

689 (0x2B1)
</dt> <dt>



Debugger will reply later.


</dt> </dl> </dd> <dt>

<span id="ERROR_DBG_UNABLE_TO_PROVIDE_HANDLE"></span><span id="error_dbg_unable_to_provide_handle"></span>**ERROR\_DBG\_UNABLE\_TO\_PROVIDE\_HANDLE**
</dt> <dd> <dl> <dt>

690 (0x2B2)
</dt> <dt>



Debugger cannot provide handle.


</dt> </dl> </dd> <dt>

<span id="ERROR_DBG_TERMINATE_THREAD"></span><span id="error_dbg_terminate_thread"></span>**ERROR\_DBG\_TERMINATE\_THREAD**
</dt> <dd> <dl> <dt>

691 (0x2B3)
</dt> <dt>



Debugger terminated thread.


</dt> </dl> </dd> <dt>

<span id="ERROR_DBG_TERMINATE_PROCESS"></span><span id="error_dbg_terminate_process"></span>**ERROR\_DBG\_TERMINATE\_PROCESS**
</dt> <dd> <dl> <dt>

692 (0x2B4)
</dt> <dt>



Debugger terminated process.


</dt> </dl> </dd> <dt>

<span id="ERROR_DBG_CONTROL_C"></span><span id="error_dbg_control_c"></span>**ERROR\_DBG\_CONTROL\_C**
</dt> <dd> <dl> <dt>

693 (0x2B5)
</dt> <dt>



Debugger got control C.


</dt> </dl> </dd> <dt>

<span id="ERROR_DBG_PRINTEXCEPTION_C"></span><span id="error_dbg_printexception_c"></span>**ERROR\_DBG\_PRINTEXCEPTION\_C**
</dt> <dd> <dl> <dt>

694 (0x2B6)
</dt> <dt>



Debugger printed exception on control C.


</dt> </dl> </dd> <dt>

<span id="ERROR_DBG_RIPEXCEPTION"></span><span id="error_dbg_ripexception"></span>**ERROR\_DBG\_RIPEXCEPTION**
</dt> <dd> <dl> <dt>

695 (0x2B7)
</dt> <dt>



Debugger received RIP exception.


</dt> </dl> </dd> <dt>

<span id="ERROR_DBG_CONTROL_BREAK"></span><span id="error_dbg_control_break"></span>**ERROR\_DBG\_CONTROL\_BREAK**
</dt> <dd> <dl> <dt>

696 (0x2B8)
</dt> <dt>



Debugger received control break.


</dt> </dl> </dd> <dt>

<span id="ERROR_DBG_COMMAND_EXCEPTION"></span><span id="error_dbg_command_exception"></span>**ERROR\_DBG\_COMMAND\_EXCEPTION**
</dt> <dd> <dl> <dt>

697 (0x2B9)
</dt> <dt>



Debugger command communication exception.


</dt> </dl> </dd> <dt>

<span id="ERROR_OBJECT_NAME_EXISTS"></span><span id="error_object_name_exists"></span>**ERROR\_OBJECT\_NAME\_EXISTS**
</dt> <dd> <dl> <dt>

698 (0x2BA)
</dt> <dt>



{Object Exists} An attempt was made to create an object and the object name already existed.


</dt> </dl> </dd> <dt>

<span id="ERROR_THREAD_WAS_SUSPENDED"></span><span id="error_thread_was_suspended"></span>**ERROR\_THREAD\_WAS\_SUSPENDED**
</dt> <dd> <dl> <dt>

699 (0x2BB)
</dt> <dt>



{Thread Suspended} A thread termination occurred while the thread was suspended. The thread was resumed, and termination proceeded.


</dt> </dl> </dd> <dt>

<span id="ERROR_IMAGE_NOT_AT_BASE"></span><span id="error_image_not_at_base"></span>**ERROR\_IMAGE\_NOT\_AT\_BASE**
</dt> <dd> <dl> <dt>

700 (0x2BC)
</dt> <dt>



{Image Relocated} An image file could not be mapped at the address specified in the image file. Local fixups must be performed on this image.


</dt> </dl> </dd> <dt>

<span id="ERROR_RXACT_STATE_CREATED"></span><span id="error_rxact_state_created"></span>**ERROR\_RXACT\_STATE\_CREATED**
</dt> <dd> <dl> <dt>

701 (0x2BD)
</dt> <dt>



This informational level status indicates that a specified registry sub-tree transaction state did not yet exist and had to be created.


</dt> </dl> </dd> <dt>

<span id="ERROR_SEGMENT_NOTIFICATION"></span><span id="error_segment_notification"></span>**ERROR\_SEGMENT\_NOTIFICATION**
</dt> <dd> <dl> <dt>

702 (0x2BE)
</dt> <dt>



{Segment Load} A virtual DOS machine (VDM) is loading, unloading, or moving an MS-DOS or Win16 program segment image. An exception is raised so a debugger can load, unload or track symbols and breakpoints within these 16-bit segments.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_CURRENT_DIRECTORY"></span><span id="error_bad_current_directory"></span>**ERROR\_BAD\_CURRENT\_DIRECTORY**
</dt> <dd> <dl> <dt>

703 (0x2BF)
</dt> <dt>



{Invalid Current Directory} The process cannot switch to the startup current directory %hs. Select OK to set current directory to %hs, or select CANCEL to exit.


</dt> </dl> </dd> <dt>

<span id="ERROR_FT_READ_RECOVERY_FROM_BACKUP"></span><span id="error_ft_read_recovery_from_backup"></span>**ERROR\_FT\_READ\_RECOVERY\_FROM\_BACKUP**
</dt> <dd> <dl> <dt>

704 (0x2C0)
</dt> <dt>



{Redundant Read} To satisfy a read request, the NT fault-tolerant file system successfully read the requested data from a redundant copy. This was done because the file system encountered a failure on a member of the fault-tolerant volume, but was unable to reassign the failing area of the device.


</dt> </dl> </dd> <dt>

<span id="ERROR_FT_WRITE_RECOVERY"></span><span id="error_ft_write_recovery"></span>**ERROR\_FT\_WRITE\_RECOVERY**
</dt> <dd> <dl> <dt>

705 (0x2C1)
</dt> <dt>



{Redundant Write} To satisfy a write request, the NT fault-tolerant file system successfully wrote a redundant copy of the information. This was done because the file system encountered a failure on a member of the fault-tolerant volume, but was not able to reassign the failing area of the device.


</dt> </dl> </dd> <dt>

<span id="ERROR_IMAGE_MACHINE_TYPE_MISMATCH"></span><span id="error_image_machine_type_mismatch"></span>**ERROR\_IMAGE\_MACHINE\_TYPE\_MISMATCH**
</dt> <dd> <dl> <dt>

706 (0x2C2)
</dt> <dt>



{Machine Type Mismatch} The image file %hs is valid, but is for a machine type other than the current machine. Select OK to continue, or CANCEL to fail the DLL load.


</dt> </dl> </dd> <dt>

<span id="ERROR_RECEIVE_PARTIAL"></span><span id="error_receive_partial"></span>**ERROR\_RECEIVE\_PARTIAL**
</dt> <dd> <dl> <dt>

707 (0x2C3)
</dt> <dt>



{Partial Data Received} The network transport returned partial data to its client. The remaining data will be sent later.


</dt> </dl> </dd> <dt>

<span id="ERROR_RECEIVE_EXPEDITED"></span><span id="error_receive_expedited"></span>**ERROR\_RECEIVE\_EXPEDITED**
</dt> <dd> <dl> <dt>

708 (0x2C4)
</dt> <dt>



{Expedited Data Received} The network transport returned data to its client that was marked as expedited by the remote system.


</dt> </dl> </dd> <dt>

<span id="ERROR_RECEIVE_PARTIAL_EXPEDITED"></span><span id="error_receive_partial_expedited"></span>**ERROR\_RECEIVE\_PARTIAL\_EXPEDITED**
</dt> <dd> <dl> <dt>

709 (0x2C5)
</dt> <dt>



{Partial Expedited Data Received} The network transport returned partial data to its client and this data was marked as expedited by the remote system. The remaining data will be sent later.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVENT_DONE"></span><span id="error_event_done"></span>**ERROR\_EVENT\_DONE**
</dt> <dd> <dl> <dt>

710 (0x2C6)
</dt> <dt>



{TDI Event Done} The TDI indication has completed successfully.


</dt> </dl> </dd> <dt>

<span id="ERROR_EVENT_PENDING"></span><span id="error_event_pending"></span>**ERROR\_EVENT\_PENDING**
</dt> <dd> <dl> <dt>

711 (0x2C7)
</dt> <dt>



{TDI Event Pending} The TDI indication has entered the pending state.


</dt> </dl> </dd> <dt>

<span id="ERROR_CHECKING_FILE_SYSTEM"></span><span id="error_checking_file_system"></span>**ERROR\_CHECKING\_FILE\_SYSTEM**
</dt> <dd> <dl> <dt>

712 (0x2C8)
</dt> <dt>



Checking file system on %wZ.


</dt> </dl> </dd> <dt>

<span id="ERROR_FATAL_APP_EXIT"></span><span id="error_fatal_app_exit"></span>**ERROR\_FATAL\_APP\_EXIT**
</dt> <dd> <dl> <dt>

713 (0x2C9)
</dt> <dt>



{Fatal Application Exit} %hs.


</dt> </dl> </dd> <dt>

<span id="ERROR_PREDEFINED_HANDLE"></span><span id="error_predefined_handle"></span>**ERROR\_PREDEFINED\_HANDLE**
</dt> <dd> <dl> <dt>

714 (0x2CA)
</dt> <dt>



The specified registry key is referenced by a predefined handle.


</dt> </dl> </dd> <dt>

<span id="ERROR_WAS_UNLOCKED"></span><span id="error_was_unlocked"></span>**ERROR\_WAS\_UNLOCKED**
</dt> <dd> <dl> <dt>

715 (0x2CB)
</dt> <dt>



{Page Unlocked} The page protection of a locked page was changed to 'No Access' and the page was unlocked from memory and from the process.


</dt> </dl> </dd> <dt>

<span id="ERROR_SERVICE_NOTIFICATION"></span><span id="error_service_notification"></span>**ERROR\_SERVICE\_NOTIFICATION**
</dt> <dd> <dl> <dt>

716 (0x2CC)
</dt> <dt>



%hs


</dt> </dl> </dd> <dt>

<span id="ERROR_WAS_LOCKED"></span><span id="error_was_locked"></span>**ERROR\_WAS\_LOCKED**
</dt> <dd> <dl> <dt>

717 (0x2CD)
</dt> <dt>



{Page Locked} One of the pages to lock was already locked.


</dt> </dl> </dd> <dt>

<span id="ERROR_LOG_HARD_ERROR"></span><span id="error_log_hard_error"></span>**ERROR\_LOG\_HARD\_ERROR**
</dt> <dd> <dl> <dt>

718 (0x2CE)
</dt> <dt>



Application popup: %1 : %2


</dt> </dl> </dd> <dt>

<span id="ERROR_ALREADY_WIN32"></span><span id="error_already_win32"></span>**ERROR\_ALREADY\_WIN32**
</dt> <dd> <dl> <dt>

719 (0x2CF)
</dt> <dt>



ERROR\_ALREADY\_WIN32


</dt> </dl> </dd> <dt>

<span id="ERROR_IMAGE_MACHINE_TYPE_MISMATCH_EXE"></span><span id="error_image_machine_type_mismatch_exe"></span>**ERROR\_IMAGE\_MACHINE\_TYPE\_MISMATCH\_EXE**
</dt> <dd> <dl> <dt>

720 (0x2D0)
</dt> <dt>



{Machine Type Mismatch} The image file %hs is valid, but is for a machine type other than the current machine.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_YIELD_PERFORMED"></span><span id="error_no_yield_performed"></span>**ERROR\_NO\_YIELD\_PERFORMED**
</dt> <dd> <dl> <dt>

721 (0x2D1)
</dt> <dt>



A yield execution was performed and no thread was available to run.


</dt> </dl> </dd> <dt>

<span id="ERROR_TIMER_RESUME_IGNORED"></span><span id="error_timer_resume_ignored"></span>**ERROR\_TIMER\_RESUME\_IGNORED**
</dt> <dd> <dl> <dt>

722 (0x2D2)
</dt> <dt>



The resumable flag to a timer API was ignored.


</dt> </dl> </dd> <dt>

<span id="ERROR_ARBITRATION_UNHANDLED"></span><span id="error_arbitration_unhandled"></span>**ERROR\_ARBITRATION\_UNHANDLED**
</dt> <dd> <dl> <dt>

723 (0x2D3)
</dt> <dt>



The arbiter has deferred arbitration of these resources to its parent.


</dt> </dl> </dd> <dt>

<span id="ERROR_CARDBUS_NOT_SUPPORTED"></span><span id="error_cardbus_not_supported"></span>**ERROR\_CARDBUS\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

724 (0x2D4)
</dt> <dt>



The inserted CardBus device cannot be started because of a configuration error on "%hs".


</dt> </dl> </dd> <dt>

<span id="ERROR_MP_PROCESSOR_MISMATCH"></span><span id="error_mp_processor_mismatch"></span>**ERROR\_MP\_PROCESSOR\_MISMATCH**
</dt> <dd> <dl> <dt>

725 (0x2D5)
</dt> <dt>



The CPUs in this multiprocessor system are not all the same revision level. To use all processors the operating system restricts itself to the features of the least capable processor in the system. Should problems occur with this system, contact the CPU manufacturer to see if this mix of processors is supported.


</dt> </dl> </dd> <dt>

<span id="ERROR_HIBERNATED"></span><span id="error_hibernated"></span>**ERROR\_HIBERNATED**
</dt> <dd> <dl> <dt>

726 (0x2D6)
</dt> <dt>



The system was put into hibernation.


</dt> </dl> </dd> <dt>

<span id="ERROR_RESUME_HIBERNATION"></span><span id="error_resume_hibernation"></span>**ERROR\_RESUME\_HIBERNATION**
</dt> <dd> <dl> <dt>

727 (0x2D7)
</dt> <dt>



The system was resumed from hibernation.


</dt> </dl> </dd> <dt>

<span id="ERROR_FIRMWARE_UPDATED"></span><span id="error_firmware_updated"></span>**ERROR\_FIRMWARE\_UPDATED**
</dt> <dd> <dl> <dt>

728 (0x2D8)
</dt> <dt>



Windows has detected that the system firmware (BIOS) was updated \[previous firmware date = %2, current firmware date %3\].


</dt> </dl> </dd> <dt>

<span id="ERROR_DRIVERS_LEAKING_LOCKED_PAGES"></span><span id="error_drivers_leaking_locked_pages"></span>**ERROR\_DRIVERS\_LEAKING\_LOCKED\_PAGES**
</dt> <dd> <dl> <dt>

729 (0x2D9)
</dt> <dt>



A device driver is leaking locked I/O pages causing system degradation. The system has automatically enabled tracking code in order to try and catch the culprit.


</dt> </dl> </dd> <dt>

<span id="ERROR_WAKE_SYSTEM"></span><span id="error_wake_system"></span>**ERROR\_WAKE\_SYSTEM**
</dt> <dd> <dl> <dt>

730 (0x2DA)
</dt> <dt>



The system has awoken.


</dt> </dl> </dd> <dt>

<span id="ERROR_WAIT_1"></span><span id="error_wait_1"></span>**ERROR\_WAIT\_1**
</dt> <dd> <dl> <dt>

731 (0x2DB)
</dt> <dt>



ERROR\_WAIT\_1


</dt> </dl> </dd> <dt>

<span id="ERROR_WAIT_2"></span><span id="error_wait_2"></span>**ERROR\_WAIT\_2**
</dt> <dd> <dl> <dt>

732 (0x2DC)
</dt> <dt>



ERROR\_WAIT\_2


</dt> </dl> </dd> <dt>

<span id="ERROR_WAIT_3"></span><span id="error_wait_3"></span>**ERROR\_WAIT\_3**
</dt> <dd> <dl> <dt>

733 (0x2DD)
</dt> <dt>



ERROR\_WAIT\_3


</dt> </dl> </dd> <dt>

<span id="ERROR_WAIT_63"></span><span id="error_wait_63"></span>**ERROR\_WAIT\_63**
</dt> <dd> <dl> <dt>

734 (0x2DE)
</dt> <dt>



ERROR\_WAIT\_63


</dt> </dl> </dd> <dt>

<span id="ERROR_ABANDONED_WAIT_0"></span><span id="error_abandoned_wait_0"></span>**ERROR\_ABANDONED\_WAIT\_0**
</dt> <dd> <dl> <dt>

735 (0x2DF)
</dt> <dt>



ERROR\_ABANDONED\_WAIT\_0


</dt> </dl> </dd> <dt>

<span id="ERROR_ABANDONED_WAIT_63"></span><span id="error_abandoned_wait_63"></span>**ERROR\_ABANDONED\_WAIT\_63**
</dt> <dd> <dl> <dt>

736 (0x2E0)
</dt> <dt>



ERROR\_ABANDONED\_WAIT\_63


</dt> </dl> </dd> <dt>

<span id="ERROR_USER_APC"></span><span id="error_user_apc"></span>**ERROR\_USER\_APC**
</dt> <dd> <dl> <dt>

737 (0x2E1)
</dt> <dt>



ERROR\_USER\_APC


</dt> </dl> </dd> <dt>

<span id="ERROR_KERNEL_APC"></span><span id="error_kernel_apc"></span>**ERROR\_KERNEL\_APC**
</dt> <dd> <dl> <dt>

738 (0x2E2)
</dt> <dt>



ERROR\_KERNEL\_APC


</dt> </dl> </dd> <dt>

<span id="ERROR_ALERTED"></span><span id="error_alerted"></span>**ERROR\_ALERTED**
</dt> <dd> <dl> <dt>

739 (0x2E3)
</dt> <dt>



ERROR\_ALERTED


</dt> </dl> </dd> <dt>

<span id="ERROR_ELEVATION_REQUIRED"></span><span id="error_elevation_required"></span>**ERROR\_ELEVATION\_REQUIRED**
</dt> <dd> <dl> <dt>

740 (0x2E4)
</dt> <dt>



The requested operation requires elevation.


</dt> </dl> </dd> <dt>

<span id="ERROR_REPARSE"></span><span id="error_reparse"></span>**ERROR\_REPARSE**
</dt> <dd> <dl> <dt>

741 (0x2E5)
</dt> <dt>



A reparse should be performed by the Object Manager since the name of the file resulted in a symbolic link.


</dt> </dl> </dd> <dt>

<span id="ERROR_OPLOCK_BREAK_IN_PROGRESS"></span><span id="error_oplock_break_in_progress"></span>**ERROR\_OPLOCK\_BREAK\_IN\_PROGRESS**
</dt> <dd> <dl> <dt>

742 (0x2E6)
</dt> <dt>



An open/create operation completed while an oplock break is underway.


</dt> </dl> </dd> <dt>

<span id="ERROR_VOLUME_MOUNTED"></span><span id="error_volume_mounted"></span>**ERROR\_VOLUME\_MOUNTED**
</dt> <dd> <dl> <dt>

743 (0x2E7)
</dt> <dt>



A new volume has been mounted by a file system.


</dt> </dl> </dd> <dt>

<span id="ERROR_RXACT_COMMITTED"></span><span id="error_rxact_committed"></span>**ERROR\_RXACT\_COMMITTED**
</dt> <dd> <dl> <dt>

744 (0x2E8)
</dt> <dt>



This success level status indicates that the transaction state already exists for the registry sub-tree, but that a transaction commit was previously aborted. The commit has now been completed.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOTIFY_CLEANUP"></span><span id="error_notify_cleanup"></span>**ERROR\_NOTIFY\_CLEANUP**
</dt> <dd> <dl> <dt>

745 (0x2E9)
</dt> <dt>



This indicates that a notify change request has been completed due to closing the handle which made the notify change request.


</dt> </dl> </dd> <dt>

<span id="ERROR_PRIMARY_TRANSPORT_CONNECT_FAILED"></span><span id="error_primary_transport_connect_failed"></span>**ERROR\_PRIMARY\_TRANSPORT\_CONNECT\_FAILED**
</dt> <dd> <dl> <dt>

746 (0x2EA)
</dt> <dt>



{Connect Failure on Primary Transport} An attempt was made to connect to the remote server %hs on the primary transport, but the connection failed. The computer WAS able to connect on a secondary transport.


</dt> </dl> </dd> <dt>

<span id="ERROR_PAGE_FAULT_TRANSITION"></span><span id="error_page_fault_transition"></span>**ERROR\_PAGE\_FAULT\_TRANSITION**
</dt> <dd> <dl> <dt>

747 (0x2EB)
</dt> <dt>



Page fault was a transition fault.


</dt> </dl> </dd> <dt>

<span id="ERROR_PAGE_FAULT_DEMAND_ZERO"></span><span id="error_page_fault_demand_zero"></span>**ERROR\_PAGE\_FAULT\_DEMAND\_ZERO**
</dt> <dd> <dl> <dt>

748 (0x2EC)
</dt> <dt>



Page fault was a demand zero fault.


</dt> </dl> </dd> <dt>

<span id="ERROR_PAGE_FAULT_COPY_ON_WRITE"></span><span id="error_page_fault_copy_on_write"></span>**ERROR\_PAGE\_FAULT\_COPY\_ON\_WRITE**
</dt> <dd> <dl> <dt>

749 (0x2ED)
</dt> <dt>



Page fault was a demand zero fault.


</dt> </dl> </dd> <dt>

<span id="ERROR_PAGE_FAULT_GUARD_PAGE"></span><span id="error_page_fault_guard_page"></span>**ERROR\_PAGE\_FAULT\_GUARD\_PAGE**
</dt> <dd> <dl> <dt>

750 (0x2EE)
</dt> <dt>



Page fault was a demand zero fault.


</dt> </dl> </dd> <dt>

<span id="ERROR_PAGE_FAULT_PAGING_FILE"></span><span id="error_page_fault_paging_file"></span>**ERROR\_PAGE\_FAULT\_PAGING\_FILE**
</dt> <dd> <dl> <dt>

751 (0x2EF)
</dt> <dt>



Page fault was satisfied by reading from a secondary storage device.


</dt> </dl> </dd> <dt>

<span id="ERROR_CACHE_PAGE_LOCKED"></span><span id="error_cache_page_locked"></span>**ERROR\_CACHE\_PAGE\_LOCKED**
</dt> <dd> <dl> <dt>

752 (0x2F0)
</dt> <dt>



Cached page was locked during operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_CRASH_DUMP"></span><span id="error_crash_dump"></span>**ERROR\_CRASH\_DUMP**
</dt> <dd> <dl> <dt>

753 (0x2F1)
</dt> <dt>



Crash dump exists in paging file.


</dt> </dl> </dd> <dt>

<span id="ERROR_BUFFER_ALL_ZEROS"></span><span id="error_buffer_all_zeros"></span>**ERROR\_BUFFER\_ALL\_ZEROS**
</dt> <dd> <dl> <dt>

754 (0x2F2)
</dt> <dt>



Specified buffer contains all zeros.


</dt> </dl> </dd> <dt>

<span id="ERROR_REPARSE_OBJECT"></span><span id="error_reparse_object"></span>**ERROR\_REPARSE\_OBJECT**
</dt> <dd> <dl> <dt>

755 (0x2F3)
</dt> <dt>



A reparse should be performed by the Object Manager since the name of the file resulted in a symbolic link.


</dt> </dl> </dd> <dt>

<span id="ERROR_RESOURCE_REQUIREMENTS_CHANGED"></span><span id="error_resource_requirements_changed"></span>**ERROR\_RESOURCE\_REQUIREMENTS\_CHANGED**
</dt> <dd> <dl> <dt>

756 (0x2F4)
</dt> <dt>



The device has succeeded a query-stop and its resource requirements have changed.


</dt> </dl> </dd> <dt>

<span id="ERROR_TRANSLATION_COMPLETE"></span><span id="error_translation_complete"></span>**ERROR\_TRANSLATION\_COMPLETE**
</dt> <dd> <dl> <dt>

757 (0x2F5)
</dt> <dt>



The translator has translated these resources into the global space and no further translations should be performed.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOTHING_TO_TERMINATE"></span><span id="error_nothing_to_terminate"></span>**ERROR\_NOTHING\_TO\_TERMINATE**
</dt> <dd> <dl> <dt>

758 (0x2F6)
</dt> <dt>



A process being terminated has no threads to terminate.


</dt> </dl> </dd> <dt>

<span id="ERROR_PROCESS_NOT_IN_JOB"></span><span id="error_process_not_in_job"></span>**ERROR\_PROCESS\_NOT\_IN\_JOB**
</dt> <dd> <dl> <dt>

759 (0x2F7)
</dt> <dt>



The specified process is not part of a job.


</dt> </dl> </dd> <dt>

<span id="ERROR_PROCESS_IN_JOB"></span><span id="error_process_in_job"></span>**ERROR\_PROCESS\_IN\_JOB**
</dt> <dd> <dl> <dt>

760 (0x2F8)
</dt> <dt>



The specified process is part of a job.


</dt> </dl> </dd> <dt>

<span id="ERROR_VOLSNAP_HIBERNATE_READY"></span><span id="error_volsnap_hibernate_ready"></span>**ERROR\_VOLSNAP\_HIBERNATE\_READY**
</dt> <dd> <dl> <dt>

761 (0x2F9)
</dt> <dt>



{Volume Shadow Copy Service} The system is now ready for hibernation.


</dt> </dl> </dd> <dt>

<span id="ERROR_FSFILTER_OP_COMPLETED_SUCCESSFULLY"></span><span id="error_fsfilter_op_completed_successfully"></span>**ERROR\_FSFILTER\_OP\_COMPLETED\_SUCCESSFULLY**
</dt> <dd> <dl> <dt>

762 (0x2FA)
</dt> <dt>



A file system or file system filter driver has successfully completed an FsFilter operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERRUPT_VECTOR_ALREADY_CONNECTED"></span><span id="error_interrupt_vector_already_connected"></span>**ERROR\_INTERRUPT\_VECTOR\_ALREADY\_CONNECTED**
</dt> <dd> <dl> <dt>

763 (0x2FB)
</dt> <dt>



The specified interrupt vector was already connected.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERRUPT_STILL_CONNECTED"></span><span id="error_interrupt_still_connected"></span>**ERROR\_INTERRUPT\_STILL\_CONNECTED**
</dt> <dd> <dl> <dt>

764 (0x2FC)
</dt> <dt>



The specified interrupt vector is still connected.


</dt> </dl> </dd> <dt>

<span id="ERROR_WAIT_FOR_OPLOCK"></span><span id="error_wait_for_oplock"></span>**ERROR\_WAIT\_FOR\_OPLOCK**
</dt> <dd> <dl> <dt>

765 (0x2FD)
</dt> <dt>



An operation is blocked waiting for an oplock.


</dt> </dl> </dd> <dt>

<span id="ERROR_DBG_EXCEPTION_HANDLED"></span><span id="error_dbg_exception_handled"></span>**ERROR\_DBG\_EXCEPTION\_HANDLED**
</dt> <dd> <dl> <dt>

766 (0x2FE)
</dt> <dt>



Debugger handled exception.


</dt> </dl> </dd> <dt>

<span id="ERROR_DBG_CONTINUE"></span><span id="error_dbg_continue"></span>**ERROR\_DBG\_CONTINUE**
</dt> <dd> <dl> <dt>

767 (0x2FF)
</dt> <dt>



Debugger continued.


</dt> </dl> </dd> <dt>

<span id="ERROR_CALLBACK_POP_STACK"></span><span id="error_callback_pop_stack"></span>**ERROR\_CALLBACK\_POP\_STACK**
</dt> <dd> <dl> <dt>

768 (0x300)
</dt> <dt>



An exception occurred in a user mode callback and the kernel callback frame should be removed.


</dt> </dl> </dd> <dt>

<span id="ERROR_COMPRESSION_DISABLED"></span><span id="error_compression_disabled"></span>**ERROR\_COMPRESSION\_DISABLED**
</dt> <dd> <dl> <dt>

769 (0x301)
</dt> <dt>



Compression is disabled for this volume.


</dt> </dl> </dd> <dt>

<span id="ERROR_CANTFETCHBACKWARDS"></span><span id="error_cantfetchbackwards"></span>**ERROR\_CANTFETCHBACKWARDS**
</dt> <dd> <dl> <dt>

770 (0x302)
</dt> <dt>



The data provider cannot fetch backwards through a result set.


</dt> </dl> </dd> <dt>

<span id="ERROR_CANTSCROLLBACKWARDS"></span><span id="error_cantscrollbackwards"></span>**ERROR\_CANTSCROLLBACKWARDS**
</dt> <dd> <dl> <dt>

771 (0x303)
</dt> <dt>



The data provider cannot scroll backwards through a result set.


</dt> </dl> </dd> <dt>

<span id="ERROR_ROWSNOTRELEASED"></span><span id="error_rowsnotreleased"></span>**ERROR\_ROWSNOTRELEASED**
</dt> <dd> <dl> <dt>

772 (0x304)
</dt> <dt>



The data provider requires that previously fetched data is released before asking for more data.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_ACCESSOR_FLAGS"></span><span id="error_bad_accessor_flags"></span>**ERROR\_BAD\_ACCESSOR\_FLAGS**
</dt> <dd> <dl> <dt>

773 (0x305)
</dt> <dt>



The data provider was not able to interpret the flags set for a column binding in an accessor.


</dt> </dl> </dd> <dt>

<span id="ERROR_ERRORS_ENCOUNTERED"></span><span id="error_errors_encountered"></span>**ERROR\_ERRORS\_ENCOUNTERED**
</dt> <dd> <dl> <dt>

774 (0x306)
</dt> <dt>



One or more errors occurred while processing the request.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_CAPABLE"></span><span id="error_not_capable"></span>**ERROR\_NOT\_CAPABLE**
</dt> <dd> <dl> <dt>

775 (0x307)
</dt> <dt>



The implementation is not capable of performing the request.


</dt> </dl> </dd> <dt>

<span id="ERROR_REQUEST_OUT_OF_SEQUENCE"></span><span id="error_request_out_of_sequence"></span>**ERROR\_REQUEST\_OUT\_OF\_SEQUENCE**
</dt> <dd> <dl> <dt>

776 (0x308)
</dt> <dt>



The client of a component requested an operation which is not valid given the state of the component instance.


</dt> </dl> </dd> <dt>

<span id="ERROR_VERSION_PARSE_ERROR"></span><span id="error_version_parse_error"></span>**ERROR\_VERSION\_PARSE\_ERROR**
</dt> <dd> <dl> <dt>

777 (0x309)
</dt> <dt>



A version number could not be parsed.


</dt> </dl> </dd> <dt>

<span id="ERROR_BADSTARTPOSITION"></span><span id="error_badstartposition"></span>**ERROR\_BADSTARTPOSITION**
</dt> <dd> <dl> <dt>

778 (0x30A)
</dt> <dt>



The iterator's start position is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_MEMORY_HARDWARE"></span><span id="error_memory_hardware"></span>**ERROR\_MEMORY\_HARDWARE**
</dt> <dd> <dl> <dt>

779 (0x30B)
</dt> <dt>



The hardware has reported an uncorrectable memory error.


</dt> </dl> </dd> <dt>

<span id="ERROR_DISK_REPAIR_DISABLED"></span><span id="error_disk_repair_disabled"></span>**ERROR\_DISK\_REPAIR\_DISABLED**
</dt> <dd> <dl> <dt>

780 (0x30C)
</dt> <dt>



The attempted operation required self healing to be enabled.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSUFFICIENT_RESOURCE_FOR_SPECIFIED_SHARED_SECTION_SIZE"></span><span id="error_insufficient_resource_for_specified_shared_section_size"></span>**ERROR\_INSUFFICIENT\_RESOURCE\_FOR\_SPECIFIED\_SHARED\_SECTION\_SIZE**
</dt> <dd> <dl> <dt>

781 (0x30D)
</dt> <dt>



The Desktop heap encountered an error while allocating session memory. There is more information in the system event log.


</dt> </dl> </dd> <dt>

<span id="ERROR_SYSTEM_POWERSTATE_TRANSITION"></span><span id="error_system_powerstate_transition"></span>**ERROR\_SYSTEM\_POWERSTATE\_TRANSITION**
</dt> <dd> <dl> <dt>

782 (0x30E)
</dt> <dt>



The system power state is transitioning from %2 to %3.


</dt> </dl> </dd> <dt>

<span id="ERROR_SYSTEM_POWERSTATE_COMPLEX_TRANSITION"></span><span id="error_system_powerstate_complex_transition"></span>**ERROR\_SYSTEM\_POWERSTATE\_COMPLEX\_TRANSITION**
</dt> <dd> <dl> <dt>

783 (0x30F)
</dt> <dt>



The system power state is transitioning from %2 to %3 but could enter %4.


</dt> </dl> </dd> <dt>

<span id="ERROR_MCA_EXCEPTION"></span><span id="error_mca_exception"></span>**ERROR\_MCA\_EXCEPTION**
</dt> <dd> <dl> <dt>

784 (0x310)
</dt> <dt>



A thread is getting dispatched with MCA EXCEPTION because of MCA.


</dt> </dl> </dd> <dt>

<span id="ERROR_ACCESS_AUDIT_BY_POLICY"></span><span id="error_access_audit_by_policy"></span>**ERROR\_ACCESS\_AUDIT\_BY\_POLICY**
</dt> <dd> <dl> <dt>

785 (0x311)
</dt> <dt>



Access to %1 is monitored by policy rule %2.


</dt> </dl> </dd> <dt>

<span id="ERROR_ACCESS_DISABLED_NO_SAFER_UI_BY_POLICY"></span><span id="error_access_disabled_no_safer_ui_by_policy"></span>**ERROR\_ACCESS\_DISABLED\_NO\_SAFER\_UI\_BY\_POLICY**
</dt> <dd> <dl> <dt>

786 (0x312)
</dt> <dt>



Access to %1 has been restricted by your Administrator by policy rule %2.


</dt> </dl> </dd> <dt>

<span id="ERROR_ABANDON_HIBERFILE"></span><span id="error_abandon_hiberfile"></span>**ERROR\_ABANDON\_HIBERFILE**
</dt> <dd> <dl> <dt>

787 (0x313)
</dt> <dt>



A valid hibernation file has been invalidated and should be abandoned.


</dt> </dl> </dd> <dt>

<span id="ERROR_LOST_WRITEBEHIND_DATA_NETWORK_DISCONNECTED"></span><span id="error_lost_writebehind_data_network_disconnected"></span>**ERROR\_LOST\_WRITEBEHIND\_DATA\_NETWORK\_DISCONNECTED**
</dt> <dd> <dl> <dt>

788 (0x314)
</dt> <dt>



{Delayed Write Failed} Windows was unable to save all the data for the file %hs; the data has been lost. This error may be caused by network connectivity issues. Please try to save this file elsewhere.


</dt> </dl> </dd> <dt>

<span id="ERROR_LOST_WRITEBEHIND_DATA_NETWORK_SERVER_ERROR"></span><span id="error_lost_writebehind_data_network_server_error"></span>**ERROR\_LOST\_WRITEBEHIND\_DATA\_NETWORK\_SERVER\_ERROR**
</dt> <dd> <dl> <dt>

789 (0x315)
</dt> <dt>



{Delayed Write Failed} Windows was unable to save all the data for the file %hs; the data has been lost. This error was returned by the server on which the file exists. Please try to save this file elsewhere.


</dt> </dl> </dd> <dt>

<span id="ERROR_LOST_WRITEBEHIND_DATA_LOCAL_DISK_ERROR"></span><span id="error_lost_writebehind_data_local_disk_error"></span>**ERROR\_LOST\_WRITEBEHIND\_DATA\_LOCAL\_DISK\_ERROR**
</dt> <dd> <dl> <dt>

790 (0x316)
</dt> <dt>



{Delayed Write Failed} Windows was unable to save all the data for the file %hs; the data has been lost. This error may be caused if the device has been removed or the media is write-protected.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_MCFG_TABLE"></span><span id="error_bad_mcfg_table"></span>**ERROR\_BAD\_MCFG\_TABLE**
</dt> <dd> <dl> <dt>

791 (0x317)
</dt> <dt>



The resources required for this device conflict with the MCFG table.


</dt> </dl> </dd> <dt>

<span id="ERROR_DISK_REPAIR_REDIRECTED"></span><span id="error_disk_repair_redirected"></span>**ERROR\_DISK\_REPAIR\_REDIRECTED**
</dt> <dd> <dl> <dt>

792 (0x318)
</dt> <dt>



The volume repair could not be performed while it is online. Please schedule to take the volume offline so that it can be repaired.


</dt> </dl> </dd> <dt>

<span id="ERROR_DISK_REPAIR_UNSUCCESSFUL"></span><span id="error_disk_repair_unsuccessful"></span>**ERROR\_DISK\_REPAIR\_UNSUCCESSFUL**
</dt> <dd> <dl> <dt>

793 (0x319)
</dt> <dt>



The volume repair was not successful.


</dt> </dl> </dd> <dt>

<span id="ERROR_CORRUPT_LOG_OVERFULL"></span><span id="error_corrupt_log_overfull"></span>**ERROR\_CORRUPT\_LOG\_OVERFULL**
</dt> <dd> <dl> <dt>

794 (0x31A)
</dt> <dt>



One of the volume corruption logs is full. Further corruptions that may be detected won't be logged.


</dt> </dl> </dd> <dt>

<span id="ERROR_CORRUPT_LOG_CORRUPTED"></span><span id="error_corrupt_log_corrupted"></span>**ERROR\_CORRUPT\_LOG\_CORRUPTED**
</dt> <dd> <dl> <dt>

795 (0x31B)
</dt> <dt>



One of the volume corruption logs is internally corrupted and needs to be recreated. The volume may contain undetected corruptions and must be scanned.


</dt> </dl> </dd> <dt>

<span id="ERROR_CORRUPT_LOG_UNAVAILABLE"></span><span id="error_corrupt_log_unavailable"></span>**ERROR\_CORRUPT\_LOG\_UNAVAILABLE**
</dt> <dd> <dl> <dt>

796 (0x31C)
</dt> <dt>



One of the volume corruption logs is unavailable for being operated on.


</dt> </dl> </dd> <dt>

<span id="ERROR_CORRUPT_LOG_DELETED_FULL"></span><span id="error_corrupt_log_deleted_full"></span>**ERROR\_CORRUPT\_LOG\_DELETED\_FULL**
</dt> <dd> <dl> <dt>

797 (0x31D)
</dt> <dt>



One of the volume corruption logs was deleted while still having corruption records in them. The volume contains detected corruptions and must be scanned.


</dt> </dl> </dd> <dt>

<span id="ERROR_CORRUPT_LOG_CLEARED"></span><span id="error_corrupt_log_cleared"></span>**ERROR\_CORRUPT\_LOG\_CLEARED**
</dt> <dd> <dl> <dt>

798 (0x31E)
</dt> <dt>



One of the volume corruption logs was cleared by chkdsk and no longer contains real corruptions.


</dt> </dl> </dd> <dt>

<span id="ERROR_ORPHAN_NAME_EXHAUSTED"></span><span id="error_orphan_name_exhausted"></span>**ERROR\_ORPHAN\_NAME\_EXHAUSTED**
</dt> <dd> <dl> <dt>

799 (0x31F)
</dt> <dt>



Orphaned files exist on the volume but could not be recovered because no more new names could be created in the recovery directory. Files must be moved from the recovery directory.


</dt> </dl> </dd> <dt>

<span id="ERROR_OPLOCK_SWITCHED_TO_NEW_HANDLE"></span><span id="error_oplock_switched_to_new_handle"></span>**ERROR\_OPLOCK\_SWITCHED\_TO\_NEW\_HANDLE**
</dt> <dd> <dl> <dt>

800 (0x320)
</dt> <dt>



The oplock that was associated with this handle is now associated with a different handle.


</dt> </dl> </dd> <dt>

<span id="ERROR_CANNOT_GRANT_REQUESTED_OPLOCK"></span><span id="error_cannot_grant_requested_oplock"></span>**ERROR\_CANNOT\_GRANT\_REQUESTED\_OPLOCK**
</dt> <dd> <dl> <dt>

801 (0x321)
</dt> <dt>



An oplock of the requested level cannot be granted. An oplock of a lower level may be available.


</dt> </dl> </dd> <dt>

<span id="ERROR_CANNOT_BREAK_OPLOCK"></span><span id="error_cannot_break_oplock"></span>**ERROR\_CANNOT\_BREAK\_OPLOCK**
</dt> <dd> <dl> <dt>

802 (0x322)
</dt> <dt>



The operation did not complete successfully because it would cause an oplock to be broken. The caller has requested that existing oplocks not be broken.


</dt> </dl> </dd> <dt>

<span id="ERROR_OPLOCK_HANDLE_CLOSED"></span><span id="error_oplock_handle_closed"></span>**ERROR\_OPLOCK\_HANDLE\_CLOSED**
</dt> <dd> <dl> <dt>

803 (0x323)
</dt> <dt>



The handle with which this oplock was associated has been closed. The oplock is now broken.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_ACE_CONDITION"></span><span id="error_no_ace_condition"></span>**ERROR\_NO\_ACE\_CONDITION**
</dt> <dd> <dl> <dt>

804 (0x324)
</dt> <dt>



The specified access control entry (ACE) does not contain a condition.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_ACE_CONDITION"></span><span id="error_invalid_ace_condition"></span>**ERROR\_INVALID\_ACE\_CONDITION**
</dt> <dd> <dl> <dt>

805 (0x325)
</dt> <dt>



The specified access control entry (ACE) contains an invalid condition.


</dt> </dl> </dd> <dt>

<span id="ERROR_FILE_HANDLE_REVOKED"></span><span id="error_file_handle_revoked"></span>**ERROR\_FILE\_HANDLE\_REVOKED**
</dt> <dd> <dl> <dt>

806 (0x326)
</dt> <dt>



Access to the specified file handle has been revoked.


</dt> </dl> </dd> <dt>

<span id="ERROR_IMAGE_AT_DIFFERENT_BASE"></span><span id="error_image_at_different_base"></span>**ERROR\_IMAGE\_AT\_DIFFERENT\_BASE**
</dt> <dd> <dl> <dt>

807 (0x327)
</dt> <dt>



An image file was mapped at a different address from the one specified in the image file but fixups will still be automatically performed on the image.


</dt> </dl> </dd> <dt>

<span id="ERROR_EA_ACCESS_DENIED"></span><span id="error_ea_access_denied"></span>**ERROR\_EA\_ACCESS\_DENIED**
</dt> <dd> <dl> <dt>

994 (0x3E2)
</dt> <dt>



Access to the extended attribute was denied.


</dt> </dl> </dd> <dt>

<span id="ERROR_OPERATION_ABORTED"></span><span id="error_operation_aborted"></span>**ERROR\_OPERATION\_ABORTED**
</dt> <dd> <dl> <dt>

995 (0x3E3)
</dt> <dt>



The I/O operation has been aborted because of either a thread exit or an application request.


</dt> </dl> </dd> <dt>

<span id="ERROR_IO_INCOMPLETE"></span><span id="error_io_incomplete"></span>**ERROR\_IO\_INCOMPLETE**
</dt> <dd> <dl> <dt>

996 (0x3E4)
</dt> <dt>



Overlapped I/O event is not in a signaled state.


</dt> </dl> </dd> <dt>

<span id="ERROR_IO_PENDING"></span><span id="error_io_pending"></span>**ERROR\_IO\_PENDING**
</dt> <dd> <dl> <dt>

997 (0x3E5)
</dt> <dt>



Overlapped I/O operation is in progress.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOACCESS"></span><span id="error_noaccess"></span>**ERROR\_NOACCESS**
</dt> <dd> <dl> <dt>

998 (0x3E6)
</dt> <dt>



Invalid access to memory location.


</dt> </dl> </dd> <dt>

<span id="ERROR_SWAPERROR"></span><span id="error_swaperror"></span>**ERROR\_SWAPERROR**
</dt> <dd> <dl> <dt>

999 (0x3E7)
</dt> <dt>



Error performing inpage operation.


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

 

 

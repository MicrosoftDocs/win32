---
description: Describes error codes 0-499 defined in the WinError.h header file and is intended for developers.
ms.assetid: cacb0aec-d438-4875-a96e-4e0239fdc6ba
title: System Error Codes (0-499) (WinError.h)
ms.topic: reference
ms.date: 07/18/2019
---

# System Error Codes (0-499)

> [!NOTE]
> This information is intended for developers debugging system errors. For other errors, such as issues with Windows Update, there is a list of resources on the [Error codes](system-error-codes.md) page.

The following list describes [system error codes](system-error-codes.md) (errors 0 to 499). They are returned by the [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) function when many functions fail. To retrieve the description text for the error in your application, use the [**FormatMessage**](/windows/desktop/api/WinBase/nf-winbase-formatmessage) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag.

<dl> <dt>

<span id="ERROR_SUCCESS"></span><span id="error_success"></span>**ERROR\_SUCCESS**
</dt> <dd> <dl> <dt>

0 (0x0)
</dt> <dt>



The operation completed successfully.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_FUNCTION"></span><span id="error_invalid_function"></span>**ERROR\_INVALID\_FUNCTION**
</dt> <dd> <dl> <dt>

1 (0x1)
</dt> <dt>



Incorrect function.


</dt> </dl> </dd> <dt>

<span id="ERROR_FILE_NOT_FOUND"></span><span id="error_file_not_found"></span>**ERROR\_FILE\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

2 (0x2)
</dt> <dt>



The system cannot find the file specified.


</dt> </dl> </dd> <dt>

<span id="ERROR_PATH_NOT_FOUND"></span><span id="error_path_not_found"></span>**ERROR\_PATH\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

3 (0x3)
</dt> <dt>



The system cannot find the path specified.


</dt> </dl> </dd> <dt>

<span id="ERROR_TOO_MANY_OPEN_FILES"></span><span id="error_too_many_open_files"></span>**ERROR\_TOO\_MANY\_OPEN\_FILES**
</dt> <dd> <dl> <dt>

4 (0x4)
</dt> <dt>



The system cannot open the file.


</dt> </dl> </dd> <dt>

<span id="ERROR_ACCESS_DENIED"></span><span id="error_access_denied"></span>**ERROR\_ACCESS\_DENIED**
</dt> <dd> <dl> <dt>

5 (0x5)
</dt> <dt>



Access is denied.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_HANDLE"></span><span id="error_invalid_handle"></span>**ERROR\_INVALID\_HANDLE**
</dt> <dd> <dl> <dt>

6 (0x6)
</dt> <dt>



The handle is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_ARENA_TRASHED"></span><span id="error_arena_trashed"></span>**ERROR\_ARENA\_TRASHED**
</dt> <dd> <dl> <dt>

7 (0x7)
</dt> <dt>



The storage control blocks were destroyed.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_ENOUGH_MEMORY"></span><span id="error_not_enough_memory"></span>**ERROR\_NOT\_ENOUGH\_MEMORY**
</dt> <dd> <dl> <dt>

8 (0x8)
</dt> <dt>



Not enough memory resources are available to process this command.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_BLOCK"></span><span id="error_invalid_block"></span>**ERROR\_INVALID\_BLOCK**
</dt> <dd> <dl> <dt>

9 (0x9)
</dt> <dt>



The storage control block address is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_ENVIRONMENT"></span><span id="error_bad_environment"></span>**ERROR\_BAD\_ENVIRONMENT**
</dt> <dd> <dl> <dt>

10 (0xA)
</dt> <dt>



The environment is incorrect.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_FORMAT"></span><span id="error_bad_format"></span>**ERROR\_BAD\_FORMAT**
</dt> <dd> <dl> <dt>

11 (0xB)
</dt> <dt>



An attempt was made to load a program with an incorrect format.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_ACCESS"></span><span id="error_invalid_access"></span>**ERROR\_INVALID\_ACCESS**
</dt> <dd> <dl> <dt>

12 (0xC)
</dt> <dt>



The access code is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_DATA"></span><span id="error_invalid_data"></span>**ERROR\_INVALID\_DATA**
</dt> <dd> <dl> <dt>

13 (0xD)
</dt> <dt>



The data is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_OUTOFMEMORY"></span><span id="error_outofmemory"></span>**ERROR\_OUTOFMEMORY**
</dt> <dd> <dl> <dt>

14 (0xE)
</dt> <dt>



Not enough storage is available to complete this operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_DRIVE"></span><span id="error_invalid_drive"></span>**ERROR\_INVALID\_DRIVE**
</dt> <dd> <dl> <dt>

15 (0xF)
</dt> <dt>



The system cannot find the drive specified.


</dt> </dl> </dd> <dt>

<span id="ERROR_CURRENT_DIRECTORY"></span><span id="error_current_directory"></span>**ERROR\_CURRENT\_DIRECTORY**
</dt> <dd> <dl> <dt>

16 (0x10)
</dt> <dt>



The directory cannot be removed.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_SAME_DEVICE"></span><span id="error_not_same_device"></span>**ERROR\_NOT\_SAME\_DEVICE**
</dt> <dd> <dl> <dt>

17 (0x11)
</dt> <dt>



The system cannot move the file to a different disk drive.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_MORE_FILES"></span><span id="error_no_more_files"></span>**ERROR\_NO\_MORE\_FILES**
</dt> <dd> <dl> <dt>

18 (0x12)
</dt> <dt>



There are no more files.


</dt> </dl> </dd> <dt>

<span id="ERROR_WRITE_PROTECT"></span><span id="error_write_protect"></span>**ERROR\_WRITE\_PROTECT**
</dt> <dd> <dl> <dt>

19 (0x13)
</dt> <dt>



The media is write protected.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_UNIT"></span><span id="error_bad_unit"></span>**ERROR\_BAD\_UNIT**
</dt> <dd> <dl> <dt>

20 (0x14)
</dt> <dt>



The system cannot find the device specified.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_READY"></span><span id="error_not_ready"></span>**ERROR\_NOT\_READY**
</dt> <dd> <dl> <dt>

21 (0x15)
</dt> <dt>



The device is not ready.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_COMMAND"></span><span id="error_bad_command"></span>**ERROR\_BAD\_COMMAND**
</dt> <dd> <dl> <dt>

22 (0x16)
</dt> <dt>



The device does not recognize the command.


</dt> </dl> </dd> <dt>

<span id="ERROR_CRC"></span><span id="error_crc"></span>**ERROR\_CRC**
</dt> <dd> <dl> <dt>

23 (0x17)
</dt> <dt>



Data error (cyclic redundancy check).


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_LENGTH"></span><span id="error_bad_length"></span>**ERROR\_BAD\_LENGTH**
</dt> <dd> <dl> <dt>

24 (0x18)
</dt> <dt>



The program issued a command but the command length is incorrect.


</dt> </dl> </dd> <dt>

<span id="ERROR_SEEK"></span><span id="error_seek"></span>**ERROR\_SEEK**
</dt> <dd> <dl> <dt>

25 (0x19)
</dt> <dt>



The drive cannot locate a specific area or track on the disk.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_DOS_DISK"></span><span id="error_not_dos_disk"></span>**ERROR\_NOT\_DOS\_DISK**
</dt> <dd> <dl> <dt>

26 (0x1A)
</dt> <dt>



The specified disk or diskette cannot be accessed.


</dt> </dl> </dd> <dt>

<span id="ERROR_SECTOR_NOT_FOUND"></span><span id="error_sector_not_found"></span>**ERROR\_SECTOR\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

27 (0x1B)
</dt> <dt>



The drive cannot find the sector requested.


</dt> </dl> </dd> <dt>

<span id="ERROR_OUT_OF_PAPER"></span><span id="error_out_of_paper"></span>**ERROR\_OUT\_OF\_PAPER**
</dt> <dd> <dl> <dt>

28 (0x1C)
</dt> <dt>



The printer is out of paper.


</dt> </dl> </dd> <dt>

<span id="ERROR_WRITE_FAULT"></span><span id="error_write_fault"></span>**ERROR\_WRITE\_FAULT**
</dt> <dd> <dl> <dt>

29 (0x1D)
</dt> <dt>



The system cannot write to the specified device.


</dt> </dl> </dd> <dt>

<span id="ERROR_READ_FAULT"></span><span id="error_read_fault"></span>**ERROR\_READ\_FAULT**
</dt> <dd> <dl> <dt>

30 (0x1E)
</dt> <dt>



The system cannot read from the specified device.


</dt> </dl> </dd> <dt>

<span id="ERROR_GEN_FAILURE"></span><span id="error_gen_failure"></span>**ERROR\_GEN\_FAILURE**
</dt> <dd> <dl> <dt>

31 (0x1F)
</dt> <dt>



A device attached to the system is not functioning.


</dt> </dl> </dd> <dt>

<span id="ERROR_SHARING_VIOLATION"></span><span id="error_sharing_violation"></span>**ERROR\_SHARING\_VIOLATION**
</dt> <dd> <dl> <dt>

32 (0x20)
</dt> <dt>



The process cannot access the file because it is being used by another process.


</dt> </dl> </dd> <dt>

<span id="ERROR_LOCK_VIOLATION"></span><span id="error_lock_violation"></span>**ERROR\_LOCK\_VIOLATION**
</dt> <dd> <dl> <dt>

33 (0x21)
</dt> <dt>



The process cannot access the file because another process has locked a portion of the file.


</dt> </dl> </dd> <dt>

<span id="ERROR_WRONG_DISK"></span><span id="error_wrong_disk"></span>**ERROR\_WRONG\_DISK**
</dt> <dd> <dl> <dt>

34 (0x22)
</dt> <dt>



The wrong diskette is in the drive. Insert %2 (Volume Serial Number: %3) into drive %1.


</dt> </dl> </dd> <dt>

<span id="ERROR_SHARING_BUFFER_EXCEEDED"></span><span id="error_sharing_buffer_exceeded"></span>**ERROR\_SHARING\_BUFFER\_EXCEEDED**
</dt> <dd> <dl> <dt>

36 (0x24)
</dt> <dt>



Too many files opened for sharing.


</dt> </dl> </dd> <dt>

<span id="ERROR_HANDLE_EOF"></span><span id="error_handle_eof"></span>**ERROR\_HANDLE\_EOF**
</dt> <dd> <dl> <dt>

38 (0x26)
</dt> <dt>



Reached the end of the file.


</dt> </dl> </dd> <dt>

<span id="ERROR_HANDLE_DISK_FULL"></span><span id="error_handle_disk_full"></span>**ERROR\_HANDLE\_DISK\_FULL**
</dt> <dd> <dl> <dt>

39 (0x27)
</dt> <dt>



The disk is full.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_SUPPORTED"></span><span id="error_not_supported"></span>**ERROR\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

50 (0x32)
</dt> <dt>



The request is not supported.


</dt> </dl> </dd> <dt>

<span id="ERROR_REM_NOT_LIST"></span><span id="error_rem_not_list"></span>**ERROR\_REM\_NOT\_LIST**
</dt> <dd> <dl> <dt>

51 (0x33)
</dt> <dt>



Windows cannot find the network path. Verify that the network path is correct and the destination computer is not busy or turned off. If Windows still cannot find the network path, contact your network administrator.


</dt> </dl> </dd> <dt>

<span id="ERROR_DUP_NAME"></span><span id="error_dup_name"></span>**ERROR\_DUP\_NAME**
</dt> <dd> <dl> <dt>

52 (0x34)
</dt> <dt>



You were not connected because a duplicate name exists on the network. If joining a domain, go to System in Control Panel to change the computer name and try again. If joining a workgroup, choose another workgroup name.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_NETPATH"></span><span id="error_bad_netpath"></span>**ERROR\_BAD\_NETPATH**
</dt> <dd> <dl> <dt>

53 (0x35)
</dt> <dt>



The network path was not found.


</dt> </dl> </dd> <dt>

<span id="ERROR_NETWORK_BUSY"></span><span id="error_network_busy"></span>**ERROR\_NETWORK\_BUSY**
</dt> <dd> <dl> <dt>

54 (0x36)
</dt> <dt>



The network is busy.


</dt> </dl> </dd> <dt>

<span id="ERROR_DEV_NOT_EXIST"></span><span id="error_dev_not_exist"></span>**ERROR\_DEV\_NOT\_EXIST**
</dt> <dd> <dl> <dt>

55 (0x37)
</dt> <dt>



The specified network resource or device is no longer available.


</dt> </dl> </dd> <dt>

<span id="ERROR_TOO_MANY_CMDS"></span><span id="error_too_many_cmds"></span>**ERROR\_TOO\_MANY\_CMDS**
</dt> <dd> <dl> <dt>

56 (0x38)
</dt> <dt>



The network BIOS command limit has been reached.


</dt> </dl> </dd> <dt>

<span id="ERROR_ADAP_HDW_ERR"></span><span id="error_adap_hdw_err"></span>**ERROR\_ADAP\_HDW\_ERR**
</dt> <dd> <dl> <dt>

57 (0x39)
</dt> <dt>



A network adapter hardware error occurred.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_NET_RESP"></span><span id="error_bad_net_resp"></span>**ERROR\_BAD\_NET\_RESP**
</dt> <dd> <dl> <dt>

58 (0x3A)
</dt> <dt>



The specified server cannot perform the requested operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNEXP_NET_ERR"></span><span id="error_unexp_net_err"></span>**ERROR\_UNEXP\_NET\_ERR**
</dt> <dd> <dl> <dt>

59 (0x3B)
</dt> <dt>



An unexpected network error occurred.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_REM_ADAP"></span><span id="error_bad_rem_adap"></span>**ERROR\_BAD\_REM\_ADAP**
</dt> <dd> <dl> <dt>

60 (0x3C)
</dt> <dt>



The remote adapter is not compatible.


</dt> </dl> </dd> <dt>

<span id="ERROR_PRINTQ_FULL"></span><span id="error_printq_full"></span>**ERROR\_PRINTQ\_FULL**
</dt> <dd> <dl> <dt>

61 (0x3D)
</dt> <dt>



The printer queue is full.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_SPOOL_SPACE"></span><span id="error_no_spool_space"></span>**ERROR\_NO\_SPOOL\_SPACE**
</dt> <dd> <dl> <dt>

62 (0x3E)
</dt> <dt>



Space to store the file waiting to be printed is not available on the server.


</dt> </dl> </dd> <dt>

<span id="ERROR_PRINT_CANCELLED"></span><span id="error_print_cancelled"></span>**ERROR\_PRINT\_CANCELLED**
</dt> <dd> <dl> <dt>

63 (0x3F)
</dt> <dt>



Your file waiting to be printed was deleted.


</dt> </dl> </dd> <dt>

<span id="ERROR_NETNAME_DELETED"></span><span id="error_netname_deleted"></span>**ERROR\_NETNAME\_DELETED**
</dt> <dd> <dl> <dt>

64 (0x40)
</dt> <dt>



The specified network name is no longer available.


</dt> </dl> </dd> <dt>

<span id="ERROR_NETWORK_ACCESS_DENIED"></span><span id="error_network_access_denied"></span>**ERROR\_NETWORK\_ACCESS\_DENIED**
</dt> <dd> <dl> <dt>

65 (0x41)
</dt> <dt>



Network access is denied.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_DEV_TYPE"></span><span id="error_bad_dev_type"></span>**ERROR\_BAD\_DEV\_TYPE**
</dt> <dd> <dl> <dt>

66 (0x42)
</dt> <dt>



The network resource type is not correct.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_NET_NAME"></span><span id="error_bad_net_name"></span>**ERROR\_BAD\_NET\_NAME**
</dt> <dd> <dl> <dt>

67 (0x43)
</dt> <dt>



The network name cannot be found.


</dt> </dl> </dd> <dt>

<span id="ERROR_TOO_MANY_NAMES"></span><span id="error_too_many_names"></span>**ERROR\_TOO\_MANY\_NAMES**
</dt> <dd> <dl> <dt>

68 (0x44)
</dt> <dt>



The name limit for the local computer network adapter card was exceeded.


</dt> </dl> </dd> <dt>

<span id="ERROR_TOO_MANY_SESS"></span><span id="error_too_many_sess"></span>**ERROR\_TOO\_MANY\_SESS**
</dt> <dd> <dl> <dt>

69 (0x45)
</dt> <dt>



The network BIOS session limit was exceeded.


</dt> </dl> </dd> <dt>

<span id="ERROR_SHARING_PAUSED"></span><span id="error_sharing_paused"></span>**ERROR\_SHARING\_PAUSED**
</dt> <dd> <dl> <dt>

70 (0x46)
</dt> <dt>



The remote server has been paused or is in the process of being started.


</dt> </dl> </dd> <dt>

<span id="ERROR_REQ_NOT_ACCEP"></span><span id="error_req_not_accep"></span>**ERROR\_REQ\_NOT\_ACCEP**
</dt> <dd> <dl> <dt>

71 (0x47)
</dt> <dt>



No more connections can be made to this remote computer at this time because there are already as many connections as the computer can accept.


</dt> </dl> </dd> <dt>

<span id="ERROR_REDIR_PAUSED"></span><span id="error_redir_paused"></span>**ERROR\_REDIR\_PAUSED**
</dt> <dd> <dl> <dt>

72 (0x48)
</dt> <dt>



The specified printer or disk device has been paused.


</dt> </dl> </dd> <dt>

<span id="ERROR_FILE_EXISTS"></span><span id="error_file_exists"></span>**ERROR\_FILE\_EXISTS**
</dt> <dd> <dl> <dt>

80 (0x50)
</dt> <dt>



The file exists.


</dt> </dl> </dd> <dt>

<span id="ERROR_CANNOT_MAKE"></span><span id="error_cannot_make"></span>**ERROR\_CANNOT\_MAKE**
</dt> <dd> <dl> <dt>

82 (0x52)
</dt> <dt>



The directory or file cannot be created.


</dt> </dl> </dd> <dt>

<span id="ERROR_FAIL_I24"></span><span id="error_fail_i24"></span>**ERROR\_FAIL\_I24**
</dt> <dd> <dl> <dt>

83 (0x53)
</dt> <dt>



Fail on INT 24.


</dt> </dl> </dd> <dt>

<span id="ERROR_OUT_OF_STRUCTURES"></span><span id="error_out_of_structures"></span>**ERROR\_OUT\_OF\_STRUCTURES**
</dt> <dd> <dl> <dt>

84 (0x54)
</dt> <dt>



Storage to process this request is not available.


</dt> </dl> </dd> <dt>

<span id="ERROR_ALREADY_ASSIGNED"></span><span id="error_already_assigned"></span>**ERROR\_ALREADY\_ASSIGNED**
</dt> <dd> <dl> <dt>

85 (0x55)
</dt> <dt>



The local device name is already in use.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_PASSWORD"></span><span id="error_invalid_password"></span>**ERROR\_INVALID\_PASSWORD**
</dt> <dd> <dl> <dt>

86 (0x56)
</dt> <dt>



The specified network password is not correct.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_PARAMETER"></span><span id="error_invalid_parameter"></span>**ERROR\_INVALID\_PARAMETER**
</dt> <dd> <dl> <dt>

87 (0x57)
</dt> <dt>



The parameter is incorrect.


</dt> </dl> </dd> <dt>

<span id="ERROR_NET_WRITE_FAULT"></span><span id="error_net_write_fault"></span>**ERROR\_NET\_WRITE\_FAULT**
</dt> <dd> <dl> <dt>

88 (0x58)
</dt> <dt>



A write fault occurred on the network.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_PROC_SLOTS"></span><span id="error_no_proc_slots"></span>**ERROR\_NO\_PROC\_SLOTS**
</dt> <dd> <dl> <dt>

89 (0x59)
</dt> <dt>



The system cannot start another process at this time.


</dt> </dl> </dd> <dt>

<span id="ERROR_TOO_MANY_SEMAPHORES"></span><span id="error_too_many_semaphores"></span>**ERROR\_TOO\_MANY\_SEMAPHORES**
</dt> <dd> <dl> <dt>

100 (0x64)
</dt> <dt>



Cannot create another system semaphore.


</dt> </dl> </dd> <dt>

<span id="ERROR_EXCL_SEM_ALREADY_OWNED"></span><span id="error_excl_sem_already_owned"></span>**ERROR\_EXCL\_SEM\_ALREADY\_OWNED**
</dt> <dd> <dl> <dt>

101 (0x65)
</dt> <dt>



The exclusive semaphore is owned by another process.


</dt> </dl> </dd> <dt>

<span id="ERROR_SEM_IS_SET"></span><span id="error_sem_is_set"></span>**ERROR\_SEM\_IS\_SET**
</dt> <dd> <dl> <dt>

102 (0x66)
</dt> <dt>



The semaphore is set and cannot be closed.


</dt> </dl> </dd> <dt>

<span id="ERROR_TOO_MANY_SEM_REQUESTS"></span><span id="error_too_many_sem_requests"></span>**ERROR\_TOO\_MANY\_SEM\_REQUESTS**
</dt> <dd> <dl> <dt>

103 (0x67)
</dt> <dt>



The semaphore cannot be set again.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_AT_INTERRUPT_TIME"></span><span id="error_invalid_at_interrupt_time"></span>**ERROR\_INVALID\_AT\_INTERRUPT\_TIME**
</dt> <dd> <dl> <dt>

104 (0x68)
</dt> <dt>



Cannot request exclusive semaphores at interrupt time.


</dt> </dl> </dd> <dt>

<span id="ERROR_SEM_OWNER_DIED"></span><span id="error_sem_owner_died"></span>**ERROR\_SEM\_OWNER\_DIED**
</dt> <dd> <dl> <dt>

105 (0x69)
</dt> <dt>



The previous ownership of this semaphore has ended.


</dt> </dl> </dd> <dt>

<span id="ERROR_SEM_USER_LIMIT"></span><span id="error_sem_user_limit"></span>**ERROR\_SEM\_USER\_LIMIT**
</dt> <dd> <dl> <dt>

106 (0x6A)
</dt> <dt>



Insert the diskette for drive %1.


</dt> </dl> </dd> <dt>

<span id="ERROR_DISK_CHANGE"></span><span id="error_disk_change"></span>**ERROR\_DISK\_CHANGE**
</dt> <dd> <dl> <dt>

107 (0x6B)
</dt> <dt>



The program stopped because an alternate diskette was not inserted.


</dt> </dl> </dd> <dt>

<span id="ERROR_DRIVE_LOCKED"></span><span id="error_drive_locked"></span>**ERROR\_DRIVE\_LOCKED**
</dt> <dd> <dl> <dt>

108 (0x6C)
</dt> <dt>



The disk is in use or locked by another process.


</dt> </dl> </dd> <dt>

<span id="ERROR_BROKEN_PIPE"></span><span id="error_broken_pipe"></span>**ERROR\_BROKEN\_PIPE**
</dt> <dd> <dl> <dt>

109 (0x6D)
</dt> <dt>



The pipe has been ended.


</dt> </dl> </dd> <dt>

<span id="ERROR_OPEN_FAILED"></span><span id="error_open_failed"></span>**ERROR\_OPEN\_FAILED**
</dt> <dd> <dl> <dt>

110 (0x6E)
</dt> <dt>



The system cannot open the device or file specified.


</dt> </dl> </dd> <dt>

<span id="ERROR_BUFFER_OVERFLOW"></span><span id="error_buffer_overflow"></span>**ERROR\_BUFFER\_OVERFLOW**
</dt> <dd> <dl> <dt>

111 (0x6F)
</dt> <dt>



The file name is too long.


</dt> </dl> </dd> <dt>

<span id="ERROR_DISK_FULL"></span><span id="error_disk_full"></span>**ERROR\_DISK\_FULL**
</dt> <dd> <dl> <dt>

112 (0x70)
</dt> <dt>



There is not enough space on the disk.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_MORE_SEARCH_HANDLES"></span><span id="error_no_more_search_handles"></span>**ERROR\_NO\_MORE\_SEARCH\_HANDLES**
</dt> <dd> <dl> <dt>

113 (0x71)
</dt> <dt>



No more internal file identifiers available.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_TARGET_HANDLE"></span><span id="error_invalid_target_handle"></span>**ERROR\_INVALID\_TARGET\_HANDLE**
</dt> <dd> <dl> <dt>

114 (0x72)
</dt> <dt>



The target internal file identifier is incorrect.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_CATEGORY"></span><span id="error_invalid_category"></span>**ERROR\_INVALID\_CATEGORY**
</dt> <dd> <dl> <dt>

117 (0x75)
</dt> <dt>



The IOCTL call made by the application program is not correct.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_VERIFY_SWITCH"></span><span id="error_invalid_verify_switch"></span>**ERROR\_INVALID\_VERIFY\_SWITCH**
</dt> <dd> <dl> <dt>

118 (0x76)
</dt> <dt>



The verify-on-write switch parameter value is not correct.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_DRIVER_LEVEL"></span><span id="error_bad_driver_level"></span>**ERROR\_BAD\_DRIVER\_LEVEL**
</dt> <dd> <dl> <dt>

119 (0x77)
</dt> <dt>



The system does not support the command requested.


</dt> </dl> </dd> <dt>

<span id="ERROR_CALL_NOT_IMPLEMENTED"></span><span id="error_call_not_implemented"></span>**ERROR\_CALL\_NOT\_IMPLEMENTED**
</dt> <dd> <dl> <dt>

120 (0x78)
</dt> <dt>



This function is not supported on this system.


</dt> </dl> </dd> <dt>

<span id="ERROR_SEM_TIMEOUT"></span><span id="error_sem_timeout"></span>**ERROR\_SEM\_TIMEOUT**
</dt> <dd> <dl> <dt>

121 (0x79)
</dt> <dt>



The semaphore timeout period has expired.


</dt> </dl> </dd> <dt>

<span id="ERROR_INSUFFICIENT_BUFFER"></span><span id="error_insufficient_buffer"></span>**ERROR\_INSUFFICIENT\_BUFFER**
</dt> <dd> <dl> <dt>

122 (0x7A)
</dt> <dt>



The data area passed to a system call is too small.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_NAME"></span><span id="error_invalid_name"></span>**ERROR\_INVALID\_NAME**
</dt> <dd> <dl> <dt>

123 (0x7B)
</dt> <dt>



The filename, directory name, or volume label syntax is incorrect.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_LEVEL"></span><span id="error_invalid_level"></span>**ERROR\_INVALID\_LEVEL**
</dt> <dd> <dl> <dt>

124 (0x7C)
</dt> <dt>



The system call level is not correct.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_VOLUME_LABEL"></span><span id="error_no_volume_label"></span>**ERROR\_NO\_VOLUME\_LABEL**
</dt> <dd> <dl> <dt>

125 (0x7D)
</dt> <dt>



The disk has no volume label.


</dt> </dl> </dd> <dt>

<span id="ERROR_MOD_NOT_FOUND"></span><span id="error_mod_not_found"></span>**ERROR\_MOD\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

126 (0x7E)
</dt> <dt>



The specified module could not be found.


</dt> </dl> </dd> <dt>

<span id="ERROR_PROC_NOT_FOUND"></span><span id="error_proc_not_found"></span>**ERROR\_PROC\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

127 (0x7F)
</dt> <dt>



The specified procedure could not be found.


</dt> </dl> </dd> <dt>

<span id="ERROR_WAIT_NO_CHILDREN"></span><span id="error_wait_no_children"></span>**ERROR\_WAIT\_NO\_CHILDREN**
</dt> <dd> <dl> <dt>

128 (0x80)
</dt> <dt>



There are no child processes to wait for.


</dt> </dl> </dd> <dt>

<span id="ERROR_CHILD_NOT_COMPLETE"></span><span id="error_child_not_complete"></span>**ERROR\_CHILD\_NOT\_COMPLETE**
</dt> <dd> <dl> <dt>

129 (0x81)
</dt> <dt>



The %1 application cannot be run in Win32 mode.


</dt> </dl> </dd> <dt>

<span id="ERROR_DIRECT_ACCESS_HANDLE"></span><span id="error_direct_access_handle"></span>**ERROR\_DIRECT\_ACCESS\_HANDLE**
</dt> <dd> <dl> <dt>

130 (0x82)
</dt> <dt>



Attempt to use a file handle to an open disk partition for an operation other than raw disk I/O.


</dt> </dl> </dd> <dt>

<span id="ERROR_NEGATIVE_SEEK"></span><span id="error_negative_seek"></span>**ERROR\_NEGATIVE\_SEEK**
</dt> <dd> <dl> <dt>

131 (0x83)
</dt> <dt>



An attempt was made to move the file pointer before the beginning of the file.


</dt> </dl> </dd> <dt>

<span id="ERROR_SEEK_ON_DEVICE"></span><span id="error_seek_on_device"></span>**ERROR\_SEEK\_ON\_DEVICE**
</dt> <dd> <dl> <dt>

132 (0x84)
</dt> <dt>



The file pointer cannot be set on the specified device or file.


</dt> </dl> </dd> <dt>

<span id="ERROR_IS_JOIN_TARGET"></span><span id="error_is_join_target"></span>**ERROR\_IS\_JOIN\_TARGET**
</dt> <dd> <dl> <dt>

133 (0x85)
</dt> <dt>



A JOIN or SUBST command cannot be used for a drive that contains previously joined drives.


</dt> </dl> </dd> <dt>

<span id="ERROR_IS_JOINED"></span><span id="error_is_joined"></span>**ERROR\_IS\_JOINED**
</dt> <dd> <dl> <dt>

134 (0x86)
</dt> <dt>



An attempt was made to use a JOIN or SUBST command on a drive that has already been joined.


</dt> </dl> </dd> <dt>

<span id="ERROR_IS_SUBSTED"></span><span id="error_is_substed"></span>**ERROR\_IS\_SUBSTED**
</dt> <dd> <dl> <dt>

135 (0x87)
</dt> <dt>



An attempt was made to use a JOIN or SUBST command on a drive that has already been substituted.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_JOINED"></span><span id="error_not_joined"></span>**ERROR\_NOT\_JOINED**
</dt> <dd> <dl> <dt>

136 (0x88)
</dt> <dt>



The system tried to delete the JOIN of a drive that is not joined.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_SUBSTED"></span><span id="error_not_substed"></span>**ERROR\_NOT\_SUBSTED**
</dt> <dd> <dl> <dt>

137 (0x89)
</dt> <dt>



The system tried to delete the substitution of a drive that is not substituted.


</dt> </dl> </dd> <dt>

<span id="ERROR_JOIN_TO_JOIN"></span><span id="error_join_to_join"></span>**ERROR\_JOIN\_TO\_JOIN**
</dt> <dd> <dl> <dt>

138 (0x8A)
</dt> <dt>



The system tried to join a drive to a directory on a joined drive.


</dt> </dl> </dd> <dt>

<span id="ERROR_SUBST_TO_SUBST"></span><span id="error_subst_to_subst"></span>**ERROR\_SUBST\_TO\_SUBST**
</dt> <dd> <dl> <dt>

139 (0x8B)
</dt> <dt>



The system tried to substitute a drive to a directory on a substituted drive.


</dt> </dl> </dd> <dt>

<span id="ERROR_JOIN_TO_SUBST"></span><span id="error_join_to_subst"></span>**ERROR\_JOIN\_TO\_SUBST**
</dt> <dd> <dl> <dt>

140 (0x8C)
</dt> <dt>



The system tried to join a drive to a directory on a substituted drive.


</dt> </dl> </dd> <dt>

<span id="ERROR_SUBST_TO_JOIN"></span><span id="error_subst_to_join"></span>**ERROR\_SUBST\_TO\_JOIN**
</dt> <dd> <dl> <dt>

141 (0x8D)
</dt> <dt>



The system tried to SUBST a drive to a directory on a joined drive.


</dt> </dl> </dd> <dt>

<span id="ERROR_BUSY_DRIVE"></span><span id="error_busy_drive"></span>**ERROR\_BUSY\_DRIVE**
</dt> <dd> <dl> <dt>

142 (0x8E)
</dt> <dt>



The system cannot perform a JOIN or SUBST at this time.


</dt> </dl> </dd> <dt>

<span id="ERROR_SAME_DRIVE"></span><span id="error_same_drive"></span>**ERROR\_SAME\_DRIVE**
</dt> <dd> <dl> <dt>

143 (0x8F)
</dt> <dt>



The system cannot join or substitute a drive to or for a directory on the same drive.


</dt> </dl> </dd> <dt>

<span id="ERROR_DIR_NOT_ROOT"></span><span id="error_dir_not_root"></span>**ERROR\_DIR\_NOT\_ROOT**
</dt> <dd> <dl> <dt>

144 (0x90)
</dt> <dt>



The directory is not a subdirectory of the root directory.


</dt> </dl> </dd> <dt>

<span id="ERROR_DIR_NOT_EMPTY"></span><span id="error_dir_not_empty"></span>**ERROR\_DIR\_NOT\_EMPTY**
</dt> <dd> <dl> <dt>

145 (0x91)
</dt> <dt>



The directory is not empty.


</dt> </dl> </dd> <dt>

<span id="ERROR_IS_SUBST_PATH"></span><span id="error_is_subst_path"></span>**ERROR\_IS\_SUBST\_PATH**
</dt> <dd> <dl> <dt>

146 (0x92)
</dt> <dt>



The path specified is being used in a substitute.


</dt> </dl> </dd> <dt>

<span id="ERROR_IS_JOIN_PATH"></span><span id="error_is_join_path"></span>**ERROR\_IS\_JOIN\_PATH**
</dt> <dd> <dl> <dt>

147 (0x93)
</dt> <dt>



Not enough resources are available to process this command.


</dt> </dl> </dd> <dt>

<span id="ERROR_PATH_BUSY"></span><span id="error_path_busy"></span>**ERROR\_PATH\_BUSY**
</dt> <dd> <dl> <dt>

148 (0x94)
</dt> <dt>



The path specified cannot be used at this time.


</dt> </dl> </dd> <dt>

<span id="ERROR_IS_SUBST_TARGET"></span><span id="error_is_subst_target"></span>**ERROR\_IS\_SUBST\_TARGET**
</dt> <dd> <dl> <dt>

149 (0x95)
</dt> <dt>



An attempt was made to join or substitute a drive for which a directory on the drive is the target of a previous substitute.


</dt> </dl> </dd> <dt>

<span id="ERROR_SYSTEM_TRACE"></span><span id="error_system_trace"></span>**ERROR\_SYSTEM\_TRACE**
</dt> <dd> <dl> <dt>

150 (0x96)
</dt> <dt>



System trace information was not specified in your CONFIG.SYS file, or tracing is disallowed.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_EVENT_COUNT"></span><span id="error_invalid_event_count"></span>**ERROR\_INVALID\_EVENT\_COUNT**
</dt> <dd> <dl> <dt>

151 (0x97)
</dt> <dt>



The number of specified semaphore events for DosMuxSemWait is not correct.


</dt> </dl> </dd> <dt>

<span id="ERROR_TOO_MANY_MUXWAITERS"></span><span id="error_too_many_muxwaiters"></span>**ERROR\_TOO\_MANY\_MUXWAITERS**
</dt> <dd> <dl> <dt>

152 (0x98)
</dt> <dt>



DosMuxSemWait did not execute; too many semaphores are already set.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_LIST_FORMAT"></span><span id="error_invalid_list_format"></span>**ERROR\_INVALID\_LIST\_FORMAT**
</dt> <dd> <dl> <dt>

153 (0x99)
</dt> <dt>



The DosMuxSemWait list is not correct.


</dt> </dl> </dd> <dt>

<span id="ERROR_LABEL_TOO_LONG"></span><span id="error_label_too_long"></span>**ERROR\_LABEL\_TOO\_LONG**
</dt> <dd> <dl> <dt>

154 (0x9A)
</dt> <dt>



The volume label you entered exceeds the label character limit of the target file system.


</dt> </dl> </dd> <dt>

<span id="ERROR_TOO_MANY_TCBS"></span><span id="error_too_many_tcbs"></span>**ERROR\_TOO\_MANY\_TCBS**
</dt> <dd> <dl> <dt>

155 (0x9B)
</dt> <dt>



Cannot create another thread.


</dt> </dl> </dd> <dt>

<span id="ERROR_SIGNAL_REFUSED"></span><span id="error_signal_refused"></span>**ERROR\_SIGNAL\_REFUSED**
</dt> <dd> <dl> <dt>

156 (0x9C)
</dt> <dt>



The recipient process has refused the signal.


</dt> </dl> </dd> <dt>

<span id="ERROR_DISCARDED"></span><span id="error_discarded"></span>**ERROR\_DISCARDED**
</dt> <dd> <dl> <dt>

157 (0x9D)
</dt> <dt>



The segment is already discarded and cannot be locked.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_LOCKED"></span><span id="error_not_locked"></span>**ERROR\_NOT\_LOCKED**
</dt> <dd> <dl> <dt>

158 (0x9E)
</dt> <dt>



The segment is already unlocked.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_THREADID_ADDR"></span><span id="error_bad_threadid_addr"></span>**ERROR\_BAD\_THREADID\_ADDR**
</dt> <dd> <dl> <dt>

159 (0x9F)
</dt> <dt>



The address for the thread ID is not correct.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_ARGUMENTS"></span><span id="error_bad_arguments"></span>**ERROR\_BAD\_ARGUMENTS**
</dt> <dd> <dl> <dt>

160 (0xA0)
</dt> <dt>



One or more arguments are not correct.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_PATHNAME"></span><span id="error_bad_pathname"></span>**ERROR\_BAD\_PATHNAME**
</dt> <dd> <dl> <dt>

161 (0xA1)
</dt> <dt>



The specified path is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_SIGNAL_PENDING"></span><span id="error_signal_pending"></span>**ERROR\_SIGNAL\_PENDING**
</dt> <dd> <dl> <dt>

162 (0xA2)
</dt> <dt>



A signal is already pending.


</dt> </dl> </dd> <dt>

<span id="ERROR_MAX_THRDS_REACHED"></span><span id="error_max_thrds_reached"></span>**ERROR\_MAX\_THRDS\_REACHED**
</dt> <dd> <dl> <dt>

164 (0xA4)
</dt> <dt>



No more threads can be created in the system.


</dt> </dl> </dd> <dt>

<span id="ERROR_LOCK_FAILED"></span><span id="error_lock_failed"></span>**ERROR\_LOCK\_FAILED**
</dt> <dd> <dl> <dt>

167 (0xA7)
</dt> <dt>



Unable to lock a region of a file.


</dt> </dl> </dd> <dt>

<span id="ERROR_BUSY"></span><span id="error_busy"></span>**ERROR\_BUSY**
</dt> <dd> <dl> <dt>

170 (0xAA)
</dt> <dt>



The requested resource is in use.


</dt> </dl> </dd> <dt>

<span id="ERROR_DEVICE_SUPPORT_IN_PROGRESS"></span><span id="error_device_support_in_progress"></span>**ERROR\_DEVICE\_SUPPORT\_IN\_PROGRESS**
</dt> <dd> <dl> <dt>

171 (0xAB)
</dt> <dt>



Device's command support detection is in progress.


</dt> </dl> </dd> <dt>

<span id="ERROR_CANCEL_VIOLATION"></span><span id="error_cancel_violation"></span>**ERROR\_CANCEL\_VIOLATION**
</dt> <dd> <dl> <dt>

173 (0xAD)
</dt> <dt>



A lock request was not outstanding for the supplied cancel region.


</dt> </dl> </dd> <dt>

<span id="ERROR_ATOMIC_LOCKS_NOT_SUPPORTED"></span><span id="error_atomic_locks_not_supported"></span>**ERROR\_ATOMIC\_LOCKS\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

174 (0xAE)
</dt> <dt>



The file system does not support atomic changes to the lock type.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_SEGMENT_NUMBER"></span><span id="error_invalid_segment_number"></span>**ERROR\_INVALID\_SEGMENT\_NUMBER**
</dt> <dd> <dl> <dt>

180 (0xB4)
</dt> <dt>



The system detected a segment number that was not correct.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_ORDINAL"></span><span id="error_invalid_ordinal"></span>**ERROR\_INVALID\_ORDINAL**
</dt> <dd> <dl> <dt>

182 (0xB6)
</dt> <dt>



The operating system cannot run %1.


</dt> </dl> </dd> <dt>

<span id="ERROR_ALREADY_EXISTS"></span><span id="error_already_exists"></span>**ERROR\_ALREADY\_EXISTS**
</dt> <dd> <dl> <dt>

183 (0xB7)
</dt> <dt>



Cannot create a file when that file already exists.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_FLAG_NUMBER"></span><span id="error_invalid_flag_number"></span>**ERROR\_INVALID\_FLAG\_NUMBER**
</dt> <dd> <dl> <dt>

186 (0xBA)
</dt> <dt>



The flag passed is not correct.


</dt> </dl> </dd> <dt>

<span id="ERROR_SEM_NOT_FOUND"></span><span id="error_sem_not_found"></span>**ERROR\_SEM\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

187 (0xBB)
</dt> <dt>



The specified system semaphore name was not found.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_STARTING_CODESEG"></span><span id="error_invalid_starting_codeseg"></span>**ERROR\_INVALID\_STARTING\_CODESEG**
</dt> <dd> <dl> <dt>

188 (0xBC)
</dt> <dt>



The operating system cannot run %1.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_STACKSEG"></span><span id="error_invalid_stackseg"></span>**ERROR\_INVALID\_STACKSEG**
</dt> <dd> <dl> <dt>

189 (0xBD)
</dt> <dt>



The operating system cannot run %1.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_MODULETYPE"></span><span id="error_invalid_moduletype"></span>**ERROR\_INVALID\_MODULETYPE**
</dt> <dd> <dl> <dt>

190 (0xBE)
</dt> <dt>



The operating system cannot run %1.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_EXE_SIGNATURE"></span><span id="error_invalid_exe_signature"></span>**ERROR\_INVALID\_EXE\_SIGNATURE**
</dt> <dd> <dl> <dt>

191 (0xBF)
</dt> <dt>



Cannot run %1 in Win32 mode.


</dt> </dl> </dd> <dt>

<span id="ERROR_EXE_MARKED_INVALID"></span><span id="error_exe_marked_invalid"></span>**ERROR\_EXE\_MARKED\_INVALID**
</dt> <dd> <dl> <dt>

192 (0xC0)
</dt> <dt>



The operating system cannot run %1.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_EXE_FORMAT"></span><span id="error_bad_exe_format"></span>**ERROR\_BAD\_EXE\_FORMAT**
</dt> <dd> <dl> <dt>

193 (0xC1)
</dt> <dt>



%1 is not a valid Win32 application.


</dt> </dl> </dd> <dt>

<span id="ERROR_ITERATED_DATA_EXCEEDS_64k"></span><span id="error_iterated_data_exceeds_64k"></span><span id="ERROR_ITERATED_DATA_EXCEEDS_64K"></span>**ERROR\_ITERATED\_DATA\_EXCEEDS\_64k**
</dt> <dd> <dl> <dt>

194 (0xC2)
</dt> <dt>



The operating system cannot run %1.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_MINALLOCSIZE"></span><span id="error_invalid_minallocsize"></span>**ERROR\_INVALID\_MINALLOCSIZE**
</dt> <dd> <dl> <dt>

195 (0xC3)
</dt> <dt>



The operating system cannot run %1.


</dt> </dl> </dd> <dt>

<span id="ERROR_DYNLINK_FROM_INVALID_RING"></span><span id="error_dynlink_from_invalid_ring"></span>**ERROR\_DYNLINK\_FROM\_INVALID\_RING**
</dt> <dd> <dl> <dt>

196 (0xC4)
</dt> <dt>



The operating system cannot run this application program.


</dt> </dl> </dd> <dt>

<span id="ERROR_IOPL_NOT_ENABLED"></span><span id="error_iopl_not_enabled"></span>**ERROR\_IOPL\_NOT\_ENABLED**
</dt> <dd> <dl> <dt>

197 (0xC5)
</dt> <dt>



The operating system is not presently configured to run this application.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_SEGDPL"></span><span id="error_invalid_segdpl"></span>**ERROR\_INVALID\_SEGDPL**
</dt> <dd> <dl> <dt>

198 (0xC6)
</dt> <dt>



The operating system cannot run %1.


</dt> </dl> </dd> <dt>

<span id="ERROR_AUTODATASEG_EXCEEDS_64k"></span><span id="error_autodataseg_exceeds_64k"></span><span id="ERROR_AUTODATASEG_EXCEEDS_64K"></span>**ERROR\_AUTODATASEG\_EXCEEDS\_64k**
</dt> <dd> <dl> <dt>

199 (0xC7)
</dt> <dt>



The operating system cannot run this application program.


</dt> </dl> </dd> <dt>

<span id="ERROR_RING2SEG_MUST_BE_MOVABLE"></span><span id="error_ring2seg_must_be_movable"></span>**ERROR\_RING2SEG\_MUST\_BE\_MOVABLE**
</dt> <dd> <dl> <dt>

200 (0xC8)
</dt> <dt>



The code segment cannot be greater than or equal to 64K.


</dt> </dl> </dd> <dt>

<span id="ERROR_RELOC_CHAIN_XEEDS_SEGLIM"></span><span id="error_reloc_chain_xeeds_seglim"></span>**ERROR\_RELOC\_CHAIN\_XEEDS\_SEGLIM**
</dt> <dd> <dl> <dt>

201 (0xC9)
</dt> <dt>



The operating system cannot run %1.


</dt> </dl> </dd> <dt>

<span id="ERROR_INFLOOP_IN_RELOC_CHAIN"></span><span id="error_infloop_in_reloc_chain"></span>**ERROR\_INFLOOP\_IN\_RELOC\_CHAIN**
</dt> <dd> <dl> <dt>

202 (0xCA)
</dt> <dt>



The operating system cannot run %1.


</dt> </dl> </dd> <dt>

<span id="ERROR_ENVVAR_NOT_FOUND"></span><span id="error_envvar_not_found"></span>**ERROR\_ENVVAR\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

203 (0xCB)
</dt> <dt>



The system could not find the environment option that was entered.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_SIGNAL_SENT"></span><span id="error_no_signal_sent"></span>**ERROR\_NO\_SIGNAL\_SENT**
</dt> <dd> <dl> <dt>

205 (0xCD)
</dt> <dt>



No process in the command subtree has a signal handler.


</dt> </dl> </dd> <dt>

<span id="ERROR_FILENAME_EXCED_RANGE"></span><span id="error_filename_exced_range"></span>**ERROR\_FILENAME\_EXCED\_RANGE**
</dt> <dd> <dl> <dt>

206 (0xCE)
</dt> <dt>



The filename or extension is too long.


</dt> </dl> </dd> <dt>

<span id="ERROR_RING2_STACK_IN_USE"></span><span id="error_ring2_stack_in_use"></span>**ERROR\_RING2\_STACK\_IN\_USE**
</dt> <dd> <dl> <dt>

207 (0xCF)
</dt> <dt>



The ring 2 stack is in use.


</dt> </dl> </dd> <dt>

<span id="ERROR_META_EXPANSION_TOO_LONG"></span><span id="error_meta_expansion_too_long"></span>**ERROR\_META\_EXPANSION\_TOO\_LONG**
</dt> <dd> <dl> <dt>

208 (0xD0)
</dt> <dt>



The global filename characters, \* or ?, are entered incorrectly or too many global filename characters are specified.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_SIGNAL_NUMBER"></span><span id="error_invalid_signal_number"></span>**ERROR\_INVALID\_SIGNAL\_NUMBER**
</dt> <dd> <dl> <dt>

209 (0xD1)
</dt> <dt>



The signal being posted is not correct.


</dt> </dl> </dd> <dt>

<span id="ERROR_THREAD_1_INACTIVE"></span><span id="error_thread_1_inactive"></span>**ERROR\_THREAD\_1\_INACTIVE**
</dt> <dd> <dl> <dt>

210 (0xD2)
</dt> <dt>



The signal handler cannot be set.


</dt> </dl> </dd> <dt>

<span id="ERROR_LOCKED"></span><span id="error_locked"></span>**ERROR\_LOCKED**
</dt> <dd> <dl> <dt>

212 (0xD4)
</dt> <dt>



The segment is locked and cannot be reallocated.


</dt> </dl> </dd> <dt>

<span id="ERROR_TOO_MANY_MODULES"></span><span id="error_too_many_modules"></span>**ERROR\_TOO\_MANY\_MODULES**
</dt> <dd> <dl> <dt>

214 (0xD6)
</dt> <dt>



Too many dynamic-link modules are attached to this program or dynamic-link module.


</dt> </dl> </dd> <dt>

<span id="ERROR_NESTING_NOT_ALLOWED"></span><span id="error_nesting_not_allowed"></span>**ERROR\_NESTING\_NOT\_ALLOWED**
</dt> <dd> <dl> <dt>

215 (0xD7)
</dt> <dt>



Cannot nest calls to LoadModule.


</dt> </dl> </dd> <dt>

<span id="ERROR_EXE_MACHINE_TYPE_MISMATCH"></span><span id="error_exe_machine_type_mismatch"></span>**ERROR\_EXE\_MACHINE\_TYPE\_MISMATCH**
</dt> <dd> <dl> <dt>

216 (0xD8)
</dt> <dt>



This version of %1 is not compatible with the version of Windows you're running. Check your computer's system information and then contact the software publisher.


</dt> </dl> </dd> <dt>

<span id="ERROR_EXE_CANNOT_MODIFY_SIGNED_BINARY"></span><span id="error_exe_cannot_modify_signed_binary"></span>**ERROR\_EXE\_CANNOT\_MODIFY\_SIGNED\_BINARY**
</dt> <dd> <dl> <dt>

217 (0xD9)
</dt> <dt>



The image file %1 is signed, unable to modify.


</dt> </dl> </dd> <dt>

<span id="ERROR_EXE_CANNOT_MODIFY_STRONG_SIGNED_BINARY"></span><span id="error_exe_cannot_modify_strong_signed_binary"></span>**ERROR\_EXE\_CANNOT\_MODIFY\_STRONG\_SIGNED\_BINARY**
</dt> <dd> <dl> <dt>

218 (0xDA)
</dt> <dt>



The image file %1 is strong signed, unable to modify.


</dt> </dl> </dd> <dt>

<span id="ERROR_FILE_CHECKED_OUT"></span><span id="error_file_checked_out"></span>**ERROR\_FILE\_CHECKED\_OUT**
</dt> <dd> <dl> <dt>

220 (0xDC)
</dt> <dt>



This file is checked out or locked for editing by another user.


</dt> </dl> </dd> <dt>

<span id="ERROR_CHECKOUT_REQUIRED"></span><span id="error_checkout_required"></span>**ERROR\_CHECKOUT\_REQUIRED**
</dt> <dd> <dl> <dt>

221 (0xDD)
</dt> <dt>



The file must be checked out before saving changes.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_FILE_TYPE"></span><span id="error_bad_file_type"></span>**ERROR\_BAD\_FILE\_TYPE**
</dt> <dd> <dl> <dt>

222 (0xDE)
</dt> <dt>



The file type being saved or retrieved has been blocked.


</dt> </dl> </dd> <dt>

<span id="ERROR_FILE_TOO_LARGE"></span><span id="error_file_too_large"></span>**ERROR\_FILE\_TOO\_LARGE**
</dt> <dd> <dl> <dt>

223 (0xDF)
</dt> <dt>



The file size exceeds the limit allowed and cannot be saved.


</dt> </dl> </dd> <dt>

<span id="ERROR_FORMS_AUTH_REQUIRED"></span><span id="error_forms_auth_required"></span>**ERROR\_FORMS\_AUTH\_REQUIRED**
</dt> <dd> <dl> <dt>

224 (0xE0)
</dt> <dt>



Access Denied. Before opening files in this location, you must first add the web site to your trusted sites list, browse to the web site, and select the option to login automatically.


</dt> </dl> </dd> <dt>

<span id="ERROR_VIRUS_INFECTED"></span><span id="error_virus_infected"></span>**ERROR\_VIRUS\_INFECTED**
</dt> <dd> <dl> <dt>

225 (0xE1)
</dt> <dt>



Operation did not complete successfully because the file contains a virus or potentially unwanted software.


</dt> </dl> </dd> <dt>

<span id="ERROR_VIRUS_DELETED"></span><span id="error_virus_deleted"></span>**ERROR\_VIRUS\_DELETED**
</dt> <dd> <dl> <dt>

226 (0xE2)
</dt> <dt>



This file contains a virus or potentially unwanted software and cannot be opened. Due to the nature of this virus or potentially unwanted software, the file has been removed from this location.


</dt> </dl> </dd> <dt>

<span id="ERROR_PIPE_LOCAL"></span><span id="error_pipe_local"></span>**ERROR\_PIPE\_LOCAL**
</dt> <dd> <dl> <dt>

229 (0xE5)
</dt> <dt>



The pipe is local.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_PIPE"></span><span id="error_bad_pipe"></span>**ERROR\_BAD\_PIPE**
</dt> <dd> <dl> <dt>

230 (0xE6)
</dt> <dt>



The pipe state is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_PIPE_BUSY"></span><span id="error_pipe_busy"></span>**ERROR\_PIPE\_BUSY**
</dt> <dd> <dl> <dt>

231 (0xE7)
</dt> <dt>



All pipe instances are busy.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_DATA"></span><span id="error_no_data"></span>**ERROR\_NO\_DATA**
</dt> <dd> <dl> <dt>

232 (0xE8)
</dt> <dt>



The pipe is being closed.


</dt> </dl> </dd> <dt>

<span id="ERROR_PIPE_NOT_CONNECTED"></span><span id="error_pipe_not_connected"></span>**ERROR\_PIPE\_NOT\_CONNECTED**
</dt> <dd> <dl> <dt>

233 (0xE9)
</dt> <dt>



No process is on the other end of the pipe.


</dt> </dl> </dd> <dt>

<span id="ERROR_MORE_DATA"></span><span id="error_more_data"></span>**ERROR\_MORE\_DATA**
</dt> <dd> <dl> <dt>

234 (0xEA)
</dt> <dt>



More data is available.


</dt> </dl> </dd> <dt>

<span id="ERROR_VC_DISCONNECTED"></span><span id="error_vc_disconnected"></span>**ERROR\_VC\_DISCONNECTED**
</dt> <dd> <dl> <dt>

240 (0xF0)
</dt> <dt>



The session was canceled.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_EA_NAME"></span><span id="error_invalid_ea_name"></span>**ERROR\_INVALID\_EA\_NAME**
</dt> <dd> <dl> <dt>

254 (0xFE)
</dt> <dt>



The specified extended attribute name was invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_EA_LIST_INCONSISTENT"></span><span id="error_ea_list_inconsistent"></span>**ERROR\_EA\_LIST\_INCONSISTENT**
</dt> <dd> <dl> <dt>

255 (0xFF)
</dt> <dt>



The extended attributes are inconsistent.


</dt> </dl> </dd> <dt>

<span id="WAIT_TIMEOUT"></span><span id="wait_timeout"></span>**WAIT\_TIMEOUT**
</dt> <dd> <dl> <dt>

258 (0x102)
</dt> <dt>



The wait operation timed out.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_MORE_ITEMS"></span><span id="error_no_more_items"></span>**ERROR\_NO\_MORE\_ITEMS**
</dt> <dd> <dl> <dt>

259 (0x103)
</dt> <dt>



No more data is available.


</dt> </dl> </dd> <dt>

<span id="ERROR_CANNOT_COPY"></span><span id="error_cannot_copy"></span>**ERROR\_CANNOT\_COPY**
</dt> <dd> <dl> <dt>

266 (0x10A)
</dt> <dt>



The copy functions cannot be used.


</dt> </dl> </dd> <dt>

<span id="ERROR_DIRECTORY"></span><span id="error_directory"></span>**ERROR\_DIRECTORY**
</dt> <dd> <dl> <dt>

267 (0x10B)
</dt> <dt>



The directory name is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_EAS_DIDNT_FIT"></span><span id="error_eas_didnt_fit"></span>**ERROR\_EAS\_DIDNT\_FIT**
</dt> <dd> <dl> <dt>

275 (0x113)
</dt> <dt>



The extended attributes did not fit in the buffer.


</dt> </dl> </dd> <dt>

<span id="ERROR_EA_FILE_CORRUPT"></span><span id="error_ea_file_corrupt"></span>**ERROR\_EA\_FILE\_CORRUPT**
</dt> <dd> <dl> <dt>

276 (0x114)
</dt> <dt>



The extended attribute file on the mounted file system is corrupt.


</dt> </dl> </dd> <dt>

<span id="ERROR_EA_TABLE_FULL"></span><span id="error_ea_table_full"></span>**ERROR\_EA\_TABLE\_FULL**
</dt> <dd> <dl> <dt>

277 (0x115)
</dt> <dt>



The extended attribute table file is full.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_EA_HANDLE"></span><span id="error_invalid_ea_handle"></span>**ERROR\_INVALID\_EA\_HANDLE**
</dt> <dd> <dl> <dt>

278 (0x116)
</dt> <dt>



The specified extended attribute handle is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_EAS_NOT_SUPPORTED"></span><span id="error_eas_not_supported"></span>**ERROR\_EAS\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

282 (0x11A)
</dt> <dt>



The mounted file system does not support extended attributes.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_OWNER"></span><span id="error_not_owner"></span>**ERROR\_NOT\_OWNER**
</dt> <dd> <dl> <dt>

288 (0x120)
</dt> <dt>



Attempt to release mutex not owned by caller.


</dt> </dl> </dd> <dt>

<span id="ERROR_TOO_MANY_POSTS"></span><span id="error_too_many_posts"></span>**ERROR\_TOO\_MANY\_POSTS**
</dt> <dd> <dl> <dt>

298 (0x12A)
</dt> <dt>



Too many posts were made to a semaphore.


</dt> </dl> </dd> <dt>

<span id="ERROR_PARTIAL_COPY"></span><span id="error_partial_copy"></span>**ERROR\_PARTIAL\_COPY**
</dt> <dd> <dl> <dt>

299 (0x12B)
</dt> <dt>



Only part of a ReadProcessMemory or WriteProcessMemory request was completed.


</dt> </dl> </dd> <dt>

<span id="ERROR_OPLOCK_NOT_GRANTED"></span><span id="error_oplock_not_granted"></span>**ERROR\_OPLOCK\_NOT\_GRANTED**
</dt> <dd> <dl> <dt>

300 (0x12C)
</dt> <dt>



The oplock request is denied.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_OPLOCK_PROTOCOL"></span><span id="error_invalid_oplock_protocol"></span>**ERROR\_INVALID\_OPLOCK\_PROTOCOL**
</dt> <dd> <dl> <dt>

301 (0x12D)
</dt> <dt>



An invalid oplock acknowledgment was received by the system.


</dt> </dl> </dd> <dt>

<span id="ERROR_DISK_TOO_FRAGMENTED"></span><span id="error_disk_too_fragmented"></span>**ERROR\_DISK\_TOO\_FRAGMENTED**
</dt> <dd> <dl> <dt>

302 (0x12E)
</dt> <dt>



The volume is too fragmented to complete this operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_DELETE_PENDING"></span><span id="error_delete_pending"></span>**ERROR\_DELETE\_PENDING**
</dt> <dd> <dl> <dt>

303 (0x12F)
</dt> <dt>



The file cannot be opened because it is in the process of being deleted.


</dt> </dl> </dd> <dt>

<span id="ERROR_INCOMPATIBLE_WITH_GLOBAL_SHORT_NAME_REGISTRY_SETTING"></span><span id="error_incompatible_with_global_short_name_registry_setting"></span>**ERROR\_INCOMPATIBLE\_WITH\_GLOBAL\_SHORT\_NAME\_REGISTRY\_SETTING**
</dt> <dd> <dl> <dt>

304 (0x130)
</dt> <dt>



Short name settings may not be changed on this volume due to the global registry setting.


</dt> </dl> </dd> <dt>

<span id="ERROR_SHORT_NAMES_NOT_ENABLED_ON_VOLUME"></span><span id="error_short_names_not_enabled_on_volume"></span>**ERROR\_SHORT\_NAMES\_NOT\_ENABLED\_ON\_VOLUME**
</dt> <dd> <dl> <dt>

305 (0x131)
</dt> <dt>



Short names are not enabled on this volume.


</dt> </dl> </dd> <dt>

<span id="ERROR_SECURITY_STREAM_IS_INCONSISTENT"></span><span id="error_security_stream_is_inconsistent"></span>**ERROR\_SECURITY\_STREAM\_IS\_INCONSISTENT**
</dt> <dd> <dl> <dt>

306 (0x132)
</dt> <dt>



The security stream for the given volume is in an inconsistent state. Please run CHKDSK on the volume.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_LOCK_RANGE"></span><span id="error_invalid_lock_range"></span>**ERROR\_INVALID\_LOCK\_RANGE**
</dt> <dd> <dl> <dt>

307 (0x133)
</dt> <dt>



A requested file lock operation cannot be processed due to an invalid byte range.


</dt> </dl> </dd> <dt>

<span id="ERROR_IMAGE_SUBSYSTEM_NOT_PRESENT"></span><span id="error_image_subsystem_not_present"></span>**ERROR\_IMAGE\_SUBSYSTEM\_NOT\_PRESENT**
</dt> <dd> <dl> <dt>

308 (0x134)
</dt> <dt>



The subsystem needed to support the image type is not present.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOTIFICATION_GUID_ALREADY_DEFINED"></span><span id="error_notification_guid_already_defined"></span>**ERROR\_NOTIFICATION\_GUID\_ALREADY\_DEFINED**
</dt> <dd> <dl> <dt>

309 (0x135)
</dt> <dt>



The specified file already has a notification GUID associated with it.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_EXCEPTION_HANDLER"></span><span id="error_invalid_exception_handler"></span>**ERROR\_INVALID\_EXCEPTION\_HANDLER**
</dt> <dd> <dl> <dt>

310 (0x136)
</dt> <dt>



An invalid exception handler routine has been detected.


</dt> </dl> </dd> <dt>

<span id="ERROR_DUPLICATE_PRIVILEGES"></span><span id="error_duplicate_privileges"></span>**ERROR\_DUPLICATE\_PRIVILEGES**
</dt> <dd> <dl> <dt>

311 (0x137)
</dt> <dt>



Duplicate privileges were specified for the token.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_RANGES_PROCESSED"></span><span id="error_no_ranges_processed"></span>**ERROR\_NO\_RANGES\_PROCESSED**
</dt> <dd> <dl> <dt>

312 (0x138)
</dt> <dt>



No ranges for the specified operation were able to be processed.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_ALLOWED_ON_SYSTEM_FILE"></span><span id="error_not_allowed_on_system_file"></span>**ERROR\_NOT\_ALLOWED\_ON\_SYSTEM\_FILE**
</dt> <dd> <dl> <dt>

313 (0x139)
</dt> <dt>



Operation is not allowed on a file system internal file.


</dt> </dl> </dd> <dt>

<span id="ERROR_DISK_RESOURCES_EXHAUSTED"></span><span id="error_disk_resources_exhausted"></span>**ERROR\_DISK\_RESOURCES\_EXHAUSTED**
</dt> <dd> <dl> <dt>

314 (0x13A)
</dt> <dt>



The physical resources of this disk have been exhausted.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_TOKEN"></span><span id="error_invalid_token"></span>**ERROR\_INVALID\_TOKEN**
</dt> <dd> <dl> <dt>

315 (0x13B)
</dt> <dt>



The token representing the data is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_DEVICE_FEATURE_NOT_SUPPORTED"></span><span id="error_device_feature_not_supported"></span>**ERROR\_DEVICE\_FEATURE\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

316 (0x13C)
</dt> <dt>



The device does not support the command feature.


</dt> </dl> </dd> <dt>

<span id="ERROR_MR_MID_NOT_FOUND"></span><span id="error_mr_mid_not_found"></span>**ERROR\_MR\_MID\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

317 (0x13D)
</dt> <dt>



The system cannot find message text for message number 0x%1 in the message file for %2.


</dt> </dl> </dd> <dt>

<span id="ERROR_SCOPE_NOT_FOUND"></span><span id="error_scope_not_found"></span>**ERROR\_SCOPE\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

318 (0x13E)
</dt> <dt>



The scope specified was not found.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNDEFINED_SCOPE"></span><span id="error_undefined_scope"></span>**ERROR\_UNDEFINED\_SCOPE**
</dt> <dd> <dl> <dt>

319 (0x13F)
</dt> <dt>



The Central Access Policy specified is not defined on the target machine.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_CAP"></span><span id="error_invalid_cap"></span>**ERROR\_INVALID\_CAP**
</dt> <dd> <dl> <dt>

320 (0x140)
</dt> <dt>



The Central Access Policy obtained from Active Directory is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_DEVICE_UNREACHABLE"></span><span id="error_device_unreachable"></span>**ERROR\_DEVICE\_UNREACHABLE**
</dt> <dd> <dl> <dt>

321 (0x141)
</dt> <dt>



The device is unreachable.


</dt> </dl> </dd> <dt>

<span id="ERROR_DEVICE_NO_RESOURCES"></span><span id="error_device_no_resources"></span>**ERROR\_DEVICE\_NO\_RESOURCES**
</dt> <dd> <dl> <dt>

322 (0x142)
</dt> <dt>



The target device has insufficient resources to complete the operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_DATA_CHECKSUM_ERROR"></span><span id="error_data_checksum_error"></span>**ERROR\_DATA\_CHECKSUM\_ERROR**
</dt> <dd> <dl> <dt>

323 (0x143)
</dt> <dt>



A data integrity checksum error occurred. Data in the file stream is corrupt.


</dt> </dl> </dd> <dt>

<span id="ERROR_INTERMIXED_KERNEL_EA_OPERATION"></span><span id="error_intermixed_kernel_ea_operation"></span>**ERROR\_INTERMIXED\_KERNEL\_EA\_OPERATION**
</dt> <dd> <dl> <dt>

324 (0x144)
</dt> <dt>



An attempt was made to modify both a KERNEL and normal Extended Attribute (EA) in the same operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_FILE_LEVEL_TRIM_NOT_SUPPORTED"></span><span id="error_file_level_trim_not_supported"></span>**ERROR\_FILE\_LEVEL\_TRIM\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

326 (0x146)
</dt> <dt>



Device does not support file-level TRIM.


</dt> </dl> </dd> <dt>

<span id="ERROR_OFFSET_ALIGNMENT_VIOLATION"></span><span id="error_offset_alignment_violation"></span>**ERROR\_OFFSET\_ALIGNMENT\_VIOLATION**
</dt> <dd> <dl> <dt>

327 (0x147)
</dt> <dt>



The command specified a data offset that does not align to the device's granularity/alignment.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_FIELD_IN_PARAMETER_LIST"></span><span id="error_invalid_field_in_parameter_list"></span>**ERROR\_INVALID\_FIELD\_IN\_PARAMETER\_LIST**
</dt> <dd> <dl> <dt>

328 (0x148)
</dt> <dt>



The command specified an invalid field in its parameter list.


</dt> </dl> </dd> <dt>

<span id="ERROR_OPERATION_IN_PROGRESS"></span><span id="error_operation_in_progress"></span>**ERROR\_OPERATION\_IN\_PROGRESS**
</dt> <dd> <dl> <dt>

329 (0x149)
</dt> <dt>



An operation is currently in progress with the device.


</dt> </dl> </dd> <dt>

<span id="ERROR_BAD_DEVICE_PATH"></span><span id="error_bad_device_path"></span>**ERROR\_BAD\_DEVICE\_PATH**
</dt> <dd> <dl> <dt>

330 (0x14A)
</dt> <dt>



An attempt was made to send down the command via an invalid path to the target device.


</dt> </dl> </dd> <dt>

<span id="ERROR_TOO_MANY_DESCRIPTORS"></span><span id="error_too_many_descriptors"></span>**ERROR\_TOO\_MANY\_DESCRIPTORS**
</dt> <dd> <dl> <dt>

331 (0x14B)
</dt> <dt>



The command specified a number of descriptors that exceeded the maximum supported by the device.


</dt> </dl> </dd> <dt>

<span id="ERROR_SCRUB_DATA_DISABLED"></span><span id="error_scrub_data_disabled"></span>**ERROR\_SCRUB\_DATA\_DISABLED**
</dt> <dd> <dl> <dt>

332 (0x14C)
</dt> <dt>



Scrub is disabled on the specified file.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_REDUNDANT_STORAGE"></span><span id="error_not_redundant_storage"></span>**ERROR\_NOT\_REDUNDANT\_STORAGE**
</dt> <dd> <dl> <dt>

333 (0x14D)
</dt> <dt>



The storage device does not provide redundancy.


</dt> </dl> </dd> <dt>

<span id="ERROR_RESIDENT_FILE_NOT_SUPPORTED"></span><span id="error_resident_file_not_supported"></span>**ERROR\_RESIDENT\_FILE\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

334 (0x14E)
</dt> <dt>



An operation is not supported on a resident file.


</dt> </dl> </dd> <dt>

<span id="ERROR_COMPRESSED_FILE_NOT_SUPPORTED"></span><span id="error_compressed_file_not_supported"></span>**ERROR\_COMPRESSED\_FILE\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

335 (0x14F)
</dt> <dt>



An operation is not supported on a compressed file.


</dt> </dl> </dd> <dt>

<span id="ERROR_DIRECTORY_NOT_SUPPORTED"></span><span id="error_directory_not_supported"></span>**ERROR\_DIRECTORY\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

336 (0x150)
</dt> <dt>



An operation is not supported on a directory.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_READ_FROM_COPY"></span><span id="error_not_read_from_copy"></span>**ERROR\_NOT\_READ\_FROM\_COPY**
</dt> <dd> <dl> <dt>

337 (0x151)
</dt> <dt>



The specified copy of the requested data could not be read.


</dt> </dl> </dd> <dt>

<span id="ERROR_FAIL_NOACTION_REBOOT"></span><span id="error_fail_noaction_reboot"></span>**ERROR\_FAIL\_NOACTION\_REBOOT**
</dt> <dd> <dl> <dt>

350 (0x15E)
</dt> <dt>



No action was taken as a system reboot is required.


</dt> </dl> </dd> <dt>

<span id="ERROR_FAIL_SHUTDOWN"></span><span id="error_fail_shutdown"></span>**ERROR\_FAIL\_SHUTDOWN**
</dt> <dd> <dl> <dt>

351 (0x15F)
</dt> <dt>



The shutdown operation failed.


</dt> </dl> </dd> <dt>

<span id="ERROR_FAIL_RESTART"></span><span id="error_fail_restart"></span>**ERROR\_FAIL\_RESTART**
</dt> <dd> <dl> <dt>

352 (0x160)
</dt> <dt>



The restart operation failed.


</dt> </dl> </dd> <dt>

<span id="ERROR_MAX_SESSIONS_REACHED"></span><span id="error_max_sessions_reached"></span>**ERROR\_MAX\_SESSIONS\_REACHED**
</dt> <dd> <dl> <dt>

353 (0x161)
</dt> <dt>



The maximum number of sessions has been reached.


</dt> </dl> </dd> <dt>

<span id="ERROR_THREAD_MODE_ALREADY_BACKGROUND"></span><span id="error_thread_mode_already_background"></span>**ERROR\_THREAD\_MODE\_ALREADY\_BACKGROUND**
</dt> <dd> <dl> <dt>

400 (0x190)
</dt> <dt>



The thread is already in background processing mode.


</dt> </dl> </dd> <dt>

<span id="ERROR_THREAD_MODE_NOT_BACKGROUND"></span><span id="error_thread_mode_not_background"></span>**ERROR\_THREAD\_MODE\_NOT\_BACKGROUND**
</dt> <dd> <dl> <dt>

401 (0x191)
</dt> <dt>



The thread is not in background processing mode.


</dt> </dl> </dd> <dt>

<span id="ERROR_PROCESS_MODE_ALREADY_BACKGROUND"></span><span id="error_process_mode_already_background"></span>**ERROR\_PROCESS\_MODE\_ALREADY\_BACKGROUND**
</dt> <dd> <dl> <dt>

402 (0x192)
</dt> <dt>



The process is already in background processing mode.


</dt> </dl> </dd> <dt>

<span id="ERROR_PROCESS_MODE_NOT_BACKGROUND"></span><span id="error_process_mode_not_background"></span>**ERROR\_PROCESS\_MODE\_NOT\_BACKGROUND**
</dt> <dd> <dl> <dt>

403 (0x193)
</dt> <dt>



The process is not in background processing mode.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_ADDRESS"></span><span id="error_invalid_address"></span>**ERROR\_INVALID\_ADDRESS**
</dt> <dd> <dl> <dt>

487 (0x1E7)
</dt> <dt>



Attempt to access invalid address.


</dt> </dl> </dd> </dl>


## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>WinError.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[System Error Codes](system-error-codes.md)
</dt> </dl>

 

 





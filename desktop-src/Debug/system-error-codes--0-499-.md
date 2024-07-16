---
description: Describes error codes 0-499 defined in the WinError.h header file and is intended for developers.
ms.assetid: cacb0aec-d438-4875-a96e-4e0239fdc6ba
title: System Error Codes (0-499) (WinError.h)
ms.topic: reference
ms.date: 07/15/2024
---

# System Error Codes (0-499)

The following list describes [system error codes](system-error-codes.md) (errors 0 to 499). They are returned by the [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) function when many functions fail. To retrieve the description text for the error in your application, use the [**FormatMessage**](/windows/desktop/api/WinBase/nf-winbase-formatmessage) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag.

> [!NOTE]
> This information is intended for developers debugging system errors. For other errors, such as issues with Windows Update, see the list of resources on the [Error codes](system-error-codes.md) page.

 

<span id="ERROR_SUCCESS"></span><span id="error_success"></span>**ERROR\_SUCCESS**
   

0 (0x0)
 



The operation completed successfully.


   

<span id="ERROR_INVALID_FUNCTION"></span><span id="error_invalid_function"></span>**ERROR\_INVALID\_FUNCTION**
   

1 (0x1)
 



Incorrect function.


   

<span id="ERROR_FILE_NOT_FOUND"></span><span id="error_file_not_found"></span>**ERROR\_FILE\_NOT\_FOUND**
   

2 (0x2)
 



The system cannot find the file specified.


   

<span id="ERROR_PATH_NOT_FOUND"></span><span id="error_path_not_found"></span>**ERROR\_PATH\_NOT\_FOUND**
   

3 (0x3)
 



The system cannot find the path specified.


   

<span id="ERROR_TOO_MANY_OPEN_FILES"></span><span id="error_too_many_open_files"></span>**ERROR\_TOO\_MANY\_OPEN\_FILES**
   

4 (0x4)
 



The system cannot open the file.


   

<span id="ERROR_ACCESS_DENIED"></span><span id="error_access_denied"></span>**ERROR\_ACCESS\_DENIED**
   

5 (0x5)
 



Access is denied.


   

<span id="ERROR_INVALID_HANDLE"></span><span id="error_invalid_handle"></span>**ERROR\_INVALID\_HANDLE**
   

6 (0x6)
 



The handle is invalid.


   

<span id="ERROR_ARENA_TRASHED"></span><span id="error_arena_trashed"></span>**ERROR\_ARENA\_TRASHED**
   

7 (0x7)
 



The storage control blocks were destroyed.


   

<span id="ERROR_NOT_ENOUGH_MEMORY"></span><span id="error_not_enough_memory"></span>**ERROR\_NOT\_ENOUGH\_MEMORY**
   

8 (0x8)
 



Not enough memory resources are available to process this command.


   

<span id="ERROR_INVALID_BLOCK"></span><span id="error_invalid_block"></span>**ERROR\_INVALID\_BLOCK**
   

9 (0x9)
 



The storage control block address is invalid.


   

<span id="ERROR_BAD_ENVIRONMENT"></span><span id="error_bad_environment"></span>**ERROR\_BAD\_ENVIRONMENT**
   

10 (0xA)
 



The environment is incorrect.


   

<span id="ERROR_BAD_FORMAT"></span><span id="error_bad_format"></span>**ERROR\_BAD\_FORMAT**
   

11 (0xB)
 



An attempt was made to load a program with an incorrect format.


   

<span id="ERROR_INVALID_ACCESS"></span><span id="error_invalid_access"></span>**ERROR\_INVALID\_ACCESS**
   

12 (0xC)
 



The access code is invalid.


   

<span id="ERROR_INVALID_DATA"></span><span id="error_invalid_data"></span>**ERROR\_INVALID\_DATA**
   

13 (0xD)
 



The data is invalid.


   

<span id="ERROR_OUTOFMEMORY"></span><span id="error_outofmemory"></span>**ERROR\_OUTOFMEMORY**
   

14 (0xE)
 



Not enough storage is available to complete this operation.


   

<span id="ERROR_INVALID_DRIVE"></span><span id="error_invalid_drive"></span>**ERROR\_INVALID\_DRIVE**
   

15 (0xF)
 



The system cannot find the drive specified.


   

<span id="ERROR_CURRENT_DIRECTORY"></span><span id="error_current_directory"></span>**ERROR\_CURRENT\_DIRECTORY**
   

16 (0x10)
 



The directory cannot be removed.


   

<span id="ERROR_NOT_SAME_DEVICE"></span><span id="error_not_same_device"></span>**ERROR\_NOT\_SAME\_DEVICE**
   

17 (0x11)
 



The system cannot move the file to a different disk drive.


   

<span id="ERROR_NO_MORE_FILES"></span><span id="error_no_more_files"></span>**ERROR\_NO\_MORE\_FILES**
   

18 (0x12)
 



There are no more files.


   

<span id="ERROR_WRITE_PROTECT"></span><span id="error_write_protect"></span>**ERROR\_WRITE\_PROTECT**
   

19 (0x13)
 



The media is write protected.


   

<span id="ERROR_BAD_UNIT"></span><span id="error_bad_unit"></span>**ERROR\_BAD\_UNIT**
   

20 (0x14)
 



The system cannot find the device specified.


   

<span id="ERROR_NOT_READY"></span><span id="error_not_ready"></span>**ERROR\_NOT\_READY**
   

21 (0x15)
 



The device is not ready.


   

<span id="ERROR_BAD_COMMAND"></span><span id="error_bad_command"></span>**ERROR\_BAD\_COMMAND**
   

22 (0x16)
 



The device does not recognize the command.


   

<span id="ERROR_CRC"></span><span id="error_crc"></span>**ERROR\_CRC**
   

23 (0x17)
 



Data error (cyclic redundancy check).


   

<span id="ERROR_BAD_LENGTH"></span><span id="error_bad_length"></span>**ERROR\_BAD\_LENGTH**
   

24 (0x18)
 



The program issued a command but the command length is incorrect.


   

<span id="ERROR_SEEK"></span><span id="error_seek"></span>**ERROR\_SEEK**
   

25 (0x19)
 



The drive cannot locate a specific area or track on the disk.


   

<span id="ERROR_NOT_DOS_DISK"></span><span id="error_not_dos_disk"></span>**ERROR\_NOT\_DOS\_DISK**
   

26 (0x1A)
 



The specified disk or diskette cannot be accessed.


   

<span id="ERROR_SECTOR_NOT_FOUND"></span><span id="error_sector_not_found"></span>**ERROR\_SECTOR\_NOT\_FOUND**
   

27 (0x1B)
 



The drive cannot find the sector requested.


   

<span id="ERROR_OUT_OF_PAPER"></span><span id="error_out_of_paper"></span>**ERROR\_OUT\_OF\_PAPER**
   

28 (0x1C)
 



The printer is out of paper.


   

<span id="ERROR_WRITE_FAULT"></span><span id="error_write_fault"></span>**ERROR\_WRITE\_FAULT**
   

29 (0x1D)
 



The system cannot write to the specified device.


   

<span id="ERROR_READ_FAULT"></span><span id="error_read_fault"></span>**ERROR\_READ\_FAULT**
   

30 (0x1E)
 



The system cannot read from the specified device.


   

<span id="ERROR_GEN_FAILURE"></span><span id="error_gen_failure"></span>**ERROR\_GEN\_FAILURE**
   

31 (0x1F)
 



A device attached to the system is not functioning.


   

<span id="ERROR_SHARING_VIOLATION"></span><span id="error_sharing_violation"></span>**ERROR\_SHARING\_VIOLATION**
   

32 (0x20)
 



The process cannot access the file because it is being used by another process.


   

<span id="ERROR_LOCK_VIOLATION"></span><span id="error_lock_violation"></span>**ERROR\_LOCK\_VIOLATION**
   

33 (0x21)
 



The process cannot access the file because another process has locked a portion of the file.


   

<span id="ERROR_WRONG_DISK"></span><span id="error_wrong_disk"></span>**ERROR\_WRONG\_DISK**
   

34 (0x22)
 



The wrong diskette is in the drive. Insert %2 (Volume Serial Number: %3) into drive %1.


   

<span id="ERROR_SHARING_BUFFER_EXCEEDED"></span><span id="error_sharing_buffer_exceeded"></span>**ERROR\_SHARING\_BUFFER\_EXCEEDED**
   

36 (0x24)
 



Too many files opened for sharing.


   

<span id="ERROR_HANDLE_EOF"></span><span id="error_handle_eof"></span>**ERROR\_HANDLE\_EOF**
   

38 (0x26)
 



Reached the end of the file.


   

<span id="ERROR_HANDLE_DISK_FULL"></span><span id="error_handle_disk_full"></span>**ERROR\_HANDLE\_DISK\_FULL**
   

39 (0x27)
 



The disk is full.


   

<span id="ERROR_NOT_SUPPORTED"></span><span id="error_not_supported"></span>**ERROR\_NOT\_SUPPORTED**
   

50 (0x32)
 



The request is not supported.


   

<span id="ERROR_REM_NOT_LIST"></span><span id="error_rem_not_list"></span>**ERROR\_REM\_NOT\_LIST**
   

51 (0x33)
 



Windows cannot find the network path. Verify that the network path is correct and the destination computer is not busy or turned off. If Windows still cannot find the network path, contact your network administrator.


   

<span id="ERROR_DUP_NAME"></span><span id="error_dup_name"></span>**ERROR\_DUP\_NAME**
   

52 (0x34)
 



You were not connected because a duplicate name exists on the network. If joining a domain, go to System in Control Panel to change the computer name and try again. If joining a workgroup, choose another workgroup name.


   

<span id="ERROR_BAD_NETPATH"></span><span id="error_bad_netpath"></span>**ERROR\_BAD\_NETPATH**
   

53 (0x35)
 



The network path was not found.


   

<span id="ERROR_NETWORK_BUSY"></span><span id="error_network_busy"></span>**ERROR\_NETWORK\_BUSY**
   

54 (0x36)
 



The network is busy.


   

<span id="ERROR_DEV_NOT_EXIST"></span><span id="error_dev_not_exist"></span>**ERROR\_DEV\_NOT\_EXIST**
   

55 (0x37)
 



The specified network resource or device is no longer available.


   

<span id="ERROR_TOO_MANY_CMDS"></span><span id="error_too_many_cmds"></span>**ERROR\_TOO\_MANY\_CMDS**
   

56 (0x38)
 



The network BIOS command limit has been reached.


   

<span id="ERROR_ADAP_HDW_ERR"></span><span id="error_adap_hdw_err"></span>**ERROR\_ADAP\_HDW\_ERR**
   

57 (0x39)
 



A network adapter hardware error occurred.


   

<span id="ERROR_BAD_NET_RESP"></span><span id="error_bad_net_resp"></span>**ERROR\_BAD\_NET\_RESP**
   

58 (0x3A)
 



The specified server cannot perform the requested operation.


   

<span id="ERROR_UNEXP_NET_ERR"></span><span id="error_unexp_net_err"></span>**ERROR\_UNEXP\_NET\_ERR**
   

59 (0x3B)
 



An unexpected network error occurred.


   

<span id="ERROR_BAD_REM_ADAP"></span><span id="error_bad_rem_adap"></span>**ERROR\_BAD\_REM\_ADAP**
   

60 (0x3C)
 



The remote adapter is not compatible.


   

<span id="ERROR_PRINTQ_FULL"></span><span id="error_printq_full"></span>**ERROR\_PRINTQ\_FULL**
   

61 (0x3D)
 



The printer queue is full.


   

<span id="ERROR_NO_SPOOL_SPACE"></span><span id="error_no_spool_space"></span>**ERROR\_NO\_SPOOL\_SPACE**
   

62 (0x3E)
 



Space to store the file waiting to be printed is not available on the server.


   

<span id="ERROR_PRINT_CANCELLED"></span><span id="error_print_cancelled"></span>**ERROR\_PRINT\_CANCELLED**
   

63 (0x3F)
 



Your file waiting to be printed was deleted.


   

<span id="ERROR_NETNAME_DELETED"></span><span id="error_netname_deleted"></span>**ERROR\_NETNAME\_DELETED**
   

64 (0x40)
 



The specified network name is no longer available.


   

<span id="ERROR_NETWORK_ACCESS_DENIED"></span><span id="error_network_access_denied"></span>**ERROR\_NETWORK\_ACCESS\_DENIED**
   

65 (0x41)
 



Network access is denied.


   

<span id="ERROR_BAD_DEV_TYPE"></span><span id="error_bad_dev_type"></span>**ERROR\_BAD\_DEV\_TYPE**
   

66 (0x42)
 



The network resource type is not correct.


   

<span id="ERROR_BAD_NET_NAME"></span><span id="error_bad_net_name"></span>**ERROR\_BAD\_NET\_NAME**
   

67 (0x43)
 



The network name cannot be found.


   

<span id="ERROR_TOO_MANY_NAMES"></span><span id="error_too_many_names"></span>**ERROR\_TOO\_MANY\_NAMES**
   

68 (0x44)
 



The name limit for the local computer network adapter card was exceeded.


   

<span id="ERROR_TOO_MANY_SESS"></span><span id="error_too_many_sess"></span>**ERROR\_TOO\_MANY\_SESS**
   

69 (0x45)
 



The network BIOS session limit was exceeded.


   

<span id="ERROR_SHARING_PAUSED"></span><span id="error_sharing_paused"></span>**ERROR\_SHARING\_PAUSED**
   

70 (0x46)
 



The remote server has been paused or is in the process of being started.


   

<span id="ERROR_REQ_NOT_ACCEP"></span><span id="error_req_not_accep"></span>**ERROR\_REQ\_NOT\_ACCEP**
   

71 (0x47)
 



No more connections can be made to this remote computer at this time because there are already as many connections as the computer can accept.


   

<span id="ERROR_REDIR_PAUSED"></span><span id="error_redir_paused"></span>**ERROR\_REDIR\_PAUSED**
   

72 (0x48)
 



The specified printer or disk device has been paused.


   

<span id="ERROR_FILE_EXISTS"></span><span id="error_file_exists"></span>**ERROR\_FILE\_EXISTS**
   

80 (0x50)
 



The file exists.


   

<span id="ERROR_CANNOT_MAKE"></span><span id="error_cannot_make"></span>**ERROR\_CANNOT\_MAKE**
   

82 (0x52)
 



The directory or file cannot be created.


   

<span id="ERROR_FAIL_I24"></span><span id="error_fail_i24"></span>**ERROR\_FAIL\_I24**
   

83 (0x53)
 



Fail on INT 24.


   

<span id="ERROR_OUT_OF_STRUCTURES"></span><span id="error_out_of_structures"></span>**ERROR\_OUT\_OF\_STRUCTURES**
   

84 (0x54)
 



Storage to process this request is not available.


   

<span id="ERROR_ALREADY_ASSIGNED"></span><span id="error_already_assigned"></span>**ERROR\_ALREADY\_ASSIGNED**
   

85 (0x55)
 



The local device name is already in use.


   

<span id="ERROR_INVALID_PASSWORD"></span><span id="error_invalid_password"></span>**ERROR\_INVALID\_PASSWORD**
   

86 (0x56)
 



The specified network password is not correct.


   

<span id="ERROR_INVALID_PARAMETER"></span><span id="error_invalid_parameter"></span>**ERROR\_INVALID\_PARAMETER**
   

87 (0x57)
 



The parameter is incorrect.


   

<span id="ERROR_NET_WRITE_FAULT"></span><span id="error_net_write_fault"></span>**ERROR\_NET\_WRITE\_FAULT**
   

88 (0x58)
 



A write fault occurred on the network.


   

<span id="ERROR_NO_PROC_SLOTS"></span><span id="error_no_proc_slots"></span>**ERROR\_NO\_PROC\_SLOTS**
   

89 (0x59)
 



The system cannot start another process at this time.


   

<span id="ERROR_TOO_MANY_SEMAPHORES"></span><span id="error_too_many_semaphores"></span>**ERROR\_TOO\_MANY\_SEMAPHORES**
   

100 (0x64)
 



Cannot create another system semaphore.


   

<span id="ERROR_EXCL_SEM_ALREADY_OWNED"></span><span id="error_excl_sem_already_owned"></span>**ERROR\_EXCL\_SEM\_ALREADY\_OWNED**
   

101 (0x65)
 



The exclusive semaphore is owned by another process.


   

<span id="ERROR_SEM_IS_SET"></span><span id="error_sem_is_set"></span>**ERROR\_SEM\_IS\_SET**
   

102 (0x66)
 



The semaphore is set and cannot be closed.


   

<span id="ERROR_TOO_MANY_SEM_REQUESTS"></span><span id="error_too_many_sem_requests"></span>**ERROR\_TOO\_MANY\_SEM\_REQUESTS**
   

103 (0x67)
 



The semaphore cannot be set again.


   

<span id="ERROR_INVALID_AT_INTERRUPT_TIME"></span><span id="error_invalid_at_interrupt_time"></span>**ERROR\_INVALID\_AT\_INTERRUPT\_TIME**
   

104 (0x68)
 



Cannot request exclusive semaphores at interrupt time.


   

<span id="ERROR_SEM_OWNER_DIED"></span><span id="error_sem_owner_died"></span>**ERROR\_SEM\_OWNER\_DIED**
   

105 (0x69)
 



The previous ownership of this semaphore has ended.


   

<span id="ERROR_SEM_USER_LIMIT"></span><span id="error_sem_user_limit"></span>**ERROR\_SEM\_USER\_LIMIT**
   

106 (0x6A)
 



Insert the diskette for drive %1.


   

<span id="ERROR_DISK_CHANGE"></span><span id="error_disk_change"></span>**ERROR\_DISK\_CHANGE**
   

107 (0x6B)
 



The program stopped because an alternate diskette was not inserted.


   

<span id="ERROR_DRIVE_LOCKED"></span><span id="error_drive_locked"></span>**ERROR\_DRIVE\_LOCKED**
   

108 (0x6C)
 



The disk is in use or locked by another process.


   

<span id="ERROR_BROKEN_PIPE"></span><span id="error_broken_pipe"></span>**ERROR\_BROKEN\_PIPE**
   

109 (0x6D)
 



The pipe has been ended.


   

<span id="ERROR_OPEN_FAILED"></span><span id="error_open_failed"></span>**ERROR\_OPEN\_FAILED**
   

110 (0x6E)
 



The system cannot open the device or file specified.


   

<span id="ERROR_BUFFER_OVERFLOW"></span><span id="error_buffer_overflow"></span>**ERROR\_BUFFER\_OVERFLOW**
   

111 (0x6F)
 



The file name is too long.


   

<span id="ERROR_DISK_FULL"></span><span id="error_disk_full"></span>**ERROR\_DISK\_FULL**
   

112 (0x70)
 



There is not enough space on the disk.


   

<span id="ERROR_NO_MORE_SEARCH_HANDLES"></span><span id="error_no_more_search_handles"></span>**ERROR\_NO\_MORE\_SEARCH\_HANDLES**
   

113 (0x71)
 



No more internal file identifiers available.


   

<span id="ERROR_INVALID_TARGET_HANDLE"></span><span id="error_invalid_target_handle"></span>**ERROR\_INVALID\_TARGET\_HANDLE**
   

114 (0x72)
 



The target internal file identifier is incorrect.


   

<span id="ERROR_INVALID_CATEGORY"></span><span id="error_invalid_category"></span>**ERROR\_INVALID\_CATEGORY**
   

117 (0x75)
 



The IOCTL call made by the application program is not correct.


   

<span id="ERROR_INVALID_VERIFY_SWITCH"></span><span id="error_invalid_verify_switch"></span>**ERROR\_INVALID\_VERIFY\_SWITCH**
   

118 (0x76)
 



The verify-on-write switch parameter value is not correct.


   

<span id="ERROR_BAD_DRIVER_LEVEL"></span><span id="error_bad_driver_level"></span>**ERROR\_BAD\_DRIVER\_LEVEL**
   

119 (0x77)
 



The system does not support the command requested.


   

<span id="ERROR_CALL_NOT_IMPLEMENTED"></span><span id="error_call_not_implemented"></span>**ERROR\_CALL\_NOT\_IMPLEMENTED**
   

120 (0x78)
 



This function is not supported on this system.


   

<span id="ERROR_SEM_TIMEOUT"></span><span id="error_sem_timeout"></span>**ERROR\_SEM\_TIMEOUT**
   

121 (0x79)
 



The semaphore timeout period has expired.


   

<span id="ERROR_INSUFFICIENT_BUFFER"></span><span id="error_insufficient_buffer"></span>**ERROR\_INSUFFICIENT\_BUFFER**
   

122 (0x7A)
 



The data area passed to a system call is too small.


   

<span id="ERROR_INVALID_NAME"></span><span id="error_invalid_name"></span>**ERROR\_INVALID\_NAME**
   

123 (0x7B)
 



The filename, directory name, or volume label syntax is incorrect.


   

<span id="ERROR_INVALID_LEVEL"></span><span id="error_invalid_level"></span>**ERROR\_INVALID\_LEVEL**
   

124 (0x7C)
 



The system call level is not correct.


   

<span id="ERROR_NO_VOLUME_LABEL"></span><span id="error_no_volume_label"></span>**ERROR\_NO\_VOLUME\_LABEL**
   

125 (0x7D)
 



The disk has no volume label.


   

<span id="ERROR_MOD_NOT_FOUND"></span><span id="error_mod_not_found"></span>**ERROR\_MOD\_NOT\_FOUND**
   

126 (0x7E)
 



The specified module could not be found.


   

<span id="ERROR_PROC_NOT_FOUND"></span><span id="error_proc_not_found"></span>**ERROR\_PROC\_NOT\_FOUND**
   

127 (0x7F)
 



The specified procedure could not be found.


   

<span id="ERROR_WAIT_NO_CHILDREN"></span><span id="error_wait_no_children"></span>**ERROR\_WAIT\_NO\_CHILDREN**
   

128 (0x80)
 



There are no child processes to wait for.


   

<span id="ERROR_CHILD_NOT_COMPLETE"></span><span id="error_child_not_complete"></span>**ERROR\_CHILD\_NOT\_COMPLETE**
   

129 (0x81)
 



The %1 application cannot be run in Win32 mode.


   

<span id="ERROR_DIRECT_ACCESS_HANDLE"></span><span id="error_direct_access_handle"></span>**ERROR\_DIRECT\_ACCESS\_HANDLE**
   

130 (0x82)
 



Attempt to use a file handle to an open disk partition for an operation other than raw disk I/O.


   

<span id="ERROR_NEGATIVE_SEEK"></span><span id="error_negative_seek"></span>**ERROR\_NEGATIVE\_SEEK**
   

131 (0x83)
 



An attempt was made to move the file pointer before the beginning of the file.


   

<span id="ERROR_SEEK_ON_DEVICE"></span><span id="error_seek_on_device"></span>**ERROR\_SEEK\_ON\_DEVICE**
   

132 (0x84)
 



The file pointer cannot be set on the specified device or file.


   

<span id="ERROR_IS_JOIN_TARGET"></span><span id="error_is_join_target"></span>**ERROR\_IS\_JOIN\_TARGET**
   

133 (0x85)
 



A JOIN or SUBST command cannot be used for a drive that contains previously joined drives.


   

<span id="ERROR_IS_JOINED"></span><span id="error_is_joined"></span>**ERROR\_IS\_JOINED**
   

134 (0x86)
 



An attempt was made to use a JOIN or SUBST command on a drive that has already been joined.


   

<span id="ERROR_IS_SUBSTED"></span><span id="error_is_substed"></span>**ERROR\_IS\_SUBSTED**
   

135 (0x87)
 



An attempt was made to use a JOIN or SUBST command on a drive that has already been substituted.


   

<span id="ERROR_NOT_JOINED"></span><span id="error_not_joined"></span>**ERROR\_NOT\_JOINED**
   

136 (0x88)
 



The system tried to delete the JOIN of a drive that is not joined.


   

<span id="ERROR_NOT_SUBSTED"></span><span id="error_not_substed"></span>**ERROR\_NOT\_SUBSTED**
   

137 (0x89)
 



The system tried to delete the substitution of a drive that is not substituted.


   

<span id="ERROR_JOIN_TO_JOIN"></span><span id="error_join_to_join"></span>**ERROR\_JOIN\_TO\_JOIN**
   

138 (0x8A)
 



The system tried to join a drive to a directory on a joined drive.


   

<span id="ERROR_SUBST_TO_SUBST"></span><span id="error_subst_to_subst"></span>**ERROR\_SUBST\_TO\_SUBST**
   

139 (0x8B)
 



The system tried to substitute a drive to a directory on a substituted drive.


   

<span id="ERROR_JOIN_TO_SUBST"></span><span id="error_join_to_subst"></span>**ERROR\_JOIN\_TO\_SUBST**
   

140 (0x8C)
 



The system tried to join a drive to a directory on a substituted drive.


   

<span id="ERROR_SUBST_TO_JOIN"></span><span id="error_subst_to_join"></span>**ERROR\_SUBST\_TO\_JOIN**
   

141 (0x8D)
 



The system tried to SUBST a drive to a directory on a joined drive.


   

<span id="ERROR_BUSY_DRIVE"></span><span id="error_busy_drive"></span>**ERROR\_BUSY\_DRIVE**
   

142 (0x8E)
 



The system cannot perform a JOIN or SUBST at this time.


   

<span id="ERROR_SAME_DRIVE"></span><span id="error_same_drive"></span>**ERROR\_SAME\_DRIVE**
   

143 (0x8F)
 



The system cannot join or substitute a drive to or for a directory on the same drive.


   

<span id="ERROR_DIR_NOT_ROOT"></span><span id="error_dir_not_root"></span>**ERROR\_DIR\_NOT\_ROOT**
   

144 (0x90)
 



The directory is not a subdirectory of the root directory.


   

<span id="ERROR_DIR_NOT_EMPTY"></span><span id="error_dir_not_empty"></span>**ERROR\_DIR\_NOT\_EMPTY**
   

145 (0x91)
 



The directory is not empty.


   

<span id="ERROR_IS_SUBST_PATH"></span><span id="error_is_subst_path"></span>**ERROR\_IS\_SUBST\_PATH**
   

146 (0x92)
 



The path specified is being used in a substitute.


   

<span id="ERROR_IS_JOIN_PATH"></span><span id="error_is_join_path"></span>**ERROR\_IS\_JOIN\_PATH**
   

147 (0x93)
 



Not enough resources are available to process this command.


   

<span id="ERROR_PATH_BUSY"></span><span id="error_path_busy"></span>**ERROR\_PATH\_BUSY**
   

148 (0x94)
 



The path specified cannot be used at this time.


   

<span id="ERROR_IS_SUBST_TARGET"></span><span id="error_is_subst_target"></span>**ERROR\_IS\_SUBST\_TARGET**
   

149 (0x95)
 



An attempt was made to join or substitute a drive for which a directory on the drive is the target of a previous substitute.


   

<span id="ERROR_SYSTEM_TRACE"></span><span id="error_system_trace"></span>**ERROR\_SYSTEM\_TRACE**
   

150 (0x96)
 



System trace information was not specified in your CONFIG.SYS file, or tracing is disallowed.


   

<span id="ERROR_INVALID_EVENT_COUNT"></span><span id="error_invalid_event_count"></span>**ERROR\_INVALID\_EVENT\_COUNT**
   

151 (0x97)
 



The number of specified semaphore events for DosMuxSemWait is not correct.


   

<span id="ERROR_TOO_MANY_MUXWAITERS"></span><span id="error_too_many_muxwaiters"></span>**ERROR\_TOO\_MANY\_MUXWAITERS**
   

152 (0x98)
 



DosMuxSemWait did not execute; too many semaphores are already set.


   

<span id="ERROR_INVALID_LIST_FORMAT"></span><span id="error_invalid_list_format"></span>**ERROR\_INVALID\_LIST\_FORMAT**
   

153 (0x99)
 



The DosMuxSemWait list is not correct.


   

<span id="ERROR_LABEL_TOO_LONG"></span><span id="error_label_too_long"></span>**ERROR\_LABEL\_TOO\_LONG**
   

154 (0x9A)
 



The volume label you entered exceeds the label character limit of the target file system.


   

<span id="ERROR_TOO_MANY_TCBS"></span><span id="error_too_many_tcbs"></span>**ERROR\_TOO\_MANY\_TCBS**
   

155 (0x9B)
 



Cannot create another thread.


   

<span id="ERROR_SIGNAL_REFUSED"></span><span id="error_signal_refused"></span>**ERROR\_SIGNAL\_REFUSED**
   

156 (0x9C)
 



The recipient process has refused the signal.


   

<span id="ERROR_DISCARDED"></span><span id="error_discarded"></span>**ERROR\_DISCARDED**
   

157 (0x9D)
 



The segment is already discarded and cannot be locked.


   

<span id="ERROR_NOT_LOCKED"></span><span id="error_not_locked"></span>**ERROR\_NOT\_LOCKED**
   

158 (0x9E)
 



The segment is already unlocked.


   

<span id="ERROR_BAD_THREADID_ADDR"></span><span id="error_bad_threadid_addr"></span>**ERROR\_BAD\_THREADID\_ADDR**
   

159 (0x9F)
 



The address for the thread ID is not correct.


   

<span id="ERROR_BAD_ARGUMENTS"></span><span id="error_bad_arguments"></span>**ERROR\_BAD\_ARGUMENTS**
   

160 (0xA0)
 



One or more arguments are not correct.


   

<span id="ERROR_BAD_PATHNAME"></span><span id="error_bad_pathname"></span>**ERROR\_BAD\_PATHNAME**
   

161 (0xA1)
 



The specified path is invalid.


   

<span id="ERROR_SIGNAL_PENDING"></span><span id="error_signal_pending"></span>**ERROR\_SIGNAL\_PENDING**
   

162 (0xA2)
 



A signal is already pending.


   

<span id="ERROR_MAX_THRDS_REACHED"></span><span id="error_max_thrds_reached"></span>**ERROR\_MAX\_THRDS\_REACHED**
   

164 (0xA4)
 



No more threads can be created in the system.


   

<span id="ERROR_LOCK_FAILED"></span><span id="error_lock_failed"></span>**ERROR\_LOCK\_FAILED**
   

167 (0xA7)
 



Unable to lock a region of a file.


   

<span id="ERROR_BUSY"></span><span id="error_busy"></span>**ERROR\_BUSY**
   

170 (0xAA)
 



The requested resource is in use.


   

<span id="ERROR_DEVICE_SUPPORT_IN_PROGRESS"></span><span id="error_device_support_in_progress"></span>**ERROR\_DEVICE\_SUPPORT\_IN\_PROGRESS**
   

171 (0xAB)
 



Device's command support detection is in progress.


   

<span id="ERROR_CANCEL_VIOLATION"></span><span id="error_cancel_violation"></span>**ERROR\_CANCEL\_VIOLATION**
   

173 (0xAD)
 



A lock request was not outstanding for the supplied cancel region.


   

<span id="ERROR_ATOMIC_LOCKS_NOT_SUPPORTED"></span><span id="error_atomic_locks_not_supported"></span>**ERROR\_ATOMIC\_LOCKS\_NOT\_SUPPORTED**
   

174 (0xAE)
 



The file system does not support atomic changes to the lock type.


   

<span id="ERROR_INVALID_SEGMENT_NUMBER"></span><span id="error_invalid_segment_number"></span>**ERROR\_INVALID\_SEGMENT\_NUMBER**
   

180 (0xB4)
 



The system detected a segment number that was not correct.


   

<span id="ERROR_INVALID_ORDINAL"></span><span id="error_invalid_ordinal"></span>**ERROR\_INVALID\_ORDINAL**
   

182 (0xB6)
 



The operating system cannot run %1.


   

<span id="ERROR_ALREADY_EXISTS"></span><span id="error_already_exists"></span>**ERROR\_ALREADY\_EXISTS**
   

183 (0xB7)
 



Cannot create a file when that file already exists.


   

<span id="ERROR_INVALID_FLAG_NUMBER"></span><span id="error_invalid_flag_number"></span>**ERROR\_INVALID\_FLAG\_NUMBER**
   

186 (0xBA)
 



The flag passed is not correct.


   

<span id="ERROR_SEM_NOT_FOUND"></span><span id="error_sem_not_found"></span>**ERROR\_SEM\_NOT\_FOUND**
   

187 (0xBB)
 



The specified system semaphore name was not found.


   

<span id="ERROR_INVALID_STARTING_CODESEG"></span><span id="error_invalid_starting_codeseg"></span>**ERROR\_INVALID\_STARTING\_CODESEG**
   

188 (0xBC)
 



The operating system cannot run %1.


   

<span id="ERROR_INVALID_STACKSEG"></span><span id="error_invalid_stackseg"></span>**ERROR\_INVALID\_STACKSEG**
   

189 (0xBD)
 



The operating system cannot run %1.


   

<span id="ERROR_INVALID_MODULETYPE"></span><span id="error_invalid_moduletype"></span>**ERROR\_INVALID\_MODULETYPE**
   

190 (0xBE)
 



The operating system cannot run %1.


   

<span id="ERROR_INVALID_EXE_SIGNATURE"></span><span id="error_invalid_exe_signature"></span>**ERROR\_INVALID\_EXE\_SIGNATURE**
   

191 (0xBF)
 



Cannot run %1 in Win32 mode.


   

<span id="ERROR_EXE_MARKED_INVALID"></span><span id="error_exe_marked_invalid"></span>**ERROR\_EXE\_MARKED\_INVALID**
   

192 (0xC0)
 



The operating system cannot run %1.


   

<span id="ERROR_BAD_EXE_FORMAT"></span><span id="error_bad_exe_format"></span>**ERROR\_BAD\_EXE\_FORMAT**
   

193 (0xC1)
 



%1 is not a valid Win32 application.


   

<span id="ERROR_ITERATED_DATA_EXCEEDS_64k"></span><span id="error_iterated_data_exceeds_64k"></span><span id="ERROR_ITERATED_DATA_EXCEEDS_64K"></span>**ERROR\_ITERATED\_DATA\_EXCEEDS\_64k**
   

194 (0xC2)
 



The operating system cannot run %1.


   

<span id="ERROR_INVALID_MINALLOCSIZE"></span><span id="error_invalid_minallocsize"></span>**ERROR\_INVALID\_MINALLOCSIZE**
   

195 (0xC3)
 



The operating system cannot run %1.


   

<span id="ERROR_DYNLINK_FROM_INVALID_RING"></span><span id="error_dynlink_from_invalid_ring"></span>**ERROR\_DYNLINK\_FROM\_INVALID\_RING**
   

196 (0xC4)
 



The operating system cannot run this application program.


   

<span id="ERROR_IOPL_NOT_ENABLED"></span><span id="error_iopl_not_enabled"></span>**ERROR\_IOPL\_NOT\_ENABLED**
   

197 (0xC5)
 



The operating system is not presently configured to run this application.


   

<span id="ERROR_INVALID_SEGDPL"></span><span id="error_invalid_segdpl"></span>**ERROR\_INVALID\_SEGDPL**
   

198 (0xC6)
 



The operating system cannot run %1.


   

<span id="ERROR_AUTODATASEG_EXCEEDS_64k"></span><span id="error_autodataseg_exceeds_64k"></span><span id="ERROR_AUTODATASEG_EXCEEDS_64K"></span>**ERROR\_AUTODATASEG\_EXCEEDS\_64k**
   

199 (0xC7)
 



The operating system cannot run this application program.


   

<span id="ERROR_RING2SEG_MUST_BE_MOVABLE"></span><span id="error_ring2seg_must_be_movable"></span>**ERROR\_RING2SEG\_MUST\_BE\_MOVABLE**
   

200 (0xC8)
 



The code segment cannot be greater than or equal to 64K.


   

<span id="ERROR_RELOC_CHAIN_XEEDS_SEGLIM"></span><span id="error_reloc_chain_xeeds_seglim"></span>**ERROR\_RELOC\_CHAIN\_XEEDS\_SEGLIM**
   

201 (0xC9)
 



The operating system cannot run %1.


   

<span id="ERROR_INFLOOP_IN_RELOC_CHAIN"></span><span id="error_infloop_in_reloc_chain"></span>**ERROR\_INFLOOP\_IN\_RELOC\_CHAIN**
   

202 (0xCA)
 



The operating system cannot run %1.


   

<span id="ERROR_ENVVAR_NOT_FOUND"></span><span id="error_envvar_not_found"></span>**ERROR\_ENVVAR\_NOT\_FOUND**
   

203 (0xCB)
 



The system could not find the environment option that was entered.


   

<span id="ERROR_NO_SIGNAL_SENT"></span><span id="error_no_signal_sent"></span>**ERROR\_NO\_SIGNAL\_SENT**
   

205 (0xCD)
 



No process in the command subtree has a signal handler.


   

<span id="ERROR_FILENAME_EXCED_RANGE"></span><span id="error_filename_exced_range"></span>**ERROR\_FILENAME\_EXCED\_RANGE**
   

206 (0xCE)
 



The filename or extension is too long.


   

<span id="ERROR_RING2_STACK_IN_USE"></span><span id="error_ring2_stack_in_use"></span>**ERROR\_RING2\_STACK\_IN\_USE**
   

207 (0xCF)
 



The ring 2 stack is in use.


   

<span id="ERROR_META_EXPANSION_TOO_LONG"></span><span id="error_meta_expansion_too_long"></span>**ERROR\_META\_EXPANSION\_TOO\_LONG**
   

208 (0xD0)
 



The global filename characters, \* or ?, are entered incorrectly or too many global filename characters are specified.


   

<span id="ERROR_INVALID_SIGNAL_NUMBER"></span><span id="error_invalid_signal_number"></span>**ERROR\_INVALID\_SIGNAL\_NUMBER**
   

209 (0xD1)
 



The signal being posted is not correct.


   

<span id="ERROR_THREAD_1_INACTIVE"></span><span id="error_thread_1_inactive"></span>**ERROR\_THREAD\_1\_INACTIVE**
   

210 (0xD2)
 



The signal handler cannot be set.


   

<span id="ERROR_LOCKED"></span><span id="error_locked"></span>**ERROR\_LOCKED**
   

212 (0xD4)
 



The segment is locked and cannot be reallocated.


   

<span id="ERROR_TOO_MANY_MODULES"></span><span id="error_too_many_modules"></span>**ERROR\_TOO\_MANY\_MODULES**
   

214 (0xD6)
 



Too many dynamic-link modules are attached to this program or dynamic-link module.


   

<span id="ERROR_NESTING_NOT_ALLOWED"></span><span id="error_nesting_not_allowed"></span>**ERROR\_NESTING\_NOT\_ALLOWED**
   

215 (0xD7)
 



Cannot nest calls to LoadModule.


   

<span id="ERROR_EXE_MACHINE_TYPE_MISMATCH"></span><span id="error_exe_machine_type_mismatch"></span>**ERROR\_EXE\_MACHINE\_TYPE\_MISMATCH**
   

216 (0xD8)
 



This version of %1 is not compatible with the version of Windows you're running. Check your computer's system information and then contact the software publisher.


   

<span id="ERROR_EXE_CANNOT_MODIFY_SIGNED_BINARY"></span><span id="error_exe_cannot_modify_signed_binary"></span>**ERROR\_EXE\_CANNOT\_MODIFY\_SIGNED\_BINARY**
   

217 (0xD9)
 



The image file %1 is signed, unable to modify.


   

<span id="ERROR_EXE_CANNOT_MODIFY_STRONG_SIGNED_BINARY"></span><span id="error_exe_cannot_modify_strong_signed_binary"></span>**ERROR\_EXE\_CANNOT\_MODIFY\_STRONG\_SIGNED\_BINARY**
   

218 (0xDA)
 



The image file %1 is strong signed, unable to modify.


   

<span id="ERROR_FILE_CHECKED_OUT"></span><span id="error_file_checked_out"></span>**ERROR\_FILE\_CHECKED\_OUT**
   

220 (0xDC)
 



This file is checked out or locked for editing by another user.


   

<span id="ERROR_CHECKOUT_REQUIRED"></span><span id="error_checkout_required"></span>**ERROR\_CHECKOUT\_REQUIRED**
   

221 (0xDD)
 



The file must be checked out before saving changes.


   

<span id="ERROR_BAD_FILE_TYPE"></span><span id="error_bad_file_type"></span>**ERROR\_BAD\_FILE\_TYPE**
   

222 (0xDE)
 



The file type being saved or retrieved has been blocked.


   

<span id="ERROR_FILE_TOO_LARGE"></span><span id="error_file_too_large"></span>**ERROR\_FILE\_TOO\_LARGE**
   

223 (0xDF)
 



The file size exceeds the limit allowed and cannot be saved.


   

<span id="ERROR_FORMS_AUTH_REQUIRED"></span><span id="error_forms_auth_required"></span>**ERROR\_FORMS\_AUTH\_REQUIRED**
   

224 (0xE0)
 



Access Denied. Before opening files in this location, you must first add the web site to your trusted sites list, browse to the web site, and select the option to login automatically.


   

<span id="ERROR_VIRUS_INFECTED"></span><span id="error_virus_infected"></span>**ERROR\_VIRUS\_INFECTED**
   

225 (0xE1)
 



Operation did not complete successfully because the file contains a virus or potentially unwanted software.


   

<span id="ERROR_VIRUS_DELETED"></span><span id="error_virus_deleted"></span>**ERROR\_VIRUS\_DELETED**
   

226 (0xE2)
 



This file contains a virus or potentially unwanted software and cannot be opened. Due to the nature of this virus or potentially unwanted software, the file has been removed from this location.


   

<span id="ERROR_PIPE_LOCAL"></span><span id="error_pipe_local"></span>**ERROR\_PIPE\_LOCAL**
   

229 (0xE5)
 



The pipe is local.


   

<span id="ERROR_BAD_PIPE"></span><span id="error_bad_pipe"></span>**ERROR\_BAD\_PIPE**
   

230 (0xE6)
 



The pipe state is invalid.


   

<span id="ERROR_PIPE_BUSY"></span><span id="error_pipe_busy"></span>**ERROR\_PIPE\_BUSY**
   

231 (0xE7)
 



All pipe instances are busy.


   

<span id="ERROR_NO_DATA"></span><span id="error_no_data"></span>**ERROR\_NO\_DATA**
   

232 (0xE8)
 



The pipe is being closed.


   

<span id="ERROR_PIPE_NOT_CONNECTED"></span><span id="error_pipe_not_connected"></span>**ERROR\_PIPE\_NOT\_CONNECTED**
   

233 (0xE9)
 



No process is on the other end of the pipe.


   

<span id="ERROR_MORE_DATA"></span><span id="error_more_data"></span>**ERROR\_MORE\_DATA**
   

234 (0xEA)
 



More data is available.


   

<span id="ERROR_VC_DISCONNECTED"></span><span id="error_vc_disconnected"></span>**ERROR\_VC\_DISCONNECTED**
   

240 (0xF0)
 



The session was canceled.


   

<span id="ERROR_INVALID_EA_NAME"></span><span id="error_invalid_ea_name"></span>**ERROR\_INVALID\_EA\_NAME**
   

254 (0xFE)
 



The specified extended attribute name was invalid.


   

<span id="ERROR_EA_LIST_INCONSISTENT"></span><span id="error_ea_list_inconsistent"></span>**ERROR\_EA\_LIST\_INCONSISTENT**
   

255 (0xFF)
 



The extended attributes are inconsistent.


   

<span id="WAIT_TIMEOUT"></span><span id="wait_timeout"></span>**WAIT\_TIMEOUT**
   

258 (0x102)
 



The wait operation timed out.


   

<span id="ERROR_NO_MORE_ITEMS"></span><span id="error_no_more_items"></span>**ERROR\_NO\_MORE\_ITEMS**
   

259 (0x103)
 



No more data is available.


   

<span id="ERROR_CANNOT_COPY"></span><span id="error_cannot_copy"></span>**ERROR\_CANNOT\_COPY**
   

266 (0x10A)
 



The copy functions cannot be used.


   

<span id="ERROR_DIRECTORY"></span><span id="error_directory"></span>**ERROR\_DIRECTORY**
   

267 (0x10B)
 



The directory name is invalid.


   

<span id="ERROR_EAS_DIDNT_FIT"></span><span id="error_eas_didnt_fit"></span>**ERROR\_EAS\_DIDNT\_FIT**
   

275 (0x113)
 



The extended attributes did not fit in the buffer.


   

<span id="ERROR_EA_FILE_CORRUPT"></span><span id="error_ea_file_corrupt"></span>**ERROR\_EA\_FILE\_CORRUPT**
   

276 (0x114)
 



The extended attribute file on the mounted file system is corrupt.


   

<span id="ERROR_EA_TABLE_FULL"></span><span id="error_ea_table_full"></span>**ERROR\_EA\_TABLE\_FULL**
   

277 (0x115)
 



The extended attribute table file is full.


   

<span id="ERROR_INVALID_EA_HANDLE"></span><span id="error_invalid_ea_handle"></span>**ERROR\_INVALID\_EA\_HANDLE**
   

278 (0x116)
 



The specified extended attribute handle is invalid.


   

<span id="ERROR_EAS_NOT_SUPPORTED"></span><span id="error_eas_not_supported"></span>**ERROR\_EAS\_NOT\_SUPPORTED**
   

282 (0x11A)
 



The mounted file system does not support extended attributes.


   

<span id="ERROR_NOT_OWNER"></span><span id="error_not_owner"></span>**ERROR\_NOT\_OWNER**
   

288 (0x120)
 



Attempt to release mutex not owned by caller.


   

<span id="ERROR_TOO_MANY_POSTS"></span><span id="error_too_many_posts"></span>**ERROR\_TOO\_MANY\_POSTS**
   

298 (0x12A)
 



Too many posts were made to a semaphore.


   

<span id="ERROR_PARTIAL_COPY"></span><span id="error_partial_copy"></span>**ERROR\_PARTIAL\_COPY**
   

299 (0x12B)
 



Only part of a ReadProcessMemory or WriteProcessMemory request was completed.


   

<span id="ERROR_OPLOCK_NOT_GRANTED"></span><span id="error_oplock_not_granted"></span>**ERROR\_OPLOCK\_NOT\_GRANTED**
   

300 (0x12C)
 



The oplock request is denied.


   

<span id="ERROR_INVALID_OPLOCK_PROTOCOL"></span><span id="error_invalid_oplock_protocol"></span>**ERROR\_INVALID\_OPLOCK\_PROTOCOL**
   

301 (0x12D)
 



An invalid oplock acknowledgment was received by the system.


   

<span id="ERROR_DISK_TOO_FRAGMENTED"></span><span id="error_disk_too_fragmented"></span>**ERROR\_DISK\_TOO\_FRAGMENTED**
   

302 (0x12E)
 



The volume is too fragmented to complete this operation.


   

<span id="ERROR_DELETE_PENDING"></span><span id="error_delete_pending"></span>**ERROR\_DELETE\_PENDING**
   

303 (0x12F)
 



The file cannot be opened because it is in the process of being deleted.


   

<span id="ERROR_INCOMPATIBLE_WITH_GLOBAL_SHORT_NAME_REGISTRY_SETTING"></span><span id="error_incompatible_with_global_short_name_registry_setting"></span>**ERROR\_INCOMPATIBLE\_WITH\_GLOBAL\_SHORT\_NAME\_REGISTRY\_SETTING**
   

304 (0x130)
 



Short name settings may not be changed on this volume due to the global registry setting.


   

<span id="ERROR_SHORT_NAMES_NOT_ENABLED_ON_VOLUME"></span><span id="error_short_names_not_enabled_on_volume"></span>**ERROR\_SHORT\_NAMES\_NOT\_ENABLED\_ON\_VOLUME**
   

305 (0x131)
 



Short names are not enabled on this volume.


   

<span id="ERROR_SECURITY_STREAM_IS_INCONSISTENT"></span><span id="error_security_stream_is_inconsistent"></span>**ERROR\_SECURITY\_STREAM\_IS\_INCONSISTENT**
   

306 (0x132)
 



The security stream for the given volume is in an inconsistent state. Please run CHKDSK on the volume.


   

<span id="ERROR_INVALID_LOCK_RANGE"></span><span id="error_invalid_lock_range"></span>**ERROR\_INVALID\_LOCK\_RANGE**
   

307 (0x133)
 



A requested file lock operation cannot be processed due to an invalid byte range.


   

<span id="ERROR_IMAGE_SUBSYSTEM_NOT_PRESENT"></span><span id="error_image_subsystem_not_present"></span>**ERROR\_IMAGE\_SUBSYSTEM\_NOT\_PRESENT**
   

308 (0x134)
 



The subsystem needed to support the image type is not present.


   

<span id="ERROR_NOTIFICATION_GUID_ALREADY_DEFINED"></span><span id="error_notification_guid_already_defined"></span>**ERROR\_NOTIFICATION\_GUID\_ALREADY\_DEFINED**
   

309 (0x135)
 



The specified file already has a notification GUID associated with it.


   

<span id="ERROR_INVALID_EXCEPTION_HANDLER"></span><span id="error_invalid_exception_handler"></span>**ERROR\_INVALID\_EXCEPTION\_HANDLER**
   

310 (0x136)
 



An invalid exception handler routine has been detected.


   

<span id="ERROR_DUPLICATE_PRIVILEGES"></span><span id="error_duplicate_privileges"></span>**ERROR\_DUPLICATE\_PRIVILEGES**
   

311 (0x137)
 



Duplicate privileges were specified for the token.


   

<span id="ERROR_NO_RANGES_PROCESSED"></span><span id="error_no_ranges_processed"></span>**ERROR\_NO\_RANGES\_PROCESSED**
   

312 (0x138)
 



No ranges for the specified operation were able to be processed.


   

<span id="ERROR_NOT_ALLOWED_ON_SYSTEM_FILE"></span><span id="error_not_allowed_on_system_file"></span>**ERROR\_NOT\_ALLOWED\_ON\_SYSTEM\_FILE**
   

313 (0x139)
 



Operation is not allowed on a file system internal file.


   

<span id="ERROR_DISK_RESOURCES_EXHAUSTED"></span><span id="error_disk_resources_exhausted"></span>**ERROR\_DISK\_RESOURCES\_EXHAUSTED**
   

314 (0x13A)
 



The physical resources of this disk have been exhausted.


   

<span id="ERROR_INVALID_TOKEN"></span><span id="error_invalid_token"></span>**ERROR\_INVALID\_TOKEN**
   

315 (0x13B)
 



The token representing the data is invalid.


   

<span id="ERROR_DEVICE_FEATURE_NOT_SUPPORTED"></span><span id="error_device_feature_not_supported"></span>**ERROR\_DEVICE\_FEATURE\_NOT\_SUPPORTED**
   

316 (0x13C)
 



The device does not support the command feature.


   

<span id="ERROR_MR_MID_NOT_FOUND"></span><span id="error_mr_mid_not_found"></span>**ERROR\_MR\_MID\_NOT\_FOUND**
   

317 (0x13D)
 



The system cannot find message text for message number 0x%1 in the message file for %2.


   

<span id="ERROR_SCOPE_NOT_FOUND"></span><span id="error_scope_not_found"></span>**ERROR\_SCOPE\_NOT\_FOUND**
   

318 (0x13E)
 



The scope specified was not found.


   

<span id="ERROR_UNDEFINED_SCOPE"></span><span id="error_undefined_scope"></span>**ERROR\_UNDEFINED\_SCOPE**
   

319 (0x13F)
 



The Central Access Policy specified is not defined on the target machine.


   

<span id="ERROR_INVALID_CAP"></span><span id="error_invalid_cap"></span>**ERROR\_INVALID\_CAP**
   

320 (0x140)
 



The Central Access Policy obtained from Active Directory is invalid.


   

<span id="ERROR_DEVICE_UNREACHABLE"></span><span id="error_device_unreachable"></span>**ERROR\_DEVICE\_UNREACHABLE**
   

321 (0x141)
 



The device is unreachable.


   

<span id="ERROR_DEVICE_NO_RESOURCES"></span><span id="error_device_no_resources"></span>**ERROR\_DEVICE\_NO\_RESOURCES**
   

322 (0x142)
 



The target device has insufficient resources to complete the operation.


   

<span id="ERROR_DATA_CHECKSUM_ERROR"></span><span id="error_data_checksum_error"></span>**ERROR\_DATA\_CHECKSUM\_ERROR**
   

323 (0x143)
 



A data integrity checksum error occurred. Data in the file stream is corrupt.


   

<span id="ERROR_INTERMIXED_KERNEL_EA_OPERATION"></span><span id="error_intermixed_kernel_ea_operation"></span>**ERROR\_INTERMIXED\_KERNEL\_EA\_OPERATION**
   

324 (0x144)
 



An attempt was made to modify both a KERNEL and normal Extended Attribute (EA) in the same operation.


   

<span id="ERROR_FILE_LEVEL_TRIM_NOT_SUPPORTED"></span><span id="error_file_level_trim_not_supported"></span>**ERROR\_FILE\_LEVEL\_TRIM\_NOT\_SUPPORTED**
   

326 (0x146)
 



Device does not support file-level TRIM.


   

<span id="ERROR_OFFSET_ALIGNMENT_VIOLATION"></span><span id="error_offset_alignment_violation"></span>**ERROR\_OFFSET\_ALIGNMENT\_VIOLATION**
   

327 (0x147)
 



The command specified a data offset that does not align to the device's granularity/alignment.


   

<span id="ERROR_INVALID_FIELD_IN_PARAMETER_LIST"></span><span id="error_invalid_field_in_parameter_list"></span>**ERROR\_INVALID\_FIELD\_IN\_PARAMETER\_LIST**
   

328 (0x148)
 



The command specified an invalid field in its parameter list.


   

<span id="ERROR_OPERATION_IN_PROGRESS"></span><span id="error_operation_in_progress"></span>**ERROR\_OPERATION\_IN\_PROGRESS**
   

329 (0x149)
 



An operation is currently in progress with the device.


   

<span id="ERROR_BAD_DEVICE_PATH"></span><span id="error_bad_device_path"></span>**ERROR\_BAD\_DEVICE\_PATH**
   

330 (0x14A)
 



An attempt was made to send down the command via an invalid path to the target device.


   

<span id="ERROR_TOO_MANY_DESCRIPTORS"></span><span id="error_too_many_descriptors"></span>**ERROR\_TOO\_MANY\_DESCRIPTORS**
   

331 (0x14B)
 



The command specified a number of descriptors that exceeded the maximum supported by the device.


   

<span id="ERROR_SCRUB_DATA_DISABLED"></span><span id="error_scrub_data_disabled"></span>**ERROR\_SCRUB\_DATA\_DISABLED**
   

332 (0x14C)
 



Scrub is disabled on the specified file.


   

<span id="ERROR_NOT_REDUNDANT_STORAGE"></span><span id="error_not_redundant_storage"></span>**ERROR\_NOT\_REDUNDANT\_STORAGE**
   

333 (0x14D)
 



The storage device does not provide redundancy.


   

<span id="ERROR_RESIDENT_FILE_NOT_SUPPORTED"></span><span id="error_resident_file_not_supported"></span>**ERROR\_RESIDENT\_FILE\_NOT\_SUPPORTED**
   

334 (0x14E)
 



An operation is not supported on a resident file.


   

<span id="ERROR_COMPRESSED_FILE_NOT_SUPPORTED"></span><span id="error_compressed_file_not_supported"></span>**ERROR\_COMPRESSED\_FILE\_NOT\_SUPPORTED**
   

335 (0x14F)
 



An operation is not supported on a compressed file.


   

<span id="ERROR_DIRECTORY_NOT_SUPPORTED"></span><span id="error_directory_not_supported"></span>**ERROR\_DIRECTORY\_NOT\_SUPPORTED**
   

336 (0x150)
 



An operation is not supported on a directory.


   

<span id="ERROR_NOT_READ_FROM_COPY"></span><span id="error_not_read_from_copy"></span>**ERROR\_NOT\_READ\_FROM\_COPY**
   

337 (0x151)
 



The specified copy of the requested data could not be read.


   

<span id="ERROR_FAIL_NOACTION_REBOOT"></span><span id="error_fail_noaction_reboot"></span>**ERROR\_FAIL\_NOACTION\_REBOOT**
   

350 (0x15E)
 



No action was taken as a system reboot is required.


   

<span id="ERROR_FAIL_SHUTDOWN"></span><span id="error_fail_shutdown"></span>**ERROR\_FAIL\_SHUTDOWN**
   

351 (0x15F)
 



The shutdown operation failed.


   

<span id="ERROR_FAIL_RESTART"></span><span id="error_fail_restart"></span>**ERROR\_FAIL\_RESTART**
   

352 (0x160)
 



The restart operation failed.


   

<span id="ERROR_MAX_SESSIONS_REACHED"></span><span id="error_max_sessions_reached"></span>**ERROR\_MAX\_SESSIONS\_REACHED**
   

353 (0x161)
 



The maximum number of sessions has been reached.


   

<span id="ERROR_THREAD_MODE_ALREADY_BACKGROUND"></span><span id="error_thread_mode_already_background"></span>**ERROR\_THREAD\_MODE\_ALREADY\_BACKGROUND**
   

400 (0x190)
 



The thread is already in background processing mode.


   

<span id="ERROR_THREAD_MODE_NOT_BACKGROUND"></span><span id="error_thread_mode_not_background"></span>**ERROR\_THREAD\_MODE\_NOT\_BACKGROUND**
   

401 (0x191)
 



The thread is not in background processing mode.


   

<span id="ERROR_PROCESS_MODE_ALREADY_BACKGROUND"></span><span id="error_process_mode_already_background"></span>**ERROR\_PROCESS\_MODE\_ALREADY\_BACKGROUND**
   

402 (0x192)
 



The process is already in background processing mode.


   

<span id="ERROR_PROCESS_MODE_NOT_BACKGROUND"></span><span id="error_process_mode_not_background"></span>**ERROR\_PROCESS\_MODE\_NOT\_BACKGROUND**
   

403 (0x193)
 



The process is not in background processing mode.


   

<span id="ERROR_INVALID_ADDRESS"></span><span id="error_invalid_address"></span>**ERROR\_INVALID\_ADDRESS**
   

487 (0x1E7)
 



Attempt to access invalid address.


   


## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                      |
| Header<br/>                   |  WinError.h (include Windows.h)  |



## See also

 

[System Error Codes](system-error-codes.md)
 

 

 





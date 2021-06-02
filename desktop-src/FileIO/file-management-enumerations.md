---
description: Enumerations used in file management.
ms.assetid: 14b1cfff-5e47-4309-8e62-fb5c8da9ce97
title: File Management Enumerations
ms.topic: article
ms.date: 05/31/2018
---

# File Management Enumerations

The following enumerations are used in file management.

## In this section



| Enumeration                                                                   | Description                                                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**COPYFILE2\_COPY\_PHASE**](/windows/desktop/api/WinBase/ne-winbase-copyfile2_copy_phase)<br/>             | Indicates the phase of a copy at the time of an error.<br/>                                                                                                                                                                           |
| [**COPYFILE2\_MESSAGE\_ACTION**](/windows/desktop/api/WinBase/ne-winbase-copyfile2_message_action)<br/>     | Returned by the [*CopyFile2ProgressRoutine*](/windows/desktop/api/WinBase/nc-winbase-pcopyfile2_progress_routine) callback function to indicate what action should be taken for the pending copy operation.<br/>                                                             |
| [**COPYFILE2\_MESSAGE\_TYPE**](/windows/desktop/api/WinBase/ne-winbase-copyfile2_message_type)<br/>         | Indicates the type of message passed in the [**COPYFILE2\_MESSAGE**](/windows/desktop/api/WinBase/ns-winbase-copyfile2_message) structure to the [*CopyFile2ProgressRoutine*](/windows/desktop/api/WinBase/nc-winbase-pcopyfile2_progress_routine) callback function.<br/>                                       |
| [**CSV\_CONTROL\_OP**](/windows/desktop/api/WinIoCtl/ne-winioctl-csv_control_op)<br/>                         | Specifies the type of CSV control operation to use with the [**FSCTL\_CSV\_CONTROL**](/windows/win32/api/winioctl/ni-winioctl-fsctl_csv_control) control code.<br/>                                                                                                       |
| [**FILE\_ID\_TYPE**](/windows/desktop/api/WinBase/ne-winbase-file_id_type)<br/>                             | Discriminator for the union in the [**FILE\_ID\_DESCRIPTOR**](/windows/desktop/api/WinBase/ns-winbase-file_id_descriptor) structure.<br/>                                                                                                                                 |
| [**FILE\_INFO\_BY\_HANDLE\_CLASS**](/windows/win32/api/minwinbase/ne-minwinbase-file_info_by_handle_class)<br/> | Identifies the type of file information that [**GetFileInformationByHandleEx**](/windows/desktop/api/WinBase/nf-winbase-getfileinformationbyhandleex) should retrieve or [**SetFileInformationByHandle**](/windows/desktop/api/FileAPI/nf-fileapi-setfileinformationbyhandle) should set.<br/>                |
| [**FINDEX\_INFO\_LEVELS**](/windows/win32/api/minwinbase/ne-minwinbase-findex_info_levels)<br/>             | Defines values that are used with the [**FindFirstFileEx**](/windows/desktop/api/FileAPI/nf-fileapi-findfirstfileexa) function to specify the information level of the returned data.<br/>                                                                                 |
| [**FINDEX\_SEARCH\_OPS**](/windows/win32/api/minwinbase/ne-minwinbase-findex_search_ops)<br/>               | Defines values that are used with the [**FindFirstFileEx**](/windows/desktop/api/FileAPI/nf-fileapi-findfirstfileexa) function to specify the type of filtering to perform.<br/>                                                                                           |
| [**GET\_FILEEX\_INFO\_LEVELS**](/windows/win32/api/minwinbase/ne-minwinbase-get_fileex_info_levels)<br/>        | Defines values that are used with the [**GetFileAttributesEx**](/windows/desktop/api/FileAPI/nf-fileapi-getfileattributesexa) and [**GetFileAttributesTransacted**](/windows/desktop/api/WinBase/nf-winbase-getfileattributestransacteda) functions to specify the information level of the returned data.<br/> |
| [**PRIORITY\_HINT**](/windows/desktop/api/WinBase/ne-winbase-priority_hint)<br/>                            | Defines values that are used with the [**FILE\_IO\_PRIORITY\_HINT\_INFO**](/windows/desktop/api/WinBase/ns-winbase-file_io_priority_hint_info) structure to specify the priority hint for a file I/O operation.<br/>                                                      |
| [**STREAM\_INFO\_LEVELS**](/windows/desktop/api/fileapi/ne-fileapi-stream_info_levels)<br/>                 | Defines values that are used with the [**FindFirstStreamW**](/windows/desktop/api/fileapi/nf-fileapi-findfirststreamw) function to specify the information level of the returned data.<br/>                                                                               |



 

 


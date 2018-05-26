---
Description: Enumerations used in file management.
ms.assetid: 14b1cfff-5e47-4309-8e62-fb5c8da9ce97
title: File Management Enumerations
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# File Management Enumerations

The following enumerations are used in file management.

## In this section



| Enumeration                                                                   | Description                                                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**COPYFILE2\_COPY\_PHASE**](/windows/win32/WinBase/ne-winbase-_copyfile2_copy_phase?branch=master)<br/>             | Indicates the phase of a copy at the time of an error.<br/>                                                                                                                                                                           |
| [**COPYFILE2\_MESSAGE\_ACTION**](/windows/win32/WinBase/ne-winbase-_copyfile2_message_action?branch=master)<br/>     | Returned by the [*CopyFile2ProgressRoutine*](/windows/win32/WinBase/nc-winbase-pcopyfile2_progress_routine?branch=master) callback function to indicate what action should be taken for the pending copy operation.<br/>                                                             |
| [**COPYFILE2\_MESSAGE\_TYPE**](/windows/win32/WinBase/ne-winbase-_copyfile2_message_type?branch=master)<br/>         | Indicates the type of message passed in the [**COPYFILE2\_MESSAGE**](/windows/win32/WinBase/ns-winbase-copyfile2_message?branch=master) structure to the [*CopyFile2ProgressRoutine*](/windows/win32/WinBase/nc-winbase-pcopyfile2_progress_routine?branch=master) callback function.<br/>                                       |
| [**CSV\_CONTROL\_OP**](/windows/win32/WinIoCtl/ne-winioctl-_csv_control_op?branch=master)<br/>                         | Specifies the type of CSV control operation to use with the [**FSCTL\_CSV\_CONTROL**](/windows/win32/WinIoCtl/?branch=master) control code.<br/>                                                                                                       |
| [**FILE\_ID\_TYPE**](/windows/win32/WinBase/ne-winbase-_file_id_type?branch=master)<br/>                             | Discriminator for the union in the [**FILE\_ID\_DESCRIPTOR**](/windows/win32/WinBase/ns-winbase-file_id_descriptor?branch=master) structure.<br/>                                                                                                                                 |
| [**FILE\_INFO\_BY\_HANDLE\_CLASS**](file-info-by-handle-class.md)<br/> | Identifies the type of file information that [**GetFileInformationByHandleEx**](/windows/win32/WinBase/nf-winbase-getfileinformationbyhandleex?branch=master) should retrieve or [**SetFileInformationByHandle**](/windows/win32/FileAPI/nf-fileapi-setfileinformationbyhandle?branch=master) should set.<br/>                |
| [**FINDEX\_INFO\_LEVELS**](findex-info-levels-str.md)<br/>             | Defines values that are used with the [**FindFirstFileEx**](/windows/win32/FileAPI/nf-fileapi-findfirstfileexa?branch=master) function to specify the information level of the returned data.<br/>                                                                                 |
| [**FINDEX\_SEARCH\_OPS**](findex-search-ops-str.md)<br/>               | Defines values that are used with the [**FindFirstFileEx**](/windows/win32/FileAPI/nf-fileapi-findfirstfileexa?branch=master) function to specify the type of filtering to perform.<br/>                                                                                           |
| [**GET\_FILEEX\_INFO\_LEVELS**](get-fileex-info-levels.md)<br/>        | Defines values that are used with the [**GetFileAttributesEx**](/windows/win32/FileAPI/nf-fileapi-getfileattributesexa?branch=master) and [**GetFileAttributesTransacted**](/windows/win32/WinBase/nf-winbase-getfileattributestransacteda?branch=master) functions to specify the information level of the returned data.<br/> |
| [**PRIORITY\_HINT**](/windows/win32/WinBase/ne-winbase-_priority_hint?branch=master)<br/>                            | Defines values that are used with the [**FILE\_IO\_PRIORITY\_HINT\_INFO**](/windows/win32/WinBase/ns-winbase-_file_io_priority_hint_info?branch=master) structure to specify the priority hint for a file I/O operation.<br/>                                                      |
| [**STREAM\_INFO\_LEVELS**](/windows/win32/fileapi/ne-fileapi-_stream_info_levels?branch=master)<br/>                 | Defines values that are used with the [**FindFirstStreamW**](/windows/win32/fileapi/nf-fileapi-findfirststreamw?branch=master) function to specify the information level of the returned data.<br/>                                                                               |



 

 

 





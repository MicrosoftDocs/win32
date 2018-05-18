---
Description: 'Enumerations used in file management.'
ms.assetid: '14b1cfff-5e47-4309-8e62-fb5c8da9ce97'
title: File Management Enumerations
---

# File Management Enumerations

The following enumerations are used in file management.

## In this section



| Enumeration                                                                   | Description                                                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**COPYFILE2\_COPY\_PHASE**](copyfile2-copy-phase.md)<br/>             | Indicates the phase of a copy at the time of an error.<br/>                                                                                                                                                                           |
| [**COPYFILE2\_MESSAGE\_ACTION**](copyfile2-message-action.md)<br/>     | Returned by the [*CopyFile2ProgressRoutine*](copyfile2progressroutine.md) callback function to indicate what action should be taken for the pending copy operation.<br/>                                                             |
| [**COPYFILE2\_MESSAGE\_TYPE**](copyfile2-message-type.md)<br/>         | Indicates the type of message passed in the [**COPYFILE2\_MESSAGE**](copyfile2-message.md) structure to the [*CopyFile2ProgressRoutine*](copyfile2progressroutine.md) callback function.<br/>                                       |
| [**CSV\_CONTROL\_OP**](csv-control-op.md)<br/>                         | Specifies the type of CSV control operation to use with the [**FSCTL\_CSV\_CONTROL**](fsctl-csv-control.md) control code.<br/>                                                                                                       |
| [**FILE\_ID\_TYPE**](file-id-type.md)<br/>                             | Discriminator for the union in the [**FILE\_ID\_DESCRIPTOR**](file-id-descriptor.md) structure.<br/>                                                                                                                                 |
| [**FILE\_INFO\_BY\_HANDLE\_CLASS**](file-info-by-handle-class.md)<br/> | Identifies the type of file information that [**GetFileInformationByHandleEx**](getfileinformationbyhandleex.md) should retrieve or [**SetFileInformationByHandle**](setfileinformationbyhandle.md) should set.<br/>                |
| [**FINDEX\_INFO\_LEVELS**](findex-info-levels-str.md)<br/>             | Defines values that are used with the [**FindFirstFileEx**](findfirstfileex.md) function to specify the information level of the returned data.<br/>                                                                                 |
| [**FINDEX\_SEARCH\_OPS**](findex-search-ops-str.md)<br/>               | Defines values that are used with the [**FindFirstFileEx**](findfirstfileex.md) function to specify the type of filtering to perform.<br/>                                                                                           |
| [**GET\_FILEEX\_INFO\_LEVELS**](get-fileex-info-levels.md)<br/>        | Defines values that are used with the [**GetFileAttributesEx**](getfileattributesex.md) and [**GetFileAttributesTransacted**](getfileattributestransacted.md) functions to specify the information level of the returned data.<br/> |
| [**PRIORITY\_HINT**](priority-hint.md)<br/>                            | Defines values that are used with the [**FILE\_IO\_PRIORITY\_HINT\_INFO**](file-io-priority-hint-info.md) structure to specify the priority hint for a file I/O operation.<br/>                                                      |
| [**STREAM\_INFO\_LEVELS**](stream-info-levels.md)<br/>                 | Defines values that are used with the [**FindFirstStreamW**](findfirststreamw.md) function to specify the information level of the returned data.<br/>                                                                               |



 

 

 





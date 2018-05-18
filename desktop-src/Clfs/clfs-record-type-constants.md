---
Description: 'Specifies the type of records that can be written to a log. These constants are used when a client calls ReadLogRecord, ReadNextLogRecord, or the DumpLogRecords callback function.'
ms.assetid: '63489b1b-75de-469d-9ffc-f0353bb2fdd9'
title: 'CLFS\_RECORD\_TYPE Constants'
---

# CLFS\_RECORD\_TYPE Constants

Specifies the type of records that can be written to a log. These constants are used when a client calls [**ReadLogRecord**](readlogrecord.md), [**ReadNextLogRecord**](readnextlogrecord.md), or the [**DumpLogRecords**](dumplogrecords.md) callback function. The following record types are defined.



| Constant/value                                                                                                                                                                                                                                                         | Description                                                        |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------|
| <span id="ClfsDataRecord"></span><span id="clfsdatarecord"></span><span id="CLFSDATARECORD"></span><dl> <dt>**ClfsDataRecord**</dt> <dt>0x01</dt> </dl>             | Specifies that the log record contains client data.<br/>     |
| <span id="ClfsRestartRecord"></span><span id="clfsrestartrecord"></span><span id="CLFSRESTARTRECORD"></span><dl> <dt>**ClfsRestartRecord**</dt> <dt>0x02</dt> </dl> | Specifies that the log record is a restart record.<br/>      |
| <span id="ClfsClientRecord"></span><span id="clfsclientrecord"></span><span id="CLFSCLIENTRECORD"></span><dl> <dt>**ClfsClientRecord**</dt> <dt>0x3F</dt> </dl>     | Specifies a mask for all valid data or restart records.<br/> |



## Requirements



|                                     |                                                                                                       |
|-------------------------------------|-------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                                               |
| Header<br/>                   | <dl> <dt>Clfs.h (include Clfsw32.h)</dt> </dl> |



## See also

<dl> <dt>

[**DumpLogRecords**](dumplogrecords.md)
</dt> <dt>

[**ReadLogRecord**](readlogrecord.md)
</dt> <dt>

[**ReadNextLogRecord**](readnextlogrecord.md)
</dt> </dl>

 

 





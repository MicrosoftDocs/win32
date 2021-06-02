---
description: The PdhVbOpenLog function opens the specified log file for reading and writing. This function calls PdhOpenLog.
ms.assetid: d9b8d98c-64f2-4319-8ab2-67b776143cf7
title: PdhVbOpenLog function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PdhVbOpenLog
api_type: 
- DllExport
api_location: 
- Pdh.dll
---

# PdhVbOpenLog function

The **PdhVbOpenLog** function opens the specified log file for reading and writing. This function calls [**PdhOpenLog**](/windows/desktop/api/Pdh/nf-pdh-pdhopenloga).

> [!IMPORTANT]
> The function that this topic describes may be altered or unavailable in the future. Instead, Microsoft recommends that you use the functions described in [Performance Counters Functions](performance-counters-functions.md).

Function PdhVbOpenLog( \_ ByVal szLogFileName As LPCTSTR, \_ ByVal dwAccessFlags As DWORD, \_ ByVal lpdwLogType As LPDWORD, \_ ByVal hQuery As PDH\_HQUERY, \_ ByVal dwMaxSize As DWORD, \_ ByVal szUserCaption As LPCSTR, \_ ByRef phLog As PDH\_HLOG \_ ) As DWORD

## Parameters

<dl> <dt>

*szLogFileName* \[in\]
</dt> <dd>

Pointer to a string that specifies the name of the log file to be opened.

If the log file contains SQL data, the format of the name of the log file is **SQL:***DataSourceName***!***LogFileName*. In this case, the value of the *lpdwLogType* parameter is PDH\_LOG\_TYPE\_SQL.

</dd> <dt>

*dwAccessFlags* \[in\]
</dt> <dd>

Type of access to be specified when the log file is opened. This parameter can be one of the following values.



| Value                                                                                                                                                                                   | Meaning                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <span id="PDH_LOG_READ_ACCESS"></span><span id="pdh_log_read_access"></span><dl> <dt>**PDH\_LOG\_READ\_ACCESS**</dt> </dl>       | A log file is opened for a read operation.<br/>            |
| <span id="PDH_LOG_WRITE_ACCESS"></span><span id="pdh_log_write_access"></span><dl> <dt>**PDH\_LOG\_WRITE\_ACCESS**</dt> </dl>    | A new log file is opened for a write operation.<br/>       |
| <span id="PDH_LOG_UPDATE_ACCESS"></span><span id="pdh_log_update_access"></span><dl> <dt>**PDH\_LOG\_UPDATE\_ACCESS**</dt> </dl> | An existing log file is opened for a write operation.<br/> |



 

The value selected from the previous table can be combined using the OR operator with one of the following create access flags.



| Value                                                                                                                                                                                   | Meaning                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="PDH_LOG_CREATE_NEW"></span><span id="pdh_log_create_new"></span><dl> <dt>**PDH\_LOG\_CREATE\_NEW**</dt> </dl>          | A new log file with the specified name is created.<br/>                                                                                                    |
| <span id="PDH_LOG_CREATE_ALWAYS"></span><span id="pdh_log_create_always"></span><dl> <dt>**PDH\_LOG\_CREATE\_ALWAYS**</dt> </dl> | A new log file with the specified name is created and any existing log file with the same name is erased.<br/>                                             |
| <span id="PDH_LOG_OPEN_EXISTING"></span><span id="pdh_log_open_existing"></span><dl> <dt>**PDH\_LOG\_OPEN\_EXISTING**</dt> </dl> | An existing log file with the specified name is opened. If a log file with the specified name does not exist, this is equal to PDH\_LOG\_CREATE\_NEW.<br/> |
| <span id="PDH_LOG_OPEN_ALWAYS"></span><span id="pdh_log_open_always"></span><dl> <dt>**PDH\_LOG\_OPEN\_ALWAYS**</dt> </dl>       | An existing log file with the specified name is opened or a new log file with the specified name is created.<br/>                                          |



 

</dd> <dt>

*lpdwLogType* \[in\]
</dt> <dd>

Pointer to a variable that indicates the type of log file to be opened. This parameter can be one of the following values.



| Value                                                                                                                                                                                      | Meaning                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| <span id="PDH_LOG_TYPE_UNDEFINED"></span><span id="pdh_log_type_undefined"></span><dl> <dt>**PDH\_LOG\_TYPE\_UNDEFINED**</dt> </dl> | Undefined log file format.<br/>                                                                                   |
| <span id="PDH_LOG_TYPE_CSV"></span><span id="pdh_log_type_csv"></span><dl> <dt>**PDH\_LOG\_TYPE\_CSV**</dt> </dl>                   | Text files containing column headers in the first line, and individual data samples in each subsequent line.<br/> |
| <span id="PDH_LOG_TYPE_SQL"></span><span id="pdh_log_type_sql"></span><dl> <dt>**PDH\_LOG\_TYPE\_SQL**</dt> </dl>                   | The data in the log file is in SQL.<br/>                                                                          |
| <span id="PDH_LOG_TYPE_TSV"></span><span id="pdh_log_type_tsv"></span><dl> <dt>**PDH\_LOG\_TYPE\_TSV**</dt> </dl>                   | Same as PDH\_LOG\_TYPE\_CSV.<br/>                                                                                 |
| <span id="PDH_LOG_TYPE_BINARY"></span><span id="pdh_log_type_binary"></span><dl> <dt>**PDH\_LOG\_TYPE\_BINARY**</dt> </dl>          | Binary log file format. Includes circular log files.<br/>                                                         |
| <span id="PDH_LOG_TYPE_PERFMON"></span><span id="pdh_log_type_perfmon"></span><dl> <dt>**PDH\_LOG\_TYPE\_PERFMON**</dt> </dl>       | Perfmon log file format.<br/>                                                                                     |



 

</dd> <dt>

*hQuery* \[in\]
</dt> <dd>

Query handle. This handle is returned by the [**PdhVbOpenQuery**](pdhvbopenquery.md) function.

This parameter can be **NULL** if the log file is to be opened for reading.

</dd> <dt>

*dwMaxSize* \[in\]
</dt> <dd>

Maximum size of the log file, in bytes. This value is used only if the log file is a limited-size or circular log file.

</dd> <dt>

*szUserCaption* \[in\]
</dt> <dd>

Pointer to a string that specifies the user-defined caption of the log file. A log file caption generally describes the contents of the log file. When an existing log file is opened, the value of this parameter is ignored.

</dd> <dt>

*phLog* \[in, ref\]
</dt> <dd>

Pointer to a buffer that receives a handle to the opened log file.

</dd> </dl>

## Return value

If the function succeeds, it returns 0.

If the function fails, the return value is a [system error code](/windows/desktop/Debug/system-error-codes) or a [PDH error code](pdh-error-codes.md). The following are possible values.



| Return code                                                                                                | Description                                                                                            |
|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| <dl> <dt>**PDH\_INSUFFICIENT\_BUFFER**</dt> </dl>   | The requested data is larger than the buffer supplied. Unable to return the requested data.<br/> |
| <dl> <dt>**PDH\_INVALID\_ARGUMENT**</dt> </dl>      | One or more of the string buffers is not the correct size.<br/>                                  |
| <dl> <dt>**PDH\_INVALID\_HANDLE**</dt> </dl>        | The handle is not a valid PDH object.<br/>                                                       |
| <dl> <dt>**PDH\_LOG\_FILE\_OPEN\_ERROR**</dt> </dl> | Unable to open the specified log file.<br/>                                                      |
| <dl> <dt>**PDH\_FILE\_NOT\_FOUND**</dt> </dl>       | Unable to find the specified file.<br/>                                                          |



 

## Remarks

When using this function to write performance data to a log file, a query must first be opened using [**PdhVbOpenQuery**](pdhvbopenquery.md).

There must be a currently opened query, and the desired counters must be added to it, before this function is called.

Note that log files in the Perfmon format can only be opened for reading.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Library<br/>                  | <dl> <dt>Pdh.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Pdh.dll</dt> </dl> |



## See also

<dl> <dt>

[**PdhOpenLog**](/windows/desktop/api/Pdh/nf-pdh-pdhopenloga)
</dt> <dt>

[**PdhVbGetLogFileSize**](pdhvbgetlogfilesize.md)
</dt> <dt>

[**PdhVbUpdateLog**](pdhvbupdatelog.md)
</dt> </dl>

 


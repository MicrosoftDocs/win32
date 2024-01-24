---
description: All Performance Data Helper (PDH) functions return a value of type PDH\_STATUS.
ms.assetid: ea67d798-81db-44ad-b0fb-24e0c3be7388
title: Performance Data Helper Error Codes
ms.topic: article
ms.date: 05/31/2018
---

# Performance Data Helper Error Codes

All Performance Data Helper (PDH) functions return a value of type **PDH\_STATUS**. If the function succeeds, the return value is `ERROR_SUCCESS`. Otherwise, the function returns a [system error code](/windows/desktop/Debug/system-error-codes) or a PDH error code. To retrieve the description text for the error in your application, use the [**FormatMessage**](/windows/desktop/api/winbase/nf-winbase-formatmessage) function as shown in the following example.

```C++
#include <windows.h>
#include <stdio.h>
#include <pdhmsg.h>

void main(void)
{
    HANDLE hPdhLibrary = NULL;
    LPWSTR pMessage = NULL;
    DWORD dwErrorCode = PDH_PLA_ERROR_ALREADY_EXISTS;

    hPdhLibrary = LoadLibrary(L"pdh.dll");
    if (NULL == hPdhLibrary)
    {
        wprintf(L"LoadLibrary failed with %lu\n", GetLastError());
        return;
    }

    if (!FormatMessage(FORMAT_MESSAGE_FROM_HMODULE |
                       FORMAT_MESSAGE_ALLOCATE_BUFFER |
                       FORMAT_MESSAGE_IGNORE_INSERTS,
                       hPdhLibrary,
                       dwErrorCode,
                       0,
                       (LPWSTR)&pMessage,
                       0,
                       NULL))
    {
        wprintf(L"Format message failed with 0x%x\n", GetLastError());
        return;
    }

    wprintf(L"Formatted message: %ls\n", pMessage);
    LocalFree(pMessage);
}
```

For data collection and formatting functions, it is important to remember that the return value of the function indicates the success or error of the function call and not necessarily that of the counter data. Always check the **CStatus** member of the counter value returned to ensure that the data returned is valid before you use it. If the value of the **CStatus** member does not indicate success, do not use the data.

The following table provides a list of error codes that are specific to PDH. These values are defined in the `pdhmsg.h` header file.

| Error code                                                   | Description
|--------------------------------------------------------------|------------
| 0x00000000 (PDH\_CSTATUS\_VALID\_DATA)                       | The returned data is valid.
| 0x00000001 (PDH\_CSTATUS\_NEW\_DATA)                         | The return data value is valid and different from the last sample.
| 0x800007D0 (PDH\_CSTATUS\_NO\_MACHINE)                       | Unable to connect to the specified computer, or the computer is offline.
| 0x800007D1 (PDH\_CSTATUS\_NO\_INSTANCE)                      | The specified instance is not present.
| 0x800007D2 (PDH\_MORE\_DATA)                                 | There is more data to return than would fit in the supplied buffer. Allocate a larger buffer and call the function again.
| 0x800007D3 (PDH\_CSTATUS\_ITEM\_NOT\_VALIDATED)              | The data item has been added to the query but has not been validated nor accessed. No other status information on this data item is available.
| 0x800007D4 (PDH\_RETRY)                                      | The selected operation should be retried.
| 0x800007D5 (PDH\_NO\_DATA)                                   | No data to return.
| 0x800007D6 (PDH\_CALC\_NEGATIVE\_DENOMINATOR)                | A counter with a negative denominator value was detected.
| 0x800007D7 (PDH\_CALC\_NEGATIVE\_TIMEBASE)                   | A counter with a negative time base value was detected.
| 0x800007D8 (PDH\_CALC\_NEGATIVE\_VALUE)                      | A counter with a negative value was detected.
| 0x800007D9 (PDH\_DIALOG\_CANCELLED)                          | The user canceled the dialog box.
| 0x800007DA (PDH\_END\_OF\_LOG\_FILE)                         | The end of the log file was reached.
| 0x800007DB (PDH\_ASYNC\_QUERY\_TIMEOUT)                      | A time-out occurred while waiting for the asynchronous counter collection thread to end.
| 0x800007DC (PDH\_CANNOT\_SET\_DEFAULT\_REALTIME\_DATASOURCE) | Cannot change set default real-time data source. There are real-time query sessions collecting counter data.
| 0xC0000BB8 (PDH\_CSTATUS\_NO\_OBJECT)                        | The specified object is not found on the system.
| 0xC0000BB9 (PDH\_CSTATUS\_NO\_COUNTER)                       | The specified counter could not be found.
| 0xC0000BBA (PDH\_CSTATUS\_INVALID\_DATA)                     | The returned data is not valid.
| 0xC0000BBB (PDH\_MEMORY\_ALLOCATION\_FAILURE)                | A PDH function could not allocate enough temporary memory to complete the operation. Close some applications or extend the page file and retry the function.
| 0xC0000BBC (PDH\_INVALID\_HANDLE)                            | The handle is not a valid PDH object.
| 0xC0000BBD (PDH\_INVALID\_ARGUMENT)                          | A required argument is missing or incorrect.
| 0xC0000BBE (PDH\_FUNCTION\_NOT\_FOUND)                       | Unable to find the specified function.
| 0xC0000BBF (PDH\_CSTATUS\_NO\_COUNTERNAME)                   | No counter was specified.
| 0xC0000BC0 (PDH\_CSTATUS\_BAD\_COUNTERNAME)                  | Unable to parse the counter path. Check the format and syntax of the specified path.
| 0xC0000BC1 (PDH\_INVALID\_BUFFER)                            | The buffer passed by the caller is not valid.
| 0xC0000BC2 (PDH\_INSUFFICIENT\_BUFFER)                       | The requested data is larger than the buffer supplied. Unable to return the requested data.
| 0xC0000BC3 (PDH\_CANNOT\_CONNECT\_MACHINE)                   | Unable to connect to the requested computer.
| 0xC0000BC4 (PDH\_INVALID\_PATH)                              | The specified counter path could not be interpreted.
| 0xC0000BC5 (PDH\_INVALID\_INSTANCE)                          | The instance name could not be read from the specified counter path.
| 0xC0000BC6 (PDH\_INVALID\_DATA)                              | The data is not valid.
| 0xC0000BC7 (PDH\_NO\_DIALOG\_DATA)                           | The dialog box data block was missing or not valid.
| 0xC0000BC8 (PDH\_CANNOT\_READ\_NAME\_STRINGS)                | Unable to read the counter and/or help text from the specified computer.
| 0xC0000BC9 (PDH\_LOG\_FILE\_CREATE\_ERROR)                   | Unable to create the specified log file.
| 0xC0000BCA (PDH\_LOG\_FILE\_OPEN\_ERROR)                     | Unable to open the specified log file.
| 0xC0000BCB (PDH\_LOG\_TYPE\_NOT\_FOUND)                      | The specified log file type has not been installed on this system.
| 0xC0000BCC (PDH\_NO\_MORE\_DATA)                             | No more data is available.
| 0xC0000BCD (PDH\_ENTRY\_NOT\_IN\_LOG\_FILE)                  | The specified record was not found in the log file.
| 0xC0000BCE (PDH\_DATA\_SOURCE\_IS\_LOG\_FILE)                | The specified data source is a log file.
| 0xC0000BCF (PDH\_DATA\_SOURCE\_IS\_REAL\_TIME)               | The specified data source is the current activity.
| 0xC0000BD0 (PDH\_UNABLE\_READ\_LOG\_HEADER)                  | The log file header could not be read.
| 0xC0000BD1 (PDH\_FILE\_NOT\_FOUND)                           | Unable to find the specified file.
| 0xC0000BD2 (PDH\_FILE\_ALREADY\_EXISTS)                      | There is already a file with the specified file name.
| 0xC0000BD3 (PDH\_NOT\_IMPLEMENTED)                           | The function referenced has not been implemented.
| 0xC0000BD4 (PDH\_STRING\_NOT\_FOUND)                         | Unable to find the specified string in the list of performance name and help text strings.
| 0x80000BD5 (PDH\_UNABLE\_MAP\_NAME\_FILES)                   | Unable to map to the performance counter name data files. The data will be read from the registry and stored locally.
| 0xC0000BD6 (PDH\_UNKNOWN\_LOG\_FORMAT)                       | The format of the specified log file is not recognized by the PDH DLL.
| 0xC0000BD7 (PDH\_UNKNOWN\_LOGSVC\_COMMAND)                   | The specified Log Service command value is not recognized.
| 0xC0000BD8 (PDH\_LOGSVC\_QUERY\_NOT\_FOUND)                  | The specified query from the Log Service could not be found or could not be opened.
| 0xC0000BD9 (PDH\_LOGSVC\_NOT\_OPENED)                        | The Performance Data Log Service key could not be opened. This may be due to insufficient privilege or because the service has not been installed.
| 0xC0000BDA (PDH\_WBEM\_ERROR)                                | An error occurred while accessing the WBEM data store.
| 0xC0000BDB (PDH\_ACCESS\_DENIED)                             | Unable to access the desired computer or service. Check the permissions and authentication of the log service or the interactive user session against those on the computer or service being monitored.
| 0xC0000BDC (PDH\_LOG\_FILE\_TOO\_SMALL)                      | The maximum log file size specified is too small to log the selected counters. No data will be recorded in this log file. Specify a smaller set of counters to log or a larger file size and retry this call.
| 0xC0000BDD (PDH\_INVALID\_DATASOURCE)                        | Cannot connect to ODBC DataSource Name.
| 0xC0000BDE (PDH\_INVALID\_SQLDB)                             | SQL Database does not contain a valid set of tables for Perfmon.
| 0xC0000BDF (PDH\_NO\_COUNTERS)                               | No counters were found for this Perfmon SQL Log Set.
| 0xC0000BE0 (PDH\_SQL\_ALLOC\_FAILED)                         | Call to SQLAllocStmt failed with %1.
| 0xC0000BE1 (PDH\_SQL\_ALLOCCON\_FAILED)                      | Call to SQLAllocConnect failed with %1.
| 0xC0000BE2 (PDH\_SQL\_EXEC\_DIRECT\_FAILED)                  | Call to SQLExecDirect failed with %1.
| 0xC0000BE3 (PDH\_SQL\_FETCH\_FAILED)                         | Call to SQLFetch failed with %1.
| 0xC0000BE4 (PDH\_SQL\_ROWCOUNT\_FAILED)                      | Call to SQLRowCount failed with %1.
| 0xC0000BE5 (PDH\_SQL\_MORE\_RESULTS\_FAILED)                 | Call to SQLMoreResults failed with %1.
| 0xC0000BE6 (PDH\_SQL\_CONNECT\_FAILED)                       | Call to SQLConnect failed with %1.
| 0xC0000BE7 (PDH\_SQL\_BIND\_FAILED)                          | Call to SQLBindCol failed with %1.
| 0xC0000BE8 (PDH\_CANNOT\_CONNECT\_WMI\_SERVER)               | Unable to connect to the WMI server on requested computer.
| 0xC0000BE9 (PDH\_PLA\_COLLECTION\_ALREADY\_RUNNING)          | Collection "%1!s!" is already running.
| 0xC0000BEA (PDH\_PLA\_ERROR\_SCHEDULE\_OVERLAP)              | The specified start time is after the end time.
| 0xC0000BEB (PDH\_PLA\_COLLECTION\_NOT\_FOUND)                | Collection "%1!s!" does not exist.
| 0xC0000BEC (PDH\_PLA\_ERROR\_SCHEDULE\_ELAPSED)              | The specified end time has already elapsed.
| 0xC0000BED (PDH\_PLA\_ERROR\_NOSTART)                        | Collection "%1!s!" did not start; check the application event log for any errors.
| 0xC0000BEE (PDH\_PLA\_ERROR\_ALREADY\_EXISTS)                | Collection "%1!s!" already exists.
| 0xC0000BEF (PDH\_PLA\_ERROR\_TYPE\_MISMATCH)                 | There is a mismatch in the settings type.
| 0xC0000BF0 (PDH\_PLA\_ERROR\_FILEPATH)                       | The information specified does not resolve to a valid path name.
| 0xC0000BF1 (PDH\_PLA\_SERVICE\_ERROR)                        | The "Performance Logs & Alerts" service did not respond.
| 0xC0000BF2 (PDH\_PLA\_VALIDATION\_ERROR)                     | The information passed is not valid.
| 0x80000BF3 (PDH\_PLA\_VALIDATION\_WARNING)                   | The information passed is not valid.
| 0xC0000BF4 (PDH\_PLA\_ERROR\_NAME\_TOO\_LONG)                | The name supplied is too long.
| 0xC0000BF5 (PDH\_INVALID\_SQL\_LOG\_FORMAT)                  | SQL log format is incorrect. Correct format is `SQL:<DSN-name>!<LogSet-Name>`.
| 0xC0000BF6 (PDH\_COUNTER\_ALREADY\_IN\_QUERY)                | Performance counter in [**PdhAddCounter**](/windows/desktop/api/Pdh/nf-pdh-pdhaddcountera) call has already been added in the performance query. This counter is ignored.
| 0xC0000BF7 (PDH\_BINARY\_LOG\_CORRUPT)                       | Unable to read counter information and data from input binary log files.
| 0xC0000BF8 (PDH\_LOG\_SAMPLE\_TOO\_SMALL)                    | At least one of the input binary log files contain fewer than two data samples.
| 0xC0000BF9 (PDH\_OS\_LATER\_VERSION)                         | The version of the operating system on the computer named %1 is later than that on the local computer. This operation is not available from the local computer.
| 0xC0000BFA (PDH\_OS\_EARLIER\_VERSION)                       | %1 supports %2 or later. Check the operating system version on the computer named %3.
| 0xC0000BFB (PDH\_INCORRECT\_APPEND\_TIME)                    | The output file must contain earlier data than the file to be appended.
| 0xC0000BFC (PDH\_UNMATCHED\_APPEND\_COUNTER)                 | Both files must have identical counters in order to append.
| 0xC0000BFD (PDH\_SQL\_ALTER\_DETAIL\_FAILED)                 | Cannot alter CounterDetail table layout in SQL database.
| 0xC0000BFE (PDH\_QUERY\_PERF\_DATA\_TIMEOUT)                 | System is busy. A time-out occurred when collecting counter data. Please retry later or increase the **CollectTime** registry value.

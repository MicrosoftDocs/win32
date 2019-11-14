---
title: Error Logging in Windows Server 2003 SP1
description: Error Logging in Windows Server 2003 SP1
ms.assetid: 8c7fcc66-5446-4e25-8e6d-1a9260c55e36
keywords:
- Error Logging in Windows Server 2003 with Service Pack 1 (SP1)
ms.topic: article
ms.date: 05/31/2018
---

# Error Logging in Windows Server 2003 SP1

## Addition of W3C Style Headers

Starting with Windows Server 2003 with Service Pack 1 (SP1), the HTTP Server API error log includes W3C style headers allowing log files to be parsed using standard log parsers. The template shown below lists all the fields that can be logged in the http error log file.

``` syntax
#Software: <Name of the HTTP Server>
#Version: 1.0 <Log format version>
#Date: <Log file creation date and time>
#Fields: <date time s-computername c-ip c-port s-ip s-port cs-version
         cs-method cs-uri cs(User-Agent) cs(Cookie) cs(referrer) 
         cs-host sc-status sc-bytes cs-bytes time-taken s-siteid  
         s- reason s-queuename <header names of fields logged>

```

## Logging Additional Fields

The HTTP error log has been extended to include nine more fields to log data about failures that occur. The new error fields are listed below:

-   Server Computer Name \[S-COMPUTERNAME\]
-   User Agent \[CS(USER\_AGENT)\]
-   Cookie \[CS(COOKIE)\]
-   referrer \[CS(referrer)\]
-   Host Name \[CS-HOST\]
-   Bytes received by the server \[SC-BYTES\]
-   Bytes received and processed by the server \[CS-BYTES\]
-   Time Taken to process the request \[TIME-TAKEN\]
-   Queue-Name (Reserved for IIS) \[S-QUEUENAME\]

## Selecting Fileds to Log in the HTTP Error Log File

The **ErrorLoggingFields** registry key has been added to control the fields logged into the HTTP error log. This registry values is located under an HTTP\\Parameters key located at:

```
HKEY_LOCAL_MACHINE
   System
      CurrentControlSet
      Services
         HTTP
            Parameters
```

The **ErrorLoggingFields** registry value is a DWORD value that contains bit values for each of the fields that can be logged. To enable logging of a specific field, set its corresponding bit value to 1 and restart the HTTP service. To disable logging, set the bit value to 0. To configure multiple fields, use a bitwise OR of the individual values. For example, to turn on the Cookie and Referrer logging fields, the value should be 0x00020000 \| 0x00040000 = 0x00060000. If the **ErrorLoggingFields** registry key is absent, the default fields are logged. The **ErrorLoggingFields** value to log the default fields is 0x7c884c7. To enable logging for all the fields shown in the table below, set the value to 0x7dff4e7.

The error logging fields are listed in the following table:



| Log field            | Logged by default | Bit value  |
|----------------------|-------------------|------------|
| Date                 | Yes               | 0x00000001 |
| Time                 | Yes               | 0x00000002 |
| Server Computer Name | No                | 0x00000020 |
| Client IP Address    | Yes               | 0x00000004 |
| Client Port          | Yes               | 0x00400000 |
| Server IP Address    | Yes               | 0x00000040 |
| Server Port          | Yes               | 0x00008000 |
| Protocol Version     | Yes               | 0x00080000 |
| Method               | Yes               | 0x00000080 |
| URI                  | Yes               | 0x00800000 |
| User Agent           | No                | 0x00010000 |
| Cookie               | No                | 0x00020000 |
| referrer             | No                | 0x00040000 |
| Host                 | No                | 0x00100000 |
| Protocol Status      | Yes               | 0x00000400 |
| SC-Bytes             | No                | 0x00001000 |
| CS-Bytes             | No                | 0x00002000 |
| Time Taken           | No                | 0x00004000 |
| SiteId               | Yes               | 0x01000000 |
| Reason Phrase        | Yes               | 0x02000000 |
| Queue Name           | No                | 0x04000000 |
| Stream Id            | No                | 0x???????? |



 

## Time and Date Rollover

By default, a new HTTP error log file is created (termed file rollover) when the current log file reaches a specified size. Starting with Windows Server 2003 with SP1, new error log files can be created based on date and time. Time and date rollover are controlled by two new registry values: **ErrorLoggingRolloverType** and **ErrorLoggingLocaltimeRollover**. To enable time and date rollover, these registry values must be added to the registry. The Http service must be restarted when these keys are added to the registry. The log file rollover registry keys are created under the following key:

```
HKEY_LOCAL_MACHINE
   System
      CurrentControlSet
         Services
            HTTP
               Parameters
```

The **ErrorLoggingRolloverType** registry key indicates the type of rollover desired and is by default set to size based rollover. Rollover can also be set to occur on a daily, weekly, monthly, or hourly basis. When file rollover is based on time, an **ErrorLoggingLocaltimeRollover** value of 0 indicates that the rollover time is expressed in GMT, and a value of 1 indicates that the rollover time is expressed in local time. The **ErrorLoggingRolloverType** key can take a value from 0 to 4 as listed in the following table.



| Rollover type value | Description                                                                                                                             |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| 0                   | Size based rollover. Log files are rolled over when the file reaches the size defined in the **ErrorLogFileTruncateSize** registry key. |
| 1                   | Log file rollover occurs daily.                                                                                                         |
| 2                   | Log file rollover occurs weekly.                                                                                                        |
| 3                   | Log file rollover occurs monthly.                                                                                                       |
| 4                   | Log file rollover occurs hourly.                                                                                                        |



 

The naming conventions for files that store the error logs are different for size, date, and time based rollover. The following table lists the naming conventions for Http log files.



| Tollover type | Log file name  | Description                                                                                                                         |
|---------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Size          | HTTPERRn.LOG   | The log file is recycled when it reaches a specific size. n is the file number and is incremented when the log file is rolled over. |
| Daily         | htYYMMDD.log   | The log file is recycled daily.                                                                                                     |
| Weekly        | htYYMMww.log   | The log file is recycled weekly, where ww is the week of the month.                                                                 |
| Monthly       | htYYMM.log     | The log file is recycled every month.                                                                                               |
| Hourly        | htYYMMDDhh.log | The log file is recycled hourly, where hh is the hour of the day expressed in 0-24 hour notation.                                   |



 

 

 





---
title: IIS Logging
description: IIS logging is one type of server side logging that can be enabled on a URL group.
ms.assetid: 2adfee73-090a-4bc1-827e-4b0e8075e2b3
ms.topic: article
ms.date: 05/31/2018
---

# IIS Logging

IIS logging is one type of server side logging that can be enabled on a URL group. The IIS log file format is a fixed ASCII text-based format that cannot be customized. The IIS log file contains the HTTP Server API kernel-mode cache hits. This type of logging can be enabled on a URL group only; it cannot be used on the server session.

The IIS log file format records the following data. The data in the table is in the order of occurrence in the log file.



| Field                | Description                                                                                                                                                                       |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Client IP address    | The IP address of the client that made the request.                                                                                                                               |
| User name            | The name of the authenticated user that accessed the server. Anonymous users are indicated by a hyphen. The best practice is for the application always to provide the user name. |
| Date                 | The date on which the activity occurred.                                                                                                                                          |
| Time                 | The local time at which the activity occurred.                                                                                                                                    |
| Service and instance | The Internet service name and instance number that was running on the client.                                                                                                     |
| Server name          | The name of the server on which the log file entry was generated.                                                                                                                 |
| Server IP address    | The IP address of the server on which the log file entry was generated.                                                                                                           |
| Time taken           | The length of time that the action took, in milliseconds.                                                                                                                         |
| Client bytes sent    | The number of bytes sent by the client.                                                                                                                                           |
| Server bytes sent    | The number of bytes sent by the server.                                                                                                                                           |
| Service status code  | A value of 200 indicates that the request was fulfilled successfully.                                                                                                             |
| Windows status code  | A value of 0 (zero) indicates that the request was fulfilled successfully.                                                                                                        |
| Request type         | The request verb.                                                                                                                                                                 |
| Target of operation  | The target of the verb, for example, Default.htm.                                                                                                                                 |
| Parameters           | The parameters that are passed to a script.                                                                                                                                        |



 

Not all fields will contain information. For fields for which there is no information, a hyphen (-) appears as a placeholder. If a field contains a nonprintable character, the HTTP Server API replaces it with a plus sign (+) to preserve the log file format. This typically occurs with virus attacks, when, for example, a malicious user sends carriage returns and line feeds that, if not replaced with the plus sign (+), would break the log file format. Fields are separated by commas, making the format easier to read than the other ASCII formats, which use spaces for separators. The time is recorded as local time. The time taken is recorded in milliseconds. For more information about the time taken field, see the [W3C Logging](w3c-logging.md) topic.

The following example shows an NCSA Common log file entry.

``` syntax
192.168.114.201, -, 03/20/05, 7:55:20, W3SVC2, SERVER, 
172.21.13.45, 4502, 163, 3223, 200, 0, GET, /DeptLogo.gif, -,
```

 

 





---
title: NCSA Logging
description: NCSA extended logging is one type of server side logging that can be enabled on a URL group.
ms.assetid: 14a2492a-3bcf-46f3-a3a5-1ea578516865
ms.topic: article
ms.date: 05/31/2018
---

# NCSA Logging

NCSA extended logging is one type of server side logging that can be enabled on a URL group. The NCSA Common log file format is a fixed ASCII text-based format that cannot be customized. The NCSA log file contains the HTTP Server API kernel-mode cache hits. This type of logging can be enabled on a URL group only; it cannot be used on the server session.

The NCSA Common log file format records the following data. The data in the table is in the order of occurrence in the log file.



| Field                                            | Description                                                                                                                                                                       |
|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Remote host address                              | The IP address of the client that made the request.                                                                                                                               |
| Remote log name                                  | Not used. This value is always a hyphen.                                                                                                                                          |
| User name                                        | The name of the authenticated user that accessed the server. Anonymous users are indicated by a hyphen. The best practice is for the application always to provide the user name. |
| Date, time, and Greenwich mean time (GMT) offset | The local date and time at which the activity occurred. The offset from Greenwich mean time is also indicated.                                                                    |
| Request and Protocol version                     | The HTTP protocol version that the client used.                                                                                                                                   |
| Service status code                              | The HTTP status code. (A value of 200 indicates that the request completed successfully.)                                                                                         |
| Bytes sent                                       | The number of bytes sent by the server.                                                                                                                                           |



 

Not all fields will contain information. For fields for which there is no information, a hyphen (-) appears as a placeholder. If a field contains a nonprintable character, the HTTP Server API replaces it with a plus sign (+) to preserve the log file format. This typically occurs with virus attacks, when, for example, a malicious user sends carriage returns and line feeds that, if not replaced with the plus sign (+), would break the log file format. Fields are separated by spaces, and the time is recorded as local time with the GMT offset.

The following example shows an NCSA Common log file entry, as viewed in a text editor.

``` syntax
172.21.13.45 - Microsoft\JohnDoe [07/Apr/2004:17:39:04 -0800] 
"GET /scripts/iisadmin/ism.dll?http/serv HTTP/1.0" 200 3401
```

The IP address of the client is 172.21.13.45, and the user name is Microsoft\\JohnDoe. The log was recorded on April 7, 2005 at 17:39:04 local time with a Greenwich offset of 8 hours. The request verb and protocol version were "GET /scripts/iisadmin/ism.dll?http/serv HTTP/1.0". The status codes was 200 OK, and the number of bytes sent by the client was 3401.

 

 





---
title: HTTP Server API
description: The HTTP Server API enables applications to communicate over HTTP without using Microsoft Internet Information Server (IIS).
ms.assetid: ef18716c-7511-4c8a-99bc-28369c3e46f4
keywords:
- HTTP Server API
- HTTP Server API, start page
ms.topic: article
ms.date: 05/31/2018
---

# HTTP Server API

## Purpose

The HTTP Server API enables applications to communicate over HTTP without using Microsoft Internet Information Server (IIS). Applications can register to receive HTTP requests for particular URLs, receive HTTP requests, and send HTTP responses. The HTTP Server API includes SSL support so that applications can exchange data over secure HTTP connections without IIS. It is also designed to work with I/O completion ports.

## Developer audience

This API is designed for use by C/C++ programmers.

## Run-time requirements

The HTTP Server API is supported on Windows Server 2003 operating systems and on Windows XP with Service Pack 2 (SP2). Be aware that Microsoft IIS 5 running on Windows XP with SP2 is not able to share port 80 with other HTTP applications running simultaneously.

## In this section



| Topic                                                                           | Description                                                                                             |
|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [About HTTP Server API](about-http-server-api.md)<br/>                   | General information about HTTP.<br/>                                                              |
| [Using HTTP Server API](using-http-server-api.md)<br/>                   | Procedural guide for using HTTP.<br/>                                                             |
| [HTTP Server API Reference](http-server-api-reference.md)<br/>           | Documentation of specific functions, structures, and enumeration types available in HTTP.<br/>    |
| [HTTP Server Sample Application](http-server-sample-application.md)<br/> | A sample application that shows how to use the HTTP Server API to perform server-side tasks.<br/> |



 

## Related topics

<dl> <dt>

[Windows HTTP Services (WinHTTP)](/windows/desktop/WinHttp/winhttp-start-page)
</dt> </dl>

 


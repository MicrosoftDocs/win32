---
Description: Most programmatic fax management requires you to connect to the fax server.
ms.assetid: aa3cd5cf-fff5-453b-9574-7ef617239da6
title: Connecting to the Fax Server
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Connecting to the Fax Server

Most programmatic fax management requires you to connect to the fax server. You can either specify the full path and name of a remote server, or use an empty string to connect to the local fax server. Following are examples of the syntax you need to connect to the server.

## Visual Basic and VBScript


```
objFaxServer.Connect "computername"
```



or, for the local server


```
objFaxServer.Connect ""
```



## JScript


```
objFaxServer.Connect ""
```



## C++


```
sipFaxServer->Connect("computername");
```



or, for the local server


```
sipFaxServer->Connect("");
```



## Remarks

Using the fax extended Component Object Model (COM) API you can connect to a remote fax server running on a Windows Server 2003 computer. However, you cannot connect to a Windows 2000 fax.

There are some limitations while working with a remote fax connection, as follow:

-   In Windows Server 2003, the fax printer must be shared to support a remote connection.
-   If you want to submit faxes remotely to a Windows Server 2003 fax you must have a fax printer connection to that server.

 

 




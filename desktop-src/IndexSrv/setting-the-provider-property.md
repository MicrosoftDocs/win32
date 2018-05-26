---
title: Setting the Provider Property
description: Setting the Provider Property
ms.assetid: fb991003-94c7-4cd5-acc1-74a9acad0e5d
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Setting the Provider Property

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

To use the ActiveX Data Objects (ADO) API, a program or script needs to open a connection to the [OLE DB Provider for Indexing Service](ole-db-provider-for-indexing-service.md) and set the **Provider** property of the ADO **Connection** object to the string "MSIDXS". The **Provider** property can also be set by the contents of the **ConnectionString** property or the *ConnectionString* parameter of the **Open** method. Alternatively, you can generate a **Recordset** object and ensure that the associated **Open** method includes a *ConnectionString* parameter containing the string "PROVIDER=MSIDXS;".

The following is an example of the minimal Microsoft Visual Basic Scripting Edition (VBScript) code needed to generate an ADO **Recordset** object.


```
Set rstMain = Server.CreateObject("ADODB.Recordset")
RstMain.Open "SELECT DocAuthor, DocTitle, FileName 
                FROM SCOPE() WHERE size > 50000",
                "PROVIDER=MSIDXS;"
```



The following is an example of the ADO code that creates a **Connection** object.


```
Set Conn = Server.CreateObject ("ADODB.Connection")
Conn.ConnectionString = "provider=msidxs;"
Conn.Open 
```



After executing the preceding example, you can create a **Command** object, associate it to the active connection you opened, set the **CommandText** property of the **Command** object to the desired SQL query string, and create the associated **Recordset** object to retrieve the results of your query.

 

 





---
Description: Before you can use a file log, you must call SetupInitializeFileLog to open or create it. When you call this function, you can specify flags to create or overwrite a file log, open the system log, or open a file log as read-only.
ms.assetid: 7ab133f6-2088-4bca-bf24-d3dcb29376a1
title: Using the File Log
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using the File Log

Before you can use a file log, you must call [**SetupInitializeFileLog**](/windows/win32/Setupapi/nf-setupapi-setupinitializefileloga?branch=master) to open or create it. When you call this function, you can specify flags to create or overwrite a file log, open the system log, or open a file log as read-only.

After [**SetupInitializeFileLog**](/windows/win32/Setupapi/nf-setupapi-setupinitializefileloga?branch=master) returns a handle to a file log, you can add an entry by calling [**SetupLogFile**](/windows/win32/Setupapi/nf-setupapi-setuplogfilea?branch=master), delete an entry by calling [**SetupRemoveFileLogEntry**](/windows/win32/Setupapi/nf-setupapi-setupremovefilelogentrya?branch=master), or retrieve information about a particular file in a file log by calling [**SetupQueryFileLog**](/windows/win32/Setupapi/nf-setupapi-setupqueryfileloga?branch=master).

When the file log is no longer needed, [**SetupTerminateFileLog**](/windows/win32/Setupapi/nf-setupapi-setupterminatefilelog?branch=master) should be called to release the resources allocated during the call to [**SetupInitializeFileLog**](/windows/win32/Setupapi/nf-setupapi-setupinitializefileloga?branch=master).

 

 




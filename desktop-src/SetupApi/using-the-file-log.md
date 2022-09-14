---
description: Before you can use a file log, you must call SetupInitializeFileLog to open or create it. When you call this function, you can specify flags to create or overwrite a file log, open the system log, or open a file log as read-only.
ms.assetid: 7ab133f6-2088-4bca-bf24-d3dcb29376a1
title: Using the File Log
ms.topic: article
ms.date: 05/31/2018
---

# Using the File Log

Before you can use a file log, you must call [**SetupInitializeFileLog**](/windows/desktop/api/Setupapi/nf-setupapi-setupinitializefileloga) to open or create it. When you call this function, you can specify flags to create or overwrite a file log, open the system log, or open a file log as read-only.

After [**SetupInitializeFileLog**](/windows/desktop/api/Setupapi/nf-setupapi-setupinitializefileloga) returns a handle to a file log, you can add an entry by calling [**SetupLogFile**](/windows/desktop/api/Setupapi/nf-setupapi-setuplogfilea), delete an entry by calling [**SetupRemoveFileLogEntry**](/windows/desktop/api/Setupapi/nf-setupapi-setupremovefilelogentrya), or retrieve information about a particular file in a file log by calling [**SetupQueryFileLog**](/windows/desktop/api/Setupapi/nf-setupapi-setupqueryfileloga).

When the file log is no longer needed, [**SetupTerminateFileLog**](/windows/desktop/api/Setupapi/nf-setupapi-setupterminatefilelog) should be called to release the resources allocated during the call to [**SetupInitializeFileLog**](/windows/desktop/api/Setupapi/nf-setupapi-setupinitializefileloga).

 

 




---
Description: 'Before you can use a file log, you must call SetupInitializeFileLog to open or create it. When you call this function, you can specify flags to create or overwrite a file log, open the system log, or open a file log as read-only.'
ms.assetid: '7ab133f6-2088-4bca-bf24-d3dcb29376a1'
title: Using the File Log
---

# Using the File Log

Before you can use a file log, you must call [**SetupInitializeFileLog**](setupinitializefilelog.md) to open or create it. When you call this function, you can specify flags to create or overwrite a file log, open the system log, or open a file log as read-only.

After [**SetupInitializeFileLog**](setupinitializefilelog.md) returns a handle to a file log, you can add an entry by calling [**SetupLogFile**](setuplogfile.md), delete an entry by calling [**SetupRemoveFileLogEntry**](setupremovefilelogentry.md), or retrieve information about a particular file in a file log by calling [**SetupQueryFileLog**](setupqueryfilelog.md).

When the file log is no longer needed, [**SetupTerminateFileLog**](setupterminatefilelog.md) should be called to release the resources allocated during the call to [**SetupInitializeFileLog**](setupinitializefilelog.md).

 

 




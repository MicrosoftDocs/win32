---
Description: 'The \_MSIExecute Mutex is set only while processing the InstallExecuteSequence table, AdminExecuteSequence table, or AdvtExecuteSequence table.'
ms.assetid: '2186422d-ccb2-4f7e-8c6d-326c00e0d9a9'
title: '\_MSIExecute Mutex'
---

# \_MSIExecute Mutex

The \_MSIExecute Mutex is set only while processing the [InstallExecuteSequence table](installexecutesequence-table.md), [AdminExecuteSequence table](adminexecutesequence-table.md), or [AdvtExecuteSequence table](advtexecutesequence-table.md).

Because two installations cannot be run in the same process, an attempt to call the installer's application programming interface (API) returns ERROR\_INSTALL\_ALREADY\_RUNNING (1618) in two cases:

-   While the \_MSIExecute Mutex is set.
-   While the current process is processing the [InstallUISequence table](installuisequence-table.md) or [AdminUISequence table](adminuisequence-table.md).

See the [Event Logging](event-logging.md) messages for information about what application is being installed.

In cases where it is impractical to return an ERROR\_INSTALL\_ALREADY\_RUNNING error, you can retrieve the current status of the Windows Installer service before attempting to start the installation by using the [**QueryServiceStatusEx**](https://msdn.microsoft.com/library/windows/desktop/ms684941) function. The Windows Installer service is currently running if the value of the **dwControlsAccepted** member of the returned [**SERVICE\_STATUS\_PROCESS**](https://msdn.microsoft.com/library/windows/desktop/ms685992) structure is **SERVICE\_ACCEPT\_SHUTDOWN**.

**Windows Installer 2.0:** Not supported. The use of the [**QueryServiceStatusEx**](https://msdn.microsoft.com/library/windows/desktop/ms684941) function to retrieve the current status of the Windows Installer service requires Windows Installer version 3.0 or greater.

 

 




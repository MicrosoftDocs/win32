---
description: HKLM\\SOFTWARE\\Microsoft\\MSSQLServer\\Client.
ms.assetid: d6eb774b-d7ae-4f51-9947-90fb176e9acf
title: ConnectTo
ms.topic: article
ms.date: 05/31/2018
---

# ConnectTo

**HKLM\\SOFTWARE\\Microsoft\\MSSQLServer\\Client**

## Description

The **ConnectTo** subkey stores connection information for Windows-based clients that connect to instances of the Microsoft SQL Server database engine. Registry entries in this subkey are of data type REG\_SZ, and their values specify the Net-Library to use for connecting to the instance, as well as any network-specific parameters.

The connection information stored in this subkey is read by the OLE DB Provider for SQL Server, the SQL Server ODBC driver, or the SQL Server DB-Library dynamic-link library (DLL).

## Change Method

You should not modify entries in this subkey by using the registry editor. Use the SQL Server Client Network Utility to configure server name and connection information. See SQL Server Client Network Utility Help for further instructions.

## Notes

-   The **ConnectTo** subkey is used by the OLE DB Provider for SQL Server, the SQL Server ODBC Driver, and the SQL Server DB-Library DLL. Entries in this subkey identify which Net-Library these data access application programming interface (API) components call.
-   Net-Libraries are SQL Server components that shield the data access API components from the details of using different Interprocess Communication (IPC) methods to communicate with an instancess of the SQL Server database engine.
-   Improperly updating the **ConnectTo** subkey might prevent applications from successfully connecting to an instance of the SQL Server database engine.

 

 




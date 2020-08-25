---
title: Centralized Binary Logging
description: Centralized binary logging is a type of server side logging that can be enabled on the server session.
ms.assetid: 957a7bc4-9db3-4153-b0a9-e53b3cc514c6
ms.topic: article
ms.date: 05/31/2018
---

# Centralized Binary Logging

Centralized binary logging is a type of server side logging that can be enabled on the server session. Centralized binary logging functions as a centralized form of logging for all the URL groups created under the server session, and allows all the URL groups under the server session to send binary, unformatted log data to a single log file. This type of logging can be enabled on the server session only; it cannot be enabled on the URL group.

## When to use Centralized Binary Logging

When the server session has numerous URL groups under it, the process of creating hundreds of formatted log files for individual URL groups and writing the log data to a disk can quickly consume valuable CPU and memory resources, thereby creating performance and scalability issues. Centralized binary logging minimizes the amount of system resources that are used for logging, while at the same time providing detailed log data for organizations that require it.

Centralized binary logging is a server session property that, when enabled, configures logging for all of the URL groups under the server session. When centralized binary logging is enabled, data cannot be recorded or formatted for individual URL groups. The centralized binary logging log file has an Internet binary log (.ibl) file name extension. This file name extension ensures that text utilities do not try to open and read the central binary logging log file.

## Extracting Data from the Centralized Binary Log File

The following steps are performed to extract data from a raw log file:

-   Create a tool that locates and extracts the data that you want from the raw file and converts the data into formatted text. You can view a header file and log file format descriptions in the IIS 6.0 Software Development Kit on MSDN.
-   Use the Log Parser tool to extract data from the raw file. The Log Parser tool and its accompanying user documentation are included in the IIS 6.0 Resource Kit Tools.

## Centralized Binary Logging File Format

The raw centralized binary logging log file is made up of fixed-length records or index records that contain string identifiers. The index records appear because, in an effort to record as much information as possible, variable-length string fields are replaced by numeric identifiers — indexes — that map the variable-length string to the logged identifier.

The raw log file is not human-readable, and it cannot be read using most available log analyzers. To extract data from a raw log file, you can create a tool that locates and extracts the data and then converts it into formatted text.

For more information, see [Centralized Binary Logging](/previous-versions/windows/it-pro/windows-server-2003/cc758733(v=ws.10)) on Microsoft TechNet.

 

 
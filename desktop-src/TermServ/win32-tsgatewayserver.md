---
title: Win32\_TSGatewayServer class
description: Used for Remote Desktop Gateway (RD Gateway) server-specific operations.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ae24b7ff-2c26-43a5-ac11-52f83225f4ee
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- Win32_TSGatewayServer class Remote Desktop Services
- Win32_TSGatewayServer class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_TSGatewayServer
api_location:
- AagWmi.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Win32\_TSGatewayServer class

Used for Remote Desktop Gateway (RD Gateway) server-specific operations.

## Syntax

``` syntax
[singleton, dynamic, provider("AAGProvider"), AMENDMENT]
class Win32_TSGatewayServer
{
};
```

## Members

The **Win32\_TSGatewayServer** class has these types of members:

-   [Methods](#methods)

### Methods

The **Win32\_TSGatewayServer** class has these methods.



| Method                                                                                   | Description                                                                                                                    |
|:-----------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------|
| [**CreateSelfSignedCertificate**](createselfsignedcertificate-win32-tsgatewayserver.md) | Creates a self-signed certificate with a given subject name and returns the certificate hash as an "out" parameter.<br/> |
| [**Export**](export-win32-tsgatewayserver.md)                                           | Returns the RD Gateway server configuration as an XML string.<br/>                                                       |
| [**Import**](import-win32-tsgatewayserver.md)                                           | Imports a given configuration to the RD Gateway server.<br/>                                                             |



 

## Remarks

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](https://msdn.microsoft.com/library/aa823192).

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                 |
| MOF<br/>                      | <dl> <dt>TSGateway.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AagWmi.dll</dt> </dl>    |



 

 






---
title: Application types
description: This topic covers types of applications that you might choose to create as rights-enabled.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '97169FC3-1395-4433-A632-7B0F020FABFE'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
---

# Application types

This topic covers types of applications that you might choose to create as rights-enabled.

The following application types are currently supported by Rights Management Services SDK 2.1

## Simple applications

A simple application could be a command line tool built to encrypt a provided file. For an example of a simple, rights-enabled application see, [IPCHelloWorld - an example application](https://msdn.microsoft.com/library/jj127293).

## Server mode applications

*Server mode* is meant for non-interactive applications that consume, protect or process RMS-protected content. An example would be a *Data Loss Prevention* application that runs as a service on a file server and automatically protects sensitive documents. See the [IpcDlp sample](https://Code.MSDN.Microsoft.Com/IpcDlp-Sample-Application-d30bb99d) for an example of this application type.

If your application uses the *server mode*, it should authenticate to the RMS server silently. Unlike the *client mode*, the RMS SDK 2.1 will not open a credential prompt when it fails to authenticate silently.

For more information on setting the API security mode see, [Setting the API security mode](setting-the-api-security-mode--api-mode-.md).

## Rich client applications

A rich client application allows users to view and manipulate data through a graphical user interface (GUI). Often, the data presented in this GUI is high-value and sensitive to theft or accidental exposure. Information protection support typically enhances existing scenarios but, is not the primary motivation for developing the application.

Using RMS SDK 2.1 with rich client applications helps you:

-   Ensure that this data is always encrypted.

-   Prevent users from extracting data to an unprotected format (for example, prevent using the clipboard to copy and paste).

Microsoft Notepad is a simple rich client application. Microsoft Office is a more complex rich client application.

For more information on protecting your application, see [Understanding usage restrictions](understanding-usage-restrictions.md).

## Related topics

<dl> <dt>

[Developer concepts](https://msdn.microsoft.com/library/windows/desktop/jj127291)
</dt> <dt>

[IpcDlp sample](https://Code.MSDN.Microsoft.Com/IpcDlp-Sample-Application-d30bb99d)
</dt> <dt>

[IPCHelloWorld - an example application](https://msdn.microsoft.com/library/jj127293)
</dt> <dt>

[Setting the API security mode](setting-the-api-security-mode--api-mode-.md)
</dt> <dt>

[Understanding usage restrictions](understanding-usage-restrictions.md)
</dt> </dl>

 

 





---
description: 'To create an application for WMI using C++: you must initialize COM, access and set WMI protocols, and perform a manual cleanup.'
ms.assetid: 0b9b7990-6982-4ba9-8dba-7470990405f7
ms.tgt_platform: multiple
title: Creating a WMI Application Using C++
ms.topic: article
ms.date: 05/31/2018
---

# Creating a WMI Application Using C++

To create an application for WMI using C++: you must initialize COM, access and set WMI protocols, and perform a manual cleanup. However, C++ does have the advantage of flexibility and power. Therefore, while you are better served in using Visual Basic Scripting Edition (VBScript) or Windows PowerShell for simple processes, C++ works better for more sophisticated applications and is required for writing [providers](providing-data-to-wmi.md).

The following procedure describes how to create a WMI application.

**To create a WMI application**

1.  [Initialize COM](initializing-com-for-a-wmi-application.md).

    Because WMI is based on COM technology, you must perform calls to the [**CoInitializeEx**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex) and [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity) functions to access WMI.

2.  [Create a connection to a WMI namespace](creating-a-connection-to-a-wmi-namespace.md).

    By definition, WMI runs in a different process than your application. Therefore, you must create a connection between your application and WMI.

3.  [Set the security levels on the WMI connection](setting-the-security-levels-on-a-wmi-connection.md).

    To use the connection you create to WMI, you must set the impersonation and authentication levels for your application.

4.  Implement the purpose of your application.

    WMI exposes a variety of COM interfaces use to access and manipulate data across your enterprise. For more information, see [Manipulating Class and Instance Information](manipulating-class-and-instance-information.md), [Receiving a WMI Event](receiving-a-wmi-event.md), and [COM API for WMI](com-api-for-wmi.md).

    This is where the bulk of your WMI client application should exist, such as accessing WMI objects or manipulating data.

5.  [Cleanup and shut down your application](cleaning-up-and-shutting-down-a-wmi-application.md).

    After you complete your queries to WMI, you should destroy all COM pointers and shut down your application correctly.

For more information and a code example about how to create a WMI application, see [Example: Creating a WMI Application](example-creating-a-wmi-application.md).

 

 

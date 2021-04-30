---
description: The following procedure demonstrates how to debug a monitor.
ms.assetid: 499f409c-e25a-4ab3-b0aa-e6b308fc7169
title: Debugging a Monitor
ms.topic: article
ms.date: 05/31/2018
---

# Debugging a Monitor

The following procedure demonstrates how to debug a monitor.

**To debug a monitor**

1.  Install the monitor DLL and the program database (.pdb) file generated when you compiled the monitor in the correct location. See [Installing a Monitor to Network Monitor](installing-a-monitor-to-network-monitor.md) for further details.
2.  Verify that the Monitor Control Service is configured as a server instead of a service by selecting Control Panel, Services.
3.  Open a command prompt and go to the Network Monitor directory. Type:

    **Mcsvc.exe /RegServer**

    After the monitor debugging session is complete, you can return the MCSVC to its default condition by typing:

    **Mcsvc.exe /Service**

4.  In Microsoft Visual Studio, launch Microsoft Visual C++.
5.  From the **File**, **Open** menu option, select the name of your monitor DLL.
6.  After Microsoft Visual C++ loads, click **Project**, **Settings**.
7.  Click the **Debug** tab under **Executable** for debug session and type the full path of Mcsvc.exe. For example, C:\\Program files\\Netmon2\\Mcsvc.exe.
8.  Set the breakpoints in the code.

> [!Note]  
> Do not use a message box for monitor debugging. If the MCSVC is running as a service, you will not see the popup, and MCSVC will appear to hang.

 

 

 




---
description: Typically, a provider provides data on behalf of an application.
ms.assetid: 65ea6099-79df-4baa-9752-7df032ccc9a0
title: Communicating With Your Application
ms.topic: article
ms.date: 05/31/2018
---

# Communicating With Your Application

Typically, a provider provides data on behalf of an application. For example, a server might create a performance DLL to provide its counter data. Communication between an application and its provider differs for user-mode and kernel-mode applications. Providers execute in user mode. Because of this, user-mode applications, such as print and display applications, can use any technique for interprocess communication, such as named pipes, file mapping, or RPC. However, kernel-mode applications must provide an IOCTL interface that returns the performance data to the provider.

> [!WARNING]
> Do not use COM as the IPC mechanism. The system cannot guarantee the COM initialization state of the thread calling the interface. Therefore, the DLL may not be able to successfully initialize COM and collect the data.

 

 

 




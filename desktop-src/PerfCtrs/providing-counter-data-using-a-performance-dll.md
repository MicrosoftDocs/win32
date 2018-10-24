---
Description: A service, driver, or application that wants to provide counter data can write a performance DLL to provide the data.
ms.assetid: 030316e5-f9f3-4333-9bb4-7ad301bbe7bf
title: Providing Counter Data Using a Performance DLL
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Providing Counter Data Using a Performance DLL

\[The method for providing performance counter data that this topic describes may be altered or unavailable in the future. Instead, Microsoft recommends that you use the method described in [Providing Counter Data Using Version 2.0](providing-counter-data-using-version-2-0.md) for creating new performance counters, and that you migrate existing performance counters to use that method as well.\]

A service, driver, or application that wants to provide counter data can write a performance DLL to provide the data. When a consumer queries performance data, the system calls the provider to collect the data. For details on writing the performance DLL, see [Creating a Performance Extension DLL](creating-a-performance-extension-dll.md).

The system uses the registry to determine which provider to call. For information on registering your provider and the counters that it supports, see [Adding Performance Counters](adding-performance-counters.md).

You can use a performance DLL to provide counter data for all supported operating systems.

 

 




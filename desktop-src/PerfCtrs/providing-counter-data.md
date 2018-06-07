---
Description: In Windows Vista, Performance Counters implemented a new architecture (version 2.0) for providing counter data.
ms.assetid: c17eda2f-3cf8-40d6-8be6-c1ce190d1a26
title: Providing Counter Data
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Providing Counter Data

In Windows Vista, Performance Counters implemented a new architecture (version 2.0) for providing counter data. The new architecture uses a manifest to define the counter data and injects a thread into your process that collects the counter data directly from your application; all your application does is define and set the counter values and the system handles providing the values to the consumer. For complete details, see [Providing Counter Data Using Version 2.0](providing-counter-data-using-version-2-0.md).

In version 1.0, providers implemented a performance DLL to provide the counter data when a consumer requested it. The provider also used an initialization (.ini) file and registry entries to define the counters and to configure the performance DLL. Although you can still use a performance DLL to provide counter data in Windows Vista, you are encouraged to use the new architecture instead. For details on using a performance DLL, see [Providing Counter Data Using a Performance DLL](providing-counter-data-using-a-performance-dll.md).

 

 




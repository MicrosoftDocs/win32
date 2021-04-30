---
description: Architecture Overview
ms.assetid: ff20d83a-e9cd-46e9-95f7-3ebdf791e667
title: Architecture Overview
ms.topic: article
ms.date: 05/31/2018
---

# Architecture Overview

The WPD architecture can be divided into three processes. Within these processes are the three primary components of WPD: the API, the serializer, and the driver. The following illustration depicts the processes and components that constitute the WPD architecture.

![illustration showing api, serializer, and driver components of wpd](images/wpd-overview-figure1.gif)

## The WPD Application Programming Interface

The WPD API is implemented as an in-proc COM server. The API uses standard Microsoft Win32 APIs to communicate with the appropriate WPD driver. A component called the WPD serializer is used by both API objects and the driver to pack or unpack parameters to or from Windows Driver Foundation (WDF)-User-Mode Driver Framework (UMDF) buffers.

## The WPD Serializer

The WPD serializer is implemented as an in-proc COM server. The WPD API uses the serializer to pack commands and parameters into message buffers that are sent to the driver. The driver uses the serializer to unpack these message buffers for processing. The driver also uses the serializer to pack data and parameters into response buffers that are returned to the WPD API, and the WPD API uses the serializer to unpack these response buffers to return to callers.

## WPD Driver

The WPD driver is implemented as a standard Windows Driver Foundation (WDF)-User-Mode Driver Framework (UMDF) driver. WPD drivers are hosted by UMDF in a separate process called the Driver Host.

The driver receives messages from the UMDF reflector (this is not shown in the diagram, since how the buffers are received is not important to the driver. See UMDF documentation for more information). The driver implements a WPD-specific I/O Control code (IOCL) handler to process WPD messages received by the WPD API. The driver uses the WPD serializer to unpack commands and parameters from these message buffers, and to pack the response into the return buffer.

WPD drivers may communicate with their devices by going through a kernel-mode driver, typically accessed via Win32 file operations (that is, CreateFile, ReadFile, WriteFile, and so on). For the common buses, Microsoft will provide standard kernel drivers for vendors to use, which will allow vendors to ship a user-mode-only driver solution. In addition, for Media Transfer Protocol (MTP) and Mass Storage Class (MSC) devices, Microsoft will provide WPD class drivers.

For more information about WPD drivers, see the Windows Portable Devices Driver documentation in the Windows Driver Kit.

## Related topics

<dl> <dt>

[**Application Overview**](application-overview.md)
</dt> </dl>

 

 




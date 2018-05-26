---
title: Callback Functions
description: Callback Functions
ms.assetid: d238a238-9702-4ba6-92bd-5ef1605b4983
keywords:
- installable drivers,callback functions
- installable drivers,DriverCallback function
- installable drivers,events
- DriverCallback function
- DRV_OPEN message
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Callback Functions

Installable drivers can notify the application, window, or task that opened the given instance about events by using the [DriverCallback](/windows/win32/Digitalv/nf-mmiscapi-drivercallback?branch=master) function. This function gives the driver the means to return information to an application or DLL while continuing to process a request.

If a driver supports callback functions, the application or DLL that opens the instance must supply a value this is either the address of a callback function, a window handle, or a task handle. This value and a flag identifying the type of the value are typically passed in a structure pointed to by the second parameter of the [**DRV\_OPEN**](drv-open.md) message.

 

 





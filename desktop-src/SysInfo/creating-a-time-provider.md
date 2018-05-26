---
Description: A time provider is implemented as a DLL. Each DLL can support multiple time providers. Each provider is responsible for its own configuration and synchronization.
ms.assetid: 04f523d7-7e99-4bf5-941f-ae67f4b9df0a
title: Creating a Time Provider
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating a Time Provider

A time provider is implemented as a DLL. Each DLL can support multiple time providers. Each provider is responsible for its own configuration and synchronization.

Time providers must implement the following callback functions:

-   [**TimeProvClose**](/windows/win32/Timeprov/nf-timeprov-timeprovclose?branch=master)
-   [**TimeProvCommand**](/windows/win32/Timeprov/nf-timeprov-timeprovcommand?branch=master)
-   [**TimeProvOpen**](/windows/win32/Timeprov/nf-timeprov-timeprovopen?branch=master)

After it has loaded the provider DLL, the time provider manager calls [**TimeProvOpen**](/windows/win32/Timeprov/nf-timeprov-timeprovopen?branch=master), passing the name of the provider and pointers to the following functions:

-   [**AlertSamplesAvailFunc**](/windows/win32/Timeprov/nc-timeprov-alertsamplesavailfunc?branch=master)
-   [**GetTimeSysInfoFunc**](/windows/win32/Timeprov/nc-timeprov-gettimesysinfofunc?branch=master)
-   [**LogTimeProvEventFunc**](/windows/win32/Timeprov/nc-timeprov-logtimeproveventfunc?branch=master)

These functions are for use by the time provider. The time provider uses [**TimeProvOpen**](/windows/win32/Timeprov/nf-timeprov-timeprovopen?branch=master) to return a provider handle that the time provider manager uses when sending commands to the time provider. The handle value is defined by the time provider and is used primarily to distinguish between different providers implemented in the same DLL. The time provider can log significant events using [**LogTimeProvEventFunc**](/windows/win32/Timeprov/nc-timeprov-logtimeproveventfunc?branch=master).

The time provider manager uses [**TimeProvCommand**](/windows/win32/Timeprov/nf-timeprov-timeprovcommand?branch=master) to send commands to the time provider. When the time provider needs to notify the time provider manager that it has time samples available, it calls [**AlertSamplesAvailFunc**](/windows/win32/Timeprov/nc-timeprov-alertsamplesavailfunc?branch=master). The time provider manager then calls **TimeProvCommand** with the TPC\_GetSamples command to retrieve the time samples. It can take up to 16 seconds for the time provider manager to request the sample. Therefore, the application should not wait for the request.

To ensure accuracy, the time provider should retrieve all time-related information using [**GetTimeSysInfoFunc**](/windows/win32/Timeprov/nc-timeprov-gettimesysinfofunc?branch=master).

When it is time to shut down the time provider, the time provider manager calls [**TimeProvClose**](/windows/win32/Timeprov/nf-timeprov-timeprovclose?branch=master).

 

 




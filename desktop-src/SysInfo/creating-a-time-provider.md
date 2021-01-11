---
description: A time provider is implemented as a DLL. Each DLL can support multiple time providers. Each provider is responsible for its own configuration and synchronization.
ms.assetid: 04f523d7-7e99-4bf5-941f-ae67f4b9df0a
title: Creating a Time Provider
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Time Provider

A time provider is implemented as a DLL. Each DLL can support multiple time providers. Each provider is responsible for its own configuration and synchronization.

Time providers must implement the following callback functions:

-   [**TimeProvClose**](/windows/desktop/api/Timeprov/nf-timeprov-timeprovclose)
-   [**TimeProvCommand**](/windows/desktop/api/Timeprov/nf-timeprov-timeprovcommand)
-   [**TimeProvOpen**](/windows/desktop/api/Timeprov/nf-timeprov-timeprovopen)

After it has loaded the provider DLL, the time provider manager calls [**TimeProvOpen**](/windows/desktop/api/Timeprov/nf-timeprov-timeprovopen), passing the name of the provider and pointers to the following functions:

-   [**AlertSamplesAvailFunc**](/windows/desktop/api/Timeprov/nc-timeprov-alertsamplesavailfunc)
-   [**GetTimeSysInfoFunc**](/windows/desktop/api/Timeprov/nc-timeprov-gettimesysinfofunc)
-   [**LogTimeProvEventFunc**](/windows/desktop/api/Timeprov/nc-timeprov-logtimeproveventfunc)

These functions are for use by the time provider. The time provider uses [**TimeProvOpen**](/windows/desktop/api/Timeprov/nf-timeprov-timeprovopen) to return a provider handle that the time provider manager uses when sending commands to the time provider. The handle value is defined by the time provider and is used primarily to distinguish between different providers implemented in the same DLL. The time provider can log significant events using [**LogTimeProvEventFunc**](/windows/desktop/api/Timeprov/nc-timeprov-logtimeproveventfunc).

The time provider manager uses [**TimeProvCommand**](/windows/desktop/api/Timeprov/nf-timeprov-timeprovcommand) to send commands to the time provider. When the time provider needs to notify the time provider manager that it has time samples available, it calls [**AlertSamplesAvailFunc**](/windows/desktop/api/Timeprov/nc-timeprov-alertsamplesavailfunc). The time provider manager then calls **TimeProvCommand** with the TPC\_GetSamples command to retrieve the time samples. It can take up to 16 seconds for the time provider manager to request the sample. Therefore, the application should not wait for the request.

To ensure accuracy, the time provider should retrieve all time-related information using [**GetTimeSysInfoFunc**](/windows/desktop/api/Timeprov/nc-timeprov-gettimesysinfofunc).

When it is time to shut down the time provider, the time provider manager calls [**TimeProvClose**](/windows/desktop/api/Timeprov/nf-timeprov-timeprovclose).

 

 




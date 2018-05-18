---
Description: 'A time provider is implemented as a DLL. Each DLL can support multiple time providers. Each provider is responsible for its own configuration and synchronization.'
ms.assetid: '04f523d7-7e99-4bf5-941f-ae67f4b9df0a'
title: Creating a Time Provider
---

# Creating a Time Provider

A time provider is implemented as a DLL. Each DLL can support multiple time providers. Each provider is responsible for its own configuration and synchronization.

Time providers must implement the following callback functions:

-   [**TimeProvClose**](timeprovclose.md)
-   [**TimeProvCommand**](timeprovcommand.md)
-   [**TimeProvOpen**](timeprovopen.md)

After it has loaded the provider DLL, the time provider manager calls [**TimeProvOpen**](timeprovopen.md), passing the name of the provider and pointers to the following functions:

-   [**AlertSamplesAvailFunc**](alertsamplesavail.md)
-   [**GetTimeSysInfoFunc**](gettimesysinfo.md)
-   [**LogTimeProvEventFunc**](logtimeprovevent.md)

These functions are for use by the time provider. The time provider uses [**TimeProvOpen**](timeprovopen.md) to return a provider handle that the time provider manager uses when sending commands to the time provider. The handle value is defined by the time provider and is used primarily to distinguish between different providers implemented in the same DLL. The time provider can log significant events using [**LogTimeProvEventFunc**](logtimeprovevent.md).

The time provider manager uses [**TimeProvCommand**](timeprovcommand.md) to send commands to the time provider. When the time provider needs to notify the time provider manager that it has time samples available, it calls [**AlertSamplesAvailFunc**](alertsamplesavail.md). The time provider manager then calls **TimeProvCommand** with the TPC\_GetSamples command to retrieve the time samples. It can take up to 16 seconds for the time provider manager to request the sample. Therefore, the application should not wait for the request.

To ensure accuracy, the time provider should retrieve all time-related information using [**GetTimeSysInfoFunc**](gettimesysinfo.md).

When it is time to shut down the time provider, the time provider manager calls [**TimeProvClose**](timeprovclose.md).

 

 




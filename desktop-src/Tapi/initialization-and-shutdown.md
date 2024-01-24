---
description: For an application to use any of TAPIs 30 supplementary phone functions, it needs a connection to TAPI, through which it can receive messages.
ms.assetid: c0211f64-4f73-4348-ae49-9a898d3aa093
title: Initialization and Shutdown
ms.topic: article
ms.date: 05/31/2018
---

# Initialization and Shutdown

For an application to use any of TAPI's 30 supplementary phone functions, it needs a connection to TAPI, through which it can receive messages. The application establishes this connection using the [**phoneInitializeEx**](/windows/desktop/api/Tapi/nf-tapi-phoneinitializeexa) function. In this function, the application specifies the notification mechanism by which TAPI informs the application of changes in the state of the phone and of asynchronous completion of phone functions.

The [**phoneInitializeEx**](/windows/desktop/api/Tapi/nf-tapi-phoneinitializeexa) function returns two pieces of information to the application: an *application handle*, and the number of phone devices. The application handle represents the application's usage of TAPI. The TAPI functions that use phone handles do not require the application handle, as this handle is derived from the specified phone handle.

The second piece of information returned by [**phoneInitializeEx**](/windows/desktop/api/Tapi/nf-tapi-phoneinitializeexa) is the number of phone devices available to TAPI. Phone devices are identified by their device identifier (*device ID*). Valid device identifiers range from zero to the number of phone devices minus one. For example, if **phoneInitializeEx** reports that there are two phone devices in a system, then valid phone device identifiers are 0 and 1. After an application is finished using the phone functions of TAPI, it invokes [**phoneShutdown**](/windows/desktop/api/Tapi/nf-tapi-phoneshutdown), passing its application handle to shut down its usage of TAPI. This allows TAPI to free any resources assigned to the application.

Applications should not invoke [**phoneInitializeEx**](/windows/desktop/api/Tapi/nf-tapi-phoneinitializeexa) without subsequently opening a phone (at least for monitoring). If the application is not monitoring and not using any devices, it should call [**phoneShutdown**](/windows/desktop/api/Tapi/nf-tapi-phoneshutdown) so that memory resources allocated by the TAPI dynamic-link library can be released if unneeded, and the library itself can be unloaded from memory while not needed.

Both [**phoneInitializeEx**](/windows/desktop/api/Tapi/nf-tapi-phoneinitializeexa) and [**phoneShutdown**](/windows/desktop/api/Tapi/nf-tapi-phoneshutdown) operate synchronously. That is, these functions either return a success or failure indication, and never return an asynchronous request identifier.

 

 




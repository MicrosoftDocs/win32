---
Description: All service providers must implement Basic Telephony functions.
ms.assetid: 4250f3a0-a66a-4a6e-8566-d71be7463179
title: TSPI Basic Telephony Functions
ms.topic: article
ms.date: 05/31/2018
---

# TSPI Basic Telephony Functions

All service providers must implement Basic Telephony functions. The following is a list of such functions by category. A function is identified as *asynchronous* if it indicates completion in a REPLY message to the application. If the function always returns its result immediately, the function is considered *synchronous*.

-   [Addresses](#addresses)
-   [Answering Incoming Calls](#answering-incoming-calls)
-   [Call Drop Functions](#call-drop-functions)
-   [Call States and Events](#call-states-and-events)
-   [Line Status and Capabilities](#line-status-and-capabilities)
-   [Line Version Negotiation](#line-version-negotiation)
-   [Making Calls](#making-calls)
-   [Opening and Closing Line Devices](#opening-and-closing-line-devices)
-   [Phone Version Negotiation](#phone-version-negotiation)
-   [TSP Initialization and Shutdown](#tsp-initialization-and-shutdown)

## TSP Initialization and Shutdown



|                                                           |                                                           |
|-----------------------------------------------------------|-----------------------------------------------------------|
| [**TUISPI\_providerInstall**](https://msdn.microsoft.com/library/ms725984(v=VS.85).aspx) | Installs a TSP. Synchronous.                              |
| [**TSPI\_providerInstall**](https://msdn.microsoft.com/library/ms725961(v=VS.85).aspx)     | Installs the TSP. Obsolete with Version 2.0. Synchronous. |
| [**TSPI\_providerInit**](https://msdn.microsoft.com/library/ms725960(v=VS.85).aspx)           | Initializes the TSP. Synchronous.                         |
| [**TSPI\_providerShutdown**](https://msdn.microsoft.com/library/ms725963(v=VS.85).aspx)   | Shuts down the service provider.                          |
| [**TUISPI\_providerRemove**](https://msdn.microsoft.com/library/ms725985(v=VS.85).aspx)   | Removes a TSP. Synchronous.                               |
| [**TSPI\_providerRemove**](https://msdn.microsoft.com/library/ms725962(v=VS.85).aspx)       | Removes a TSP. Obsolete with Version 2.0. Synchronous.    |



 

## Phone Version Negotiation



|                                                                           |                                                                                         |
|---------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [**TSPI\_phoneNegotiateTSPIVersion**](https://msdn.microsoft.com/library/ms725940(v=VS.85).aspx) | Returns the highest SPI version the service provider can operate under for this device. |



 

## Line Version Negotiation



|                                                                         |                                                                                                 |
|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| [**TSPI\_lineNegotiateTSPIVersion**](https://msdn.microsoft.com/library/ms725582(v=VS.85).aspx) | Allows an application to negotiate a TSPI version to use with a given line device. Synchronous. |



 

## Line Status and Capabilities



|                                                                     |                                                                                                                                                                |
|---------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**TSPI\_lineGetDevCaps**](https://msdn.microsoft.com/library/ms725568(v=VS.85).aspx)                 | Returns the capabilities of a given line device. Synchronous.                                                                                                  |
| [**TSPI\_lineGetDevConfig**](https://msdn.microsoft.com/library/ms725569(v=VS.85).aspx)             | Returns configuration of a media stream device. Synchronous.                                                                                                   |
| [**TSPI\_lineGetLineDevStatus**](https://msdn.microsoft.com/library/ms725573(v=VS.85).aspx)     | Returns current status of the specified open line device. Synchronous.                                                                                         |
| [**TSPI\_lineSetDevConfig**](https://msdn.microsoft.com/library/ms725602(v=VS.85).aspx)             | Sets the configuration of the specified media stream device. Synchronous.                                                                                      |
| [**TSPI\_lineSetStatusMessages**](https://msdn.microsoft.com/library/ms725606(v=VS.85).aspx)   | Specifies the status changes for which the application needs to be notified. Synchronous.                                                                      |
| [**TSPI\_lineGetID**](https://msdn.microsoft.com/library/ms725572(v=VS.85).aspx)                           | Retrieves a device ID associated with the specified open line, address, or call. Synchronous.                                                                  |
| [**TSPI\_lineGetIcon**](https://msdn.microsoft.com/library/ms725571(v=VS.85).aspx)                       | Allows an application to retrieve an icon for display to the user. Synchronous.                                                                                |
| [**TUISPI\_lineConfigDialog**](https://msdn.microsoft.com/library/ms725976(v=VS.85).aspx)         | Causes the provider of the specified line device to display a dialog box that allows the user to configure parameters related to the line device. Synchronous. |
| [**TUISPI\_lineConfigDialogEdit**](https://msdn.microsoft.com/library/ms725977(v=VS.85).aspx) | Displays a dialog box allowing the user to change configuration information for a line device. Synchronous.                                                    |



 

## Addresses



|                                                                 |                                                                                          |
|-----------------------------------------------------------------|------------------------------------------------------------------------------------------|
| [**TSPI\_lineGetAddressCaps**](https://msdn.microsoft.com/library/ms725560(v=VS.85).aspx)     | Returns the telephony capabilities of an address. Synchronous.                           |
| [**TSPI\_lineGetAddressStatus**](https://msdn.microsoft.com/library/ms725562(v=VS.85).aspx) | Returns current status of a specified address. Synchronous.                              |
| [**TSPI\_lineGetNumAddressIDs**](https://msdn.microsoft.com/library/ms725574(v=VS.85).aspx) | Retrieves the number of address identifiers supported on the indicated line.             |
| [**TSPI\_lineGetAddressID**](https://msdn.microsoft.com/library/ms725561(v=VS.85).aspx)         | Retrieves the address ID of an address specified using an alternate format. Synchronous. |



 

## Opening and Closing Line Devices



|                                           |                                                                                                            |
|-------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [**TSPI\_lineOpen**](https://msdn.microsoft.com/library/ms725583(v=VS.85).aspx)   | Opens a specified line device for providing subsequent monitoring and/or control of the line. Synchronous. |
| [**TSPI\_lineClose**](https://msdn.microsoft.com/library/ms725531(v=VS.85).aspx) | Closes a specified opened line device. Synchronous.                                                        |



 

## Call States and Events



|                                                             |                                                                                     |
|-------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [**TSPI\_lineGetCallInfo**](https://msdn.microsoft.com/library/ms725566(v=VS.85).aspx)       | Returns fixed information about a call. Synchronous.                                |
| [**TSPI\_lineGetCallStatus**](https://msdn.microsoft.com/library/ms725567(v=VS.85).aspx)   | Returns complete call status information for the specified call. Synchronous.       |
| [**TSPI\_lineSetAppSpecific**](https://msdn.microsoft.com/library/ms725594(v=VS.85).aspx) | Sets the application-specific field of a call's information structure. Synchronous. |



 

## Making Calls



|                                                 |                                                                        |
|-------------------------------------------------|------------------------------------------------------------------------|
| [**TSPI\_lineMakeCall**](https://msdn.microsoft.com/library/ms725576(v=VS.85).aspx) | Makes an outbound call and returns a call handle for it. Asynchronous. |
| [**TSPI\_lineDial**](https://msdn.microsoft.com/library/ms725542(v=VS.85).aspx)         | Dials (parts of one or more) dialable addresses. Asynchronous.         |



 

## Answering Incoming Calls



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| [**TSPI\_lineAnswer**](https://msdn.microsoft.com/library/ms725529(v=VS.85).aspx) | Answers an incoming call. Asynchronous. |



 

## Call Drop Functions



|                                         |                                                                           |
|-----------------------------------------|---------------------------------------------------------------------------|
| [**TSPI\_lineDrop**](https://msdn.microsoft.com/library/ms725543(v=VS.85).aspx) | Disconnects a call, or abandons a call attempt in progress. Asynchronous. |



 

 

 




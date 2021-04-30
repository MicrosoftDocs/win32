---
description: All service providers must implement Basic Telephony functions.
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
| [**TUISPI\_providerInstall**](/windows/win32/api/tspi/nf-tspi-tuispi_providerinstall) | Installs a TSP. Synchronous.                              |
| [**TSPI\_providerInstall**](/windows/win32/api/tspi/nf-tspi-tspi_providerinstall)     | Installs the TSP. Obsolete with Version 2.0. Synchronous. |
| [**TSPI\_providerInit**](/windows/win32/api/tspi/nf-tspi-tspi_providerinit)           | Initializes the TSP. Synchronous.                         |
| [**TSPI\_providerShutdown**](/windows/win32/api/tspi/nf-tspi-tspi_providershutdown)   | Shuts down the service provider.                          |
| [**TUISPI\_providerRemove**](/windows/win32/api/tspi/nf-tspi-tuispi_providerremove)   | Removes a TSP. Synchronous.                               |
| [**TSPI\_providerRemove**](/windows/win32/api/tspi/nf-tspi-tspi_providerremove)       | Removes a TSP. Obsolete with Version 2.0. Synchronous.    |



 

## Phone Version Negotiation



|                                                                           |                                                                                         |
|---------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [**TSPI\_phoneNegotiateTSPIVersion**](/windows/win32/api/tspi/nf-tspi-tspi_phonenegotiatetspiversion) | Returns the highest SPI version the service provider can operate under for this device. |



 

## Line Version Negotiation



|                                                                         |                                                                                                 |
|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| [**TSPI\_lineNegotiateTSPIVersion**](/windows/win32/api/tspi/nf-tspi-tspi_linenegotiatetspiversion) | Allows an application to negotiate a TSPI version to use with a given line device. Synchronous. |



 

## Line Status and Capabilities



|                                                                     |                                                                                                                                                                |
|---------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**TSPI\_lineGetDevCaps**](/windows/win32/api/tspi/nf-tspi-tspi_linegetdevcaps)                 | Returns the capabilities of a given line device. Synchronous.                                                                                                  |
| [**TSPI\_lineGetDevConfig**](/windows/win32/api/tspi/nf-tspi-tspi_linegetdevconfig)             | Returns configuration of a media stream device. Synchronous.                                                                                                   |
| [**TSPI\_lineGetLineDevStatus**](/windows/win32/api/tspi/nf-tspi-tspi_linegetlinedevstatus)     | Returns current status of the specified open line device. Synchronous.                                                                                         |
| [**TSPI\_lineSetDevConfig**](/windows/win32/api/tspi/nf-tspi-tspi_linesetdevconfig)             | Sets the configuration of the specified media stream device. Synchronous.                                                                                      |
| [**TSPI\_lineSetStatusMessages**](/windows/win32/api/tspi/nf-tspi-tspi_linesetstatusmessages)   | Specifies the status changes for which the application needs to be notified. Synchronous.                                                                      |
| [**TSPI\_lineGetID**](/windows/win32/api/tspi/nf-tspi-tspi_linegetid)                           | Retrieves a device ID associated with the specified open line, address, or call. Synchronous.                                                                  |
| [**TSPI\_lineGetIcon**](/windows/win32/api/tspi/nf-tspi-tspi_linegeticon)                       | Allows an application to retrieve an icon for display to the user. Synchronous.                                                                                |
| [**TUISPI\_lineConfigDialog**](/windows/win32/api/tspi/nf-tspi-tuispi_lineconfigdialog)         | Causes the provider of the specified line device to display a dialog box that allows the user to configure parameters related to the line device. Synchronous. |
| [**TUISPI\_lineConfigDialogEdit**](/windows/win32/api/tspi/nf-tspi-tuispi_lineconfigdialogedit) | Displays a dialog box allowing the user to change configuration information for a line device. Synchronous.                                                    |



 

## Addresses



|                                                                 |                                                                                          |
|-----------------------------------------------------------------|------------------------------------------------------------------------------------------|
| [**TSPI\_lineGetAddressCaps**](/windows/win32/api/tspi/nf-tspi-tspi_linegetaddresscaps)     | Returns the telephony capabilities of an address. Synchronous.                           |
| [**TSPI\_lineGetAddressStatus**](/windows/win32/api/tspi/nf-tspi-tspi_linegetaddressstatus) | Returns current status of a specified address. Synchronous.                              |
| [**TSPI\_lineGetNumAddressIDs**](/windows/win32/api/tspi/nf-tspi-tspi_linegetnumaddressids) | Retrieves the number of address identifiers supported on the indicated line.             |
| [**TSPI\_lineGetAddressID**](/windows/win32/api/tspi/nf-tspi-tspi_linegetaddressid)         | Retrieves the address ID of an address specified using an alternate format. Synchronous. |



 

## Opening and Closing Line Devices



|                                           |                                                                                                            |
|-------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [**TSPI\_lineOpen**](/windows/win32/api/tspi/nf-tspi-tspi_lineopen)   | Opens a specified line device for providing subsequent monitoring and/or control of the line. Synchronous. |
| [**TSPI\_lineClose**](/windows/win32/api/tspi/nf-tspi-tspi_lineclose) | Closes a specified opened line device. Synchronous.                                                        |



 

## Call States and Events



|                                                             |                                                                                     |
|-------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [**TSPI\_lineGetCallInfo**](/windows/win32/api/tspi/nf-tspi-tspi_linegetcallinfo)       | Returns fixed information about a call. Synchronous.                                |
| [**TSPI\_lineGetCallStatus**](/windows/win32/api/tspi/nf-tspi-tspi_linegetcallstatus)   | Returns complete call status information for the specified call. Synchronous.       |
| [**TSPI\_lineSetAppSpecific**](/windows/win32/api/tspi/nf-tspi-tspi_linesetappspecific) | Sets the application-specific field of a call's information structure. Synchronous. |



 

## Making Calls



|                                                 |                                                                        |
|-------------------------------------------------|------------------------------------------------------------------------|
| [**TSPI\_lineMakeCall**](/windows/win32/api/tspi/nf-tspi-tspi_linemakecall) | Makes an outbound call and returns a call handle for it. Asynchronous. |
| [**TSPI\_lineDial**](/windows/win32/api/tspi/nf-tspi-tspi_linedial)         | Dials (parts of one or more) dialable addresses. Asynchronous.         |



 

## Answering Incoming Calls



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| [**TSPI\_lineAnswer**](/windows/win32/api/tspi/nf-tspi-tspi_lineanswer) | Answers an incoming call. Asynchronous. |



 

## Call Drop Functions



|                                         |                                                                           |
|-----------------------------------------|---------------------------------------------------------------------------|
| [**TSPI\_lineDrop**](/windows/win32/api/tspi/nf-tspi-tspi_linedrop) | Disconnects a call, or abandons a call attempt in progress. Asynchronous. |



 

 

 

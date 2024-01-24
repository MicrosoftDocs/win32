---
description: The supplementary phone service functions are listed by category in the following topics.
ms.assetid: 0d1a81d2-aa9e-4a85-85d3-aa4eabb26eb5
title: Supplementary Phone Service Functions
ms.topic: article
ms.date: 05/31/2018
---

# Supplementary Phone Service Functions

The supplementary phone service functions are listed by category in the following topics. A function is identified as [*asynchronous*](a-tapgloss.md) if it will indicate completion in a REPLY message to the application. If the function always returns its result to the application immediately, the function is considered [*synchronous*](s-tapgloss.md).

Following is a functional grouping of the supplementary phone service functions:

-   [Buttons](#buttons)
-   [Data areas](#data-areas)
-   [Display](#display)
-   [Hookswitch devices](#hookswitch-devices)
-   [Lamps](#lamps)
-   [Opening and closing phone devices](#opening-and-closing-phone-devices)
-   [Phone initialization and shutdown](#phone-initialization-and-shutdown)
-   [Phone status and capabilities](#phone-status-and-capabilities)
-   [Phone version negotiation](#phone-version-negotiation)
-   [Ring](#ring)
-   [Status](#status)

## Phone Initialization and Shutdown



| Function                                       | Description                                                                          |
|------------------------------------------------|--------------------------------------------------------------------------------------|
| [**phoneInitializeEx**](/windows/desktop/api/Tapi/nf-tapi-phoneinitializeexa) | Initializes TAPI phone abstraction for use by the invoking application. Synchronous. |
| [**phoneShutdown**](/windows/desktop/api/Tapi/nf-tapi-phoneshutdown)         | Shuts down an application's use of TAPI's phone abstraction. Synchronous.            |



 

## Phone Version Negotiation



| Function                                                     | Description                                                            |
|--------------------------------------------------------------|------------------------------------------------------------------------|
| [**phoneNegotiateAPIVersion**](/windows/desktop/api/Tapi/nf-tapi-phonenegotiateapiversion) | Allows an application to negotiate a TAPI version to use. Synchronous. |



 

## Opening and Closing Phone Devices



| Function                         | Description                                                                                               |
|----------------------------------|-----------------------------------------------------------------------------------------------------------|
| [**phoneOpen**](/windows/desktop/api/Tapi/nf-tapi-phoneopen)   | Opens the specified phone device, giving the application either owner or monitor privileges. Synchronous. |
| [**phoneClose**](/windows/desktop/api/Tapi/nf-tapi-phoneclose) | Closes a specified open phone device. Synchronous.                                                        |



 

## Phone Status and Capabilities



| Function                                       | Description                                                                                                                                                      |
|------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**phoneGetDevCaps**](/windows/desktop/api/Tapi/nf-tapi-phonegetdevcaps)     | Returns the capabilities of a given phone device. Synchronous.                                                                                                   |
| [**phoneGetID**](/windows/desktop/api/Tapi/nf-tapi-phonegetid)               | Returns a device ID for the given device class associated with the specified phone device. Synchronous.                                                          |
| [**phoneGetIcon**](/windows/desktop/api/Tapi/nf-tapi-phonegeticon)           | Allows an application to retrieve an icon for display to the user. Synchronous.                                                                                  |
| [**phoneConfigDialog**](/windows/desktop/api/Tapi/nf-tapi-phoneconfigdialog) | Causes the provider of the specified phone device to display a dialog box that allows the user to configure parameters related to the phone device. Synchronous. |



 

## Hookswitch Devices



| Function                                         | Description                                                                                       |
|--------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [**phoneSetHookSwitch**](/windows/desktop/api/Tapi/nf-tapi-phonesethookswitch) | Sets the hook state of an open phone's hookswitch devices to a specified mode. Asynchronous.      |
| [**phoneGetHookSwitch**](/windows/desktop/api/Tapi/nf-tapi-phonegethookswitch) | Queries the hookswitch mode of a hookswitch device of an open phone device. Synchronous.          |
| [**phoneSetVolume**](/windows/desktop/api/Tapi/nf-tapi-phonesetvolume)         | Sets the volume of a hookswitch device's speaker of an open phone device. Asynchronous.           |
| [**phoneGetVolume**](/windows/desktop/api/Tapi/nf-tapi-phonegetvolume)         | Returns the volume setting of a hookswitch device's speaker of an open phone device. Synchronous. |
| [**phoneSetGain**](/windows/desktop/api/Tapi/nf-tapi-phonesetgain)             | Sets the gain of a hookswitch device's mic of an open phone device. Asynchronous.                 |
| [**phoneGetGain**](/windows/desktop/api/Tapi/nf-tapi-phonegetgain)             | Returns the gain setting of a hookswitch device's mic of an open phone. Synchronous.              |



 

## Display



| Function                                   | Description                                                              |
|--------------------------------------------|--------------------------------------------------------------------------|
| [**phoneSetDisplay**](/windows/desktop/api/Tapi/nf-tapi-phonesetdisplay) | Writes information to the display of an open phone device. Asynchronous. |
| [**phoneGetDisplay**](/windows/desktop/api/Tapi/nf-tapi-phonegetdisplay) | Returns the current contents of a phone's display. Synchronous.          |



 

## Ring



| Function                             | Description                                                              |
|--------------------------------------|--------------------------------------------------------------------------|
| [**phoneSetRing**](/windows/desktop/api/Tapi/nf-tapi-phonesetring) | Rings an open phone device according to a given ring mode. Asynchronous. |
| [**phoneGetRing**](/windows/desktop/api/Tapi/nf-tapi-phonegetring) | Returns the current ring mode of an opened phone device. Synchronous.    |



 

## Buttons



| Function                                         | Description                                                                    |
|--------------------------------------------------|--------------------------------------------------------------------------------|
| [**phoneSetButtonInfo**](/windows/desktop/api/Tapi/nf-tapi-phonesetbuttoninfo) | Sets the information associated with a button on a phone device. Asynchronous. |
| [**phoneGetButtonInfo**](/windows/desktop/api/Tapi/nf-tapi-phonegetbuttoninfo) | Returns information associated with a button on a phone device. Synchronous.   |



 

## Lamps



| Function                             | Description                                                                                 |
|--------------------------------------|---------------------------------------------------------------------------------------------|
| [**phoneSetLamp**](/windows/desktop/api/Tapi/nf-tapi-phonesetlamp) | Lights a lamp on a specified open phone device in a given lamp lighting mode. Asynchronous. |
| [**phoneGetLamp**](/windows/desktop/api/Tapi/nf-tapi-phonegetlamp) | Returns the current lamp mode of the specified lamp. Synchronous.                           |



 

## Data Areas



| Function                             | Description                                                                             |
|--------------------------------------|-----------------------------------------------------------------------------------------|
| [**phoneSetData**](/windows/desktop/api/Tapi/nf-tapi-phonesetdata) | Downloads a buffer of data to a given data area in the phone device. Asynchronous.      |
| [**phoneGetData**](/windows/desktop/api/Tapi/nf-tapi-phonegetdata) | Uploads the contents of a given data area in the phone device to a buffer. Synchronous. |



 

## Status



| Function                                                 | Description                                                                               |
|----------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [**phoneSetStatusMessages**](/windows/desktop/api/Tapi/nf-tapi-phonesetstatusmessages) | Specifies the status changes for which the application wants to be notified. Synchronous. |
| [**phoneGetStatusMessages**](/windows/desktop/api/Tapi/nf-tapi-phonegetstatusmessages) | Returns the status changes for which the application wants to be notified. Synchronous.   |
| [**phoneGetStatus**](/windows/desktop/api/Tapi/nf-tapi-phonegetstatus)                 | Returns the complete status of an open phone device. Synchronous.                         |



 

 

 




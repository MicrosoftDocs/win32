---
description: Other TAPI phone functions use a handle to an open phone device to identify the open phone device.
ms.assetid: 3e8e18fc-d577-4406-8225-048813c4cb9e
title: Device IDs
ms.topic: article
ms.date: 05/31/2018
---

# Device IDs

Other TAPI phone functions use a handle to an open phone device to identify the open phone device. The only functions for phone devices that take a phone device identifier parameter (as opposed to a phone handle) are the [**phoneGetDevCaps**](/windows/desktop/api/Tapi/nf-tapi-phonegetdevcaps) and [**phoneOpen**](/windows/desktop/api/Tapi/nf-tapi-phoneopen) functions. An application can retrieve the phone's device identifier by using the [**phoneGetID**](/windows/desktop/api/Tapi/nf-tapi-phonegetid) function with the phone handle as a parameter.

An application can also obtain device identifiers for various device classes associated with an opened phone by invoking [**phoneGetID**](/windows/desktop/api/Tapi/nf-tapi-phonegetid). See [TAPI Device Classes](tapi-device-classes.md) for device class names.

This function takes a phone handle and a device class description. It returns the device identifier for the device of the given device class that is associated with the open phone device. If the device class is "tapi/phone", the device identifier of the phone device is returned.

In contrast with line devices, for which the basic line services provide the equivalent of POTS, no minimum guaranteed set of functions is defined for phone devices. While each phone device provides at least the functions and messages described in this section, they do not offer any actual operations on the physical phone device.

 

 




---
description: The Device Power API makes it easy to determine which devices are able to wake the system from a sleep state, and which sleep states those devices support waking from. For more information about sleep states, see System Power States.
ms.assetid: aaa776e5-3fc2-41bd-a805-6c09ef73807b
title: Device Power Management
ms.topic: article
ms.date: 05/31/2018
---

# Device Power Management

The Device Power API makes it easy to determine which devices are able to wake the system from a sleep state, and which sleep states those devices support waking from. For more information about sleep states, see [System Power States](system-power-states.md).

The [**DevicePowerEnumDevices**](/windows/desktop/api/PowrProf/nf-powrprof-devicepowerenumdevices) function can be used to search the device list for devices that match specified criteria. The criteria may include the device's ability to support a system state, or wake from that state. Currently supported flags can be found in WinNT.h and DevPower.h.

The [**DevicePowerSetDeviceState**](/windows/desktop/api/PowrProf/nf-powrprof-devicepowersetdevicestate) function enables or disables a specified device from waking the system from a sleep state.

The Device Power API allows developers to create a better user experience by giving the user more information about what the system is doing, and more control over the devices in the system. Device Power is useful in situations where power consumption is critical, such as in portable devices running on batteries. For example, the power management scheme used in a desktop computer may not be the optimal scheme for a laptop computer, so the user may want to disable certain devices from waking the system. This can conserve energy because the disabled devices will not draw power while the system is in sleep mode.

For an example, see [Using the Device Power API](using-the-device-power-api.md).

 

 




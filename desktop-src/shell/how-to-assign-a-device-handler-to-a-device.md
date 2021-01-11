---
description: Illustrates the process for adding a device handler to a device.
title: How to Assign a Device Handler to a Device
ms.topic: article
ms.date: 05/31/2018
---

# How to Assign a Device Handler to a Device

Illustrates the process for adding a device handler to a device.

## Instructions


To assign a device handler to a device, under the **Device Parameters** subkey of the device instance, add a value of type **REG\_SZ** named **DeviceHandlers**. The data entry for this value is the name of the device handler.

The following is an example entry for a fictitious Vid\_059&Pid\_0031 device.

```
HKEY_LOCAL_MACHINE
   SYSTEM
      CurrentControlSet
         Enum
            USB
               Vid_059b&Pid_0031
                  059B003112010E93
                     Device Parameters
                        DeviceHandlers = MyDeviceHandler
```

Device handlers can also be assigned by using [device group](how-to-specify-an-icon--label--or-device-handler-for-a-device-using-a-device-group.md) or [device class](how-to-specify-an-icon--label--or-device-handler-for-a-device-using-a-device-class.md) settings.

 

 




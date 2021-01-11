---
description: Device groups allow the specification of the Icons, Label, or DeviceHandlers properties for any device that declares itself part of that group.
ms.assetid: 84433068-A869-479D-8ADA-E8221B38CCAE
title: How to Specify an Icon, Label, or Device Handler for a Device Using a Device Group
ms.topic: article
ms.date: 05/31/2018
---

# How to Specify an Icon, Label, or Device Handler for a Device Using a Device Group

Device groups allow the specification of the Icons, Label, or DeviceHandlers properties for any device that declares itself part of that group. If the device group is not a system-provided device group, a key that defines the device group will be added under the **AutoplayHandlers**\\**DeviceGroups** key. You do not need to set all three properties for each group; you can set only those properties that you want to customize. However, devices and device handlers should always have associated icons and labels to meet minimum usability requirements.

## Instructions


The following example uses a system with several attached Zip drives. Without specifying the Icons, Label, and DeviceHandlers values for each drive individually, you create a device group called ZipDrive and define those values within it. Each Zip drive is then declared a member of the ZipDrive group.

First, define the device group by adding the following *ZipDrive* key and its values.

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Microsoft
         Windows
            CurrentVersion
               Explorer
                  AutoplayHandlers
                     DeviceGroups
                        ZipDrive
                           Icons [REG_MULTI_SZ] = %SystemRoot%\system32\mydll.dll,-103
                           NoMediaIcons [REG_MULTI_SZ] = %SystemRoot%\system32\mydll.dll,-104
                           Label [REG_SZ] = My Custom Device Label
                           DeviceHandlers [REG_SZ] = MyDeviceHandler
```

Each Zip drive device is then declared as part of the ZipDrive group, inheriting the properties of that group. Under the **DeviceParameters** key of the device instance, add a value named DeviceGroup as type **REG\_SZ**. The data entry for this value is the name of the device group.

```
HKEY_LOCAL_MACHINE
   SYSTEM
      CurrentControlSet
         Enum
            USB
               Vid_059b&Pid_0031
                  059B003112010E93
                     Device Parameters
                        DeviceGroup [REG_SZ] = ZipDrive
```

You can also add custom device properties other than Icons, Label, and DeviceHandlers under the device group's key and then apply them to all devices that belong to that device group.

> [!Note]  
> Properties that are defined at the device instance level take precedence over properties defined at the device group level, which in turn take precedence over properties defined at the device class level.

 

 

 




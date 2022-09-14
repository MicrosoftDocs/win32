---
description: Device classes allow the specification of the Icons, Label, and DeviceHandlers properties for any device of that class.
ms.assetid: E32C1BA6-B520-4809-A9E9-48813C7EBAA4
title: How to Specify an Icon, Label, or Device Handler for a Device Using a Device Class
ms.topic: article
ms.date: 05/31/2018
---

# How to Specify an Icon, Label, or Device Handler for a Device Using a Device Class

Device classes allow the specification of the Icons, Label, and DeviceHandlers properties for any device of that class. This is similar to the use of device groups, but device classes and their memberships are determined by the hardware rather than being created or assigned. Each class key name, which is the Plug and Play device interface GUID, is found under the **DeviceClasses** key. Under the individual class key, assign the values for Icons, Label, and DeviceHandlers.

## Instructions

### Step 1:

The following example shows the class key and DeviceHandlers values for the volume interface.

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Microsoft
         Windows
            CurrentVersion
               Explorer
                  AutoplayHandlers
                     DeviceClasses
                        {53f5630d-b6bf-11d0-94f2-00a0c91efb8b}
                           DeviceHandlers [REG_SZ] = GenericVolumeHandler
```

You can also add custom device properties under the device class key. The custom device properties then apply to all devices in that class. Devices and device handlers should always have associated icons and labels to meet minimum usability requirements.

> [!Note]  
> Properties that are defined at the device instance level take precedence over properties defined at the device group level, which in turn take precedence over properties defined at the device class level.

 

 

 




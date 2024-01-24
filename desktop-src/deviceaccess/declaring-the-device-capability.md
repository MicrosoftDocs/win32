---
title: Declaring the Device Capability
description: This topic explains how to declare the device capability GUID.
ms.assetid: C663F8D2-2CB6-4C3C-A1EB-A3D93AA71FC8
ms.topic: article
ms.date: 02/11/2020
---

# Declaring the Device Capability

This topic explains how to declare the device capability GUID. All applications that target custom drivers must declare this capability.

In your application manifest, you'll need to add a device capability, as follows:

This is an example of a capability declaration for a custom device. The GUID is the GUID of the device interface class.

```XML
<DeviceCapability Name="0B1F1048-B64B-FC9A-CED7-7E4FED3A0DEB" />
```

## Related topics

[Custom Driver Access Sample](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/411c271e537727d737a53fa2cbe99eaecac00cc0/Official%20Windows%20Platform%20Sample/Custom%20driver%20access%20sample), [UWP device apps for internal devices](/windows-hardware/drivers/devapps/uwp-device-apps-for-specialized-devices), [Hardware Dev Center](/windows-hardware/drivers/)

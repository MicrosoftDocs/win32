---
title: Declaring the Device Capability
description: This topic explains how to declare the device capability GUID.
ms.assetid: 'C663F8D2-2CB6-4C3C-A1EB-A3D93AA71FC8'
---

# Declaring the Device Capability

This topic explains how to declare the device capability GUID. All applications that target custom drivers must declare this capability.

In your application manifest, you'll need to add a device capability, as follows:

This is an example of a capability declaration for a custom device. The GUID is the GUID of the device interface class.


```XML
<DeviceCapability Name="0B1F1048-B64B-FC9A-CED7-7E4FED3A0DEB" />
```



## Related topics

<dl> <dt>

**Samples**
</dt> <dt>

[Custom Driver Access Sample](http://go.microsoft.com/fwlink/p/?linkid=242014)
</dt> <dt>

**White papers**
</dt> <dt>

[Windows Store device app Design Guide for Specialized Devices](http://go.microsoft.com/fwlink/p/?linkid=242009)
</dt> <dt>

**Other resources**
</dt> <dt>

[Device Experience for Specialized Devices](http://go.microsoft.com/fwlink/p/?linkid=242009)
</dt> <dt>

[Device Experience for Windows 8](http://go.microsoft.com/fwlink/p/?linkid=241442)
</dt> <dt>

[Enabling device capabilities](https://msdn.microsoft.com/library/windows/apps/hh768221)
</dt> </dl>

 

 





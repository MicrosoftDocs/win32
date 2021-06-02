---
description: Device Mode
ms.assetid: d56021be-616b-41cd-8cf0-9e0d314f62cd
title: Device Mode
ms.topic: article
ms.date: 05/31/2018
---

# Device Mode

IEEE 1394 and USB camcorders can switch between camera mode and video tape recorder (VTR) mode. When an IEEE 1394 camcorder switches modes, the device resets and the application must enumerate it again. There is no way for an application to switch the mode programmatically. USB camcorders, on the other hand, can switch between camera and VTR modes without resetting, and the application can change the mode.

**MSDV Driver**

To get the current mode on an IEEE 1394 device, call the [**IAMExtDevice::GetCapability**](/windows/desktop/api/Strmif/nf-strmif-iamextdevice-getcapability) method with the value ED\_DEVCAP\_DEVICE\_TYPE. If the method returns the value ED\_DEVTYPE\_VCR, the device is in VTR mode and has functions such as pause, stop, fast-forward, and rewind. Otherwise, if the method returns ED\_DEVTYPE\_CAMERA, the device is in camera mode. The following code example shows how to query the device type:


```C++
if (MyDevCap.bHasDevice) 
{
    LONG lDeviceType = 0;
    MyDevCap.pDevice->GetCapability(ED_DEVCAP_DEVICE_TYPE, &lDeviceType, 0);

    if (lDeviceType == ED_DEVTYPE_VCR) 
    {
        // Device is a VTR. Enable all VTR functions.
    }
    else 
    {
        // Device is a camera. 
        // Enable record and record-pause; disable other functions.
    }
}
```



If the camcorder goes offline, you should query it again when it next becomes available. The filter graph manager posts an [**EC\_DEVICE\_LOST**](ec-device-lost.md) event when the device is removed.

**UVC Driver**

Because USB video devices can switch modes without resetting, the code shown in the previous examples is not reliable for USB devices. Instead, use the [**ISelector**](/previous-versions/windows/desktop/api/Vidcap/nn-vidcap-iselector) interface to get the current mode. You can also use this interface to switch modes programmatically if the device supports it.

## Related topics

<dl> <dt>

[Controlling a DV Camcorder](controlling-a-dv-camcorder.md)
</dt> </dl>

 

 




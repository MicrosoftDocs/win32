---
Description: This section describes the I/O control codes (IOCTLs) that are supported by the Energy Measurement Interface (EMI).
ms.assetid: 18EB5020-2328-4E54-BE63-E9FEB8A5C7C8
title: EMI IOCTLs
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EMI IOCTLs

This section describes the I/O control codes (IOCTLs) that are supported by the Energy Measurement Interface (EMI).

## In this section



| Topic                                                                             | Description                                                                                                                                                                                                                                                              |
|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IOCTL\_EMI\_GET\_MEASUREMENT**](/windows/win32/emi/ni-emi-ioctl_emi_get_measurement?branch=master)<br/>      | The [**IOCTL\_EMI\_GET\_MEASUREMENT**](/windows/win32/emi/ni-emi-ioctl_emi_get_measurement?branch=master) control code retrieves the current energy measurement and the time at which the measurement was taken. <br/>                                                                                 |
| [**IOCTL\_EMI\_GET\_METADATA**](/windows/win32/emi/ni-emi-ioctl_emi_get_metadata?branch=master)<br/>            | The [**IOCTL\_EMI\_GET\_METADATA**](/windows/win32/emi/ni-emi-ioctl_emi_get_metadata?branch=master) control code retrieves EMI metadata from a device.<br/>                                                                                                                                            |
| [**IOCTL\_EMI\_GET\_METADATA\_SIZE**](/windows/win32/emi/ni-emi-ioctl_emi_get_metadata_size?branch=master)<br/> | The [**IOCTL\_EMI\_GET\_METADATA\_SIZE**](/windows/win32/emi/ni-emi-ioctl_emi_get_metadata_size?branch=master) control code retrieves the size of the EMI metadata object that can be obtained from the device by issuing an [**IOCTL\_EMI\_GET\_METADATA**](/windows/win32/emi/ni-emi-ioctl_emi_get_metadata?branch=master) request.<br/> |
| [**IOCTL\_EMI\_GET\_VERSION**](/windows/win32/emi/ni-emi-ioctl_emi_get_version?branch=master)<br/>              | The [**IOCTL\_EMI\_GET\_VERSION**](/windows/win32/emi/ni-emi-ioctl_emi_get_version?branch=master) control code retrieves the current version of the EMI interface supported by the device.<br/>                                                                                                        |



 

> [!Note]  
> The EMI IOCTLs are supported in Windows 10 and later versions of the Windows operating systems.

 

## Related topics

<dl> <dt>

[Energy Metering Interface](energy-metering-interface.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bpowermeter\powermeter%5D:%20EMI%20IOCTLs%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")






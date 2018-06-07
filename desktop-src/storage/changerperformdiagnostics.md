---
title: ChangerPerformDiagnostics function
description: ChangerPerformDiagnostics performs diagnostic tests on the changer device.
ms.assetid: 87767b2b-8ca3-4d19-8719-673562246a41
keywords:
- ChangerPerformDiagnostics function Storage Devices
topic_type:
- apiref
api_name:
- ChangerPerformDiagnostics
api_location:
- mcd.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ChangerPerformDiagnostics function

**ChangerPerformDiagnostics** performs diagnostic tests on the changer device.

## Syntax


```C++
NTSTATUS ChangerPerformDiagnostics(
  _In_  PDEVICE_OBJECT                    DeviceObject,
  _Out_ PWMI_CHANGER_PROBLEM_DEVICE_ERROR ChangerDeviceError
);
```



## Parameters

<dl> <dt>

*DeviceObject* \[in\]
</dt> <dd>

Pointer to the device object that represents the changer.

</dd> <dt>

*ChangerDeviceError* \[out\]
</dt> <dd>

Pointer to the buffer of type [**WMI\_CHANGER\_PROBLEM\_DEVICE\_ERROR**](wmi-changer-problem-device-error.md) in which the minidriver returns the diagnostic information.

</dd> </dl>

## Return value

**ChangerPerformDiagnostics** returns the status returned by the system port driver or one of the following values:

STATUS\_SUCCESS

STATUS\_INSUFFICIENT\_RESOURCES

STATUS\_BUFFER\_TOO\_SMALL

## Remarks

**ChangerPerformDiagnostics** routine performs diagnostic tests on the changer device, and reports the problem to the caller. The kind of tests performed depends on the diagnostics support provided by the device.

## Requirements



|                            |                                                                                                                |
|----------------------------|----------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                             |
| Header<br/>          | <dl> <dt>Mcd.h (include Mcd.h or Ntddchgr.h)</dt> </dl> |



## See also

<dl> <dt>

[**WMI\_CHANGER\_PROBLEM\_DEVICE\_ERROR**](wmi-changer-problem-device-error.md)
</dt> <dt>

[**CHANGER\_DEVICE\_PROBLEM\_TYPE**](changer-device-problem-type.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ChangerPerformDiagnostics%20function%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







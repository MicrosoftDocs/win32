---
Description: The ReceiveMode property is a value from the FAX\_DEVICE\_RECEIVE\_MODE\_ENUM enumeration that defines the way a device answers an incoming call.
ms.assetid: d65397eb-2ede-4320-82ea-8fc48aa3f2b0
title: FaxDevice.ReceiveMode property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxDevice.ReceiveMode property

The **ReceiveMode** property is a value from the [**FAX\_DEVICE\_RECEIVE\_MODE\_ENUM**](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_device_receive_mode_enum) enumeration that defines the way a device answers an incoming call. The value assigned to this property indicates whether the device does not answer the call, the device can answer the call manually, or the device answers the call automatically.

This property is read/write.

## Syntax


```VB
Property ReceiveMode As Integer
```



## Property value

Value from the [**FAX\_DEVICE\_RECEIVE\_MODE\_ENUM**](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_device_receive_mode_enum) enumeration that receives or specifies the way a device answers an incoming call.

## Remarks

You can set only one device to receive faxes manually at any given time. If you set a device to answer manually and another device is already set to the manual mode, the device that had been previously set will automatically change to the no-answer mode. You should call the [**Refresh**](-mfax-faxdevice-refresh-vb.md) method on that device to see the change.

Some devices, such as virtual devices, do not support the manual-answer receive mode. For those devices, the **ReceiveMode** will fail if you set the receive mode to [****fdrmMANUAL\_ANSWER****](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_device_receive_mode_enum). In C++, the method will return an ERROR\_NOT\_SUPPORTED error code in an **Long** format.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-configuring-a-fax-device.md)
</dt> <dt>

[**FaxDevice**](-mfax-faxdevice.md)
</dt> <dt>

[**IFaxDevice**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxdevice)
</dt> </dl>

 

 





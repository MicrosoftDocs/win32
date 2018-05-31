---
Description: The RingsBeforeAnswer property is a number that specifies the number of rings that occur before the fax device answers an incoming fax call.
ms.assetid: 9f8eb0f7-6f54-4ff6-be50-94e65ecc163b
title: FaxDevice.RingsBeforeAnswer property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxDevice.RingsBeforeAnswer property

The **RingsBeforeAnswer** property is a number that specifies the number of rings that occur before the fax device answers an incoming fax call.

This property is read/write.

## Syntax


```VB
Property RingsBeforeAnswer As Long
```



## Property value

A **Long** that specifies or receives the number of rings that occur before the fax device answers an incoming fax call. Possible values are 1 to 99 inclusive.

## Remarks

This property is used only if the [**ReceiveMode**](-mfax-faxdevice-receivemode.md) property of the device is set to [****fdrmAUTO\_ANSWER****](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_device_receive_mode_enum).

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

 

 





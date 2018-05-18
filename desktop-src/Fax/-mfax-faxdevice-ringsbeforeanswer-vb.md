---
Description: 'The RingsBeforeAnswer property is a number that specifies the number of rings that occur before the fax device answers an incoming fax call.'
ms.assetid: '9f8eb0f7-6f54-4ff6-be50-94e65ecc163b'
title: 'FaxDevice.RingsBeforeAnswer property'
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

This property is used only if the [**ReceiveMode**](-mfax-faxdevice-receivemode.md) property of the device is set to [****fdrmAUTO\_ANSWER****](-mfax-fax-device-receive-mode-enum.md).

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

[**IFaxDevice**](-mfax-faxdevice-cpp.md)
</dt> </dl>

 

 





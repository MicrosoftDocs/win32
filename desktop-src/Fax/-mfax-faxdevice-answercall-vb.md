---
Description: The AnswerCall method causes the fax device to answer an incoming call.
ms.assetid: 2075bb20-9eb0-4295-87db-df9e70434ab5
title: FaxDevice.AnswerCall method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxDevice.AnswerCall method

The **AnswerCall** method causes the fax device to answer an incoming call.

## Syntax


```VB
FaxDevice.AnswerCall() As Long
```



## Parameters

This method has no parameters.

## Remarks

The **AnswerCall** method will only work on a fax device on the local server. The method will work regardless of the value of the [**ReceiveMode**](-mfax-faxdevice-receivemode.md) property.

You can use this method to manually answer a call. You may use this method if the [**ReceiveMode**](-mfax-faxdevice-receivemode.md) property is set to answer manually, automatically, or not at all. The fax device must be idle for the incoming call to succeed.

To use this method, a user must have the [****farQUERY\_IN\_ARCHIVE****](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum) access right.

If the method succeeds, the service has successfully accepted the request and has validated the parameters and the access rights. Method success does not indicate that the service answered the call and started to receive a fax. If the method succeeds but the service fails to answer a call on a device, as in the case when the device does not respond as expected, no notification is sent.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxDevice**](-mfax-faxdevice.md)
</dt> <dt>

[**IFaxDevice**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxdevice)
</dt> </dl>

 

 





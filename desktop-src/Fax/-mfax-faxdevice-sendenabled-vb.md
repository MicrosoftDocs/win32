---
Description: The SendEnabled property is a Boolean value that indicates whether the fax device is enabled for sending faxes.
ms.assetid: d525f34f-a8c3-4895-8281-a06d3653af0f
title: FaxDevice.SendEnabled property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxDevice.SendEnabled property

The **SendEnabled** property is a Boolean value that indicates whether the fax device is enabled for sending faxes.

This property is read/write.

## Syntax


```VB
Property SendEnabled As Boolean
```



## Property value

A **Boolean** that specifies or receives a value indicating whether the fax device is enabled for sending faxes.

## Remarks

If this property is equal to **True**, the fax device is enabled to send faxes. If this property is equal to **False**, the fax device is not enabled to send faxes.

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

[**IFaxDevice**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxdevice?branch=master)
</dt> </dl>

 

 





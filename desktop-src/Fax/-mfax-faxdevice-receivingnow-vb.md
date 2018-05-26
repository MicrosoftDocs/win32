---
Description: The ReceivingNow property is a Boolean value that indicates whether the fax device is receiving a fax at the moment the property is retrieved (the status could change immediately thereafter).
ms.assetid: 782a54b1-a417-4daa-be02-497773cdc40c
title: FaxDevice.ReceivingNow property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxDevice.ReceivingNow property

The **ReceivingNow** property is a Boolean value that indicates whether the fax device is receiving a fax at the moment the property is retrieved (the status could change immediately thereafter).

This property is read/write.

## Syntax


```VB
Property ReceivingNow As Boolean
```



## Property value

A **Boolean** that specifies or receives a value indicating whether the fax device is receiving a fax at the moment the property is retrieved.

## Remarks

If this property is equal to **True**, the fax device is currently receiving a fax. If this property is equal to **False**, the fax device is not currently receiving a fax.

> [!Note]  
> The value of this property is set at the time that the [**FaxDevice**](-mfax-faxdevice.md) object is created and is refreshed when you call the [**Refresh**](-mfax-faxdevice-refresh-vb.md) method.

 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-managing-the-fax-device-collection.md)
</dt> <dt>

[**FaxDevice**](-mfax-faxdevice.md)
</dt> <dt>

[**IFaxDevice**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxdevice?branch=master)
</dt> </dl>

 

 





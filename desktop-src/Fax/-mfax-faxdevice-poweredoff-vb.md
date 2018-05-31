---
Description: The PoweredOff property is a Boolean value that indicates whether the fax device is currently available for sending and receiving faxes.
ms.assetid: 3978e0d8-ed2b-47af-837c-a167326ba808
title: FaxDevice.PoweredOff property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxDevice.PoweredOff property

The **PoweredOff** property is a Boolean value that indicates whether the fax device is currently available for sending and receiving faxes.

This property is read-only.

## Syntax


```VB
Property PoweredOff As Boolean
```



## Property value

A **Boolean** that receives a value indicating whether the fax device is currently available for sending and receiving faxes.

## Remarks

If this property is equal to **True**, the fax device is currently offline and unavailable for sending and receiving faxes. If this property is equal to **False**, the fax device is online and available.

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

[**IFaxDevice**](-mfax-faxdevice-cpp.md)
</dt> </dl>

 

 





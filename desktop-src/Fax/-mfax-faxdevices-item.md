---
Description: The Item property returns a FaxDevice object from the FaxDevices collection, using its index.
ms.assetid: 2c8539a4-19e5-47a3-9375-f7adefcb72a4
title: FaxDevices.Item property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxDevices.Item property

The **Item** property returns a [**FaxDevice**](-mfax-faxdevice.md) object from the [**FaxDevices**](-mfax-faxdevices.md) collection, using its index.

This property is read-only.

## Syntax


```VB
Property Item( _
  ByVal vIndex As Variant _
) As IFaxDevice
```



## Property value

A variable of type [**IFaxDevice**](-mfax-faxdevice-cpp.md) that receives a [**FaxDevice**](-mfax-faxdevice.md) object.

## Remarks

To retrieve an item from the [**FaxDevices**](-mfax-faxdevices.md) collection using the device ID, call the [**ItemById**](-mfax-faxdevices-itembyid-vb.md) property.

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

[**FaxDevices**](-mfax-faxdevices.md)
</dt> </dl>

 

 





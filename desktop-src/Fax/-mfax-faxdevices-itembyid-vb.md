---
Description: The get\_ItemById property returns a FaxDevice object from the FaxDevices collection, using its device ID.
ms.assetid: b9629ce2-03ea-4eb1-8e35-1d725658508d
title: FaxDevices.ItemById property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxDevices.ItemById property

The [**get\_ItemById**](/windows/previous-versions/FaxComex/nf-faxcomex-ifaxdevices-get_itembyid?branch=master) property returns a [**FaxDevice**](-mfax-faxdevice.md) object from the [**FaxDevices**](-mfax-faxdevices.md) collection, using its device ID.

This property is read-only.

## Syntax


```VB
Property ItemById( _
  ByVal lId As Long _
) As IFaxDevice
```



## Property value

A variable of type [**IFaxDevice**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxdevice?branch=master) that receives a [**FaxDevice**](-mfax-faxdevice.md) object.

## Remarks

To retrieve an item from the [**FaxDevices**](-mfax-faxdevices.md) collection using the device's index, call the [**Item**](-mfax-faxdevices-item.md) property.

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

[**FaxDevices**](-mfax-faxdevices.md)
</dt> <dt>

[**IFaxDevices**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxdevices?branch=master)
</dt> </dl>

 

 





---
Description: The FaxDevices collection is used by a fax client application to manage fax devices, where each device is represented by a FaxDevice object.
ms.assetid: f04644e4-5e20-490d-847c-001ae2aa7fe5
title: FaxDevices object
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxDevices object

The **FaxDevices** collection is used by a fax client application to manage fax devices, where each device is represented by a [**FaxDevice**](-mfax-faxdevice.md) object.

## Members

The **FaxDevices** object has these types of members:

-   [Properties](#properties)

### Properties

The **FaxDevices** object has these properties.



| Property                                                    | Access type          | Description                                                                                                                                                                                       |
|:------------------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Count**](-mfax-faxdevices-count-vb.md)<br/>       | Read-only<br/> | The [**Count**](-mfax-faxdevices-count-vb.md) property represents the number of objects in the **FaxDevices** collection. This is the total number of devices used by the fax server.<br/> |
| [**Item**](-mfax-faxdevices-item.md)<br/>            | Read-only<br/> | The [**Item**](-mfax-faxdevices-item.md) property returns a [**FaxDevice**](-mfax-faxdevice.md) object from the **FaxDevices** collection, using its index.<br/>                          |
| [**ItemById**](-mfax-faxdevices-itembyid-vb.md)<br/> | Read-only<br/> | The [**get\_ItemById**](/windows/previous-versions/FaxComex/nf-faxcomex-ifaxdevices-get_itembyid?branch=master) property returns a [**FaxDevice**](-mfax-faxdevice.md) object from the **FaxDevices** collection, using its device ID.<br/>         |



 

## Remarks

A **FaxDevices** object is accessed through a [**FaxServer**](-mfax-faxserver.md) object.

![faxserver, faxdevices, and faxdevice objects](images/faxdevices.png)

To create a **FaxDevices** object in Microsoft Visual Basic, call the [**GetDevices**](-mfax-faxserver-getdevices.md) property of the [**FaxServer**](-mfax-faxserver.md) object.

To create a **FaxDevices** object in C++, call the [**GetDevices**](-mfax-faxserver-getdevices.md) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |
| IID<br/>                      | CLSID\_FaxDevices<br/>                                                            |



## See also

<dl> <dt>

[Fax Service object hierarchy](-mfax-fax-service-extended-com-object-model.md)
</dt> <dt>

[**IFaxDevices**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxdevices?branch=master)
</dt> </dl>

 

 





---
title: Properties object
description: Contains a collection of all the Property objects associated with a given Device, DeviceInfo, Filter, ImageFile, or Item object. See the Properties property on any of these objects for details about accessing the Properties object.
ms.assetid: 961252bd-cf93-4f7a-9a46-816bfe7d9afd
keywords:
- Properties object WIA Automation
- Properties object WIA Automation , described
topic_type:
- apiref
api_name:
- Properties
api_location:
- Wiaaut.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# Properties object

Contains a collection of all the [**Property**](-wiaaut-property.md) objects associated with a given [**Device**](-wiaaut-device.md), [**DeviceInfo**](-wiaaut-deviceinfo.md), [**Filter**](-wiaaut-filter.md), [**ImageFile**](-wiaaut-imagefile.md), or [**Item**](-wiaaut-item.md) object. See the Properties property on any of these objects for details about accessing the **Properties** object.

## Members

The **Properties** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Properties** object has these methods.



| Method                                       | Description                                                                                               |
|:---------------------------------------------|:----------------------------------------------------------------------------------------------------------|
| [**Exists**](-wiaaut-iproperties-exists.md) | Indicates whether the specified [**Property**](-wiaaut-property.md) exists in the collection.<br/> |



 

### Properties

The **Properties** object has these properties.



| Property                                                           | Access type          | Description                                                                                          |
|:-------------------------------------------------------------------|:---------------------|:-----------------------------------------------------------------------------------------------------|
| [**Count (Properties)**](-wiaaut-iproperties-count.md)<br/> | Read-only<br/> | Retrieves the number of members in the **Properties** collection.<br/>                         |
| [**Item (Properties)**](-wiaaut-iproperties-item.md)<br/>   | Read-only<br/> | Retrieves the specified item in the **Properties** collection either by position or name.<br/> |



 

## Remarks

Due to the dynamic nature of imaging devices, filters, and image files, the exact collection of [**Property**](-wiaaut-property.md) objects can be very different. Further, **Property** objects are not guaranteed to be in any particular order from one instance of an object to the next.

### Creation\\Access Functions

Use any of the following to retrieve a reference to the object:



[**Properties (ImageFile)**](-wiaaut-iimagefile-properties.md)

[**Properties (Filter)**](-wiaaut-ifilter-properties.md)

[**Properties (Item)**](-wiaaut-iitem-properties.md)

[**Properties (DeviceInfo)**](-wiaaut-ideviceinfo-properties.md)

[**Properties (Device)**](-wiaaut-idevice-properties.md)



 

## Examples

The following sample shows how to enumerate all the properties on a selected device.


```
Dim dev 'As Device
Dim p 'As Property
Dim s 'As String

Set dev = CommonDialog1.ShowSelectDevice

For Each p In dev.Properties
    s = p.Name & "(" & p.PropertyID & ")"
    MsgBox s
Next
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**Properties (Device)**](-wiaaut-idevice-properties.md)
</dt> <dt>

[**Properties (DeviceInfo)**](-wiaaut-ideviceinfo-properties.md)
</dt> <dt>

[**Properties (Filter)**](-wiaaut-ifilter-properties.md)
</dt> <dt>

[**Properties (ImageFile)**](-wiaaut-iimagefile-properties.md)
</dt> <dt>

[**Properties (Item)**](-wiaaut-iitem-properties.md)
</dt> </dl>

 

 






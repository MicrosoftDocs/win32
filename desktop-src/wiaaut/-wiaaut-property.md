---
title: Property object
description: Holds a property associated with a Device, DeviceInfo, Filter, ImageFile or Item object. See the Properties property on any of these objects for details on accessing Property objects. The Property object is a container.
ms.assetid: b5e5a461-f520-4ef1-9b72-0a2b128366f5
keywords:
- Property object WIA Automation
- Property object WIA Automation , described
topic_type:
- apiref
api_name:
- Property
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

# Property object

Holds a property associated with a [**Device**](-wiaaut-device.md), [**DeviceInfo**](-wiaaut-deviceinfo.md), [**Filter**](-wiaaut-filter.md), [**ImageFile**](-wiaaut-imagefile.md) or [**Item**](-wiaaut-item.md) object. See the Properties property on any of these objects for details on accessing **Property** objects. The **Property** object is a container.

## Members

The **Property** object has these types of members:

-   [Properties](#properties)

### Properties

The **Property** object has these properties.



| Property                                                              | Access type           | Description                                                                                                                                               |
|:----------------------------------------------------------------------|:----------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IsReadOnly**](-wiaaut-iproperty-isreadonly.md)<br/>         | Read-only<br/>  | Indicates whether the **Property** value is <br/>                                                                                                   |
| [**IsVector**](-wiaaut-iproperty-isvector.md)<br/>             | Read-only<br/>  | Indicates whether the **Property** value is a vector.<br/>                                                                                          |
| [**Name (Property)**](-wiaaut-iproperty-name.md)<br/>          | Read-only<br/>  | Retrieves the **Property** name.<br/>                                                                                                               |
| [**PropertyID**](-wiaaut-iproperty-propertyid.md)<br/>         | Read-only<br/>  | Retrieves the PropertyID of this **Property**.<br/>                                                                                                 |
| [**SubType**](-wiaaut-iproperty-subtype.md)<br/>               | Read-only<br/>  | Retrieves the SubType of the **Property**, if any exist.<br/>                                                                                       |
| [**SubTypeDefault**](-wiaaut-iproperty-subtypedefault.md)<br/> | Read-only<br/>  | Retrieves the default **Property** value.<br/>                                                                                                      |
| [**SubTypeMax**](-wiaaut-iproperty-subtypemax.md)<br/>         | Read-only<br/>  | Retrieves the maximum valid **Property** value.<br/>                                                                                                |
| [**SubTypeMin**](-wiaaut-iproperty-subtypemin.md)<br/>         | Read-only<br/>  | Retrieves the minimum valid **Property** value.<br/>                                                                                                |
| [**SubTypeStep**](-wiaaut-iproperty-subtypestep.md)<br/>       | Read-only<br/>  | Retrieves the step increment of **Property** values.<br/>                                                                                           |
| [**SubTypeValues**](-wiaaut-iproperty-subtypevalues.md)<br/>   | Read-only<br/>  | Retrieves a [**Vector**](-wiaaut-vector.md) of valid **Property** values or valid flag values.<br/>                                                |
| [**Type (Property)**](-wiaaut-iproperty-type.md)<br/>          | Read-only<br/>  | Retrieves either a [**WiaPropertyType**](-wiaaut-wiapropertytype.md) or a [**WiaImagePropertyType**](-wiaaut-wiaimagepropertytype.md) value.<br/> |
| [**Value (Property)**](-wiaaut-iproperty-value.md)<br/>        | Read/write<br/> | Sets or retrieves the **Property** value.<br/>                                                                                                      |



 

## Remarks

Note that the [**SubTypeDefault**](-wiaaut-iproperty-subtypedefault.md), [**SubTypeValues**](-wiaaut-iproperty-subtypevalues.md), [**SubTypeMin**](-wiaaut-iproperty-subtypemin.md), [**SubTypeMax**](-wiaaut-iproperty-subtypemax.md), and [**SubTypeStep**](-wiaaut-iproperty-subtypestep.md) properties are only accessible if [**SubType**](-wiaaut-iproperty-subtype.md) has a certain value.

For example code, see [Display Detailed Property Information](https://www.bing.com/search?q=Display Detailed Property Information) in Shared Samples.

### Creation\\Access Functions

Use any of the following to retrieve a reference to the object:



[**Item (Properties)**](-wiaaut-iproperties-item.md)



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

[**Item (Properties)**](-wiaaut-iproperties-item.md)
</dt> </dl>

 

 






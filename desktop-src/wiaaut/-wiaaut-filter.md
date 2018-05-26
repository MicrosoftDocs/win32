---
title: Filter object
description: Represents a unit of modification on an ImageFile object. To use a Filter, add it to the Filters collection, and then set the filters properties. Finally, use the Apply method of the ImageProcess object to filter an ImageFile.
ms.assetid: aa1a9ac0-78af-4053-8550-71dbf624400d
keywords:
- Filter object WIA Automation
- Filter object WIA Automation , described
topic_type:
- apiref
api_name:
- Filter
api_location:
- Wiaaut.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Filter object

Represents a unit of modification on an [**ImageFile**](-wiaaut-imagefile.md) object. To use a **Filter**, add it to the [**Filters**](-wiaaut-filters.md) collection, and then set the filter's properties. Finally, use the [**Apply**](-wiaaut-iimageprocess-apply.md) method of the [**ImageProcess**](-wiaaut-imageprocess.md) object to filter an **ImageFile**.

## Members

The **Filter** object has these types of members:

-   [Properties](#properties)

### Properties

The **Filter** object has these properties.



| Property                                                               | Access type          | Description                                                                                     |
|:-----------------------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------------------------|
| [**Description (Filter)**](-wiaaut-ifilter-description.md)<br/> | Read-only<br/> | Retrieves a description of what the filter does.<br/>                                     |
| [**FilterID (Filter)**](-wiaaut-ifilter-filterid.md)<br/>       | Read-only<br/> | Retrieves the [**FilterID (Filter)**](-wiaaut-ifilter-filterid.md) for this Filter.<br/> |
| [**Name (Filter)**](-wiaaut-ifilter-name.md)<br/>               | Read-only<br/> | Retrieves the **Filter** name.<br/>                                                       |
| [**Properties (Filter)**](-wiaaut-ifilter-properties.md)<br/>   | Read-only<br/> | Retrieves a collection of all properties for this filter.<br/>                            |



 

## Remarks

Note that each different filter is listed in the [**FilterInfos**](-wiaaut-filterinfos.md) collection. See the [**FilterInfos (ImageProcess)**](-wiaaut-iimageprocess-filterinfos.md) property on the [**ImageProcess**](-wiaaut-imageprocess.md) object for more information on discovering all the filters available to your application.

For examples that show how to use various filters, see [How To Use Filters](-wiaaut-howto-use-filters.md).

### Creation\\Access Functions

Use any of the following to retrieve a reference to the object:



[**Item (Filters)**](-wiaaut-ifilters-item.md)



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

[**Item (Filters)**](-wiaaut-ifilters-item.md)
</dt> </dl>

 

 






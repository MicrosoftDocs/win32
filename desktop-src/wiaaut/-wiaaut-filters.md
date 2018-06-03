---
title: Filters object
description: Contains a collection of the Filters that are applied to an ImageFile when you call the Apply method on the ImageProcess object.
ms.assetid: 5aa2ec73-a8de-4703-a0bd-c98688456d21
keywords:
- Filters object WIA Automation
- Filters object WIA Automation , described
topic_type:
- apiref
api_name:
- Filters
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

# Filters object

Contains a collection of the Filters that are applied to an [**ImageFile**](-wiaaut-imagefile.md) when you call the [**Apply**](-wiaaut-iimageprocess-apply.md) method on the [**ImageProcess**](-wiaaut-imageprocess.md) object.

## Members

The **Filters** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Filters** object has these methods.



| Method                                              | Description                                                                                                                     |
|:----------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------|
| [**Add (Filters)**](-wiaaut-ifilters-add.md)       | Appends or inserts a new [**Filter**](-wiaaut-filter.md) of the specified *FilterID* into a **Filters** collection.<br/> |
| [**Remove (Filters)**](-wiaaut-ifilters-remove.md) | Removes the designated filter.<br/>                                                                                       |



 

### Properties

The **Filters** object has these properties.



| Property                                                     | Access type          | Description                                                                                   |
|:-------------------------------------------------------------|:---------------------|:----------------------------------------------------------------------------------------------|
| [**Count (Filters)**](-wiaaut-ifilters-count.md)<br/> | Read-only<br/> | Retrieves the number of members in the **Filters** collection.<br/>                     |
| [**Item (Filters)**](-wiaaut-ifilters-item.md)<br/>   | Read-only<br/> | Retrieves the specified item in the **Filters** collection by position or FilterID<br/> |



 

## Remarks

Note that the **Filters** are applied to an [**ImageFile**](-wiaaut-imagefile.md) in the order they are found in this collection. As such, the Convert filter, if used, must be the last filter in the collection and can only occur once.

For example code, see [Convert Filter: Create a Compressed JPEG File from Another File](https://www.bing.com/search?q=Convert Filter: Create a Compressed JPEG File from Another File).

### Creation\\Access Functions

Use any of the following to retrieve a reference to the object:



[**Filters (ImageProcess)**](-wiaaut-iimageprocess-filters.md)



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

[**Filters (ImageProcess)**](-wiaaut-iimageprocess-filters.md)
</dt> </dl>

 

 






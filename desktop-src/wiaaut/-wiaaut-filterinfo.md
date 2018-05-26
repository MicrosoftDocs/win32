---
title: FilterInfo object
description: Describes a Filter object without requiring a Filter to be added to the process chain. The FilterInfo object is a container. See the FilterInfos (ImageProcess) property on the ImageProcess object for details on accessing FilterInfo objects.
ms.assetid: 0a66320e-41c3-457a-82f6-0ed5678ff862
keywords:
- FilterInfo object WIA Automation
- FilterInfo object WIA Automation , described
topic_type:
- apiref
api_name:
- FilterInfo
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

# FilterInfo object

Describes a [**Filter**](-wiaaut-filter.md) object without requiring a **Filter** to be added to the process chain. The **FilterInfo** object is a container. See the [**FilterInfos (ImageProcess)**](-wiaaut-iimageprocess-filterinfos.md) property on the [**ImageProcess**](-wiaaut-imageprocess.md) object for details on accessing **FilterInfo** objects.

## Members

The **FilterInfo** object has these types of members:

-   [Properties](#properties)

### Properties

The **FilterInfo** object has these properties.



| Property                                                                       | Access type          | Description                                                                                               |
|:-------------------------------------------------------------------------------|:---------------------|:----------------------------------------------------------------------------------------------------------|
| [**Description (FilterInfo)**](-wiaaut-ifilterinfo-description.md)<br/> | Read-only<br/> | Retrieves a technical description of what the filter does and how to use it in a filter chain.<br/> |
| [**FilterID (FilterInfo)**](-wiaaut-ifilterinfo-filterid.md)<br/>       | Read-only<br/> | Retrieves the [**FilterID (FilterInfo)**](-wiaaut-ifilterinfo-filterid.md) for this filter.<br/>   |
| [**Name (FilterInfo)**](-wiaaut-ifilterinfo-name.md)<br/>               | Read-only<br/> | Retrieves the **FilterInfo** name.<br/>                                                             |



 

## Remarks

Note that to add a [**Filter**](-wiaaut-filter.md) to a filter chain, you need to use the [**FilterID (FilterInfo)**](-wiaaut-ifilterinfo-filterid.md) property to get the FilterID. Next, use this ID when calling the [**Add (Filters)**](-wiaaut-ifilters-add.md) method on the [**Filters**](-wiaaut-filters.md) collection in the [**ImageProcess**](-wiaaut-imageprocess.md) object.

For more information on all the filters available to your application, see the [**Filter**](-wiaaut-filter.md) object.

For example code, see [Create an ImageProcess Object and Enumerate Filters](-wiaaut-shared-samples.md#create-an-imageprocess-object-and-enumerate-filters) in Shared Samples.

### Creation\\Access Functions

Use any of the following to retrieve a reference to the object:



[**Item (FilterInfos)**](-wiaaut-ifilterinfos-item.md)



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

[**Item (FilterInfos)**](-wiaaut-ifilterinfos-item.md)
</dt> </dl>

 

 






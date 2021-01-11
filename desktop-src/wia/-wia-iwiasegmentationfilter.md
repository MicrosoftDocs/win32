---
description: The IWiaSegmentationFilter interface detects sub-regions of an image stream and makes separate IWiaItem2 items for each.
ms.assetid: eb7f1284-ab98-4d86-8b30-7abd504cee12
title: IWiaSegmentationFilter interface (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaSegmentationFilter
api_type: 
- COM
api_location: 
- Wia.h
---

# IWiaSegmentationFilter interface

The **IWiaSegmentationFilter** interface detects sub-regions of an image stream and makes separate [**IWiaItem2**](-wia-iwiaitem2.md) items for each.

## Members

The **IWiaSegmentationFilter** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IWiaSegmentationFilter** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWiaSegmentationFilter** interface has these methods.



| Method                                                             | Description                                                                                                                                              |
|:-------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DetectRegions**](-wia-iwiasegmentationfilter-detectregions.md) | Determines the sub-regions of an image laid out on the flatbed platen so that each of sub-region can be acquired into a separate image item. <br/> |



 

## Remarks

An application should use [**IWiaItem2::GetExtension**](-wia-iwiaitem2-getextension.md) to create a new instance of the segmentation filter. An application typically calls this function before displaying its preview window.

When implementing this filter, use [**IWiaItem2::CreateChildItem**](-wia-iwiaitem2-createchilditem.md) to create the child items. The application should pass **COPY\_PARENT\_PROPERTY\_VALUES** to the *ICreationFlags* parameter to ensure that properties such as image format and resolution is the same in the newly created child as in the parent item.

A segmentation filter must support all the image formats that the driver it is used with supports. The Microsoft provided filter supports bitmap (BMP), Graphics Interchange Format (GIF), JPEG, Portable Network Graphics (PNG), and Tagged Image File Format (TIFF).

The segmentation filter should be used only on film and flatbed scanner items. For film scanning, a scanner often comes with fixed frames in which case the driver created the child items and the application should not invoke the segmentation filter.

The **IWiaSegmentationFilter** interface, like all Component Object Model (COM) interfaces, inherits the [IUnknown](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface methods.



| IUnknown Methods                                        | Description                               |
|---------------------------------------------------------|-------------------------------------------|
| [IUnknown::QueryInterface](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) | Returns pointers to supported interfaces. |
| [IUnknown::AddRef](/windows/win32/api/unknwn/nf-unknwn-iunknown-addref)                 | Increments reference count.               |
| [IUnknown::Release](/windows/win32/api/unknwn/nf-unknwn-iunknown-release)               | Decrements reference count.               |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl> |



 

 

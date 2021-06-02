---
description: Defines methods to obtain information about the properties of a search item. This interface is supported only on Windows XP and Windows Server 2003, and should no longer be used.
ms.assetid: 0fef34c5-f20f-475a-9223-5cb73079c842
title: IItemPropertyBag interface
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IItemPropertyBag
api_type: 
- COM
api_location: 
---

# IItemPropertyBag interface

Defines methods to obtain information about the properties of a search item. This interface is supported only on Windows XP and Windows Server 2003, and should no longer be used.

## Members

The **IItemPropertyBag** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IItemPropertyBag** also has these types of members:

-   [Methods](#methods)

### Methods

The **IItemPropertyBag** interface has these methods.



| Method                                                      | Description                                                                                  |
|:------------------------------------------------------------|:---------------------------------------------------------------------------------------------|
| [**CountProperties**](/previous-versions/windows/desktop/legacy/ff684387(v=vs.85)) | Gets a count of the number of properties in the property bag.<br/>                     |
| [**GetPropertyInfo**](iitempropertybag-getpropertyinfo.md) | Gets the information required to read or save the properties in the property bag.<br/> |
| [**Read**](iitempropertybag-read.md)                       | Causes one or more properties to be read from the property bag.<br/>                   |
| [**Write**](iitempropertybag-write.md)                     | Causes one or more properties to be saved into the property bag.<br/>                  |



 

## Remarks

The **IItemPropertyBag** interface is supported only on Windows XP and Windows Server 2003, and should no longer be used.

To preview attachments with a third-party protocol handler on computers running Windows XP or Windows Server 2003, it may be necessary to use the **IItemPropertyBag** interface and the following APIs: the [**ISearchProtocolUI**](-search-isearchprotocolui.md), [**IItemPreviewerExt**](-search-iitempreviewerext.md) and [**ISearchItem**](-search-isearchitem.md) interfaces, the [**LINKINFO**](-search-linkinfo.md) and [**ITEMPROP**](/windows/desktop/api/subsmgr/ns-subsmgr-itemprop) structures, and the [**LINKTYPE**](-search-linktype.md) enumeration.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |
| Redistributable<br/>          | Windows Desktop Search (WDS) 3.0<br/>          |



 

 

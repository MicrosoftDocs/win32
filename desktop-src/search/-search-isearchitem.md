---
description: Provides methods that define interaction between a user interface (UI) and the Search namespace objects created by the indexer.
ms.assetid: e48c9e5b-9b15-4bc1-91ef-81ba7a05bfbd
title: ISearchItem interface
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISearchItem
api_type: 
- COM
api_location: 
---

# ISearchItem interface

Provides methods that define interaction between a user interface (UI) and the Search namespace objects created by the indexer.

## Members

The **ISearchItem** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ISearchItem** also has these types of members:

-   [Methods](#methods)

### Methods

The **ISearchItem** interface has these methods.



| Method                                                         | Description                                                                                                                               |
|:---------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetParentFolder**](-search-isearchitem-getparentfolder.md) | Gets the **ISearchItem** object if the URL represents an actual Shell data source (also known as a Shell namespace extension).<br/> |
| [**GetUIObjectOf**](/previous-versions/windows/desktop/legacy/dd756721(v=vs.85))     | Gets the user interface (UI) object of **ISearchItem**.<br/>                                                                        |



 

## Remarks

The [**ISearchItem::GetParentFolder**](-search-isearchitem-getparentfolder.md) is supported only on Windows XP and Windows Server 2003, and should no longer be used.

To preview attachments with a third-party protocol handler on computers running Windows XP or Windows Server 2003, it may be necessary to use the **ISearchItem** interface, and the following APIs: the [**IItemPreviewerExt**](-search-iitempreviewerext.md), [**IItemPropertyBag**](iitempropertybag.md), and [**ISearchProtocolUI**](-search-isearchprotocolui.md) interfaces, the [**LINKINFO**](-search-linkinfo.md) structure, and the [**LINKTYPE**](-search-linktype.md) enumeration.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |
| Redistributable<br/>          | Windows Desktop Search (WDS) 3.0<br/>          |



 

 

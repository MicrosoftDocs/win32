---
description: Provides methods for supplying browser settings. The IItemPreviewerExt interface is supported only on Windows XP and Windows Server 2003, and should no longer be used.
ms.assetid: d7d6cbb0-18bf-4e68-b7b4-307cadbced5c
title: IItemPreviewerExt interface
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IItemPreviewerExt
api_type: 
- COM
api_location: 
---

# IItemPreviewerExt interface

Provides methods for supplying browser settings. The **IItemPreviewerExt** interface is supported only on Windows XP and Windows Server 2003, and should no longer be used.

## Members

The **IItemPreviewerExt** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IItemPreviewerExt** also has these types of members:

-   [Methods](#methods)

### Methods

The **IItemPreviewerExt** interface has these methods.



| Method                                                                               | Description                                                                                  |
|:-------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------|
| [**GetLinkedContent**](-search-iitempreviewerext-getlinkedcontent.md)               | Permits the extension to rich content for a property. <br/>                            |
| [**GetRelatedPart**](-search-iitempreviewerext-getrelatedpart.md)                   | Gets a related body part for embedding into the output MHTML stream.<br/>              |
| [**ProcessTransformCommand**](-search-iitempreviewerext-processtransformcommand.md) | Permits processing of a transformation command encountered in a preview template.<br/> |
| [**SuggestBrowserPolicy**](-search-iitempreviewerext-suggestbrowserpolicy.md)       | Suggests the security policy to be applied to the browser.<br/>                        |



 

## Remarks

The **IItemPreviewerExt** interface is supported only on Windows XP and Windows Server 2003, and should no longer be used.

To preview attachments with a third-party protocol handler on computers running Windows XP or Windows Server 2003, it may be necessary to use the **IItemPreviewerExt** interface, and the following APIs: the [**ISearchProtocolUI**](-search-isearchprotocolui.md), [**IItemPropertyBag**](iitempropertybag.md) and [**ISearchItem**](-search-isearchitem.md) interfaces, the [**LINKINFO**](-search-linkinfo.md) structure, and the [**LINKTYPE**](-search-linktype.md) enumeration.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |
| Redistributable<br/>          | Windows Desktop Search (WDS) 3.0<br/>          |



 

 

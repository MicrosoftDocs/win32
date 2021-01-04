---
title: DROPEFFECT Constants (OleIdl.h)
description: Represents information about the effects of a drag-and-drop operation.
ms.assetid: d8e46899-3fbf-4012-8dd3-67fa627526d5
topic_type:
- apiref
api_name:
- DROPEFFECT_NONE
- DROPEFFECT_COPY
- DROPEFFECT_MOVE
- DROPEFFECT_LINK
- DROPEFFECT_SCROLL
api_location:
- OleIdl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DROPEFFECT Constants

Represents information about the effects of a drag-and-drop operation. The [**DoDragDrop**](/windows/desktop/api/Ole2/nf-ole2-dodragdrop) function and many of the methods in the [**IDropSource**](/windows/desktop/api/OleIdl/nn-oleidl-idropsource) and [**IDropTarget**](/windows/desktop/api/OleIdl/nn-oleidl-idroptarget) use the values of this enumeration.



| Constant/value                                                                                                                                                                                                                            | Description                                                                                                                         |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------|
| <span id="DROPEFFECT_NONE"></span><span id="dropeffect_none"></span><dl> <dt>**DROPEFFECT\_NONE**</dt> <dt>0</dt> </dl>                | Drop target cannot accept the data.<br/>                                                                                      |
| <span id="DROPEFFECT_COPY"></span><span id="dropeffect_copy"></span><dl> <dt>**DROPEFFECT\_COPY**</dt> <dt>1</dt> </dl>                | Drop results in a copy. The original data is untouched by the drag source.<br/>                                               |
| <span id="DROPEFFECT_MOVE"></span><span id="dropeffect_move"></span><dl> <dt>**DROPEFFECT\_MOVE**</dt> <dt>2</dt> </dl>                | Drag source should remove the data. <br/>                                                                                     |
| <span id="DROPEFFECT_LINK"></span><span id="dropeffect_link"></span><dl> <dt>**DROPEFFECT\_LINK**</dt> <dt>4</dt> </dl>                | Drag source should create a link to the original data.<br/>                                                                   |
| <span id="DROPEFFECT_SCROLL"></span><span id="dropeffect_scroll"></span><dl> <dt>**DROPEFFECT\_SCROLL**</dt> <dt>0x80000000</dt> </dl> | Scrolling is about to start or is currently occurring in the target. This value is used in addition to the other values.<br/> |



## Remarks

Your application should always mask values from the **DROPEFFECT** enumeration to ensure compatibility with future implementations. Presently, only some of the positions in a **DROPEFFECT** value have meaning. In the future, more interpretations for the bits will be added. Drag sources and drop targets should carefully mask these values appropriately before comparing. They should never compare a **DROPEFFECT** against, say, DROPEFFECT\_COPY by doing the following:

``` syntax
if (dwDropEffect == DROPEFFECT_COPY)... 
```

Instead, the application should always mask for the value or values being sought as using one of the following techniques:

``` syntax
if (dwDropEffect & DROPEFFECT_COPY) == DROPEFFECT_COPY)...

if (dwDropEffect & DROPEFFECT_COPY)... 
```

This allows for the definition of new drop effects, while preserving backward compatibility with existing code.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>OleIdl.h</dt> </dl> |



## See also

<dl> <dt>

[**DoDragDrop**](/windows/desktop/api/Ole2/nf-ole2-dodragdrop)
</dt> <dt>

[**IDropSource**](/windows/desktop/api/OleIdl/nn-oleidl-idropsource)
</dt> <dt>

[**IDropTarget**](/windows/desktop/api/OleIdl/nn-oleidl-idroptarget)
</dt> </dl>

 

 






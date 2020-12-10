---
title: LB_ADDFILE message (Winuser.h)
description: Adds the specified filename to a list box that contains a directory listing.
ms.assetid: 60426293-779b-4a4b-95a2-4901b5f6a13b
keywords:
- LB_ADDFILE message Windows Controls
topic_type:
- apiref
api_name:
- LB_ADDFILE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LB\_ADDFILE message

Adds the specified filename to a list box that contains a directory listing.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a buffer that specifies the name of the file to add.

</dd> </dl>

## Return value

The return value is the zero-based index of the file that was added, or LB\_ERR if an error occurs.

## Remarks

The list box to which *lParam* is added must have been filled by the [**DlgDirList**](/windows/desktop/api/Winuser/nf-winuser-dlgdirlista) function.

The [**LB\_INITSTORAGE**](lb-initstorage.md) message helps speed up the initialization of list boxes that have a large number of items (more than 100). It reserves the specified amount of memory so that subsequent **LB\_ADDFILE** messages take the shortest possible time. You can use estimates for the *wParam* and *lParam* parameters. If you overestimate, the extra memory is allocated; if you underestimate, the normal allocation is used for items that exceed the requested amount.

For an ANSI application, the system converts the text in a list box to Unicode using CP\_ACP. This can cause problems. For example, accented Roman characters in a non-Unicode list box in Japanese Windows will come out garbled. To fix this, either compile the application as Unicode or use an owner-drawn list box.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**DlgDirList**](/windows/desktop/api/Winuser/nf-winuser-dlgdirlista)
</dt> <dt>

[**LB\_ADDSTRING**](lb-addstring.md)
</dt> </dl>

 

 






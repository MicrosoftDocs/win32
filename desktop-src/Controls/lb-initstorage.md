---
title: LB_INITSTORAGE message (Winuser.h)
description: Allocates memory for storing list box items. This message can be used before an application adds a large number of items to a list box.
ms.assetid: abc49049-3424-46c6-981a-b858afe88883
keywords:
- LB_INITSTORAGE message Windows Controls
topic_type:
- apiref
api_name:
- LB_INITSTORAGE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LB\_INITSTORAGE message

Allocates memory for storing list box items. This message can be used before an application adds a large number of items to a list box.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The number of items for which to reserve space.

Windows 95/Windows 98/Windows Millennium Edition (Windows Me) : The *wParam* parameter is limited to 16-bit values. This means list boxes cannot contain more than 32,767 items. Although the number of items is restricted, the total size in bytes of the items in a list box is limited only by available memory.

</dd> <dt>

*lParam* 
</dt> <dd>

The amount of additional memory, in bytes, to allocate for item strings.

</dd> </dl>

## Return value

If the message is successful, the return value is the total number of items that the list box can store before a memory reallocation is needed.

If the message fails, the return value is LB\_ERRSPACE.

Microsoft Windows NT 4.0 : This message does not allocate the specified amount of memory; however, it always returns the value specified in the *wParam* parameter.

## Remarks

The **LB\_INITSTORAGE** message helps speed up the initialization of list boxes that have a large number of items (more than 100). It reserves the specified amount of memory so that subsequent [**LB\_ADDSTRING**](lb-addstring.md), [**LB\_INSERTSTRING**](lb-insertstring.md), [**LB\_DIR**](lb-dir.md), and [**LB\_ADDFILE**](lb-addfile.md) messages are more efficient. You can use estimates for the *wParam* and *lParam* parameters. If you overestimate, the extra memory remains allocated; if you underestimate, the list box will allocate additional memory as necessary.

The memory required to store a string includes the null terminator. Therefore, if you plan to add 100 strings, each with a length of 10 characters, you would pass a *wParam* of 100 and an *lParam* of 100 &times; (10 + 1) &times; sizeof(TCHAR).

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

[**LB\_ADDFILE**](lb-addfile.md)
</dt> <dt>

[**LB\_ADDSTRING**](lb-addstring.md)
</dt> <dt>

[**LB\_DIR**](lb-dir.md)
</dt> <dt>

[**LB\_INSERTSTRING**](lb-insertstring.md)
</dt> </dl>

 

 






---
title: TVM_SETBORDER message (Commctrl.h)
description: Sets the size of the border for the items in a tree-view control. You can send the message explicitly or by using the TreeView\_SetBorder macro.
ms.assetid: 468b46ae-2ab2-4753-a0af-7c644f75ce62
keywords:
- TVM_SETBORDER message Windows Controls
topic_type:
- apiref
api_name:
- TVM_SETBORDER
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_SETBORDER message

**Intended for internal use; not recommended for use in applications.**

Sets the size of the border for the items in a tree-view control. You can send the message explicitly or by using the [**TreeView\_SetBorder**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_setborder) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Action flags. This parameter can be one or more of the following values:



| Value                                                                                                                                                         | Meaning                                                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| <span id="TVSBF_XBORDER"></span><span id="tvsbf_xborder"></span><dl> <dt>**TVSBF\_XBORDER**</dt> </dl> | Applies the specified border size to the left side of the items in the tree-view control. <br/> |
| <span id="TVSBF_YBORDER"></span><span id="tvsbf_yborder"></span><dl> <dt>**TVSBF\_YBORDER**</dt> </dl> | Applies the specified border size to the top of the items in the tree-view control.<br/>        |



 

</dd> <dt>

*lParam* 
</dt> <dd>

The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) is a **SHORT** that specifies the size of the left border, in pixels. The [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) is a **SHORT** that specifies the size of the top border, in pixels.

</dd> </dl>

## Return value

Returns a **LONG** value that contains the previous border size, in pixels. The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) contains the previous size of the horizontal border, and the [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) contains the previous size of the vertical border.

## Remarks

**Security Warning:** Using this message might compromise the security of your program.

The item border is set just for spacing purposes. A successful setting triggers a recalculation of the scroll bars.

This message may not be supported in future versions of Comctl32.dll. Also, this message is not defined in commctrl.h. Add the following definitions to the source files of your application to use the message:

``` syntax
#define TVM_SETBORDER (TV_FIRST + 35)
#define TVSBF_XBORDER 0x00000001
#define TVSBF_YBORDER 0x00000002 
```

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TreeView\_SetBorder**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_setborder)
</dt> </dl>

 


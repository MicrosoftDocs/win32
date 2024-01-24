---
description: The WM\_TABLET\_DELETED message is posted when a tablet device is removed from Windows.
ms.assetid: af5be7f0-a213-49a1-800e-c922281522c8
title: WM_TABLET_DELETED message (Tpcshrd.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_TABLET\_DELETED message

The **WM\_TABLET\_DELETED** message is posted when a tablet device is removed from Windows.


```C++
#define WM_TABLET_DEFBASE   0x02C0
#define WM_TABLET_DELETED   (WM_TABLET_DEFBASE + 9)     
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Index of tablet device being removed.

</dd> <dt>

*lParam* 
</dt> <dd>

Unused.

</dd> </dl>

## Remarks

This message is sent to all top-level windows in the system, including disabled or invisible unowned windows, overlapped windows, and pop-up windows; but the message is not sent to child windows.

The indexes passed in *wParam* are related to the index used by the [**ITabletManager::GetTablet**](/previous-versions/windows/desktop/legacy/aa373683(v=vs.85)) method.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                        |
| Minimum supported server<br/> | None supported<br/>                                                            |
| Header<br/>                   | <dl> <dt>Tpcshrd.h</dt> </dl> |



 

 

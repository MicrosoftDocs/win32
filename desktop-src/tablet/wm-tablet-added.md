---
description: The WM\_TABLET\_ADDED message is posted when a tablet device is added to Windows.
ms.assetid: 74323b34-2364-47eb-b8ac-b97546e43b32
title: WM_TABLET_ADDED message (Tpcshrd.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_TABLET\_ADDED message

The **WM\_TABLET\_ADDED** message is posted when a tablet device is added to Windows.


```C++
#define WM_TABLET_DEFBASE  0x02C0
#define WM_TABLET_ADDED    (WM_TABLET_DEFBASE + 8)      
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Index of tablet device being added

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



 

 

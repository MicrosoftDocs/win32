---
Description: The following are the Flicks constants.
ms.assetid: 21aaf8f0-13b7-4f97-ad4a-3557a7020337
title: Flicks Constants
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Flicks Constants

The following are the Flicks constants.



| Constant/value                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="FLICK_WM_HANDLED_MASK"></span><span id="flick_wm_handled_mask"></span><dl> <dt>**FLICK\_WM\_HANDLED\_MASK**</dt> <dt>0x1</dt> </dl> | The value to return after handling the [**WM\_TABLET\_FLICK Message**](wm-tablet-flick-message.md) message. If **FLICK\_WM\_HANDLED\_MASK** is returned, no further action occurs. Otherwise, Windows sends follow-up notifications, such as [**WM\_APPCOMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms646275), [**WM\_VSCROLL**](https://msdn.microsoft.com/library/windows/desktop/bb787577), or [**WM\_KEYDOWN**](https://msdn.microsoft.com/library/windows/desktop/ms646280), depending on which action is associated with the pen flick. <br/> |
| <span id="NUM_FLICK_DIRECTIONS"></span><span id="num_flick_directions"></span><dl> <dt>**NUM\_FLICK\_DIRECTIONS**</dt> <dt>8</dt> </dl>       | The number of directions defined in the [**FLICKDIRECTION**](/windows/desktop/api/tabflicks/ne-tabflicks-flickdirection) enumeration.<br/>                                                                                                                                                                                                                                                                                                                                                              |



## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Tabflicks.h</dt> </dl> |



## See also

<dl> <dt>

[**FLICKDIRECTION Enumeration**](/windows/desktop/api/tabflicks/ne-tabflicks-flickdirection)
</dt> <dt>

[**WM\_TABLET\_FLICK Message**](wm-tablet-flick-message.md)
</dt> <dt>

[Flicks Gestures](flicks-gestures.md)
</dt> <dt>

[Responding to Pen Flicks](https://www.bing.com/search?q=Responding+to+Pen+Flicks)
</dt> </dl>

 

 





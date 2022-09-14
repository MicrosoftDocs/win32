---
title: Desktop App functionality is impacted if not run in Windowed Mode
description: In Windows 10, Windows apps are no longer full-screen by default – instead, they are windowed and operations like minimizing, restoring, maximizing, resizing (and any other operation that you’ve always been able to do to any other Classic Windows application window) is now possible.
ms.assetid: 435E85DA-008B-437E-92CB-AC105855760A
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Desktop App functionality is impacted if not run in Windowed Mode

In Windows 10, Windows apps are no longer full-screen by default – instead, they are windowed and operations like minimizing, restoring, maximizing, resizing (and any other operation that you’ve always been able to do to any other Classic Windows application window) is now possible.

## Manifestations

The most noticeable change now is that you can get sized to arbitrary sizes that are not just the size of the screen/height of the screen. A user can continuously resize the app window to their liking (down to the app’s minimal window size). This is different from Windows 8.0 or Windows 8.1, where the act of resizing a window was a discrete action (users resized a thumbnail of the window, which then caused the window to resize once the user committed the action). Today instead when the user drags the window by the bottom corner (or other border location) it is a continuous resize, and the app receives resize messages in a row, rather than size change.

## Mitigations

To mitigate this for Windows 8.0 and 8.1 apps:

-   If the expected feature within the app functionality is broken, then the user mitigation is to place the app into full screen mode (by using the “go full screen button” in the upper right corner of the title bar).
-   If app start-up is impacted that it does not open as expected, then the user should still be able to switch to Tablet Mode to force the app to start in full-screen mode without user intervention.

The best way to handle this is to change the app to be aware of the fact that it can be sized to non-monitor sized places/heights (i.e. don’t have a hardcoded table of height/widths and only expect those, or expect hardcoded ratios as well). App developers should expect that as the app is being resized, that another resizing message can happen right after the current resize message gets delivered – as a result, if the app starts animations during resize, it’s possible that the app may receive another resize message right after (so it’s important to ensure that this type of situation doesn’t lead to the app crashing).

 

 





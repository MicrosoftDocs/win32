---
Description: The following table describes on which threads the InkOverlay object events can fire.EventThreadsCursorButtonDownFires on the ink threadCursorButtonUpFires on the ink threadCursorDownFires on the ink threadCursorInRangeFires on the ink threadCursorOutOfRangeFires on the ink threadDoubleClick (Automation only).Fires on the applications user interface (UI) threadDoubleClick (Managed Library only).Fires on the applications UI threadGestureFires on the ink threadMouseDownFires on the applications UI threadMouseMoveFires on the applications UI threadMouseUpFires on the applications UI threadMouseWheelFires on the applications UI threadNewInAirPacketsFires on the ink threadNewPacketsFires on the ink threadPaintedFires on the applications UI threadPaintingFires on the applications UI threadSelectionChangedFires on the ink thread, or on the thread which updates the InkOverlay objects Selection propertySelectionChangingFires on the ink threadSelectionMovedFires on the ink threadSelectionMovingFires on the ink threadSelectionResizedFires on the ink threadSelectionResizingFires on the ink threadStrokeFires on the ink threadStrokesDeletedFires on the ink threadStrokesDeletingFires on the ink threadSystemGestureFires on the ink threadTabletAddedFires on the ink threadTabletRemovedFires on the ink thread
ms.assetid: 5d679e66-6ea1-491e-86a8-974c4ec61b96
title: InkOverlay Object Events
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# InkOverlay Object Events

The following table describes on which threads the [**InkOverlay**](/windows/win32/msinkaut/?branch=master) object events can fire.



| Event                                                                             | Threads                                                                                                                                                                   |
|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CursorButtonDown**](inkoverlay-cursorbuttondown.md)                           | Fires on the ink thread<br/>                                                                                                                                        |
| [**CursorButtonUp**](inkoverlay-cursorbuttonup.md)                               | Fires on the ink thread<br/>                                                                                                                                        |
| [**CursorDown**](inkoverlay-cursordown.md)                                       | Fires on the ink thread<br/>                                                                                                                                        |
| [**CursorInRange**](inkoverlay-cursorinrange.md)                                 | Fires on the ink thread<br/>                                                                                                                                        |
| [**CursorOutOfRange**](inkoverlay-cursoroutofrange.md)                           | Fires on the ink thread<br/>                                                                                                                                        |
| [**DoubleClick**](inkoverlay-doubleclick.md) (Automation only).                  | Fires on the application's user interface (UI) thread<br/>                                                                                                          |
| [**DoubleClick**](E:Microsoft.Ink.InkOverlay.DoubleClick) (Managed Library only). | Fires on the application's UI thread<br/>                                                                                                                           |
| [**Gesture**](inkoverlay-gesture.md)                                             | Fires on the ink thread<br/>                                                                                                                                        |
| [**MouseDown**](inkoverlay-mousedown.md)                                         | Fires on the application's UI thread<br/>                                                                                                                           |
| [**MouseMove**](inkoverlay-mousemove.md)                                         | Fires on the application's UI thread<br/>                                                                                                                           |
| [**MouseUp**](inkoverlay-mouseup.md)                                             | Fires on the application's UI thread<br/>                                                                                                                           |
| [**MouseWheel**](inkoverlay-mousewheel.md)                                       | Fires on the application's UI thread<br/>                                                                                                                           |
| [**NewInAirPackets**](inkoverlay-newinairpackets.md)                             | Fires on the ink thread<br/>                                                                                                                                        |
| [**NewPackets**](inkoverlay-newpackets.md)                                       | Fires on the ink thread<br/>                                                                                                                                        |
| [**Painted**](inkoverlay-painted.md)                                             | Fires on the application's UI thread<br/>                                                                                                                           |
| [**Painting**](inkoverlay-painting.md)                                           | Fires on the application's UI thread<br/>                                                                                                                           |
| [**SelectionChanged**](inkoverlay-selectionchanged.md)                           | Fires on the ink thread, or on the thread which updates the [**InkOverlay**](/windows/win32/msinkaut/?branch=master) object's [**Selection**](/windows/win32/msinkaut/?branch=master) property<br/> |
| [**SelectionChanging**](inkoverlay-selectionchanging.md)                         | Fires on the ink thread<br/>                                                                                                                                        |
| [**SelectionMoved**](inkoverlay-selectionmoved.md)                               | Fires on the ink thread<br/>                                                                                                                                        |
| [**SelectionMoving**](inkoverlay-selectionmoving.md)                             | Fires on the ink thread<br/>                                                                                                                                        |
| [**SelectionResized**](inkoverlay-selectionresized.md)                           | Fires on the ink thread<br/>                                                                                                                                        |
| [**SelectionResizing**](inkoverlay-selectionresizing.md)                         | Fires on the ink thread<br/>                                                                                                                                        |
| [**Stroke**](inkoverlay-stroke.md)                                               | Fires on the ink thread<br/>                                                                                                                                        |
| [**StrokesDeleted**](inkoverlay-strokesdeleted.md)                               | Fires on the ink thread<br/>                                                                                                                                        |
| [**StrokesDeleting**](inkoverlay-strokesdeleting.md)                             | Fires on the ink thread<br/>                                                                                                                                        |
| [**SystemGesture**](inkoverlay-systemgesture.md)                                 | Fires on the ink thread<br/>                                                                                                                                        |
| [**TabletAdded**](inkoverlay-tabletadded.md)                                     | Fires on the ink thread<br/>                                                                                                                                        |
| [**TabletRemoved**](inkoverlay-tabletremoved.md)                                 | Fires on the ink thread<br/>                                                                                                                                        |



 

 

 





---
title: Carets
description: This section discusses carets which are blinking lines, blocks, or bitmaps in the client area of a window.
ms.assetid: '4487c93c-9a0f-467c-86b1-969f664d5526'
keywords: ["resources,carets", "carets,about", "blinking lines", "blinking blocks", "blinking bitmaps"]
---

# Carets

A *caret* is a blinking line, block, or bitmap in the client area of a window. The caret typically indicates the place at which text or graphics will be inserted.

The following illustration shows some common variations in the appearance of the caret.

![](images/cscrt-01.png)

Applications can create a caret, change its blink time, and display, hide, or relocate the caret.

### In This Section



| Name                                   | Description                                                               |
|----------------------------------------|---------------------------------------------------------------------------|
| [About Carets](about-carets.md)       | Discusses carets.<br/>                                              |
| [Using Carets](using-carets.md)       | Code samples that show how to perform tasks related to carets.<br/> |
| [Caret Reference](caret-reference.md) | Contains the API reference.<br/>                                    |



 

### Caret Functions



| Name                                           | Description                                                                                                                                                                                                                                                   |
|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateCaret**](createcaret.md)             | Creates a new shape for the system caret and assigns ownership of the caret to the specified window. The caret shape can be a line, a block, or a bitmap. <br/>                                                                                         |
| [**DestroyCaret**](destroycaret.md)           | Destroys the caret's current shape, frees the caret from the window, and removes the caret from the screen. <br/>                                                                                                                                       |
| [**GetCaretBlinkTime**](getcaretblinktime.md) | Retrieves the time required to invert the caret's pixels. The user can set this value. <br/>                                                                                                                                                            |
| [**GetCaretPos**](getcaretpos.md)             | Copies the caret's position to the specified [**POINT**](https://msdn.microsoft.com/library/windows/desktop/dd162805) structure. <br/>                                                                                                                                                                    |
| [**HideCaret**](hidecaret.md)                 | Removes the caret from the screen. Hiding a caret does not destroy its current shape or invalidate the insertion point. <br/>                                                                                                                           |
| [**SetCaretBlinkTime**](setcaretblinktime.md) | Sets the caret blink time to the specified number of milliseconds. The blink time is the elapsed time, in milliseconds, required to invert the caret's pixels. <br/>                                                                                    |
| [**SetCaretPos**](setcaretpos.md)             | Moves the caret to the specified coordinates. If the window that owns the caret was created with the **CS\_OWNDC** class style, then the specified coordinates are subject to the mapping mode of the device context associated with that window. <br/> |
| [**ShowCaret**](showcaret.md)                 | Makes the caret visible on the screen at the caret's current position. When the caret becomes visible, it begins flashing automatically. <br/>                                                                                                          |



 

 

 






---
title: Saving Recorded Content
description: Saving Recorded Content
ms.assetid: 0c159c44-f96c-4c08-bd3f-9e65b413026c
keywords:
- MCIWndSave macro
- MCIWndSaveDialog macro
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Saving Recorded Content

\[The feature associated with this page, [MCIWnd Window Class](/windows/win32/multimedia/mciwnd-window-class), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCIWnd Window Class**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

After completing the recording, you can save the content by using the [**MCIWndSave**](/windows/desktop/api/Vfw/nf-vfw-mciwndsave) or [**MCIWndSaveDialog**](/windows/desktop/api/Vfw/nf-vfw-mciwndsavedialog) macro, or by using the [**GetSaveFileNamePreview**](/windows/desktop/api/Vfw/nf-vfw-getsavefilenamepreviewa) function with **MCIWndSave**. The **MCIWndSave** macro saves data in the file associated with the MCIWnd window. The **MCIWndSaveDialog** macro lets the user specify a filename and save the recorded data in the specified file. The **GetSaveFileNamePreview** function displays the **SaveAs** dialog box for choosing a file and lets the user preview (play) the file. When the name of an existing file is specified in the **SaveAs** dialog box, **GetSaveFileNamePreview** provides a small control in the dialog box to let the user preview the contents of the file. You can save the recorded data in a file selected with **GetSaveFileNamePreview** by using **MCIWndSave**.

 

 





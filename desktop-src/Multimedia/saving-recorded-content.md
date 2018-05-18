---
title: Saving Recorded Content
description: Saving Recorded Content
ms.assetid: '0c159c44-f96c-4c08-bd3f-9e65b413026c'
keywords: ["MCIWndSave macro", "MCIWndSaveDialog macro"]
---

# Saving Recorded Content

After completing the recording, you can save the content by using the [**MCIWndSave**](mciwndsave.md) or [**MCIWndSaveDialog**](mciwndsavedialog.md) macro, or by using the [**GetSaveFileNamePreview**](getsavefilenamepreview.md) function with **MCIWndSave**. The **MCIWndSave** macro saves data in the file associated with the MCIWnd window. The **MCIWndSaveDialog** macro lets the user specify a filename and save the recorded data in the specified file. The **GetSaveFileNamePreview** function displays the **SaveAs** dialog box for choosing a file and lets the user preview (play) the file. When the name of an existing file is specified in the **SaveAs** dialog box, **GetSaveFileNamePreview** provides a small control in the dialog box to let the user preview the contents of the file. You can save the recorded data in a file selected with **GetSaveFileNamePreview** by using **MCIWndSave**.

 

 





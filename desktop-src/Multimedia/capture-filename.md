---
title: Capture Filename
description: Capture Filename
ms.assetid: b17ecdd4-899e-4e94-98f2-496f93491e06
keywords:
- WM_CAP_FILE_SET_CAPTURE_FILE message
- capFileSetCaptureFile macro
- WM_CAP_FILE_GET_CAPTURE_FILE message
- capFileGetCaptureFile macro
ms.topic: article
ms.date: 05/31/2018
---

# Capture Filename

AVICap, by default, routes video and audio stream data from a capture window to a file named CAPTURE.AVI in the root directory of the current drive. You can specify an alternate filename by sending the [**WM\_CAP\_FILE\_SET\_CAPTURE\_FILE**](wm-cap-file-set-capture-file.md) message (or the [**capFileSetCaptureFile**](/windows/desktop/api/Vfw/nf-vfw-capfilesetcapturefile) macro) to a capture window. This message specifies the filename; it does not create, allocate, or open the file. You can retrieve the current capture filename by sending the [**WM\_CAP\_FILE\_GET\_CAPTURE\_FILE**](wm-cap-file-get-capture-file.md) message (or the [**capFileGetCaptureFile**](/windows/desktop/api/Vfw/nf-vfw-capfilegetcapturefile) macro) to a capture window.

 

 





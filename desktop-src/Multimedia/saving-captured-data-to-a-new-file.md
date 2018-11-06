---
title: Saving Captured Data to a New File
description: Saving Captured Data to a New File
ms.assetid: 2e6db328-c45e-4a98-9d21-f3c9da261f44
keywords:
- WM_CAP_FILE_SAVEAS message
- capFileSaveAs macro
ms.topic: article
ms.date: 05/31/2018
---

# Saving Captured Data to a New File

If the user wants to save captured data, the application should save the contents of the capture file to another file by using the [**WM\_CAP\_FILE\_SAVEAS**](wm-cap-file-saveas.md) message (or the [**capFileSaveAs**](/windows/desktop/api/Vfw/nf-vfw-capfilesaveas) macro). This message does not change the name or contents of the capture file. Your application must specify a name for the new file because the capture file retains its original filename.

Typically, a capture file is preallocated for the largest capture segment anticipated, and only a portion of it might be used to capture data. This message copies only the portion of the capture file containing the capture data.

 

 





---
title: Using the Download Manager
description: Using the Download Manager
ms.assetid: f332a981-727f-4abc-a84e-76ab3e72b7f2
keywords:
- Windows Media Player online stores,Download Manager
- online stores,Download Manager
- type 2 online stores,Download Manager
- Windows Media Player,Download Manager
- Windows Media Player Download Manager
- Download Manager
ms.topic: article
ms.date: 05/31/2018
---

# Using the Download Manager

The Windows Media Player SDK includes a sample webpage that demonstrates using the Download Manager to download files to the user's computer. You can locate the sample in the folder named WebPage where you installed the SDK. The name of the file is sample.asp. The sample provides the following functionality:

-   Creates the **DownloadManager** object.
-   Creates a **DownloadCollection** object.
-   Starts downloading five files when the user clicks **Download**. Default file paths are provided in the sample. You should replace these default paths with the locations of files on your own server. You can change the paths by changing the values assigned to the global array named g\_sFiles.
-   Shows status information for a download when the user selects it.
-   Provides controls to pause, resume, cancel, and remove a download item.
-   Maintains information about download collections between sessions by using cookies. This is important because the user can close the Player at any time. Also, if the user switches task panes in the Player, the online store session ends.
-   Uses real-time downloading by default. You can change the behavior to background downloading by changing the value of the variable named g\_sDLType. Background downloading is available for use with the Microsoft Windows XP operating system.
-   Synchronizes the background color with the Player color. You can use this feature to make your online store change appearance when the user chooses to change the color of the Player.

The following sections provide more information:

-   [Initializing the Page](initializing-the-page.md)
-   [Starting the Downloads](starting-the-downloads.md)
-   [Retrieving Status Information](retrieving-status-information.md)
-   [Maintaining Session Information](maintaining-session-information.md)
-   [Debugging the Page](debugging-the-page.md)

## Related topics

<dl> <dt>

[**Programming Guide for Type 2 Online Stores**](programming-guide-for-type-2-online-stores.md)
</dt> </dl>

 

 





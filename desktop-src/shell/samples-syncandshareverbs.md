---
description: Demonstrates how to register a verb that extends the &\#0034;Sync&\#0034; and &\#0034;Share&\#0034; verbs in the Windows Explorer Command Bar.
title: Sync and Share Verbs
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 78267C74-7597-4b98-9DAE-89F2FD515C6B
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Sync and Share Verbs

Demonstrates how to register a verb that extends the "Sync" and "Share" verbs in the Windows Explorer Command Bar.

This topic contains the following sections.

-   [Requirements](#requirements)
-   [Downloading the Sample](#downloading-the-sample)
-   [Running the Sample](#running-the-sample)
-   [Removing the Sample](#removing-the-sample)

## Requirements



| Product                                | Minimum Product Version |
|----------------------------------------|-------------------------|
| Windows                                | Windows 7               |
| Windows Software Development Kit (SDK) | 7.0                     |



 

## Downloading the Sample

| Location      | Path URL                                                                                             |
|---------------|------------------------------------------------------------------------------------------------------|
| GitHub  | [SyncAndShareVerbs sample](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/winui/shell/appshellintegration/SyncAndShareVerbs) |

## Running the Sample

To run the sample (sync):

1.  Navigate to the directory that contains the `sync.reg` file
2.  Type `sync.reg ` at the command line, or double-click the icon for `sync.reg` register it.
3.  Open the Windows Explorer and select a file.
4.  Click the **Sync** option in the Command Bar and select a suboption such as **Paint**.

To run the sample (share):

1.  Navigate to the directory that contains the `share.reg` file.
2.  Type `share.reg` at the command line, or double-click the icon for `share.reg` register it.
3.  Open Windows Explorer and select a file. Click the **Share** option in the Command Bar.
4.  Click the **Share with** option in the Command Bar and select a suboption such as **Paint**.

## Removing the Sample

To remove the sample (sync):

1.  Navigate to the directory that contains the Uninstallsync.reg file.
2.  Type `uninstallsync.reg` at the command line, or double-click the icon for `uninstallsync.reg`.

To remove the sample (share):

1.  Navigate to the directory that contains the Uninstallshare.reg file.
2.  Type `uninstallshare.reg` at the command line, or double-click the icon for `uninstallshare.reg.`

 

 




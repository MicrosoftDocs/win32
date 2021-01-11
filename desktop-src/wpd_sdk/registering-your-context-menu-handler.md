---
description: Registering Your Context Menu Handler
ms.assetid: 0023004b-b6b3-486a-8b8c-8e63c5731206
title: Registering Your Context Menu Handler
ms.topic: article
ms.date: 05/31/2018
---

# Registering Your Context Menu Handler

In order for your context menu handler to be recognized by the WPD namespace you must register it properly in the Windows registry. The registration entries for a WPD context menu handler are similar to those for the shell, but they are registered as special file types. WPD context menu handlers are registered according to the content type they represent. Below is a sample registration tree for a WPD context menu handler:


```C++
HKEY_CLASSES_ROOT
 \-- WPDContextMenu.Image
      \-- shellex
           \-- ContextMenuHandlers
                \-- ShImageViewer (Default)  REG_SZ {E847DA7C-1D6A-45F6-B725-CB260C236066}

```



The above example registers the shell image viewer with the WPD namespace. When a user right-clicks or double-clicks content on a device through the Windows Vista Shell, it invokes this context menu handler. The WPD namespace uses WPD\_CONTENT\_TYPE to determine which context menu handlers to load. If WPD\_CONTENT\_TYPE is equal to WPD\_CONTENT\_TYPE\_UNSPECIFIED, WPD\_CONTENT\_TYPE\_GENERIC\_FILE or WPD\_CONTENT\_TYPE\_PROGRAM, then the WPD namespace will try to find the best match based on the extension of the selected file. If neither the file extension nor the content type provides a useful classification, the WPD namespace will load the context menu handlers under the **WPDContextMenu.Generic** registry key. The following table lists all of the file classes available to a context menu handler and what content types and file extensions they represent:



| Registry Key                           | WPD Content Type                                                                                               | File Extension                                                                                           |
|----------------------------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| **WPDContextMenu.Device**              | Registering under this key enables your context menu handler at the device level. (Right-click on a device.)   | (N/A)                                                                                                    |
| **WPDContextMenu.Storage**             | Registering under this key enables your context menu handler at the storage level. (Right-click on a storage.) | (N/A)                                                                                                    |
| **WPDContextMenu.Folder**              | WPD\_CONTENT\_TYPE\_FOLDER                                                                                     | (N/A)                                                                                                    |
| **WPDContextMenu.Image**               | WPD\_CONTENT\_TYPE\_IMAGE                                                                                      | .bmp <br/> .gif <br/> .png <br/> .jpg <br/> .jpe <br/> .jpeg <br/>   |
| **WPDContextMenu.Audio**               | WPD\_CONTENT\_TYPE\_AUDIO                                                                                      | .aiff <br/> .mp3 <br/> .wav <br/> .wma <br/>                                     |
| **WPDContextMenu.Video**               | WPD\_CONTENT\_TYPE\_VIDEO                                                                                      | .asf<br/> .avi <br/> .dvr-ms <br/> .mpeg <br/> .mpg <br/> .wmv <br/> |
| **WPDContextMenu.Playlist**<br/> | WPD\_CONTENT\_TYPE\_PLAYLIST                                                                                   | .wpl <br/> .m3u <br/> .mpl <br/> .asx <br/> .pls <br/>                     |
| **WPDContextMenu.Document**            | WPD\_CONTENT\_TYPE\_DOCUMENT                                                                                   | .doc <br/> .txt <br/> .rtf <br/> .xls <br/> .ppt <br/>                     |
| **WPDContextMenu.Contact**<br/>  | WPD\_CONTENT\_TYPE\_CONTACT                                                                                    | None                                                                                                     |
| **WPDContextMenu.Email**               | WPD\_CONTENT\_TYPE\_EMAIL                                                                                      | None                                                                                                     |
| **WPDContextMenu.Appointment**         | WPD\_CONTENT\_TYPE\_APPOINTMENT                                                                                | None                                                                                                     |
| **WPDContextMenu.Task**                | WPD\_CONTENT\_TYPE\_TASK                                                                                       | None                                                                                                     |
| **WPDContextMenu.Memo**                | WPD\_CONTENT\_TYPE\_MEMO                                                                                       | None                                                                                                     |
| **WPDContextMenu.ImageAlbum**          | WPD\_CONTENT\_TYPE\_IMAGE\_ALBUM                                                                               | None                                                                                                     |
| **WPDContextMenu.AudioAlbum**          | WPD\_CONTENT\_TYPE\_AUDIO\_ALBUM                                                                               | None                                                                                                     |
| **WPDContextMenu.VideoAlbum**          | WPD\_CONTENT\_TYPE\_VIDEO\_ALBUM                                                                               | None                                                                                                     |
| **WPDContextMenu.MixedAlbum**          | WPD\_CONTENT\_TYPE\_MIXED\_CONTENT\_ALBUM                                                                      | None                                                                                                     |
| **WPDContextMenu.Generic**             | WPD\_CONTENT\_TYPE\_UNSPECIFIED                                                                                | All other file extensions                                                                                |



 

 

 





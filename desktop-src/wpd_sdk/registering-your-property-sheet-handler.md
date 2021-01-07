---
description: Registering Your Property Sheet Handler
ms.assetid: 6621529c-717b-4f36-8d9e-769d6b720b8a
title: Registering Your Property Sheet Handler
ms.topic: article
ms.date: 05/31/2018
---

# Registering Your Property Sheet Handler

In order for your property sheet handler to be recognized by the WPD namespace you must register it properly in the Windows registry. The registration entries for a WPD property sheet handler are similar to those for the shell, but they are registered as special file types. WPD property sheet handlers are registered according to the content type they represent. Below is a sample registration tree for a WPD context menu handler:


```C++
HKEY_CLASSES_ROOT
 \-- WPDPropSheet.Image
      \-- shellex
           \-- PropertySheetHandlers
                \-- MyHandler (Default)  REG_SZ {0000000-0000-0000-0000-000000000000}

```



The above example registers a custom handler with the WPD namespace. When a user right-clicks an image file on a device through the Windows Shell and selects **Properties**, it invokes this property sheet handler. The WPD namespace uses the WPD\_CONTENT\_TYPE to determine which property sheet handlers to load. If the content type does not provide a useful classification, then the namespace will load the property sheet handlers under the **WPDPropSheet.Generic registry** key. The following table lists all of the file classes available to a context menu handler and what content types and file extensions they represent.



| Registry Key                   | WPD Content Type                                                                                                               |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| **WPDContextMenu.Device**      | Registering under this key enables your context menu handler at the device level. (Right-click on a device.)                   |
| **WPDContextMenu.Storage**     | Registering under this key enables your context menu handler at the storage level. (Right-click on a storage.)                 |
| **WPDContextMenu.Folder**      | WPD\_CONTENT\_TYPE\_FOLDER                                                                                                     |
| **WPDContextMenu.Image**       | WPD\_CONTENT\_TYPE\_IMAGE                                                                                                      |
| **WPDContextMenu.Audio**       | WPD\_CONTENT\_TYPE\_AUDIO                                                                                                      |
| **WPDContextMenu.Video**       | WPD\_CONTENT\_TYPE\_VIDEO                                                                                                      |
| **WPDContextMenu.Playlist**    | WPD\_CONTENT\_TYPE\_PLAYLIST                                                                                                   |
| **WPDContextMenu.Document**    | WPD\_CONTENT\_TYPE\_DOCUMENT                                                                                                   |
| **WPDContextMenu.Contact**     | WPD\_CONTENT\_TYPE\_CONTACT                                                                                                    |
| **WPDContextMenu.Email**       | WPD\_CONTENT\_TYPE\_EMAIL                                                                                                      |
| **WPDContextMenu.Appointment** | WPD\_CONTENT\_TYPE\_APPOINTMENT                                                                                                |
| **WPDContextMenu.Task**        | WPD\_CONTENT\_TYPE\_TASK                                                                                                       |
| **WPDContextMenu.Memo**        | WPD\_CONTENT\_TYPE\_MEMO                                                                                                       |
| **WPDContextMenu.ImageAlbum**  | WPD\_CONTENT\_TYPE\_IMAGE\_ALBUM                                                                                               |
| **WPDContextMenu.AudioAlbum**  | WPD\_CONTENT\_TYPE\_AUDIO\_ALBUM                                                                                               |
| **WPDContextMenu.VideoAlbum**  | WPD\_CONTENT\_TYPE\_VIDEO\_ALBUM                                                                                               |
| **WPDContextMenu.MixedAlbum**  | WPD\_CONTENT\_TYPE\_MIXED\_CONTENT\_ALBUM                                                                                      |
| **WPDContextMenu.Generic**     | WPD\_CONTENT\_TYPE\_UNSPECIFIED<br/> WPD\_CONTENT\_TYPE\_GENERIC\_FILE<br/> WPD\_CONTENT\_TYPE\_PROGRAM<br/> |



 

 

 





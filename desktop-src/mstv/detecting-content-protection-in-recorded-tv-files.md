---
title: Detecting Content Protection in Recorded TV Files
description: Detecting Content Protection in Recorded TV Files
ms.assetid: 534eab34-736f-4073-bb8f-d27ee240b6e1
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Detecting Content Protection in Recorded TV Files

This topic describes how an application can detect whether a recorded television file contains protected content, which might limit the ability of the user to play the file on another computer or after a certain period of time.

Windows Media Center Edition can record broadcast television in the form of DVR-MS files. If a recording contains protected content, Windows Media Center limits the ability to play the recording on computers other than the one that made the original recording. In addition, some content might have a time limit, past which the recording cannot be played on any computer. Content protection is enforced by encrypting the protected content. Even when DVR-MS files contain protected content, however, they can be freely copied to other computers—for example, to create backup copies. The copy cannot be played on the other computer until it is copied back to the original computer.

In broadcast television, content protection might not be indicated until the recording has already started. The protection state can also switch off and on during the broadcast. Therefore, a DVR-MS file might contain a mix of protected and unprotected content.

The DVR-MS file format is packetized, and content protection is applied to each packet individually. However, it would be time consuming and impractical for an application to scan the entire file looking for the protection status of each packet. For this reason, the content header contains metadata that provides a summary of the overall content protection.

**Content Protection Attributes**

To get the attributes from a DVR-MS file, do the following:

1.  Create the Stream Buffer Engine (SBE) recording attributes object and retrieve the [**IFileSourceFilter**](https://msdn.microsoft.com/library/windows/desktop/dd389981) interface.
2.  Call [**IFileSourceFilter::Load**](https://msdn.microsoft.com/library/windows/desktop/dd389983) with the name of the DVR-MS file.
3.  Query the recording attributes object for [**IStreamBufferRecordingAttribute**](istreambufferrecordingattribute.md) interface.
4.  Use the **IStreamBufferRecordingAttribute** interface to retrieve the attributes.

The main attribute that applications should check is the [**WM/WMRVContentProtected**](wm-wmrvcontentprotected.md) attribute. Windows Media Center sets this attribute to **TRUE** if more than 5 minutes of the file is protected, or more than 5 percent of the total file is protected. Other content protection attributes include the following:

-   [**WM/WMRVContentProtectedPercent**](wm-wmrvcontentprotectedpercent.md): Specifies the total percentage of the file that is protected.
-   [**WM/WMRVExpirationDate**](wm-wmrvexpirationdate.md): Specifies the expiration date for the file.

> [!Note]  
> When DVR-MS files were first introduced, the file format was very similar to Advanced Systems Format (ASF). This made it possible to retrieve DVR-MS attributes using the Windows Media Format SDK. However, that approach is not guaranteed to work in the future. Applications should always use the **IStreamBufferRecordingAttribute** interface to retrieve attributes from DVR-MS files.

 

**Content Protection Events**

The content protection attributes do not describe the protection status of individual packets in the file. Applications that use the Video Control to play DVR-MS files should use the [**IBroadcastEventEx**](ibroadcasteventex.md) interface to subscribe to broadcast events. If playback reaches a section of protected content, the application receives an **EVENTID\_EncDecFilterEvent** event. The data associated with this event is a member of the [**CPEvents**](cpevents.md) enumeration. After that, if playback reaches a section of unprotected content, the application receives another **EVENTID\_EncDecFilterEvent** event, with the value CPEVENT\_NONE. For more information, see [**TV Ratings Broadcast Events**](tv-ratings-broadcast-events.md).

## Related topics

<dl> <dt>

[Overview of Microsoft TV Technologies](overview-of-microsoft-tv-technologies.md)
</dt> </dl>

 

 





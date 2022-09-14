---
title: Burning Playlists That Contain Secure Files
description: Burning Playlists That Contain Secure Files
ms.assetid: 0d9415a1-a154-4fe4-af4c-cce4cb05ade5
keywords:
- Windows Media Format SDK,burning playlists with secure files
- Windows Media Format SDK,playlists with secure files
- Advanced Systems Format (ASF),burning playlists with secure files
- ASF (Advanced Systems Format),burning playlists with secure files
- Advanced Systems Format (ASF),playlists with secure files
- ASF (Advanced Systems Format),playlists with secure files
- digital rights management (DRM),burning playlists with secure files
- DRM (digital rights management),burning playlists with secure files
- digital rights management (DRM),playlists with secure files
- DRM (digital rights management),playlists with secure files
ms.topic: article
ms.date: 05/31/2018
---

# Burning Playlists That Contain Secure Files

Licenses created by using the objects of the Windows Media Rights Manager 10 SDK can specify the right to copy a file to compact disc as part of a playlist. This feature, called playlist burning, requires that you verify the licenses of all of the files in the playlist before starting to copy data. The Windows Media Format SDK provides the [**IWMReaderPlaylistBurn**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderplaylistburn) interface to perform file verification for you.

To implement playlist burning, perform the following steps:

1.  Create an instance of the reader object, or the synchronous reader object. For more information, see [Reading ASF Files](reading-asf-files.md).
2.  Call the **QueryInterface** method of the reader interface ([**IWMReader**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreader) or [**IWMSyncReader**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmsyncreader)) to obtain a pointer to the [**IWMReaderPlaylistBurn**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderplaylistburn) interface.
3.  Copy the file names from the playlist into an array of wide-character strings. The file names in the array must be in the same order as they appear in the playlist.
4.  Call the [**IWMReaderPlaylistBurn::InitPlaylistBurn**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderplaylistburn-initplaylistburn) method, passing in a pointer to the array created in step 3, to initialize the license verification for the files.
5.  When the license verification is completed, the reader object sends a WMT\_INIT\_PLAYLIST\_BURN message to your implementation of the [**IWMStatusCallback::OnStatus**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstatuscallback-onstatus) callback method. When your callback receives this message, call the [**IWMReaderPlaylistBurn::GetInitResults**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderplaylistburn-getinitresults) method to get the results of the license check. This method takes an array of **HRESULT** variables that correspond to the file names in the array passed to **InitPlaylistBurn**. If all of the values in the result array are equal to S\_OK, you can continue. If any result is an error code, the playlist must not be copied.
6.  Using the same instance of the reader, open and read each file. You must open the files in the order in which the file names appeared in the file name array passed to **InitPlaylistBurn**.
7.  When you have copied all of the files in the playlist, call the [**IWMReaderPlaylistBurn::EndPlaylistBurn**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderplaylistburn-endplaylistburn) to complete the playlist burn process and free the resources used by the reader.

> [!Note]  
> DRM is not supported by the x64-based version of this SDK.

 

## Related topics

<dl> <dt>

[**Enabling DRM Support**](enabling-drm-support.md)
</dt> </dl>

 

 





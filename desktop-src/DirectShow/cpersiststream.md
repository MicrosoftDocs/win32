---
description: CPersistStream is the base class for persistent properties of filters (that is, filter properties in saved graphs).
ms.assetid: 8073e2be-aaf9-4b01-a7d5-bab5c1dcc19b
title: CPersistStream class
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPersistStream
api_type: 
- COM
api_location: 
ms.custom: UpdateFrequency5
---

# CPersistStream class

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

![cpersiststream class hierarchy](images/pstrm01.png)

`CPersistStream` is the base class for persistent properties of filters (that is, filter properties in saved graphs).

The simplest way to use `CPersistStream` is to:

1.  Arrange for your filter to inherit this class.
2.  Implement [**WriteToStream**](cpersiststream-writetostream.md) and [**ReadFromStream**](cpersiststream-readfromstream.md) in your class. These will override the functions here, which do nothing but act as placeholders.
3.  Change your **NonDelegatingQueryInterface** to handle **IPersistStream**.
4.  Implement [**SizeMax**](cpersiststream-sizemax.md) to return an upper bound on the number of bytes of data you save.

    If you save Unicode™ data, remember that a WCHAR is 2 bytes.

5.  When your data changes, call [**SetDirty**](cpersiststream-setdirty.md).

## Version Numbers

At some point you might decide to alter or extend the format of your data. You will then wish you had a version number in all the old saved streams so you can tell, when you read them, whether they represent the old or new form. To assist you, this class writes and reads a version number. When it writes, it calls [**GetSoftwareVersion**](cpersiststream-getsoftwareversion.md) to inquire as to the version of the software being used at the moment. (In effect, this is a version number of the data layout in the file.) It writes this as the first thing in the data. If you want to change the version, implement (override) **GetSoftwareVersion**. It reads the version number from the file into **mPS\_dwFileVersion** before calling [**ReadFromStream**](cpersiststream-readfromstream.md), so in **ReadFromStream** you can check **mPS\_dwFileVersion** to see if you are reading an old version file. Usually you should accept files whose version is no newer than the software version that is reading them.

**CPersistStream** implements [**IPersistStream**](/windows/desktop/api/objidl/nn-objidl-ipersiststream). For more implementation information, see the COM Reference in the Microsoft Platform SDK.



| Protected Data Members                                          | Description                                                                   |
|-----------------------------------------------------------------|-------------------------------------------------------------------------------|
| mPS\_dwFileVersion                                              | Version number of the file.                                                   |
| mPS\_fDirty                                                     | Data for this stream must be saved.                                           |
| Member Functions                                                | Description                                                                   |
| [**CPersistStream**](cpersiststream-cpersiststream.md)         | Constructs a **CPersistStream** object.                                       |
| [**SetDirty**](cpersiststream-setdirty.md)                     | Indicates that the object must be saved to the stream.                        |
| Overridable Member Functions                                    | Description                                                                   |
| [**GetClassID**](cpersiststream-getclassid.md)                 | Retrieves the class identifier of this stream.                                |
| [**GetSoftwareVersion**](cpersiststream-getsoftwareversion.md) | Retrieves the version number for this file format.                            |
| [**ReadFromStream**](cpersiststream-readfromstream.md)         | Reads the filter's data from the stream.                                      |
| [**SizeMax**](cpersiststream-sizemax.md)                       | Retrieves the number of bytes needed for data (not including version number). |
| [**WriteToStream**](cpersiststream-writetostream.md)           | Writes the filter's data to the stream.                                       |
| IPersistStream Methods                                          | Description                                                                   |
| [**GetSizeMax**](cpersiststream-getsizemax.md)                 | Retrieves the number of bytes needed for data (including version number).     |
| [**IsDirty**](cpersiststream-isdirty.md)                       | Checks if the object must be saved.                                           |
| [**Load**](cpersiststream-load.md)                             | Loads the data from the stream into memory.                                   |
| [**Save**](cpersiststream-save.md)                             | Saves the data from memory to the stream.                                     |



 

 

 

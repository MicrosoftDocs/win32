---
title: About Conversion Plug-ins
description: About Conversion Plug-ins
ms.assetid: bd6d1020-e8e1-492e-9c76-9f3cf04190de
keywords:
- Windows Media Player,conversion plug-ins
- Windows Media Player plug-ins,conversion
- plug-ins,conversion
- conversion plug-ins,about
- Advanced Systems Format (ASF)
- ASF (Advanced Systems Format)
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About Conversion Plug-ins

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can create a Windows Media Player plug-in to convert digital media files that are created using technologies not provided by Microsoft, into Advanced Systems Format (ASF).

Conversion plug-ins are Component Object Model (COM) objects that are packaged and distributed as executable (.exe) files. Windows Media Player instantiates conversion plug-ins to convert third-party digital media formats in the following scenarios:

-   Digital media content is copied to the computer from a portable device.
-   Digital media content is added to the library by using **IWMPMediaCollection::add**.
-   Digital media content is added to the library by using the search feature of Windows Media Player.
-   Digital media content is added to the library by the folder monitoring feature of Windows Media Player.
-   Digital media content is added to the sync list when the user drags and drops a file.

After Windows Media Player creates an instance of a conversion plug-in, the plug-in must convert the supplied file to ASF or WMA and add relevant metadata. (Do not use the conversion plug-in to transcode the file.) The plug-in must then copy the converted file to the specified folder and return the path to the new file to Windows Media Player.

Conversion plug-ins must implement the **IWMPConvert** interface. See [Conversion Plug-ins Programming Reference](conversion-plug-ins-programming-reference.md).

## Related topics

<dl> <dt>

[**About the Conversion Process**](about-the-conversion-process.md)
</dt> <dt>

[**Adding Metadata to Converted Files**](adding-metadata-to-converted-files.md)
</dt> <dt>

[**Windows Media Player Conversion Plug-ins**](windows-media-player-conversion-plug-ins.md)
</dt> </dl>

 

 





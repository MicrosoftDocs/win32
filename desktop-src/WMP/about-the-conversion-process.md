---
title: About the Conversion Process
description: About the Conversion Process
ms.assetid: 147b82fd-9e82-4acf-8f8a-43eb02e99024
keywords:
- Windows Media Player,conversion process
- Windows Media Player plug-ins,conversion
- plug-ins,conversion
- conversion plug-ins,process
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About the Conversion Process

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

After Windows Media Player instantiates the conversion plug-in, the process proceeds as follows:

1.  The Player calls [IWMPConvert::ConvertFile](/previous-versions/windows/desktop/api/wmpservices/nf-wmpservices-iwmpconvert-convertfile).
2.  The plug-in converts the file provided in the *bstrInputFile* parameter into an ASF format.
3.  If the conversion fails for some reason, the plug-in returns an appropriate failure code and the process stops.
4.  If the conversion succeeds, the plug-in places the converted file into the folder provided in the *bstrDestinationFolder* parameter and returns the fully qualified path to the converted file through the *pbstrOutputFile* parameter.
5.  The plug-in returns a success code from **ConvertFile**.
6.  The Player copies the converted file to a folder in the user's music folder hierarchy. Exactly where the Player copies the file to depends on content. As part of this process, the Player might rename the file.
7.  The Player copies the original (unconverted) file to a folder in the user's music folder hierarchy. As part of this process, the Player might rename the file. This is the copy of the file that the Player uses when the user syncs the content from the computer to a device that requires the original file format. This file is called a *shadow file*.
8.  The Player adds information about the converted file to the library. This includes setting the value for the **ShadowFilePath** attribute to the new location where the shadow file is saved.

If you need to work with the converted file, you can query the library to retrieve the content by using the **ContentDistributor** and **WM/UniqueFileIdentifier** attributes. If you need to work with the shadow file, you must still retrieve the **Media** object for the converted file and then query for the **ShadowFilePath** attribute. See [Adding Metadata to Converted Files](adding-metadata-to-converted-files.md).

## Related topics

<dl> <dt>

[**About Conversion Plug-ins**](about-conversion-plug-ins.md)
</dt> <dt>

[**Adding Metadata to Converted Files**](adding-metadata-to-converted-files.md)
</dt> <dt>

[**Reading Attribute Values**](reading-attribute-values.md)
</dt> <dt>

[**ShadowFilePath Attribute**](shadowfilepath-attribute.md)
</dt> <dt>

[**WM/ContentDistributor Attribute**](wm-contentdistributor-attribute.md)
</dt> <dt>

[**WM/UniqueFileIdentifier Attribute**](wm-uniquefileidentifier-attribute.md)
</dt> </dl>

 

 





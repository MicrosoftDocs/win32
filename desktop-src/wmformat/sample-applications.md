---
title: Windows Media Format SDK Sample Applications
description: Windows Media Format SDK Sample Applications
ms.assetid: '037741cb-c5fb-485f-bf62-79b5465abfe4'
keywords:
- Windows Media Format SDK,sample applications
- digital rights management (DRM),sample applications
- DRM (digital rights management),sample applications
ms.topic: article
ms.date: 05/31/2018
---

# Windows Media Format SDK Sample Applications

The sample code supplied with this SDK is in the form of projects for Microsoft Visual Studio 2005. Most of the samples are in C++, but ManagedWMFSDKWrapper and ManagedMetadataEdit require C#.

These samples will not work unless the Windows Media Format SDK or the Windows Player SDK has been installed.

Usage information for each sample is contained in a readme.txt file in each sample directory.




| Samle | Description | 
|-------|-------------|
| AudioPlayer | Plays Windows Media files including DRM-protected files. It is controlled through a GUI, and commands include Play, Pause, Seek and Stop. It can play local files or files read from the Internet (including those output to the Internet by using the WMVNetWrite sample).<blockquote>[!Note]<br />The DRM portions of this sample are not supported on x64-based versions of Windows.</blockquote><br /> | 
| DRMHeader | DRMHeader is a console application that uses the metadata editor's <a href="/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmdrmeditor"><strong>IWMDRMEditor</strong></a> interface to read DRM attributes of files without linking to the DRM static library.<blockquote>[!Note]<br />This sample is not supported on x64-based versions of Windows.</blockquote><br /> | 
| DRMShow | DRMShow is a console application that shows how to read <a href="wmformat-glossary.md"><em>DRM</em></a> properties of a Windows Media file using the <strong>IWMDRMReader::GetDRMProperty</strong> method.This sample demonstrates the use of the <strong>IWMDRMReader::GetDRMProperty</strong> method and the properties that can be retrieved from the DRM reader. It does not demonstrate how to acquire a license for DRM-protected content. This sample requires the DRM stub library WMStubDRM.lib to build.<br /><blockquote>[!Note]<br />This sample is not supported on x64-based versions of Windows.</blockquote><br /> When you acquire the WMStubDRM.lib from Microsoft, the library is assigned an application security level. If the security level of the library you receive is not sufficient to play a protected file, this sample will display an error.<br /> | 
| DirectShowInterop/DSCopy | Transcodes one or more files to an ASF file using the DirectShow  WM ASF Writer filter. The input file may be any compressed or uncompressed format supported by DirectShow. | 
| DirectShowInterop/DSPlay | This sample is an interactive audio/video media file player with <a href="wmformat-glossary.md"><em>DRM</em></a> support. It uses DirectShow's WM ASF Reader filter to play Windows Media files (ASF, WMA, WMV) without DRM protection and files which use DRM at a level of 100 or below. See readme.txt in the sample's directory for more information. | 
| DirectShowInterop/DSSeekFm | This sample demonstrates how to use the DirectShow WM ASF Reader Filter to play ASF content in a DirectShow filter graph, and also how to use the frame seeking support in the Windows Media Format SDK. | 
| Managed/WMFSDKWrapper | This managed assembly serves as a wrapper used by managed-code samples for accessing some metadata interfaces of this SDK. | 
| Managed/MetadataEdit | This C# application can be used to view and edit metadata from Windows Media files. | 
| MetaDataEdit | This is a C++ version of the Managed MetadataEdit application. | 
| ReadFromStream | This console application sample shows how to read data from <strong>IStream</strong> with WMReader. <strong>IStream</strong> source has been implemented to use a file in Windows Media Format (WMA/WMV/ASF).<blockquote>[!Note]<br />This sample does not show how to process the media samples coming out of WMReader. For examples on how to process audio/video or other types of media samples, please refer to other samples, for instance AudioPlayer, that are included with the Windows Media Format SDK.</blockquote><br /> | 
| UncompAVIToWMV | This console application sample shows the necessary code to compress an AVI file to a WMV file. It shows how to merge samples for audio and video streams from several AVI files and either merge these into similar streams or create a new stream based on the source stream profile. It also shows how to create an arbitrary stream, do multipass encoding, add SMPTE time code, and apply DRM version 1 protection. | 
| WMGenProfile/exe | This sample has been updated from the 7.1 release. It is now an MFC Dialog application. WMGenProfile sample demonstrates the use of the WMGenProfile static library. It also serves as a tool for the creation of profiles. This tool is meant for developers familiar with the Windows Media Format. The UI has not been tested for user experience and is not meant as a recommendation about how to present this information to a user. | 
| WMGenProfile/lib | The GenProfile library sample demonstrates the creation of profiles. It shows how to create media types and streams for various stream types (audio, video, script, image, file transfer, and Web). It does not demonstrate how to work with system profiles or how to convert system profiles to profiles that specify the Windows Media Audio and Video 9 Series codecs. | 
| WMProp | This console application demonstrates how to retrieve attributes by using the metadata editor object and profile information from the reader. | 
| WMStats | This console application displays Reader and Writer statistics. Multiple instances of WMStats can also be used concurrently on one machine. Start one instance as a server to send the stream to the network and then run a second instance as a client to verify that server is streaming correctly. | 
| WMSyncReader | This console application sample shows how to read a media file using <strong>IWMSyncReader</strong> without creating any extra thread or using callbacks. The following features are implemented :Reading compressed or decompressed samples<br /> Time-based seeking<br /> Frame-based seeking<br /><strong>IStream</strong> derived source<br /> | 
| WMVAppend | This console application takes two Windows Media files for input, and attempts to create an output file with the contents of the first followed by the second. The sample compares the profiles of the two input files to ensure they are similar enough to be appended. If this is not the case, an error message appears. For example, an error message occurs when one file is audio only and the second is an audio-video file, or when two audio files have different bit rates.The sample accepts variable bit rate (VBR) sources. However, when comparing the profiles of the two VBR sources, the sample ignores the average bit rate difference because two VBR streams will have different average bit rates even if they were created using the same profile. WMVAppend cannot compare the peak bit rate of unconstrained bit-rate-based VBR streams, or the quality level of quality-based VBR streams, because this information does not exist in the source files. It is therefore the user's responsibility to make sure that two source files are created using the same profile. Otherwise, invalid content can be created.<br /> | 
| WMVCopy | This sample shows the code necessary to copy a WMV file. It shows how to read and write compressed samples, read header attributes and scripts, and modify header attributes. | 
| WMVNetWrite | This console application shows how a Windows Media file is streamed across the Internet. The sample requires a port to be specified, and then the file can be played using a player. | 
| WMVRecompress | This console application shows how to recompress a WMV file. It demonstrates reading uncompressed samples, writing uncompressed samples, and doing multi-pass encoding, multi-channel output, and smart recompression. | 




 

## Related topics

<dl> <dt>

[**About the Windows Media Format SDK**](about-the-windows-media-format-sdk.md)
</dt> <dt>

[**Programming Guide**](programming-guide.md)
</dt> </dl>

 

 






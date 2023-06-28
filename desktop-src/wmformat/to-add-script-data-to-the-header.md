---
title: To Add Script Data to the Header
description: To Add Script Data to the Header
ms.assetid: 25f63d9e-c81a-4098-81d4-e848659a60e5
keywords:
- Windows Media Format SDK,adding script data to headers
- Advanced Systems Format (ASF),adding script data to headers
- ASF (Advanced Systems Format),adding script data to headers
- scripts,adding data to headers
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# To Add Script Data to the Header

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can include script commands in the header of an ASF file. To write script commands to the header at the time of encoding, perform the following steps. Perform these steps prior to calling [**IWMWriter::BeginWriting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-beginwriting).

1.  Obtain a pointer to the **IWMHeaderInfo** interface by calling **IWMWriter::QueryInterface**.
2.  Add each desired script command by calling [**IWMHeaderInfo::AddScript**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmheaderinfo-addscript). Each call takes the two strings separately and the presentation time to be used for the command as parameters.

When an application reads the file, it will need to retrieve all of the script commands. To find all script commands in the header of a file, perform the following steps. This should be done before starting playback.

1.  Obtain a pointer to the **IWMHeaderInfo** interface of the reader object (or synchronous reader object) by calling the **QueryInterface** method of another interface in the object.
2.  Get the total number of scripts in the header by calling [**IWMHeaderInfo::GetScriptCount**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmheaderinfo-getscriptcount).
3.  Loop through all of the scripts in the header one at a time using calls to [**IWMHeaderInfo::GetScript**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmheaderinfo-getscript).
4.  Create a list of the presentation times so that your application can react to the commands at the appropriate time.

> [!Note]  
> When using DRM to encrypt a file, no script command can have a presentation time of 0.

 

## Related topics

<dl> <dt>

[**IWMHeaderInfo Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmheaderinfo)
</dt> <dt>

[**IWMWriter Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriter)
</dt> <dt>

[**Using Script Commands**](using-script-commands.md)
</dt> </dl>

 

 





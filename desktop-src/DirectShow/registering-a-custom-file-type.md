---
description: This article describes how the Filter Graph Manager locates a source filter, given a file name.
ms.assetid: bc0d5719-6325-40fe-8261-ad00b91f272c
title: Registering a Custom File Type
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Registering a Custom File Type

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This article describes how the Filter Graph Manager locates a source filter, given a file name. You can use this mechanism to register your own custom file types. Once the file type is registered, DirectShow will automatically load the correct source filter whenever an application calls [**IGraphBuilder::RenderFile**](/windows/desktop/api/Strmif/nf-strmif-igraphbuilder-renderfile) or [**IGraphBuilder::AddSourceFilter**](/windows/desktop/api/Strmif/nf-strmif-igraphbuilder-addsourcefilter).

-   [Overview](#overview)
-   [Protocols](#protocols)
-   [File Extensions](#file-extensions)
-   [Check Bytes](#check-bytes)
-   [Loading the Source Filter](#loading-the-source-filter)
-   [Custom File Types in Windows Media Player](#custom-file-types-in-windows-media-player)
-   [Related topics](#related-topics)

## Overview

To locate a source filter from a given file name, the Filter Graph Manager attempts to do the following, in order:

1.  Match the protocol, if any.
2.  Match the file extension.
3.  Match patterns of bytes within the file, called *check bytes*.

## Protocols

Protocol names such as "ftp" or "http" are registered under the

**HKEY\_CLASSES\_ROOT**

key, with the following structure:


```C++
HKEY_CLASSES_ROOT
    <protocol>
        Source Filter = <Source filter CLSID>
        Extensions
            <.ext1> = <Source filter CLSID>
            <.ext2> = <Source filter CLSID>
```



If the file name or URL contains a colon (':'), the Filter Graph Manager attempts to use the portion before the ':' as a protocol name. For example, if the name is "myprot://myfile.ext", it searches for a registry key named **myprot**. If this key exists and contains a subkey named "Extensions", the Filter Graph Manager searches within that subkey for entries that match the file extension. The value of the key must be a GUID in string form; for example, "{00000000-0000-0000-0000-000000000000}". If the Filter Graph Manager cannot match anything within the **Extensions** subkey, it looks for a subkey named **Source Filter**, which must also be a GUID in string form.

If the Filter Graph Manager finds a matching GUID, it uses this as the CLSID of the source filter, and attempts to load the filter. If it does not find a match, it uses the [File Source (URL)](file-source--url--filter.md) filter, which treats the file name as a URL.

There are two exceptions to this algorithm:

-   To exclude driver letters, single-character strings are not considered protocols.
-   If the string is "file:" or "file://", it is not treated as a protocol.

## File Extensions

If there is no protocol in the file name, the Filter Graph Manager looks in the registry for entries with the key **HKEY\_CLASSES\_ROOT\\Media Type\\Extensions\\**.*ext*\\, where .*ext* is the file extension. If this key exists, the value **Source Filter** contains the CLSID of the source filter, in string form. Optionally, the key can have values for **Media Type** and **Subtype**, which give the major type and subtype GUIDs.

## Check Bytes

Some file types can be identified by specific patterns of bits occurring at specific byte offsets in the file. The Filter Graph Manager looks in the registry for keys with the following form:

**HKEY\_CLASSES\_ROOT\\MediaType\\**{ *major type* }\\{ *subtype* }

where *major type* and *subtype* are GUIDs that define the media type for the byte stream. Each key contains one or more subkeys, usually named 1, 2, and so on, which define the check bytes; and a subkey named **Source Filter** that gives the CLSID of the source filter, in string form. The check-byte subkeys are strings that contain one or more quads of numbers called:

*offset*, *cb*, *mask*, *val*

To match the file, the Filter Graph Manager reads cb bytes, starting from byte number offset. It then performs a bitwise-AND against the value in mask. If the result equals val, the file is a match for that quad. The values mask and val are given in hex. A blank entry for mask is treated as a string of 1s of length cb. A negative value for offset indicates an offset from the end of the file. To match the key, the file must match all of the quads in any of the subkeys.

For example, assume the registry contains the following keys under **HKCR\\Media Type**:


```C++
{e436eb83-524f-11ce-9f53-0020af0ba770}
    {7364696D-0000-0010-8000-00AA00389B71}
        0                    "0,4,,52494646,8,4,,524D4944"
        1                    "0,4,,4D546864"
        Source Filter        "{E436EBB5-524F-11CE-9F53-0020AF0BA770}"
```



The first key corresponds to the major type MEDIATYPE\_Stream. The subkey below that corresponds to the subtype MEDIATYPE\_Midi. The value for the Source Filter subkey is CLSID\_AsyncReader, the CLSID of the [File Source (Async)](file-source--async--filter.md) filter.

Each entry can have multiple quadruples; all of them must match. In the following example, the first 4 bytes of the file must be 0xAB, 0xCD, 0x12, 0x34; and the last 4 bytes of the file must be 0xAB, 0xAB, 0x00, 0xAB:


```C++
    0, 4, , ABCD1234,  -4, 4, , ABAB00AB 
```



Also, there can be multiple entries listed under a single media type. A match to any of them is sufficient. This scheme allows for a set of alternative masks; for instance, .wav files that might or might not have a RIFF header.

> [!Note]  
> This scheme is similar to the one used by the [**GetClassFile**](/windows/win32/api/objbase/nf-objbase-getclassfile) function.

 

## Loading the Source Filter

Assuming that the Filter Graph Manager finds a matching source filter for the file, it adds that filter to the graph, queries the filter for the [**IFileSourceFilter**](/windows/desktop/api/Strmif/nn-strmif-ifilesourcefilter) interface, and calls [**IFileSourceFilter::Load**](/windows/desktop/api/Strmif/nf-strmif-ifilesourcefilter-load). The arguments to the **Load** method are the file name and the media type, as determined from the registry.

If the Filter Graph Manager cannot find anything from the registry, it defaults to using the Async File Source filter. In that case, it sets the media type to **MEDIATYPE\_Stream**, **MEDIASUBTYPE\_None**.

## Custom File Types in Windows Media Player

Windows Media Player uses an additional set of registry entries. For more information, see [File Name Extension Registry Settings](../wmp/file-name-extension-registry-settings.md) in the Windows Media Player SDK.

## Related topics

<dl> <dt>

[Writing DirectShow Filters](writing-directshow-filters.md)
</dt> </dl>

 

 

---
description: GuidNames is a global array in the DirectShow base class library that contains strings representing the GUIDs defined in Uuids.h. This array is useful for generating debug output.
ms.assetid: 6d72ad1e-588a-4a82-a1c1-e1e7b49df572
title: GuidNames (Wxdebug.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GuidNames
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# GuidNames

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

`GuidNames` is a global array in the DirectShow base class library that contains strings representing the GUIDs defined in Uuids.h. This array is useful for generating debug output.

``` syntax
char* GuidNames[guid]
```

## Parameters

<dl> <dt>

<span id="guid"></span><span id="GUID"></span>*guid*
</dt> <dd>

Specifies any GUID value defined in the header file Uuids.h.

</dd> </dl>

## Remarks

Use this global array to output GUID constants as strings. For example, the following code prints the string "MEDIATYPE\_Video" to the console:


```C++
puts(GuidNames[MEDIATYPE_Video]);
```



If the GUID is not matched, the string "Unknown GUID Name" is returned. Not all DirectShow GUIDs are defined in uuids.h.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxdebug.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Debug Output Functions](debug-output-functions.md)
</dt> </dl>

 

 





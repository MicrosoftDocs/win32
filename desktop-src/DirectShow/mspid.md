---
description: Note  This API is deprecated. New applications should not use it. The MSPID data type identifies the purpose of a media steam.
ms.assetid: 83a84eb7-a72c-4ca7-b152-8cc81a5bfdaf
title: MSPID (Mmstream.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# MSPID

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This API is deprecated. New applications should not use it.

 

The **MSPID** data type identifies the purpose of a media steam.


```C++
typedef GUID MSPID;
typedef REFGUID REFMSPID;
```



## Remarks

**MSPID** is simply a typedef for GUID. The following MSPIDs are defined.



| Value               | Description           |
|---------------------|-----------------------|
| MSPID\_PrimaryVideo | Primary video stream. |
| MSPID\_PrimaryAudio | Primary audio stream. |



 

The **REFMSPID** type defines a reference to an **MSPID**.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mmstream.h</dt> </dl> |



## See also

<dl> <dt>

[Multimedia Streaming Data Types](multimedia-streaming-data-types.md)
</dt> </dl>

 

 





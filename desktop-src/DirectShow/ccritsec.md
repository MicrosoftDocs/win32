---
description: The CCritSec class provides a thread lock.
ms.assetid: ecc60afe-15d0-4780-8133-1dfc558c6325
title: CCritSec class (Wxutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CCritSec
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CCritSec class

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **CCritSec** class provides a thread lock.

This class is a thin wrapper for a Windows **CRITICAL\_SECTION** object. You can lock and unlock the thread by calling the [**CCritSec::Lock**](ccritsec-lock.md) and [**CCritSec::Unlock**](ccritsec-unlock.md) methods. However, it is safer to use this class in conjunction with the [**CAutoLock**](cautolock.md) class. When the **CAutoLock** class goes out of scope, it automatically unlocks the **CCritSec** object. Moreover, it compiles to efficient inline code.



| Public Member Variables                            | Description                                              |
|----------------------------------------------------|----------------------------------------------------------|
| [**m\_currentOwner**](ccritsec-m-currentowner.md) | Thread identifier of the owning thread.                  |
| [**m\_lockCount**](ccritsec-m-lockcount.md)       | Number of outstanding locks on this object.              |
| [**m\_fTrace**](ccritsec-m-ftrace.md)             | Boolean value that specifies whether to trace this lock. |
| Public Methods                                     | Description                                              |
| [**CCritSec**](ccritsec-ccritsec.md)              | Constructor method.                                      |
| [**~CCritSec**](ccritsec--ccritsec.md)            | Destructor method.                                       |
| [**Lock**](ccritsec-lock.md)                      | Locks the critical section object.                       |
| [**Unlock**](ccritsec-unlock.md)                  | Unlocks the critical section object.                     |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Critical Section Objects](/windows/desktop/Sync/critical-section-objects)
</dt> <dt>

[DirectShow Base Class Reference](base-class-reference.md)
</dt> </dl>

 


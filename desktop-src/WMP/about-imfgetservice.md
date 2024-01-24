---
title: About IMFGetService
description: About IMFGetService
ms.assetid: c71b1362-a596-42e5-b894-f8a3c0e70140
keywords:
- Windows Media Player plug-ins,interfaces
- plug-ins,interfaces
- digital signal processing plug-ins,interfaces
- DSP plug-ins,interfaces
- interfaces,DSP plug-ins
- Windows Media Player plug-ins,IMFGetService interface
- plug-ins,IMFGetService interface
- digital signal processing plug-ins,IMFGetService interface
- DSP plug-ins,IMFGetService interface
- IMFGetService interface
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About IMFGetService

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **IMFGetService** interface is one of the interfaces that must be implemented by a dual-mode DSP plug-in. It has only one method, **GetService**. A DSP plug-in implements the **GetService** method so that clients can obtain pointers to the interfaces supported by the plug-in when the plug-in is running natively in the Media Foundation pipeline.

 

 





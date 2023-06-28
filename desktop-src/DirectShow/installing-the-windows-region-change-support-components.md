---
description: Installing the Windows Region Change Support Components
ms.assetid: af0e5e19-f4de-4932-a42b-590a1131e0f6
title: Installing the Windows Region Change Support Components
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Installing the Windows Region Change Support Components

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Application developers can utilize the DVD region change support built into Windows to change region inside the DVD playback applications.

On Windows 2000 and later, the component that provides the DVD region change support is in the DLL storprop.dll (available in %windir%\\system32). This DLL is installed by default and no extra steps are required to ensure that this DLL is available.

## Related topics

<dl> <dt>

[DVD Region Change Support in Windows](dvd-region-change-support-in-windows.md)
</dt> </dl>

 

 




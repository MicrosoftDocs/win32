---
description: Subsequent DVD Region Change
ms.assetid: 08c0b48a-2851-40c8-addc-21baeb83df1b
title: Subsequent DVD Region Change
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Subsequent DVD Region Change

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

In Windows 2000 and later, the DVD Navigator invokes a property page on the DVD-ROM drive device in the Device Manager. This property page is also brought up by the DVDPlay.exe application when a region needs to be changed. The UI of this property page is very similar to that of DVDRgn.exe and it is regionalized in the operating system.

For RPC1 drives, the Windows Operating System components manage region changes. RPC2 drives maintain the region setting in their own hardware. When the number of allowed changes are exhausted on a RPC2 drive, the drive will fail the call to change the region and the region-change component in the operating system will indicate that to the user.

## Related topics

<dl> <dt>

[DVD Region Change Support in Windows](dvd-region-change-support-in-windows.md)
</dt> </dl>

 

 




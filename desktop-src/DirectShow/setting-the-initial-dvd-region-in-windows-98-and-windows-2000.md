---
description: Setting the Initial DVD Region
ms.assetid: b8238cb4-a101-4998-866f-4cf9ebd5d277
title: Setting the Initial DVD Region
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Setting the Initial DVD Region

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

It is the responsibility of the system manufacturer to select an initial DVD region for the DVD drive in their PCs.

> [!Note]  
> Only encrypted discs can be used to set the region.

 

### Windows 2000 and Later

Starting in Windows 2000, the default DVD region is selected based upon the locale that the machine is set up for. Windows 2000 will always set the initial region for a DVD drive using this default region as well as the disc's region, if there is a disc is in the drive. The system manufacturer does not have to do anything to set the initial region for Windows 2000 or later DVD drives.

For RPC1 drives, if there is no disc in the drive during boot up then the default region is set based only on the locale of the machine. If there is a DVD disc in the drive during boot up, the default region is selected to be the drive's region, provided it matches a region of the disc; otherwise the lowest region on the disc is picked as the initial region of the drive. The user (or system manufacturer) has one remaining change allowed, in case the default was not correct.

For RPC2 drives, if during the setup process Windows 2000 finds that the drive does not have any region set, it will try to pick a region as above, but only if there is a disc in the drive. (RPC1 drives will choose the region without any disc in drive). Once a region is set for RPC2 drives, it is not auto-changed by either a re-installation or a clean installation of the Operating System.

The OEM can set a registry key containing the default DVD region for the system. On first boot, the drive region will be set to this value. The registry key on Windows 2000 and later is HKLM\\System\\CurrentControlSet\\Control\\Class\\\<CDROM GUID\>\\ \<instance number\>\\DefaultDVDRegion(binary) .

## Related topics

<dl> <dt>

[DVD Region Change Support in Windows](dvd-region-change-support-in-windows.md)
</dt> </dl>

 

 




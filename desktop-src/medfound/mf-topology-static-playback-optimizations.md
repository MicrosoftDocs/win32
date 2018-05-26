---
Description: Enables static optimizations in the video pipeline.
ms.assetid: 62fb3f0f-ab1f-4c61-8e7f-62908b947788
title: MF\_TOPOLOGY\_STATIC\_PLAYBACK\_OPTIMIZATIONS attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_TOPOLOGY\_STATIC\_PLAYBACK\_OPTIMIZATIONS attribute

Enables static optimizations in the video pipeline.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master).

## Applies to

[**IMFTopology**](/windows/win32/mfidl/nn-mfidl-imftopology?branch=master)

## Remarks

Set this attribute before loading a topology. If the attribute is **TRUE**, the topology loader attempts to optimize the pipeline before playback starts.

If you set this attribute, you should also set the following attributes:

-   [MF\_TOPOLOGY\_PLAYBACK\_FRAMERATE](mf-topology-playback-framerate.md)
-   [MF\_TOPOLOGY\_PLAYBACK\_MAX\_DIMS](mf-topology-playback-max-dims.md)

The GUID constant for this attribute is exported from mfuuid.lib.

## Examples


```C++
HRESULT SetPlaybackOptimizations(IMFTopology *pTopology, HWND hwnd)
{
    HRESULT hr = pTopology->SetUINT32(
        MF_TOPOLOGY_STATIC_PLAYBACK_OPTIMIZATIONS, TRUE);

    if (FAILED(hr))
    {
        return hr;
    }

    HMONITOR hCurrentMon = MonitorFromWindow(hwnd, MONITOR_DEFAULTTOPRIMARY);

    if (hCurrentMon)
    {
        MONITORINFO MonitorInfo = {0};
        MonitorInfo.cbSize = sizeof(MONITORINFO);

        BOOL fSucceeded = GetMonitorInfo(hCurrentMon, &amp;MonitorInfo);

        if (fSucceeded )
        {
            const RECT&amp; rcMonitor = MonitorInfo.rcMonitor;

            LONG width = rcMonitor.right - rcMonitor.left;
            LONG height = rcMonitor.bottom - rcMonitor.top;

            hr = MFSetAttributeSize(
                pTopology, 
                MF_TOPOLOGY_PLAYBACK_MAX_DIMS, 
                (UINT32)width, (UINT32)height
                );

            if (FAILED(hr))
            {
                goto done;
            }

            HDC hdc = GetDC(hwnd);

            hr = MFSetAttributeRatio(
                pTopology,
                MF_TOPOLOGY_PLAYBACK_FRAMERATE,
                GetDeviceCaps(hdc, VREFRESH), 1
                );

            ReleaseDC(hwnd, hdc);
        }
    }
done:
    return hr;
}
```



## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                            |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Topology Attributes](topology-attributes.md)
</dt> <dt>

[Video Quality Management](video-quality-management.md)
</dt> </dl>

 

 





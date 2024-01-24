---
description: Describes swapchain statistics relating to PresentEx calls.
ms.assetid: aa100b83-6fbf-442d-9891-7fc034a5b1d5
title: D3DPRESENTSTATS structure (D3d9types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DPRESENTSTATS
api_type: 
- HeaderDef
api_location: 
- d3d9types.h
---

# D3DPRESENTSTATS structure

Describes swapchain statistics relating to [**PresentEx**](/windows/win32/api/d3d9/nf-d3d9-idirect3ddevice9ex-presentex) calls.

## Syntax


```C++
typedef struct _D3DPRESENTSTATS {
  UINT          PresentCount;
  UINT          PresentRefreshCount;
  UINT          SyncRefreshCount;
  LARGE_INTEGER SyncQPCTime;
  LARGE_INTEGER SyncGPUTime;
} D3DPRESENTSTATS;
```



## Members

<dl> <dt>

**PresentCount**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Running count of successful Present calls made by a display device that is currently outputting to screen. This parameter is really the Present ID of the last Present call and is not necessarily the total number of Present API calls made.

</dd> <dt>

**PresentRefreshCount**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

The vblank count at which the last Present was displayed on screen, the vblank count increments once every vblank interval.

</dd> <dt>

**SyncRefreshCount**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

The vblank count when the scheduler last sampled the machine time by calling QueryPerformanceCounter.

</dd> <dt>

**SyncQPCTime**
</dt> <dd>

Type: **[**LARGE\_INTEGER**](/windows/win32/api/winnt/ns-winnt-large_integer-r1)**

</dd> <dd>

The scheduler's last sampled machine time, obtained by calling [**QueryPerformanceCounter**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter).

</dd> <dt>

**SyncGPUTime**
</dt> <dd>

Type: **[**LARGE\_INTEGER**](/windows/win32/api/winnt/ns-winnt-large_integer-r1)**

</dd> <dd>

This value is not used.

</dd> </dl>

## Remarks

When a 9Ex application adopts Flip Mode present (D3DSWAPEFFECT\_FLIPEX), applications can detect frame dropping by calling GetPresentStatistics at any point in time. In effect, they can do the following.

1.  Render to the back buffer
2.  Call Present
3.  Call GetPresentStats and store the resulting D3DPRESENTSTATS structure
4.  Render the next frame to the back buffer
5.  Call Present
6.  Repeat steps 4 and 5 one or more times
7.  Call GetPresentStats and store the resulting D3DPRESENTSTATS structure
8.  Compare the values of PresentRefreshCount from the two stored D3DPRESENTSTATS structures. The application can calculate the corresponding PresentRefreshCount of a particular PresentCount parameter based on the assumptions of PresentRefreshCount increment and PresentCount assignment of frame presents. If the PresentRefreshCount last sampled does not match the PresentCount (i.e. if the PresentRefreshCount has incremented but PresentCount has not, then there was frame dropping.)

Applications can determine whether a frame has been dropped by sampling any two instances of PresentCount and GetPresentStats (by calling GetPresentStats API at any two points in time). For example, a media application that is presenting at the same rate as the monitor refresh rate (for example, monitor refresh rate is 60Hz, the application presents a frame every 1/60 seconds) wants to present frames A, B, C, D, E, each corresponding to Present IDs (PresentCount) 1, 2, 3, 7, 8.

The application code looks like the following sequence.

1.  Render frame A to the back buffer
2.  Call Present, PresentCount = 1
3.  Call GetPresentStats and store the resulting D3DPRESENTSTATS structure
4.  Render the next 4 frames, B, C, D, E, respectively
5.  Call Present 4 times, PresentCounts = 2, 3, 7, 8, respectively
6.  Call GetPresentStats and store the resulting D3DPRESENTSTATS structure
7.  Compare the values of PresentRefreshCount from the two stored D3DPRESENTSTATS structures. If the difference is 2, i.e. 2 vblank intervals has elapsed between the two GetPresentStats API calls, then the last presented frame should be frame C. Because the application presents once very vblank interval (the refresh rate of the monitor), the time elapsed between when frame A is presented and when frame C is presented should be 2 vblanks.
8.  Compare the values of PresentCount from the two stored D3DPRESENTSTATS structures. If the first PresentCount is 1 (corresponding to frame A) and the second PresentCount is 3 (corresponding to frame C), then no frames have been dropped. If the second PresentCount is 3, which corresponds to frame D, then the application knows that one frame has been dropped.

Note that GetPresentStatistics will be processed after it is called, regardless of the state of FLIPEX mode PresentEx calls.

**Windows Vista:** The Present calls will be queued and then processed before GetPresentStats call will be processed.

When an application detects that the presentation of certain frames are behind, it can skip those frames and correct the presentation to re-synchronize with the vblank. To do this, an application can simply not render the late frames and start rendering with the next correct frame in the queue. However, if an application has already started the rendering of late frames, it can use a new Present parameter in D3D9Ex called D3DPRESENT\_FORCEIMMEDIATE. The flag will be passed in the parameters of Present API call and indicates to the runtime that the frame will be processed immediately within the next vblank interval, effectively not visible on screen at all. Here is the application usage example after the last step in the previous example.

1.  Render the next frame to the back buffer
2.  Discover from PresentRefreshCount that the next frame is already late
3.  Set Present interval to D3DPRESENT\_FORCEIMMEDIATE
4.  Call Present on the next frame

Applications can synchronize video and audio streams in the same manner because the behavior of GetPresentStatistics does not change in that scenario.

D3D9Ex Flip Mode provides frame statistics information to windowed applications and full screen 9Ex applications.

**Windows Vista:** Use the DWM APIs for retrieving present statistics.

When Desktop Window Manager is turned off, windowed mode 9Ex applications using flip mode will receive present statistics information of limited accuracy.

**Windows Vista:**

If an application is not fast enough to keep up with the monitor's refresh rate, possibly due to slow hardware or lack of system resources, then it can experience a graphics glitch. A glitch is a so-called visual hiccup. If a monitor is set to refresh at 60 Hz, and the application can only manage 30 fps, then half of the frames will have glitches.

Applications can detect a glitch by keeping track of SynchRefreshCount. For example, an application might perform the following sequence of actions.

1.  Render to the back buffer.
2.  Call Present.
3.  Call GetPresentStats and store the resulting D3DPRESENTSTATS structure.
4.  Render the next frame to the back buffer.
5.  Call Present.
6.  Call GetPresentStats and store the resulting D3DPRESENTSTATS structure.
7.  Compare the values of SyncRefreshCount from the two stored D3DPRESENTSTATS structures. If the difference is greater than one, then a frame was skipped.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3d9types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> </dl>

 

 

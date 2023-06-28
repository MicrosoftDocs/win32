---
description: This topic is step 1 of the tutorial Audio/Video Playback in DirectShow.
ms.assetid: 3ccd201d-e60d-40bf-a602-6d42df03b36b
title: 'Step 1: Declare the DShowPlayer Class'
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Step 1: Declare the DShowPlayer Class

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This topic is step 1 of the tutorial [Audio/Video Playback in DirectShow](audio-video-playback-in-directshow.md). The complete code is shown in the topic [DirectShow Playback Example](directshow-playback-example.md).

In this tutorial, the `DShowPlayer` class manages all DirectShow functionality. This class is declared as folows.


```C++
#include <new>
#include <windows.h>
#include <dshow.h>


enum PlaybackState
{
    STATE_NO_GRAPH,
    STATE_RUNNING,
    STATE_PAUSED,
    STATE_STOPPED,
};

const UINT WM_GRAPH_EVENT = WM_APP + 1;

typedef void (CALLBACK *GraphEventFN)(HWND hwnd, long eventCode, LONG_PTR param1, LONG_PTR param2);

class DShowPlayer
{
public:
    DShowPlayer(HWND hwnd);
    ~DShowPlayer();

    PlaybackState State() const { return m_state; }

    HRESULT OpenFile(PCWSTR pszFileName);
    
    HRESULT Play();
    HRESULT Pause();
    HRESULT Stop();

    BOOL    HasVideo() const;
    HRESULT UpdateVideoWindow(const LPRECT prc);
    HRESULT Repaint(HDC hdc);
    HRESULT DisplayModeChanged();

    HRESULT HandleGraphEvent(GraphEventFN pfnOnGraphEvent);

private:
    HRESULT InitializeGraph();
    void    TearDownGraph();
    HRESULT CreateVideoRenderer();
    HRESULT RenderStreams(IBaseFilter *pSource);

    PlaybackState   m_state;

    HWND m_hwnd; // Video window. This window also receives graph events.

    IGraphBuilder   *m_pGraph;
    IMediaControl   *m_pControl;
    IMediaEventEx   *m_pEvent;
    CVideoRenderer  *m_pVideo;
};
```





Notes:

-   The `PlaybackState` enumeration describes the current state of the `DShowPlayer` object.
-   The constant WM\_GRAPH\_EVENT defines a private window message. This message is used to notify the application about filter graph events. See [Step 6: Handle Graph Events](step-6--handle-graph-events.md).
-   `GraphEventFN` is a pointer to a callback function for handling filter graph events. The application implements this callback function.
-   The *m\_pVideo* member variable provides a wrapper for the various DirectShow video renderers. See [Step 2: Declare CVideoRenderer and Derived Classes](step-2--declare-cvideorenderer-and-derived-classes.md).
-   Throughout this tutorial, the [SafeRelease](../medfound/saferelease.md) function is used to release COM interface pointers.

Next: [Step 2: Declare CVideoRenderer and Derived Classes](step-2--declare-cvideorenderer-and-derived-classes.md).

## Related topics

<dl> <dt>

[Audio/Video Playback in DirectShow](audio-video-playback-in-directshow.md)
</dt> </dl>

 

 

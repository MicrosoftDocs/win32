---
description: This topic is step 2 of the tutorial Audio/Video Playback in DirectShow.
ms.assetid: 61106781-d10c-41a8-993e-121e0a1e4c4d
title: 'Step 2: Declare CVideoRenderer and Derived Classes'
ms.topic: article
ms.date: 05/31/2018
---

# Step 2: Declare CVideoRenderer and Derived Classes

This topic is step 2 of the tutorial [Audio/Video Playback in DirectShow](audio-video-playback-in-directshow.md). The complete code is shown in the topic [DirectShow Playback Example](directshow-playback-example.md).

DirectShow provides several different filters that render video:

-   [**Enhanced Video Renderer Filter**](enhanced-video-renderer-filter.md) (EVR)
-   [Video Mixing Renderer Filter 9](video-mixing-renderer-filter-9.md) (VMR-9)
-   [Video Mixing Renderer Filter 7](video-mixing-renderer-filter-7.md) (VMR-7)

For more information about the differences between these filters, see [Choosing the Right Video Renderer](choosing-the-right-renderer.md).

In this tutorial, the following abstract class is used to wrap the video renderer filter.


```C++
// Abstract class to manage the video renderer filter.
// Specific implementations handle the VMR-7, VMR-9, or EVR filter.

class CVideoRenderer
{
public:
    virtual ~CVideoRenderer() {};
    virtual BOOL    HasVideo() const = 0;
    virtual HRESULT AddToGraph(IGraphBuilder *pGraph, HWND hwnd) = 0;
    virtual HRESULT FinalizeGraph(IGraphBuilder *pGraph) = 0;
    virtual HRESULT UpdateVideoWindow(HWND hwnd, const LPRECT prc) = 0;
    virtual HRESULT Repaint(HWND hwnd, HDC hdc) = 0;
    virtual HRESULT DisplayModeChanged() = 0;
};
```



Notes:

-   The `HasVideo` method returns **TRUE** if the video renderer has been created.
-   The `AddToGraph` method adds the video renderer to the filter graph.
-   The `FinalizeGraph` method completes the graph-building step.
-   The `UpdateVideoWindow` method updates the video destination rectangle.
-   The `Repaint` method redraws the current video frame.
-   The `DisplayModeChanged` method handles display-mode changes.

Each of these methods is described in detail later in this tutorial.

Next, declare a derived class to wrap each of the three video renderers: the EVR, the VMR-9, and the VMR-7.

### CEVR Class

The `CEVR` class manages the EVR. It contains a pointer to the [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter) and [**IMFVideoDisplayControl**](/windows/win32/api/evr/nn-evr-imfvideodisplaycontrol) interfaces of the EVR.


```C++
// Manages the EVR video renderer filter.

class CEVR : public CVideoRenderer
{
    IBaseFilter            *m_pEVR;
    IMFVideoDisplayControl *m_pVideoDisplay;

public:
    CEVR();
    ~CEVR();
    BOOL    HasVideo() const;
    HRESULT AddToGraph(IGraphBuilder *pGraph, HWND hwnd);
    HRESULT FinalizeGraph(IGraphBuilder *pGraph);
    HRESULT UpdateVideoWindow(HWND hwnd, const LPRECT prc);
    HRESULT Repaint(HWND hwnd, HDC hdc);
    HRESULT DisplayModeChanged();
};
```



### CVMR9 Class

The `CVMR9` class manages the VMR-9. It contains a pointer to the [**IVMRWindowlessControl9**](/previous-versions/windows/desktop/api/Vmr9/nn-vmr9-ivmrwindowlesscontrol9) interface.


```C++
// Manages the VMR-9 video renderer filter.

class CVMR9 : public CVideoRenderer
{
    IVMRWindowlessControl9 *m_pWindowless;

public:
    CVMR9();
    ~CVMR9();
    BOOL    HasVideo() const;
    HRESULT AddToGraph(IGraphBuilder *pGraph, HWND hwnd);
    HRESULT FinalizeGraph(IGraphBuilder *pGraph);
    HRESULT UpdateVideoWindow(HWND hwnd, const LPRECT prc);
    HRESULT Repaint(HWND hwnd, HDC hdc);
    HRESULT DisplayModeChanged();
};
```



### CVMR7 Class

The `CVMR7` class manages the VMR-7. It contains a pointer to the [**IVMRWindowlessControl**](/windows/desktop/api/Strmif/nn-strmif-ivmrwindowlesscontrol) interface.


```C++
// Manages the VMR-7 video renderer filter.

class CVMR7 : public CVideoRenderer
{
    IVMRWindowlessControl   *m_pWindowless;

public:
    CVMR7();
    ~CVMR7();
    BOOL    HasVideo() const;
    HRESULT AddToGraph(IGraphBuilder *pGraph, HWND hwnd);
    HRESULT FinalizeGraph(IGraphBuilder *pGraph);
    HRESULT UpdateVideoWindow(HWND hwnd, const LPRECT prc);
    HRESULT Repaint(HWND hwnd, HDC hdc);
    HRESULT DisplayModeChanged();
};
```



Next: [Step 3: Build the Filter Graph](step-3--build-the-filter-graph.md).

## Related topics

<dl> <dt>

[Audio/Video Playback in DirectShow](audio-video-playback-in-directshow.md)
</dt> <dt>

[Using the Video Mixing Renderer](using-the-video-mixing-renderer.md)
</dt> <dt>

[Video Rendering](video-rendering.md)
</dt> </dl>

 

 

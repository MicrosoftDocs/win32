---
title: Update the Animation Manager and Draw Frames
description: Each time an application schedules a storyboard, the application must supply the current time to the animation manager.
ms.assetid: c4f746c3-e47c-4b82-a41b-e2c0d177d097
keywords:
- animation manager objects Windows Animation ,updating
- animation timer objects Windows Animation ,connecting
ms.topic: article
ms.date: 05/31/2018
---

# Update the Animation Manager and Draw Frames

Each time an application schedules a storyboard, the application must supply the current time to the animation manager. The current time is also required when directing the animation manager to update its state and set all animation variables to the appropriate interpolated values.

## Overview

There are two configurations supported by Windows Animation: application-driven animation and timer-driven animation.

To use application-driven animation in your application, you must update the animation manager before drawing each frame and use an appropriate mechanism to draw frames frequently enough for animation. An application using application-driven animation can use any mechanism to determine the current time, but the Windows Animation timer object returns a precise time in the units accepted by the animation manager. To avoid unnecessary drawing when no animations are playing, you should also provide a manager event handler to start redrawing when animations are scheduled and check after each frame whether redrawing can be suspended. For more information, see [Application-Driven Animation](scenic-animation-api-overview.md).

In the application-driven configuration, an application can call the [**IUIAnimationManager::GetStatus**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationmanager-getstatus) method to verify that animations are currently scheduled and continue to draw frames if they are. Because redrawing stops when there are no animations scheduled, it is necessary to restart it the next time an animation is scheduled. An application can register a manager event handler to be notified when the status of the animation manager changes from idle (no animations are currently scheduled) to busy.

To use timer-driven animation in your application, you must connect the animation manager to an animation timer and provide a timer event handler. When the animation manager is connected to a timer, the timer can tell the manager when the animation state should be updated as time progresses. The application should draw a frame for each timer tick. The animation manager can in turn tell the timer when there are animations playing, so the timer can shut itself off during idle periods when redrawing is unnecessary. To avoid unnecessary drawing when no animations are playing, you should configure the timer to disable itself automatically. For more information, see [Timer-Driven Animation](scenic-animation-api-overview.md).

## Example Code

-   [Application-Driven Animation](#application-driven-animation)
-   [Timer-Driven Animation](#timer-driven-animation)

### Application-Driven Animation

The following example code is taken from ManagerEventHandler.h from the Windows Animation samples [Application-Driven Animation](application-driven-animation-sample.md) and [Grid Layout](/windows/desktop/UIAnimation/grid-layout-sample). It defines the manager event handler.


```C++
#include "UIAnimationHelper.h"

// Event handler object for manager status changes

class CManagerEventHandler :
    public CUIAnimationManagerEventHandlerBase<CManagerEventHandler>
{
public:

    static HRESULT
    CreateInstance
    (
        CMainWindow *pMainWindow,
        IUIAnimationManagerEventHandler **ppManagerEventHandler
    ) throw()
    {
        CManagerEventHandler *pManagerEventHandler;
        HRESULT hr = CUIAnimationCallbackBase::CreateInstance(
            ppManagerEventHandler,
            &pManagerEventHandler
            );
        if (SUCCEEDED(hr))
        {
            pManagerEventHandler->m_pMainWindow = pMainWindow;
        }
        
        return hr;
    }

    // IUIAnimationManagerEventHandler

    IFACEMETHODIMP
    OnManagerStatusChanged
    (
        UI_ANIMATION_MANAGER_STATUS newStatus,
        UI_ANIMATION_MANAGER_STATUS previousStatus
    )
    {
        HRESULT hr = S_OK;

        if (newStatus == UI_ANIMATION_MANAGER_BUSY)
        {
            hr = m_pMainWindow->Invalidate();
        }

        return hr;
    }

    ...

};
```



The following example code is taken from MainWindow.cpp from the Windows Animation sample [Application-Driven Animation](application-driven-animation-sample.md); see CMainWindow::InitializeAnimation. This example creates an instance of the manager event handler using the [**CreateInstance**](/windows/desktop/api/unknwn/nf-unknwn-iclassfactory-createinstance) method and passes it to the animation manager using the [**IUIAnimationManager::SetManagerEventHandler**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationmanager-setmanagereventhandler) method.


```C++
// Create and set the ManagerEventHandler to start updating when animations are scheduled

IUIAnimationManagerEventHandler *pManagerEventHandler;
HRESULT hr = CManagerEventHandler::CreateInstance(
    this,
    &pManagerEventHandler
    );
if (SUCCEEDED(hr))
{
    hr = m_pAnimationManager->SetManagerEventHandler(
        pManagerEventHandler
        );
    pManagerEventHandler->Release();
}
```



Because the manager event handler retains a reference to the main window object, the manager event handler should be cleared (by passing **NULL** to [**SetManagerEventHandler**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationmanager-setmanagereventhandler)) or the animation manager should be completely released before the main window is destroyed.

The following example code is taken from MainWindow.cpp in the Windows Animation sample [Application-Driven Animation](application-driven-animation-sample.md); see the CMainWindow::OnPaint method. It calls the [**IUIAnimationManager::GetTime**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationtimer-gettime) method to retrieve the time in the units required by the [**IUIAnimationManager::Update**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationmanager-update) method.


```C++
// Update the animation manager with the current time

UI_ANIMATION_SECONDS secondsNow;
HRESULT hr = m_pAnimationTimer->GetTime(
    &secondsNow
    );

if (SUCCEEDED(hr))
{
    hr = m_pAnimationManager->Update(
        secondsNow
        );

    ...

}
```



The following example code is taken from MainWindow.cpp from the Windows Animation samples [Application-Driven Animation](application-driven-animation-sample.md) and [Grid Layout](/windows/desktop/UIAnimation/grid-layout-sample); see the CMainWindow::OnPaint method. It assumes that the application is using a graphics API that automatically synchronizes to the monitor refresh rate (such as Direct2D with its default settings), in which case a call to the [**InvalidateRect**](/windows/desktop/api/winuser/nf-winuser-invalidaterect) function is enough to ensure that the painting code will be called again when it is time to draw the next frame. Rather than call **InvalidateRect** unconditionally, it is better to check if there are still any animations scheduled using [**GetStatus**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationmanager-getstatus).


```C++
// Read the values of the animation variables and draw the client area

hr = DrawClientArea();
if (SUCCEEDED(hr))
{          
    // Continue redrawing the client area as long as there are animations scheduled
    UI_ANIMATION_MANAGER_STATUS status;
    hr = m_pAnimationManager->GetStatus(
        &status
        );
    if (SUCCEEDED(hr))
    {
        if (status == UI_ANIMATION_MANAGER_BUSY)
        {
            InvalidateRect(
                m_hwnd,
                NULL,
                FALSE
                );
        }
    }
}
```



### Timer-Driven Animation

The following example code is taken from TimerEventHandler.h from the Windows Animation sample [Timer-Driven Animation](timer-driven-animation-sample.md). The example code defines the timer event handler, which invalidates the window's client area to cause a repaint after each update of the animation state.


```C++
#include "UIAnimationHelper.h"

// Event handler object for timer events

class CTimerEventHandler :
    public CUIAnimationTimerEventHandlerBase<CTimerEventHandler>
{
public:

    static HRESULT
    CreateInstance
    (
        CMainWindow *pMainWindow,
        IUIAnimationTimerEventHandler **ppTimerEventHandler
    ) throw()
    {
        CTimerEventHandler *pTimerEventHandler;
        HRESULT hr = CUIAnimationCallbackBase::CreateInstance(
            ppTimerEventHandler,
            &pTimerEventHandler
            );

        if (SUCCEEDED(hr))
        {
            pTimerEventHandler->m_pMainWindow = pMainWindow;
        }
        
        return hr;
    }

    // IUIAnimationTimerEventHandler

    IFACEMETHODIMP
    OnPreUpdate()
    {
        return S_OK;
    }

    IFACEMETHODIMP
    OnPostUpdate()
    {
        HRESULT hr = m_pMainWindow->Invalidate();

        return hr;
    }

    IFACEMETHODIMP
    OnRenderingTooSlow
    (
        UINT32 /* fps */
    )
    {
        return S_OK;
    }

    ...

};
```



The following example code is taken from MainWindow.cpp from the Windows Animation sample [Timer-Driven Animation](timer-driven-animation-sample.md); see CMainWindow::InitializeAnimation. This example creates an instance of the timer event handler using the [**CreateInstance**](/windows/desktop/api/unknwn/nf-unknwn-iclassfactory-createinstance) method and passes it to the timer using the [**IUIAnimationTimer::SetTimerEventHandler**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationtimer-settimereventhandler) method. Because the timer event handler retains a reference to the main window object, the timer event handler should be cleared (by passing **NULL** to **SetTimerEventHandler**) or the timer completely released before the main window is destroyed.


```C++
// Create and set the timer event handler

IUIAnimationTimerEventHandler *pTimerEventHandler;
hr = CTimerEventHandler::CreateInstance(
    this,
    &pTimerEventHandler
    );
if (SUCCEEDED(hr))
{
    hr = m_pAnimationTimer->SetTimerEventHandler(
        pTimerEventHandler
        );
    pTimerEventHandler->Release();
}
```



The following example code is taken from MainWindow.cpp in the Windows Animation sample [Timer-Driven Animation](timer-driven-animation-sample.md); see the CMainWindow::InitializeAnimation method. It calls the [**QueryInterface**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) method on the animation manager object to get a pointer to [**IUIAnimationTimerUpdateHandler**](/windows/desktop/api/UIAnimation/nn-uianimation-iuianimationtimerupdatehandler), then connects the [**UIAnimationManager**](/previous-versions/windows/desktop/legacy/dd317019(v=vs.85)) and [**UIAnimationTimer**](/previous-versions/windows/desktop/legacy/dd317021(v=vs.85)) objects by setting the animation manager as the timer's update handler using the [**IUIAnimationTimer::SetTimerUpdateHandler**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationtimer-settimerupdatehandler) method. Note that it is not necessary to explicitly clear this connection; the connection is cleared safely after the application releases both the animation manager and the animation timer.


```C++
// Connect the animation manager to the timer

IUIAnimationTimerUpdateHandler *pTimerUpdateHandler;
hr = m_pAnimationManager->QueryInterface(
    IID_PPV_ARGS(&pTimerUpdateHandler)
    );

if (SUCCEEDED(hr))
{
    hr = m_pAnimationTimer->SetTimerUpdateHandler(
        pTimerUpdateHandler
        UI_ANIMATION_IDLE_BEHAVIOR_DISABLE  // timer will shut itself off when there are no animations playing
        );
    pTimerUpdateHandler->Release();
    if (SUCCEEDED(hr))
    {
        // Create and set the timer event handler

        ...

    }
}
```



If **UI\_ANIMATION\_IDLE\_BEHAVIOR\_DISABLE** is not used, it is also necessary to enable the timer to start it ticking.

## Previous Step

Before starting this step, you should have completed this step: [Create Animation Variables](create-animation-variables.md).

## Next Step

After completing this step, the next step is: [Read the Animation Variable Values](updating---application-driven-animation.md).

## Related topics

<dl> <dt>

[**IUIAnimationManager::GetStatus**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationmanager-getstatus)
</dt> <dt>

[**IUIAnimationManager::SetManagerEventHandler**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationmanager-setmanagereventhandler)
</dt> <dt>

[**IUIAnimationManager::Update**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationmanager-update)
</dt> <dt>

[**IUIAnimationTimer::GetTime**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationtimer-gettime)
</dt> <dt>

[**IUIAnimationTimer::SetTimerUpdateHandler**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationtimer-settimerupdatehandler)
</dt> <dt>

[**UIAnimationManager**](/previous-versions/windows/desktop/legacy/dd317019(v=vs.85))
</dt> <dt>

[**UIAnimationTimer**](/previous-versions/windows/desktop/legacy/dd317021(v=vs.85))
</dt> <dt>

[Windows Animation Overview](scenic-animation-api-overview.md)
</dt> </dl>

 

 
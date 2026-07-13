---
title: Precision Touchpad Programming Guide
description: Learn how to use the Precision Touchpad APIs for receiving two-finger gestures, handling global touchpad gestures, and injecting touchpad input.
ms.topic: concept-article
ms.date: 03/28/2026
---

# Precision Touchpad Programming Guide

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

This guide demonstrates three key scenarios for working with the Precision Touchpad APIs: receiving two-finger touchpad gestures and reporting inertia, adding handlers for global touchpad gestures, and injecting touchpad input into the system.

## Receiving two-finger touchpad gestures and reporting inertia

This sample demonstrates how touchpad input can be received for two-finger gestures, and how inertia can be reported based on gesture recognition.

### C++ example

```cpp
class PointerInputSample :
    public winrt::implements<PointerInputSample,
        winrt::Windows::Foundation::IInspectable>
{
public:
    void InitializeComponent();

private:
    static LRESULT CALLBACK WndProcStatic(
        HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam);
    LRESULT CALLBACK WndProc(
        HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam);
    static void CALLBACK OutputCallbackStatic(
        PVOID pvClient, const INTERACTION_CONTEXT_OUTPUT* pOutput);
    void OutputCallback(const INTERACTION_CONTEXT_OUTPUT* pOutput);
    void InitializeInteractionContext();
    void ProcessPointerInput(WPARAM wParam);
    void ProcessTimer();
    void ProcessInertia(UINT message);

private:
    wil::unique_hwnd m_hwnd = nullptr;
    using unique_interaction_context =
        wil::unique_any<HINTERACTIONCONTEXT,
            decltype(&::DestroyInteractionContext),
            ::DestroyInteractionContext>;
    unique_interaction_context m_interactionContext;
    UINT_PTR m_inertiaTimer = 0;
    INTERACTION_FLAGS m_lastInteractionFlags = INTERACTION_FLAG_NONE;
};

void
PointerInputSample::InitializeComponent()
{
    // Create and show a window.
    WNDCLASSEX wcex = { sizeof(WNDCLASSEX) };
    wcex.hCursor = ::LoadCursor(nullptr, IDC_ARROW);
    wcex.lpszClassName = L"PointerInputSampleClass";
    wcex.lpfnWndProc = WndProcStatic;
    m_hwnd.reset(::CreateWindow(
        MAKEINTATOM(::RegisterClassEx(&wcex)),
        L"Touchpad Pointer Input Sample",
        WS_OVERLAPPEDWINDOW | WS_VISIBLE,
        50, 50, 450, 150,
        nullptr, nullptr, nullptr, this));
    THROW_LAST_ERROR_IF_NULL(m_hwnd);

    // Register the window as being able to receive WM_POINTER messages for touchpads.
    THROW_IF_WIN32_BOOL_FALSE(::RegisterTouchpadCapableWindow(
        m_hwnd.get(),
        TRUE /*fEnable*/));

    // Create and configure an Interaction Context that will be fed the touchpad input.
    InitializeInteractionContext();
}

void
PointerInputSample::InitializeInteractionContext()
{
    THROW_IF_FAILED(::CreateInteractionContext(&m_interactionContext));
    THROW_IF_FAILED(::RegisterOutputCallbackInteractionContext(
        m_interactionContext.get(),
        OutputCallbackStatic,
        this));

    // Configure the Interaction Context with railed panning support with inertia.
    INTERACTION_CONTEXT_CONFIGURATION cfg[] =
    {
        {INTERACTION_ID_MANIPULATION,
            INTERACTION_CONFIGURATION_FLAG_MANIPULATION |
            INTERACTION_CONFIGURATION_FLAG_MANIPULATION_TRANSLATION_X |
            INTERACTION_CONFIGURATION_FLAG_MANIPULATION_TRANSLATION_Y |
            INTERACTION_CONFIGURATION_FLAG_MANIPULATION_TRANSLATION_INERTIA |
            INTERACTION_CONFIGURATION_FLAG_MANIPULATION_RAILS_X |
            INTERACTION_CONFIGURATION_FLAG_MANIPULATION_RAILS_Y},
    };

    THROW_IF_FAILED(::SetInteractionConfigurationInteractionContext(
        m_interactionContext.get(),
        ARRAYSIZE(cfg),
        cfg));

    // By using himetric measurement units, the output will be in the coordinate
    // space of the device. Screen measurement units are special for touchpads
    // because the same gesture can result in different screen output, depending
    // on the scale factor of the display the gesture is performed on.
    THROW_IF_FAILED(::SetPropertyInteractionContext(
        m_interactionContext.get(),
        INTERACTION_CONTEXT_PROPERTY_MEASUREMENT_UNITS,
        0 /*himetric*/));

    // By setting this property, contacts fed to the IC are implicitly assumed to
    // be part of the interaction, rather than requiring explicit inclusion via
    // AddPointerInteractionContext.
    THROW_IF_FAILED(::SetPropertyInteractionContext(
        m_interactionContext.get(),
        INTERACTION_CONTEXT_PROPERTY_FILTER_POINTERS,
        FALSE));
}

LRESULT CALLBACK
PointerInputSample::WndProcStatic(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam)
{
    switch (message)
    {
    case WM_CREATE:
    {
        CREATESTRUCT *pCreate = reinterpret_cast<CREATESTRUCT*>(lParam);
        auto pThis = reinterpret_cast<PointerInputSample*>(pCreate->lpCreateParams);
        ::SetWindowLongPtr(hWnd, GWLP_USERDATA, reinterpret_cast<LONG_PTR>(pThis));
        break;
    }
    case WM_DESTROY:
    {
        ::PostQuitMessage(0);
        break;
    }
    default:
    {
        auto pThis = reinterpret_cast<PointerInputSample*>(
            ::GetWindowLongPtr(hWnd, GWLP_USERDATA));
        return pThis->WndProc(hWnd, message, wParam, lParam);
    }
    }
    return 0;
}

LRESULT CALLBACK
PointerInputSample::WndProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam)
{
    try
    {
        switch (message)
        {
        case WM_POINTERDOWN:
        case WM_POINTERUPDATE:
        case WM_POINTERUP:
            ProcessPointerInput(wParam);
            break;
        case WM_TIMER:
            ProcessTimer();
            break;
        case WM_STOPINERTIA:
        case WM_ENDINERTIA:
            ProcessInertia(message);
            break;
        default:
            return ::DefWindowProc(hWnd, message, wParam, lParam);
        }
    }
    catch (...)
    {
        return 0;
    }
    return 0;
}

void
PointerInputSample::ProcessPointerInput(WPARAM wParam)
{
    UINT32 const pointerId = GET_POINTERID_WPARAM(wParam);
    POINTER_INFO info;
    THROW_IF_WIN32_BOOL_FALSE(::GetPointerInfo(pointerId, &info));

    // Filter to only touchpad pointer input.
    if (info.pointerType != PT_TOUCHPAD)
    {
        return;
    }

    // The full touchpad info can be queried via GetPointerTouchpadInfo, but
    // since we're just feeding the input into our InteractionContext, we want
    // to retrieve the basic POINTER_INFO data.
    UINT32 cFrames, cPointers;
    THROW_IF_WIN32_BOOL_FALSE(::GetPointerFrameTouchpadInfoHistory(
        pointerId,
        &cFrames,
        &cPointers,
        nullptr));

    auto pointerTouchInfos = std::make_unique<POINTER_TOUCH_INFO[]>(cFrames * cPointers);
    THROW_IF_WIN32_BOOL_FALSE(::GetPointerFrameTouchpadInfoHistory(
        pointerId,
        &cFrames,
        &cPointers,
        pointerTouchInfos.get()));

    // Copy the input frames into POINTER_TYPE_INFO structs.
    auto pointerTypeInfos = std::make_unique<POINTER_TYPE_INFO[]>(cFrames * cPointers);
    for (DWORD idx = 0; idx != cFrames * cPointers; ++idx)
    {
        pointerTypeInfos[idx].type = pointerTouchInfos[idx].pointerInfo.pointerType;
        pointerTypeInfos[idx].touchInfo = pointerTouchInfos[idx];
    }

    // Feed the input into our InteractionContext for gesture recognition.
    THROW_IF_FAILED(::ProcessPointerFramesInteractionContext2(
        m_interactionContext.get(),
        cFrames,
        cPointers,
        pointerTypeInfos.get()));

    // Skip the pointer messages associated with the rest of the frame.
    THROW_IF_WIN32_BOOL_FALSE(::SkipPointerFrameMessages(pointerId));
}

void
PointerInputSample::ProcessTimer()
{
    // When the inertia timer fires, we tell our IC to process inertia.
    THROW_IF_FAILED(::ProcessInertiaInteractionContext(m_interactionContext.get()));
}

void
PointerInputSample::ProcessInertia(UINT message)
{
    // WM_STOPINERTIA => the inertia animation should be stopped, but the content
    // being manipulated can remain in an inertial state for the purposes of
    // continuing the manipulation upon further input.
    // WM_ENDINERTIA => the inertia animation should be stopped and the content should
    // no longer be in an inertial state.
    std::printf("INERTIA MESSAGE: %s\n",
        (message == WM_STOPINERTIA) ? "WM_STOPINERTIA" : "WM_ENDINERTIA");
    THROW_IF_FAILED(::StopInteractionContext(m_interactionContext.get()));
}

void CALLBACK
PointerInputSample::OutputCallbackStatic(
    PVOID pvClient,
    const INTERACTION_CONTEXT_OUTPUT* pOutput)
{
    reinterpret_cast<PointerInputSample*>(pvClient)->OutputCallback(pOutput);
}

void
PointerInputSample::OutputCallback(const INTERACTION_CONTEXT_OUTPUT* pOutput)
{
    // Log the interaction flags to keep track of the manipulation's state.
    if (pOutput->interactionFlags != m_lastInteractionFlags)
    {
        m_lastInteractionFlags = pOutput->interactionFlags;
        if (m_lastInteractionFlags != INTERACTION_FLAG_NONE)
        {
            bool addedFlag = false;
            std::stringstream flags;
            auto checkFlag = [&](INTERACTION_FLAGS flag, std::string text)
            {
                if (WI_IsAnyFlagSet(m_lastInteractionFlags, flag))
                {
                    if (addedFlag)
                    {
                        flags << " | ";
                    }
                    addedFlag = true;
                    flags << text;
                }
            };
            checkFlag(INTERACTION_FLAG_BEGIN,   "BEGIN");
            checkFlag(INTERACTION_FLAG_END,     "END");
            checkFlag(INTERACTION_FLAG_CANCEL,  "CANCEL");
            checkFlag(INTERACTION_FLAG_INERTIA, "INERTIA");
            std::printf("INTERACTION OUTPUT: %s\n", flags.str().c_str());
        }
    }

    // If inertia is present in the output, ensure that our inertia timer
    // is running and that the inertia is reported to the OS.
    if (WI_IsFlagSet(pOutput->interactionFlags, INTERACTION_FLAG_INERTIA) &&
        (m_inertiaTimer == 0))
    {
        std::printf("<REPORTING INERTIA START>\n");
        m_inertiaTimer = ::SetTimer(m_hwnd.get(), 1, 15, nullptr);
        ::ReportWindowContentInertia(m_hwnd.get(), true);
    }

    // If the interaction is ending or no longer in inertia, cancel the
    // inertia timer and report the end of inertia to the OS.
    if ((m_inertiaTimer != 0) &&
        (WI_IsFlagSet(pOutput->interactionFlags, INTERACTION_FLAG_END) ||
         !WI_IsFlagSet(pOutput->interactionFlags, INTERACTION_FLAG_INERTIA)))
    {
        std::printf("<REPORTING INERTIA STOP>\n");
        ::KillTimer(m_hwnd.get(), m_inertiaTimer);
        m_inertiaTimer = 0;
        ::ReportWindowContentInertia(m_hwnd.get(), false);
    }
}
```

## Adding handlers for global touchpad gestures

This sample demonstrates how to listen for global touchpad gestures when in foreground.

### C++/WinRT example

```cpp
class GlobalGesturesSample :
    public winrt::implements<GlobalGesturesSample,
        winrt::Windows::Foundation::IInspectable>
{
public:
    void InitializeComponent();
    void final_release();

private:
    void OnGlobalActionPerformed(
        const winrt::Windows::UI::Input::TouchpadGesturesController& sender,
        const winrt::Windows::UI::Input::TouchpadGlobalActionEventArgs& args);
    void OnPointerPressed(
        const winrt::Windows::UI::Input::TouchpadGesturesController& sender,
        const winrt::Windows::UI::Core::PointerEventArgs& args);
    void OnPointerMoved(
        const winrt::Windows::UI::Input::TouchpadGesturesController& sender,
        const winrt::Windows::UI::Core::PointerEventArgs& args);
    void OnPointerReleased(
        const winrt::Windows::UI::Input::TouchpadGesturesController& sender,
        const winrt::Windows::UI::Core::PointerEventArgs& args);
    void OnManipulationCompleted(
        const winrt::Windows::UI::Input::PhysicalGestureRecognizer& sender,
        const winrt::Windows::UI::Input::ManipulationCompletedEventArgs& args);
    static LRESULT CALLBACK WndProcStatic(
        HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam);
    LRESULT CALLBACK WndProc(
        HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam);

private:
    winrt::Windows::UI::Input::TouchpadGesturesController m_controller = nullptr;
    winrt::Windows::UI::Input::PhysicalGestureRecognizer m_recognizer = nullptr;
    winrt::event_token m_globalActionEvent{};
    winrt::event_token m_pointerPressedEvent{};
    winrt::event_token m_pointerMovedEvent{};
    winrt::event_token m_pointerReleasedEvent{};
    winrt::event_token m_manipulationCompletedEvent{};
    wil::unique_hwnd m_hwnd = nullptr;
};

void
GlobalGesturesSample::InitializeComponent()
{
    // Create the TouchpadGesturesController and configure it to receive 3-finger
    // actions (taps and button presses) and manipulations (finger motion).
    THROW_HR_IF_FALSE(E_ABORT, winrt::TouchpadGesturesController::IsSupported());
    m_controller = winrt::TouchpadGesturesController::CreateForProcess();
    m_controller.Enabled(true);
    m_controller.SupportedGestures(
        winrt::TouchpadGlobalGestureKinds::ThreeFingerActions |
        winrt::TouchpadGlobalGestureKinds::ThreeFingerManipulations);

    m_globalActionEvent = m_controller.GlobalActionPerformed(
        { get_weak(), &GlobalGesturesSample::OnGlobalActionPerformed });
    m_pointerPressedEvent = m_controller.PointerPressed(
        { get_weak(), &GlobalGesturesSample::OnPointerPressed });
    m_pointerMovedEvent = m_controller.PointerMoved(
        { get_weak(), &GlobalGesturesSample::OnPointerMoved });
    m_pointerReleasedEvent = m_controller.PointerReleased(
        { get_weak(), &GlobalGesturesSample::OnPointerReleased });

    // Create the PhysicalGestureRecognizer. It will be used to recognize the pointer
    // input received for 3-finger manipulations.
    m_recognizer = winrt::PhysicalGestureRecognizer();
    m_recognizer.GestureSettings(
        winrt::GestureSettings::ManipulationTranslateX |
        winrt::GestureSettings::ManipulationTranslateY |
        winrt::GestureSettings::ManipulationTranslateRailsX |
        winrt::GestureSettings::ManipulationTranslateRailsY);
    m_manipulationCompletedEvent = m_recognizer.ManipulationCompleted(
        { get_weak(), &GlobalGesturesSample::OnManipulationCompleted });

    // Create and show a window. The TouchpadGesturesController can only receive
    // events if the current process is in foreground.
    WNDCLASSEX wcex = { sizeof(WNDCLASSEX) };
    wcex.hCursor = ::LoadCursor(nullptr, IDC_ARROW);
    wcex.lpszClassName = L"GlobalGesturesSampleClass";
    wcex.lpfnWndProc = WndProcStatic;
    m_hwnd.reset(::CreateWindow(
        MAKEINTATOM(::RegisterClassEx(&wcex)),
        L"Touchpad Global Gestures Sample",
        WS_OVERLAPPEDWINDOW | WS_VISIBLE,
        50, 250, 450, 150,
        nullptr, nullptr, nullptr, this));
    THROW_LAST_ERROR_IF_NULL(m_hwnd);
}

void
GlobalGesturesSample::final_release()
{
    m_controller.GlobalActionPerformed(m_globalActionEvent);
    m_controller.PointerPressed(m_globalActionEvent);
    m_controller.PointerMoved(m_globalActionEvent);
    m_controller.PointerReleased(m_globalActionEvent);
    m_recognizer.ManipulationCompleted(m_manipulationCompletedEvent);
}

LRESULT CALLBACK
GlobalGesturesSample::WndProcStatic(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam)
{
    switch (message)
    {
    case WM_CREATE:
    {
        CREATESTRUCT *pCreate = reinterpret_cast<CREATESTRUCT*>(lParam);
        auto pThis = reinterpret_cast<GlobalGesturesSample*>(pCreate->lpCreateParams);
        ::SetWindowLongPtr(hWnd, GWLP_USERDATA, reinterpret_cast<LONG_PTR>(pThis));
        break;
    }
    case WM_DESTROY:
    {
        ::PostQuitMessage(0);
        break;
    }
    default:
    {
        auto pThis = reinterpret_cast<GlobalGesturesSample*>(
            ::GetWindowLongPtr(hWnd, GWLP_USERDATA));
        return pThis->WndProc(hWnd, message, wParam, lParam);
    }
    }
    return 0;
}

LRESULT CALLBACK
GlobalGesturesSample::WndProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam)
{
    return ::DefWindowProc(hWnd, message, wParam, lParam);
}

void
GlobalGesturesSample::OnGlobalActionPerformed(
    const winrt::TouchpadGesturesController& /* sender */,
    const winrt::TouchpadGlobalActionEventArgs& args)
{
    winrt::TouchpadGlobalAction action = args.Action();
    switch (action)
    {
    case winrt::TouchpadGlobalAction::ThreeFingerTap:
        std::printf("<TAP>\n");
        break;
    case winrt::TouchpadGlobalAction::ThreeFingerPress:
        std::printf("<PRESS DOWN>\n");
        break;
    case winrt::TouchpadGlobalAction::ThreeFingerRelease:
        std::printf("<PRESS UP>\n");
        break;
    }
}

void
GlobalGesturesSample::OnPointerPressed(
    const winrt::Windows::UI::Input::TouchpadGesturesController& /* sender */,
    const winrt::Windows::UI::Core::PointerEventArgs& args)
{
    m_recognizer.ProcessDownEvent(args.CurrentPoint());
}

void
GlobalGesturesSample::OnPointerMoved(
    const winrt::Windows::UI::Input::TouchpadGesturesController& /* sender */,
    const winrt::Windows::UI::Core::PointerEventArgs& args)
{
    m_recognizer.ProcessMoveEvents(args.GetIntermediatePoints());
}

void
GlobalGesturesSample::OnPointerReleased(
    const winrt::Windows::UI::Input::TouchpadGesturesController& /* sender */,
    const winrt::Windows::UI::Core::PointerEventArgs& args)
{
    m_recognizer.ProcessUpEvent(args.CurrentPoint());
}

void
GlobalGesturesSample::OnManipulationCompleted(
    const winrt::Windows::UI::Input::PhysicalGestureRecognizer& /* sender */,
    const winrt::Windows::UI::Input::ManipulationCompletedEventArgs& args)
{
    auto motion = args.Cumulative();
    if (abs(motion.Translation.X) > abs(motion.Translation.Y))
    {
        std::printf((motion.Translation.X < 0) ? "<SWIPE LEFT>\n" : "<SWIPE RIGHT>\n");
    }
    else
    {
        std::printf((motion.Translation.Y < 0) ? "<SWIPE UP>\n" : "<SWIPE DOWN>\n");
    }
}
```

## Injecting touchpad input

This sample demonstrates how to inject touchpad input into the system.

### C++ example

```cpp
class InputInjectionSample :
    public winrt::implements<InputInjectionSample,
        winrt::Windows::Foundation::IInspectable>
{
public:
    void InitializeComponent();
    void InjectPan();
    void InjectTap();
    void Inject3FingerPressRelease();

private:
    void InjectInput(
        HSYNTHETICPOINTERDEVICE device,
        _In_reads_(cPoints) POINT* pStartingLocations,
        _In_reads_(cPoints) POINT* pStoppingLocations,
        DWORD cPoints,
        DWORD steps,
        DWORD durationMsPerStep);

private:
    using unique_synthetic_pointer_device =
        wil::unique_any<HSYNTHETICPOINTERDEVICE,
            decltype(&::DestroySyntheticPointerDevice),
            ::DestroySyntheticPointerDevice>;
    unique_synthetic_pointer_device m_touchpadGestureInjector;
    unique_synthetic_pointer_device m_touchpadGenericInjector;
    TOUCHPAD_PARAMETERS m_touchpadParams;
};

void
InputInjectionSample::InitializeComponent()
{
    // Create a touchpad injection device that's "gesture-only" - its input can
    // only be recognized as panning, zooming, or global manipulation-style gestures.
    SYNTHETIC_DEVICE_CREATION_PARAMS creationParams;
    creationParams.pointerType = PT_TOUCHPAD;
    creationParams.maxCount = 5;
    creationParams.feedbackMode = POINTER_FEEDBACK_NONE;
    creationParams.hMonitor = nullptr;
    creationParams.deviceWidth = 10000;
    creationParams.deviceHeight = 6000;
    creationParams.options = SDCO_PHYSICAL_SIZE |
        SDCO_TOUCHPAD_GESTURE_ONLY;
    m_touchpadGestureInjector.reset(::CreateSyntheticPointerDevice2(&creationParams));
    THROW_LAST_ERROR_IF_NULL(m_touchpadGestureInjector);

    // Create another touchpad with no gesturing restrictions.
    creationParams.options = SDCO_PHYSICAL_SIZE;
    m_touchpadGenericInjector.reset(::CreateSyntheticPointerDevice2(&creationParams));
    THROW_LAST_ERROR_IF_NULL(m_touchpadGenericInjector);

    // Check the user's current touchpad settings.
    TOUCHPAD_PARAMETERS params = {};
    params.versionNumber = TOUCHPAD_PARAMETERS_LATEST_VERSION;
    THROW_IF_WIN32_BOOL_FALSE(::SystemParametersInfo(
        SPI_GETTOUCHPADPARAMETERS, sizeof(params), &params, 0));
}

void
InputInjectionSample::InjectInput(
    HSYNTHETICPOINTERDEVICE device,
    _In_reads_(cPoints) POINT* pStartingLocations,
    _In_reads_(cPoints) POINT* pStoppingLocations,
    DWORD cPoints,
    DWORD steps,
    DWORD durationMsPerStep)
{
    auto injectedInfos = std::make_unique<POINTER_TYPE_INFO[]>(cPoints);

    for (DWORD idx = 0; idx != cPoints; ++idx)
    {
        auto& info = injectedInfos.get()[idx];
        auto& pointerInfo = info.touchInfo.pointerInfo;
        info.type = PT_TOUCHPAD;
        pointerInfo.pointerId = idx;
        pointerInfo.pointerFlags = POINTER_FLAG_INRANGE |
            POINTER_FLAG_INCONTACT |
            POINTER_FLAG_CONFIDENCE;
        pointerInfo.ptHimetricLocation.x = pStartingLocations[idx].x;
        pointerInfo.ptHimetricLocation.y = pStartingLocations[idx].y;
        info.touchInfo.pointerInfo.dwTime = 1;
    }
    THROW_IF_WIN32_BOOL_FALSE(::InjectSyntheticPointerInput(
        device, injectedInfos.get(), cPoints));

    for (DWORD step = 0; step != steps; ++step)
    {
        for (DWORD idx = 0; idx != cPoints; ++idx)
        {
            const auto xDist = pStoppingLocations[idx].x - pStartingLocations[idx].x;
            const auto yDist = pStoppingLocations[idx].y - pStartingLocations[idx].y;
            auto& pointerInfo = injectedInfos.get()[idx].touchInfo.pointerInfo;
            pointerInfo.ptHimetricLocation.x =
                pStartingLocations[idx].x + MulDiv(xDist, step + 1, steps);
            pointerInfo.ptHimetricLocation.y =
                pStartingLocations[idx].y + MulDiv(yDist, step + 1, steps);
            pointerInfo.dwTime += durationMsPerStep;
        }
        ::Sleep(durationMsPerStep);
        THROW_IF_WIN32_BOOL_FALSE(::InjectSyntheticPointerInput(
            device, injectedInfos.get(), cPoints));
    }

    for (DWORD idx = 0; idx != cPoints; ++idx)
    {
        auto& pointerInfo = injectedInfos.get()[idx].touchInfo.pointerInfo;
        pointerInfo.pointerFlags = POINTER_FLAG_CONFIDENCE;
        pointerInfo.dwTime += durationMsPerStep;
    }
    ::Sleep(durationMsPerStep);
    THROW_IF_WIN32_BOOL_FALSE(::InjectSyntheticPointerInput(
        device, injectedInfos.get(), cPoints));
}

void
InputInjectionSample::InjectPan()
{
    POINT* gestureStart;
    POINT* gestureStop;
    POINT gestureBottom[] = { POINT{ 3000, 5000 }, POINT{ 7000, 5000 } };
    POINT gestureTop[] = { POINT{ 3000, 1000 }, POINT{ 7000, 1000 } };

    if (m_touchpadParams.scrollDirectionReversed)
    {
        gestureStart = gestureTop;
        gestureStop = gestureBottom;
    }
    else
    {
        gestureStart = gestureBottom;
        gestureStop = gestureTop;
    }

    InjectInput(m_touchpadGestureInjector.get(),
        gestureStart, gestureStop,
        2, 10, 10);
}

void
InputInjectionSample::InjectTap()
{
    POINT tapStartStop = POINT{ 5000, 3000 };
    InjectInput(m_touchpadGenericInjector.get(),
        &tapStartStop, &tapStartStop,
        1, 5, 10);
}

void
InputInjectionSample::Inject3FingerPressRelease()
{
    THROW_IF_WIN32_BOOL_FALSE(::InjectTouchpadAction(
        m_touchpadGenericInjector.get(), TA_3FINGER_PRESS));
    THROW_IF_WIN32_BOOL_FALSE(::InjectTouchpadAction(
        m_touchpadGenericInjector.get(), TA_3FINGER_RELEASE));
}
```

## Related topics

- [**RegisterTouchpadCapableWindow**](registertouchpadcapable.md)
- [**GetPointerTouchpadInfo**](getpointertouchpadinfo.md)
- [**ReportWindowContentInertia**](reportwindowcontentinertia.md)
- [**ProcessPointerFramesInteractionContext2**](processpointerframesinteractioncontext2.md)
- [**TouchpadGesturesController**](touchpadgesturescontroller.md)
- [**PhysicalGestureRecognizer**](physicalgesturerecognizer.md)
- [**CreateSyntheticPointerDevice2**](createsyntheticpointerdevice2.md)
- [**InjectTouchpadAction**](injecttouchpadaction.md)
- [Precision Touchpad Reference](precision-touchpad-reference.md)
- [Precision Touchpad Input](precision-touchpad-portal.md)

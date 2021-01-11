---
description: This tutorial presents a complete application that plays video using MFPlay.
ms.assetid: f72a7c1f-b059-474c-96f2-8fad3b1f7035
title: 'MFPlay Tutorial: Video Playback'
ms.topic: article
ms.date: 05/31/2018
---

# MFPlay Tutorial: Video Playback

\[MFPlay is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

This tutorial presents a complete application that plays video using MFPlay. It is based on the [SimplePlay](simpleplay-sample.md) SDK sample.

This tutorial contains the following sections:

-   [Requirements](#requirements)
-   [Header and Library Files](#header-and-library-files)
-   [Global Variables](#global-variables)
-   [Declare the Callback Class](#declare-the-callback-class)
-   [Declare the SafeRelease Function](#declare-the-saferelease-function)
-   [Open a Media File](#open-a-media-file)
-   [Window Message Handlers](#window-message-handlers)
-   [Implement the Callback Method](#implement-the-callback-method)
-   [Implement WinMain](#implement-winmain)
-   [Related topics](#related-topics)

For a more detailed discussion of the MFPlay API, see [Getting Started with MFPlay](getting-started-with-mfplay.md).

## Requirements

MFPlay requires Windows 7.

## Header and Library Files

Include the following header files in your project:


```C++
#define WINVER _WIN32_WINNT_WIN7

#include <new>
#include <windows.h>
#include <windowsx.h>
#include <mfplay.h>
#include <mferror.h>
#include <shobjidl.h>   // defines IFileOpenDialog
#include <strsafe.h>
#include <Shlwapi.h>
```



Link to the following code libraries:

-   mfplay.lib
-   shlwapi.lib

## Global Variables

Declare the following global variables:


```C++
IMFPMediaPlayer         *g_pPlayer = NULL;      // The MFPlay player object.
MediaPlayerCallback     *g_pPlayerCB = NULL;    // Application callback object.

BOOL                    g_bHasVideo = FALSE;
```



These variables will be used as follows:

<dl> <dt>

<span id="g_hwnd"></span><span id="G_HWND"></span>*g\_hwnd*
</dt> <dd>

A handle to the application window.

</dd> <dt>

<span id="g_bVideo"></span><span id="g_bvideo"></span><span id="G_BVIDEO"></span>*g\_bVideo*
</dt> <dd>

A Boolean value that tracks whether video is playing.

</dd> <dt>

<span id="g_pPlayer"></span><span id="g_pplayer"></span><span id="G_PPLAYER"></span>*g\_pPlayer*
</dt> <dd>

A pointer to the [**IMFPMediaPlayer**](/windows/desktop/api/mfplay/nn-mfplay-imfpmediaplayer) interface. This interface is used to control playback.

</dd> <dt>

<span id="g_pCallback"></span><span id="g_pcallback"></span><span id="G_PCALLBACK"></span>*g\_pCallback*
</dt> <dd>

A pointer to the [**IMFPMediaPlayerCallback**](/windows/desktop/api/mfplay/nn-mfplay-imfpmediaplayercallback) interface. The application implements this callback interface to get notifications from the player object.

</dd> </dl>

## Declare the Callback Class

To get event notifications from the player object, the application must implement the [**IMFPMediaPlayerCallback**](/windows/desktop/api/mfplay/nn-mfplay-imfpmediaplayercallback) interface. The following code declares a class that implements the interface. The only member variable is *m\_cRef*, which stores the reference count.

The **IUnknown** methods are implemented inline. The implementation of the [**IMFPMediaPlayerCallback::OnMediaPlayerEvent**](/windows/desktop/api/mfplay/nf-mfplay-imfpmediaplayercallback-onmediaplayerevent) method is shown later; see [Implement the Callback Method](#implement-the-callback-method).


```C++
// Implements the callback interface for MFPlay events.

class MediaPlayerCallback : public IMFPMediaPlayerCallback
{
    long m_cRef; // Reference count

public:

    MediaPlayerCallback() : m_cRef(1)
    {
    }

    IFACEMETHODIMP QueryInterface(REFIID riid, void** ppv)
    {
        static const QITAB qit[] =
        {
            QITABENT(MediaPlayerCallback, IMFPMediaPlayerCallback),
            { 0 },
        };
        return QISearch(this, qit, riid, ppv);
    }

    IFACEMETHODIMP_(ULONG) AddRef()
    {
        return InterlockedIncrement(&m_cRef);
    }

    IFACEMETHODIMP_(ULONG) Release()
    {
        ULONG count = InterlockedDecrement(&m_cRef);
        if (count == 0)
        {
            delete this;
            return 0;
        }
        return count;
    }

    // IMFPMediaPlayerCallback methods
    IFACEMETHODIMP_(void) OnMediaPlayerEvent(MFP_EVENT_HEADER *pEventHeader);
};
```



## Declare the SafeRelease Function

Throughout this tutorial, the [SafeRelease](saferelease.md) function is used to release interface pointers:


```C++
template <class T> void SafeRelease(T **ppT)
{
    if (*ppT)
    {
        (*ppT)->Release();
        *ppT = NULL;
    }
}
```



## Open a Media File

The `PlayMediaFile` function opens a media file, as follows:

1.  If *g\_pPlayer* is **NULL**, the function calls [**MFPCreateMediaPlayer**](/windows/desktop/api/mfplay/nf-mfplay-mfpcreatemediaplayer) to create a new instance of the media player object. The input parameters to **MFPCreateMediaPlayer** include a pointer to the callback interface and a handle to the video window.
2.  To open the media file, the function calls [**IMFPMediaPlayer::CreateMediaItemFromURL**](/windows/desktop/api/mfplay/nf-mfplay-imfpmediaplayer-createmediaitemfromurl), passing in the URL of the file. This method completes asynchronously. When it completes, the application's [**IMFPMediaPlayerCallback::OnMediaPlayerEvent**](/windows/desktop/api/mfplay/nf-mfplay-imfpmediaplayercallback-onmediaplayerevent) method is called.


```C++
HRESULT PlayMediaFile(HWND hwnd, PCWSTR pszURL)
{
    HRESULT hr = S_OK;

    // Create the MFPlayer object.
    if (g_pPlayer == NULL)
    {
        g_pPlayerCB = new (std::nothrow) MediaPlayerCallback();

        if (g_pPlayerCB == NULL)
        {
            return E_OUTOFMEMORY;
        }

        hr = MFPCreateMediaPlayer(
            NULL,
            FALSE,          // Start playback automatically?
            0,              // Flags
            g_pPlayerCB,    // Callback pointer
            hwnd,           // Video window
            &g_pPlayer
            );
    }

    // Create a new media item for this URL.

    if (SUCCEEDED(hr))
    {
        hr = g_pPlayer->CreateMediaItemFromURL(pszURL, FALSE, 0, NULL);
    }

    // The CreateMediaItemFromURL method completes asynchronously.
    // The application will receive an MFP_EVENT_TYPE_MEDIAITEM_CREATED
    // event. See MediaPlayerCallback::OnMediaPlayerEvent().

    return hr;
}
```



The `OnFileOpen` function displays the common file dialog, which enables the user to select a file for playback. The **IFileOpenDialog** interface is used to display the common file dialog. This interface is part of the Windows Shell APIs; it was introduced in Windows Vista as a replacement for the older **GetOpenFileName** function. After the user selects a file, `OnFileOpen` calls `PlayMediaFile` to start playback.


```C++
void OnFileOpen(HWND hwnd)
{
    IFileOpenDialog *pFileOpen = NULL;
    IShellItem *pItem = NULL;
    PWSTR pwszFilePath = NULL;

    // Create the FileOpenDialog object.
    HRESULT hr = CoCreateInstance(__uuidof(FileOpenDialog), NULL,
        CLSCTX_INPROC_SERVER, IID_PPV_ARGS(&pFileOpen));
    if (SUCCEEDED(hr))
    {
        hr = pFileOpen->SetTitle(L"Select a File to Play");
    }

    // Show the file-open dialog.
    if (SUCCEEDED(hr))
    {
        hr = pFileOpen->Show(hwnd);
    }

    if (hr == HRESULT_FROM_WIN32(ERROR_CANCELLED))
    {
        // User canceled.
        SafeRelease(&pFileOpen);
        return;
    }

    // Get the file name from the dialog.
    if (SUCCEEDED(hr))
    {
        hr = pFileOpen->GetResult(&pItem);
    }

    if (SUCCEEDED(hr))
    {
       hr = pItem->GetDisplayName(SIGDN_URL, &pwszFilePath);
    }

    // Open the media file.
    if (SUCCEEDED(hr))
    {
        hr = PlayMediaFile(hwnd, pwszFilePath);
    }

    if (FAILED(hr))
    {
        ShowErrorMessage(L"Could not open file.", hr);
    }

    CoTaskMemFree(pwszFilePath);

    SafeRelease(&pItem);
    SafeRelease(&pFileOpen);
}
```



## Window Message Handlers

Next, declare message handlers for the following window messages:

-   **WM\_PAINT**
-   **WM\_SIZE**
-   **WM\_CLOSE**

For the **WM\_PAINT** message, you must track whether video is currently playing. If so, call the [**IMFPMediaPlayer::UpdateVideo**](/windows/desktop/api/mfplay/nf-mfplay-imfpmediaplayer-updatevideo) method. This method causes the player object to redraw the most recent video frame.

If there is no video, the application is responsible for painting the window. For this tutorial, the application simply calls the GDI **FillRect** function to fill the entire client area.


```C++
void OnPaint(HWND hwnd)
{
    PAINTSTRUCT ps;
    HDC hdc = BeginPaint(hwnd, &ps);

    if (g_pPlayer && g_bHasVideo)
    {
        // Playback has started and there is video.

        // Do not draw the window background, because the video
        // frame fills the entire client area.

        g_pPlayer->UpdateVideo();
    }
    else
    {
        // There is no video stream, or playback has not started.
        // Paint the entire client area.

        FillRect(hdc, &ps.rcPaint, (HBRUSH) (COLOR_WINDOW+1));
    }

    EndPaint(hwnd, &ps);
}
```



For the **WM\_SIZE** message, call [**IMFPMediaPlayer::UpdateVideo**](/windows/desktop/api/mfplay/nf-mfplay-imfpmediaplayer-updatevideo). This method causes the player object to readjust the video to match the current size of the window. Note that **UpdateVideo** is used for both **WM\_PAINT** and **WM\_SIZE**.


```C++
void OnSize(HWND /*hwnd*/, UINT state, int /*cx*/, int /*cy*/)
{
    if (state == SIZE_RESTORED)
    {
        if (g_pPlayer)
        {
            // Resize the video.
            g_pPlayer->UpdateVideo();
        }
    }
}
```



For the **WM\_CLOSE** message, release the [**IMFPMediaPlayer**](/windows/desktop/api/mfplay/nn-mfplay-imfpmediaplayer) and [**IMFPMediaPlayerCallback**](/windows/desktop/api/mfplay/nn-mfplay-imfpmediaplayercallback) pointers.


```C++
void OnClose(HWND /*hwnd*/)
{
    SafeRelease(&g_pPlayer);
    SafeRelease(&g_pPlayerCB);
    PostQuitMessage(0);
}
```



## Implement the Callback Method

The [**IMFPMediaPlayerCallback**](/windows/desktop/api/mfplay/nn-mfplay-imfpmediaplayercallback) interface defines a single method, [**OnMediaPlayerEvent**](/windows/desktop/api/mfplay/nf-mfplay-imfpmediaplayercallback-onmediaplayerevent). This method notifies the application whenever an event occurs during playback. The method takes one parameter, a pointer to an [**MFP\_EVENT\_HEADER**](/windows/desktop/api/mfplay/ns-mfplay-mfp_event_header) structure. The **eEventType** member of the structure specifies the event that occurred.

The [**MFP\_EVENT\_HEADER**](/windows/desktop/api/mfplay/ns-mfplay-mfp_event_header) structure may be followed by additional data. For each event type, a macro is defined that casts the **MFP\_EVENT\_HEADER** pointer to an event-specific structure. (See [**MFP\_EVENT\_TYPE**](/windows/desktop/api/mfplay/ne-mfplay-mfp_event_type).)

For this tutorial, two events are significant:



| Event                                    | Description                                                                                       |
|------------------------------------------|---------------------------------------------------------------------------------------------------|
| **MFP\_EVENT\_TYPE\_MEDIAITEM\_CREATED** | Sent when the [**CreateMediaItemFromURL**](/windows/desktop/api/mfplay/nf-mfplay-imfpmediaplayer-createmediaitemfromurl) completes. |
| **MFP\_EVENT\_TYPE\_MEDIAITEM\_SET**     | Sent when [**SetMediaItem**](/windows/desktop/api/mfplay/nf-mfplay-imfpmediaplayer-setmediaitem) completes.                         |



 

The following code shows how to cast the [**MFP\_EVENT\_HEADER**](/windows/desktop/api/mfplay/ns-mfplay-mfp_event_header) pointer to the event-specific structure.


```C++
void MediaPlayerCallback::OnMediaPlayerEvent(MFP_EVENT_HEADER * pEventHeader)
{
    if (FAILED(pEventHeader->hrEvent))
    {
        ShowErrorMessage(L"Playback error", pEventHeader->hrEvent);
        return;
    }

    switch (pEventHeader->eEventType)
    {
    case MFP_EVENT_TYPE_MEDIAITEM_CREATED:
        OnMediaItemCreated(MFP_GET_MEDIAITEM_CREATED_EVENT(pEventHeader));
        break;

    case MFP_EVENT_TYPE_MEDIAITEM_SET:
        OnMediaItemSet(MFP_GET_MEDIAITEM_SET_EVENT(pEventHeader));
        break;
    }
}
```



The **MFP\_EVENT\_TYPE\_MEDIAITEM\_CREATED** event notifies the application that the [**IMFPMediaPlayer::CreateMediaItemFromURL**](/windows/desktop/api/mfplay/nf-mfplay-imfpmediaplayer-createmediaitemfromurl) method has completed. The event structure contains a pointer to the [**IMFPMediaItem**](/windows/desktop/api/mfplay/nn-mfplay-imfpmediaitem) interface, which represents the media item created from the URL. To queue the item for playback, pass this pointer to the [**IMFPMediaPlayer::SetMediaItem**](/windows/desktop/api/mfplay/nf-mfplay-imfpmediaplayer-setmediaitem) method:


```C++
void OnMediaItemCreated(MFP_MEDIAITEM_CREATED_EVENT *pEvent)
{
    // The media item was created successfully.

    if (g_pPlayer)
    {
        BOOL    bHasVideo = FALSE;
        BOOL    bIsSelected = FALSE;

        // Check if the media item contains video.
        HRESULT hr = pEvent->pMediaItem->HasVideo(&bHasVideo, &bIsSelected);
        if (SUCCEEDED(hr))
        {
            g_bHasVideo = bHasVideo && bIsSelected;

            // Set the media item on the player. This method completes
            // asynchronously.
            hr = g_pPlayer->SetMediaItem(pEvent->pMediaItem);
        }

        if (FAILED(hr))
        {
            ShowErrorMessage(L"Error playing this file.", hr);
        }
   }
}
```



The **MFP\_EVENT\_TYPE\_MEDIAITEM\_SET** event notifies the application that [**SetMediaItem**](/windows/desktop/api/mfplay/nf-mfplay-imfpmediaplayer-setmediaitem) has completed. Call [**IMFPMediaPlayer::Play**](/windows/desktop/api/mfplay/nf-mfplay-imfpmediaplayer-play) to start playback:


```C++
void OnMediaItemSet(MFP_MEDIAITEM_SET_EVENT * /*pEvent*/)
{
    HRESULT hr = g_pPlayer->Play();
    if (FAILED(hr))
    {
        ShowErrorMessage(L"IMFPMediaPlayer::Play failed.", hr);
    }
}
```



## Implement WinMain

In the remainder of this tutorial, there are no calls to Media Foundation APIs. The following code shows the window procedure:


```C++
LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    switch (uMsg)
    {
        HANDLE_MSG(hwnd, WM_CLOSE,   OnClose);
        HANDLE_MSG(hwnd, WM_PAINT,   OnPaint);
        HANDLE_MSG(hwnd, WM_COMMAND, OnCommand);
        HANDLE_MSG(hwnd, WM_SIZE,    OnSize);

    case WM_ERASEBKGND:
        return 1;

    default:
        return DefWindowProc(hwnd, uMsg, wParam, lParam);
    }
}
```



The `InitializeWindow` function registers the application's window class and creates the window.


```C++
BOOL InitializeWindow(HWND *pHwnd)
{
    const wchar_t CLASS_NAME[]  = L"MFPlay Window Class";
    const wchar_t WINDOW_NAME[] = L"MFPlay Sample Application";

    WNDCLASS wc = {};

    wc.lpfnWndProc   = WindowProc;
    wc.hInstance     = GetModuleHandle(NULL);
    wc.hCursor       = LoadCursor(NULL, IDC_ARROW);
    wc.lpszClassName = CLASS_NAME;
    wc.lpszMenuName  = MAKEINTRESOURCE(IDR_MENU1);

    RegisterClass(&wc);

    HWND hwnd = CreateWindow(
        CLASS_NAME, WINDOW_NAME, WS_OVERLAPPEDWINDOW,
        CW_USEDEFAULT, CW_USEDEFAULT, CW_USEDEFAULT, CW_USEDEFAULT,
        NULL, NULL, GetModuleHandle(NULL), NULL);

    if (!hwnd)
    {
        return FALSE;
    }

    ShowWindow(hwnd, SW_SHOWDEFAULT);
    UpdateWindow(hwnd);

    *pHwnd = hwnd;

    return TRUE;
}
```



Finally, implement the application entry point:


```C++
int WINAPI wWinMain(HINSTANCE, HINSTANCE, PWSTR, int)
{
    HeapSetInformation(NULL, HeapEnableTerminationOnCorruption, NULL, 0);

    HRESULT hr = CoInitializeEx(NULL,
        COINIT_APARTMENTTHREADED | COINIT_DISABLE_OLE1DDE);

    if (FAILED(hr))
    {
        return 0;
    }

    HWND hwnd = NULL;
    if (InitializeWindow(&hwnd))
    {
        // Message loop
        MSG msg = {};
        while (GetMessage(&msg, NULL, 0, 0))
        {
            TranslateMessage(&msg);
            DispatchMessage(&msg);
        }

        DestroyWindow(hwnd);
    }
    CoUninitialize();

    return 0;
}
```



## Related topics

<dl> <dt>

[Using MFPlay for Audio/Video Playback](using-mfplay-for-audio-video-playback.md)
</dt> </dl>

 

 




---
description: This topic contains code for the tutorial How to Play Media Files with Media Foundation.
ms.assetid: f13cba48-bfb6-4964-a9de-004cbb5c0dce
title: winmain.cpp
ms.topic: article
ms.date: 05/31/2018
---

# winmain.cpp

This topic contains code for the tutorial [How to Play Media Files with Media Foundation](how-to-play-unprotected-media-files.md).


```C++
// THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
// ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
// THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
// PARTICULAR PURPOSE.
//
// Copyright (c) Microsoft Corporation. All rights reserved.

#include "Player.h"

PCWSTR szTitle = L"BasicPlayback";
PCWSTR szWindowClass = L"MFBASICPLAYBACK";

HINSTANCE   g_hInstance;                        // current instance
BOOL        g_bRepaintClient = TRUE;            // Repaint the application client area?
CPlayer     *g_pPlayer = NULL;                  // Global player object. 

// Note: After WM_CREATE is processed, g_pPlayer remains valid until the
// window is destroyed.

// Forward declarations of functions included in this code module:
BOOL                InitInstance(HINSTANCE, int);
LRESULT CALLBACK    WndProc(HWND, UINT, WPARAM, LPARAM);
INT_PTR CALLBACK    OpenUrlDialogProc(HWND, UINT, WPARAM, LPARAM);
void                NotifyError(HWND hwnd, const WCHAR *sErrorMessage, HRESULT hr);
void                UpdateUI(HWND hwnd, PlayerState state);
HRESULT             AllocGetWindowText(HWND hwnd, WCHAR **pszText, DWORD *pcchLen);

// Message handlers
LRESULT             OnCreateWindow(HWND hwnd);
void                OnFileOpen(HWND hwnd);
void                OnOpenURL(HWND hwnd);
void                OnPlayerEvent(HWND hwnd, WPARAM pUnkPtr);
void                OnPaint(HWND hwnd);
void                OnResize(WORD width, WORD height);
void                OnKeyPress(WPARAM key);

// OpenUrlDialogInfo: Contains data passed to the "Open URL" dialog proc.
struct OpenUrlDialogInfo
{
    WCHAR *pszURL;
    DWORD cch;
};

int WINAPI wWinMain(HINSTANCE hInstance, HINSTANCE, PWSTR, int nCmdShow)
{
    HeapSetInformation(NULL, HeapEnableTerminationOnCorruption, NULL, 0);

    MSG msg;

    ZeroMemory(&msg, sizeof(msg));

    // Perform application initialization.
    if (!InitInstance(hInstance, nCmdShow))
    {
        NotifyError(NULL, L"Could not initialize the application.", 
            HRESULT_FROM_WIN32(GetLastError()));
        return FALSE;
    }

    // Main message loop.
    while (GetMessage(&msg, NULL, 0, 0))
    {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    // Clean up.
    if (g_pPlayer)
    {
        g_pPlayer->Shutdown();
        SafeRelease(&g_pPlayer);
    }
    return 0;
}

//  Create the application window.
BOOL InitInstance(HINSTANCE hInst, int nCmdShow)
{
    HWND hwnd;
    WNDCLASSEX wcex;

    g_hInstance = hInst; // Store the instance handle.

    // Register the window class.
    ZeroMemory(&wcex, sizeof(WNDCLASSEX));
    wcex.cbSize         = sizeof(WNDCLASSEX);
    wcex.style          = CS_HREDRAW | CS_VREDRAW;
    wcex.lpfnWndProc    = WndProc;
    wcex.hInstance      = hInst;
    wcex.hbrBackground  = (HBRUSH)(COLOR_WINDOW+1);
    wcex.lpszMenuName   = MAKEINTRESOURCE(IDC_MFPLAYBACK);
    wcex.lpszClassName  = szWindowClass;

    if (RegisterClassEx(&wcex) == 0)
    {
        return FALSE;
    }

    // Create the application window.
    hwnd = CreateWindow(szWindowClass, szTitle, WS_OVERLAPPEDWINDOW,
        CW_USEDEFAULT, 0, CW_USEDEFAULT, 0, NULL, NULL, hInst, NULL);

    if (hwnd == 0)
    {
        return FALSE;
    }

    ShowWindow(hwnd, nCmdShow);
    UpdateWindow(hwnd);

    return TRUE;
}


//  Message handler for the main window.

LRESULT CALLBACK WndProc(HWND hwnd, UINT message, WPARAM wParam, LPARAM lParam)
{
    switch (message)
    {
    case WM_CREATE:
        return OnCreateWindow(hwnd);

    case WM_COMMAND:
        switch (LOWORD(wParam))
        {
        case IDM_EXIT:
            DestroyWindow(hwnd);
            break;
        case ID_FILE_OPENFILE:
            OnFileOpen(hwnd);
            break;
        case ID_FILE_OPENURL:
            OnOpenURL(hwnd);
            break;

        default:
            return DefWindowProc(hwnd, message, wParam, lParam);
        }
        break;

    case WM_PAINT:
        OnPaint(hwnd);
        break;

    case WM_SIZE:
        OnResize(LOWORD(lParam), HIWORD(lParam));
        break;

    case WM_ERASEBKGND:
        // Suppress window erasing, to reduce flickering while the video is playing.
        return 1;

    case WM_DESTROY:
        PostQuitMessage(0);
        break;

    case WM_CHAR:
        OnKeyPress(wParam);
        break;

    case WM_APP_PLAYER_EVENT:
        OnPlayerEvent(hwnd, wParam);
        break;

    default:
        return DefWindowProc(hwnd, message, wParam, lParam);
    }
    return 0;
}

//  Open an audio/video file.
void OnFileOpen(HWND hwnd)
{
    IFileOpenDialog *pFileOpen = NULL;
    IShellItem *pItem = NULL;
    PWSTR pszFilePath = NULL;

    // Create the FileOpenDialog object.
    HRESULT hr = CoCreateInstance(__uuidof(FileOpenDialog), NULL, 
        CLSCTX_INPROC_SERVER, IID_PPV_ARGS(&pFileOpen));
    if (FAILED(hr))
    {
        goto done;
    }

    // Show the Open dialog box.
    hr = pFileOpen->Show(NULL);
    if (hr == HRESULT_FROM_WIN32(ERROR_CANCELLED))
    {
        // The user canceled the dialog. Do not treat as an error.
        hr = S_OK;
        goto done;
    }
    else if (FAILED(hr))
    {
        goto done;
    }

    // Get the file name from the dialog box.
    hr = pFileOpen->GetResult(&pItem);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pItem->GetDisplayName(SIGDN_FILESYSPATH, &pszFilePath);
    if (FAILED(hr))
    {
        goto done;
    }

    // Display the file name to the user.
    hr = g_pPlayer->OpenURL(pszFilePath);
    if (SUCCEEDED(hr))
    {
        UpdateUI(hwnd, OpenPending);
    }

done:
    if (FAILED(hr))
    {
        NotifyError(hwnd, L"Could not open the file.", hr);
        UpdateUI(hwnd, Closed);
    }
    CoTaskMemFree(pszFilePath);
    SafeRelease(&pItem);
    SafeRelease(&pFileOpen);
}

//  Open a media file from a URL.
void OnOpenURL(HWND hwnd)
{
    HRESULT hr = S_OK;

    // Pass in an OpenUrlDialogInfo structure to the dialog. The dialog 
    // fills in this structure with the URL. The dialog proc allocates
    // the memory for the string. 

    OpenUrlDialogInfo url;
    ZeroMemory(&url, sizeof(&url));

    // Show the Open URL dialog.
    if (IDOK == DialogBoxParam(g_hInstance, MAKEINTRESOURCE(IDD_OPENURL), hwnd,
        OpenUrlDialogProc, (LPARAM)&url))
    {
        // Open the file with the playback object.
        hr = g_pPlayer->OpenURL(url.pszURL);
        if (SUCCEEDED(hr))
        {
            UpdateUI(hwnd, OpenPending);
        }
        else
        {
            NotifyError(hwnd, L"Could not open this URL.", hr);
            UpdateUI(hwnd, Closed);
        }
    }

    // The caller must free the URL string.
    CoTaskMemFree(url.pszURL);
}

//  Handler for WM_CREATE message.
LRESULT OnCreateWindow(HWND hwnd)
{
    // Initialize the player object.
    HRESULT hr = CPlayer::CreateInstance(hwnd, hwnd, &g_pPlayer); 
    if (SUCCEEDED(hr))
    {
        UpdateUI(hwnd, Closed);
        return 0;   // Success.
    }
    else
    {
        NotifyError(NULL, L"Could not initialize the player object.", hr);
        return -1;  // Destroy the window
    }
}

//  Handler for WM_PAINT messages.
void OnPaint(HWND hwnd)
{
    PAINTSTRUCT ps;
    HDC hdc = BeginPaint(hwnd, &ps);

    if (g_pPlayer && g_pPlayer->HasVideo())
    {
        // Video is playing. Ask the player to repaint.
        g_pPlayer->Repaint();
    }
    else
    {
        // The video is not playing, so we must paint the application window.
        RECT rc;
        GetClientRect(hwnd, &rc);
        FillRect(hdc, &rc, (HBRUSH) COLOR_WINDOW);
    }
    EndPaint(hwnd, &ps);
}

//  Handler for WM_SIZE messages.
void OnResize(WORD width, WORD height)
{
    if (g_pPlayer)
    {
        g_pPlayer->ResizeVideo(width, height);
    }
}


// Handler for WM_CHAR messages. 
void OnKeyPress(WPARAM key)
{
    switch (key)
    {
    // Space key toggles between running and paused
    case VK_SPACE:
        if (g_pPlayer->GetState() == Started)
        {
            g_pPlayer->Pause();
        }
        else if (g_pPlayer->GetState() == Paused)
        {
            g_pPlayer->Play();
        }
        break;
    }
}

// Handler for Media Session events.
void OnPlayerEvent(HWND hwnd, WPARAM pUnkPtr)
{
    HRESULT hr = g_pPlayer->HandleEvent(pUnkPtr);
    if (FAILED(hr))
    {
        NotifyError(hwnd, L"An error occurred.", hr);
    }
    UpdateUI(hwnd, g_pPlayer->GetState());
}


// Update the application UI to reflect the current state.

void UpdateUI(HWND hwnd, PlayerState state)
{
    BOOL bWaiting = FALSE;
    BOOL bPlayback = FALSE;

    assert(g_pPlayer != NULL);

    switch (state)
    {
    case OpenPending:
        bWaiting = TRUE;
        break;

    case Started:
        bPlayback = TRUE;
        break;

    case Paused:
        bPlayback = TRUE;
        break;
    }

    HMENU hMenu = GetMenu(hwnd);
    UINT  uEnable = MF_BYCOMMAND | (bWaiting ? MF_GRAYED : MF_ENABLED);

    EnableMenuItem(hMenu, ID_FILE_OPENFILE, uEnable);
    EnableMenuItem(hMenu, ID_FILE_OPENURL, uEnable);

    if (bPlayback && g_pPlayer->HasVideo())
    {
        g_bRepaintClient = FALSE;
    }
    else
    {
        g_bRepaintClient = TRUE;
    }
}

//  Show a message box with an error message.
void NotifyError(HWND hwnd, PCWSTR pszErrorMessage, HRESULT hrErr)
{
    const size_t MESSAGE_LEN = 512;
    WCHAR message[MESSAGE_LEN];

    if (SUCCEEDED(StringCchPrintf(message, MESSAGE_LEN, L"%s (HRESULT = 0x%X)", 
        pszErrorMessage, hrErr)))
    {
        MessageBox(hwnd, message, NULL, MB_OK | MB_ICONERROR);
    }
}


//  Dialog proc for the "Open URL" dialog.
INT_PTR CALLBACK OpenUrlDialogProc(HWND hDlg, UINT message, WPARAM wParam, LPARAM lParam)
{
    static OpenUrlDialogInfo *pUrl = NULL;

    BOOL result = FALSE;

    switch (message)
    {
    case WM_INITDIALOG:
        // The caller sends a pointer to an OpenUrlDialogInfo structure as the 
        // lParam. This structure stores the URL.
        pUrl = (OpenUrlDialogInfo*)lParam;
        return (INT_PTR)TRUE;

    case WM_COMMAND:
        switch (LOWORD(wParam))
        {
        case IDOK:
            if (pUrl)
            {
                // Get the URL from the edit box in the dialog. This function 
                // allocates memory. The caller must call CoTaskMemAlloc.
                if (SUCCEEDED(AllocGetWindowText(GetDlgItem(hDlg, IDC_EDIT_URL), 
                    &pUrl->pszURL, &pUrl->cch)))
                {
                    result = TRUE;
                }
            }
            EndDialog(hDlg, result ? IDOK : IDABORT);
            break;

        case IDCANCEL:
            EndDialog(hDlg, LOWORD(IDCANCEL));
            break;
        }
        return (INT_PTR)FALSE;
    }
    return (INT_PTR)FALSE;
}

// Helper function to get text from a window.
//
// This function allocates a buffer and returns it in pszText. The caller must
// call CoTaskMemFree on the buffer.
//
// hwnd:     Handle to the window.
// pszText:  Receives a pointer to the string.
// pcchLen:  Receives the length of the string, in characters, not including
//           the terminating NULL character. 

HRESULT AllocGetWindowText(HWND hwnd, WCHAR **pszText, DWORD *pcchLen)
{
    if (pszText == NULL || pcchLen == NULL)
    {
        return E_POINTER;
    }

    *pszText = NULL;  

    int cch = GetWindowTextLength(hwnd);  
    if (cch < 0) 
    {
        return E_UNEXPECTED; 
    }

    PWSTR pszTmp = (PWSTR)CoTaskMemAlloc(sizeof(WCHAR) * (cch + 1)); 
    // Includes room for terminating NULL character

    if (!pszTmp)
    {
        return E_OUTOFMEMORY;
    }

    if (cch == 0)
    {
        pszTmp[0] = L'\0';  // No text.
    }
    else
    {
        int res = GetWindowText(hwnd, pszTmp, (cch + 1));  
        // Size includes terminating null character.

        // GetWindowText returns 0 if (a) there is no text or (b) it failed.
        // We checked for (a) already, so 0 means failure here.
        if (res == 0)
        {
            CoTaskMemFree(pszTmp);
            return __HRESULT_FROM_WIN32(GetLastError());
        }
    }

    // If we got here, szTmp is valid, so return it to the caller.
    *pszText = pszTmp;

    // Return the length NOT including the '\0'.
    *pcchLen = static_cast<DWORD>(cch);  

     return S_OK;
}
```



## Related topics

<dl> <dt>

[Media Session Playback Example](media-session-playback-example.md)
</dt> <dt>

[Audio/Video Playback](audio-video-playback.md)
</dt> </dl>

 

 




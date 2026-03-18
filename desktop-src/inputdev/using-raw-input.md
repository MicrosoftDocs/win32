---
title: Using Raw Input
description: This section includes sample code for tasks relating to raw input.
ms.assetid: e078e13c-06b8-4440-9d37-78c344b587e9
keywords:
- user input,raw input
- capturing user input,raw input
- raw input
- buffered read of raw input
- standard read of raw input
- registering raw input
- reading raw input
- joystick raw input
- game pad raw input
ms.topic: concept-article
ms.date: 07/14/2025
---

# Using Raw Input

This section includes sample code for the following purposes:

-   [Registering for Raw Input](#registering-for-raw-input)
    -   [Example 1](#example-1)
    -   [Example 2](#example-2)
-   [Performing a Standard Read of Raw Input](#performing-a-standard-read-of-raw-input)
-   [Performing a Buffered Read of Raw Input](#performing-a-buffered-read-of-raw-input)

## Registering for Raw Input

### Example 1

In this sample, an application specifies the raw input from game controllers (both game pads and joysticks) and all devices off the telephony usage page except answering machines.

```cpp
RAWINPUTDEVICE Rid[4];
        
Rid[0].usUsagePage = 0x01;          // HID_USAGE_PAGE_GENERIC
Rid[0].usUsage = 0x05;              // HID_USAGE_GENERIC_GAMEPAD
Rid[0].dwFlags = 0;                 // adds game pad
Rid[0].hwndTarget = 0;

Rid[1].usUsagePage = 0x01;          // HID_USAGE_PAGE_GENERIC
Rid[1].usUsage = 0x04;              // HID_USAGE_GENERIC_JOYSTICK
Rid[1].dwFlags = 0;                 // adds joystick
Rid[1].hwndTarget = 0;

Rid[2].usUsagePage = 0x0B;          // HID_USAGE_PAGE_TELEPHONY
Rid[2].usUsage = 0x00; 
Rid[2].dwFlags = RIDEV_PAGEONLY;    // adds all devices from telephony page
Rid[2].hwndTarget = 0;

Rid[3].usUsagePage = 0x0B;          // HID_USAGE_PAGE_TELEPHONY
Rid[3].usUsage = 0x02;              // HID_USAGE_TELEPHONY_ANSWERING_MACHINE
Rid[3].dwFlags = RIDEV_EXCLUDE;     // excludes answering machines
Rid[3].hwndTarget = 0;

if (RegisterRawInputDevices(Rid, 4, sizeof(Rid[0])) == FALSE)
{
    //registration failed. Call GetLastError for the cause of the error.
}
```

### Example 2

In this sample, an application wants raw input from the keyboard and mouse but wants to ignore  [legacy keyboard](keyboard-input-notifications.md) and [mouse window messages](mouse-input-notifications.md) (which would come from the same keyboard and mouse).

```cpp
RAWINPUTDEVICE Rid[2];
        
Rid[0].usUsagePage = 0x01;          // HID_USAGE_PAGE_GENERIC
Rid[0].usUsage = 0x02;              // HID_USAGE_GENERIC_MOUSE
Rid[0].dwFlags = RIDEV_NOLEGACY;    // adds mouse and also ignores legacy mouse messages
Rid[0].hwndTarget = 0;

Rid[1].usUsagePage = 0x01;          // HID_USAGE_PAGE_GENERIC
Rid[1].usUsage = 0x06;              // HID_USAGE_GENERIC_KEYBOARD
Rid[1].dwFlags = RIDEV_NOLEGACY;    // adds keyboard and also ignores legacy keyboard messages
Rid[1].hwndTarget = 0;

if (RegisterRawInputDevices(Rid, 2, sizeof(Rid[0])) == FALSE)
{
    //registration failed. Call GetLastError for the cause of the error
}
```

## Performing a Standard Read of Raw Input

This sample shows how an application does an unbuffered (or standard) read of raw input from either a keyboard or mouse Human Interface Device (HID) and then prints out various information from the device.

```cpp
case WM_INPUT: 
{
    UINT dwSize;

    GetRawInputData((HRAWINPUT)lParam, RID_INPUT, NULL, &dwSize, sizeof(RAWINPUTHEADER));
    LPBYTE lpb = new BYTE[dwSize];

    if (GetRawInputData((HRAWINPUT)lParam, RID_INPUT, lpb, &dwSize, sizeof(RAWINPUTHEADER)) != dwSize)
         OutputDebugString (TEXT("GetRawInputData does not return correct size !\n")); 

    RAWINPUT* raw = (RAWINPUT*)lpb;

    if (raw->header.dwType == RIM_TYPEKEYBOARD) 
    {
        hResult = StringCchPrintf(szTempOutput, STRSAFE_MAX_CCH,
            TEXT(" Kbd: make=%04x Flags:%04x Reserved:%04x ExtraInformation:%08x, msg=%04x VK=%04x \n"), 
            raw->data.keyboard.MakeCode, 
            raw->data.keyboard.Flags, 
            raw->data.keyboard.Reserved, 
            raw->data.keyboard.ExtraInformation, 
            raw->data.keyboard.Message, 
            raw->data.keyboard.VKey);
        if (FAILED(hResult))
        {
        // TODO: write error handler
        }
        OutputDebugString(szTempOutput);
    }
    else if (raw->header.dwType == RIM_TYPEMOUSE) 
    {
        hResult = StringCchPrintf(szTempOutput, STRSAFE_MAX_CCH,
            TEXT("Mouse: usFlags=%04x ulButtons=%04x usButtonFlags=%04x usButtonData=%04x ulRawButtons=%04x lLastX=%04x lLastY=%04x ulExtraInformation=%04x\r\n"), 
            raw->data.mouse.usFlags, 
            raw->data.mouse.ulButtons, 
            raw->data.mouse.usButtonFlags, 
            raw->data.mouse.usButtonData, 
            raw->data.mouse.ulRawButtons, 
            raw->data.mouse.lLastX, 
            raw->data.mouse.lLastY, 
            raw->data.mouse.ulExtraInformation);

        if (FAILED(hResult))
        {
        // TODO: write error handler
        }
        OutputDebugString(szTempOutput);
    } 

    delete[] lpb; 
    return 0;
} 
```

## Performing a Standard Read of Raw Input

This sample shows the minimal pattern for reading raw input from a [**WM_INPUT**](wm-input.md) message handler. Each [**WM_INPUT**](wm-input.md) message carries an **HRAWINPUT** handle in **lParam** referencing the current input event — it must be read via [**GetRawInputData**](/windows/win32/api/winuser/nf-winuser-getrawinputdata) before calling [**DefWindowProc**](/windows/win32/api/winuser/nf-winuser-defwindowprocw).

```cpp
/* Initialized once at startup */
UINT  g_bufferSize = 64 * sizeof(RAWINPUT);
void* g_pBuffer    = NULL;

void ProcessInput(const RAWINPUT* input)
{
    if (input->header.dwType == RIM_TYPEKEYBOARD)
        printf("key vk=0x%02x flags=0x%x\n", input->data.keyboard.VKey, input->data.keyboard.Flags);
    else if (input->header.dwType == RIM_TYPEMOUSE)
        printf("mouse dx=%d dy=%d\n", input->data.mouse.lLastX, input->data.mouse.lLastY);
}

/* ... */

g_pBuffer = malloc(g_bufferSize);

/* ... */

case WM_INPUT:
{
    UINT bufferSize = g_bufferSize;
    UINT result = GetRawInputData((HRAWINPUT)lParam, RID_INPUT, g_pBuffer, &bufferSize, sizeof(RAWINPUTHEADER));

    if (result != (UINT)-1)
        ProcessInput((RAWINPUT*)g_pBuffer);
    else
        Log(_T("GetRawInputData failed: %d"), GetLastError());

    return DefWindowProc(hWnd, uMsg, wParam, lParam);
}
```

## Performing a Buffered Read of Raw Input

This sample shows how to read raw input in fixed-rate batches using a periodic timer. [**WM_INPUT**](wm-input.md) messages are intentionally never dispatched through [**DispatchMessage**](/windows/win32/api/winuser/nf-winuser-dispatchmessage) — because [**GetMessage**](/windows/win32/api/winuser/nf-winuser-getmessage) removes messages from the raw input queue before returning, only [**PeekMessage**](/windows/win32/api/winuser/nf-winuser-peekmessagew) with explicit message range filters is used, skipping [**WM_INPUT**](wm-input.md) entirely. This keeps all raw input events in the queue where [**GetRawInputBuffer**](/windows/win32/api/winuser/nf-winuser-getrawinputbuffer) can drain them all at once on each timer tick. This approach is well-suited for game loops and other applications that process input at a fixed rate rather than reacting to each event individually.

```cpp
HWND hWnd = CreateWindowExW(0, L"RawInputSink", NULL, 0, 0, 0, 0, 0, HWND_MESSAGE, NULL, NULL, NULL);
RAWINPUTDEVICE rid = { 0x01, 0x02, RIDEV_INPUTSINK, hWnd }; /* mouse */
RegisterRawInputDevices(&rid, 1, sizeof(rid));

/* Drain raw input queue every 16ms (~60Hz) */
SetTimer(hWnd, 1, 16, NULL);

MSG msg;
for (;;)
{
    /* Dispatch all messages except WM_INPUT */
    while (PeekMessageW(&msg, NULL, 0, WM_INPUT - 1, PM_REMOVE) ||
           PeekMessageW(&msg, NULL, WM_INPUT + 1, 0xFFFF, PM_REMOVE))
    {
        if (msg.message == WM_QUIT)
            goto Exit;

        if (msg.message == WM_TIMER)
        {
            /* Timer tick — drain all WM_INPUT accumulated in the queue */
            for (;;)
            {
                UINT bufferSize = g_bufferSize;
                UINT count = GetRawInputBuffer((RAWINPUT*)g_pBuffer, &bufferSize, sizeof(RAWINPUTHEADER));

                if (count == 0)
                    break;

                if (count == (UINT)-1)
                {
                    /* Buffer too small — grow and retry */
                    g_bufferSize = max(bufferSize, g_bufferSize * 2);
                    g_pBuffer = realloc(g_pBuffer, g_bufferSize);
                    if (g_pBuffer == NULL)
                        goto Exit;
                    continue;
                }

                {
                    RAWINPUT* input = (RAWINPUT*)g_pBuffer;
                    UINT i;
                    for (i = 0; i < count; ++i, input = NEXTRAWINPUTBLOCK(input))
                        ProcessInput(input);
                    /* Do not break — there may be more events in the queue. */
                }
            }
        }

        DispatchMessageW(&msg);
    }

    WaitMessage();
}

Exit:;
```

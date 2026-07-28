---
title: Using Cursors
description: This section provides code samples that show how to perform tasks related to cursors.
ms.assetid: eab7b781-783e-4fc5-868d-6ff773c40a21
keywords:
- resources,cursors
- cursors,custom
- custom cursors
- hourglass cursor
- cursors,creating
- cursors,hourglass
- creating cursors
- destroying cursors
- displaying cursors
- confining cursors
- cursors,destroying
- cursors,displaying
- cursors,confining
ms.topic: concept-article
ms.date: 05/31/2018
---

# Using Cursors

This section discusses the following topics.

-   [Creating a Cursor](#creating-a-cursor)
-   [Using Cursor Functions to Create a Mousetrap](#using-cursor-functions-to-create-a-mousetrap)
-   [Creating an Alpha Blended Cursor](#creating-an-alpha-blended-cursor)
-   [Getting Cursor Size from Handle](#getting-cursor-size-from-handle)
-   [Displaying a Cursor](#displaying-a-cursor)
-   [Confining a Cursor](#confining-a-cursor)
-   [Using the Keyboard to Move the Cursor](#using-the-keyboard-to-move-the-cursor)

## Creating a Cursor

The following example creates two cursor handles: one for the standard hourglass cursor and one for a custom cursor included as a resource in the application's resource-definition file.

```c
HCURSOR hCurs1 = LoadCursor(NULL, IDC_WAIT);
HCURSOR hCurs2 = LoadCursor(hInstance, MAKEINTRESOURCE(IDC_MYICON));
```

Applications should implement custom cursors as resources and use [**LoadCursor**](/windows/win32/api/winuser/nf-winuser-loadcursorw), [**LoadCursorFromFile**](/windows/win32/api/winuser/nf-winuser-loadcursorfromfilew), or [**LoadImage**](/windows/win32/api/winuser/nf-winuser-loadimagew) rather than create the cursor at run time. Using cursor resources avoids device dependence, simplifies localization, and enables applications to share cursor designs.

The following example uses the [**CreateCursor**](/windows/win32/api/winuser/nf-winuser-createcursor) function to create a custom monochrome cursor at run time. The example is included here to illustrate how the system interprets cursor masks.

Each pixel in the cursor map is represented by a single character:

| Symbol | AND bit | XOR bit | Display         |
|--------|---------|---------|-----------------|
| ` `    | 1       | 0       | Transparent     |
| `X`    | 1       | 1       | Invert screen   |
| `o`    | 0       | 1       | White           |
| `+`    | 0       | 0       | Black           |

```c
#define CURSOR_SIZE 32

// Symbol encoding: ' '=transparent  'o'=white  '+'=black
static const char *const yin_cursor[CURSOR_SIZE] = {
    "              ++++              ",
    "          ++++oooo+             ",
    "        ++oooooo++              ",
    "       +ooooooo+                ",
    "     +oooooooo+                 ",
    "    +oooooooo+                  ",
    "    +oooooooo+                  ",
    "   +oooooooo+                   ",
    "  +ooooooooo+                   ",
    "  +oooooooo+                    ",
    " +ooooooooo+                    ",
    " +ooooooooo+                    ",
    " +oooooooooo+                   ",
    "+ooooooooooo+                   ",
    "+oooooooooooo+                  ",
    "+ooooooooooooo++                ",
    "+ooooooooooooooo+               ",
    "+oooooooooooooooo++             ",
    "+oooooooooooooooooo+            ",
    " +ooooooooooooooooo+            ",
    " +oooooooo+++ooooooo+           ",
    " +ooooooo+++++oooooo+           ",
    "  +oooooo+++++oooooo+           ",
    "  +oooooo+++++ooooo+            ",
    "   +oooooo+++oooooo+            ",
    "    +ooooooooooooo+             ",
    "    +ooooooooooooo+             ",
    "     ++oooooooooo+              ",
    "       +oooooooo+               ",
    "        ++oooo++                ",
    "          ++++                  ",
    "                                ",
};

// Pack an XPM-style cursor map into separate 1bpp AND and XOR bit planes.
// Output buffers must be sized: ((w + 15) / 16) * 2 * h bytes.
static void PackCursorMasks(const char *const rows[], int w, int h,
                             BYTE *pbAnd, BYTE *pbXor)
{
    int stride = ((w + 15) / 16) * 2;  // WORD-aligned row stride, per CreateCursor contract
    ZeroMemory(pbAnd, stride * h);
    ZeroMemory(pbXor, stride * h);
    for (int y = 0; y < h; y++) {
        for (int x = 0; x < w; x++) {
            BYTE bit = (BYTE)(0x80 >> (x % 8));
            int  idx = y * stride + x / 8;
            char sym = rows[y][x];
            if (sym == ' ' || sym == 'X') pbAnd[idx] |= bit;
            if (sym == 'o' || sym == 'X') pbXor[idx] |= bit;
        }
    }
}

// Row stride for a 32-pixel-wide 1bpp mask: ((32 + 15) / 16) * 2 = 4 bytes.
BYTE abAnd[CURSOR_SIZE * 4];
BYTE abXor[CURSOR_SIZE * 4];
PackCursorMasks(yin_cursor, CURSOR_SIZE, CURSOR_SIZE, abAnd, abXor);

// hInstance is the application's HINSTANCE from WinMain.
// Call DestroyCursor when the cursor is no longer needed.
HCURSOR hCurs3 = CreateCursor(
    hInstance,  // application instance
    19,         // hot spot x
    2,          // hot spot y
    CURSOR_SIZE,
    CURSOR_SIZE,
    abAnd,
    abXor);
```

For more information, see [Bitmaps](/windows/win32/gdi/bitmaps).

## Using Cursor Functions to Create a Mousetrap

The following example uses the [**SetCursorPos**](/windows/win32/api/winuser/nf-winuser-setcursorpos), [**GetCursorPos**](/windows/win32/api/winuser/nf-winuser-getcursorpos), [**CreateCursor**](/windows/win32/api/winuser/nf-winuser-createcursor), [**CreateIcon**](/windows/win32/api/winuser/nf-winuser-createicon), [**SetCursor**](/windows/win32/api/winuser/nf-winuser-setcursor), and [**DrawIconEx**](/windows/win32/api/winuser/nf-winuser-drawiconex) functions to create a simple mousetrap. A yang-shaped icon is drawn in the center of the window. If the cursor has not moved for 3 seconds, it snaps to the yang icon and changes to the yin shape. Moving the mouse resets the trap.

```c
// PackCursorMasks, yin_cursor, and CURSOR_SIZE are defined in the preceding example.

#define ICON_SIZE     32
#define YIN_HOT_X     19
#define YIN_HOT_Y      2
#define IDT_CURSOR     1
#define TRAP_DELAY  3000    // ms of inactivity before the cursor snaps to the icon

// Symbol encoding: ' '=transparent  'o'=white  '+'=black
static const char *const yang_icon[ICON_SIZE] = {
    "                                ",
    "                  ++++          ",
    "                ++++++++        ",
    "               ++++++++++       ",
    "              +++++++++++++     ",
    "             +++++++++++++++    ",
    "             +++++++++++++++    ",
    "            ++++++ooo++++++++   ",
    "            +++++ooooo++++++++  ",
    "           ++++++ooooo++++++++  ",
    "           ++++++ooooo+++++++++ ",
    "           +++++++ooo++++++++++ ",
    "            +++++++++++++++++++ ",
    "            ++++++++++++++++++++",
    "             +++++++++++++++++++",
    "              ++++++++++++++++++",
    "                ++++++++++++++++",
    "                 +++++++++++++++",
    "                   +++++++++++++",
    "                   ++++++++++++ ",
    "                    +++++++++++ ",
    "                    +++++++++++ ",
    "                    ++++++++++  ",
    "                   +++++++++++  ",
    "                   ++++++++++   ",
    "                  ++++++++++    ",
    "                  ++++++++++    ",
    "                 ++++++++++     ",
    "                +++++++++       ",
    "              ++++++++++        ",
    "             +++++++++          ",
    "              ++++              ",
};

static HICON   hYang;
static HCURSOR hYin;
static POINT   ptLast;
static BOOL    bTrapped;

LRESULT CALLBACK MainWndProc(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    switch (uMsg)
    {
        case WM_CREATE:
        {
            HINSTANCE hInstance = ((LPCREATESTRUCT)lParam)->hInstance;

            BYTE abAndIcon[ICON_SIZE * 4];
            BYTE abXorIcon[ICON_SIZE * 4];
            PackCursorMasks(yang_icon, ICON_SIZE, ICON_SIZE, abAndIcon, abXorIcon);
            hYang = CreateIcon(hInstance, ICON_SIZE, ICON_SIZE, 1, 1,
                               abAndIcon, abXorIcon);

            BYTE abAndCursor[CURSOR_SIZE * 4];
            BYTE abXorCursor[CURSOR_SIZE * 4];
            PackCursorMasks(yin_cursor, CURSOR_SIZE, CURSOR_SIZE, abAndCursor, abXorCursor);
            hYin = CreateCursor(hInstance, YIN_HOT_X, YIN_HOT_Y, CURSOR_SIZE, CURSOR_SIZE,
                                abAndCursor, abXorCursor);

            GetCursorPos(&ptLast);
            SetTimer(hWnd, IDT_CURSOR, TRAP_DELAY, (TIMERPROC)NULL);
            return 0;
        }

        case WM_PAINT:
        {
            PAINTSTRUCT ps;
            HDC hDC = BeginPaint(hWnd, &ps);
            RECT rc;
            GetClientRect(hWnd, &rc);
            DrawIconEx(hDC,
                       (rc.right  - ICON_SIZE) / 2,
                       (rc.bottom - ICON_SIZE) / 2,
                       hYang, ICON_SIZE, ICON_SIZE, 0, NULL, DI_NORMAL);
            EndPaint(hWnd, &ps);
            return 0;
        }

        case WM_MOUSEMOVE:
            GetCursorPos(&ptLast);
            bTrapped = FALSE;
            SetTimer(hWnd, IDT_CURSOR, TRAP_DELAY, (TIMERPROC)NULL);
            break;

        case WM_TIMER:
        {
            POINT ptNow;
            GetCursorPos(&ptNow);
            if (ptNow.x == ptLast.x && ptNow.y == ptLast.y)
            {
                RECT rc;
                GetClientRect(hWnd, &rc);
                POINT ptTarget = {
                    (rc.right  - ICON_SIZE) / 2 + YIN_HOT_X,
                    (rc.bottom - ICON_SIZE) / 2 + YIN_HOT_Y
                };
                ClientToScreen(hWnd, &ptTarget);
                SetCursorPos(ptTarget.x, ptTarget.y);
                SetCursor(hYin);
                bTrapped = TRUE;
            }
            KillTimer(hWnd, IDT_CURSOR);
            return 0;
        }

        case WM_SETCURSOR:
            if (bTrapped)
            {
                SetCursor(hYin);
                return TRUE;
            }
            break;

        case WM_DESTROY:
            KillTimer(hWnd, IDT_CURSOR);
            DestroyCursor(hYin);
            DestroyIcon(hYang);
            PostQuitMessage(0);
            return 0;
    }

    return DefWindowProc(hWnd, uMsg, wParam, lParam);
}
```

## Creating an Alpha Blended Cursor

Follow these steps to create an alpha blended cursor or icon at run time:
- Fill a [**BITMAPINFOHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader) for a top-down DIB (`biBitCount=32`, `biCompression=BI_RGB`, `biHeight` negative) and call [**CreateDIBSection**](/windows/win32/api/wingdi/nf-wingdi-createdibsection) to get the color bitmap. Reuse the same header with `biBitCount=1` to create the 1bpp AND mask.
- Draw the cursor image into the color DIB section and set the alpha byte of each pixel.
- Fill the AND mask: set each bit to 0 (opaque) where `alpha > 0`, and to 1 (transparent) where `alpha == 0`.
- Fill an [**ICONINFO**](/windows/win32/api/winuser/ns-winuser-iconinfo) structure with the DIB section as `hbmColor` and the AND mask as `hbmMask`.
- Call [**CreateIconIndirect**](/windows/win32/api/winuser/nf-winuser-createiconindirect) to create the cursor or icon.

The following code demonstrates how to create an alpha blended cursor. `DrawRGBCircles` writes three overlapping R/G/B semi-transparent circles directly into a pixel buffer: it composites the circles analytically using the AC\_SRC\_OVER formula and un-premultiplies the result, so the output is ready-to-use straight alpha. The cursor size is read from [**GetSystemMetrics**](/windows/win32/api/winuser/nf-winuser-getsystemmetrics) to match the system cursor size setting. Change `fIcon` to `TRUE` to create an icon instead.

```c
#define WIDTHBYTES(bits) ((DWORD)(((bits) + 31) & ~31) / 8)

// Fill pixels (top-down, cx-cy) with three overlapping R/G/B circles, each alpha=128.
// Composites with AC_SRC_OVER and writes straight alpha into rgbReserved.
static void DrawRGBCircles(RGBQUAD *pixels, int cx, int cy)
{
    // r = cx/3: each center is r px from its nearest edge, so the circle touches exactly.
    const int r = cx / 3;
    struct { int x, y; RGBQUAD color; } circles[3] = {
        //                  B    G    R    A
        { cx / 2,  r,      {  0,   0, 255, 128 } },  // red,   top-center
        { r,       cy - r, {  0, 255,   0, 128 } },  // green, bottom-left
        { cx - r,  cy - r, {255,   0,   0, 128 } },  // blue,  bottom-right
    };

    for (int y = 0; y < cy; y++) {
        for (int x = 0; x < cx; x++) {
            DWORD R = 0, G = 0, B = 0, A = 0;
            for (int i = 0; i < 3; i++) {
                int dx = x - circles[i].x, dy = y - circles[i].y;
                if (dx*dx + dy*dy > r*r) continue;
                DWORD a = circles[i].color.rgbReserved, inv = 255 - a;
                // AC_SRC_OVER (premultiplied): dst = src + dst * (1 - src_a/255)
                R = circles[i].color.rgbRed   * a / 255 + R * inv / 255;
                G = circles[i].color.rgbGreen * a / 255 + G * inv / 255;
                B = circles[i].color.rgbBlue  * a / 255 + B * inv / 255;
                A = a                                    + A * inv / 255;
            }
            RGBQUAD *p = &pixels[y * cx + x];
            p->rgbReserved = (BYTE)A;
            if (A > 0) {
                p->rgbRed   = (BYTE)(R * 255 / A);  // un-premultiply to straight alpha
                p->rgbGreen = (BYTE)(G * 255 / A);
                p->rgbBlue  = (BYTE)(B * 255 / A);
            }
        }
    }
}

HCURSOR CreateAlphaCursor(void)
{
    int cx = GetSystemMetrics(SM_CXCURSOR);
    int cy = GetSystemMetrics(SM_CYCURSOR);

    // Extra RGBQUAD at the end for the 1bpp colour table (index 1 = white).
    BYTE bmiBuffer[sizeof(BITMAPINFO) + sizeof(RGBQUAD)] = {0};
    BITMAPINFO *pBmi = (BITMAPINFO *)bmiBuffer;
    pBmi->bmiHeader.biSize        = sizeof(pBmi->bmiHeader);
    pBmi->bmiHeader.biWidth       = cx;
    pBmi->bmiHeader.biHeight      = -cy;   // negative = top-down
    pBmi->bmiHeader.biPlanes      = 1;
    pBmi->bmiHeader.biCompression = BI_RGB;

    // Create a top-down 32bpp DIB section for the color (XOR) image.
    pBmi->bmiHeader.biBitCount = 32;
    RGBQUAD *lpBits;
    HBITMAP hBitmap = CreateDIBSection(NULL, pBmi, DIB_RGB_COLORS, (void **)&lpBits, NULL, 0);

    DrawRGBCircles(lpBits, cx, cy);

    // Reuse the same header for the 1bpp AND mask; switch biBitCount and set the colour table.
    pBmi->bmiHeader.biBitCount = 1;
    pBmi->bmiColors[0].rgbRed = pBmi->bmiColors[0].rgbGreen = pBmi->bmiColors[0].rgbBlue = 0;
    pBmi->bmiColors[1].rgbRed = pBmi->bmiColors[1].rgbGreen = pBmi->bmiColors[1].rgbBlue = 255;
    BYTE *andBits;
    HBITMAP hMaskBitmap = CreateDIBSection(NULL, pBmi, DIB_RGB_COLORS, (void **)&andBits, NULL, 0);

    // Set AND mask: bit=1 (transparent) wherever no circle was drawn.
    int maskStride = WIDTHBYTES(cx * 1);
    for (int y = 0; y < cy; y++) {
        for (int x = 0; x < cx; x++) {
            if (lpBits[y * cx + x].rgbReserved == 0)
                andBits[y * maskStride + x / 8] |= (BYTE)(0x80 >> (x % 8));
        }
    }

    ICONINFO ii = {0};
    ii.fIcon     = FALSE;
    ii.xHotspot  = cx / 2;
    ii.yHotspot  = cy / 2;
    ii.hbmMask   = hMaskBitmap;
    ii.hbmColor  = hBitmap;

    HCURSOR hCursor = (HCURSOR)CreateIconIndirect(&ii);

    DeleteObject(hBitmap);
    DeleteObject(hMaskBitmap);

    return hCursor;
}

```

Before closing, you must use the [**DestroyCursor**](/windows/win32/api/winuser/nf-winuser-destroycursor) function to destroy any cursors you created with [**CreateCursor**](/windows/win32/api/winuser/nf-winuser-createcursor) or [**CreateIconIndirect**](/windows/win32/api/winuser/nf-winuser-createiconindirect). It is not necessary to destroy cursors created by other functions.

## Getting Cursor Size from Handle

The following example retrieves the dimensions of a cursor or icon from its handle:

```c
BOOL GetCursorDimensions(_In_ HCURSOR hcur, _Out_ SIZE *psiz)
{
    ICONINFO ii;
    BOOL fResult = GetIconInfo(hcur, &ii);
    if (fResult) {
        BITMAP bm;
        fResult = GetObject(ii.hbmMask, sizeof(bm), &bm) == sizeof(bm);
        if (fResult) {
            psiz->cx = bm.bmWidth;
            psiz->cy = ii.hbmColor ? bm.bmHeight : bm.bmHeight / 2;
        }
        DeleteObject(ii.hbmMask);
        if (ii.hbmColor) DeleteObject(ii.hbmColor);
    }
    return fResult;
}
```

## Displaying a Cursor

The system automatically displays the class cursor (the cursor associated with the window to which the cursor is pointing). You can assign a class cursor while registering a window class. The following example illustrates this by assigning a cursor handle to the **hCursor** member of the [**WNDCLASS**](/windows/win32/api/winuser/ns-winuser-wndclassa) structure identified by the *wc* parameter.

```c
WNDCLASS wc = {0};
wc.lpfnWndProc   = MainWndProc;
wc.hInstance     = hInstance;
wc.hIcon         = LoadIcon(NULL, IDI_APPLICATION);
wc.hCursor       = LoadCursor(hInstance, MAKEINTRESOURCE(IDC_MYICON));
wc.hbrBackground = GetStockObject(WHITE_BRUSH);
wc.lpszMenuName  = TEXT("GenericMenu");
wc.lpszClassName = TEXT("GenericWClass");

return RegisterClass(&wc);
```

When the window class is registered, the cursor identified by `IDC_MYICON` in the application's resource-definition file is the default cursor for all windows based on the class.

Your application can change the design of the cursor by using the [**SetCursor**](/windows/win32/api/winuser/nf-winuser-setcursor) function and specifying a different cursor handle. However, when the cursor moves, the system redraws the class cursor at the new location. To prevent the class cursor from being redrawn, you must process the [**WM\_SETCURSOR**](wm-setcursor.md) message. Each time the cursor moves and mouse input is not captured, the system sends this message to the window in which the cursor is moving.

You can specify different cursors for different conditions while processing [**WM\_SETCURSOR**](wm-setcursor.md). Check `LOWORD(lParam)` to distinguish the client area from non-client areas such as resize handles; pass non-client hits to [**DefWindowProc**](/windows/win32/api/winuser/nf-winuser-defwindowproc) so the system sets the appropriate system cursor there.

```c
case WM_SETCURSOR:
    if (LOWORD(lParam) == HTCLIENT)
    {
        SetCursor(hCurs3);
        return TRUE;
    }
    return DefWindowProc(hWnd, uMsg, wParam, lParam);
```

Returning `TRUE` prevents **DefWindowProc** from resetting the cursor to the class cursor. Passing non-client hits to **DefWindowProc** preserves system resize and move cursors.

You can replace a class cursor by using the [**SetClassLongPtr**](/windows/win32/api/winuser/nf-winuser-setclasslongptrw) function. This function changes the default window settings for all windows of a specified class. The following example replaces the existing class cursor with the `hCurs2` cursor.


```c
SetClassLongPtr(hWnd, GCLP_HCURSOR, (LONG_PTR)hCurs2);
```

For more information, see [Window Classes](/windows/win32/winmsg/window-classes) and [Mouse Input](/windows/win32/inputdev/mouse-input).

## Confining a Cursor

The following example confines the cursor to the application's window and then restores the cursor to its previous window. The example uses the [**GetClipCursor**](/windows/win32/api/winuser/nf-winuser-getclipcursor) function to record the area in which the cursor can move and the [**ClipCursor**](/windows/win32/api/winuser/nf-winuser-clipcursor) function to confine and restore the cursor.

```c
RECT rcOldClip;
GetClipCursor(&rcOldClip);

RECT rcClip;
GetWindowRect(hWnd, &rcClip);
ClipCursor(&rcClip);

// ... process input from the confined cursor ...

ClipCursor(&rcOldClip);
```

Because there is only one cursor at a time available in the system, an application that confines the cursor must restore the cursor before relinquishing control to another window.

## Using the Keyboard to Move the Cursor

Because the system does not require a mouse, an application should be able to simulate mouse actions with the keyboard. The following example shows how to achieve this by using the [**GetCursorPos**](/windows/win32/api/winuser/nf-winuser-getcursorpos) and [**SetCursorPos**](/windows/win32/api/winuser/nf-winuser-setcursorpos) functions and by processing input from the arrow keys.

```c
static int nRepeat = 1;

switch (uMsg)
{
    case WM_KEYDOWN:
    {
        int dx = 0, dy = 0;
        switch (wParam)
        {
            case VK_LEFT:  dx = -nRepeat; break;
            case VK_RIGHT: dx = +nRepeat; break;
            case VK_UP:    dy = -nRepeat; break;
            case VK_DOWN:  dy = +nRepeat; break;
            default: return DefWindowProc(hWnd, uMsg, wParam, lParam);
        }

        POINT pt;
        GetCursorPos(&pt);
        ScreenToClient(hWnd, &pt);
        pt.x += dx;
        pt.y += dy;

        RECT rc;
        GetClientRect(hWnd, &rc);
        if (pt.x < rc.left)         pt.x = rc.left;
        else if (pt.x >= rc.right)  pt.x = rc.right - 1;
        if (pt.y < rc.top)          pt.y = rc.top;
        else if (pt.y >= rc.bottom) pt.y = rc.bottom - 1;

        ClientToScreen(hWnd, &pt);
        SetCursorPos(pt.x, pt.y);
        if (nRepeat < 32) nRepeat++;
        return 0;
    }
    case WM_KEYUP:
        nRepeat = 1;
        return 0;
}
```

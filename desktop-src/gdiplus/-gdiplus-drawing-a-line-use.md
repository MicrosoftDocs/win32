---
Description: This topic demonstrates how to draw a line using GDI Plus.
ms.assetid: 2e7444f8-94a6-40d6-b243-0764e245eec4
title: Drawing a Line
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Drawing a Line

This topic demonstrates how to draw a line using GDI Plus.

To draw a line in Windows GDI+ you need a [**Graphics**](/windows/desktop/api/gdiplusgraphics/nl-gdiplusgraphics-graphics) object, a [**Pen**](/windows/desktop/api/gdipluspen/nl-gdipluspen-pen) object, and a [**Color**](/windows/desktop/api/gdipluscolor/nl-gdipluscolor-color) object. The **Graphics** object provides the [DrawLine Methods](/windows/desktop/api/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawline(in const pen_in const point &_in const point &)) method, and the **Pen** object holds attributes of the line, such as color and width. The address of the **Pen** object is passed as an argument to the DrawLine Methods method.

The following program, which draws a line from (0, 0) to (200, 100), consists of three functions: **WinMain**, **WndProc**, and **OnPaint**. The **WinMain** and **WndProc** functions provide the fundamental code common to most Windows applications. There is no GDI+ code in the **WndProc** function. The **WinMain** function has a small amount of GDI+ code, namely the required calls to [**GdiplusStartup**](/windows/desktop/api/Gdiplusinit/nf-gdiplusinit-gdiplusstartup) and [**GdiplusShutdown**](/windows/desktop/api/Gdiplusinit/nf-gdiplusinit-gdiplusshutdown). The GDI+ code that actually creates a [**Graphics**](/windows/desktop/api/gdiplusgraphics/nl-gdiplusgraphics-graphics) object and draws a line is in the **OnPaint** function.

The **OnPaint** function receives a handle to a device context and passes that handle to a [**Graphics**](/windows/desktop/api/gdiplusgraphics/nl-gdiplusgraphics-graphics) constructor. The argument passed to the [**Pen**](/windows/desktop/api/gdipluspen/nl-gdipluspen-pen) constructor is a reference to a [**Color**](/windows/desktop/api/gdipluscolor/nl-gdipluscolor-color) object. The four numbers passed to the color constructor represent the alpha, red, green, and blue components of the color. The alpha component determines the transparency of the color; 0 is fully transparent and 255 is fully opaque. The four numbers passed to the [DrawLine Methods](/windows/desktop/api/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawline(in const pen_in const point &_in const point &)) method represent the starting point (0, 0) and the ending point (200, 100) of the line.


```C++
#include <stdafx.h>
#include <windows.h>
#include <objidl.h>
#include <gdiplus.h>
using namespace Gdiplus;
#pragma comment (lib,"Gdiplus.lib")

VOID OnPaint(HDC hdc)
{
   Graphics graphics(hdc);
   Pen      pen(Color(255, 0, 0, 255));
   graphics.DrawLine(&amp;pen, 0, 0, 200, 100);
}

LRESULT CALLBACK WndProc(HWND, UINT, WPARAM, LPARAM);

INT WINAPI WinMain(HINSTANCE hInstance, HINSTANCE, PSTR, INT iCmdShow)
{
   HWND                hWnd;
   MSG                 msg;
   WNDCLASS            wndClass;
   GdiplusStartupInput gdiplusStartupInput;
   ULONG_PTR           gdiplusToken;
   
   // Initialize GDI+.
   GdiplusStartup(&amp;gdiplusToken, &amp;gdiplusStartupInput, NULL);
   
   wndClass.style          = CS_HREDRAW | CS_VREDRAW;
   wndClass.lpfnWndProc    = WndProc;
   wndClass.cbClsExtra     = 0;
   wndClass.cbWndExtra     = 0;
   wndClass.hInstance      = hInstance;
   wndClass.hIcon          = LoadIcon(NULL, IDI_APPLICATION);
   wndClass.hCursor        = LoadCursor(NULL, IDC_ARROW);
   wndClass.hbrBackground  = (HBRUSH)GetStockObject(WHITE_BRUSH);
   wndClass.lpszMenuName   = NULL;
   wndClass.lpszClassName  = TEXT("GettingStarted");
   
   RegisterClass(&amp;wndClass);
   
   hWnd = CreateWindow(
      TEXT("GettingStarted"),   // window class name
      TEXT("Getting Started"),  // window caption
      WS_OVERLAPPEDWINDOW,      // window style
      CW_USEDEFAULT,            // initial x position
      CW_USEDEFAULT,            // initial y position
      CW_USEDEFAULT,            // initial x size
      CW_USEDEFAULT,            // initial y size
      NULL,                     // parent window handle
      NULL,                     // window menu handle
      hInstance,                // program instance handle
      NULL);                    // creation parameters
      
   ShowWindow(hWnd, iCmdShow);
   UpdateWindow(hWnd);
   
   while(GetMessage(&amp;msg, NULL, 0, 0))
   {
      TranslateMessage(&amp;msg);
      DispatchMessage(&amp;msg);
   }
   
   GdiplusShutdown(gdiplusToken);
   return msg.wParam;
}  // WinMain

LRESULT CALLBACK WndProc(HWND hWnd, UINT message, 
   WPARAM wParam, LPARAM lParam)
{
   HDC          hdc;
   PAINTSTRUCT  ps;
   
   switch(message)
   {
   case WM_PAINT:
      hdc = BeginPaint(hWnd, &amp;ps);
      OnPaint(hdc);
      EndPaint(hWnd, &amp;ps);
      return 0;
   case WM_DESTROY:
      PostQuitMessage(0);
      return 0;
   default:
      return DefWindowProc(hWnd, message, wParam, lParam);
   }
} // WndProc
```



Note the call to [**GdiplusStartup**](/windows/desktop/api/Gdiplusinit/nf-gdiplusinit-gdiplusstartup) in the **WinMain** function. The first parameter of the **GdiplusStartup** function is the address of a ULONG\_PTR. **GdiplusStartup** fills that variable with a token that is later passed to the [**GdiplusShutdown**](/windows/desktop/api/Gdiplusinit/nf-gdiplusinit-gdiplusshutdown) function. The second parameter of the **GdiplusStartup** function is the address of a [**GdiplusStartupInput**](/windows/desktop/api/Gdiplusinit/ns-gdiplusinit-gdiplusstartupinput) structure. The preceding code relies on the default **GdiplusStartupInput** constructor to set the structure members appropriately.

 

 




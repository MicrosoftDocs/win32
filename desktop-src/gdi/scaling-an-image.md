---
description: Some applications scale images; that is, they display zoomed or reduced views of an image. For example, a drawing application may provide a zoom feature that enables the user to view and edit a drawing on a pixel-by-pixel basis.
ms.assetid: ab7d5224-62de-40a8-909f-564f61c45d01
title: Scaling an Image
ms.topic: article
ms.date: 05/31/2018
---

# Scaling an Image

Some applications scale images; that is, they display zoomed or reduced views of an image. For example, a drawing application may provide a zoom feature that enables the user to view and edit a drawing on a pixel-by-pixel basis.

Applications scale images by calling the [**StretchBlt**](/windows/desktop/api/Wingdi/nf-wingdi-stretchblt) function. Like the [**BitBlt**](/windows/desktop/api/Wingdi/nf-wingdi-bitblt) function, **StretchBlt** copies bitmap data from a bitmap in a source device context ([**DC**](/windows/desktop/api/Winuser/nf-winuser-getdcex)) into a bitmap in a target DC. However, unlike the **BitBlt** function, **StretchBlt** scales the image based on the specified dimensions of the source and target rectangles. If the source rectangle is larger than the target rectangle, the resultant image will appear to have shrunk; if the source rectangle is smaller than the target rectangle, the resultant image will appear to have expanded.

If the target rectangle is smaller than the source rectangle, [**StretchBlt**](/windows/desktop/api/Wingdi/nf-wingdi-stretchblt) removes color data from the image according to a specified stretch mode as shown in the following table.



| Stretch mode | Method                                                                                                                    |
|--------------|---------------------------------------------------------------------------------------------------------------------------|
| BLACKONWHITE | Performs a logical AND operation on the color data for the eliminated pixels and the color data for the remaining pixels. |
| WHITEONBLACK | Performs a logical OR operation on the color data for the eliminated pixels and the color data for the remaining pixels.  |
| COLORONCOLOR | Eliminates the color data of the deleted pixels completely.                                                               |
| HALFTONE     | Approximates the original (source) color data in the destination.                                                         |



 

You set the stretch mode by calling the [**SetStretchBltMode**](/windows/desktop/api/Wingdi/nf-wingdi-setstretchbltmode) function.

The following example code is taken from an application that demonstrates all four of the stretch modes available with the [**StretchBlt**](/windows/desktop/api/Wingdi/nf-wingdi-stretchblt) function.


```C++
#include "stdafx.h"
#include "GDIBitmapScaling.h"
#include <commctrl.h>
#include <CommDlg.h>




#define MAX_LOADSTRING 100

// Global Variables:
HINSTANCE hInst;                                // current instance
TCHAR szTitle[MAX_LOADSTRING];                    // The title bar text
TCHAR szWindowClass[MAX_LOADSTRING];            // the main window class name

// Forward declarations of functions included in this code module:
ATOM                MyRegisterClass(HINSTANCE hInstance);
BOOL                InitInstance(HINSTANCE, int);
LRESULT CALLBACK    WndProc(HWND, UINT, WPARAM, LPARAM);


int APIENTRY _tWinMain(HINSTANCE hInstance,
                     HINSTANCE hPrevInstance,
                     LPTSTR    lpCmdLine,
                     int       nCmdShow)
{
    UNREFERENCED_PARAMETER(hPrevInstance);
    UNREFERENCED_PARAMETER(lpCmdLine);

     // TODO: Place code here.
    MSG msg;
    HACCEL hAccelTable;

    // Initialize global strings
    LoadString(hInstance, IDS_APP_TITLE, szTitle, MAX_LOADSTRING);
    LoadString(hInstance, IDC_GDIBITMAPSCALING, szWindowClass, MAX_LOADSTRING);
    MyRegisterClass(hInstance);

    // Perform application initialization:
    if (!InitInstance (hInstance, nCmdShow))
    {
        return FALSE;
    }

    hAccelTable = LoadAccelerators(hInstance, MAKEINTRESOURCE(IDC_GDIBITMAPSCALING));

    // Main message loop:
    while (GetMessage(&msg, NULL, 0, 0))
    {
        if (!TranslateAccelerator(msg.hwnd, hAccelTable, &msg))
        {
            TranslateMessage(&msg);
            DispatchMessage(&msg);
        }
    }

    return (int) msg.wParam;
}



//
//  FUNCTION: MyRegisterClass()
//
//  PURPOSE: Registers the window class.
//
//  COMMENTS:
//
//    This function and its usage are only necessary if you want this code
//    to be compatible with Win32 systems prior to the 'RegisterClassEx'
//    function that was added to Windows 95. It is important to call this function
//    so that the application will get 'well formed' small icons associated
//    with it.
//
ATOM MyRegisterClass(HINSTANCE hInstance)
{
    WNDCLASSEX wcex;

    wcex.cbSize = sizeof(WNDCLASSEX);

    wcex.style            = CS_HREDRAW | CS_VREDRAW;
    wcex.lpfnWndProc    = WndProc;
    wcex.cbClsExtra        = 0;
    wcex.cbWndExtra        = 0;
    wcex.hInstance        = hInstance;
    wcex.hIcon            = LoadIcon(hInstance, MAKEINTRESOURCE(IDI_GDIBITMAPSCALING));
    wcex.hCursor        = LoadCursor(NULL, IDC_ARROW);
    wcex.hbrBackground    = (HBRUSH)(COLOR_WINDOW+1);
    wcex.lpszMenuName    = MAKEINTRESOURCE(IDC_GDIBITMAPSCALING);
    wcex.lpszClassName    = szWindowClass;
    wcex.hIconSm        = LoadIcon(wcex.hInstance, MAKEINTRESOURCE(IDI_SMALL));

    return RegisterClassEx(&wcex);
}

//
//   FUNCTION: InitInstance(HINSTANCE, int)
//
//   PURPOSE: Saves instance handle and creates main window
//
//   COMMENTS:
//
//        In this function, we save the instance handle in a global variable and
//        create and display the main program window.
//

#define NEW_DIB_FORMAT(lpbih) (lpbih->biSize != sizeof(BITMAPCOREHEADER))
BOOL InitInstance(HINSTANCE hInstance, int nCmdShow)
{
   HWND hWnd;

   hInst = hInstance; // Store instance handle in our global variable

   hWnd = CreateWindow(szWindowClass, szTitle, WS_SYSMENU,
      CW_USEDEFAULT, 0, 1024, 768, NULL, NULL, hInstance, NULL);

   if (!hWnd)
   {
      return FALSE;
   }

   ShowWindow(hWnd, nCmdShow);
   UpdateWindow(hWnd);

   return TRUE;
}

static   HCURSOR hcurSave;

WORD DIBNumColors (LPVOID lpv)
{
    INT                 bits;
    LPBITMAPINFOHEADER  lpbih = (LPBITMAPINFOHEADER)lpv;
    LPBITMAPCOREHEADER  lpbch = (LPBITMAPCOREHEADER)lpv;

    /*  With the BITMAPINFO format headers, the size of the palette
     *  is in biClrUsed, whereas in the BITMAPCORE - style headers, it
     *  is dependent on the bits per pixel ( = 2 raised to the power of
     *  bits/pixel).
     */
    if (NEW_DIB_FORMAT(lpbih)) {
      if (lpbih->biClrUsed != 0)
        return (WORD)lpbih->biClrUsed;
      bits = lpbih->biBitCount;
    }
    else
      bits = lpbch->bcBitCount;

    if (bits > 8) 
      return 0; /* Since biClrUsed is 0, we dont have a an optimal palette */
    else
      return (1 << bits); 
}
/* Macro to determine to round off the given value to the closest byte */
#define WIDTHBYTES(i)   ((((i)+31) >> 5) << 2)
/******************************************************************************
 *                                                                            *
 *  FUNCTION   : DIBInfo(HANDLE hbi, LPBITMAPINFOHEADER lpbih)                *
 *                                                                            *
 *  PURPOSE    : Retrieves the DIB info associated with a CF_DIB              *
 *               format memory block.                                         *
 *                                                                            *
 *  RETURNS    : TRUE  - if successful.                                       *
 *               FALSE - otherwise                                            *
 *                                                                            *
 *****************************************************************************/
BOOL DIBInfo (HANDLE hbi, LPBITMAPINFOHEADER lpbih)
{
    if (hbi){
      *lpbih = *(LPBITMAPINFOHEADER)hbi;

      /* fill in the default fields */
      if (NEW_DIB_FORMAT(lpbih)) {
        if (lpbih->biSizeImage == 0L)
          lpbih->biSizeImage = WIDTHBYTES(lpbih->biWidth*lpbih->biBitCount) * lpbih->biHeight;

        if (lpbih->biClrUsed == 0L)
          lpbih->biClrUsed = DIBNumColors (lpbih);
      }

      return TRUE;
    }
    return FALSE;
}
/* flags for mmioSeek() */
#ifndef SEEK_SET
#define SEEK_SET        0               /* seek to an absolute position */
#define SEEK_CUR        1               /* seek relative to current position */
#define SEEK_END        2               /* seek relative to end of file */
#endif  /* ifndef SEEK_SET */
VOID ReadPackedFileHeader(HFILE hFile, LPBITMAPFILEHEADER lpbmfhdr, LPDWORD lpdwOffset)
{
    *lpdwOffset = _llseek(hFile, 0L, (UINT) SEEK_CUR);
    _hread(hFile, (LPSTR) &lpbmfhdr->bfType, sizeof(WORD)); /* read in bfType*/            
    _hread(hFile, (LPSTR) &lpbmfhdr->bfSize, sizeof(DWORD) * 3); /* read in last 3 dwords*/
}




/* macro to determine if resource is a DIB */
#define ISDIB(bft) ((bft) == BFT_BITMAP)

/* Header signatutes for various resources */
#define BFT_ICON   0x4349   /* 'IC' */
#define BFT_BITMAP 0x4d42   /* 'BM' */
#define BFT_CURSOR 0x5450   /* 'PT' */
HANDLE ReadDIBBitmapInfo (INT hFile)
{
    DWORD              dwOffset;
    HANDLE             hbi = NULL;
    INT                size;
    INT                i;
    WORD               nNumColors;
    LPRGBQUAD          lprgbq;
    BITMAPINFOHEADER   bih;
    BITMAPCOREHEADER   bch;
    LPBITMAPINFOHEADER lpbih;
    BITMAPFILEHEADER   bf;
    DWORD              dwDWMasks= 0;
    DWORD              dwWidth = 0;
    DWORD              dwHeight = 0;
    WORD               wPlanes, wBitCount;

    if (hFile == HFILE_ERROR)
        return NULL;

    /* Read the bitmap file header */
    ReadPackedFileHeader(hFile, &bf, &dwOffset);

    /* Do we have a RC HEADER? */
    if (!ISDIB (bf.bfType)) {    
      bf.bfOffBits = 0L;               
        _llseek(hFile, dwOffset, (UINT)SEEK_SET); /* seek back to beginning of file */
    }

    if (sizeof(bih) != _hread(hFile, (LPSTR)&bih, (UINT)sizeof(bih)))
      return FALSE;

    nNumColors = DIBNumColors (&bih);

    /* Check the nature (BITMAPINFO or BITMAPCORE) of the info. block
     * and extract the field information accordingly. If a BITMAPCOREHEADER, 
     * transfer it's field information to a BITMAPINFOHEADER-style block
     */
    switch (size = (INT)bih.biSize){
        case sizeof (BITMAPINFOHEADER):
            break;

        case sizeof (BITMAPCOREHEADER):

            bch = *(LPBITMAPCOREHEADER)&bih;

            dwWidth   = (DWORD)bch.bcWidth;
            dwHeight  = (DWORD)bch.bcHeight;
            wPlanes   = bch.bcPlanes;
            wBitCount = bch.bcBitCount;

            bih.biSize           = sizeof(BITMAPINFOHEADER);
            bih.biWidth          = dwWidth;
            bih.biHeight         = dwHeight;
            bih.biPlanes         = wPlanes;
            bih.biBitCount       = wBitCount;
            bih.biCompression    = BI_RGB;
            bih.biSizeImage      = 0;
            bih.biXPelsPerMeter  = 0;
            bih.biYPelsPerMeter  = 0;
            bih.biClrUsed        = nNumColors;
            bih.biClrImportant   = nNumColors;

            _llseek(hFile, (LONG)sizeof (BITMAPCOREHEADER) - sizeof (BITMAPINFOHEADER), (UINT)SEEK_CUR);
            break;

        default:
            /* Not a DIB! */
            return NULL;
    }

    /*  Fill in some default values if they are zero */
    if (bih.biSizeImage == 0){
        bih.biSizeImage = WIDTHBYTES((DWORD)bih.biWidth * bih.biBitCount) * bih.biHeight;
    }
    if (bih.biClrUsed == 0)
        bih.biClrUsed = DIBNumColors(&bih);

    /* Allocate for the BITMAPINFO structure and the color table. */
    if ((bih.biBitCount == 16) || (bih.biBitCount == 32))
      dwDWMasks = sizeof(DWORD) * 3;
    hbi = GlobalAlloc (GPTR, (LONG)bih.biSize + nNumColors * sizeof(RGBQUAD) + dwDWMasks);
    if (!hbi)
        return NULL;
    lpbih = (LPBITMAPINFOHEADER)hbi;
    *lpbih = bih;

    /* Get a pointer to the color table */
    lprgbq = (LPRGBQUAD)((LPSTR)lpbih + bih.biSize);
    if (nNumColors){
        if (size == sizeof(BITMAPCOREHEADER)){
            /* Convert a old color table (3 byte RGBTRIPLEs) to a new
             * color table (4 byte RGBQUADs)
             */
            _hread(hFile, (LPSTR)lprgbq, (UINT)nNumColors * sizeof(RGBTRIPLE));

            for (i = nNumColors - 1; i >= 0; i--){
                RGBQUAD rgbq;

                rgbq.rgbRed      = ((RGBTRIPLE*)lprgbq)[i].rgbtRed;
                rgbq.rgbBlue     = ((RGBTRIPLE*)lprgbq)[i].rgbtBlue;
                rgbq.rgbGreen    = ((RGBTRIPLE*)lprgbq)[i].rgbtGreen;
                rgbq.rgbReserved = (BYTE)0;

                lprgbq[i] = rgbq;
            }
        }
        else
            _hread(hFile, (LPSTR)lprgbq, (UINT)nNumColors * sizeof(RGBQUAD));
    } else
        if (dwDWMasks)
           _hread(hFile, (LPSTR)lprgbq, dwDWMasks);

    if (bf.bfOffBits != 0L){
        _llseek(hFile, dwOffset + bf.bfOffBits, (UINT)SEEK_SET);
        }
    
    return hbi;
}
HGLOBAL GlobalFreeDIB(HGLOBAL hDIB)
{
   LPBITMAPINFOHEADER lpbi = (LPBITMAPINFOHEADER)hDIB;

   if (!lpbi->biClrImportant)
     return GlobalFree(hDIB);

   if (GlobalFlags((HGLOBAL)lpbi->biClrImportant) == GMEM_INVALID_HANDLE) {
    SetLastError(0);
    return GlobalFree(hDIB);
  } else
    return GlobalFree((HANDLE)lpbi->biClrImportant); 
}
/******************************************************************************
 *                                                                            *
 *  FUNCTION   :  ColorTableSize(LPVOID lpv)                                  *
 *                                                                            *
 *  PURPOSE    :  Calculates the palette size in bytes. If the info. block    *
 *                is of the BITMAPCOREHEADER type, the number of colors is    *
 *                multiplied by 3 to give the palette size, otherwise the     *
 *                number of colors is multiplied by 4.                        *
 *                                                                            *
 *  RETURNS    :  Color table size in number of bytes.                        *
 *                                                                            *
 *****************************************************************************/
WORD ColorTableSize (LPVOID lpv)
{
    LPBITMAPINFOHEADER lpbih = (LPBITMAPINFOHEADER)lpv;
    
    if (NEW_DIB_FORMAT(lpbih))
    {
      if (((LPBITMAPINFOHEADER)(lpbih))->biCompression == BI_BITFIELDS)
         /* Remember that 16/32bpp dibs can still have a color table */
         return (sizeof(DWORD) * 3) + (DIBNumColors (lpbih) * sizeof (RGBQUAD));
      else
         return (DIBNumColors (lpbih) * sizeof (RGBQUAD));
    }
    else
      return (DIBNumColors (lpbih) * sizeof (RGBTRIPLE));
}

/******************************************************************************
 *                                                                            *
 *  FUNCTION   :OpenDIB(LPSTR szFilename)                                     *
 *                                                                            *
 *  PURPOSE    :Open a DIB file and create a memory DIB -- a memory handle    *
 *              containing BITMAPINFO, palette data and the bits.             * 
 *                                                                            *
 *  RETURNS    :A handle to the DIB.                                          *
 *                                                                            *
 *****************************************************************************/
HANDLE OpenDIB (LPSTR szFilename)
{
    HFILE               hFile;
    BITMAPINFOHEADER    bih;
    LPBITMAPINFOHEADER  lpbih;
    DWORD               dwLen = 0;
    DWORD               dwBits;
    HANDLE              hDIB;
    HANDLE              hMem;
    OFSTRUCT            of;

    /* Open the file and read the DIB information */
    hFile = OpenFile(szFilename, &of, (UINT)OF_READ);
    if (hFile == HFILE_ERROR)
        return NULL;

    hDIB = ReadDIBBitmapInfo(hFile);
    if (!hDIB)
        return NULL;
    DIBInfo(hDIB, &bih);

    /* Calculate the memory needed to hold the DIB */
    dwBits = bih.biSizeImage;
    dwLen  = bih.biSize + (DWORD)ColorTableSize (&bih) + dwBits;

    /* Try to increase the size of the bitmap info. buffer to hold the DIB */
    hMem = GlobalReAlloc(hDIB, dwLen, GMEM_MOVEABLE);

    if (!hMem){
        GlobalFreeDIB(hDIB);
        hDIB = NULL;
    }
    else
        hDIB = hMem;

    /* Read in the bits */
    if (hDIB){
        lpbih = (LPBITMAPINFOHEADER)hDIB;
        _hread(hFile, (LPSTR)lpbih + (WORD)lpbih->biSize + ColorTableSize(lpbih), dwBits);
    }
    _lclose(hFile);

    return hDIB;
}/* Macros to display/remove hourglass cursor for lengthy operations */
#define StartWait() hcurSave = SetCursor(LoadCursor(NULL, IDC_WAIT))
#define EndWait()   SetCursor(hcurSave)
/******************************************************************************
 *                                                                            *
 *  FUNCTION   : BitmapFromDIB(HANDLE hDIB, HPALETTE hPal)                    *
 *                                                                            *
 *  PURPOSE    : Will create a DDB (Device Dependent Bitmap) given a global   *
 *               handle to a memory block in CF_DIB format                    *
 *                                                                            *
 *  RETURNS    : A handle to the DDB.                                         *
 *                                                                            *
 *****************************************************************************/
HBITMAP BitmapFromDIB (HANDLE hDIB, HPALETTE  hPal)
{
    LPBITMAPINFOHEADER  lpbih;
    HPALETTE            hPalOld;
    HDC                 hDC;
    HBITMAP             hBitmap;  

    StartWait();

    if (!hDIB)
        return NULL;

    lpbih = (LPBITMAPINFOHEADER)hDIB;

    if (!lpbih)
        return NULL;

    hDC = GetDC(NULL);

    if (hPal){
        hPalOld = SelectPalette(hDC, hPal, FALSE);
        RealizePalette(hDC);     
    }                              
   
    hBitmap = CreateDIBitmap(hDC, 
                lpbih, 
                CBM_INIT, 
                (LPSTR)lpbih + lpbih->biSize + ColorTableSize(lpbih), 
                (LPBITMAPINFO)lpbih, 
                DIB_RGB_COLORS ); 

    if (hPal)
        SelectPalette(hDC, hPalOld, FALSE);

    ReleaseDC(NULL, hDC);

    EndWait();

    return hBitmap;
}
/******************************************************************************
 *                                                                            *
 *  FUNCTION   : DrawBitmap(HDC hDC, int x, int y,                            *
 *                          HBITMAP hBitmap, DWORD dwROP)                     * 
 *                                                                            *
 *  PURPOSE    : Draws bitmap <hBitmap> at the specified position in DC <hDC> *
 *                                                                            *
 *  RETURNS    : Return value of BitBlt()                                     *
 *                                                                            *
 *****************************************************************************/
BOOL DrawBitmap (HDC hDC, INT x, INT y, HBITMAP hBitmap, DWORD dwROP)
{
    HDC       hDCBits;
    BITMAP    Bitmap;
    BOOL      bResult;

    if (!hDC || !hBitmap)
        return FALSE;

    hDCBits = CreateCompatibleDC(hDC);
    GetObject(hBitmap, sizeof(BITMAP), (LPSTR)&Bitmap);
    SelectObject(hDCBits, hBitmap);
    bResult = BitBlt(hDC, x, y, Bitmap.bmWidth, Bitmap.bmHeight, hDCBits, 0, 0, dwROP);
    DeleteDC(hDCBits);

    return bResult;
}

  /*FUNCTION: WndProc(HWND, UINT, WPARAM, LPARAM)

  PURPOSE:  Processes messages for the main window.

  WM_COMMAND    - process the application menu
  WM_PAINT    - Paint the main window
  WM_DESTROY    - post a quit message and return*/



#define ID_LOADBITMAP 1

LRESULT CALLBACK WndProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam)
{
    int wmId, wmEvent;
    PAINTSTRUCT ps;
    //Handle to a GDI device context
    HDC hDC;
    //Handle to a DDB(device-dependent bitmap)
    HBITMAP hBitmap;
    

    HFONT hFont;
    NONCLIENTMETRICS ncm={0};
    ncm.cbSize= sizeof(NONCLIENTMETRICS);
    
    
    static HWND hwndButton;
    static HWND hwndButtonExit;
    static HANDLE hDIB = NULL;
    
    char szDirName[MAX_PATH];
    char szFilename[MAX_PATH]="\0";
    char szBitmapName[MAX_PATH]="\\Waterfall.bmp";
    //char szBitmapName[MAX_PATH]="\\tulips256.bmp";
    OPENFILENAMEA ofn;
        
    
    switch (message)
    {
    
    case WM_CREATE:
        
        //Creates a font from the current theme's caption font
        SystemParametersInfo(SPI_GETNONCLIENTMETRICS, NULL, &ncm, NULL);
        hFont = CreateFontIndirect(&ncm.lfCaptionFont);
        
        //Gets the device context for the current window
        hDC = GetDC(hWnd);
        
        //Gets the directory of the current project and loads Waterfall.bmp
        GetCurrentDirectoryA(MAX_PATH, szDirName);
        strcat_s(szDirName, szBitmapName);
        strcat_s(szFilename,szDirName);
        hDIB = OpenDIB(szFilename);
        hBitmap = BitmapFromDIB(hDIB, NULL);

        //Draws Waterfall.bmp as a device dependent bitmap
        DrawBitmap(hDC,0,0,hBitmap,SRCCOPY);
        InvalidateRect(hWnd, NULL, FALSE);
        ReleaseDC(hWnd,hDC);
    
        //Draws the "Load Bitmap" button
        hwndButton = CreateWindowW(TEXT("button"),TEXT("Load Bitmap"), 
            WS_CHILD | WS_VISIBLE | WS_BORDER, 600, 200, 150,50,
            hWnd, 
            (HMENU)ID_LOADBITMAP, 
            ((LPCREATESTRUCT) lParam)-> hInstance, NULL);

        //Set the font of the button to the theme's caption font
        SendMessage(hwndButton, WM_SETFONT, (WPARAM)hFont, TRUE );
        
    
        return 0;


    case WM_COMMAND:
        wmId    = LOWORD(wParam);
        wmEvent = HIWORD(wParam);
        
        
        //if Load Bitmap button is pressed
        if (wmId == ID_LOADBITMAP && wmEvent == BN_CLICKED)
        {
                            
            //Get the current directory name, and store in szDirName 
            GetCurrentDirectoryA(MAX_PATH, szDirName);
            
            //Set all structure members to zero. 
            ZeroMemory(&ofn, sizeof(OPENFILENAMEA));
            
            //Initializing the OPENFILENAMEA structure 
            ofn.lStructSize = sizeof(OPENFILENAMEA);
            ofn.hwndOwner = hWnd;
            ofn.lpstrFilter ="BMP Files (*.BMP)\0 *.BMP\0\0";
            ofn.lpstrFile = szFilename;
            ofn.nMaxFile = sizeof(szFilename);
            ofn.lpstrDefExt = "BMP";
            ofn.lpstrInitialDir = szDirName;
            ofn.Flags = OFN_EXPLORER | OFN_SHOWHELP | OFN_PATHMUSTEXIST | OFN_FILEMUSTEXIST;

                            

            if (GetOpenFileNameA(&ofn)) {
               hDIB = OpenDIB((LPSTR)szFilename);   
               if (!hDIB)
                  MessageBox(hWnd, TEXT("Unable to load file!"), TEXT("Oops"), MB_ICONSTOP);
            } else {
                if (strlen((const char *)szFilename) != 0)
                  MessageBox(hWnd, TEXT("Unable to load file!"), TEXT("Oops"), MB_ICONSTOP);
                
                return 0;
            }
            
            
            

            InvalidateRect(hWnd, NULL, FALSE);
                            
                        
        }
        
        
        break;
    case WM_PAINT:
        {
            //Initializing arrays for boxes
            POINT pRect1[5] = {{0,0},{400,0},{400,400},{0,400},{0,0}};
            POINT pRect2[5] = {{0,500}, {200, 500}, {200, 700}, {0,700},{0,500}};
            POINT pRect3[5] = {{210,500}, {410, 500}, {410, 700}, {210,700},{210,500}};
            POINT pRect4[5] = {{420,500}, {620, 500}, {620, 700}, {420,700},{420,500}};
            POINT pRect5[5] = {{630,500}, {830, 500}, {830, 700}, {630,700},{630,500}};
            
            //For the white background
            RECT clientRect;
            HRGN hRegion1;
            HRGN hRegion2;
            HRGN hRegion3;
            HBRUSH hBGBrush;
            
            //Handle to a logical font
            HFONT hFont;

            //Get the caption font that is currently in use
            SystemParametersInfo(SPI_GETNONCLIENTMETRICS, NULL, &ncm, NULL);
            hFont = CreateFontIndirect(&ncm.lfCaptionFont);
            
            //Begin drawing
            hDC = BeginPaint(hWnd, &ps);

            //Draw and fill rectangles for the background
            GetClientRect(hWnd, &clientRect);
            hRegion1 = CreateRectRgn(clientRect.left,clientRect.top,clientRect.right,clientRect.bottom);
            hBGBrush = CreateSolidBrush(RGB(255,255,255));
            FillRgn(hDC, hRegion1, hBGBrush);
            
            //Create an HBITMAP(device dependent bitmap) to be drawn
            hBitmap = BitmapFromDIB(hDIB,NULL);
            //Draw the DDB
            DrawBitmap(hDC,0,0,hBitmap,SRCCOPY);
            
            
            if(hDIB)
            {
                hRegion2 = CreateRectRgn(401,0,clientRect.right,401);
                hRegion3 = CreateRectRgn(0,401,clientRect.right,clientRect.bottom);
                FillRgn(hDC,hRegion2,hBGBrush);
                FillRgn(hDC,hRegion3,hBGBrush);
                //Set stretch mode as BLACKONWHITE and then copy from the 
                //source rectangle into the smaller rectangle
                SetStretchBltMode(hDC,BLACKONWHITE);
                StretchBlt(hDC,0,500,200,200,hDC, 0,0,400,400,SRCCOPY);
            
                //Set stretch mode as WHITEONBLACK and then copy from the 
                //source rectangle into the smaller rectangle
                SetStretchBltMode(hDC,WHITEONBLACK);
                StretchBlt(hDC,210,500,200,200, hDC, 0,0,400,400, SRCCOPY);
            
                //Set stretch mode as COLORONCOLOR and then copy from the 
                //source rectangle into the smaller rectangle
                SetStretchBltMode(hDC,COLORONCOLOR);
                StretchBlt(hDC,420,500,200,200, hDC, 0,0,400,400, SRCCOPY);

                //Set stretch mode as HALFTONE and then copy from the 
                //source rectangle into the smaller rectangle
                SetStretchBltMode(hDC,HALFTONE);
                StretchBlt(hDC,630,500,200,200, hDC, 0,0,400,400, SRCCOPY);

            }
            //Select the caption font created earlier
            SelectObject(hDC,hFont);

            //Create captions for each demonstration of color loss modes
            TextOut(hDC,50,480,TEXT("BLACKONWHITE"),12);
            TextOut(hDC,250,480,TEXT("WHITEONBLACK"),12);
            TextOut(hDC,460,480,TEXT("COLORONCOLOR"),12);
            TextOut(hDC,680,480,TEXT("HALFTONE"),8);
            DeleteObject(hFont);

            //Selecting the stock object pen to draw with
            SelectObject(hDC, GetStockObject(DC_PEN));
            //The pen is gray
            SetDCPenColor(hDC, RGB(80,80,80));
            
            //Polylines are drawn from arrays of POINTs
            Polyline(hDC, pRect1, 5);
            Polyline(hDC, pRect2, 5);
            Polyline(hDC, pRect3, 5);
            Polyline(hDC, pRect4, 5);
            Polyline(hDC, pRect5, 5);
            
            FillRgn(hDC,hRegion2,hBGBrush);
            EndPaint(hWnd, &ps);
            
            break;
        }
    case WM_DESTROY:
        PostQuitMessage(0);
        break;
    default:
        return DefWindowProc(hWnd, message, wParam, lParam);
    }
    return 0;
}

```



 

 




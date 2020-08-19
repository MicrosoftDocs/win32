---
title: Handling Screen Savers
description: The Microsoft Win32 API supports special applications called screen savers.
ms.assetid: cda5e690-71fe-4df7-b8a2-3a2ad65b1bfb
keywords:
- screen savers
- Control Panel,screen savers
- ScreenSaverConfigureDialog
- module-definition files
ms.topic: article
ms.date: 05/31/2018
---

# Handling Screen Savers

The Microsoft Win32 API supports special applications called *screen savers*. Screen savers start when the mouse and keyboard have been idle for a specified period of time. They are used for these two reasons:

-   To protect a screen from phosphor burn caused by static images.
-   To conceal sensitive information left on a screen.

This topic is divided into the following sections.

-   [About Screen Savers](#about-screen-savers)
-   [Using the Screen Saver Functions](#using-the-screen-saver-functions)
    -   [Creating a Screen Saver](#creating-a-screen-saver)
    -   [Installing New Screen Savers](#installing-new-screen-savers)
    -   [Adding Help to the Screen Saver Configuration Dialog Box](#adding-help-to-the-screen-saver-configuration-dialog-box)

## About Screen Savers

The Desktop application in the Windows Control Panel lets users select from a list of screen savers, specify how much time should elapse before the screen saver starts, configure screen savers, and preview screen savers. Screen savers are loaded automatically when Windows starts or when a user activates the screen saver through the Control Panel.

Once a screen saver is chosen, Windows monitors keystrokes and mouse movements and then starts the screen saver after a period of inactivity. However, Windows does not start the screen saver if any of the following conditions exist:

-   The active application is not a Windows-based application.
-   A computer-based training (CBT) window is present.
-   The active application receives the [WM\_SYSCOMMAND](../menurc/wm-syscommand.md) message with the *wParam* parameter set to the SC\_SCREENSAVE value, but it does not pass the message to the [DefWindowProc](/windows/win32/api/winuser/nf-winuser-defwindowproca) function.

**Security Context of the Screen Saver**

The security context of the screen saver is dependent on whether a user is interactively logged on. If a user is interactively logged on when the screen saver is invoked, the screen saver runs in the security context of the interactive user. If no user is logged on, the security context of the screen saver is dependent on the version of Windows being used.

-   Windows XP and Windows 2000 - screen saver runs in the context of LocalSystem with accounts restricted.
-   Windows 2003 - screen saver runs in the context of LocalService with all privileges removed and administrators group disabled.
-   Does not apply to Windows NT4.

The security context determines the level of privileged operations which can be done from a screen saver.

**Windows Vista and later:** If password protection is enabled by policy, the screen saver is started regardless of what an application does with the SC\_SCREENSAVE notification.

Screen savers contain specific exported functions, resource definitions, and variable declarations. The screen saver library contains the **main** function and other startup code required for a screen saver. When a screen saver starts, the startup code in the screen saver library creates a full-screen window. The window class for this window is declared as follows:


```
WNDCLASS cls; 
cls.hCursor        = NULL; 
cls.hIcon          = LoadIcon(hInst, MAKEINTATOM(ID_APP)); 
cls.lpszMenuName   = NULL; 
cls.lpszClassName  = "WindowsScreenSaverClass"; 
cls.hbrBackground  = GetStockObject(BLACK_BRUSH); 
cls.hInstance      = hInst; 
cls.style          = CS_VREDRAW  | CS_HREDRAW | CS_SAVEBITS | CS_DBLCLKS; 
cls.lpfnWndProc    = (WNDPROC) ScreenSaverProc; 
cls.cbWndExtra     = 0; 
cls.cbClsExtra     = 0;
```



To create a screen saver, most developers create a source code module containing three required functions and link them with the screen saver library. A screen saver module is responsible only for configuring itself and for providing visual effects.

One of the three required functions in a screen saver module is [**ScreenSaverProc**](/windows/desktop/api/scrnsave/nf-scrnsave-screensaverproc). This function processes specific messages and passes any unprocessed messages back to the screen saver library. Following are some of the typical messages processed by **ScreenSaverProc**.



| Message        | Meaning                                                                                                                                                                                    |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WM\_CREATE     | Retrieve any initialization data from the Regedit.ini file. Set a window timer for the screen saver window. Perform any other required initialization.                                     |
| WM\_ERASEBKGND | Erase the screen saver window and prepare for subsequent drawing operations.                                                                                                               |
| WM\_TIMER      | Perform drawing operations.                                                                                                                                                                |
| WM\_DESTROY    | Destroy the timers created when the application processed the [WM\_CREATE](../winmsg/wm-create.md) message. Perform any additional required cleanup. |



 

[**ScreenSaverProc**](/windows/desktop/api/scrnsave/nf-scrnsave-screensaverproc) passes unprocessed messages to the screen saver library by calling the [**DefScreenSaverProc**](/windows/desktop/api/scrnsave/nf-scrnsave-defscreensaverproc) function. The following table describes how this function processes various messages.



| Message         | Action                                                                    |
|-----------------|---------------------------------------------------------------------------|
| WM\_SETCURSOR   | Set the cursor to the null cursor, removing it from the screen.           |
| WM\_PAINT       | Paint the screen background.                                              |
| WM\_LBUTTONDOWN | Terminate the screen saver.                                               |
| WM\_MBUTTONDOWN | Terminate the screen saver.                                               |
| WM\_RBUTTONDOWN | Terminate the screen saver.                                               |
| WM\_KEYDOWN     | Terminate the screen saver.                                               |
| WM\_MOUSEMOVE   | Terminate the screen saver.                                               |
| WM\_ACTIVATE    | Terminate the screen saver if the *wParam* parameter is set to **FALSE**. |



 

The second required function in a screen saver module is [**ScreenSaverConfigureDialog**](/windows/desktop/api/scrnsave/nf-scrnsave-screensaverconfiguredialog). This function displays a dialog box that enables the user to configure the screen saver (an application must provide a corresponding dialog box template). Windows displays the configuration dialog box when the user selects the **Setup** button in the Control Panel's Screen Saver dialog box.

The third required function in a screen saver module is [**RegisterDialogClasses**](/windows/desktop/api/scrnsave/nf-scrnsave-registerdialogclasses). This function must be called by all screen saver applications. However, applications that do not require special windows or custom controls in the configuration dialog box can simply return **TRUE**. Applications requiring special windows or custom controls should use this function to register the corresponding window classes.

In addition to creating a module that supports the three functions just described, a screen saver should supply an icon. This icon is visible only when the screen saver is run as a standalone application. (To be run by the Control Panel, a screen saver must have the .scr file name extension; to be run as a standalone application, it must have the .exe file name extension.) The icon must be identified in the screen saver's resource file by the constant ID\_APP, which is defined in the Scrnsave.h header file.

One final requirement is a screen saver description string. The resource file for a screen saver must contain a string that the Control Panel displays as the screen saver name. The description string must be the first string in the resource file's string table (identified with the ordinal value 1). However, the description string is ignored by the Control Panel if the screen saver has a long filename. In such case, the filename will be used as the description string.

## Using the Screen Saver Functions

This section uses example code taken from a screen saver application to illustrate the following tasks:

-   [Creating a Screen Saver](#creating-a-screen-saver)
-   [Installing New Screen Savers](#installing-new-screen-savers)
-   [Adding Help to the Screen Saver Configuration Dialog Box](#adding-help-to-the-screen-saver-configuration-dialog-box)

### Creating a Screen Saver

At intervals ranging from 1 through 10 seconds, the application in this example repaints the screen with one of four colors: white, light gray, dark gray, and black. The application paints the screen each time it receives a [WM\_TIMER](../winmsg/wm-timer.md) message. The user can adjust the interval at which this message is sent by selecting the application's configuration dialog box and adjusting a single horizontal scroll bar.

### Screen saver library

The static screen saver functions are contained in the screen saver library. There are two versions of the library available, Scrnsave.lib and Scrnsavw.lib. You must link your project with one of these. Scrnsave.lib is used for screen savers that use ANSI characters, and Scrnsavw.lib is used for screen savers that use Unicode characters. A screen saver that is linked with Scrnsavw.lib will only run on Windows platforms that support Unicode, while a screen saver linked with Scrnsave.lib will run on any Windows platform.

### Supporting the configuration dialog box

Most screen savers provide a configuration dialog box to let the user specify customization data such as unique colors, drawing speeds, line thickness, fonts, and so on. To support the configuration dialog box, the application must provide a dialog box template and must also support the [**ScreenSaverConfigureDialog**](/windows/desktop/api/scrnsave/nf-scrnsave-screensaverconfiguredialog) function. Following is the dialog box template for the sample application.


```
DLG_SCRNSAVECONFIGURE DIALOG 6, 18, 160, 63
LANGUAGE LANG_NEUTRAL, SUBLANG_NEUTRAL
STYLE DS_MODALFRAME | WS_POPUP | WS_VISIBLE | WS_CAPTION | WS_SYSMENU
CAPTION "Sample Screen-Saver Setup"
FONT 8, "MS Shell Dlg"
BEGIN
    GROUPBOX      "Redraw Speed", 101, 0, 6, 98, 40
    SCROLLBAR     ID_SPEED, 5, 31, 89, 10
    LTEXT         "Fast", 103, 6, 21, 20, 8
    LTEXT         "Slow", 104, 75, 21, 20, 8
    PUSHBUTTON    "OK", ID_OK, 117, 10, 40, 14
    PUSHBUTTON    "Cancel", ID_CANCEL, 117, 32, 40, 14
END
```



You must define the constant used to identify the dialog box template by using the decimal value 2003, as in the following example:


```
#define  DLG_SCRNSAVECONFIGURE 2003
```



The following example shows the [**ScreenSaverConfigureDialog**](/windows/desktop/api/scrnsave/nf-scrnsave-screensaverconfiguredialog) function found in the sample application.


```
#define MINVEL  1                 // minimum redraw speed value     
#define MAXVEL  10                // maximum redraw speed value    
#define DEFVEL  5                 // default redraw speed value    
 
LONG    lSpeed = DEFVEL;          // redraw speed variable         
  
extern HINSTANCE hMainInstance;   // screen saver instance handle  
 
CHAR   szAppName[80];             // .ini section name             
CHAR   szTemp[20];                // temporary array of characters  
CHAR   szRedrawSpeed[ ] = "Redraw Speed";   // .ini speed entry 
CHAR   szIniFile[MAXFILELEN];     // .ini or registry file name  
 
BOOL WINAPI ScreenSaverConfigureDialog(hDlg, message, wParam, lParam) 
HWND     hDlg; 
UINT     message; 
DWORD    wParam; 
LONG     lParam; 
HRESULT  hr;
{ 
    static HWND hSpeed;   // handle to speed scroll bar 
    static HWND hOK;      // handle to OK push button  
 
    switch(message) 
    { 
        case WM_INITDIALOG: 
 
            // Retrieve the application name from the .rc file.  
            LoadString(hMainInstance, idsAppName, szAppName, 
                       80 * sizeof(TCHAR)); 
 
            // Retrieve the .ini (or registry) file name. 
            LoadString(hMainInstance, idsIniFile, szIniFile, 
                       MAXFILELEN * sizeof(TCHAR)); 
 
            // TODO: Add error checking to verify LoadString success
            //       for both calls.
            
            // Retrieve any redraw speed data from the registry. 
            lSpeed = GetPrivateProfileInt(szAppName, szRedrawSpeed, 
                                          DEFVEL, szIniFile); 
 
            // If the initialization file does not contain an entry 
            // for this screen saver, use the default value. 
            if(lSpeed > MAXVEL || lSpeed < MINVEL) 
                lSpeed = DEFVEL; 
 
            // Initialize the redraw speed scroll bar control.
            hSpeed = GetDlgItem(hDlg, ID_SPEED); 
            SetScrollRange(hSpeed, SB_CTL, MINVEL, MAXVEL, FALSE); 
            SetScrollPos(hSpeed, SB_CTL, lSpeed, TRUE); 
 
            // Retrieve a handle to the OK push button control.  
            hOK = GetDlgItem(hDlg, ID_OK); 
 
            return TRUE; 
 
        case WM_HSCROLL: 

            // Process scroll bar input, adjusting the lSpeed 
            // value as appropriate. 
            switch (LOWORD(wParam)) 
                { 
                    case SB_PAGEUP: 
                        --lSpeed; 
                    break; 
 
                    case SB_LINEUP: 
                        --lSpeed; 
                    break; 
 
                    case SB_PAGEDOWN: 
                        ++lSpeed; 
                    break; 
 
                    case SB_LINEDOWN: 
                        ++lSpeed; 
                    break; 
 
                    case SB_THUMBPOSITION: 
                        lSpeed = HIWORD(wParam); 
                    break; 
 
                    case SB_BOTTOM: 
                        lSpeed = MINVEL; 
                    break; 
 
                    case SB_TOP: 
                        lSpeed = MAXVEL; 
                    break; 
 
                    case SB_THUMBTRACK: 
                    case SB_ENDSCROLL: 
                        return TRUE; 
                    break; 
                } 

                if ((int) lSpeed <= MINVEL) 
                    lSpeed = MINVEL; 
                if ((int) lSpeed >= MAXVEL) 
                    lSpeed = MAXVEL; 
 
                SetScrollPos((HWND) lParam, SB_CTL, lSpeed, TRUE); 
            break; 
 
        case WM_COMMAND: 
            switch(LOWORD(wParam)) 
            { 
                case ID_OK: 
 
                    // Write the current redraw speed variable to
                    // the .ini file. 
                    hr = StringCchPrintf(szTemp, 20, "%ld", lSpeed);
                    if (SUCCEEDED(hr))
                        WritePrivateProfileString(szAppName, szRedrawSpeed, 
                                                  szTemp, szIniFile); 
 
                case ID_CANCEL: 
                    EndDialog(hDlg, LOWORD(wParam) == ID_OK); 

                return TRUE; 
            } 
    } 
    return FALSE; 
}
```



In addition to providing the dialog box template and supporting the [**ScreenSaverConfigureDialog**](/windows/desktop/api/scrnsave/nf-scrnsave-screensaverconfiguredialog) function, an application must also support the [**RegisterDialogClasses**](/windows/desktop/api/scrnsave/nf-scrnsave-registerdialogclasses) function. This function registers any nonstandard window classes required by the screen saver. Because the sample application used only standard window classes in its dialog box procedure, this function simply returns **TRUE**, as in the following example:


```
BOOL WINAPI RegisterDialogClasses(hInst) 
HANDLE  hInst; 
{ 
    return TRUE; 
}
```



### Supporting the screen saver window procedure

Each screen saver must support a window procedure named [**ScreenSaverProc**](/windows/desktop/api/scrnsave/nf-scrnsave-screensaverproc). Like most window procedures, **ScreenSaverProc** processes a set of specific messages and passes any unprocessed messages to a default procedure. However, instead of passing them to the [DefWindowProc](/windows/win32/api/winuser/nf-winuser-defwindowproca) function, **ScreenSaverProc** passes unprocessed messages to the [**DefScreenSaverProc**](/windows/desktop/api/scrnsave/nf-scrnsave-defscreensaverproc) function. Another difference between **ScreenSaverProc** and a normal window procedure is that the handle passed to **ScreenSaverProc** identifies the entire desktop rather than a client window. The following example shows the **ScreenSaverProc** window procedure for the sample screen saver.


```
LONG WINAPI ScreenSaverProc(hwnd, message, wParam, lParam) 
HWND  hwnd; 
UINT  message; 
DWORD wParam; 
LONG  lParam; 
{ 
    static HDC          hdc;      // device-context handle  
    static RECT         rc;       // RECT structure  
    static UINT         uTimer;   // timer identifier  
 
    switch(message) 
    { 
        case WM_CREATE: 
 
            // Retrieve the application name from the .rc file. 
            LoadString(hMainInstance, idsAppName, szAppName, 80 * sizeof(TCHAR)); 
 
            // Retrieve the .ini (or registry) file name. 
            LoadString(hMainInstance, idsIniFile, szIniFile, MAXFILELEN * sizeof(TCHAR)); 
 
            // TODO: Add error checking to verify LoadString success
            //       for both calls.
            
            // Retrieve any redraw speed data from the registry.  
            lSpeed = GetPrivateProfileInt(szAppName, szRedrawSpeed, 
                                          DEFVEL, szIniFile); 
 
            // Set a timer for the screen saver window using the 
            // redraw rate stored in Regedit.ini. 
            uTimer = SetTimer(hwnd, 1, lSpeed * 1000, NULL); 
            break; 
 
        case WM_ERASEBKGND: 
 
            // The WM_ERASEBKGND message is issued before the 
            // WM_TIMER message, allowing the screen saver to 
            // paint the background as appropriate. 

            hdc = GetDC(hwnd); 
            GetClientRect (hwnd, &rc); 
            FillRect (hdc, &rc, GetStockObject(BLACK_BRUSH)); 
            ReleaseDC(hwnd,hdc); 
            break; 
 
        case WM_TIMER: 
 
            // The WM_TIMER message is issued at (lSpeed * 1000) 
            // intervals, where lSpeed == .001 seconds. This 
            // code repaints the entire desktop with a white, 
            // light gray, dark gray, or black brush each 
            // time a WM_TIMER message is issued. 

            hdc = GetDC(hwnd); 
            GetClientRect(hwnd, &rc); 
            if (i++ <= 4) 
                FillRect(hdc, &rc, GetStockObject(i)); 
            else 
                (i = 0); 
            ReleaseDC(hwnd,hdc); 
            break; 
 
        case WM_DESTROY: 
 
            // When the WM_DESTROY message is issued, the screen saver 
            // must destroy any of the timers that were set at WM_CREATE 
            // time. 

            if (uTimer) 
                KillTimer(hwnd, uTimer); 
            break; 
    } 
 
    // DefScreenSaverProc processes any messages ignored by ScreenSaverProc. 
    return DefScreenSaverProc(hwnd, message, wParam, lParam); 
}
```



### Creating a module-definition file

The [**ScreenSaverProc**](/windows/desktop/api/scrnsave/nf-scrnsave-screensaverproc) and [**ScreenSaverConfigureDialog**](/windows/desktop/api/scrnsave/nf-scrnsave-screensaverconfiguredialog) functions must be exported in the application's module-definition file; [**RegisterDialogClasses**](/windows/desktop/api/scrnsave/nf-scrnsave-registerdialogclasses) should not be exported, however. The following example shows the module-definition file for the sample application.


```
NAME    SSTEST.SCR 

DESCRIPTION 'SCRNSAVE : Test' 
 
STUB    'WINSTUB.EXE' 
EXETYPE WINDOWS 
 
CODE    MOVEABLE 
DATA    MOVEABLE MULTIPLE 
 
HEAPSIZE  1024 
STACKSIZE 4096 
 
EXPORTS 
        ScreenSaverProc 
        ScreenSaverConfigureDialog
```



### Installing New Screen Savers

When compiling the list of available screen savers, the Control Panel searches the Windows Startup directory for files with the .scr extension. Because screen savers are standard Windows executable files with .exe extensions, you must rename them so they have .scr extensions and copy them to the correct directory.

### Adding Help to the Screen Saver Configuration Dialog Box

The configuration dialog box for a screen saver typically includes a **Help** button. Screen saver applications can check for the Help button identifier and call the [**WinHelp**](/windows/desktop/api/winuser/nf-winuser-winhelpa) function in the same way Help is provided in other Windows-based applications.

 

 
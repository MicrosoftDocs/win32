---
Description: To enumerate all the devices on the computer, call the EnumDisplayDevices function. The information that is returned also indicates which monitor is part of the desktop.
ms.assetid: 834dee04-66fa-42eb-adff-c08a74c6cea8
title: Enumeration and Display Control
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Enumeration and Display Control

To enumerate all the devices on the computer, call the [**EnumDisplayDevices**](/windows/win32/Winuser/nf-winuser-enumdisplaydevicesa?branch=master) function. The information that is returned also indicates which monitor is part of the desktop.

To enumerate the devices on the desktop that intersect a clipping region, call [**EnumDisplayMonitors**](/windows/win32/Winuser/nf-winuser-enumdisplaymonitors?branch=master). This returns the HMONITOR handle to each monitor, which is used with [**GetMonitorInfo**](/windows/win32/Winuser/nf-winuser-getmonitorinfoa?branch=master). To enumerate all the devices in the virtual screen, use **EnumDisplayMonitors**. as shown in the following code:


```C++
EnumDisplayMonitors(NULL, NULL, MyInfoEnumProc, 0);  
```



To get information about a display device, use [**EnumDisplaySettings**](/windows/win32/Winuser/nf-winuser-enumdisplaysettingsa?branch=master) or [**EnumDisplaySettingsEx**](/windows/win32/Winuser/nf-winuser-enumdisplaysettingsexa?branch=master).

The [**ChangeDisplaySettingsEx**](/windows/win32/Winuser/nf-winuser-changedisplaysettingsexa?branch=master) function is used to control the display devices on the computer. It can modify the configuration of the devices, such as specifying the position of a monitor on the virtual desktop and changing the bit depth of any display. Typically, an application does not use this function. To add a display monitor to a multiple-monitor system programmatically, set **DEVMODE.dmFields** to DM\_POSITION and specify a position (using **DEVMODE.dmPosition** ) for the monitor you are adding that is adjacent to at least one pixel of the display area of an existing monitor. To detach the monitor, set **DEVMODE.dmFields** to DM\_POSITION and set **DEVMODE.dmPelsWidth** and **DEVMODE.dmPelsHeight** to zero.

The following code demonstrates how to detach all secondary display devices from the desktop:


```
void DetachDisplay()
{
    BOOL            FoundSecondaryDisp = FALSE;
    DWORD           DispNum = 0;
    DISPLAY_DEVICE  DisplayDevice;
    LONG            Result;
    TCHAR           szTemp[200];
    int             i = 0;
    DEVMODE   defaultMode;

    // initialize DisplayDevice
    ZeroMemory(&amp;DisplayDevice, sizeof(DisplayDevice));
    DisplayDevice.cb = sizeof(DisplayDevice);

    // get all display devices
    while (EnumDisplayDevices(NULL, DispNum, &amp;DisplayDevice, 0))
        {
        ZeroMemory(&amp;defaultMode, sizeof(DEVMODE));
        defaultMode.dmSize = sizeof(DEVMODE);
        if ( !EnumDisplaySettings((LPSTR)DisplayDevice.DeviceName, ENUM_REGISTRY_SETTINGS, &amp;defaultMode) )
                  OutputDebugString("Store default failed\n");

        if ((DisplayDevice.StateFlags & DISPLAY_DEVICE_ATTACHED_TO_DESKTOP) &amp;&amp;
            !(DisplayDevice.StateFlags & DISPLAY_DEVICE_PRIMARY_DEVICE))
            {
            DEVMODE    DevMode;
            ZeroMemory(&amp;DevMode, sizeof(DevMode));
            DevMode.dmSize = sizeof(DevMode);
            DevMode.dmFields = DM_PELSWIDTH | DM_PELSHEIGHT | DM_BITSPERPEL | DM_POSITION
                        | DM_DISPLAYFREQUENCY | DM_DISPLAYFLAGS ;
            Result = ChangeDisplaySettingsEx((LPSTR)DisplayDevice.DeviceName, 
                                            &amp;DevMode,
                                            NULL,
                                            CDS_UPDATEREGISTRY,
                                            NULL);

            //The code below shows how to re-attach the secondary displays to the desktop

            //ChangeDisplaySettingsEx((LPSTR)DisplayDevice.DeviceName,
            //                       &amp;defaultMode,
            //                       NULL,
            //                       CDS_UPDATEREGISTRY,
            //                       NULL);

            }

        // Reinit DisplayDevice just to be extra clean

        ZeroMemory(&amp;DisplayDevice, sizeof(DisplayDevice));
        DisplayDevice.cb = sizeof(DisplayDevice);
        DispNum++;
        } // end while for all display devices
}
```



For each display device, the application can save information in the registry that describes the configuration parameters for the device, as well as location parameters. The application can also determine which displays are part of the desktop, and which are not, through the DISPLAY\_DEVICE\_ATTACHED\_TO\_DESKTOP flag in the [**DISPLAY\_DEVICE**](/windows/win32/Wingdi/ns-wingdi-_display_devicea?branch=master) structure. Once all the configuration information is stored in the registry, the application can call [**ChangeDisplaySettingsEx**](/windows/win32/Winuser/nf-winuser-changedisplaysettingsexa?branch=master) again to dynamically change the settings, with no restart required.

 

 




---
description: To enumerate all the devices on the computer, call the EnumDisplayDevices function. The information that is returned also indicates which monitor is part of the desktop.
ms.assetid: 834dee04-66fa-42eb-adff-c08a74c6cea8
title: Enumeration and Display Control
ms.topic: article
ms.date: 05/31/2018
---

# Enumeration and Display Control

To enumerate all the devices on the computer, call the [**EnumDisplayDevices**](/windows/desktop/api/Winuser/nf-winuser-enumdisplaydevicesa) function. The information that is returned also indicates which monitor is part of the desktop.

To enumerate the devices on the desktop that intersect a clipping region, call [**EnumDisplayMonitors**](/windows/desktop/api/Winuser/nf-winuser-enumdisplaymonitors). This returns the HMONITOR handle to each monitor, which is used with [**GetMonitorInfo**](/windows/desktop/api/Winuser/nf-winuser-getmonitorinfoa). To enumerate all the devices in the virtual screen, use **EnumDisplayMonitors**. as shown in the following code:


```C++
EnumDisplayMonitors(NULL, NULL, MyInfoEnumProc, 0);  
```



To get information about a display device, use [**EnumDisplaySettings**](/windows/desktop/api/Winuser/nf-winuser-enumdisplaysettingsa) or [**EnumDisplaySettingsEx**](/windows/desktop/api/Winuser/nf-winuser-enumdisplaysettingsexa).

The [**ChangeDisplaySettingsEx**](/windows/desktop/api/Winuser/nf-winuser-changedisplaysettingsexa) function is used to control the display devices on the computer. It can modify the configuration of the devices, such as specifying the position of a monitor on the virtual desktop and changing the bit depth of any display. Typically, an application does not use this function. To add a display monitor to a multiple-monitor system programmatically, set **DEVMODE.dmFields** to DM\_POSITION and specify a position (using **DEVMODE.dmPosition** ) for the monitor you are adding that is adjacent to at least one pixel of the display area of an existing monitor. To detach the monitor, set **DEVMODE.dmFields** to DM\_POSITION and set **DEVMODE.dmPelsWidth** and **DEVMODE.dmPelsHeight** to zero.

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
    ZeroMemory(&DisplayDevice, sizeof(DisplayDevice));
    DisplayDevice.cb = sizeof(DisplayDevice);

    // get all display devices
    while (EnumDisplayDevices(NULL, DispNum, &DisplayDevice, 0))
        {
        ZeroMemory(&defaultMode, sizeof(DEVMODE));
        defaultMode.dmSize = sizeof(DEVMODE);
        if ( !EnumDisplaySettings((LPSTR)DisplayDevice.DeviceName, ENUM_REGISTRY_SETTINGS, &defaultMode) )
                  OutputDebugString("Store default failed\n");

        if ((DisplayDevice.StateFlags & DISPLAY_DEVICE_ATTACHED_TO_DESKTOP) &&
            !(DisplayDevice.StateFlags & DISPLAY_DEVICE_PRIMARY_DEVICE))
            {
            DEVMODE    DevMode;
            ZeroMemory(&DevMode, sizeof(DevMode));
            DevMode.dmSize = sizeof(DevMode);
            DevMode.dmFields = DM_PELSWIDTH | DM_PELSHEIGHT | DM_BITSPERPEL | DM_POSITION
                        | DM_DISPLAYFREQUENCY | DM_DISPLAYFLAGS ;
            Result = ChangeDisplaySettingsEx((LPSTR)DisplayDevice.DeviceName, 
                                            &DevMode,
                                            NULL,
                                            CDS_UPDATEREGISTRY,
                                            NULL);

            //The code below shows how to re-attach the secondary displays to the desktop

            //ChangeDisplaySettingsEx((LPSTR)DisplayDevice.DeviceName,
            //                       &defaultMode,
            //                       NULL,
            //                       CDS_UPDATEREGISTRY,
            //                       NULL);

            }

        // Reinit DisplayDevice just to be extra clean

        ZeroMemory(&DisplayDevice, sizeof(DisplayDevice));
        DisplayDevice.cb = sizeof(DisplayDevice);
        DispNum++;
        } // end while for all display devices
}
```



For each display device, the application can save information in the registry that describes the configuration parameters for the device, as well as location parameters. The application can also determine which displays are part of the desktop, and which are not, through the DISPLAY\_DEVICE\_ATTACHED\_TO\_DESKTOP flag in the [**DISPLAY\_DEVICE**](/windows/desktop/api/Wingdi/ns-wingdi-display_devicea) structure. Once all the configuration information is stored in the registry, the application can call [**ChangeDisplaySettingsEx**](/windows/desktop/api/Winuser/nf-winuser-changedisplaysettingsexa) again to dynamically change the settings, with no restart required.

 

 




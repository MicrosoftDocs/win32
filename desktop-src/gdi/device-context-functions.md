---
description: The following functions are used with device contexts.
ms.assetid: 9ff68d16-0f27-4cc8-932a-b2063cfed135
title: Device Context Functions
ms.topic: article
ms.date: 05/31/2018
---

# Device Context Functions

The following functions are used with device contexts.



| Function                                                   | Description                                                                                                                               |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| [**CancelDC**](/windows/desktop/api/Wingdi/nf-wingdi-canceldc)                               | Cancels any pending operation on the specified device context.                                                                            |
| [**ChangeDisplaySettings**](/windows/desktop/api/Winuser/nf-winuser-changedisplaysettingsa)     | Changes the settings of the default display device to the specified graphics mode.                                                        |
| [**ChangeDisplaySettingsEx**](/windows/desktop/api/Winuser/nf-winuser-changedisplaysettingsexa) | Changes the settings of the specified display device to the specified graphics mode.                                                      |
| [**CreateCompatibleDC**](/windows/desktop/api/Wingdi/nf-wingdi-createcompatibledc)           | Creates a memory device context compatible with the specified device.                                                                     |
| [**CreateDC**](/windows/desktop/api/Wingdi/nf-wingdi-createdca)                               | Creates a device context for a device using the specified name.                                                                           |
| [**CreateIC**](/windows/desktop/api/Wingdi/nf-wingdi-createica)                               | Creates an information context for the specified device.                                                                                  |
| [**DeleteDC**](/windows/desktop/api/Wingdi/nf-wingdi-deletedc)                               | Deletes the specified device context.                                                                                                     |
| [**DeleteObject**](/windows/desktop/api/Wingdi/nf-wingdi-deleteobject)                       | Deletes a logical pen, brush, font, bitmap, region, or palette, freeing all system resources associated with the object.                  |
| [**DeviceCapabilities**](/windows/win32/api/wingdi/nf-wingdi-devicecapabilitiesa)           | Retrieves the capabilities of a printer device driver.                                                                                    |
| [**DrawEscape**](/windows/desktop/api/Wingdi/nf-wingdi-drawescape)                           | Provides drawing capabilities of the specified video display that are not directly available through the graphics device interface.       |
| [**EnumDisplayDevices**](/windows/desktop/api/Winuser/nf-winuser-enumdisplaydevicesa)           | Retrieves information about the display devices in a system.                                                                              |
| [**EnumDisplaySettings**](/windows/desktop/api/Winuser/nf-winuser-enumdisplaysettingsa)         | Retrieves information about one of the graphics modes for a display device.                                                               |
| [**EnumDisplaySettingsEx**](/windows/desktop/api/Winuser/nf-winuser-enumdisplaysettingsexa)     | Retrieves information about one of the graphics modes for a display device.                                                               |
| [**EnumObjects**](/windows/desktop/api/Wingdi/nf-wingdi-enumobjects)                         | Enumerates the pens or brushes available for the specified device context.                                                                |
| [**EnumObjectsProc**](/windows/win32/api/wingdi/nc-wingdi-gobjenumproc)                 | An application-defined callback function used with the [**EnumObjects**](/windows/desktop/api/Wingdi/nf-wingdi-enumobjects) function.                                       |
| [**GetCurrentObject**](/windows/desktop/api/Wingdi/nf-wingdi-getcurrentobject)               | Retrieves a handle to an object of the specified type that has been selected into the specified device context.                           |
| [**GetDC**](/windows/desktop/api/Winuser/nf-winuser-getdc)                                     | Retrieves a handle to a display device context for the client area of a specified window or for the entire screen.                        |
| [**GetDCBrushColor**](/windows/desktop/api/WinGdi/nf-wingdi-getdcbrushcolor)                 | Retrieves the current brush color for the specified device context.                                                                       |
| [**GetDCEx**](/windows/desktop/api/Winuser/nf-winuser-getdcex)                                 | Retrieves a handle to a display device context for the client area of a specified window or for the entire screen.                        |
| [**GetDCOrgEx**](/windows/desktop/api/Wingdi/nf-wingdi-getdcorgex)                           | Retrieves the final translation origin for a specified device context.                                                                    |
| [**GetDCPenColor**](/windows/desktop/api/WinGdi/nf-wingdi-getdcpencolor)                     | Retrieves the current pen color for the specified device context.                                                                         |
| [**GetDeviceCaps**](/windows/desktop/api/Wingdi/nf-wingdi-getdevicecaps)                     | Retrieves device-specific information for the specified device.                                                                           |
| [**GetLayout**](/windows/desktop/api/Wingdi/nf-wingdi-getlayout)                             | Retrieves the layout of a device context.                                                                                                 |
| [**GetObject**](/windows/desktop/api/Wingdi/nf-wingdi-getobject)                             | Retrieves information for the specified graphics object.                                                                                  |
| [**GetObjectType**](/windows/desktop/api/Wingdi/nf-wingdi-getobjecttype)                     | Retrieves the type of the specified object.                                                                                               |
| [**GetStockObject**](/windows/desktop/api/Wingdi/nf-wingdi-getstockobject)                   | Retrieves a handle to one of the stock pens, brushes, fonts, or palettes.                                                                 |
| [**ReleaseDC**](/windows/desktop/api/Winuser/nf-winuser-releasedc)                             | Releases a device context, freeing it for use by other applications.                                                                      |
| [**ResetDC**](/windows/desktop/api/Wingdi/nf-wingdi-resetdca)                                 | Updates the specified printer or plotter device context using the specified information.                                                  |
| [**RestoreDC**](/windows/desktop/api/Wingdi/nf-wingdi-restoredc)                             | Restores a device context to the specified state.                                                                                         |
| [**SaveDC**](/windows/desktop/api/Wingdi/nf-wingdi-savedc)                                   | Saves the current state of the specified device context by copying data describing selected objects and graphic modes to a context stack. |
| [**SelectObject**](/windows/desktop/api/Wingdi/nf-wingdi-selectobject)                       | Selects an object into the specified device context.                                                                                      |
| [**SetDCBrushColor**](/windows/desktop/api/Wingdi/nf-wingdi-setdcbrushcolor)                 | Sets the current device context brush color to the specified color value.                                                                 |
| [**SetDCPenColor**](/windows/desktop/api/Wingdi/nf-wingdi-setdcpencolor)                     | Sets the current device context pen color to the specified color value.                                                                   |
| [**SetLayout**](/windows/desktop/api/Wingdi/nf-wingdi-setlayout)                             | Sets the layout for a device context.                                                                                                     |
| [**WindowFromDC**](/windows/desktop/api/Winuser/nf-winuser-windowfromdc)                       | Returns a handle to the window associated with a device context.                                                                          |



 

 

 

---
Description: The following functions are used with device contexts.
ms.assetid: 9ff68d16-0f27-4cc8-932a-b2063cfed135
title: Device Context Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Device Context Functions

The following functions are used with device contexts.



| Function                                                   | Description                                                                                                                               |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| [**CancelDC**](/windows/win32/Wingdi/nf-wingdi-canceldc?branch=master)                               | Cancels any pending operation on the specified device context.                                                                            |
| [**ChangeDisplaySettings**](/windows/win32/Winuser/nf-winuser-changedisplaysettingsa?branch=master)     | Changes the settings of the default display device to the specified graphics mode.                                                        |
| [**ChangeDisplaySettingsEx**](/windows/win32/Winuser/nf-winuser-changedisplaysettingsexa?branch=master) | Changes the settings of the specified display device to the specified graphics mode.                                                      |
| [**CreateCompatibleDC**](/windows/win32/Wingdi/nf-wingdi-createcompatibledc?branch=master)           | Creates a memory device context compatible with the specified device.                                                                     |
| [**CreateDC**](/windows/win32/Wingdi/nf-wingdi-createdca?branch=master)                               | Creates a device context for a device using the specified name.                                                                           |
| [**CreateIC**](/windows/win32/Wingdi/nf-wingdi-createica?branch=master)                               | Creates an information context for the specified device.                                                                                  |
| [**DeleteDC**](/windows/win32/Wingdi/nf-wingdi-deletedc?branch=master)                               | Deletes the specified device context.                                                                                                     |
| [**DeleteObject**](/windows/win32/Wingdi/nf-wingdi-deleteobject?branch=master)                       | Deletes a logical pen, brush, font, bitmap, region, or palette, freeing all system resources associated with the object.                  |
| [**DeviceCapabilities**](gdi.devicecapabilities)           | Retrieves the capabilities of a printer device driver.                                                                                    |
| [**DrawEscape**](/windows/win32/Wingdi/nf-wingdi-drawescape?branch=master)                           | Provides drawing capabilities of the specified video display that are not directly available through the graphics device interface.       |
| [**EnumDisplayDevices**](/windows/win32/Winuser/nf-winuser-enumdisplaydevicesa?branch=master)           | Retrieves information about the display devices in a system.                                                                              |
| [**EnumDisplaySettings**](/windows/win32/Winuser/nf-winuser-enumdisplaysettingsa?branch=master)         | Retrieves information about one of the graphics modes for a display device.                                                               |
| [**EnumDisplaySettingsEx**](/windows/win32/Winuser/nf-winuser-enumdisplaysettingsexa?branch=master)     | Retrieves information about one of the graphics modes for a display device.                                                               |
| [**EnumObjects**](/windows/win32/Wingdi/nf-wingdi-enumobjects?branch=master)                         | Enumerates the pens or brushes available for the specified device context.                                                                |
| [**EnumObjectsProc**](enumobjectsproc.md)                 | An application-defined callback function used with the [**EnumObjects**](/windows/win32/Wingdi/nf-wingdi-enumobjects?branch=master) function.                                       |
| [**GetCurrentObject**](/windows/win32/Wingdi/nf-wingdi-getcurrentobject?branch=master)               | Retrieves a handle to an object of the specified type that has been selected into the specified device context.                           |
| [**GetDC**](/windows/win32/Winuser/nf-winuser-getdc?branch=master)                                     | Retrieves a handle to a display device context for the client area of a specified window or for the entire screen.                        |
| [**GetDCBrushColor**](/windows/win32/WinGdi/nf-wingdi-getdcbrushcolor?branch=master)                 | Retrieves the current brush color for the specified device context.                                                                       |
| [**GetDCEx**](/windows/win32/Winuser/nf-winuser-getdcex?branch=master)                                 | Retrieves a handle to a display device context for the client area of a specified window or for the entire screen.                        |
| [**GetDCOrgEx**](/windows/win32/Wingdi/nf-wingdi-getdcorgex?branch=master)                           | Retrieves the final translation origin for a specified device context.                                                                    |
| [**GetDCPenColor**](/windows/win32/WinGdi/nf-wingdi-getdcpencolor?branch=master)                     | Retrieves the current pen color for the specified device context.                                                                         |
| [**GetDeviceCaps**](/windows/win32/Wingdi/nf-wingdi-getdevicecaps?branch=master)                     | Retrieves device-specific information for the specified device.                                                                           |
| [**GetLayout**](/windows/win32/Wingdi/nf-wingdi-getlayout?branch=master)                             | Retrieves the layout of a device context.                                                                                                 |
| [**GetObject**](/windows/win32/Wingdi/nf-wingdi-getobject?branch=master)                             | Retrieves information for the specified graphics object.                                                                                  |
| [**GetObjectType**](/windows/win32/Wingdi/nf-wingdi-getobjecttype?branch=master)                     | Retrieves the type of the specified object.                                                                                               |
| [**GetStockObject**](/windows/win32/Wingdi/nf-wingdi-getstockobject?branch=master)                   | Retrieves a handle to one of the stock pens, brushes, fonts, or palettes.                                                                 |
| [**ReleaseDC**](/windows/win32/Winuser/nf-winuser-releasedc?branch=master)                             | Releases a device context, freeing it for use by other applications.                                                                      |
| [**ResetDC**](/windows/win32/Wingdi/nf-wingdi-resetdca?branch=master)                                 | Updates the specified printer or plotter device context using the specified information.                                                  |
| [**RestoreDC**](/windows/win32/Wingdi/nf-wingdi-restoredc?branch=master)                             | Restores a device context to the specified state.                                                                                         |
| [**SaveDC**](/windows/win32/Wingdi/nf-wingdi-savedc?branch=master)                                   | Saves the current state of the specified device context by copying data describing selected objects and graphic modes to a context stack. |
| [**SelectObject**](/windows/win32/Wingdi/nf-wingdi-selectobject?branch=master)                       | Selects an object into the specified device context.                                                                                      |
| [**SetDCBrushColor**](/windows/win32/Wingdi/nf-wingdi-setdcbrushcolor?branch=master)                 | Sets the current device context brush color to the specified color value.                                                                 |
| [**SetDCPenColor**](/windows/win32/Wingdi/nf-wingdi-setdcpencolor?branch=master)                     | Sets the current device context pen color to the specified color value.                                                                   |
| [**SetLayout**](/windows/win32/Wingdi/nf-wingdi-setlayout?branch=master)                             | Sets the layout for a device context.                                                                                                     |
| [**WindowFromDC**](/windows/win32/Winuser/nf-winuser-windowfromdc?branch=master)                       | Returns a handle to the window associated with a device context.                                                                          |



 

 

 




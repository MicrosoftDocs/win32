---
Description: 'The following functions are used with device contexts.'
ms.assetid: '9ff68d16-0f27-4cc8-932a-b2063cfed135'
title: Device Context Functions
---

# Device Context Functions

The following functions are used with device contexts.



| Function                                                   | Description                                                                                                                               |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| [**CancelDC**](canceldc.md)                               | Cancels any pending operation on the specified device context.                                                                            |
| [**ChangeDisplaySettings**](changedisplaysettings.md)     | Changes the settings of the default display device to the specified graphics mode.                                                        |
| [**ChangeDisplaySettingsEx**](changedisplaysettingsex.md) | Changes the settings of the specified display device to the specified graphics mode.                                                      |
| [**CreateCompatibleDC**](createcompatibledc.md)           | Creates a memory device context compatible with the specified device.                                                                     |
| [**CreateDC**](createdc.md)                               | Creates a device context for a device using the specified name.                                                                           |
| [**CreateIC**](createic.md)                               | Creates an information context for the specified device.                                                                                  |
| [**DeleteDC**](deletedc.md)                               | Deletes the specified device context.                                                                                                     |
| [**DeleteObject**](deleteobject.md)                       | Deletes a logical pen, brush, font, bitmap, region, or palette, freeing all system resources associated with the object.                  |
| [**DeviceCapabilities**](gdi.devicecapabilities)           | Retrieves the capabilities of a printer device driver.                                                                                    |
| [**DrawEscape**](drawescape.md)                           | Provides drawing capabilities of the specified video display that are not directly available through the graphics device interface.       |
| [**EnumDisplayDevices**](enumdisplaydevices.md)           | Retrieves information about the display devices in a system.                                                                              |
| [**EnumDisplaySettings**](enumdisplaysettings.md)         | Retrieves information about one of the graphics modes for a display device.                                                               |
| [**EnumDisplaySettingsEx**](enumdisplaysettingsex.md)     | Retrieves information about one of the graphics modes for a display device.                                                               |
| [**EnumObjects**](enumobjects.md)                         | Enumerates the pens or brushes available for the specified device context.                                                                |
| [**EnumObjectsProc**](enumobjectsproc.md)                 | An application-defined callback function used with the [**EnumObjects**](enumobjects.md) function.                                       |
| [**GetCurrentObject**](getcurrentobject.md)               | Retrieves a handle to an object of the specified type that has been selected into the specified device context.                           |
| [**GetDC**](getdc.md)                                     | Retrieves a handle to a display device context for the client area of a specified window or for the entire screen.                        |
| [**GetDCBrushColor**](getdcbrushcolor.md)                 | Retrieves the current brush color for the specified device context.                                                                       |
| [**GetDCEx**](getdcex.md)                                 | Retrieves a handle to a display device context for the client area of a specified window or for the entire screen.                        |
| [**GetDCOrgEx**](getdcorgex.md)                           | Retrieves the final translation origin for a specified device context.                                                                    |
| [**GetDCPenColor**](getdcpencolor.md)                     | Retrieves the current pen color for the specified device context.                                                                         |
| [**GetDeviceCaps**](getdevicecaps.md)                     | Retrieves device-specific information for the specified device.                                                                           |
| [**GetLayout**](getlayout.md)                             | Retrieves the layout of a device context.                                                                                                 |
| [**GetObject**](getobject.md)                             | Retrieves information for the specified graphics object.                                                                                  |
| [**GetObjectType**](getobjecttype.md)                     | Retrieves the type of the specified object.                                                                                               |
| [**GetStockObject**](getstockobject.md)                   | Retrieves a handle to one of the stock pens, brushes, fonts, or palettes.                                                                 |
| [**ReleaseDC**](releasedc.md)                             | Releases a device context, freeing it for use by other applications.                                                                      |
| [**ResetDC**](resetdc.md)                                 | Updates the specified printer or plotter device context using the specified information.                                                  |
| [**RestoreDC**](restoredc.md)                             | Restores a device context to the specified state.                                                                                         |
| [**SaveDC**](savedc.md)                                   | Saves the current state of the specified device context by copying data describing selected objects and graphic modes to a context stack. |
| [**SelectObject**](selectobject.md)                       | Selects an object into the specified device context.                                                                                      |
| [**SetDCBrushColor**](setdcbrushcolor.md)                 | Sets the current device context brush color to the specified color value.                                                                 |
| [**SetDCPenColor**](setdcpencolor.md)                     | Sets the current device context pen color to the specified color value.                                                                   |
| [**SetLayout**](setlayout.md)                             | Sets the layout for a device context.                                                                                                     |
| [**WindowFromDC**](windowfromdc.md)                       | Returns a handle to the window associated with a device context.                                                                          |



 

 

 




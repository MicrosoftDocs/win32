---
description: When a call is active in LINEBEARERMODE\_PASSTHROUGH, the service provider gives direct access to the attached hardware for control by the application.
ms.assetid: 75e31241-c782-4d50-9590-cf68c0505add
title: Passthrough Mode
ms.topic: article
ms.date: 05/31/2018
---

# Passthrough Mode

When a call is active in **LINEBEARERMODE\_PASSTHROUGH**, the service provider gives direct access to the attached hardware for control by the application. Applications can use this mode for temporary direct control over asynchronous modems, accessed through the [communications functions](/windows/desktop/DevIO/communications-functions), for the purpose of configuring or using special features not otherwise supported by the service provider, such as facsimile (Class 1, 2, and so on). This bearer mode is supported by the Universal Modem Driver (UNIMODEM) service provider.

Service providers that support **LINEBEARERMODE\_PASSTHROUGH** indicate it in the **dwBearerModes** member of the [**LINEDEVCAPS**](/windows/desktop/api/Tapi/ns-tapi-linedevcaps) structure. When **LINEBEARERMODE\_PASSTHROUGH** is indicated, the Unimodem service provider will also include in the **DevSpecific** area of the **LINEDEVCAPS** structure the registry key used to access data about the modem associated with the line device, in the following format:

``` syntax
struct {
    DWORD dwContents;   // Set to 1 (indicates containing key).
    DWORD dwKeyOffset;  // Offset to key from start of this
                        // structure (not from start of
                        // LINEDEVCAPS structure).
                        // 8 in this case. 
    BYTE rgby[...];     // Place that contains null-terminated
                        // registry key. 
}
```

For example:

``` syntax
    00000001 00000008 74737953 435c6d65  ........System\C
    65727275 6f43746e 6f72746e 7465536c  urrentControlSet
    7265535c 65636976 6c435c73 5c737361  urrentControlSet
    65646f4d 30305c6d xx003030 xxxxxxxx  Modem\0000.
```

This registry key could then be opened using the [**RegOpenKey**](/windows/desktop/api/winreg/nf-winreg-regopenkeya) function.

Passthrough mode is invoked most often using the [**lineMakeCall**](/windows/desktop/api/Tapi/nf-tapi-linemakecall) function, by setting the **LINEBEARERMODE\_PASSTHROUGH** bit in the **dwBearerMode** member of the [**LINECALLPARAMS**](/windows/desktop/api/Tapi/ns-tapi-linecallparams) structure pointed to by the *lpCallParams* parameter. When this is done, the service provider opens the serial port to the modem and immediately place the call into **LINECALLSTATE\_CONNECTED**. The application can then use the [**lineGetID**](/windows/desktop/api/Tapi/nf-tapi-linegetid) function with the device class "comm/datamodem" to obtain an open file handle to read from and write to the comm port.

Passthrough mode can be invoked in response to an incoming call as well. Generally, applications will invoke passthrough mode while the call is in **LINECALLSTATE\_OFFERING**, before the call has been answered. Instead of calling [**lineAnswer**](/windows/desktop/api/Tapi/nf-tapi-lineanswer), the application calls [**lineSetCallParams**](/windows/desktop/api/Tapi/nf-tapi-linesetcallparams), passing **LINEBEARERMODE\_PASSTHROUGH** as the *dwBearerMode* parameter. When this is done, as with [**lineMakeCall**](/windows/desktop/api/Tapi/nf-tapi-linemakecall), the call is immediately placed into **LINECALLSTATE\_CONNECTED** by the service provider, and the application can obtain a handle to the open port using [**lineGetID**](/windows/desktop/api/Tapi/nf-tapi-linegetid). The **lineSetCallParams** function can be called when the call is in **LINECALLSTATE\_OFFERING**, **LINECALLSTATE\_ACCEPTED**, or **LINECALLSTATE\_CONNECTED**.

Passthrough mode is normally terminated by calling [**lineDrop**](/windows/desktop/api/Tapi/nf-tapi-linedrop) on the call handle obtained from [**lineMakeCall**](/windows/desktop/api/Tapi/nf-tapi-linemakecall) or the first [**LINE\_CALLSTATE**](line-callstate.md) message, if the call was an incoming call. The service provider will close the port, and restore the modem to its default state. The application must call [**CloseHandle**](/windows/desktop/api/handleapi/nf-handleapi-closehandle) on the handle it received from [**lineGetID**](/windows/desktop/api/Tapi/nf-tapi-linegetid).

Passthrough mode can also be terminated by calling [**lineSetCallParams**](/windows/desktop/api/Tapi/nf-tapi-linesetcallparams) with the *dwBearerMode* parameter set to **LINEBEARERMODE\_VOICE**. The media type (mode) set by [**lineSetMediaMode**](/windows/desktop/api/Tapi/nf-tapi-linesetmediamode) is presumed to be in effect. If **LINEMEDIAMODE\_DATAMODEM** is active, the service provider will take over the call as though it was a data modem call already in progress; if [**lineDrop**](/windows/desktop/api/Tapi/nf-tapi-linedrop) is subsequently called, the service provider will issue the appropriate modem commands or interface state changes to drop a data call.

> [!Note]  
> If Passthrough mode is terminated while the call is in progress, the TAPI service provider (TSP) for the line may restore the modem settings to their default state. Unimodem is an example of a TSP that always restores the modem settings when terminating passthrough mode. For this reason, Passthrough mode cannot be used as a method to configure the device. Passthrough mode should only be used for distinct activities that can be considered complete when Passthrough is terminated. Examples of activities that can use passthrough mode include sending a fax or playing wave/audio data through a proprietary modem protocol.

 

 

 

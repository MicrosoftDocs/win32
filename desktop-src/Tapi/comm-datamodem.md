---
description: The comm/datamodem device class consists of datamodem devices.
ms.assetid: 6bc314c6-30ec-4318-856a-3ab2fa6aadfb
title: comm/datamodem
ms.topic: article
ms.date: 05/31/2018
---

# comm/datamodem

The comm/datamodem device class consists of datamodem devices. You access these devices by using the [file](/windows/desktop/FileIO/file-management-functions) and [communications functions](/windows/desktop/DevIO/communications-functions). Devices in this class are associated with line devices that support the LINEMEDIAMODE\_DATAMODEM media type, which is specified in the **dwMediaModes** member of the [**LINEDEVCAPS**](/windows/desktop/api/Tapi/ns-tapi-linedevcaps) structure for the line device.

The [**lineGetID**](/windows/desktop/api/Tapi/nf-tapi-linegetid) function fills a [**VARSTRING**](/windows/desktop/api/Tapi/ns-tapi-varstring) structure, setting **dwStringFormat** to the STRINGFORMAT\_BINARY value and appending these additional members:

``` syntax
HANDLE hComm;            // file handle to data modem
CHAR   szDeviceName[1];  // name of data modem
```

The **hComm** member is the handle of the open communications port. This member is **NULL** if the port is not yet open or if the *dwSelect* parameter of [**lineGetID**](/windows/desktop/api/Tapi/nf-tapi-linegetid) is not the LINECALLSELECT\_CALL value. If a call is active, the service provider typically opens the port itself to get direct control of the communications hardware, but is only required to return a valid handle if the line is connected. The service provider opens the port using the FILE\_FLAG\_OVERLAPPED value and then configures the port using the settings specified by the [**lineSetDevConfig**](/windows/desktop/api/Tapi/nf-tapi-linesetdevconfig) function. You can set additional configuration options for the device by using communications functions with the returned handle.

The **szDeviceName** member is a **null**-terminated string that specifies the name of the communications port associated with the line, address, or call.

If **hComm** is a valid handle, you can use it in subsequent calls to file functions, such as [**ReadFile**](/windows/desktop/api/fileapi/nf-fileapi-readfile) and [**WriteFile**](/windows/desktop/api/fileapi/nf-fileapi-writefile), to send and receive data on the call. When you are finished using the communications port and preferably before you use the [**lineDeallocateCall**](/windows/desktop/api/Tapi/nf-tapi-linedeallocatecall) function to deallocate the call, you must close the port by using the [**CloseHandle**](/windows/desktop/api/handleapi/nf-handleapi-closehandle) function.

When using the [**lineGetDevConfig**](/windows/desktop/api/Tapi/nf-tapi-linegetdevconfig) and [**lineSetDevConfig**](/windows/desktop/api/Tapi/nf-tapi-linesetdevconfig) functions, some service providers require that the configuration data for this device class have the following format:

``` syntax
typedef struct  tagDEVCFG  {
  DEVCFGHDR   dfgHdr;
  COMMCONFIG  commconfig;
} DEVCFG, *PDEVCFG, FAR* LPDEVCFG;

// Device setting information
typedef struct  tagDEVCFGDR  {
  DWORD       dwSize;
  DWORD       dwVersion;
  WORD        fwOptions;
  WORD        wWaitBong;
} DEVCFGHDR;
```

The following is device configuration information for use with the [**lineGetDevConfig**](/windows/desktop/api/Tapi/nf-tapi-linegetdevconfig) and [**lineSetDevConfig**](/windows/desktop/api/Tapi/nf-tapi-linesetdevconfig) functions.

<dl> <dt>

<span id="dwSize"></span><span id="dwsize"></span><span id="DWSIZE"></span>**dwSize**
</dt> <dd>

Sum of the size of the **DEVCFGHDR** structure and the actual size of the [**COMMCONFIG**](/windows/desktop/api/winbase/ns-winbase-commconfig) structure.

</dd> <dt>

<span id="dwVersion"></span><span id="dwversion"></span><span id="DWVERSION"></span>**dwVersion**
</dt> <dd>

Version number of the Unimodem **DevConfig** structure. This member can be MDMCFG\_VERSION (0x00010003).

</dd> <dt>

<span id="fwOptions"></span><span id="fwoptions"></span><span id="FWOPTIONS"></span>**fwOptions**
</dt> <dd>

Option flags that appear on the Unimodem Option page. This member can be a combination of these values:

<dl> <dt>

<span id="TERMINAL_PRE__1_"></span><span id="terminal_pre__1_"></span>TERMINAL\_PRE (1)
</dt> <dd>

Displays the pre-terminal screen.

</dd> <dt>

<span id="TERMINAL_POST__2_"></span><span id="terminal_post__2_"></span>TERMINAL\_POST (2)
</dt> <dd>

Displays the post-terminal screen.

</dd> <dt>

<span id="MANUAL_DIAL__4_"></span><span id="manual_dial__4_"></span>MANUAL\_DIAL (4)
</dt> <dd>

Dials the phone manually, if capable of doing so.

</dd> <dt>

<span id="LAUNCH_LIGHTS__8_"></span><span id="launch_lights__8_"></span>LAUNCH\_LIGHTS (8)
</dt> <dd>

Displays the modem icon in the status area of the taskbar.

Only the LAUNCH\_LIGHTS value is set by default

</dd> </dl> </dd> <dt>

<span id="wWaitBong"></span><span id="wwaitbong"></span><span id="WWAITBONG"></span>**wWaitBong**
</dt> <dd>

Number of seconds (in two seconds granularity) to replace the wait for credit tone ($).

</dd> <dt>

<span id="Commconfig"></span><span id="commconfig"></span><span id="COMMCONFIG"></span>**Commconfig**
</dt> <dd>

[**COMMCONFIG**](/windows/desktop/api/winbase/ns-winbase-commconfig) structure that can be used with the communications and modem configuration functions.

</dd> </dl>

 

 

---
description: Installs the system components specified.
ms.assetid: f4b7b8e5-b392-4208-9f56-b343974e05ff
title: IcfgInstallInetComponents function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IcfgInstallInetComponents
api_type: 
- DllExport
api_location: 
- Icfgnt5.dll
---

# IcfgInstallInetComponents function

Installs the system components specified.

## Syntax


```C++
HRESULT IcfgInstallInetComponents(
   HWND   hwndParent,
   DWORD  dwfOptions,
   LPBOOL lpfNeedsRestart
);
```



## Parameters

<dl> <dt>

*hwndParent* 
</dt> <dd>

A handle to the parent window.

</dd> <dt>

*dwfOptions* 
</dt> <dd>

A combination of the following flags that control the installation and configuration.



| Value                                                                                                                                                                                                                                  | Meaning                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| <span id="ICFG_INSTALLMAIL"></span><span id="icfg_installmail"></span><dl> <dt>**ICFG\_INSTALLMAIL**</dt> <dt>0x00000004</dt> </dl> | Install Exchange and Internet mail.<br/> |
| <span id="ICFG_INSTALLRAS"></span><span id="icfg_installras"></span><dl> <dt>**ICFG\_INSTALLRAS**</dt> <dt>0x00000002</dt> </dl>    | Install RAS (if needed).<br/>            |
| <span id="ICFG_INSTALLTCP"></span><span id="icfg_installtcp"></span><dl> <dt>**ICFG\_INSTALLTCP**</dt> <dt>0x00000001</dt> </dl>    | Install TCP/IP (if needed).<br/>         |



 

</dd> <dt>

*lpfNeedsRestart* 
</dt> <dd>

If this value is non-**NULL**, on return it will be **TRUE** only if Windows must be restarted to complete the installation.

</dd> </dl>

## Return value

Returns an **HRESULT** value. If no errors occur, it returns the **ERROR\_SUCCESS** code.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Icfgnt5.dll</dt> </dl> |



 

 

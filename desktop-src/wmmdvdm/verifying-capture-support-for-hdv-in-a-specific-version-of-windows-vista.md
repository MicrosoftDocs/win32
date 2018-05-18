---
title: Verifying Capture Support for HDV in a Specific Version of Windows Vista
description: Verifying Capture Support for HDV in a Specific Version of Windows Vista
ms.assetid: 'fb91bda8-8fde-4eb6-baae-ad509476c180'
keywords: ["Windows DVD Maker,capturing HDV from camcorders", "DVD Maker,capturing HDV from camcorders", "programming guide,capturing HDV from camcorders", "Windows Vista,capturing HDV from camcorders", "Windows Vista,Capture Wizard", "Capture Wizard", "capturing HDV from camcorders", "high-definition video (HDV)", "HDV (high-definition video)"]
---

# Verifying Capture Support for HDV in a Specific Version of Windows Vista

To determine whether your computer can capture high-definition video (HDV) from a camcorder by using the Capture Wizard on a specific version of Windows Vista, call the following software licensing function:


```C++
HRESULT WINAPI SLGetWindowsInformationDWORD( PCWSTR pwszValueName, DWORD* pdwValue );
```



When you call **SLGetWindowsInformationDWORD** with "CaptureWizard-HiDef" as the value of the *pwszValueName* parameter, you can determine whether HDV is supported by the Capture Wizard on your computer by reading the value pointed to by the out parameter, *pdwValue*.

For more information, see the reference for the [SLGetWindowsInformationDWORD](http://go.microsoft.com/fwlink/p/?linkid=91953) function on MSDN.

## Related topics

<dl> <dt>

[**Getting Information from Windows Vista About Windows Movie Maker and Windows DVD Maker**](getting-information-from-windows-vista-about-windows-movie-maker-and-windows-dvd-maker.md)
</dt> </dl>

 

 





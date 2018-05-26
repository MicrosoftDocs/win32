---
title: Verifying That Windows DVD Maker Has the Right to Run on a Specific Version of Windows Vista
description: Verifying That Windows DVD Maker Has the Right to Run on a Specific Version of Windows Vista
ms.assetid: f9424044-0c20-4b09-8571-6670ba411a9b
keywords:
- Windows DVD Maker,specific Windows Vista versions
- DVD Maker,specific Windows Vista versions
- programming guide,specific Windows Vista versions
- Windows Vista,specific versions for Windows DVD Maker
- SLGetWindowsInformationDWORD function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Verifying That Windows DVD Maker Has the Right to Run on a Specific Version of Windows Vista

You can verify that Windows DVD Maker has the right to run on a specific version of Windows Vista by using the following software licensing function:


```C++
HRESULT WINAPI SLGetWindowsInformationDWORD( PCWSTR pwszValueName, DWORD* pdwValue );
```



When you call **SLGetWindowsInformationDWORD** with "OMD-API-Enabled" as the value of the *pwszValueName* parameter, you can determine whether Windows DVD Maker has the right to run on your computer by reading the value pointed to by the out parameter *pdwValue*.

For more information, see the reference for the [SLGetWindowsInformationDWORD](http://go.microsoft.com/fwlink/p/?linkid=91953) function on MSDN.

## Related topics

<dl> <dt>

[**Getting Information from Windows Vista About Windows Movie Maker and Windows DVD Maker**](getting-information-from-windows-vista-about-windows-movie-maker-and-windows-dvd-maker.md)
</dt> </dl>

 

 





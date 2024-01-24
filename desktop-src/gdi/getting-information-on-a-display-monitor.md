---
description: The following code sample shows how to use EnumDisplayDevices to get information on a display monitor.
ms.assetid: 8c2420de-292f-481e-b06b-54cc174a8faf
title: Getting Information on a Display Monitor
ms.topic: article
ms.date: 05/31/2018
---

# Getting Information on a Display Monitor

The following code sample shows how to use [**EnumDisplayDevices**](/windows/desktop/api/Winuser/nf-winuser-enumdisplaydevicesa) to get information on a display monitor.


```C++
BOOL GetDisplayMonitorInfo(int nDeviceIndex, LPSTR lpszMonitorInfo)
{
    FARPROC EnumDisplayDevices;
    HINSTANCE  hInstUser32;
    DISPLAY_DEVICE DispDev; 
    char szSaveDeviceName[33];  // 32 + 1 for the null-terminator 
    BOOL bRet = TRUE;
        HRESULT hr;
    
    hInstUser32 = LoadLibrary("c:\\windows\User32.DLL");
    if (!hInstUser32) return FALSE;  
    
    // Get the address of the EnumDisplayDevices function 
    EnumDisplayDevices = (FARPROC)GetProcAddress(hInstUser32,"EnumDisplayDevicesA");
    if (!EnumDisplayDevices) {
        FreeLibrary(hInstUser32);
        return FALSE;
    }

    ZeroMemory(&DispDev, sizeof(DispDev));
    DispDev.cb = sizeof(DispDev); 
    
    // After the first call to EnumDisplayDevices,  
    // DispDev.DeviceString is the adapter name 
    if (EnumDisplayDevices(NULL, nDeviceIndex, &DispDev, 0)) 
        {  
                hr = StringCchCopy(szSaveDeviceName, 33, DispDev.DeviceName);
                if (FAILED(hr))
                {
                // TODO: write error handler 
                }
        
        // After second call, DispDev.DeviceString is the  
        // monitor name for that device  
        EnumDisplayDevices(szSaveDeviceName, 0, &DispDev, 0);   
        
                // In the following, lpszMonitorInfo must be 128 + 1 for  
                // the null-terminator. 
                hr = StringCchCopy(lpszMonitorInfo, 129, DispDev.DeviceString);
                if (FAILED(hr))
                {
                // TODO: write error handler 
                }
                
    } else    {
        bRet = FALSE;
    }

    FreeLibrary(hInstUser32);

    return bRet;
}
```



 

 




---
title: Gaming Device Information
description: Due to differing console capabilities, Universal Windows Platform (UWP) game developers on Xbox need a way to determine the type of console the game is running on, in order to make run-time choices on how to best use the hardware.
ms.assetid: bf210289-5963-4327-828b-98a0d14b5bfa
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Gaming Device Information

Due to differing console capabilities, Universal Windows Platform (UWP) game developers on Xbox need a way to determine the type of console the game is running on, in order to make run-time choices on how to best use the hardware. The Gaming Device Information APIs in **&lt;gamingdeviceinformation.h&gt;** provide this functionality.

> [!Note]  
> These are Win32 APIs that are supported in both Win32 and UWP apps. While they work on any device family, they are only really of value on Xbox devices.

 

## Example: Allocate memory on startup

This is a simple query example which demonstrates an early call pattern for allocating pool memory that is specialized for the target device.


```C++
int init_game(void)
{
    GAMING_DEVICE_MODEL_INFORMATION modelInformation;
    if (FAILED(GetGamingDeviceModelInformation(&amp;modelInformation)))
    {
        // Optionally, allocate a generic memory pool with whatever 
        // the default characteristics are. 
        return 0;
    }

    if (modelInformation.vendorId != GAMING_DEVICE_VENDOR_ID_MICROSOFT)
    {
        return 0;
    }

    if (modelInformation.deviceId == GAMING_DEVICE_DEVICE_ID_XBOX_ONE_X)
    {
        // Allocate pool of memory with appropriate characteristics for 
        // Xbox One X (i.e. write combined, cachable, GPU read-only, etc). 
    }

    if (modelInformation.deviceId == GAMING_DEVICE_DEVICE_ID_XBOX_ONE_X_DEVKIT)
    {
        // Allocate block of tools memory. 
    }

    return 0;
}

[Platform::MTAThread]
int __cdecl main(Platform::Array<Platform::String^>^)
{
    init_game();
    auto direct3DApplicationSource = ref new Direct3DApplicationSource();
    CoreApplication::Run(direct3DApplicationSource);
    return 0;
}
```



## In this section



| Topic                                       | Description                                                               |
|---------------------------------------------|---------------------------------------------------------------------------|
| [Enumerations](enumerations.md)<br/> | The Gaming Device Information API contains these enumerations.<br/> |
| [Functions](functions.md)<br/>       | The Gaming Device Information API contains these functions.<br/>    |
| [Structures](structures.md)<br/>     | The Gaming Device Information API contains these structures.<br/>   |



 

 

 






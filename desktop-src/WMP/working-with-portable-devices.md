---
title: Working with Portable Devices
description: Working with Portable Devices
ms.assetid: 145ede07-a23b-486b-a561-9c87a48b72a8
keywords:
- Windows Media Player,portable devices
- Windows Media Player object model,portable devices
- object model,portable devices
- Windows Media Player ActiveX control,portable devices
- ActiveX control,portable devices
- Windows Media Player Mobile ActiveX control,portable devices
- Windows Media Player Mobile,portable devices
- portable devices,about
ms.topic: article
ms.date: 05/31/2018
---

# Working with Portable Devices

This section describes how to use a remoted Windows Media Player ActiveX control to work with portable devices.

The code examples in this section use Active Template Library (ATL) classes, such as **CComPtr**.

## Included Headers

To use the code in this section, include the following headers:


```C++
#include <atlbase.h>
#include <atlcom.h>
#include <atlwin.h>
#include <commctrl.h>
#include "wmp.h"
#include "wmpids.h"
```



## IWMPPlayer Pointer

The **IWMPPlayer** pointer is stored in a member variable.


```C++
CComPtr<IWMPPlayer> m_spPlayer;
```



## Devices are Stored in an Array

The example code accesses the following member variable, to be declared in the project header:


```C++
IWMPSyncDevice **m_ppWMPDevices; // Points to the custom device array.
```



The device count is stored in a member variable.


```C++
int m_cDevices; // Count of devices.
```



## Retrieving a Device Pointer

A pointer to a particular device is retrieved through its array index by using code similar to the following:


```C++
CComPtr<IWMPSyncDevice> spSyncDevice(m_ppWMPDevices[lIndex]);
```



Note that the index shown in the preceding examples is not the partnership index for the device. It is the index to the device in the custom array of devices.

## Cleaning Up

The examples use the following function to free the memory in the device array and to release the interface pointers:


```C++
void CMainDlg::FreeDeviceArray()
{
    if(m_ppWMPDevices)
    {
        for(long i = 0; i < m_cDevices; i++)
        {
            m_ppWMPDevices[i]->Release();
        }
 
        delete[] m_ppWMPDevices;
        m_ppWMPDevices = NULL;        
    }
}
```



## Devices are Displayed in a List Box

The GetSelectedDeviceIndex function returns the index of the device the user selected in a list box by using the following code:


```C++
long CMainDlg::GetSelectedDeviceIndex()
{
    return (long)SendMessage(GetDlgItem(IDC_DEVICES), LB_GETCURSEL, 0, 0);
}
```



## User Interface State is Managed by a Single Function

The SetUIState function manages the user interface.


```C++
SetUIState(UIState 
NewState, BOOL 
bConnected)
```



The details of this function are not relevant to the discussions in this section, but be aware that this function performs tasks like enabling or disabling controls and changing display text in the user interface.

The UIState enumeration was defined as follows:


```C++
enum UIState
{
    Partnership,
    NoPartnership,
    Synchronizing
};
```



The *bConnected* parameter specifies whether to configure the user interface for a connected device (TRUE means the device is connected). The *NewState* and *bConnected* parameters convey the information needed for the function to do its work.

The following sections provide explanations of the example code:

-   [Enumerating Devices](enumerating-devices.md)
-   [Retrieving Device Attributes](retrieving-device-attributes.md)
-   [Showing Synchronization Progress](showing-synchronization-progress.md)
-   [Managing Synchronization Playlists](managing-synchronization-playlists.md)

## Related topics

<dl> <dt>

[**Player Control Guide**](player-control-guide.md)
</dt> </dl>

 

 





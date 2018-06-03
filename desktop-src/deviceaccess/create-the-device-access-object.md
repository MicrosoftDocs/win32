---
title: Implement the Device Access Object
description: This topic explains how to instantiate the device access object and use it to access a device.
ms.assetid: 26619A25-67FE-44DC-82DD-36076326748D
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Implement the Device Access Object

This topic explains how to instantiate the device access object and use it to access a device. The instantiated class implements the [**IDeviceIoControl**](/previous-versions/windows/desktop/api/Deviceaccess/nn-deviceaccess-ideviceiocontrol) and [**ICreateDeviceAccessAsync**](/previous-versions/windows/desktop/api/Deviceaccess/nn-deviceaccess-icreatedeviceaccessasync) interfaces.

## Instructions

### Step 1:

To instantiate the device access object, you must first call the [**CreateDeviceAccessInstance**](/previous-versions/windows/desktop/api/deviceaccess/nf-deviceaccess-createdeviceaccessinstance) function. If **CreateDeviceAccessInstance** succeeds, you can then call the [**Wait**](/previous-versions/windows/desktop/api/Deviceaccess/nf-deviceaccess-icreatedeviceaccessasync-wait) method to wait for the asynchronous operation to finish. If **Wait** succeeds, you can retrieve an [**IDeviceIoControl**](/previous-versions/windows/desktop/api/Deviceaccess/nn-deviceaccess-ideviceiocontrol) object (or the appropriate error) from the [**GetResult**](/previous-versions/windows/desktop/api/Deviceaccess/nf-deviceaccess-icreatedeviceaccessasync-getresult) method.


```C++
HRESULT
CMyServer::Initialize(
        PCWSTR   pszDeviceInterfacePath
    )

/*++
Routine Description:

    This routine is called to initialize the Device Access object.
    It's not part of the constructor as the initialization can fail.
    It opens the device and gets the IDeviceIoControl interface to the device instance
    via the broker.

Arguments:
    pszDeviceInterfacePath - the device interface string that needs to be opened

Return Value:

    HRESULT

--*/

{
    HRESULT hr;
    ICreateDeviceAccessAsync *pDeviceAccess;

     //
     // Here's the actual open call.  This will *fail* if your lowbox does
     // not have the capability mapped to the interface class specified.
     // If you are running this as normal user, it will just pass through to
     // create file.
     //

   hr = CreateDeviceAccessInstance(pszDeviceInterfacePath,
                                   GENERIC_READ|GENERIC_WRITE,
                                   &amp;pDeviceAccess);

    if (FAILED(hr)) {
        return hr;
    }

    if (SUCCEEDED(hr)) {
        hr = pDeviceAccess->Wait(INFINITE);
    }

    if (SUCCEEDED(hr)) {
        hr = pDeviceAccess->GetResult(IID_IDeviceIoControl,
                                            (void **)&amp;m_pDeviceIoControl);
    }

    pDeviceAccess->Release();

    return hr;
}
```



### Step 2:

This is an example of a call to the **DeviceIoControlSync** method.


```C++
IFACEMETHODIMP 
CMyServer::put_SevenSegmentDisplay(
    BYTE   value
    )
/*++

Routine Description:
    This routine puts the display value into the device.

Arguments:
    
    value - The value to be written to the device.
    
Return Value:

    HRESULT

--*/
{
    BYTE sevenSegment = 0;
    HRESULT hr;

    if (value >= ARRAYSIZE(g_NumberToMask)) {
        return E_INVALIDARG;
    }


    sevenSegment = g_NumberToMask[value];
    hr = m_pDeviceIoControl->DeviceIoControlSync(
                         IOCTL_OSRUSBFX2_SET_7_SEGMENT_DISPLAY,
                         &amp;sevenSegment,
                         sizeof(BYTE),
                         NULL,
                         0,
                         NULL
                         );

    return hr;
}
```



## Remarks

You can also send an IOCTL asynchronously by using the [**DeviceIoControlAsync**](/previous-versions/windows/desktop/api/Deviceaccess/nf-deviceaccess-ideviceiocontrol-deviceiocontrolasync) method. In that case, you must implement the [**IDeviceRequestCompletionCallback**](/previous-versions/windows/desktop/api/Deviceaccess/nn-deviceaccess-idevicerequestcompletioncallback) interface.

## Related topics

<dl> <dt>

**Samples**
</dt> <dt>

[Custom Driver Access Sample](http://go.microsoft.com/fwlink/p/?linkid=242014)
</dt> <dt>

**White papers**
</dt> <dt>

[Windows Store device app Design Guide for Specialized Devices](http://go.microsoft.com/fwlink/p/?linkid=242009)
</dt> <dt>

**Other resources**
</dt> <dt>

[Device Experience for Specialized Devices](http://go.microsoft.com/fwlink/p/?linkid=242009)
</dt> <dt>

[Device Experience for Windows 8](http://go.microsoft.com/fwlink/p/?linkid=241442)
</dt> </dl>

 

 





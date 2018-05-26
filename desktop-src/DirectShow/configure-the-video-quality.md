---
Description: This topic describes how an application can programmatically change the image and camera settings on a video capture device.
ms.assetid: f789db78-292e-4092-a5dc-1906845fb1dd
title: Configure the Video Quality
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Configure the Video Quality

This topic describes how an application can programmatically change the image and camera settings on a video capture device.

-   [ProcAmp Settings](#procamp-settings)
-   [Camera Settings](#camera-settings)
-   [Related topics](#related-topics)

## ProcAmp Settings

Windows Driver Model (WDM) video cameras can support properties that control the quality of the image:

-   Backlight compensation
-   Brightness
-   Contrast
-   Gain
-   Gamma
-   Hue
-   Saturation
-   Sharpness
-   White balance

These properties are controlled through the [**IAMVideoProcAmp**](/windows/win32/Strmif/nn-strmif-iamvideoprocamp?branch=master) interface. Use this interface as follows:

1.  Call [**QueryInterface**](https://msdn.microsoft.com/library/windows/desktop/ms682521) on the capture filter for the [**IAMVideoProcAmp**](/windows/win32/Strmif/nn-strmif-iamvideoprocamp?branch=master) interface.
2.  For each property that you want to set, call the [**IAMVideoProcAmp::GetRange**](/windows/win32/Strmif/nf-strmif-iamvideoprocamp-getrange?branch=master) method. Properties are specified by the [**VideoProcAmpProperty**](/windows/win32/strmif/ne-strmif-tagvideoprocampproperty?branch=master) enumeration. If the **GetRange** method fails, it means the camera does not support that particular property.
3.  If [**GetRange**](/windows/win32/Strmif/nf-strmif-iamvideoprocamp-getrange?branch=master) succeeds, it returns the range of supported values for the property, the default value, and the minimum increment.
4.  To get the current value of a property, call [**IAMVideoProcAmp::Get**](/windows/win32/Strmif/nf-strmif-iamvideoprocamp-get?branch=master).
5.  To set a property, call the [**IAMVideoProcAmp::Set**](/windows/win32/Strmif/nf-strmif-iamvideoprocamp-set?branch=master) method. To restore a property to its default value, call [**GetRange**](/windows/win32/Strmif/nf-strmif-iamvideoprocamp-getrange?branch=master) to find the default and pass that value to the **Set** method.

You do not have to stop the filter graph when you set the properties.

The following code configures a trackbar control so that it can be used to set the brightness. The range of the trackbar corresponds to the brightness range that the device supports, and position of the trackbar corresponds to the device's initial brightness setting.


```C++
HWND hTrackbar; // Handle to the trackbar control. 
// Initialize hTrackbar (not shown).

// Query the capture filter for the IAMVideoProcAmp interface.
IAMVideoProcAmp *pProcAmp = 0;
hr = pCap->QueryInterface(IID_IAMVideoProcAmp, (void**)&amp;pProcAmp);
if (FAILED(hr))
{
    // The device does not support IAMVideoProcAmp, so disable the control.
    EnableWindow(hTrackbar, FALSE);
}
else
{
    long Min, Max, Step, Default, Flags, Val;

    // Get the range and default value. 
    hr = m_pProcAmp->GetRange(VideoProcAmp_Brightness, &amp;Min, &amp;Max, &amp;Step,
        &amp;Default, &amp;Flags);
    if (SUCCEEDED(hr))
    {
        // Get the current value.
        hr = m_pProcAmp->Get(VideoProcAmp_Brightness, &amp;Val, &amp;Flags);
    }
    if (SUCCEEDED(hr))
    {
        // Set the trackbar range and position.
        SendMessage(hTrackbar, TBM_SETRANGE, TRUE, MAKELONG(Min, Max));
        SendMessage(hTrackbar, TBM_SETPOS, TRUE, Val);
        EnableWindow(hTrackbar, TRUE);
    }
    else
    {
        // This property is not supported, so disable the control.
        EnableWindow(hTrackbar, FALSE);
    }
}
```



## Camera Settings

The [**IAMCameraControl**](/windows/win32/Strmif/nn-strmif-iamcameracontrol?branch=master) interface is similar to [**IAMVideoProcAmp**](/windows/win32/Strmif/nn-strmif-iamvideoprocamp?branch=master), but controls various setttings on the camera itself:

-   Exposure
-   Focus
-   Iris
-   Pan
-   Roll
-   Tilt
-   Zoom

To use this interface, follow the same steps used for [**IAMVideoProcAmp**](/windows/win32/Strmif/nn-strmif-iamvideoprocamp?branch=master):

1.  Query the capture filter for the [**IAMCameraControl**](/windows/win32/Strmif/nn-strmif-iamcameracontrol?branch=master).
2.  Call [**IAMCameraControl::GetRange**](/windows/win32/Strmif/nf-strmif-iamcameracontrol-getrange?branch=master) to find which settings are supported, and the possible range for each settings.
3.  Call [**IAMCameraControl::Get**](/windows/win32/Strmif/nf-strmif-iamcameracontrol-get?branch=master) to get the current value of a setting.
4.  Call [**IAMCameraControl::Set**](/windows/win32/Strmif/nf-strmif-iamcameracontrol-set?branch=master) to set the value.

## Related topics

<dl> <dt>

[Configuring a Video Capture Device](configuring-a-video-capture-device.md)
</dt> </dl>

 

 




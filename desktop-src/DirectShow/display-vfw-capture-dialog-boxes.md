---
description: Display VFW Capture Dialog Boxes
ms.assetid: 708212ca-d148-4079-8052-3bf6696a33ab
title: Display VFW Capture Dialog Boxes
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Display VFW Capture Dialog Boxes

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A capture device that still uses a Video for Windows (VFW) driver can support any of the following three dialog boxes, which are used to configure the device.



| Dialog box    | Description                                                                                           |
|---------------|-------------------------------------------------------------------------------------------------------|
| Video Source  | Used to select the video input and to adjust device settings, such as picture brightness or contrast. |
| Video Format  | Used to select the image dimensions and bit depth.                                                    |
| Video Display | Used to control the appearance of the rendered video.                                                 |



 

To show one of these dialog boxes, do the following:

1.  Stop the filter graph.
2.  Query the capture filter for the [**IAMVfwCaptureDialogs**](/windows/desktop/api/Strmif/nn-strmif-iamvfwcapturedialogs) interface. If **QueryInterface** succeeds, it means the capture device is a VFW device.
3.  Call [**IAMVfwCaptureDialogs::HasDialog**](/windows/desktop/api/Strmif/nf-strmif-iamvfwcapturedialogs-hasdialog) to check if the driver supports the dialog box that you wish to display. The [**VfwCaptureDialogs**](/windows/desktop/api/strmif/ne-strmif-vfwcapturedialogs) enumeration defines flags for each of the VFW dialog boxes. **HasDialog** returns S\_OK if the dialog box is supported. It returns S\_FALSE otherwise, so check for the value S\_OK directly, rather than using the **SUCCEEDED** macro.
4.  If the dialog box is supported, call [**IAMVfwCaptureDialogs::ShowDialog**](/windows/desktop/api/Strmif/nf-strmif-iamvfwcapturedialogs-showdialog) to display the dialog box.
5.  Restart the graph.

The following code shows these steps for the Video Source dialog box:


```C++
pControl->Stop(); // Stop the graph.

// Query the capture filter for the IAMVfwCaptureDialogs interface.
IAMVfwCaptureDialogs *pVfw = 0;
hr = pCap->QueryInterface(IID_IAMVfwCaptureDialogs, (void**)&pVfw);
if (SUCCEEDED(hr))
{
    // Check if the device supports this dialog box.
    if (S_OK == pVfw->HasDialog(VfwCaptureDialog_Source))
    {
        // Show the dialog box.
        hr = pVfw->ShowDialog(VfwCaptureDialog_Source, hwndParent);
    }
}
pControl->Run();
```



## Related topics

<dl> <dt>

[Configuring a Video Capture Device](configuring-a-video-capture-device.md)
</dt> </dl>

 

 




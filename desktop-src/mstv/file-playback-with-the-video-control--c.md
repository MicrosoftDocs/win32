---
title: File Playback with the Video Control (C)
description: File Playback with the Video Control (C)
ms.assetid: 639931c1-c810-4750-a34f-2afd715af0f2
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# File Playback with the Video Control (C)

This topic applies to Windows XP or later.

To play a media file with the Video Control, pass the file name to the [**IMSVidCtl::View**](imsvidctl-view.md) method:


```C++
CComVariant var(OLESTR("C:\\Example.avi"));
hr = pVidControl->View(&amp;var);
```



If the method call succeeds, the active input device is the [MSVidFilePlaybackDevice](msvidfileplaybackdevice.md) object, which exposes the [**IMSVidFilePlayback**](/windows/desktop/api/segment/nn-segment-imsvidfileplayback) interface. (The **IMSVidFilePlayback** interface inherits [**IMSVidPlayback**](/windows/desktop/api/segment/nn-segment-imsvidplayback).) You can use this interface to seek in the file, change the playback rate, or step through the file.

The following code shows how to obtain the input device and query for the playback interface:


```C++
CComPtr<IMSVidInputDevice> pInputDevice;
HRESULT hr = pVidControl->get_InputActive(&amp;pInputDevice);
if (SUCCEEDED(hr))
{
    CComQIPtr<IMSVidFilePlayback> pFilePlayback(pInputDevice);
    if (pFilePlayback != NULL)
    {
         /* The file playback device is the active input. Call
            IMSVidFilePlayback methods to control the device. */
    }
}
```



To seek, call the **put\_CurrentPosition** method:


```C++
hr = pFilePlayback->put_CurrentPosition(200); // 2 msec
```



The default units are hundredths of seconds. You can change this to frames by calling the [**IMSVidPlayback::put\_PositionMode**](/windows/desktop/api/segment/nf-segment-imsvidplayback-put_positionmode) method.

To change the playback rate, call the **put\_Rate** method:


```C++
hr = pFilePlayback->put_Rate(2.0); // Twice normal speed.
```



To step forward frame-by-frame, first call **get\_CanStep** to determine whether the source file supports frame stepping. If so, call the **Step** method to step forward in the file:


```C++
VARIANT_BOOL fCan;
hr = pFilePlayback->get_CanStep(VARIANT_FALSE, &amp;fCan);
if (SUCCEEDED(hr)) &amp;&amp; (fCan == VARIANT_TRUE))
{
    hr = pFilePlayback->Step(2);  // Step two frames.
}
```



 

 





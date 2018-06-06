---
Description: Apps can't render in stereo unless the operating system indicates that it enables stereoscopic 3D display behavior. Apps determine whether to render in stereoscopic 3D differently depending on whether they are windowed or full screen.
ms.assetid: FB8AC57E-38DD-47B5-8666-1F4B73488F8B
title: Rendering in stereo and notifying about stereo status
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Rendering in stereo and notifying about stereo status

Apps can't render in stereo unless the operating system indicates that it enables stereoscopic 3D display behavior. Apps determine whether to render in stereoscopic 3D differently depending on whether they are windowed or full screen.

A windowed app calls the [**IDXGIFactory2::IsWindowedStereoEnabled**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgifactory2-iswindowedstereoenabled) method to determine whether to render in stereo. A full-screen app calls the [**IDXGIOutput1::GetDisplayModeList1**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgioutput1-getdisplaymodelist1) method and then determines whether any of the returned display modes support rendering in stereo. The **GetDisplayModeList1** method does not enumerate stereo modes unless you specify the [**DXGI\_ENUM\_MODES\_STEREO**](dxgi-enum-modes.md#dxgi-enum-modes-stereo) flag in the *Flags* parameter. A windowed or full-screen app that supports stereo first makes the determination to render in stereo based on a call to the **IDXGIFactory2::IsWindowedStereoEnabled** or **IDXGIOutput1::GetDisplayModeList1** method respectively, and then registers for notification of stereo status changes. Because the app can't rely on the notification to indicate the current status of the stereoscopic 3D display behavior, when it receives a notification event or window message, it must call either **IDXGIFactory2::IsWindowedStereoEnabled** or **IDXGIOutput1::GetDisplayModeList1** again to determine the current status of the operating system's stereoscopic 3D display behavior.

If you want to render in stereo, you must register for stereo notifications to know when the user turns off or on stereo behavior. An app can register to be notified about stereoscopic 3D status changes through a message to a window or through event signaling. To register to receive notification messages to a window about stereo status changes, an app calls the [**IDXGIFactory2::RegisterStereoStatusWindow**](https://msdn.microsoft.com/42DA05B8-1490-45B6-B22D-95176EBE7150) method. To register to receive notification of stereo status changes via event signaling, an app calls the [**IDXGIFactory2::RegisterStereoStatusEvent**](https://msdn.microsoft.com/912FC8B0-8B66-4203-BF27-8D7186F7CAC0) method. Both methods return a pointer to a key value that the app can use to unregister the notification. To unregister the notification, the app passes this key value to the [**IDXGIFactory2::UnregisterStereoStatus**](https://msdn.microsoft.com/8E3994C4-DA37-4D17-9F4D-C31E48CDE170) method.

Stereo status can contain the following elements:

-   The user configuration.

    Windows users can enable or disable stereo display with the enable stereoscopic 3D option in Control Panel's Change Display Settings.

-   The computer capability and configuration, which includes graphics adapter, graphics driver, and monitor setup.

The [Direct3D 11.1 Simple Stereo 3D Sample](http://go.microsoft.com/fwlink/p/?linkid=238402) shows how to add a stereoscopic 3D effect and how to respond to system stereo changes.

## Related topics

<dl> <dt>

[DXGI 1.2 Improvements](dxgi-1-2-improvements.md)
</dt> </dl>

 

 




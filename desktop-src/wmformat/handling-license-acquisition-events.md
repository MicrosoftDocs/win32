---
title: Handling License Acquisition Events
description: Handling License Acquisition Events
ms.assetid: e118bf09-1fa6-41b6-a6bb-3e8cb6097994
keywords:
- Windows Media Format SDK,handling license acquisition events
- Windows Media Format SDK,license acquisition events
- Advanced Systems Format (ASF),handling license acquisition events
- ASF (Advanced Systems Format),handling license acquisition events
- Advanced Systems Format (ASF),license acquisition events
- ASF (Advanced Systems Format),license acquisition events
- digital rights management (DRM),handling license acquisition events
- DRM (digital rights management),handling license acquisition events
- digital rights management (DRM),license acquisition events
- DRM (digital rights management),license acquisition events
ms.topic: article
ms.date: 05/31/2018
---

# Handling License Acquisition Events

A DRM-enabled reader application, in its [**IWMStatusCallback::OnStatus**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstatuscallback-onstatus) callback method, handles the following four events related to the license acquisition process:

-   **WMT\_LICENSEURL\_SIGNATURE\_STATE**
-   **WMT\_NO\_RIGHTS**
-   **WMT\_NO\_RIGHTS\_EX**
-   **WMT\_ACQUIRE\_LICENSE**

**WMT\_LICENSEURL\_SIGNATURE\_STATE**

When the DRM component detects content protected by DRM version 7, it first looks for a valid license on the local system. If none exists, it then evaluates the license acquisition URL in the file's DRM header and sends a **WMT\_LICENSEURL\_SIGNATURE\_STATE** event with *pValue* set to one of the [**WMT\_DRMLA\_TRUST**](/previous-versions/windows/desktop/api/wmsdkidl/ne-wmsdkidl-wmt_drmla_trust) values, indicating whether the URL is trusted, untrusted, or has been tampered with. If the URL is not trusted, then the application should warn the user. If the URL has been tampered with, then the file should be considered corrupted, and the application should not navigate to the URL without issuing a strong warning the user.

**WMT\_NO\_RIGHTS**

The **WMT\_NO\_RIGHTS** event is sent only for DRM version 1 content, which means that the license must be acquired non-silently. In other words, the user must navigate to a Web page to acquire a license. The URL for the page is retrieved as a wide-character null-terminated string from the *pValue* parameter in the **OnStatus** method.

If appropriate, an application can make it easier for the user to navigate to the Web page, either by opening up Internet Explorer in a separate process or else by hosting the Web Browser control. This is not required, however. At the very least, an application could simply display the URL to the user in a message box and prompt them to paste it into the address bar of Internet Explorer. The Audioplayer sample demonstrates proper handling of the **WMT\_NO\_RIGHTS** event, including how to format the URL string, and how to use the **CreateProcess** method to open Internet Explorer and navigate to the specified URL.

Because the application has no way of knowing when a DRM version 1 license has been acquired, it is up to the user to attempt to open the file again after acquiring the license.

This same non-silent license acquisition process can also be used for version 7 licenses, but in this case the application can first call [**IWMDRMReader::MonitorLicenseAcquisition**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-monitorlicenseacquisition). This method will cause the local license store to be checked repeatedly until the license for the new file is found. At that point, the application will receive a **WMT\_ACQUIRE\_LICENSE** event. For all version 7 licenses, it is recommended that applications give users the option to obtain licenses silently or non-silently.

**WMT\_NO\_RIGHTS\_EX**

The **WMT\_NO\_RIGHTS\_EX** event indicates that the content is protected by DRM version 7, and therefore the license acquisition process can proceed either silently or non-silently. In general, silent license acquisition is more convenient for end users, although some people prefer to acquire all licenses non-silently. When license acquisition requires the user to submit payment or personal information, the process should always be performed non-silently. Non-silent license acquisition is described above under the **WMT\_NO\_RIGHTS** heading. Silent acquisition proceeds as follows:

1.  Cast the *pValue* parameter to a [**WM\_GET\_LICENSE\_DATA**](wm-get-license-data.md) structure and store the structure in case it is needed later for non-silent license acquisition.
2.  Call **QueryInterface** on the reader object to obtain the [**IWMDRMReader**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmdrmreader) interface.
3.  Call [**IWMDRMReader::AcquireLicense**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-acquirelicense) and specify 0x1 in the *dwFlags* parameter to indicate silent language acquisition. This is an asynchronous call that returns immediately.
4.  Wait for the **WMT\_ACQUIRE\_LICENSE** event.

**WMT\_ACQUIRE\_LICENSE**

The **WMT\_ACQUIRE\_LICENSE** event is sent after the license acquisition process is completed for a DRM version 7 license. [**IWMDRMReader::AcquireLicense**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-acquirelicense) causes this event to be sent for silent acquisition, and [**MonitorLicenseAcquisition**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-monitorlicenseacquisition) causes it to be sent for non-silent acquisition. In your event handler, cast *pValue* to a pointer to a [**WM\_GET\_LICENSE\_DATA**](wm-get-license-data.md) structure and examine the **hr** member to determine whether the license was successfully acquired. If **hr** equals NS\_E\_DRM\_NO\_RIGHTS, it indicates that the license must be acquired non-silently. Applications should enable users to cancel the license acquisition process at any time. This is done by calling [**IWMDRMReader::CancelLicenseAcquisition**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-cancellicenseacquisition). Calling this method will send a **WMT\_ACQUIRE\_LICENSE** event with an **HRESULT** value of NS\_S\_DRM\_ACQUIRE\_CANCELLED.

If **hr** equals NS\_S\_DRM\_LICENSE\_ACQUIRED, then the license has been acquired and the application can attempt to play the file, or copy it to a device or perform whatever action it had requested rights for.

On Windows XP, a new error code was introduced: NS\_E\_DRM\_LICENSE\_NOTACQUIRED. This error code is generated whenever the Windows Media Format run-time components on Windows XP fail to acquire a license during silent or non-silent license acquisition. On other platforms, NS\_E\_DRM\_LICENSE\_STORE\_ERROR is usually returned when license acquisition fails. The new error code is intended to distinguish license acquisition failure from other failure conditions where NS\_E\_DRM\_LICENSE\_STORE\_ERROR is generated.

The recommended way to handle these errors when they are returned after a silent license acquisition attempt is shown in the following code snippet:


```C++
if( hrStatus == NS_E_DRM_LICENSE_NOTACQUIRED || 
    hrStatus == NS_E_DRM_LICENSE_STORE_ERROR )
{
  // Attempt non-silent license acquisition.
}
else if( hrStatus == NS_E_DRM_NEEDS_INDIVIDUALIZATION )
{
  // Individualize and then retry.
}
else if( FAILED(hrStatus) )
{
  // Display a helpful error message.
}
else
{
  // Success. Play content.
}
```



> [!Note]  
> DRM is not supported by the x64-based version of this SDK.

 

## Related topics

<dl> <dt>

[**Reading Protected Files**](reading-protected-files.md)
</dt> </dl>

 

 





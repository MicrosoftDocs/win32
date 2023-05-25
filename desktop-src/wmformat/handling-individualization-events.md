---
title: Handling Individualization Events
description: Handling Individualization Events
ms.assetid: f533978f-f366-4900-b784-f51e88393984
keywords:
- Windows Media Format SDK,handling individualization events
- Windows Media Format SDK,individualization events
- Advanced Systems Format (ASF),handling individualization events
- ASF (Advanced Systems Format),handling individualization events
- Advanced Systems Format (ASF),individualization events
- ASF (Advanced Systems Format),individualization events
- digital rights management (DRM),handling individualization events
- DRM (digital rights management),handling individualization events
- digital rights management (DRM),individualization events
- DRM (digital rights management),individualization events
- individualization events
- events,individualization events
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Handling Individualization Events

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When a DRM-enabled application attempts to open a protected file, the DRM component examines the [**DRM\_DRMHeader\_IndividualizedVersion**](drm-drmheader-individualizedversion.md) attribute in the file, which specifies the minimum version level required to access the content. All levels of the DRM component work with all 7.0 and later versions of Windows Media Player and the Windows Media Format SDK. If the DRM component's individualized version level is lower than the required version, the DRM component will send a **WMT\_NEEDS\_INDIVIDUALIZATION** event to the application's [**IWMStatusCallback::OnStatus**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstatuscallback-onstatus) method. The application must then display a message or dialog box prompting users to either start or cancel the security upgrade. This prompt is necessary because, for privacy reasons, users must give their permission before a security upgrade is installed on their computer.

> [!Note]  
> The header of the content specifies only the first two digits for DRM\_DRMVersion\_IndividualizedVersion. In other words, to require a level 2.2.0.1 DRM component, the header would contain "2.2".

 

To start the security upgrade and/or trigger individualization, call the [**IWMDRMReader::Individualize**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmdrmreader-individualize) method with the *dwFlags* parameter set to 1.

You must handle the **WMT\_INDIVIDUALIZE** event in your application. This event will be fired multiple times by the DRM component with the status of the individualization process indicated in the *pValue* parameter, which is cast to a pointer to a [**WM\_INDIVIDUALIZE\_STATUS**](wm-individualize-status.md) structure.

After the DRM component is successfully individualized, the application will receive a **WMT\_NO\_RIGHTS\_EX** event, indicating that the application can now proceed to acquire a license for the content.

> [!Note]  
> DRM is not supported by the x64-based version of this SDK.

 

## Related topics

<dl> <dt>

[**Handling License Acquisition Events**](handling-license-acquisition-events.md)
</dt> <dt>

[**Individualizing DRM Applications**](individualizing-drm-applications.md)
</dt> <dt>

[**IWMDRMReader Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmdrmreader)
</dt> </dl>

 

 





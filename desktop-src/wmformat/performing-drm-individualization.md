---
title: Performing DRM Individualization
description: Performing DRM Individualization
ms.assetid: daad1a31-f0a7-43ab-b920-94b9f050a44e
keywords:
- Windows Media Format SDK,DRM Client Extended APIs
- Windows Media Format SDK,Client Extended APIs
- Windows Media Format SDK,Extended APIs
- Windows Media Format SDK,APIs
- Windows Media Format SDK,digital rights management (DRM)
- Windows Media Format SDK,DRM individualization
- Windows Media Format SDK,individualization
- digital rights management (DRM),Client Extended APIs
- DRM (digital rights management),Client Extended APIs
- digital rights management (DRM),Extended APIs
- DRM (digital rights management),Extended APIs
- digital rights management (DRM),APIs
- DRM (digital rights management),APIs
- digital rights management (DRM),individualization
- DRM (digital rights management),individualization
- digital rights management (DRM),DRM individualization
- DRM (digital rights management),DRM individualization
- DRM Client Extended APIs,individualization
- Client Extended APIs,individualization
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Performing DRM Individualization

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Individualization is the process of updating the DRM component on the client computer, encrypting it, and making it unique. When a computer is individualized, the DRM component is tied to the computer and will not be able to decode content on any other computer. The Windows Media DRM Client Extended APIs provide support for individualizing the DRM component on client computers.

Individualization is performed by calling the [**IWMDRMSecurity::PerformSecurityUpdate**](iwmdrmsecurity-performsecurityupdate.md) method. You can call **PerformSecurityUpdate** so that it will individualize only if the version on the server is newer than the one installed on the client computer, or you can force individualization without regard to the relative security versions. The flag for as-needed individualization is WMDRM\_SECURITY\_PERFORM\_INDIV. The flag for forced individualization is WMDRM\_SECURITY\_PERFORM\_FORCE\_INDIV.

**PerformSecurityUpdate** is an asynchronous call. It will return quickly and then generate events to provide status information about the individualization process. The majority of the events generated will be **MEWMDRMIndividualizationProgress** events, and each has an associated [**IWMDRMIndividualizationStatus**](iwmdrmindividualizationstatus.md) interface. To get the status interface, you must call **IMFMediaEvent::GetValue** to retrieve an **IUnknown** pointer that is on the same object and then query it for **IWMDRMIndividualizationStatus**.

You can get data for a [**WM\_INDIVIDUALIZE\_STATUS**](drmwm-individualize-status.md) structure by calling [**IWMDRMIndividualizeStatus::GetStatus**](iwmdrmindividualizationstatus-getstatus.md). Each event that is generated has its own object with status, so you must go through the process of getting the event value and querying for the status interface every time.

Depending on the size of the download, there may be dozens or hundreds of **MEWMDRMIndividualizationProgress** events. When the individualization process is finished, an **MEWMDRMIndividualizationCompleted** event is generated.

When individualization is completed, the only existing objects that will reflect the new individualized state are those that inherit from [**IWMDRMSecurity**](iwmdrmsecurity.md). All other existing objects will not be updated. You must release and re-create any other objects so that they will reflect the new individualized state.

## Related topics

<dl> <dt>

[**DRM Individualization Example**](drm-individualization-example.md)
</dt> <dt>

[**Programming Guide**](drm-programming-guide.md)
</dt> <dt>

[**Using the Media Foundation Event Model**](using-the-media-foundation-model.md)
</dt> <dt>

[Windows Media DRM Individualization Best Practices](/previous-versions/ms867216(v=msdn.10))
</dt> </dl>

 

 





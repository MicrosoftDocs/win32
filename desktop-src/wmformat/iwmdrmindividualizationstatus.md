---
title: IWMDRMIndividualizationStatus interface
description: The IWMDRMIndividualizationStatus interface enables retrieval of advanced status information about the progress of individualization.This interface is delivered with MEWMDRMIndividualizationProgress events.
ms.assetid: 3a148005-22fa-4495-a47c-d9463db16293
keywords:
- IWMDRMIndividualizationStatus interface windows Media Format
- IWMDRMIndividualizationStatus interface windows Media Format , described
topic_type:
- apiref
api_name:
- IWMDRMIndividualizationStatus
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# IWMDRMIndividualizationStatus interface

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **IWMDRMIndividualizationStatus** interface enables retrieval of advanced status information about the progress of individualization.

This interface is delivered with MEWMDRMIndividualizationProgress events. Many such events are generated between a call to [**IWMDRMSecurity::PerformSecurityUpdate**](iwmdrmsecurity-performsecurityupdate.md) and the completion of the individualization process, which is signaled by the generation of an **MEWMDRMIndividualizationCompleted** event.

To retrieve a pointer to an instance of the **IWMDRMIndividualizationStatus** interface, you must first call the **IMFMediaEvent::GetValue** method of the progress event. The value you retrieve from the event is a pointer to the **IUnknown** interface of the object that implements the **IWMDRMIndividualizationStatus** interface.

## Members

The **IWMDRMIndividualizationStatus** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IWMDRMIndividualizationStatus** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWMDRMIndividualizationStatus** interface has these methods.



| Method                                                       | Description                                                        |
|:-------------------------------------------------------------|:-------------------------------------------------------------------|
| [**GetStatus**](iwmdrmindividualizationstatus-getstatus.md) | Retrieves detailed information about individualization.<br/> |



 

## See also

<dl> <dt>

[**Interfaces**](drm-interfaces.md)
</dt> </dl>

 


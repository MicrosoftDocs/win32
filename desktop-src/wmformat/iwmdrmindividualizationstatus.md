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
ms.date: 05/31/2018
api_location: 
---

# IWMDRMIndividualizationStatus interface

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

 


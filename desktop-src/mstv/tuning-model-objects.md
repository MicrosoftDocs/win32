---
title: Tuning Model Objects
description: Tuning Model Objects
ms.assetid: cf6a81cd-a955-4816-a43e-85138ecd8246
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Tuning Model Objects

## Tuning Space Objects

A tuning space represents a particular type of network, along with other information that identifies a particular network provider or broadcast source. Microsoft provides five default tuning spaces; third parties may add their own tuning space. Tuning spaces are stored in the system registry. Use the [SystemTuningSpaces](systemtuningspaces-object.md) object to create new tuning spaces or access existing ones.



| Object                                                      | Description                                                              |
|-------------------------------------------------------------|--------------------------------------------------------------------------|
| [AnalogRadioTuningSpace](analogradiotuningspace-object.md) | Represents a tuning space for analog radio networks.                     |
| [AnalogTVTuningSpace](analogtvtuningspace-object.md)       | Represents a tuning space for analog TV networks.                        |
| [ATSCTuningSpace](atsctuningspace-object.md)               | Represents a tuning space for ATSC networks.                             |
| [AuxInTuningSpace](auxintuningspace-object.md)             | Represents a video auxiliary input, such as S-Video or composite video.  |
| [DVBSTuningSpace](dvbstuningspace-object.md)               | Represents a tuning space for DVB-S networks.                            |
| [DVBTuningSpace](dvbtuningspace-object.md)                 | Represents a tuning space for DVB networks.                              |
| [SystemTuningSpaces](systemtuningspaces-object.md)         | Represents the collection of tuning spaces installed on the host system. |



 

## Stream Component Objects

In digital television, a *component* refers to an elementary stream within an MPEG-2 program stream. For example, a program stream may have three audio components, one in English, one in Spanish, and one in French. In some cases, the components that a service provides must be discovered after reception begins. The Transport Information Filter (TIF) works with the Network Provider to fill in the component data in the tune request after tuning has occurred. The application can then examine the tune request, for example to inform the user of additional audio streams that are available.



| Object                                                    | Description                                                             |
|-----------------------------------------------------------|-------------------------------------------------------------------------|
| [ATSCComponentType](atsccomponenttype-object.md)         | Represents an ATSC component type.                                      |
| [Component](component-object.md)                         | Represents a generic program component.                                 |
| [Components](components-object.md)                       | Represents a collection of components.                                  |
| [ComponentType](componenttype-object.md)                 | Represents a generic component type.                                    |
| [ComponentTypes](componenttypes-object.md)               | Represents a collection of component types.                             |
| [LanguageComponentType](languagecomponenttype-object.md) | Represents a component type that has a defined language code.           |
| [MPEG2Component](mpeg2component-object.md)               | Represents an MPEG-2 stream component.                                  |
| [MPEG2ComponentType](mpeg2componenttype-object.md)       | Represents a component type associated with an MPEG-2 stream component. |



 

## Locator Objects

Locator objects contain low-level information that a tuner and Network Provider use to locate a program within a tuning space. This information includes the frequency and modulation type of the television signal, Quadrature Phase Shift Keying (QPSK) symbol rate, the type of forward error correction used, and other parameters specific to the network type. Each tune request contains a locator object, although it is not always necessary that all properties of the locator be set. A third party such as a cable or satellite provider may provide a default locator for their tuning space, which a Guide Store loader can use when creating tune requests. Locators are typically not used by applications, except perhaps for debugging purposes, or in the case where an application creates its own tune request.



| Object                                | Description                                                                                    |
|---------------------------------------|------------------------------------------------------------------------------------------------|
| [ATSCLocator](atsclocator-object.md) | Contains tuning information specific to ATSC networks.                                         |
| [DVBCLocator](dvbclocator-object.md) | Contains tuning information specific to DVB-C networks.                                        |
| [DVBSLocator](dvbslocator-object.md) | Contains tuning information specific to DVB-S networks.                                        |
| [DVBTLocator](dvbtlocator-object.md) | Contains tuning information specific to DVB-T networks.                                        |
| [Locator](locator-object.md)         | Base class for the other locators. Contains tuning information required for all network types. |



 

## Tune Request Objects

Tune request objects contains the information needed to tune to a channel within a particular network type. To create a tune request, call [**ITuningSpace::CreateTuneRequest**](/previous-versions/windows/desktop/api/tuner/nf-tuner-ituningspace-createtunerequest) on the tuning space for that network type.



| Object                                                        | Description                                |
|---------------------------------------------------------------|--------------------------------------------|
| [ATSCChannelTuneRequest](atscchanneltunerequest-object.md)   | Tune request for ATSC networks.            |
| [DigitalCableTuneRequest](digitalcabletunerequest-object.md) | Tune request for digital cable.            |
| [DVBTuneRequest](dvbtunerequest-object.md)                   | Tune request for DVB networks.             |
| [MPEG2TuneRequest](mpeg2tunerequest-object.md)               | Tune request for MPEG-2 transport streams. |



 

## Related topics

<dl> <dt>

[Unified Tuning Model Reference](unified-tuning-model-reference.md)
</dt> </dl>

 

 





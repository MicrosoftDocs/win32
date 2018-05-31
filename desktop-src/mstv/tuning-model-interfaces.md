---
title: Tuning Model Interfaces
description: Tuning Model Interfaces
ms.assetid: 5d956e1d-88b3-4236-9987-f37f674645de
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Tuning Model Interfaces

These interfaces are used primarily by guide store loaders, to create tune requests for an EPG database (guide store), and by applications that install custom tuning spaces on a system. Applications can also use these interfaces to:

-   Create or modify a tune request dynamically.
-   Test the validity of a tuning space.
-   Create a default preferred components list that indicates user preferences for options such as the audio stream language.
-   Examine the components (such as audio substreams) available on a specified service.

For more information, see [The Microsoft Unified Tuning Model](the-microsoft-unified-tuning-model.md).

### Tuning Space Interfaces

These interfaces manage tuning space objects. You will never use the base class [**ITuningSpace**](/previous-versions/windows/desktop/api/tuner/nn-tuner-ituningspace) interface directly; you will always use a derived interface that is specific to a particular network type.



| Interface                                                    | Description                                                                                                   |
|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [**IAnalogRadioTuningSpace**](/previous-versions/windows/desktop/api/tuner/nn-tuner-ianalogradiotuningspace)   | Represents a tuning space for analog radio networks. (Not implemented in this release.)                       |
| [**IAnalogRadioTuningSpace2**](/previous-versions/windows/desktop/api/tuner/nn-tuner-ianalogradiotuningspace2) | Represents a tuning space for analog radio networks and exposes a dialing prefix property.                    |
| [**IAnalogTVTuningSpace**](/previous-versions/windows/desktop/api/tuner/nn-tuner-ianalogtvtuningspace)         | Represents a tuning space for analog TV networks.                                                             |
| [**IATSCTuningSpace**](/previous-versions/windows/desktop/api/tuner/nn-tuner-iatsctuningspace)                 | Represents a tuning space for ATSC networks.                                                                  |
| [**IAuxInTuningSpace**](/previous-versions/windows/desktop/api/tuner/)               | Represents a tuning space for S-video or composite video inputs.                                              |
| [**IAuxInTuningSpace2**](/previous-versions/windows/desktop/api/tuner/nn-tuner-iauxintuningspace2)             | Represents a tuning space for S-video or composite video inputs and exposes a dialing prefix property.        |
| [**IDigitalCableTuningSpace**](/previous-versions/windows/desktop/api/tuner/nn-tuner-idigitalcabletuningspace) | Provides methods for working with tuning spaces with an ATSC network type.                                    |
| [**IDVBSTuningSpace**](/previous-versions/windows/desktop/api/tuner/nn-tuner-idvbstuningspace)                 | Represents a tuning space for satellite DVB (DVB-S) networks.                                                 |
| [**IDVBTuningSpace**](/previous-versions/windows/desktop/api/tuner/nn-tuner-idvbtuningspace)                   | Represents a tuning space for DVB networks.                                                                   |
| [**IDVBTuningSpace2**](/previous-versions/windows/desktop/api/tuner/nn-tuner-idvbtuningspace2)                 | Represents a tuning space for DVB networks; extends the [**IDVBTuningSpace**](/previous-versions/windows/desktop/api/tuner/nn-tuner-idvbtuningspace) interface. |
| [**IEnumTuningSpaces**](/previous-versions/windows/desktop/api/tuner/nn-tuner-ienumtuningspaces)               | Standard COM enumeration interface for tuning spaces.                                                         |
| [**ITuningSpace**](/previous-versions/windows/desktop/api/tuner/nn-tuner-ituningspace)                         | Base interface for all tuning spaces.                                                                         |
| [**ITuningSpaceContainer**](/previous-versions/windows/desktop/api/tuner/nn-tuner-ituningspacecontainer)       | Provides access to all of the tuning spaces installed on the host system.                                     |
| [**ITuningSpaces**](/previous-versions/windows/desktop/api/tuner/nn-tuner-ituningspaces)                       | Represents a collection of tuning spaces.                                                                     |



 

### Tune Request Interfaces

Tune requests are not created directly. They are obtained through a call to [**CreateTuneRequest**](/previous-versions/windows/desktop/api/tuner/nf-tuner-ituningspace-createtunerequest) on a network-specific tuning space interface, such as [**IDVBTuningSpace**](/previous-versions/windows/desktop/api/tuner/nn-tuner-idvbtuningspace).



| Interface                                                    | Description                                                                                  |
|--------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| [**IATSCChannelTuneRequest**](/previous-versions/windows/desktop/api/tuner/nn-tuner-iatscchanneltunerequest)   | Provides tuning information specific to ATSC TV networks.                                    |
| [**IChannelTuneRequest**](/previous-versions/windows/desktop/api/tuner/nn-tuner-ichanneltunerequest)           | Provides tuning information specific to analog TV networks.                                  |
| [**IDigitalCableTuneRequest**](/previous-versions/windows/desktop/api/tuner/nn-tuner-idigitalcabletunerequest) | Provides methods for getting and setting the minor channel for a digital cable transmission. |
| [**IDVBTuneRequest**](/previous-versions/windows/desktop/api/tuner/nn-tuner-idvbtunerequest)                   | Provides tuning information specific to DVB TV networks.                                     |
| [**IEnumTuningSpaces**](/previous-versions/windows/desktop/api/tuner/nn-tuner-ienumtuningspaces)               | Implemented on a standard COM collection of tuning space objects.                            |
| [**IMPEG2TuneRequest**](/previous-versions/windows/desktop/api/tuner/nn-tuner-impeg2tunerequest)               | Represents a minimal MPEG-2 tune request.                                                    |
| [**IMPEG2TuneRequestFactory**](/previous-versions/windows/desktop/api/tuner/nn-tuner-impeg2tunerequestfactory) | Creates a tune request for a basic MPEG-2 transport stream containing the minimal tables.    |
| [**ITuneRequest**](/previous-versions/windows/desktop/api/tuner/nn-tuner-itunerequest)                         | Provides tuning information relevant for all network types.                                  |



 

### Stream Component Interfaces

A *component* refers to a substream within a broadcast. Applications create a default preferred components collection based on user input, in order to specify, for example, a preferred audio stream language. When an audio stream is specified in this way, the Network Provider will always attempt to use it for all tune request in the tuning space (See [**ITuningSpace::put\_DefaultPreferredComponentTypes**](/previous-versions/windows/desktop/api/tuner/nf-tuner-ituningspace-put_defaultpreferredcomponenttypes).) In some cases the actual components of a broadcast stream can only be discovered after reception begins, or the actual components may differ from what was advertised in the EPG information. At that time the [BDA Network Provider](bda-network-provider-filter.md) will fill in the component information in the tune request, and the application can then retrieve it and use it, for example, to change the audio stream or determine which audio streams are currently available.



| Interface                                                      | Description                                                                                                                             |
|----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| [**IAnalogAudioComponentType**](/previous-versions/windows/desktop/api/tuner/nn-tuner-ianalogaudiocomponenttype) | Provides methods for accessing the analog audio mode.                                                                                   |
| [**IATSCComponentType**](/previous-versions/windows/desktop/api/tuner/nn-tuner-iatsccomponenttype)               | Provides a method that indicates whether the audio substream is in AC-3 format.                                                         |
| [**IComponent**](/previous-versions/windows/desktop/api/tuner/nn-tuner-icomponent)                               | Base class for all derived component interfaces.                                                                                        |
| [**IComponents**](/previous-versions/windows/desktop/api/tuner/nn-tuner-icomponents)                             | Provides a standard COM enumeration of components.                                                                                      |
| [**IComponentType**](/previous-versions/windows/desktop/api/tuner/nn-tuner-icomponenttype)                       | Base class for all derived component type interfaces.                                                                                   |
| [**IComponentTypes**](/previous-versions/windows/desktop/api/tuner/nn-tuner-icomponenttypes)                     | Provides a standard COM enumeration of component types.                                                                                 |
| [**IEnumComponents**](/previous-versions/windows/desktop/api/tuner/nn-tuner-ienumcomponents)                     | Implemented on a standard COM collection object containing all the active or inactive components on the current broadcast stream.       |
| [**IEnumComponentTypes**](/previous-versions/windows/desktop/api/tuner/nn-tuner-ienumcomponenttypes)             | Implemented on a standard COM collection of [ComponentType](componenttype-object.md) objects associated with a given broadcast stream. |
| [**ILanguageComponentType**](/previous-versions/windows/desktop/api/tuner/nn-tuner-ilanguagecomponenttype)       | Provides methods that describe the language of the substream.                                                                           |
| [**IMPEG2Component**](/previous-versions/windows/desktop/api/tuner/nn-tuner-impeg2component)                     | Contains methods for getting and setting properties that describe an MPEG2 elementary stream.                                           |
| [**IMPEG2ComponentType**](/previous-versions/windows/desktop/api/tuner/nn-tuner-impeg2componenttype)             | Provides methods that describe a component type associated with an MPEG-2 stream type.                                                  |



 

### Locator Interfaces

Locators are used by the Network Provider and other filters in the graph to determine how to locate a specified program. These interfaces are not used by applications except possibly for debugging purposes. Third parties that install new tuning spaces should also provide a default locator for the tuning space. An individual tune request contains a locator, which can be different from the default locator. If present, the locator in the tune request takes precedence over the default locator



| Interface                                            | Description                                                                                                                      |
|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [**IAnalogLocator**](/previous-versions/windows/desktop/api/tuner/nn-tuner-ianaloglocator)             | Provides tuning information for an analog television network.                                                                    |
| [**IATSCLocator**](/previous-versions/windows/desktop/api/tuner/nn-tuner-iatsclocator)                 | Provides tuning information for an ATSC network.                                                                                 |
| [**IATSCLocator2**](/previous-versions/windows/desktop/api/tuner/nn-tuner-iatsclocator2)               | Enables the network provider to determine the physical channel, transport stream ID, and program number of an ATSC transmission. |
| [**IDigitalCableLocator**](/previous-versions/windows/desktop/api/tuner/) | Provides tuning information for a digital cable network.                                                                         |
| [**IDigitalLocator**](/previous-versions/windows/desktop/api/tuner/)           | Base interface for all derived locator interfaces for digital networks. Not used directly.                                       |
| [**IDVBCLocator**](/previous-versions/windows/desktop/api/tuner/)                 | Provides tuning information for a DVB-C network.                                                                                 |
| [**IDVBSLocator**](/previous-versions/windows/desktop/api/tuner/nn-tuner-idvbslocator)                 | Provides tuning information for a DVB-S network.                                                                                 |
| [**IDVBSLocator2**](/previous-versions/windows/desktop/api/tuner/nn-tuner-idvbslocator2)               | Extends the [**IDVBSLocator**](/previous-versions/windows/desktop/api/tuner/nn-tuner-idvbslocator) interface.                                                                      |
| [**IDVBTLocator**](/previous-versions/windows/desktop/api/tuner/nn-tuner-idvbtlocator)                 | Provides tuning information for a DVB-T network.                                                                                 |
| [**IDVBTLocator2**](/previous-versions/windows/desktop/api/tuner/nn-tuner-idvbtlocator2)               | Gets or sets tuning information for a Digital Video Broadcast - Second Generation Terrestrial (DVB-T2) network.                  |
| [**ILocator**](/previous-versions/windows/desktop/api/tuner/nn-tuner-ilocator)                         | Base interface for all derived locator interfaces. Not used directly.                                                            |



 

### Event Service Tuning Model Interfaces

Starting in Windows 7, a new event service model is available for media graphs. Using this model, a device can register with the event service to receive only specific events. This model was originally developed to support the Protected Broadcast Driver Architecture, though PBDA is not a requirement for using these interfaces. The following interfaces define events that use this new model and allow developers to develop custom events and event services that fit this model:



| Interface                                                            | Description                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IESCloseMmiEvent**](/previous-versions/windows/desktop/api/tuner/nn-tuner-iesclosemmievent)                         | Receives **CloseMMI** events from a Media Sink Device (MSD) device under the Protected Broadcast Driver Architecture (PBDA) (Windows 7 and later).                                                                                                     |
| [**IESEvent**](/previous-versions/windows/desktop/api/tuner/nn-tuner-iesevent)                                         | Implements a generic event interface that can deliver and encapsulate events that are raised by devices that work with PBDA (Windows 7 and later).                                                                                                     |
| [**IESEvents**](/previous-versions/windows/desktop/api/tuner/nn-tuner-iesevents)                                       | Implements event handling for devices that have registered to receive specific events derived from the [**IESEvent**](/previous-versions/windows/desktop/api/tuner/nn-tuner-iesevent) interface (Windows 7 and later).                                                                                   |
| [**IESEventService**](/previous-versions/windows/desktop/api/tuner/nn-tuner-ieseventservice)                           | Implements an event service that includes methods that raise events derived from the [**IESEvent**](/previous-versions/windows/desktop/api/tuner/nn-tuner-iesevent) interface (Windows 7 and later).                                                                                                     |
| [**IESEventServiceConfiguration**](/previous-versions/windows/desktop/api/tuner/nn-tuner-ieseventserviceconfiguration) | Configures an event service that implements the [**IESEventService**](/previous-versions/windows/desktop/api/tuner/nn-tuner-ieseventservice) interface (Windows 7 and later).                                                                                                                            |
| [**IESFileExpiryDateEvent**](/previous-versions/windows/desktop/api/tuner/nn-tuner-iesfileexpirydateevent)             | Gets information from a **FileExpiryDate** event, which a PBDA media transform device (MTD) fires when it receives a new license for protected content that contains a new expiry date for that content (Windows 7 and later).                         |
| [**IESIsdbCasResponseEvent**](/previous-versions/windows/desktop/api/tuner/nn-tuner-iesisdbcasresponseevent)           | Gets information from a PBDA **IsdbCasResponse** event, which an Integrated Services Digital Broadcasting (ISDB) PBDA MTD raises to signal that response data is available to an MSD that has requested conditional access data (Windows 7 and later). |
| [**IESLicenseRenewalResultEvent**](/previous-versions/windows/desktop/api/tuner/nn-tuner-ieslicenserenewalresultevent) | Gets information from a **LicenseRenewalResult** event, which contains the result of an attempt to renew a license for protected content (Windows 7 and later).                                                                                        |
| [**IESOpenMmiEvent**](/previous-versions/windows/desktop/api/tuner/nn-tuner-iesopenmmievent)                           | Gets information from an **OpenMMI** event, which a PBDA MTD raises when a user tries to open an on-screen display, such as a dialog box (Windows 7 and later).                                                                                        |
| [**IESRequestTunerEvent**](/previous-versions/windows/desktop/api/tuner/nn-tuner-iesrequesttunerevent)                 | Enable a PBDA-supported device to get exclusive access to a tuner and its Conditional Access Services (CAS) (Windows 7 and later).                                                                                                                     |
| [**IESValueUpdatedEvent**](/previous-versions/windows/desktop/api/tuner/nn-tuner-iesvalueupdatedevent)                 | Inform a PBDA MSD that an MTD has updated the value for a name-value pair or exposed a new name-value pair (Windows 7 and later).                                                                                                                      |



 

### Miscellaneous Tuning Model Interfaces



| Interface                                                    | Description                                                                                                                           |
|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [**IBDACreateTuneRequestEx**](/previous-versions/windows/desktop/api/tuner/nn-tuner-ibdacreatetunerequestex)   | Creates a new tuning request for a tuning space.                                                                                      |
| [**IChannelIDTuneRequest**](/previous-versions/windows/desktop/api/tuner/nn-tuner-ichannelidtunerequest)       | Implements methods that support channel requests using a string identifier.                                                           |
| [**ICreatePropBagOnRegKey**](/previous-versions/windows/desktop/api/regbag/nn-regbag-icreatepropbagonregkey)     | Creates a property bag that can store information in the system registry.                                                             |
| [**IMPEG2TuneRequestSupport**](/previous-versions/windows/desktop/api/tuner/) | Indicates that the default network provider for a tuning space supports the [**IMPEG2TuneRequest**](/previous-versions/windows/desktop/api/tuner/nn-tuner-impeg2tunerequest) interface. |
| [**IPersistTuneXml**](/previous-versions/windows/desktop/api/tuner/nn-tuner-ipersisttunexml)                   | Serializes a tuning model object.                                                                                                     |
| [**IPersistTuneXmlUtility**](/previous-versions/windows/desktop/api/tuner/nn-tuner-ipersisttunexmlutility)     | Defines utility methods for deserializing XML tuning requests.                                                                        |
| [**IPersistTuneXmlUtility2**](/previous-versions/windows/desktop/api/tuner/nn-tuner-ipersisttunexmlutility2)   | Extends the [**IPersistTuneXmlUtility**](/previous-versions/windows/desktop/api/tuner/nn-tuner-ipersisttunexmlutility) interface.                                                       |



 

## Related topics

<dl> <dt>

[Unified Tuning Model Reference](unified-tuning-model-reference.md)
</dt> </dl>

 

 





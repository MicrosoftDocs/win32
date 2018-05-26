---
title: Tuning Model Interfaces
description: Tuning Model Interfaces
ms.assetid: 5d956e1d-88b3-4236-9987-f37f674645de
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Tuning Model Interfaces

These interfaces are used primarily by guide store loaders, to create tune requests for an EPG database (guide store), and by applications that install custom tuning spaces on a system. Applications can also use these interfaces to:

-   Create or modify a tune request dynamically.
-   Test the validity of a tuning space.
-   Create a default preferred components list that indicates user preferences for options such as the audio stream language.
-   Examine the components (such as audio substreams) available on a specified service.

For more information, see [The Microsoft Unified Tuning Model](the-microsoft-unified-tuning-model.md).

### Tuning Space Interfaces

These interfaces manage tuning space objects. You will never use the base class [**ITuningSpace**](/windows/previous-versions/tuner/nn-tuner-ituningspace?branch=master) interface directly; you will always use a derived interface that is specific to a particular network type.



| Interface                                                    | Description                                                                                                   |
|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [**IAnalogRadioTuningSpace**](/windows/previous-versions/tuner/nn-tuner-ianalogradiotuningspace?branch=master)   | Represents a tuning space for analog radio networks. (Not implemented in this release.)                       |
| [**IAnalogRadioTuningSpace2**](/windows/previous-versions/tuner/nn-tuner-ianalogradiotuningspace2?branch=master) | Represents a tuning space for analog radio networks and exposes a dialing prefix property.                    |
| [**IAnalogTVTuningSpace**](/windows/previous-versions/tuner/nn-tuner-ianalogtvtuningspace?branch=master)         | Represents a tuning space for analog TV networks.                                                             |
| [**IATSCTuningSpace**](/windows/previous-versions/tuner/nn-tuner-iatsctuningspace?branch=master)                 | Represents a tuning space for ATSC networks.                                                                  |
| [**IAuxInTuningSpace**](/windows/previous-versions/tuner/?branch=master)               | Represents a tuning space for S-video or composite video inputs.                                              |
| [**IAuxInTuningSpace2**](/windows/previous-versions/tuner/nn-tuner-iauxintuningspace2?branch=master)             | Represents a tuning space for S-video or composite video inputs and exposes a dialing prefix property.        |
| [**IDigitalCableTuningSpace**](/windows/previous-versions/tuner/nn-tuner-idigitalcabletuningspace?branch=master) | Provides methods for working with tuning spaces with an ATSC network type.                                    |
| [**IDVBSTuningSpace**](/windows/previous-versions/tuner/nn-tuner-idvbstuningspace?branch=master)                 | Represents a tuning space for satellite DVB (DVB-S) networks.                                                 |
| [**IDVBTuningSpace**](/windows/previous-versions/tuner/nn-tuner-idvbtuningspace?branch=master)                   | Represents a tuning space for DVB networks.                                                                   |
| [**IDVBTuningSpace2**](/windows/previous-versions/tuner/nn-tuner-idvbtuningspace2?branch=master)                 | Represents a tuning space for DVB networks; extends the [**IDVBTuningSpace**](/windows/previous-versions/tuner/nn-tuner-idvbtuningspace?branch=master) interface. |
| [**IEnumTuningSpaces**](/windows/previous-versions/tuner/nn-tuner-ienumtuningspaces?branch=master)               | Standard COM enumeration interface for tuning spaces.                                                         |
| [**ITuningSpace**](/windows/previous-versions/tuner/nn-tuner-ituningspace?branch=master)                         | Base interface for all tuning spaces.                                                                         |
| [**ITuningSpaceContainer**](/windows/previous-versions/tuner/nn-tuner-ituningspacecontainer?branch=master)       | Provides access to all of the tuning spaces installed on the host system.                                     |
| [**ITuningSpaces**](/windows/previous-versions/tuner/nn-tuner-ituningspaces?branch=master)                       | Represents a collection of tuning spaces.                                                                     |



 

### Tune Request Interfaces

Tune requests are not created directly. They are obtained through a call to [**CreateTuneRequest**](/windows/previous-versions/tuner/nf-tuner-ituningspace-createtunerequest?branch=master) on a network-specific tuning space interface, such as [**IDVBTuningSpace**](/windows/previous-versions/tuner/nn-tuner-idvbtuningspace?branch=master).



| Interface                                                    | Description                                                                                  |
|--------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| [**IATSCChannelTuneRequest**](/windows/previous-versions/tuner/nn-tuner-iatscchanneltunerequest?branch=master)   | Provides tuning information specific to ATSC TV networks.                                    |
| [**IChannelTuneRequest**](/windows/previous-versions/tuner/nn-tuner-ichanneltunerequest?branch=master)           | Provides tuning information specific to analog TV networks.                                  |
| [**IDigitalCableTuneRequest**](/windows/previous-versions/tuner/nn-tuner-idigitalcabletunerequest?branch=master) | Provides methods for getting and setting the minor channel for a digital cable transmission. |
| [**IDVBTuneRequest**](/windows/previous-versions/tuner/nn-tuner-idvbtunerequest?branch=master)                   | Provides tuning information specific to DVB TV networks.                                     |
| [**IEnumTuningSpaces**](/windows/previous-versions/tuner/nn-tuner-ienumtuningspaces?branch=master)               | Implemented on a standard COM collection of tuning space objects.                            |
| [**IMPEG2TuneRequest**](/windows/previous-versions/tuner/nn-tuner-impeg2tunerequest?branch=master)               | Represents a minimal MPEG-2 tune request.                                                    |
| [**IMPEG2TuneRequestFactory**](/windows/previous-versions/tuner/nn-tuner-impeg2tunerequestfactory?branch=master) | Creates a tune request for a basic MPEG-2 transport stream containing the minimal tables.    |
| [**ITuneRequest**](/windows/previous-versions/tuner/nn-tuner-itunerequest?branch=master)                         | Provides tuning information relevant for all network types.                                  |



 

### Stream Component Interfaces

A *component* refers to a substream within a broadcast. Applications create a default preferred components collection based on user input, in order to specify, for example, a preferred audio stream language. When an audio stream is specified in this way, the Network Provider will always attempt to use it for all tune request in the tuning space (See [**ITuningSpace::put\_DefaultPreferredComponentTypes**](/windows/previous-versions/tuner/nf-tuner-ituningspace-put_defaultpreferredcomponenttypes?branch=master).) In some cases the actual components of a broadcast stream can only be discovered after reception begins, or the actual components may differ from what was advertised in the EPG information. At that time the [BDA Network Provider](bda-network-provider-filter.md) will fill in the component information in the tune request, and the application can then retrieve it and use it, for example, to change the audio stream or determine which audio streams are currently available.



| Interface                                                      | Description                                                                                                                             |
|----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| [**IAnalogAudioComponentType**](/windows/previous-versions/tuner/nn-tuner-ianalogaudiocomponenttype?branch=master) | Provides methods for accessing the analog audio mode.                                                                                   |
| [**IATSCComponentType**](/windows/previous-versions/tuner/nn-tuner-iatsccomponenttype?branch=master)               | Provides a method that indicates whether the audio substream is in AC-3 format.                                                         |
| [**IComponent**](/windows/previous-versions/tuner/nn-tuner-icomponent?branch=master)                               | Base class for all derived component interfaces.                                                                                        |
| [**IComponents**](/windows/previous-versions/tuner/nn-tuner-icomponents?branch=master)                             | Provides a standard COM enumeration of components.                                                                                      |
| [**IComponentType**](/windows/previous-versions/tuner/nn-tuner-icomponenttype?branch=master)                       | Base class for all derived component type interfaces.                                                                                   |
| [**IComponentTypes**](/windows/previous-versions/tuner/nn-tuner-icomponenttypes?branch=master)                     | Provides a standard COM enumeration of component types.                                                                                 |
| [**IEnumComponents**](/windows/previous-versions/tuner/nn-tuner-ienumcomponents?branch=master)                     | Implemented on a standard COM collection object containing all the active or inactive components on the current broadcast stream.       |
| [**IEnumComponentTypes**](/windows/previous-versions/tuner/nn-tuner-ienumcomponenttypes?branch=master)             | Implemented on a standard COM collection of [ComponentType](componenttype-object.md) objects associated with a given broadcast stream. |
| [**ILanguageComponentType**](/windows/previous-versions/tuner/nn-tuner-ilanguagecomponenttype?branch=master)       | Provides methods that describe the language of the substream.                                                                           |
| [**IMPEG2Component**](/windows/previous-versions/tuner/nn-tuner-impeg2component?branch=master)                     | Contains methods for getting and setting properties that describe an MPEG2 elementary stream.                                           |
| [**IMPEG2ComponentType**](/windows/previous-versions/tuner/nn-tuner-impeg2componenttype?branch=master)             | Provides methods that describe a component type associated with an MPEG-2 stream type.                                                  |



 

### Locator Interfaces

Locators are used by the Network Provider and other filters in the graph to determine how to locate a specified program. These interfaces are not used by applications except possibly for debugging purposes. Third parties that install new tuning spaces should also provide a default locator for the tuning space. An individual tune request contains a locator, which can be different from the default locator. If present, the locator in the tune request takes precedence over the default locator



| Interface                                            | Description                                                                                                                      |
|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [**IAnalogLocator**](/windows/previous-versions/tuner/nn-tuner-ianaloglocator?branch=master)             | Provides tuning information for an analog television network.                                                                    |
| [**IATSCLocator**](/windows/previous-versions/tuner/nn-tuner-iatsclocator?branch=master)                 | Provides tuning information for an ATSC network.                                                                                 |
| [**IATSCLocator2**](/windows/previous-versions/tuner/nn-tuner-iatsclocator2?branch=master)               | Enables the network provider to determine the physical channel, transport stream ID, and program number of an ATSC transmission. |
| [**IDigitalCableLocator**](/windows/previous-versions/tuner/?branch=master) | Provides tuning information for a digital cable network.                                                                         |
| [**IDigitalLocator**](/windows/previous-versions/tuner/?branch=master)           | Base interface for all derived locator interfaces for digital networks. Not used directly.                                       |
| [**IDVBCLocator**](/windows/previous-versions/tuner/?branch=master)                 | Provides tuning information for a DVB-C network.                                                                                 |
| [**IDVBSLocator**](/windows/previous-versions/tuner/nn-tuner-idvbslocator?branch=master)                 | Provides tuning information for a DVB-S network.                                                                                 |
| [**IDVBSLocator2**](/windows/previous-versions/tuner/nn-tuner-idvbslocator2?branch=master)               | Extends the [**IDVBSLocator**](/windows/previous-versions/tuner/nn-tuner-idvbslocator?branch=master) interface.                                                                      |
| [**IDVBTLocator**](/windows/previous-versions/tuner/nn-tuner-idvbtlocator?branch=master)                 | Provides tuning information for a DVB-T network.                                                                                 |
| [**IDVBTLocator2**](/windows/previous-versions/tuner/nn-tuner-idvbtlocator2?branch=master)               | Gets or sets tuning information for a Digital Video Broadcast - Second Generation Terrestrial (DVB-T2) network.                  |
| [**ILocator**](/windows/previous-versions/tuner/nn-tuner-ilocator?branch=master)                         | Base interface for all derived locator interfaces. Not used directly.                                                            |



 

### Event Service Tuning Model Interfaces

Starting in Windows 7, a new event service model is available for media graphs. Using this model, a device can register with the event service to receive only specific events. This model was originally developed to support the Protected Broadcast Driver Architecture, though PBDA is not a requirement for using these interfaces. The following interfaces define events that use this new model and allow developers to develop custom events and event services that fit this model:



| Interface                                                            | Description                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IESCloseMmiEvent**](/windows/previous-versions/tuner/nn-tuner-iesclosemmievent?branch=master)                         | Receives **CloseMMI** events from a Media Sink Device (MSD) device under the Protected Broadcast Driver Architecture (PBDA) (Windows 7 and later).                                                                                                     |
| [**IESEvent**](/windows/previous-versions/tuner/nn-tuner-iesevent?branch=master)                                         | Implements a generic event interface that can deliver and encapsulate events that are raised by devices that work with PBDA (Windows 7 and later).                                                                                                     |
| [**IESEvents**](/windows/previous-versions/tuner/nn-tuner-iesevents?branch=master)                                       | Implements event handling for devices that have registered to receive specific events derived from the [**IESEvent**](/windows/previous-versions/tuner/nn-tuner-iesevent?branch=master) interface (Windows 7 and later).                                                                                   |
| [**IESEventService**](/windows/previous-versions/tuner/nn-tuner-ieseventservice?branch=master)                           | Implements an event service that includes methods that raise events derived from the [**IESEvent**](/windows/previous-versions/tuner/nn-tuner-iesevent?branch=master) interface (Windows 7 and later).                                                                                                     |
| [**IESEventServiceConfiguration**](/windows/previous-versions/tuner/nn-tuner-ieseventserviceconfiguration?branch=master) | Configures an event service that implements the [**IESEventService**](/windows/previous-versions/tuner/nn-tuner-ieseventservice?branch=master) interface (Windows 7 and later).                                                                                                                            |
| [**IESFileExpiryDateEvent**](/windows/previous-versions/tuner/nn-tuner-iesfileexpirydateevent?branch=master)             | Gets information from a **FileExpiryDate** event, which a PBDA media transform device (MTD) fires when it receives a new license for protected content that contains a new expiry date for that content (Windows 7 and later).                         |
| [**IESIsdbCasResponseEvent**](/windows/previous-versions/tuner/nn-tuner-iesisdbcasresponseevent?branch=master)           | Gets information from a PBDA **IsdbCasResponse** event, which an Integrated Services Digital Broadcasting (ISDB) PBDA MTD raises to signal that response data is available to an MSD that has requested conditional access data (Windows 7 and later). |
| [**IESLicenseRenewalResultEvent**](/windows/previous-versions/tuner/nn-tuner-ieslicenserenewalresultevent?branch=master) | Gets information from a **LicenseRenewalResult** event, which contains the result of an attempt to renew a license for protected content (Windows 7 and later).                                                                                        |
| [**IESOpenMmiEvent**](/windows/previous-versions/tuner/nn-tuner-iesopenmmievent?branch=master)                           | Gets information from an **OpenMMI** event, which a PBDA MTD raises when a user tries to open an on-screen display, such as a dialog box (Windows 7 and later).                                                                                        |
| [**IESRequestTunerEvent**](/windows/previous-versions/tuner/nn-tuner-iesrequesttunerevent?branch=master)                 | Enable a PBDA-supported device to get exclusive access to a tuner and its Conditional Access Services (CAS) (Windows 7 and later).                                                                                                                     |
| [**IESValueUpdatedEvent**](/windows/previous-versions/tuner/nn-tuner-iesvalueupdatedevent?branch=master)                 | Inform a PBDA MSD that an MTD has updated the value for a name-value pair or exposed a new name-value pair (Windows 7 and later).                                                                                                                      |



 

### Miscellaneous Tuning Model Interfaces



| Interface                                                    | Description                                                                                                                           |
|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [**IBDACreateTuneRequestEx**](/windows/previous-versions/tuner/nn-tuner-ibdacreatetunerequestex?branch=master)   | Creates a new tuning request for a tuning space.                                                                                      |
| [**IChannelIDTuneRequest**](/windows/previous-versions/tuner/nn-tuner-ichannelidtunerequest?branch=master)       | Implements methods that support channel requests using a string identifier.                                                           |
| [**ICreatePropBagOnRegKey**](/windows/previous-versions/regbag/nn-regbag-icreatepropbagonregkey?branch=master)     | Creates a property bag that can store information in the system registry.                                                             |
| [**IMPEG2TuneRequestSupport**](/windows/previous-versions/tuner/?branch=master) | Indicates that the default network provider for a tuning space supports the [**IMPEG2TuneRequest**](/windows/previous-versions/tuner/nn-tuner-impeg2tunerequest?branch=master) interface. |
| [**IPersistTuneXml**](/windows/previous-versions/tuner/nn-tuner-ipersisttunexml?branch=master)                   | Serializes a tuning model object.                                                                                                     |
| [**IPersistTuneXmlUtility**](/windows/previous-versions/tuner/nn-tuner-ipersisttunexmlutility?branch=master)     | Defines utility methods for deserializing XML tuning requests.                                                                        |
| [**IPersistTuneXmlUtility2**](/windows/previous-versions/tuner/nn-tuner-ipersisttunexmlutility2?branch=master)   | Extends the [**IPersistTuneXmlUtility**](/windows/previous-versions/tuner/nn-tuner-ipersisttunexmlutility?branch=master) interface.                                                       |



 

## Related topics

<dl> <dt>

[Unified Tuning Model Reference](unified-tuning-model-reference.md)
</dt> </dl>

 

 





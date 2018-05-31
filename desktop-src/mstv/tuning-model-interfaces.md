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

These interfaces manage tuning space objects. You will never use the base class [**ITuningSpace**](ituningspace.md) interface directly; you will always use a derived interface that is specific to a particular network type.



| Interface                                                    | Description                                                                                                   |
|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [**IAnalogRadioTuningSpace**](ianalogradiotuningspace.md)   | Represents a tuning space for analog radio networks. (Not implemented in this release.)                       |
| [**IAnalogRadioTuningSpace2**](ianalogradiotuningspace2.md) | Represents a tuning space for analog radio networks and exposes a dialing prefix property.                    |
| [**IAnalogTVTuningSpace**](ianalogtvtuningspace.md)         | Represents a tuning space for analog TV networks.                                                             |
| [**IATSCTuningSpace**](iatsctuningspace.md)                 | Represents a tuning space for ATSC networks.                                                                  |
| [**IAuxInTuningSpace**](iauxintuningspace.md)               | Represents a tuning space for S-video or composite video inputs.                                              |
| [**IAuxInTuningSpace2**](iauxintuningspace2.md)             | Represents a tuning space for S-video or composite video inputs and exposes a dialing prefix property.        |
| [**IDigitalCableTuningSpace**](idigitalcabletuningspace.md) | Provides methods for working with tuning spaces with an ATSC network type.                                    |
| [**IDVBSTuningSpace**](idvbstuningspace.md)                 | Represents a tuning space for satellite DVB (DVB-S) networks.                                                 |
| [**IDVBTuningSpace**](idvbtuningspace.md)                   | Represents a tuning space for DVB networks.                                                                   |
| [**IDVBTuningSpace2**](idvbtuningspace2.md)                 | Represents a tuning space for DVB networks; extends the [**IDVBTuningSpace**](idvbtuningspace.md) interface. |
| [**IEnumTuningSpaces**](ienumtuningspaces.md)               | Standard COM enumeration interface for tuning spaces.                                                         |
| [**ITuningSpace**](ituningspace.md)                         | Base interface for all tuning spaces.                                                                         |
| [**ITuningSpaceContainer**](ituningspacecontainer.md)       | Provides access to all of the tuning spaces installed on the host system.                                     |
| [**ITuningSpaces**](ituningspaces.md)                       | Represents a collection of tuning spaces.                                                                     |



 

### Tune Request Interfaces

Tune requests are not created directly. They are obtained through a call to [**CreateTuneRequest**](ituningspace-createtunerequest.md) on a network-specific tuning space interface, such as [**IDVBTuningSpace**](idvbtuningspace.md).



| Interface                                                    | Description                                                                                  |
|--------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| [**IATSCChannelTuneRequest**](iatscchanneltunerequest.md)   | Provides tuning information specific to ATSC TV networks.                                    |
| [**IChannelTuneRequest**](ichanneltunerequest.md)           | Provides tuning information specific to analog TV networks.                                  |
| [**IDigitalCableTuneRequest**](idigitalcabletunerequest.md) | Provides methods for getting and setting the minor channel for a digital cable transmission. |
| [**IDVBTuneRequest**](idvbtunerequest.md)                   | Provides tuning information specific to DVB TV networks.                                     |
| [**IEnumTuningSpaces**](ienumtuningspaces.md)               | Implemented on a standard COM collection of tuning space objects.                            |
| [**IMPEG2TuneRequest**](impeg2tunerequest.md)               | Represents a minimal MPEG-2 tune request.                                                    |
| [**IMPEG2TuneRequestFactory**](impeg2tunerequestfactory.md) | Creates a tune request for a basic MPEG-2 transport stream containing the minimal tables.    |
| [**ITuneRequest**](itunerequest.md)                         | Provides tuning information relevant for all network types.                                  |



 

### Stream Component Interfaces

A *component* refers to a substream within a broadcast. Applications create a default preferred components collection based on user input, in order to specify, for example, a preferred audio stream language. When an audio stream is specified in this way, the Network Provider will always attempt to use it for all tune request in the tuning space (See [**ITuningSpace::put\_DefaultPreferredComponentTypes**](ituningspace-put-defaultpreferredcomponenttypes.md).) In some cases the actual components of a broadcast stream can only be discovered after reception begins, or the actual components may differ from what was advertised in the EPG information. At that time the [BDA Network Provider](bda-network-provider-filter.md) will fill in the component information in the tune request, and the application can then retrieve it and use it, for example, to change the audio stream or determine which audio streams are currently available.



| Interface                                                      | Description                                                                                                                             |
|----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| [**IAnalogAudioComponentType**](ianalogaudiocomponenttype.md) | Provides methods for accessing the analog audio mode.                                                                                   |
| [**IATSCComponentType**](iatsccomponenttype.md)               | Provides a method that indicates whether the audio substream is in AC-3 format.                                                         |
| [**IComponent**](icomponent.md)                               | Base class for all derived component interfaces.                                                                                        |
| [**IComponents**](icomponents.md)                             | Provides a standard COM enumeration of components.                                                                                      |
| [**IComponentType**](icomponenttype.md)                       | Base class for all derived component type interfaces.                                                                                   |
| [**IComponentTypes**](icomponenttypes.md)                     | Provides a standard COM enumeration of component types.                                                                                 |
| [**IEnumComponents**](ienumcomponents.md)                     | Implemented on a standard COM collection object containing all the active or inactive components on the current broadcast stream.       |
| [**IEnumComponentTypes**](ienumcomponenttypes.md)             | Implemented on a standard COM collection of [ComponentType](componenttype-object.md) objects associated with a given broadcast stream. |
| [**ILanguageComponentType**](ilanguagecomponenttype.md)       | Provides methods that describe the language of the substream.                                                                           |
| [**IMPEG2Component**](impeg2component.md)                     | Contains methods for getting and setting properties that describe an MPEG2 elementary stream.                                           |
| [**IMPEG2ComponentType**](impeg2componenttype.md)             | Provides methods that describe a component type associated with an MPEG-2 stream type.                                                  |



 

### Locator Interfaces

Locators are used by the Network Provider and other filters in the graph to determine how to locate a specified program. These interfaces are not used by applications except possibly for debugging purposes. Third parties that install new tuning spaces should also provide a default locator for the tuning space. An individual tune request contains a locator, which can be different from the default locator. If present, the locator in the tune request takes precedence over the default locator



| Interface                                            | Description                                                                                                                      |
|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [**IAnalogLocator**](ianaloglocator.md)             | Provides tuning information for an analog television network.                                                                    |
| [**IATSCLocator**](iatsclocator.md)                 | Provides tuning information for an ATSC network.                                                                                 |
| [**IATSCLocator2**](iatsclocator2.md)               | Enables the network provider to determine the physical channel, transport stream ID, and program number of an ATSC transmission. |
| [**IDigitalCableLocator**](idigitalcablelocator.md) | Provides tuning information for a digital cable network.                                                                         |
| [**IDigitalLocator**](idigitallocator.md)           | Base interface for all derived locator interfaces for digital networks. Not used directly.                                       |
| [**IDVBCLocator**](idvbclocator.md)                 | Provides tuning information for a DVB-C network.                                                                                 |
| [**IDVBSLocator**](idvbslocator.md)                 | Provides tuning information for a DVB-S network.                                                                                 |
| [**IDVBSLocator2**](idvbslocator2.md)               | Extends the [**IDVBSLocator**](idvbslocator.md) interface.                                                                      |
| [**IDVBTLocator**](idvbtlocator.md)                 | Provides tuning information for a DVB-T network.                                                                                 |
| [**IDVBTLocator2**](idvbtlocator2.md)               | Gets or sets tuning information for a Digital Video Broadcast - Second Generation Terrestrial (DVB-T2) network.                  |
| [**ILocator**](ilocator.md)                         | Base interface for all derived locator interfaces. Not used directly.                                                            |



 

### Event Service Tuning Model Interfaces

Starting in Windows 7, a new event service model is available for media graphs. Using this model, a device can register with the event service to receive only specific events. This model was originally developed to support the Protected Broadcast Driver Architecture, though PBDA is not a requirement for using these interfaces. The following interfaces define events that use this new model and allow developers to develop custom events and event services that fit this model:



| Interface                                                            | Description                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IESCloseMmiEvent**](iesclosemmievent.md)                         | Receives **CloseMMI** events from a Media Sink Device (MSD) device under the Protected Broadcast Driver Architecture (PBDA) (Windows 7 and later).                                                                                                     |
| [**IESEvent**](iesevent.md)                                         | Implements a generic event interface that can deliver and encapsulate events that are raised by devices that work with PBDA (Windows 7 and later).                                                                                                     |
| [**IESEvents**](iesevents.md)                                       | Implements event handling for devices that have registered to receive specific events derived from the [**IESEvent**](iesevent.md) interface (Windows 7 and later).                                                                                   |
| [**IESEventService**](ieseventservice.md)                           | Implements an event service that includes methods that raise events derived from the [**IESEvent**](iesevent.md) interface (Windows 7 and later).                                                                                                     |
| [**IESEventServiceConfiguration**](ieseventserviceconfiguration.md) | Configures an event service that implements the [**IESEventService**](ieseventservice.md) interface (Windows 7 and later).                                                                                                                            |
| [**IESFileExpiryDateEvent**](iesfileexpirydateevent.md)             | Gets information from a **FileExpiryDate** event, which a PBDA media transform device (MTD) fires when it receives a new license for protected content that contains a new expiry date for that content (Windows 7 and later).                         |
| [**IESIsdbCasResponseEvent**](iesisdbcasresponseevent.md)           | Gets information from a PBDA **IsdbCasResponse** event, which an Integrated Services Digital Broadcasting (ISDB) PBDA MTD raises to signal that response data is available to an MSD that has requested conditional access data (Windows 7 and later). |
| [**IESLicenseRenewalResultEvent**](ieslicenserenewalresultevent.md) | Gets information from a **LicenseRenewalResult** event, which contains the result of an attempt to renew a license for protected content (Windows 7 and later).                                                                                        |
| [**IESOpenMmiEvent**](iesopenmmievent.md)                           | Gets information from an **OpenMMI** event, which a PBDA MTD raises when a user tries to open an on-screen display, such as a dialog box (Windows 7 and later).                                                                                        |
| [**IESRequestTunerEvent**](iesrequesttunerevent.md)                 | Enable a PBDA-supported device to get exclusive access to a tuner and its Conditional Access Services (CAS) (Windows 7 and later).                                                                                                                     |
| [**IESValueUpdatedEvent**](iesvalueupdatedevent.md)                 | Inform a PBDA MSD that an MTD has updated the value for a name-value pair or exposed a new name-value pair (Windows 7 and later).                                                                                                                      |



 

### Miscellaneous Tuning Model Interfaces



| Interface                                                    | Description                                                                                                                           |
|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [**IBDACreateTuneRequestEx**](ibdacreatetunerequestex.md)   | Creates a new tuning request for a tuning space.                                                                                      |
| [**IChannelIDTuneRequest**](ichannelidtunerequest.md)       | Implements methods that support channel requests using a string identifier.                                                           |
| [**ICreatePropBagOnRegKey**](icreatepropbagonregkey.md)     | Creates a property bag that can store information in the system registry.                                                             |
| [**IMPEG2TuneRequestSupport**](impeg2tunerequestsupport.md) | Indicates that the default network provider for a tuning space supports the [**IMPEG2TuneRequest**](impeg2tunerequest.md) interface. |
| [**IPersistTuneXml**](ipersisttunexml.md)                   | Serializes a tuning model object.                                                                                                     |
| [**IPersistTuneXmlUtility**](ipersisttunexmlutility.md)     | Defines utility methods for deserializing XML tuning requests.                                                                        |
| [**IPersistTuneXmlUtility2**](ipersisttunexmlutility2.md)   | Extends the [**IPersistTuneXmlUtility**](ipersisttunexmlutility.md) interface.                                                       |



 

## Related topics

<dl> <dt>

[Unified Tuning Model Reference](unified-tuning-model-reference.md)
</dt> </dl>

 

 





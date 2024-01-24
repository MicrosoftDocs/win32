---
description: The Terminal Object interfaces give an application access to manipulate devices used to create or receive media streams.
ms.assetid: 08320d1c-1400-4746-b526-74b0789c5fc0
title: Terminal Object Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Terminal Object Interfaces

The [Terminal Object](terminal-object.md) interfaces give an application access to manipulate devices used to create or receive media streams.

These interfaces are implemented by an MSP and will not be available if the address is not supported by a media service provider. If an associated MSP exists, the [**ITTerminalSupport**](/windows/win32/api/tapi3if/nn-tapi3if-itterminalsupport) interface is exposed on the [Address Object](address-object.md).

The [**IEnumTerminal**](/windows/desktop/api/tapi3if/nn-tapi3if-ienumterminal) and [**IEnumTerminalClass**](/windows/desktop/api/tapi3if/nn-tapi3if-ienumterminalclass) interfaces are not directly exposed on the Terminal Object, but are tightly related to it and are listed here for reference convenience.



| Interface                                                                  | Description                                                                                                                       |
|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [**ITTerminal**](/windows/win32/api/tapi3if/nn-tapi3if-itterminal)                                           | Base interface for the Terminal Object. It provides methods for obtaining information such as terminal class and media supported. |
| [**ITAMMediaFormat**](/windows/win32/api/tapi3/nn-tapi3-itammediaformat)                                 | Sets and gets DirectShow media format.                                                                                            |
| [**ITBasicAudioTerminal**](/windows/desktop/api/tapi3if/nn-tapi3if-itbasicaudioterminal)                       | Provides methods to set and get standard audio terminal characteristics, such as volume.                                          |
| [**IEnumTerminal**](/windows/desktop/api/tapi3if/nn-tapi3if-ienumterminal)                                     | Enumerates [**ITTerminal**](/windows/win32/api/tapi3if/nn-tapi3if-itterminal).                                                                                      |
| [**IEnumTerminalClass**](/windows/desktop/api/tapi3if/nn-tapi3if-ienumterminalclass)                           | Enumerates [**Terminal Class**](terminal-class.md).                                                                              |
| [**IEnumPluggableSuperclassInfo**](/windows/desktop/api/tapi3if/nn-tapi3if-ienumpluggablesuperclassinfo)       | Enumerates [**ITPluggableTerminalSuperclassInfo**](/windows/desktop/api/tapi3if/nn-tapi3if-itpluggableterminalsuperclassinfo).                                        |
| [**IEnumPluggableTerminalClassInfo**](/windows/desktop/api/tapi3if/nn-tapi3if-ienumpluggableterminalclassinfo) | Enumerates [**ITPluggableTerminalClassInfo**](/windows/desktop/api/tapi3if/nn-tapi3if-itpluggableterminalclassinfo).                                                  |
| [**ITFileTrack**](/windows/desktop/api/tapi3if/nn-tapi3if-itfiletrack)                                         | Retrieves and sets information concerning file terminal tracks.                                                                   |
| [**ITASRTerminalEvent**](/windows/desktop/api/tapi3if/nn-tapi3if-itasrterminalevent)                           | Retrieves the description of Automatic Speech Recognition terminal events.                                                        |
| [**ITFileTerminalEvent**](/windows/desktop/api/tapi3if/nn-tapi3if-itfileterminalevent)                         | Retrieves the description of file terminal events.                                                                                |
| [**ITMultiTrackTerminal**](/windows/desktop/api/tapi3if/nn-tapi3if-itmultitrackterminal)                       | Enumerates, creates, or removes tracks on multitrack terminals.                                                                   |



 



| Interface                                                                                      | Description                                                                                                                  |
|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| [**ITPluggableTerminalClassInfo**](/windows/desktop/api/tapi3if/nn-tapi3if-itpluggableterminalclassinfo)                           | Retrieves information concerning a pluggable terminal.                                                                       |
| [**ITPluggableTerminalClassRegistration**](/windows/desktop/api/Termmgr/nn-termmgr-itpluggableterminalclassregistration)           | Creates, modifies, or deletes the registry entry for a pluggable terminal.                                                   |
| [**ITPluggableTerminalInitialization**](/windows/desktop/api/Termmgr/nn-termmgr-itpluggableterminalinitialization)                 | Performs primary terminal object creation for pluggable terminals, allowing the Terminal Manager to initialize the terminal. |
| [**ITPluggableTerminalSuperclassInfo**](/windows/desktop/api/tapi3if/nn-tapi3if-itpluggableterminalsuperclassinfo)                 | Retrieves the name and CLSID of a pluggable terminal class.                                                                  |
| [**ITPluggableTerminalSuperclassRegistration**](/windows/desktop/api/Termmgr/nn-termmgr-itpluggableterminalsuperclassregistration) | Retrieves and sets information about a terminal superclass (name and CLSID).                                                 |
| [**ITPluggableTerminalEventSink**](/windows/desktop/api/msp/nn-msp-itpluggableterminaleventsink)                           | Notifies client applications about changes in a pluggable terminal.                                                          |
| [**ITPluggableTerminalEventSinkRegistration**](/windows/desktop/api/msp/nn-msp-itpluggableterminaleventsinkregistration)   | Registers and unregisters a client application for notification about pluggable terminal events.                             |



 



| Interface                                            | Description                                                        |
|------------------------------------------------------|--------------------------------------------------------------------|
| [**ITTTSTerminalEvent**](/windows/desktop/api/tapi3if/nn-tapi3if-itttsterminalevent)     | Retrieves the description of text-to-speech (TTS) terminal events. |
| [**ITToneDetectionEvent**](/windows/desktop/api/Tapi3if/nn-tapi3if-ittonedetectionevent) | Retrieves information about a tone detection event.                |
| [**ITToneTerminalEvent**](/windows/desktop/api/tapi3if/nn-tapi3if-ittoneterminalevent)   | Retrieves the description of tone terminal events.                 |



 

 

 

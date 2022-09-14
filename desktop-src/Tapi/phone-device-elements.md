---
description: A phone device is a device that supports the phone device class and that includes hookswitches, handsets, speakerphones, and headsets.
ms.assetid: c2660d77-0265-49d4-bd04-1cddd674b760
title: Phone Device Elements
ms.topic: article
ms.date: 05/31/2018
---

# Phone Device Elements

A phone device is a device that supports the phone device class and that includes some or all of the following elements:

-   **Hookswitch/transducer**: This is a means for audio input and output. A phone device can have several transducers, which can be activated and deactivated (taken offhook or placed onhook) under application or manual user control.

    Telephony identifies three types of hookswitch devices common to many phone sets:

     **Handset**: The traditional mouth-and-ear piece combination that must be manually lifted from a cradle and held against the user's ear.  
    **Speakerphone**: Enables the user to conduct calls hands-free. The speakerphone may be internal or external to the phone device. The speaker part of a speakerphone allows multiple listeners.  
    **Headset**: Enables the user to conduct calls hands-free.  
    

    A hookswitch must be offhook to allow audio data to be sent to and/or received by the corresponding transducer.

-   Volume Control/Gain Control/Mute: Each hookswitch device is the pairing of a speaker and a microphone component. The API provides for volume control and muting of speaker components and for gain control or muting of microphone components.
-   [Ringer](ring.md): A means for alerting users, usually through a bell. A phone device may be able to ring in a variety of modes or patterns.
-   [Display](display.md): A mechanism for visually presenting messages to the user. A phone display is characterized by its number of rows and columns.
-   [Phone buttons](phone-buttons.md): An array of buttons. Whenever the user presses a button on the phone set, the API reports that the corresponding button was pressed. Button-lamp identifiers identify a button and lamp pair. Of course, it is possible to have button-lamp pairs with either no button or no lamp. Button-lamp identifiers are integer values that range from 0 to the maximum number of button-lamps available on the phone device, minus one. Each button belongs to a button class. Classes include call appearance buttons, feature buttons, keypad buttons, and local buttons.
-   [Lamps](lamps.md): An array of lamps (such as LEDs) individually controllable from the API. Lamps can be lit in different modes by varying the on and off frequency. The button-lamp identifier identifies the lamp.
-   [Data areas](data-areas.md): Memory areas in the phone device where instruction code or data can be downloaded to and/or uploaded from. The downloaded information would affect the behavior (or in other words, program) the phone device.

TAPI allows an application to monitor and control elements of the phone device. The most useful elements for an application are the hookswitch devices. The phone set can act as an audio I/O device (to the computer) with volume control, gain control and mute, a ringer (for alerting the user), data areas (for programming the phone), and perhaps a display, though the computer's display is more capable. The application writer is discouraged from directly controlling or using phone lamps or phone buttons, because lamp and button capabilities can vary widely among phone sets, and applications can quickly become tailored to specific phone sets.

There is no guaranteed core set of services supported by all phone devices as there is for line devices (the Basic Telephony services). Therefore, before an application can use a phone device, the application must first determine the exact capabilities of the phone device. Telephony capability varies with the configuration (client versus client/server), the telephone hardware, and the service-provider software. Applications should make no assumptions as to what telephony capabilities are available. An application determines the device capabilities of a phone device by calling the [**phoneGetDevCaps**](/windows/desktop/api/Tapi/nf-tapi-phonegetdevcaps) function. A phone's device capabilities indicate which of these elements exist for each phone device present in the system and what their capabilities are. Although strongly oriented toward real-life telephone sets, this abstraction can provide a meaningful implementation (or subset thereof) for other devices as well. Take as an example a separate headset directly connected and controllable from the computer and operated as a phone device. Hookswitch changes can be triggered by detection of voice energy (offhook) or a period of silence (onhook); ringing can be emulated by the generation of an audible signal into the headset; a display can be emulated through text-to-speech conversion.

A phone device need not be realized in hardware, but can instead be emulated in software using a mouse- or keyboard-driven graphical command interface and the computer's speaker or sound system. Such a "soft phone" can be an application that uses TAPI. It can also be a service provider, which can be listed as a phone device available to other applications through the API, and as such is assigned a phone device identifier.

Depending on the environment and configuration, phone sets can be shared devices between the application and the switch. Some minor provision is made in the API where the switch can temporarily suspend the API's control of a phone device.

 

 




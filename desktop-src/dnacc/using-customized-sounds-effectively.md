---
Description: Microsoft Corporation
ms.assetid: eca1c6f1-f426-4b46-a569-e9b1587c49da
title: Using Customized Sounds Effectively
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using Customized Sounds Effectively

Microsoft Corporation

October 2002

**Summary:** Learn about the advantages of, as well as common tools for creating customizable sounds.

-   [Introduction](#introduction)
    -   [Guidelines to Consider](#guidelines-to-consider)
    -   [Use the standard function for playing sounds](#use-the-standard-function-for-playing-sounds)
    -   [Use ShowSounds for sounds with dialog spoken by a person or a machine](#use-showsounds-for-sounds-with-dialog-spoken-by-a-person-or-a-machine)
    -   [Use the Windows operating system SoundSentry support](#use-the-windows-operating-system-soundsentry-support)
-   [Summary](#summary)
-   [Resources](#resources)

## Introduction

Sound can be an effective user interface (UI) element for people with disabilities. Even if it is used only to supplement other UI elements, sound can help users recognize events audibly.

In a graphical user interface, sound is usually designed to complement graphical or function events. If the sound is dialog spoken by a person or a machine, a user should be able to turn on captions.

However, sound can be an effective UI element only when it is properly designed. To maximize an effective design, applications should leverage sound events that are already defined by the Microsoft Windows operating system. Applications can also register a custom sound with a meaningful label in the registry key, which will allow users to customize the sound file if necessary. Because all users have different needs, it is better to make custom sounds as flexible as possible.

### Guidelines to Consider

There are a few standards for system sounds registration and handling. It is recommended that application developers follow these guidelines:

### Use the standard function for playing sounds

`PlaySound` is the standard Windows function for commanding devices to play sounds. An application can use this function to play any wave format file; however, it is recommended that applications either leverage system sounds already registered by the operating system or register custom sounds in the system registry, **Sound Alias**.

> [!Note]  
> Some basic sounds are also available through the **MessageBeep** function. Please use this function so that Windows SoundSentry support can be leveraged.

 

Properly registered sound events are customizable through the Control Panel. For design and registration of sound events, see the following technical article, [Windows User Experience Chapter 11 Integrating with the System: Creating System Sounds](ch11f)

### Use ShowSounds for sounds with dialog spoken by a person or a machine

ShowSounds is a system option for captioning that a user can turn on and off, allowing sounds to be represented visually.

It is effective not only for the deaf or hard of hearing but also for users who cannot raise the sound levels because they are in a quiet public space or who are in a noisy environment such as a public kiosk or a convention. Captioning is also a powerful tool for students learning a second language.

See the following technical articles for more information on ShowSounds:

[Supporting ShowSounds in Your Applications](supporting-showsounds-in-your-applications.md)

[Captions and Audio Descriptions for PC Multimedia](captions-and-audio-descriptions-for-pc-multimedia.md)

### Use the Windows operating system SoundSentry support

As stated above, sound is inappropriate in some environments (for example, a library or hospital setting).

SoundSentry is different from the ShowSounds option. When the SoundSentry option is active, Windows automatically generates visual warnings when an application makes sounds. The option is not universally available for all sounds played in Windows; it is effective only when the system or applications create sound with the **MessageBeep** function or with PC speaker (also known as beep noise).

If your application is asked to support SoundSentry for a particular event, you can use either the **MessageBeep** or **Beep** functions.

## Summary

It is important for application developers to design applications so that the sound interface can be customized. A particular sound may conflict with a similar sound used by other applications or the system. Some users may need to be able to customize sound for better cognition. Also, sound information may require a visual display in environments where sound is either inappropriate or inaudible.

Finally, it is strongly recommended that application developers adhere to the standards for system sounds registration and handling.

## Resources



| Document                                                                                                   | Purpose                                                                   |
|------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| [Windows User Experience Chapter 11 Integrating with the System "Creating System Sounds"](ch11f)           | General design guideline for sound events                                 |
| [Supporting ShowSounds in Your Applications](supporting-showsounds-in-your-applications.md)               | MSDN technical article about ShowSounds                                   |
| [Captions and Audio Descriptions for PC Multimedia](captions-and-audio-descriptions-for-pc-multimedia.md) | MSDN technical article about captioning and audio descriptions in general |



 

 

 




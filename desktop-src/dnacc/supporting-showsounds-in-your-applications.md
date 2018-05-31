---
Description: Microsoft Corporation
ms.assetid: 6b511e94-8bfe-4287-9382-8110d94a9e7c
title: Supporting ShowSounds in Your Applications
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Supporting ShowSounds in Your Applications

Microsoft Corporation

March 2002

**Summary:** This article discusses the ShowSounds system parameter that instructs applications to display visual equivalents, such as text captions or informative symbols, for application speech and sounds. ShowSounds is enabled or disabled through Accessibility Options in Control Panel in Microsoft Windows XP and Microsoft Windows 2000. (3 printed pages)

-   [Introduction](#introduction)
-   [Benefits of ShowSounds](#benefits-of-showsounds)
-   [Types of Sounds that Require ShowSounds Support](#types-of-sounds-that-require-showsounds-support)
    -   [Designing the User Interface to Support ShowSounds](#designing-the-user-interface-to-support-showsounds)
-   [Accessing ShowSounds Programmatically](#accessing-showsounds-programmatically)
    -   [Accessing ShowSounds from a Win32 or .NET Application](#accessing-showsounds-from-a-win32-or-net-application)
    -   [Accessing ShowSounds from an HTML+TIME Application](#accessing-showsounds-from-an-htmltime-application)

## Introduction

The ShowSounds system parameter instructs applications to display visual equivalents, such as text captions or informative symbols, for application speech and sounds. The user can enable or disable ShowSounds through Accessibility Options in Control Panel in Microsoft Windows XP and Microsoft Windows 2000.

Obviously, your application must support ShowSounds for visual equivalents to appear. Microsoft recommends that all applications provide such support. However, various approaches exist for creating and implementing visual equivalents.

The type of visual equivalents your application provides is entirely up to you. For example, let's say you're designing a multimedia product that includes a video of someone speaking before the United States Congress. The application could display synchronized captions that describe the setting and what the speaker is saying. Three existing multimedia products that use captions are Microsoft Encarta Encyclopedia, Microsoft Windows Media Player, and The Magic School Bus by Scholastic Inc.

On the other hand, let's say you are designing an email program. If the program sounds a beep to alert the user that a high-priority email message has arrived, the program could also display a blinking exclamation point symbol on the Windows taskbar.

> [!Note]  
> Your application cannot override the user's ShowSounds preference. In other words, you cannot display visual equivalents if the user does not want them.

 

## Benefits of ShowSounds

According to recent studies, in the United States alone there are approximately two million people who have some form or degree of hearing loss. For them, a text-based or graphics-based environment provides a productive and accessible work environment. However, in instances where events occur requiring the user's intervention, a sound cue alone will not catch his or her attention and draw it to the event.

While ShowSounds is primarily intended for deaf or hard-of-hearing users, it can be a valuable option for other customers as well. For example, visual cues can be a significant aid for someone learning a foreign language, for those with learning disabilities, or for customers using the PC in a loud environment, such as a factory floor. For them, some kind of visual cue must occur to focus their attention on the event so they can intervene. The same holds true for users on a computer without sound capability.

> [!Note]  
> The user's selection of ShowSounds does not restrict an application to presenting information visually. A user should be able to request visual feedback regardless of whether he or she also wants audible feedback.

 

## Types of Sounds that Require ShowSounds Support

To provide ShowSounds support, you first need to know the difference between a visual equivalent and a visual indication. A *visual equivalent* contains the same information that is normally conveyed by a sound alone. For example, a caption that contains the lyrics of a song would be a visual equivalent to the playing of that song. On the other hand, a *visual indication* merely indicates that a sound is playing — without providing specific information about that sound. For example, a symbol on the Windows Taskbar that says Music! is a visual indication that a song is playing.

If the user has selected ShowSounds, your application should display visual equivalents for all sounds that convey information important to the operation of the application. It should also display visual equivalents for sounds that normally supplement visual material. For example, if an audio track describes the content or setting of a video, captions can provide information equivalent to that audio track. For music and other sounds that convey no information, your application needs only to display visual indications.

Generally, your application does not need to provide ShowSounds support for sounds that merely emphasize visual events, such as the beep that often accompanies the appearance of a message box.

### Designing the User Interface to Support ShowSounds

The design of the visual equivalents is application-specific and depends on the information that will be presented to the user. Different applications use different forms of visual equivalents, such as captions or symbols. You should use standard Windows application design principles for user interface (UI) design.

## Accessing ShowSounds Programmatically

The ShowSounds system parameter is accessible to all applications built on Win32, .NET, or HTML+TIME technology.

### Accessing ShowSounds from a Win32 or .NET Application

From a Win32 or .NET application, call the GetSystemMetrics function with the SM\_SHOWSOUNDS parameter to get the value of the ShowSounds system parameter.

> [!Note]  
> You can also get or set ShowSounds by calling the SystemParametersInfo function with the SPI\_GETSHOWSOUNDS or SPI\_SETSHOWSOUNDS parameter, respectively. Getting ShowSounds in this manner is equivalent to calling [**GetSystemMetrics**](https://msdn.microsoft.com/library/windows/desktop/ms724385) with SM\_SHOWSOUNDS. Programmatically setting ShowSounds is not recommended.

 

From a .NET application, the ShowSounds system parameter is also accessible as the [**ShowSounds**](frlrfSystemWindowsFormsSystemInformationClassShowSoundsTopic) property of the [**SystemInformation**](frlrfSystemWindowsFormsSystemInformationClassTopic) class.

### Accessing ShowSounds from an HTML+TIME Application

From an HTML+TIME 2.0 application, access ShowSounds though the **systemCaptions** and **systemOverdubOrSubtitle** attributes, which are supported by Microsoft Internet Explorer version 5.5 and later.

If the user has selected ShowSounds, **systemCaptions** is set to "on" and **systemOverdubOrSubtitle** is set to "subtitle." If ShowSounds is disabled, **systemCaptions** is set to "off" and **systemOverdubOrSubtitle** is set to "overdub."

> [!Note]  
> For more information about HTML+TIME, see [HTML+TIME](htime_node_entry).

 

 

 




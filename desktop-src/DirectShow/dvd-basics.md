---
description: DVD Basics
ms.assetid: 08357ff5-4606-4bfc-8dd6-907aca4b5f07
title: DVD Basics
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DVD Basics

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The features that make DVD attractive to consumers—seamless branching, multiple languages, parental control, karaoke support, and multiple angles—also make the developer's job a little more complex. A DVD player must not only play back audio, video, and subpicture streams, but also must keep track of the navigation options that the disc is currently permitting, and correctly handle many types of user commands. The DVD Navigator shields you from much of this complexity while enabling you to create a fully-functional DVD application. You do not need to refer to the DVD specification to use the DVD Navigator API effectively, but you do need to know basic DVD navigation concepts.

**Navigation Control Data**

The audio and video data on a DVD-Video disc is interleaved at regular intervals with various kinds of navigation control data. This data may be an instruction that tells the player to do something, for example move to some particular place on the disc, or it may be an informational-only marker informing the player for example that the content that follows has a higher parental management level than the previous content, or that the chapter skip operation is disabled. The player relays this information to an application, and it is the responsibility of the application to act on it. These navigation markers are part of what give DVD its higher level of user-interactivity compared to Video CDs. A DVD-player application must handle events that originate with the disc as well as events that originate with the user.

**Audio, Video and Subpicture Data**

A DVD-Video disc contains three primary types of streams: video, audio and subpicture.

-   The video stream can contain up to nine "angles," which can be thought of as substreams. DVD authors can include multiple angles wherever they wish to offer the viewer a choice of camera angles from which to view the same scene. Only one angle can be active at a time. The video stream also contains line 21 Closed Caption data, if any exists.
-   There can be up to eight separate audio streams, or tracks, providing up to eight multichannel soundtracks and allowing DVD karaoke discs to make use of multichannel audio.
-   A DVD may contain up to 32 *subpicture* streams. These consist of compressed 16-color bitmaps with an alpha channel, which are overlayed on top of the video. Typically, subpicture streams contain subtitles and menu buttons, although they may contain other graphics as well. A subpicture stream may have a specified language. Some subpicture content is always shown, and some subpicture content is shown only if the user enables it.

Note that captions in a subpicture stream are not the same as line-21 closed captions. Closed captions, which are intended for hard-of-hearing viewers, are embedded in the video signal. They consist entirely of character strings. Subpicture captions, on the other hand, are graphical bitmaps. On a consumer device, closed captions are displayed by the television set, while the subpicture stream is rendered by the DVD player. A DVD may contain both types of caption.

**Titles and Chapters**

The video content in a DVD is divided into *titles* and *menus*. Titles are further divided into units that the DVD specification calls *parts of titles* (PTTs). More often, these are called *scenes* or *chapters*. (The DirectShow documentation uses the term chapter.) The viewer can navigate to specific titles or chapters within titles.

The author of a DVD decides how to divide the content into titles and chapters. When a DVD contains a feature-length film, the entire film is often placed in one title, divided into chapters for the individual scenes. Extra features on the DVD, such as trailers or deleted scenes, are placed in separate titles. However, these divisions are arbitrary, and many DVDs are organized differently.

There may be up to 99 titles on a disc and disc authors may divide the title into as many as 999 logical chapters. In most feature films on DVD, movie content is formatted as a series of chapters which automatically play one after another. On such discs, the end-of-chapter marker contains a branching instruction that tells the player to continue playing the next chapter in the sequence. These titles are referred to as *One Sequential PGC Titles*. (PGC stands for program chain, another name for a group of chapters that belong together. This term is not used in the DVD Navigator documentation.) On discs with other types of content, such as karaoke discs, an end-of-chapter marker might instruct the player to show a menu, or it might simply instruct the player to stop.

DVD application developers use title and chapter numbers to jump to specific points on a disc. For finer access, a title number and time code can be used. Time codes can only be used with One Sequential PGC Titles, since other types do not contain time code maps.

**Menus**

The DVD specification defines six types of menu:

-   **Title.** The title menu is the first menu to be displayed. Usually it has buttons for selecting titles. The title menu is also called the *video manager menu*. There is only one title menu on a DVD.
-   **Root.** A root menu is the top-level menu for a title. Each title can have a root menu. The next four menus are submenus from the root menu. A root menu is also called a *video title set menu*. The root menu typically has buttons that navigate to any of the titles in the title set. In addition, it can have submenus that enable the user to choose options for the audio stream, camera angle, subpicture stream, or chapter. However, these submenus are not used on most DVDs.
-   **Subpicture.** The subpicture menu selects the subpicture stream.
-   **Audio.** The audio menu selects the audio stream. Typically, this menu enables the viewer to select a language track.
-   **Angle.** The angle menu selects the camera angle.
-   **Chapter.** The chapter menu, also called the PTT menu, selects chapters within a title.

Most menus have buttons, which can be *selected* and *activated*. Selecting a button changes the button's appearance. Activating a button triggers a DVD command, such as showing another menu or starting playback.

**Parental Management Levels**

All or part of a DVD disc can be encoded with a Parental Management Level (PML) numbered from one to eight. Eight is the most restrictive level (adults only) and one is the least restrictive (all ages). The idea is to prevent children from watching adult content without parental consent, while allowing adults to watch child-safe content. In the United States and Canada, the levels map to the rating system of the MPAA (G, PG, PG-13, NC-17), but this is not the case in other countries or regions.

Because chapters can exist logically within a parental block, there may be two versions of the same chapter in a title, each assigned a different PML and in a different parental block. For example, a child who logs in and plays the disc would see one version of Chapter 3, and an adult who logs in would see a different version, assuming that the application supports PMLs.

A title or chapter can also contain temporary PMLs, whose content is rated higher than the PML for the title or chapter as a whole. This means that a title may have more than one parental level. Temporary PMLs are generally authored as angle blocks, so that a scene in a film may have two versions, one rated for younger viewers and one for adults.

It is the responsibility of the player application to enforce the parental levels.

**Domains**

The term *domain* refers to the internal state of a DVD player; it is not something authored on the disc. Domains are important because some DVD commands are only valid in certain domains. DirectShow provides a way to query the current domain and to be notified when the domain changes. The following domains are defined:

-   **First Play.** In this domain, the DVD player has just started playing the DVD. After it enters the First Play domain, the player switches to another domain—either a menu domain or the title domain, depending on the disc.
-   **Video Manager Menu.** The player is showing the Video Manager Menu, also called the title menu.
-   **VTS Menu.** The player is showing a menu associated with a video title set, either the root menu or a submenu (audio, sub-picture, angle, or chapter).
-   **Title.** The player is playing video in a title.
-   **Stop.** The player is not displaying anything. (Strictly speaking, the DVD specification does not call this state a domain, but it can be treated as one.)

The domain can be thought of as a state variable that a DVD player monitors, in order to keep track of the type of content that the player is currently reading from the disc. DVD players use domains to avoid issuing meaningless commands to the DVD drive.

**User Operation Controls**

User Operation Controls (UOPs) are markers on a disc that DVD authors can insert anywhere to restrict a user's navigation options. Most discs follow standard UOP restrictions. For example, most discs do not allow the viewer to fast forward or show a menu while in First Play domain. In principle, each disc can insert any UOP command at any point on the disc, even if the command would otherwise be valid within the current domain. For example, a disc may be authored to disallow fast forwarding in a certain title or to prevent a particular menu from being shown after the user enters the title domain. The DVD Navigator complies with all such commands from the disc and will not allow an application to override the disc's UOP controls.

## Related topics

<dl> <dt>

[DVD Applications](dvd-applications.md)
</dt> </dl>

 

 




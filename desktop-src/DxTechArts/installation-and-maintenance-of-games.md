---
title: Installation and Maintenance of Games
description: This article describes a set of best practices that can help reduce user frustration about the time required to install a game, prevent unnecessary support calls, and allow users to start playing your game as quickly and painlessly as possible.
ms.assetid: c953165d-2318-ca06-a895-abedcbcb594c
ms.topic: article
ms.date: 05/31/2018
---

# Installation and Maintenance of Games

This article describes a set of best practices that can help reduce user frustration about the time required to install a game, prevent unnecessary support calls, and allow users to start playing your game as quickly and painlessly as possible.

-   [Initial Installation](#initial-installation)
    -   [Streamlining the Installation UI](#streamlining-the-installation-ui)
    -   [Reducing the Time Required for Installation](#reducing-the-time-required-for-installation)
    -   [Minimal Installation](#minimal-installation)
    -   [Install on Demand](#install-on-demand)
-   [Post-Installation Game-Play](#post-installation-game-play)
    -   [AutoRun](#autorun)
    -   [Converting an Install-on-Demand Installation to a Full Installation](#converting-an-install-on-demand-installation-to-a-full-installation)
    -   [Maintenance of Game Software and Content](#maintenance-of-game-software-and-content)
    -   [Checking for Updates Automatically](#checking-for-updates-automatically)
    -   [Downloading Patches Automatically](#downloading-patches-automatically)
-   [Other Resources](#other-resources)
-   [Related topics](#related-topics)

## Initial Installation

Users buy games because they enjoy playing them, not because they enjoy installing them. Installing a game should be as quick, straightforward, and as painless as possible for the end user. Ideally, end users should not even see an installation UI; they should be able to just drop the game disc into the tray and begin playing.

### Streamlining the Installation UI

Common aspects of existing game installation UIs interfere with the desired end-user experience:

-   Asking the user unnecessary questions.

    For example, many games ask if the user wants to install DirectX. If the game requires Microsoft DirectX to run, and the right version of DirectX isn't installed already, the game should simply install DirectX.

-   Asking the user questions that a vast majority of users will answer in the same way.

    For typical users, the default settings for installation path, Start menu location, and so on, are all fine. Offer advanced options for users who want to change these settings.

The installation UI should be designed to allow the typical user to begin playing the game as soon as possible. If AutoRun is enabled on the user's computer, which is the default, the setup program should assume that the user wants to be playing the game as soon as possible, bypassing any unnecessary questions. The setup progra[Install on Demand](#install-on-demand)m should begin installing the game to the default installation path, preferably using a setup like that described in . It is appropriate to give users a chance to change the installation settings before automatically starting the installation. However, this should be accomplished by prompting the user to hit a key for advanced setup options, and then proceeding automatically with the default options if the user does not hit that key within five to ten seconds.

If AutoRun is not enabled on the user's computer, the setup program should assume that the user does not want the setup program to begin installing the game automatically. If the setup program is started by some means other than AutoRun, it should launch the advanced setup UI.

### Reducing the Time Required for Installation

Most Microsoft Windows games today take anywhere from five minutes to half an hour to finish the installation process. In contrast, most console games take no more than thirty seconds from the time the user inserts the game CD to the time the user can play the game. This difference is due to the fact that most Windows games are designed to run most, if not all, of their content from the computer's hard drive; consoles, which lack a place to permanently store large amounts of content, require that the content be run from the source media. While loading content from the local hard drive makes for faster in-game load times, the downside is that all of that content has to be copied from the source media to the hard drive at some point. Most Windows games choose to copy all of the content to the hard drive all at once, as part of an installation process. This detracts from the user's initial experience with the game by making the user watch a progress bar for several minutes before being able to play the game.

There are two approaches that can be used to minimize the time spent initially installing the game: [Minimal Installation](#minimal-installation) and [Install on Demand](#install-on-demand).

### Minimal Installation

In a minimal installation scenario, the game installs only a bare minimum set of content to the hard drive. Usually, this consists of only the game executable and DLLs. The remainder of the content is accessed directly from the source media. This drastically reduces the time required to install, since a game's executable is rarely larger than 10-20 MB. The drawback is that the game takes longer to load content during the game, since it must load it from the slower source media.

To create a minimal installation configuration in a Windows Installer-based setup:

-   Group all of the components to be installed to the hard drive into a feature that is marked to install locally.

    This feature will be referred to as the "Bootstrap" feature.

-   Group all of the components that are to be run from the source media into a feature that is marked as "run from source."
-   When opening a file that might be on the source media, use the [**MsiGetComponentPath**](/windows/desktop/api/msi/nf-msi-msigetcomponentpatha) function to determine the path to the file, instead of hard-coding the path.

    Doing so ensures that the file can be found even if the drive letter of the user's CD/DVD drive changes.

-   Compress content that stays on the CD/DVD.

    The amount of CPU time spent decompressing the content will usually be hidden by the slow transfer rate of data from the CD/DVD drive.

-   Group content into large, contiguous files and access it in sequential order.

    The seek times of CD/DVD drives are abysmal compared to those of hard drives, and most CD/DVD drives don't reach peak transfer rates unless they are reading a large, contiguous file.

-   Lay out content on the CD/DVD in the order that it is likely to be accessed.

    Seek times are greatly reduced when files are accessed in the same order as their on-disk layout.

### Install on Demand

In an install-on-demand scenario, as for minimal installation, the game initially installs to the hard drive only those files necessary to start the game. However, instead of accessing the remaining content from the source media every time it is needed, the game actually installs each piece of content to the hard drive as it is needed for the first time, and then accesses it from the local hard drive on each subsequent use. The time required for the initial installation is just as small as in for a minimal installation, but after the first time that each piece of content is accessed, the load times improve.

To create an install-on-demand configuration in a Windows Installer-based setup:

-   Group all of the components to be initially installed to the hard drive into a feature that is marked to install locally.

    Note that this is identical to the Bootstrap feature for a minimal installation.

-   Group the remaining content into multiple features based on components likely to be used together.

    For example, in a level-based game, group all the content used on a given level into one feature. Note that Windows Installer allows a component to be shared by multiple features, so if you have content that is used on multiple levels, you can add that content to the features for all of the necessary levels without replicating the content. All of these features should be marked as "Advertised", which means that they won't be installed initially, but can be installed later as needed.

-   When a file is needed, first check whether the file is already installed using the function [**MsiQueryFeatureState**](/windows/desktop/api/msi/nf-msi-msiqueryfeaturestatea).

    If it is not yet installed (that is, its state is INSTALLSTATE\_ADVERTISED), call the function [**MsiConfigureFeature**](/windows/desktop/api/msi/nf-msi-msiconfigurefeaturea) to install the feature locally. When opening the file after it is installed, call [**MsiGetComponentPath**](/windows/desktop/api/msi/nf-msi-msigetcomponentpatha) to determine the path to the file. While not strictly necessary for this scenario (since the content will always be installed to the hard drive before it is used), this makes it easier to support minimal installation in addition to installation on demand.

-   If possible, anticipate what content is likely to be needed soon, and install it in the background during idle time.

    Background installation is most appropriate when the game is at a point that doesn't need every last ounce of performance out of the computer; for example, while displaying an intro movie, cut-scene, menu, and so on.

-   Create an option in the game's options menu to force installation of all remaining content.

    To implement this, create a feature that is a parent of all of the install-on-demand features, and then call [**MsiConfigureFeature**](/windows/desktop/api/msi/nf-msi-msiconfigurefeaturea) to install this master feature locally. This will cause the subfeatures to be installed locally as well.

-   Content layout should be similar to that for a minimal installation, except that content should be clustered only with other content that is likely to be needed at the same time (for example, all of the content for one level should be together).

## Post-Installation Game-Play

### AutoRun

To play a game that is already installed, the user should only need to drop the installation disc in the drive tray. The first thing that the AutoRun executable on the disc should do is to check to see if the game has already been installed, and if so, launch the game. Assuming that the game was installed using a Windows Installer-based setup, the check to determine if the game is installed can be accomplished with a single call to the function [**MsiQueryProductState**](/windows/desktop/api/msi/nf-msi-msiqueryproductstatea).

### Converting an Install-on-Demand Installation to a Full Installation

While an install-on-demand installation allows the user to begin playing the game much sooner than a full installation, a user may want to explicitly install the remainder of the game content to the local hard drive. The user may want to be able to play the game without requiring the source media, or he or she may simply want to avoid the longer in-game load times that result from installing content on demand. If the game's setup uses Windows Installer, the game can provide an option in the in-game options UI to finish installing the remaining content. When the user selects this option, the game can call [**MsiConfigureFeature**](/windows/desktop/api/msi/nf-msi-msiconfigurefeaturea) to force the remaining features to be installed locally; there is no need to spawn a separate setup application to do so.

### Maintenance of Game Software and Content

One of the advantages that Windows games have over console games is the relative ease with which the publisher can release updates to the game after its initial release. Whether these updates introduce new content or just fix bugs, it is important to make the update process as easy as possible for the end user. The update process is even more important for online games, which typically require that all users are running the latest version of the game in order to connect.

### Checking for Updates Automatically

Users should not have to remember to go looking for patches. If there is an update available for the game, the user should at least be notified, and ideally, the patch should already be downloaded.

A simple way for a game to check for updates is to connect to a Web server hosted by the publisher using a specific URL, and download a text file that specifies the version number of the latest available version of the game, along with a URL from which to download a package that will update the game to the latest version.

Checking for updates each time that the user plays the game is adequate to make sure that the user is running the latest version. However, if the existence of a new update is discovered immediately before the user tries to play the game, the user may be forced to delay playing the game until the update has finished downloading. For large updates or slow connections, this delay may be on the order of hours. To avoid forcing the user to wait before playing the game, the game can use Task Scheduler to schedule periodic checks for new updates. If an update is detected, the game can begin downloading the update immediately, so that it is likely to be completely downloaded and ready to install by the next time the user plays the game.

### Downloading Patches Automatically

Once the game has detected that a new update is available, it should immediately begin downloading the update. Since the task that checks for updates is typically running silently in the background, the download needs to be as unobtrusive as possible. The Background Intelligent Transfer Service (BITS) is an operating system feature that allows applications to download files from the Internet even while the application itself is not running. BITS download jobs run only when the user is logged on, and only when the machine is already connected to the network. BITS will not attempt to force the machine to connect to the network on its own. If the user disconnects from the network, or logs off, the BITS job is paused, and will resume downloading the next time the user logs in and connects to the network. The application can configure its BITS jobs to use only network bandwidth that would otherwise remain unused, in order to prevent the job from impacting the performance of any other applications that might be using the network (for example, an online game). BITS is available on Windows XP and Windows 2000 Service Pack 3.

## Other Resources

For more information on the technologies referenced in this article, refer to the relevant sections of the MSDN Library:

-   [Windows Installer](/windows/desktop/Msi/windows-installer-portal)
-   [Task Scheduler](/windows/desktop/TaskSchd/task-scheduler-start-page)
-   [Background Intelligent Transfer Service](/windows/desktop/Bits/background-intelligent-transfer-service-portal) (BITS)

For more information on using Windows Installer for games, tune in to next month's Driving DirectX column, "Introduction to Windows Installer for Game Developers."

## Related topics

<dl> <dt>

[**MsiConfigureFeature**](/windows/desktop/api/msi/nf-msi-msiconfigurefeaturea)
</dt> <dt>

[**MsiQueryProductState**](/windows/desktop/api/msi/nf-msi-msiqueryproductstatea)
</dt> <dt>

[**MsiQueryFeatureState**](/windows/desktop/api/msi/nf-msi-msiqueryfeaturestatea)
</dt> <dt>

[**MsiGetComponentPath**](/windows/desktop/api/msi/nf-msi-msigetcomponentpatha)
</dt> </dl>

 

 
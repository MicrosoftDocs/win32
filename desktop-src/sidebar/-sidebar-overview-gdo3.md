---
title: Developing a Gadget for Windows Sidebar Part 3 Settings and Flyouts
description: The last of three overviews that describe how to create a basic gadget for the Windows Sidebar.
ms.assetid: 481ed853-e378-478b-bedd-e32096f82dbf
keywords:
- Windows Sidebar,creating gadgets
- Sidebar,creating gadgets
- gadgets,creating
- creating gadgets
- Windows Sidebar,examples
- Sidebar,examples
- gadgets,examples
- Windows Sidebar,Settings dialog
- Sidebar,Settings dialog
- gadgets,Settings dialog
- Windows Sidebar,Flyouts
- Sidebar,Flyouts
- gadgets,Flyouts
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Developing a Gadget for Windows Sidebar Part 3: Settings and Flyouts

\[ The Windows Gadget Platform/Sidebar is available for use in the following versions of Windows: Windows 7, Windows Vista, and Windows Server 2008. It may be altered or unavailable in subsequent versions. \]

The last of three overviews that describe how to create a basic gadget for the Windows Sidebar. In this overview, we explain the difference between **Settings** (or **Options** as specified in the gadget context menu) and **Flyout** functionality and demonstrate how to incorporate both into a gadget.

-   [Introduction](#introduction)
-   [The Settings Dialog](#the-settings-dialog)
-   [The Flyout](#the-flyout)
-   [For Further Reference](#for-further-reference)

## Introduction

The gadget object model defines two UI extensions to the basic gadget UI. The gadget's Settings dialog ([**System.Gadget.Settings**](system-gadget-settings.md)) enables a user to make configuration changes to a gadget while the gadget's Flyout ([**System.Gadget.Flyout**](system-gadget-flyout.md)) enables a user to view additional detail or information about a gadget UI.

## The Settings Dialog

Settings functionality is exposed by the [**System.Gadget.Settings**](system-gadget-settings.md) and [**System.Gadget.Settings.ClosingEvent**](system-gadget-settings-closingevent.md) scripting elements. The Settings dialog possesses its own Document Object Model (DOM) and requires its own HTML file (specified by assigning the path of an HTML file to the [**settingsUI**](system-gadget-settingsui.md) property), Microsoft JScript, and other supporting files.

The following example demonstrates how the [**settingsUI**](system-gadget-settingsui.md) property is used to enable the Settings dialog for a gadget.


```
// Enable Settings dialog for the gadget. 
System.Gadget.settingsUI = "Example.html";
```



Assigning a value to the [**settingsUI**](system-gadget-settingsui.md) property results in the display of the Settings icon (a "wrench") that appears when the mouse pointer hovers over the gadget or the gadget has focus. The following screen shot shows a gadget with the Settings icon.

![example of a gadget settings icon](images/basic/settings1.png)

Clicking the Settings icon or selecting **Options** from the gadget context menu displays the Settings dialog as shown in the following screen shot.

![example of a gadget settings dialog](images/basic/settings2.png)

The primary purpose of the Settings dialog is to allow the user to select and modify gadget configuration values (or settings). These values are persistent for the entire session of a particular gadget and unique for each gadget instance. For example, the Settings dialog for a stock tracking gadget can provide a user with the ability to specify a data provider as well as various display preferences.

A Settings value is stored by using [**write**](system-gadget-settings-write.md) or [**writeString**](system-gadget-settings-writestring.md) with a key/value pair. A Settings value is retrieved by using [**read**](system-gadget-settings-read.md) or [**readString**](system-gadget-settings-readstring.md) with the key declared when the value was stored. There is a 1024 character limit for Settings keys and a 2048 character limit for Settings values; values longer than these limits will be truncated.

> [!Note]  
> To limit type conversion errors, the use of [**writeString**](system-gadget-settings-writestring.md) and [**readString**](system-gadget-settings-readstring.md) is recommended.

 

The following example demonstrates how to store a Settings value when the user clicks **OK** in the Settings dialog.


```
// Delegate for the settings closing event. 
System.Gadget.onSettingsClosing = SettingsClosing;

// --------------------------------------------------------------------
// Handle the Settings dialog closing event.
// Parameters:
// event - event arguments.
// --------------------------------------------------------------------
function SettingsClosing(event)
{
    // Save the settings if the user clicked OK.
    if (event.closeAction == event.Action.commit)
    {
        System.Gadget.Settings.write(
            "settingsSelectionIndex", selUserEntry.selectedIndex);
    }
    // Allow the Settings dialog to close.
    event.cancel = false;
}
```



The following example demonstrates how to read values from controls in the Settings dialog.


```
var userEntry = "";

System.Gadget.onSettingsClosed = SettingsClosed;

// --------------------------------------------------------------------
// Handle the Settings dialog closed event.
// event = System.Gadget.Settings.ClosingEvent argument.
// --------------------------------------------------------------------
function SettingsClosed(event)
{
    // User hits OK on the settings page.
    if (event.closeAction == event.Action.commit)
    {
        userEntry = 
            System.Gadget.Settings.readString("settingsUserEntry");
        SetContentText(userEntry);
    }
    // User hits Cancel on the settings page.
    else if (event.closeAction == event.Action.cancel)
    {
        SetContentText("canceled");
    }
}
```



> [!Note]  
> A Settings dialog is modal and does not disappear if it or the parent gadget loses focus. The user must select **Ok** or **Cancel** to dismiss the dialog.

 

## The Flyout

Flyout functionality is exposed by the [**System.Gadget.Flyout**](system-gadget-flyout.md) scripting element. Flyouts also require their own HTML and JScript files and, as such, possess their own DOM. Communication between the Flyout and the main gadget can be accomplished through the use of the parentWindow property of the [**System.Gadget.document**](system-gadget-document.md) and [**System.Gadget.Flyout.document**](system-gadget-flyout-document.md) objects. The Flyout file is specified by setting System.Gadget.Flyout.file to the path of an HTML file.

> [!Note]  
> Since a Flyout can disappear at any time, unpredictable behavior or errors may result from attempting to communicate with a Flyout from the main gadget.

 

The following example demonstrates how to set the gadget Flyout UI from the gadget script file and listen for the Flyout events.


```
var oGadgetDocument = System.Gadget.document;
System.Gadget.Flyout.onShow = showFlyout;
System.Gadget.Flyout.onHide = hideFlyout;

// --------------------------------------------------------------------
// Initialize the gadget.
// --------------------------------------------------------------------
function Init()
{
    // Specify the Flyout root.
    System.Gadget.Flyout.file = "example.html";
    
    // Initialize the Flyout state display.
    if (!System.Gadget.Flyout.show)
    {
        sFlyoutFeedback.innerText = "Flyout hidden.";
    }
}

// --------------------------------------------------------------------
// Display the Flyout state in the gadget.
// --------------------------------------------------------------------
function showFlyout()
{
    oGadgetDocument.getElementById("strFlyoutFeedback").innerText = "Flyout visible.";
}

// --------------------------------------------------------------------
// Hide the flyout and display the Flyout state in the gadget.
// --------------------------------------------------------------------
function hideFlyout()
{
    oGadgetDocument.getElementById("strFlyoutFeedback").innerText = "Flyout hidden.";
    System.Gadget.Flyout.show = false;
}
```



A Flyout is typically spawned on an event in the main gadget UI such as a mouseover or click; setting [**show**](system-gadget-flyout-show.md) to true displays the Flyout and false hides the Flyout. This state should be queried before any communication is attempted. Flyouts can be used to display anything but are generally used to display more detail or information about the event target.

The Flyout location is determined by the user's display, the position of the gadget, the size of the Flyout (which has no intrinsic limit), and the location of the Sidebar should the gadget be docked. For example, the Flyout could be displayed to the left or right, above or below the gadget.

The following image shows a gadget Flyout that displays stock ticker details.

![example of a gadget flyout](images/basic/flyout.png)

The following image shows a gadget Flyout that allows a user to select stock symbols of interest.

![example of a gadget flyout](images/basic/flyout2.png)

> [!Note]  
> A Flyout closes when it loses focus. As a result, only one Flyout can be displayed at any time.

 

## For Further Reference

[Developing a Gadget for Windows Sidebar Part 1: The Basics](-sidebar-overview-gdo.md)

[Developing a Gadget for Windows Sidebar Part 2: The G:BACKGROUND, G:IMAGE, G:TEXT Presentation Elements and GIMAGE Protocol](-sidebar-overview-gdo2.md)

For Windows Vista User Experience Guidelines, see [Windows Vista User Experience Guidelines for the Sidebar](http://msdn.microsoft.com/library/aa974179.aspx)

To read posts from the Sidebar team, including gadget authoring tips, links to gadget information, and news about the platform, see the [Gadget Corner blog](http://blogs.msdn.com/sidebar/default.aspx).

To participate in developer community discussions on writing gadgets for the Sidebar, see the [Sidebar Gadget Development forum](http://go.microsoft.com/fwlink/p/?linkid=142587).

 

 





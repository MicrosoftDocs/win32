---
description: Discusses new taskbar functionality, including consolidation of launching and switching, enhanced capabilities of taskbar buttons such as single-click access to documents and application-specific tasks, transport controls and status notifications, thumbnail representations and switch targets based on individual tabs in a tabbed application, and the ability to reorder taskbar buttons through a drag-and-drop operation.
ms.assetid: cbf2b07d-d67c-4755-888c-d40692d13cae
title: Taskbar Extensions
ms.topic: article
ms.date: 11/21/2021
---

# Taskbar Extensions

As of Windows 11, the taskbar has been extended significantly under the guiding principle of getting users where they're going as quickly and efficiently as possible. To that end, the application windows, files, and commands that the user needs to accomplish that are now centralized into a single taskbar button that consolidates previously scattered information sources and controls. A user can now find common tasks, recent and frequent files, alerts, progress notifications, and thumbnails for individual documents or tabs all in one place.

- [Unified Launching and Switching](#unified-launching-and-switching)
- [Jump Lists](#jump-lists)
- [Destinations](#destinations)
- [Tasks](#tasks)
- [Customizing Jump Lists](#customizing-jump-lists)
- [Thumbnail Toolbars](#thumbnail-toolbars)
- [Icon Overlays](#icon-overlays)
- [Progress Bars](#progress-bars)
- [Deskbands](#deskbands)
- [Notification Area](#notification-area)
- [Thumbnails](#thumbnails)
- [Related topics](#related-topics)

## Unified Launching and Switching

As of the Windows 7 and newer taskbar, Quick Launch is no longer a separate toolbar. The launcher shortcuts that Quick Launch typically contained are now pinned to the taskbar itself, mingled with buttons for currently running applications. When a user starts an application from a pinned launcher shortcut, the icon transforms into the application's taskbar button for as long as the application is running. When the user closes the application, the button reverts to the icon. However, both the launcher shortcut and the button for the running application are just different forms of the Windows 7 and newer taskbar button.

![windows 11 taskbar](images/taskbar/taskbar.png)

A small set of applications are pinned by default for new installations. Other than these, only the user can pin further applications; programmatic pinning by an application is not permitted.

The Show Desktop feature from Quick Launch is now located at the taskbar's far right. Hovering over this area causes all active windows to become transparent, showing the desktop. Clicking the area executes the familiar action of minimizing all windows and switching to the desktop.

While the application is running, its taskbar button becomes the single place to access all of the following features, each discussed in detail below.

- [Tasks](#tasks): common application commands, present even when the application is not running.
- [Destinations](#destinations): recently and frequently accessed files specific to the application.
- [Thumbnails](#thumbnails): window switching, including switch targets for individual tabs and documents.
- [Thumbnail Toolbars](#thumbnail-toolbars): basic application control from the thumbnail itself.
- [Progress Bars](#progress-bars) and [Icon Overlays](#icon-overlays): status notifications.

The taskbar button can represent a launcher, a single application window, or a group. An identifier known as an Application User Model ID (AppUserModelID) is assigned to each group. An AppUserModelID can be specified to override standard taskbar grouping, which allows windows to become members of the same group when they might not otherwise be seen as such. Each member of a group is given a separate preview in the thumbnail flyout that is shown when the mouse hovers over the group's taskbar button. Note that grouping itself remains optional.

As of Windows 7 and newer, taskbar buttons can now be rearranged by the user through drag-and-drop operations.

> [!Note]  
> The Quick Launch folder ([****FOLDERID\_QuickLaunch****](knownfolderid.md)) is still available for backward compatibility although there is no longer a Quick Launch UI. However, new applications should not ask to add an icon to Quick Launch during installation.

 

For more information, see [Application User Model IDs (AppUserModelIDs)](appids.md).

## Jump Lists

A user typically launches a program with the intention of accessing a document or performing tasks within the program. The user of a game program might want to get to a saved game or launch as a specific character rather than restart a game from the beginning. To get users more efficiently to their final goal, a list of [destinations](#destinations) and common [tasks](#tasks) associated with an application is attached to that application's taskbar button (as well as to the equivalent **Start** menu entry). This is the application's Jump List. The Jump List is available whether the taskbar button is in a launcher state (the application isn't running) or whether it represents one or more windows. Right-clicking the taskbar button shows the application's Jump List, as shown in the following illustration.

![jump list with pinned, frequent, and tasks categories](images/taskbar/jumplist.png)

By default, a standard Jump List contains two categories: recent items and pinned items, although because only categories with content are shown in the UI, neither of these categories are shown on first launch. Always present are an application launch icon (to launch more instances of the application), an option to pin or unpin the application from the taskbar, and a **Close** command for any open windows.

## Destinations

The **Recent** and **Frequent** categories are considered to contain destinations. A destination, usually a file, document, or URL, is something that can be edited, browsed, viewed, and so on. Think of a destination as a thing rather than an action. Typically, a destination is an item in the Shell namespace, represented by an [**IShellItem**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ishellitem) or [**IShellLink**](/windows/desktop/api/Shobjidl_core/nn-shobjidl_core-ishelllinka). These portions of the destination list are analogous to the **Start** menu's recently used documents list (no longer shown by default) and frequently used application list, but they are specific to an application and therefore more accurate and useful to the user. The results used in the destination list are calculated through calls to [**SHAddToRecentDocs**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shaddtorecentdocs). Note that when the user opens a file from Windows Explorer or uses the common file dialog to open, save, or create a file, **SHAddToRecentDocs** is called for you automatically, which results in many applications getting their recent items shown in the destination list without any action on their part.

Launching a destination is much like launching an item using the **Open With** command. The application launches with that destination loaded and ready to use. Items in the destination list can also be dragged from the list to a drop destination such as an email message. By having these items centralized in a destination list, it gets users where they want to go that much faster, which is the goal.

As items appear in a destination list's **Recent** category (or the **Frequent** category or a [custom category](#customizing-jump-lists) as discussed in a later section), a user might want to ensure that the item is always in the list for quick access. To accomplish this, he or she can pin that item to the list, which adds the item to the **Pinned** category. When a user is actively working with a destination, he or she wants it easily at hand and so would pin it to the application's destination list. After the user's work there is done, he or she simply unpins the item. This user control keeps the list uncluttered and relevant.

A destination list can be regarded as an application-specific version of the **Start** menu. A destination list is not a shortcut menu. Each item in a destination list can be right-clicked for its own shortcut menu.

### APIs

- [**IApplicationDestinations::RemoveDestination**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iapplicationdestinations-removedestination)
- [**IApplicationDestinations::RemoveAllDestinations**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iapplicationdestinations-removealldestinations)
- [**IApplicationDocumentLists::GetList**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-iapplicationdocumentlists-getlist)
- [**SHAddToRecentDocs**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shaddtorecentdocs)

## Tasks

Another built-in portion of a Jump List is the **Tasks** category. While a destination is a thing, a task is an action, and in this case it is an application-specific action. Put another way, a destination is a noun and a task is a verb. Typically, tasks are [**IShellLink**](/windows/desktop/api/Shobjidl_core/nn-shobjidl_core-ishelllinka) items with command-line arguments that indicate particular functionality that can be triggered by an application. Again, the idea is to centralize as much information related to an application as is practical.

Applications define tasks based on both the program's features and the key things a user is expected to do with them. Tasks should be context-free, in that the application does not need to be running for them to work. They should also be the statistically most common actions that a normal user would perform in an application, such as compose an email message or open the calendar in a mail program, create a new document in a word processor, launch an application in a certain mode, or launch one of its subcommands. An application should not clutter the menu with advanced features that standard users won't need or one-time actions such as registration. Do not use tasks for promotional items such as upgrades or special offers.

It is strongly recommended that the task list be static. It should remain the same regardless of the state or status of the application. While it is possible to vary the list dynamically, you should consider that this could confuse the user who does not expect that portion of the destination list to change.

### APIs

- [**ICustomDestinationList::AddUserTasks**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-icustomdestinationlist-addusertasks)

## Customizing Jump Lists

An application can define its own categories and add them in addition to or in place of the standard **Recent** and **Frequent** categories in a Jump List. The application can control its own destinations in those custom categories based on the application's architecture and intended use. The following screen shot shows a Custom Jump List with a History category.

![custom jump list](images/taskbar/customjumplist.png)

If an application decides to provide a custom category, that application assumes responsibility for populating it. The category contents should still be user-specific and based on user history, actions, or both, but through a custom category an application can determine what it wants to track and what it wants to ignore, perhaps based on an application option. For example, an audio program might elect to include only recently played albums and ignore recently played individual tracks.

If a user has removed an item from the list, which is always a user option, the application must honor that. The application must also ensure that items in the list are valid or that they fail gracefully if they have been deleted. Individual items or the entire contents of the list can be programmatically removed.

The maximum number of items in a destination list is determined by the system based on various factors such as display resolution and font size. If there isn't space enough for all items in all categories, they are truncated from the bottom up.

### APIs

- [**ICustomDestinationList**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-icustomdestinationlist)
- [**IApplicationDestinations**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iapplicationdestinations)
- [**IApplicationDocumentLists**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iapplicationdocumentlists)

## Thumbnail Toolbars

To provide access to a particular window's key commands without making the user restore or activate the application's window, an active toolbar control can be embedded in that window's thumbnail preview. For example, Windows Media Player might offer standard media transport controls such as play, pause, mute, and stop. The UI displays this toolbar directly below the thumbnail as shown in the following illustration—it does not cover any part of it.

![thumbnail taskbar for windows media player, with three buttons: back, play, and forward](images/taskbar/thumbbar.png)

This toolbar is simply the familiar standard toolbar common control. It has a maximum of seven buttons. Each button's ID, image, tooltip, and state are defined in a structure, which is then passed to the taskbar. The application can show, enable, disable, or hide buttons from the thumbnail toolbar as required by its current state.

Because there is limited room to display thumbnails and a variable number of thumbnails to display, applications are not guaranteed a given toolbar size. If space is restricted, buttons in the toolbar are truncated from right to left. Therefore, when you design your toolbar, you should prioritize the commands associated with your buttons and ensure that the most important come first and are least likely to be dropped because of space issues.

> [!Note]  
> When an application displays a window, its taskbar button is created by the system. When the button is in place, the taskbar sends a **TaskbarButtonCreated** message to the window. Its value is computed by calling [**RegisterWindowMessage**](/windows/win32/api/winuser/nf-winuser-registerwindowmessagea)(L("TaskbarButtonCreated")). That message must be received by your application before it calls any [**ITaskbarList3**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-itaskbarlist3) method.

 

### API

- [**ITaskbarList3::ThumbBarAddButtons**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-itaskbarlist3-thumbbaraddbuttons)
- [**ITaskbarList3::ThumbBarSetImageList**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-itaskbarlist3-thumbbarsetimagelist)
- [**ITaskbarList3::ThumbBarUpdateButtons**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-itaskbarlist3-thumbbarupdatebuttons)
- [**THUMBBUTTON**](/windows/desktop/api/Shobjidl_core/ns-shobjidl_core-thumbbutton)

## Icon Overlays

An application can communicate certain notifications and status to the user through its taskbar button by the display of small overlays on the button. These overlays are similar to the type of existing overlay used for shortcuts or security notifications, displayed at the lower-right corner of the button. To display an overlay icon, the taskbar must be in the default large icon mode, as shown in the following screen shot.

![windows messenger taskbar button with an overlay to indicate an available status](images/taskbar/taskbaroverlay.png)

Icon overlays serve as a contextual notification of status, and are intended to negate the need for a separate notification area status icon to communicate that information to the user. For instance, the new mail status in Microsoft Outlook, currently shown in the notification area, can now be indicated through an overlay on the taskbar button. Again, you must decide during your development cycle which method is best for your application. Overlay icons are intended to supply important, long-standing status or notifications such as network status, messenger status, or new mail. The user should not be presented with constantly changing overlays or animations.

Because a single overlay is overlaid on the taskbar button and not on the individual window thumbnails, this is a per-group feature rather than per-window. Requests for overlay icons can be received from individual windows in a taskbar group, but they do not queue. The last overlay received is the overlay shown.

### APIs

- [**ITaskbarList3::SetOverlayIcon**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-itaskbarlist3-setoverlayicon)

## Progress Bars

A taskbar button can be used to display a progress bar. This enables a window to provide progress information to the user without that user having to switch to the window itself. The user can stay productive in another application while seeing at a glance the progress of one or more operations occurring in other windows. It is intended that a progress bar in a taskbar button reflects a more detailed progress indicator in the window itself. This feature can be used to track file copies, downloads, installations, media burning, or any operation that's going to take a period of time. This feature is not intended for use with normally peripheral actions such as the loading of a webpage or the printing of a document. That type of progress should continue to be shown in a window's status bar.

The taskbar button progress bar is a similar experience to the familiar Progress Bar control. It can display either determinate progress based on a completed percentage of the operation or an indeterminate marquee-style progress to indicate that the operation is in progress without any prediction of time remaining. It can also show that the operation is paused or has encountered an error and requires user intervention.

### APIs

- [**ITaskbarList3::SetProgressState**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-itaskbarlist3-setprogressstate)
- [**ITaskbarList3::SetProgressValue**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-itaskbarlist3-setprogressvalue)

## Deskbands

> [!Note]  
> In Windows 11 deskbands are no loger supported.

In versions of Windows prior to Windows 7, something similar to thumbnail toolbar functionality could be achieved through a deskband—a toolbar hosted in the taskbar. For instance, Windows Media Player could minimize to the taskbar as a set of transport controls rather than a standard button. In Windows 7 and newer, deskbands can still be implemented and thumbnail toolbars are not intended to replace them all. Not all applications will lend themselves to a thumbnail toolbar, and another solution such as a deskband or a task in a destination list might be the right answer for your application; you must decide which solution works best for your application as part of your development cycle. However, be aware that deskbands must support Windows Aero with translucency ("glass") enabled and the [**IDeskBand2**](/windows/desktop/api/Shobjidl/nn-shobjidl-ideskband2) interface.

### APIs

- [**IDeskBand2**](/windows/desktop/api/Shobjidl/nn-shobjidl-ideskband2)

## Notification Area

There have been changes to the notification area that give the user much more control over what icons appear on the taskbar. All notification icons are now hidden by default and that visibility cannot be programmatically controlled. Only the user is allowed to choose which notification icons appear on the taskbar. When a notification balloon is displayed, the icon becomes temporarily visible, but even then a user can choose to silence them. An icon overlay on a taskbar button therefore becomes an attractive choice when you want your application to communicate that information to your users.

## Thumbnails

In Windows Vista, hovering over an application's taskbar button displays a thumbnail that represents the running window. If the taskbar has collapsed the application's windows, the thumbnail represents this by appearing as a stack, but only the active window is shown in the thumbnail itself.

In Windows 7 and newer, each member of a group is shown as a separate thumbnail and is now also a switch target. An application can define its children (such as true child windows, individual documents, or tabs) and provide corresponding thumbnails for each of those windows even when they would not normally appear in the taskbar. This enables users to switch directly into the view of the application that they want rather than switching into the application and then switching to their destination. For example, multiple-document interface (MDI)/tabbed-document interface (TDI)applications can have each document or tab displayed as a separate thumbnail and switch target when the mouse hovers over a group's taskbar button.

![two taskbar thumbnails that represent individual tabs in Microsoft Edge](images/taskbar/taskbarthumbnails.png)

> [!Note]  
> As in Windows Vista, Aero must be active to view thumbnails.

 

### API

- [**ITaskbarList3::RegisterTab**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-itaskbarlist3-registertab)
- [**ITaskbarList3::SetTabActive**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-itaskbarlist3-settabactive)
- [**ITaskbarList3::SetTabOrder**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-itaskbarlist3-settaborder)
- [**ITaskbarList3::UnregisterTab**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-itaskbarlist3-unregistertab)
- [**ITaskbarList4::SetTabProperties**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-itaskbarlist4-settabproperties)

Thumbnail representations for windows are normally automatic, but in cases where the result isn't optimal, the thumbnail can be explicitly specified. By default, only top-level windows have a thumbnail automatically generated for them, and the thumbnails for child windows appear as a generic representation. This can result in a less than ideal (and even confusing) experience for the end user. A specific switch target thumbnail for each child window, for instance, provides a much better user experience.

### API

- [**DwmSetWindowAttribute**](/windows/win32/api/dwmapi/nf-dwmapi-dwmsetwindowattribute)
- [**DwmSetIconicThumbnail**](/windows/win32/api/dwmapi/nf-dwmapi-dwmseticonicthumbnail)
- [**DwmSetIconicLivePreviewBitmap**](/windows/win32/api/dwmapi/nf-dwmapi-dwmseticoniclivepreviewbitmap)
- [**DwmInvalidateIconicBitmaps**](/windows/win32/api/dwmapi/nf-dwmapi-dwminvalidateiconicbitmaps)
- [**WM\_DWMSENDICONICTHUMBNAIL**](../dwm/wm-dwmsendiconicthumbnail.md)
- [**WM\_DWMSENDICONICLIVEPREVIEWBITMAP**](../dwm/wm-dwmsendiconiclivepreviewbitmap.md)

You can select a particular area of the window to use as the thumbnail. This can be useful when an application knows that its documents or tabs will appear similar when viewed at thumbnail size. The application can then choose to show just the part of its client area that the user can use to distinguish between thumbnails. However, hovering over any thumbnail brings up a view of the full window behind it so the user can quickly glance through them as well.

If there are more thumbnails than can be displayed, the preview reverts to the legacy thumbnail or a standard icon.

### API

- [**ITaskbarList3::SetThumbnailClip**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-itaskbarlist3-setthumbnailclip)

To add **Pin to Taskbar** to an item's shortcut menu, which is normally required only for file types that include the [IsShortCut](./links.md) entry, is done by registering the appropriate context menu handler. This also applies to **Pin to Start Menu**. See [Registering Shell Extension Handlers](reg-shell-exts.md) for more information.

## Related topics

<dl> <dt>

[The Taskbar](taskbar.md)
</dt> <dt>

[Application User Model IDs (AppUserModelIDs)](appids.md)
</dt> <dt>

[Notifications and the Notification Area](notification-area.md)
</dt> </dl>

 

 

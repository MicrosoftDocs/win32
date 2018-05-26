---
title: Media Transport Controls
description: .
ms.assetid: 64b3e8c7-54ea-4ac1-baa9-0eda7ed79458
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Media Transport Controls

## Purpose

Windows provides a built-in interface that shows the user information about the currently playing media such as the title of a song or video. It also provides the user with a common and familiar way to control media playback. Windows Runtime apps can integrate with the system media transport controls with the [**SystemMediaTransportControls**](https://msdn.microsoft.com/library/windows/apps/dn278677) class. Windows desktop applications can integrate with the system media transport controls by using the [**ISystemMediaTransportControls**](isystemmediatransportcontrols.md) interface.

## In this section



| Topic                                                                                                                             | Description                                                                                                                                                                    |
|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IImageDisplayProperties**](iimagedisplayproperties.md)<br/>                                                             | Provides properties for image information that is displayed by [**ISystemMediaTransportControlsDisplayUpdater**](isystemmediatransportcontrolsdisplayupdater.md). <br/> |
| [**IMusicDisplayProperties**](imusicdisplayproperties.md)<br/>                                                             | Provides properties for music information that is displayed by [**ISystemMediaTransportControlsDisplayUpdater**](isystemmediatransportcontrolsdisplayupdater.md). <br/> |
| [**ISystemMediaTransportControls**](isystemmediatransportcontrols.md)<br/>                                                 | Represents an object that enables integrate with the system media transport controls and support for media commands. <br/>                                               |
| [**ISystemMediaTransportControlsButtonPressedEventArgs**](isystemmediatransportcontrolsbuttonpressedeventargs.md)<br/>     | Provides data for the [**ButtonPressed**](https://msdn.microsoft.com/library/windows/apps/dn278706) event. <br/>                                                               |
| [**ISystemMediaTransportControlsDisplayUpdater**](isystemmediatransportcontrolsdisplayupdater.md)<br/>                     | Provides functionality to update the media metadata that is displayed on the [**ISystemMediaTransportControls**](isystemmediatransportcontrols.md).<br/>                |
| [**ISystemMediaTransportControlsInterop**](/windows/previous-versions/systemmediatransportcontrolsinterop/nn-systemmediatransportcontrolsinterop-isystemmediatransportcontrolsinterop?branch=master)<br/>                                   | Allows an app to get an instance of the [**ISystemMediaTransportControls**](isystemmediatransportcontrols.md) interface.<br/>                                           |
| [**ISystemMediaTransportControlsPropertyChangedEventArgs**](isystemmediatransportcontrolspropertychangedeventargs.md)<br/> | Provides data for the [**PropertyChanged**](https://msdn.microsoft.com/library/windows/apps/dn278720) event. <br/>                                                           |
| [**IVideoDisplayProperties**](ivideodisplayproperties.md)<br/>                                                             | Provides properties for video information that is displayed by [**ISystemMediaTransportControlsDisplayUpdater**](isystemmediatransportcontrolsdisplayupdater.md). <br/> |



 

## Developer audience

Media Transport Controls is designed for use by...

 

 






---
title: ISystemMediaTransportControls interface
description: Represents an object that enables integrate with the system media transport controls and support for media commands.
ms.assetid: '0D3FD8BA-ABEF-4FCC-AE3F-EC035007BC07'
keywords: ["ISystemMediaTransportControls interface", "ISystemMediaTransportControls interface, described"]
topic_type:
- apiref
api_name:
- ISystemMediaTransportControls
api_location:
- Windows.Media.SystemMediaTransportControls.h
api_type:
- COM
---

# ISystemMediaTransportControls interface

Represents an object that enables integrate with the system media transport controls and support for media commands.

## Members

The **ISystemMediaTransportControls** interface inherits from [**IInspectable**](https://msdn.microsoft.com/library/windows/desktop/br205821). **ISystemMediaTransportControls** also has these types of members:

-   [Methods](#methods)

### Methods

The **ISystemMediaTransportControls** interface has these methods.



| Method                                                                                                 | Description                                                                                                                                                                                                   |
|:-------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**add\_ButtonPressed**](https://msdn.microsoft.com/library/windows/desktop/dn892319)               | Adds an event handler for the [**ButtonPressed**](https://msdn.microsoft.com/library/windows/apps/dn278706) event. <br/>                                                                                      |
| [**add\_PropertyChanged**](https://msdn.microsoft.com/library/windows/desktop/dn892320)           | Adds an event handler for the [**PropertyChanged**](https://msdn.microsoft.com/library/windows/apps/dn278720) event.<br/>                                                                                   |
| [**get\_DisplayUpdater**](https://msdn.microsoft.com/library/windows/desktop/dn892321)             | Gets the display updater for the [**ISystemMediaTransportControls**](winrt-isystemmediatransportcontrols) which enables updating the information displayed about the currently playing media item.<br/> |
| [**get\_IsChannelDownEnabled**](https://msdn.microsoft.com/library/windows/desktop/dn892322) | Gets a value that indicates if the channel down button is enabled.<br/>                                                                                                                                 |
| [**get\_IsChannelUpEnabled**](https://msdn.microsoft.com/library/windows/desktop/dn892323)     | Gets a value that indicates if the channel up button is enabled.<br/>                                                                                                                                   |
| [**get\_IsEnabled**](https://msdn.microsoft.com/library/windows/desktop/dn892324)                       | Gets a value that indicates if the system media transport controls are enabled for the calling app.<br/>                                                                                                |
| [**get\_IsFastForwardEnabled**](https://msdn.microsoft.com/library/windows/desktop/dn892325) | Gets a value that indicates if the fast forward button is enabled.<br/>                                                                                                                                 |
| [**get\_IsNextEnabled**](https://msdn.microsoft.com/library/windows/desktop/dn892326)               | Gets a value that indicates if the next button is enabled.<br/>                                                                                                                                         |
| [**get\_IsPauseEnabled**](https://msdn.microsoft.com/library/windows/desktop/dn892327)             | Gets a value that indicates if the pause button is enabled.<br/>                                                                                                                                        |
| [**get\_IsPlayEnabled**](https://msdn.microsoft.com/library/windows/desktop/dn892328)               | Gets a value that indicates if the play button is enabled.<br/>                                                                                                                                         |
| [**get\_IsPreviousEnabled**](https://msdn.microsoft.com/library/windows/desktop/dn892329)       | Gets a value that indicates if the previous button is enabled.<br/>                                                                                                                                     |
| [**get\_IsRecordEnabled**](https://msdn.microsoft.com/library/windows/desktop/dn892330)           | Gets a value that indicates if the record button is enabled.<br/>                                                                                                                                       |
| [**get\_IsRewindEnabled**](https://msdn.microsoft.com/library/windows/desktop/dn892331)           | Gets a value that indicates if the rewind button is enabled.<br/>                                                                                                                                       |
| [**get\_IsStopEnabled**](https://msdn.microsoft.com/library/windows/desktop/dn892332)               | Gets a value that indicates if the stop button is enabled.<br/>                                                                                                                                         |
| [**get\_PlaybackStatus**](https://msdn.microsoft.com/library/windows/desktop/dn892334)             | Gets the media playback status.<br/>                                                                                                                                                                    |
| [**get\_SoundLevel**](https://msdn.microsoft.com/library/windows/desktop/dn892335)                     | Gets the sound level of the media for the capture and render streams.<br/>                                                                                                                              |
| [**put\_IsChannelDownEnabled**](https://msdn.microsoft.com/library/windows/desktop/dn892336) | Sets a value that specifies if the channel down button should be enabled.<br/>                                                                                                                          |
| [**put\_IsChannelUpEnabled**](https://msdn.microsoft.com/library/windows/desktop/dn892337)     | Sets a value that specifies if the channel up button should be enabled.<br/>                                                                                                                            |
| [**put\_IsEnabled**](https://msdn.microsoft.com/library/windows/desktop/dn892338)                       | Sets a value that specifies if the system media transport controls should be enabled for the calling app.<br/>                                                                                          |
| [**put\_IsFastForwardEnabled**](https://msdn.microsoft.com/library/windows/desktop/dn892339) | Sets a value that specifies if the fast forward button should be enabled.<br/>                                                                                                                          |
| [**put\_IsNextEnabled**](https://msdn.microsoft.com/library/windows/desktop/dn892340)               | Sets a value that specifies if the fast next button should be enabled.<br/>                                                                                                                             |
| [**put\_IsPauseEnabled**](https://msdn.microsoft.com/library/windows/desktop/dn892341)             | Sets a value that specifies if the pause button should be enabled.<br/>                                                                                                                                 |
| [**put\_IsPlayEnabled**](https://msdn.microsoft.com/library/windows/desktop/dn892342)               | Sets a value that specifies if the play button should be enabled.<br/>                                                                                                                                  |
| [**put\_IsPreviousEnabled**](https://msdn.microsoft.com/library/windows/desktop/dn892343)       | Sets a value that specifies if the previous button should be enabled.<br/>                                                                                                                              |
| [**put\_IsRecordEnabled**](https://msdn.microsoft.com/library/windows/desktop/dn892344)           | Sets a value that specifies if the record button should be enabled.<br/>                                                                                                                                |
| [**put\_IsRewindEnabled**](https://msdn.microsoft.com/library/windows/desktop/dn892345)           | Sets a value that specifies if the rewind button should be enabled.<br/>                                                                                                                                |
| [**put\_IsStopEnabled**](https://msdn.microsoft.com/library/windows/desktop/dn892346)               | Sets a value that specifies if the stop button should be enabled.<br/>                                                                                                                                  |
| [**put\_PlaybackStatus**](https://msdn.microsoft.com/library/windows/desktop/dn892347)             | Sets the media playback status.<br/>                                                                                                                                                                    |
| [**remove\_ButtonPressed**](https://msdn.microsoft.com/library/windows/desktop/dn892348)         | Removes the specified event handler for the [**ButtonPressed**](https://msdn.microsoft.com/library/windows/apps/dn278706) event.<br/>                                                                         |
| [**remove\_PropertyChanged**](https://msdn.microsoft.com/library/windows/desktop/dn892349)     | Removes the specified event handler for the [**PropertyChanged**](https://msdn.microsoft.com/library/windows/apps/dn278720) event.<br/>                                                                     |



 

## Remarks

Get an instance of this interface by calling [**ISystemMediaTransportControlsInterop::GetForWindow**](isystemmediatransportcontrolsinterop-getforwindow.md) and passing in the **HWND** for the top-level window of your app.

## Requirements



|                                     |                                                                                                                           |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                                                      |
| Header<br/>                   | <dl> <dt>Windows.Media.SystemMediaTransportControls.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Windows.Media.SystemMediaTransportControls.idl</dt> </dl> |



## See also

<dl> <dt>

[**IInspectable**](https://msdn.microsoft.com/library/windows/desktop/br205821)
</dt> </dl>

 

 






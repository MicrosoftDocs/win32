---
title: ISystemMediaTransportControlsDisplayUpdater interface
description: Provides functionality to update the media metadata that is displayed on the ISystemMediaTransportControls.
ms.assetid: 17BB2465-D9FA-4508-B7F9-94FA0D72FFCC
keywords:
- ISystemMediaTransportControlsDisplayUpdater interface
- ISystemMediaTransportControlsDisplayUpdater interface, described
topic_type:
- apiref
api_name:
- ISystemMediaTransportControlsDisplayUpdater
api_location:
- windows.media.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ISystemMediaTransportControlsDisplayUpdater interface

Provides functionality to update the media metadata that is displayed on the [**ISystemMediaTransportControls**](isystemmediatransportcontrols.md).

## Members

The **ISystemMediaTransportControlsDisplayUpdater** interface inherits from [**IInspectable**](https://msdn.microsoft.com/library/windows/desktop/br205821). **ISystemMediaTransportControlsDisplayUpdater** also has these types of members:

-   [Methods](#methods)

### Methods

The **ISystemMediaTransportControlsDisplayUpdater** interface has these methods.



| Method                                                                                                     | Description                                                                                        |
|:-----------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------|
| [**ClearAll**](https://msdn.microsoft.com/library/windows/desktop/dn892303)                        | Clears all of the media metadata.<br/>                                                       |
| [**CopyFromFileAsync**](https://msdn.microsoft.com/library/windows/desktop/dn892304)      | Initializes the media properties using the specified file. IRandomAccessStreamReference<br/> |
| [**get\_AppMediaId**](https://msdn.microsoft.com/library/windows/desktop/dn892305)           | Gets the media ID of the app.<br/>                                                           |
| [**get\_ImageProperties**](https://msdn.microsoft.com/library/windows/desktop/dn892306) | Gets the image properties associated with the currently playing media.<br/>                  |
| [**get\_MusicProperties**](https://msdn.microsoft.com/library/windows/desktop/dn892307) | Gets the music properties associated with the currently playing media. <br/>                 |
| [**get\_Thumbnail**](https://msdn.microsoft.com/library/windows/desktop/dn892308)             | Gets the thumbnail image associated with the currently playing media. <br/>                  |
| [**get\_Type**](https://msdn.microsoft.com/library/windows/desktop/dn892309)                       | Gets the type of media currently playing.<br/>                                               |
| [**get\_VideoProperties**](https://msdn.microsoft.com/library/windows/desktop/dn892310) | Gets the video properties associated with the currently playing media. <br/>                 |
| [**put\_AppMediaId**](https://msdn.microsoft.com/library/windows/desktop/dn892311)           | Sets the media ID of the app.<br/>                                                           |
| [**put\_Thumbnail**](https://msdn.microsoft.com/library/windows/desktop/dn892312)             | Sets the thumbnail image associated with the currently playing media. <br/>                  |
| [**put\_Type**](https://msdn.microsoft.com/library/windows/desktop/dn892313)                       | Sets the type of media currently playing.<br/>                                               |
| [**Update**](https://msdn.microsoft.com/library/windows/desktop/dn892314)                            | Updates the currently displayed content.<br/>                                                |



 

## Requirements



|                   |                                                                                            |
|-------------------|--------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Windows.media.h</dt> </dl> |



## See also

<dl> <dt>

[**IInspectable**](https://msdn.microsoft.com/library/windows/desktop/br205821)
</dt> </dl>

 

 






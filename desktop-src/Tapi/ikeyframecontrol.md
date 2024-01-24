---
description: The IKeyFrameControl interface is implemented by the H.323 MSP and is available only on H.323 stream objects.
ms.assetid: 68cb1df1-f7fa-447a-8ea5-80dc1e802760
title: IKeyFrameControl interface (H323priv.h)
ms.topic: reference
ms.date: 05/31/2018
---

# IKeyFrameControl interface

\[**IKeyFrameControl** is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **IKeyFrameControl** interface is implemented by the [H.323 MSP](h323-msp.md) and is available only on H.323 stream objects. This interface exposes methods that enable creation and manipulation of terminals that can communicate between H323 and SDP clients. It has two methods that allow the application to ask the remote endpoint to update the video image with a keyframe.

## Members

The **IKeyFrameControl** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IKeyFrameControl** also has these types of members:

-   [Methods](#methods)

### Methods

The **IKeyFrameControl** interface has these methods.



| Method                                                                  | Description                                                                                 |
|:------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------|
| [**PeriodicUpdatePicture**](ikeyframecontrol-periodicupdatepicture.md) | Configures a timer in the stream that will ask for picture updates periodically.<br/> |
| [**UpdatePicture**](ikeyframecontrol-updatepicture.md)                 | Asks the video sender to update the picture.<br/>                                     |



 

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>H323priv.h</dt> </dl> |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Tapi3.dll</dt> </dl>  |



## See also

<dl> <dt>

[H323 MSP](h323-msp.md)
</dt> </dl>

 


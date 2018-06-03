---
title: VideoPreview object
description: Displays the video stream of a video imaging device. A VideoPreview object can be created by dropping the VideoPreview control on a form or by using an OBJECT tag. The VideoPreview control is a visible control.
ms.assetid: c6f1f61d-2edc-4820-8567-fc3e94c7d4f6
keywords:
- VideoPreview object WIA Automation
- VideoPreview object WIA Automation , described
topic_type:
- apiref
api_name:
- VideoPreview
api_location:
- Wiaaut.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# VideoPreview object

Displays the video stream of a video imaging device. A **VideoPreview** object can be created by dropping the **VideoPreview** control on a form or by using an OBJECT tag. The **VideoPreview** control is a visible control.

## Members

The **VideoPreview** object has these types of members:

-   [Properties](#properties)

### Properties

The **VideoPreview** object has these properties.



| Property                                                                 | Access type           | Description                                                                       |
|:-------------------------------------------------------------------------|:----------------------|:----------------------------------------------------------------------------------|
| [**Device (VideoPreview)**](-wiaaut-ivideopreview-device.md)<br/> | Read/write<br/> | Sets or retrieves the [**Device**](-wiaaut-device.md) to preview.<br/>     |
| [**Pause**](-wiaaut-ivideopreview-pause.md)<br/>                  | Read/write<br/> | Sets or retrieves a value indicating whether video playback is paused.<br/> |



 

## Remarks

Note that the **VideoPreview** control uses and displays the first available video imaging device on initialization. Consequently, if you want to use more than one **VideoPreview** control on a Microsoft Visual Basic form, HTML page, or HTML Application (HTA), you might encounter problems specifing the [**Device (VideoPreview)**](-wiaaut-ivideopreview-device.md) property as it might already be in use in a different **VideoPreview** control. The easiest way to handle this is to set all **Device (VideoPreview)** properties to **Nothing** prior to using any of them.

For example code, see [Use VideoPreview Control in HTML](https://www.bing.com/search?q=Use VideoPreview Control in HTML) in Shared Samples.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

[**Pause**](-wiaaut-ivideopreview-pause.md)
</dt> </dl>

 

 






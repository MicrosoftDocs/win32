---
title: INotifySeek interface
description: The transform can optionally implement the INotifySeek interface to receive notifications of playback discontinuities because of a seek operation in the file by the user.
ms.assetid: 8aa99bc1-012b-4c92-b62e-d0e71851d4d0
keywords:
- INotifySeek interface Windows Movie Maker and DVD Maker
- INotifySeek interface Windows Movie Maker and DVD Maker , described
topic_type:
- apiref
api_name:
- INotifySeek
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# INotifySeek interface

The transform can optionally implement the **INotifySeek** interface to receive notifications of playback discontinuities because of a seek operation in the file by the user. Unless your transform needs to be notified of stream-seeking, it does not need to implement this interface.

## Members

The **INotifySeek** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **INotifySeek** also has these types of members:

-   [Methods](#methods)

### Methods

The **INotifySeek** interface has these methods.



| Method                                                   | Description                                                                                                     |
|:---------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------|
| [**OnPipelineSeeked**](inotifyseek-onpipelineseeked.md) | Alerts the application that there will be a discontinuity because of a seek operation in the stream.<br/> |



 

## See also

<dl> <dt>

[**Transform Interfaces**](transform-interfaces.md)
</dt> </dl>

 

 






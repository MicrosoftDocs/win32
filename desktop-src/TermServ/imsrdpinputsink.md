---
title: IMsRdpInputSink interface
description: Remote desktop input sink.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ec30b64a-63bb-4f8f-8979-ab2ef9ece6b0'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["IMsRdpInputSink interface Remote Desktop Services", "IMsRdpInputSink interface Remote Desktop Services , described"]
topic_type:
- apiref
api_name:
- IMsRdpInputSink
api_location:
- MsTscAx.dll
api_type:
- COM
---

# IMsRdpInputSink interface

Remote desktop input sink.

## Members

The **IMsRdpInputSink** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IMsRdpInputSink** also has these types of members:

-   [Methods](#methods)

### Methods

The **IMsRdpInputSink** interface has these methods.



| Method                                                               | Description                          |
|:---------------------------------------------------------------------|:-------------------------------------|
| [**AddTouchInput**](imsrdpinputsink-addtouchinput.md)               | Adds touch input.<br/>         |
| [**BeginTouchFrame**](imsrdpinputsink-begintouchframe.md)           | Begin touch frame.<br/>        |
| [**EndTouchFrame**](imsrdpinputsink-endtouchframe.md)               | End touch frame.<br/>          |
| [**SendKeyboardEvent**](imsrdpinputsink-sendkeyboardevent.md)       | Sends keyboard event.<br/>     |
| [**SendMouseButtonEvent**](imsrdpinputsink-sendmousebuttonevent.md) | Sends mouse button event.<br/> |
| [**SendMouseMoveEvent**](imsrdpinputsink-sendmousemoveevent.md)     | Sends mouse move event.<br/>   |
| [**SendMouseWheelEvent**](imsrdpinputsink-sendmousewheelevent.md)   | Sends mouse wheel event.<br/>  |
| [**SendSyncEvent**](imsrdpinputsink-sendsyncevent.md)               | Sends sync event.<br/>         |



 

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                      |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IID\_IMsRdpInputSink is defined as 4606850E-76A7-4E28-A47E-C7174F619351<br/>     |



 

 






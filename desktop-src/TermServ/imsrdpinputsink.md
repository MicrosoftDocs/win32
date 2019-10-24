---
title: IMsRdpInputSink interface
description: Remote desktop input sink.
ms.assetid: ec30b64a-63bb-4f8f-8979-ab2ef9ece6b0
ms.tgt_platform: multiple
keywords:
- IMsRdpInputSink interface Remote Desktop Services
- IMsRdpInputSink interface Remote Desktop Services , described
topic_type:
- apiref
api_name:
- IMsRdpInputSink
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpInputSink interface

Remote desktop input sink.

## Members

The **IMsRdpInputSink** interface inherits from the [**IUnknown**](https://docs.microsoft.com/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IMsRdpInputSink** also has these types of members:

-   [Methods](#methods)

### Methods

The **IMsRdpInputSink** interface has these methods.



| Method                                                               | Description                          |
|:---------------------------------------------------------------------|:-------------------------------------|
| [**AddTouchInput**](https://msdn.microsoft.com/en-us/library/Mt786987(v=VS.85).aspx)               | Adds touch input.<br/>         |
| [**BeginTouchFrame**](https://msdn.microsoft.com/en-us/library/Mt786988(v=VS.85).aspx)           | Begin touch frame.<br/>        |
| [**EndTouchFrame**](https://msdn.microsoft.com/en-us/library/Mt786989(v=VS.85).aspx)               | End touch frame.<br/>          |
| [**SendKeyboardEvent**](https://msdn.microsoft.com/en-us/library/Mt786990(v=VS.85).aspx)       | Sends keyboard event.<br/>     |
| [**SendMouseButtonEvent**](https://msdn.microsoft.com/en-us/library/Mt786991(v=VS.85).aspx) | Sends mouse button event.<br/> |
| [**SendMouseMoveEvent**](https://msdn.microsoft.com/en-us/library/Mt786992(v=VS.85).aspx)     | Sends mouse move event.<br/>   |
| [**SendMouseWheelEvent**](https://msdn.microsoft.com/en-us/library/Mt786993(v=VS.85).aspx)   | Sends mouse wheel event.<br/>  |
| [**SendSyncEvent**](https://msdn.microsoft.com/en-us/library/Mt786994(v=VS.85).aspx)               | Sends sync event.<br/>         |



 

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                      |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IID\_IMsRdpInputSink is defined as 4606850E-76A7-4E28-A47E-C7174F619351<br/>     |



 

 






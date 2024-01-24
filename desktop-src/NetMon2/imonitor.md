---
description: The IMonitor interface provides methods that control monitor operation. These methods are called by the Monitor Control Service (MCSVC).
ms.assetid: 53140e7d-c3a1-45cd-aaa4-c6f5021a6102
title: IMonitor interface (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMonitor
api_type: 
- COM
api_location: 
- Netmon.h
---

# IMonitor interface

The **IMonitor** interface provides methods that control monitor operation. These methods are called by the [*Monitor Control Service*](m.md) (MCSVC).

## Members

The **IMonitor** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IMonitor** also has these types of members:

-   [Methods](#methods)

### Methods

The **IMonitor** interface has these methods.



| Method                                        | Description                                                                                                         |
|:----------------------------------------------|:--------------------------------------------------------------------------------------------------------------------|
| [**DoConfigure**](imonitor-doconfigure.md)   | Updates monitor configuration.<br/>                                                                           |
| [**DoInitialize**](imonitor-doinitialize.md) | Initializes a monitor.<br/>                                                                                   |
| [**OnFrames**](imonitor-onframes.md)         | Indicates the status of a frame event.<br/>                                                                   |
| [**OnStart**](imonitor-onstart.md)           | Indicates that the monitor has been configured successfully and that the data capture is about to begin.<br/> |
| [**OnStatus**](imonitor-onstatus.md)         | Indicates an NPP status event.<br/>                                                                           |
| [**OnStop**](imonitor-onstop.md)             | Indicates data capture completion.<br/>                                                                       |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 


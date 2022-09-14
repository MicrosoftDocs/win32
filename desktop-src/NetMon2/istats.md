---
description: The IStats interface provides the methods you use to connect an NPP to the network, capture network traffic, retrieve statistics, and disconnect the NPP from the network. This interface generates statistics without frames.
ms.assetid: 57cfcdd6-f16c-4a1c-b2ba-ce98f0576862
title: IStats interface (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IStats
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IStats interface

The **IStats** interface provides the methods you use to connect an NPP to the network, capture network traffic, retrieve statistics, and disconnect the NPP from the network. This interface generates statistics without frames.

## Members

The **IStats** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IStats** also has these types of members:

-   [Methods](#methods)

### Methods

The **IStats** interface has these methods.



| Method                                                                | Description                                                                                                                                               |
|:----------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Configure**](istats-configure.md)                                 | Configures the trigger, pattern match, and buffer size of the capture file.<br/>                                                                    |
| [**Connect**](istats-connect.md)                                     | Connects the NPP to the network.<br/>                                                                                                               |
| [**Disconnect**](istats-disconnect.md)                               | Disconnects the NPP from the network.<br/>                                                                                                          |
| [**GetControlState**](istats-getcontrolstate.md)                     | Retrieves the state of the [*capture*](c.md), which indicates if the capture is running or paused.<br/>                        |
| [**GetConversationStatistics**](istats-getconversationstatistics.md) | Retrieves [*session*](s.md) and [*station information*](s.md) about the current capture.<br/> |
| [**GetTotalStatistics**](istats-gettotalstatistics.md)               | Extracts time, buffer, driver, and other network statistics from the currently running capture.<br/>                                                |
| [**Pause**](istats-pause.md)                                         | Temporarily stops the current capture.<br/>                                                                                                         |
| [**QueryStations**](istats-querystations.md)                         | Retrieves a list of all computers that are using Network Monitor to capture data on a subnet.<br/>                                                  |
| [**QueryStatus**](istats-querystatus.md)                             | Retrieves the status of the NPP.<br/>                                                                                                               |
| [**Resume**](istats-resume.md)                                       | Restarts a paused capture.<br/>                                                                                                                     |
| [**Start**](istats-start.md)                                         | Starts the capture.<br/>                                                                                                                            |
| [**Stop**](istats-stop.md)                                           | Stops the current capture.<br/>                                                                                                                     |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                                     |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>                                                                      |
| DLL<br/>                      | <dl> <dt>Ndisnpp.dll; </dt> <dt>Rmtnpp.dll</dt> </dl> |



 


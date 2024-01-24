---
description: The IESP interface provides the methods that connect the NPP to the network, capture network traffic to a capture file, retrieve statistics, and disconnect the NPP from the network.
ms.assetid: e483f501-4928-4bfd-b212-e100f2b8f64f
title: IESP interface (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IESP
api_type: 
- COM
api_location: 
- Ndisnpp.dll
- Rmtnpp.dll
---

# IESP interface

The **IESP** interface provides the methods that connect the NPP to the network, capture network traffic to a capture file, retrieve statistics, and disconnect the NPP from the network. This interface is used primarily when you need to collect network [*conversation statistics*](c.md) in a proprietary ESP file format.

## Members

The **IESP** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IESP** also has these types of members:

-   [Methods](#methods)

### Methods

The **IESP** interface has these methods.



| Method                                          | Description                                                                                                                        |
|:------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|
| [**Configure**](iesp-configure.md)             | Submits configuration information for a capture<br/>                                                                         |
| [**Connect**](iesp-connect.md)                 | Connects the NPP to the network.<br/>                                                                                        |
| [**Disconnect**](iesp-disconnect.md)           | Disconnects the NPP from the network.<br/>                                                                                   |
| [**GetControlState**](iesp-getcontrolstate.md) | Retrieves the state of the [*capture*](c.md), which indicates if the capture is running or paused.<br/> |
| [**Pause**](iesp-pause.md)                     | Temporarily stops the current capture.<br/>                                                                                  |
| [**QueryStations**](iesp-querystations.md)     | Retrieves a list of all computers that are using Network Monitor to capture data on a subnet.<br/>                           |
| [**QueryStatus**](iesp-querystatus.md)         | Retrieves the status of the NPP.<br/>                                                                                        |
| [**Resume**](iesp-resume.md)                   | Resumes a paused capture.<br/>                                                                                               |
| [**Start**](iesp-start.md)                     | Starts the capture and creates the capture file.<br/>                                                                        |
| [**Stop**](iesp-stop.md)                       | Stops the current capture.<br/>                                                                                              |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                                     |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>                                                                      |
| DLL<br/>                      | <dl> <dt>Ndisnpp.dll; </dt> <dt>Rmtnpp.dll</dt> </dl> |



 


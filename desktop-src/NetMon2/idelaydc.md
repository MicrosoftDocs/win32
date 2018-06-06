---
Description: The IDelaydC interface provides the methods used to connect to the network, capture network traffic to a capture file, retrieve statistics, and disconnect from the network.
ms.assetid: ab275653-2377-4af6-a810-48515962c88c
title: IDelaydC interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IDelaydC interface

The **IDelaydC** interface provides the methods used to connect to the network, capture network traffic to a capture file, retrieve statistics, and disconnect from the network.

This interface captures frames from the network data stream and then copies the frames to a capture file. This interface is used by Network Monitor and NPP applications. To receive the network data, the targeted NIC must support promiscuous mode.

## Members

The **IDelaydC** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IDelaydC** also has these types of members:

-   [Methods](#methods)

### Methods

The **IDelaydC** interface has these methods.



| Method                                                                  | Description                                                                                                                                             |
|:------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Configure**](idelaydc-configure.md)                                 | Submits configuration information used for a capture.<br/>                                                                                        |
| [**Connect**](idelaydc-connect.md)                                     | Connects the NPP to the network.<br/>                                                                                                             |
| [**Disconnect**](idelaydc-disconnect.md)                               | Disconnects the NPP from the network.<br/>                                                                                                        |
| [**GetControlState**](idelaydc-getcontrolstate.md)                     | Retrieves the state of the [*capture*](c.md#-netmon-capture-gly), which indicates if the capture is running or paused.<br/>                      |
| [**GetConversationStatistics**](idelaydc-getconversationstatistics.md) | Retrieves [*session*](s.md#-netmon-session-gly) and [*station information*](s.md#-netmon-station-information-gly) for the current capture.<br/> |
| [**GetTotalStatistics**](idelaydc-gettotalstatistics.md)               | Extracts time, buffer, driver, and other network statistics from the currently running capture.<br/>                                              |
| [**Pause**](idelaydc-pause.md)                                         | Temporarily stops the current capture.<br/>                                                                                                       |
| [**QueryStations**](idelaydc-querystations.md)                         | Retrieves a list of all computers that use Network Monitor to capture data on a subnet.<br/>                                                      |
| [**QueryStatus**](idelaydc-querystatus.md)                             | Retrieves the status of the NPP.<br/>                                                                                                             |
| [**Resume**](idelaydc-resume.md)                                       | Resumes a paused capture.<br/>                                                                                                                    |
| [**Start**](idelaydc-start.md)                                         | Starts a capture and creates the [*capture file*](c.md#-netmon-capture-file-gly).<br/>                                                           |
| [**Stop**](idelaydc-stop.md)                                           | Stops the current capture and closes the [*capture file*](c.md#-netmon-capture-file-gly).<br/>                                                   |



 

## Requirements



|                                     |                                                                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                                     |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>                                                                      |
| DLL<br/>                      | <dl> <dt>Ndisnpp.dll; </dt> <dt>Rmtnpp.dll</dt> </dl> |



 

 





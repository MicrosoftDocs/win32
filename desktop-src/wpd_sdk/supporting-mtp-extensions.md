---
Description: Supporting MTP Extensions
ms.assetid: 9e5f3da6-346a-4eca-bc85-2755c569986d
title: Supporting MTP Extensions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Supporting MTP Extensions

## Media Transfer Protocol

Media Transfer Protocol (MTP) is an extension to the Picture Transfer Protocol (PTP). As a result, all PTP protocol semantics are valid in MTP.

MTP communicates by using commands and responses between two parties, the initiator and the responder. The roles of the involved devices are very clearly defined. The PC typically is the initiator, and the device is always the responder. A non-PC device could also be an initiator (for example, a car deck or a Microsoft X-box). A device can never assume both roles at the same time.

The initiator starts communication by sending a command to the responder. The responder processes the command and sends back an appropriate response. There might be a data phase associated with the command. If this is the case, the direction of data flow must be known beforehand and accepted by both the initiator and the responder. Be aware that there is not a descriptive header that indicates data flows for new commands.

The responder can start communication independent of the initiator. For example, the responder can send events to the initiator. However, no data can be sent together with the event. If there is any data that needs to be read as part of the event, the initiator must send an MTP command, and the device can then send data in response to the command.

For a complete description of MTP, refer to the [MTP specification](http://go.microsoft.com/fwlink/p/?linkid=179917).

## Sending MTP Commands

Applications can send MTP commands to a device by invoking the [**IPortableDevice::SendCommand**](/windows/desktop/api/PortableDeviceApi/nf-portabledeviceapi-iportabledevice-sendcommand) method. The command that is sent depends on whether there is a data phase, and, on whether any accompanying data is read from or written to the device. The following table describes the three possible MTP extension commands.

Be aware that these commands are specific to MTP; and are therefore, only implemented by the WPD MTP class driver.



|                                                                                                                                      |                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| Command                                                                                                                              | Description                                                                                       |
| [**WPD\_COMMAND\_MTP\_EXT\_END\_DATA\_TRANSFER**](https://msdn.microsoft.com/library/windows/desktop/ff394843)                                      | Issues an MTP command that signals the conclusion of a data read or write operation.              |
| [**WPD\_COMMAND\_MTP\_EXT\_EXECUTE\_COMMAND\_WITHOUT\_DATA\_PHASE**](https://msdn.microsoft.com/library/windows/desktop/ff384850)  | Issues an MTP command without a corresponding data phase.                                         |
| [**WPD\_COMMAND\_MTP\_EXT\_EXECUTE\_COMMAND\_WITH\_DATA\_TO\_WRITE**](https://msdn.microsoft.com/library/windows/desktop/ff384852) | Issues an MTP command that is followed by accompanying data, which will be written to the device. |
| [**WPD\_COMMAND\_MTP\_EXT\_EXECUTE\_COMMAND\_WITH\_DATA\_TO\_READ**](https://msdn.microsoft.com/library/windows/desktop/ff384851)   | Issues an MTP command that is followed by accompanying data, which is read from the device.       |
| [**WPD\_COMMAND\_MTP\_EXT\_READ\_DATA**](https://msdn.microsoft.com/library/windows/desktop/ff384855)                                                       | Issues an MTP command that sends data from the device to the PC.                                  |
| [**WPD\_COMMAND\_MTP\_EXT\_WRITE\_DATA**](https://msdn.microsoft.com/library/windows/desktop/ff384856)                                                     | Issues an MTP command that sends data to the device from the PC.                                  |



 

Regardless of the phase, **WPD\_PROPERTY\_MTP\_EXT\_OPERATION\_CODE** and **WPD\_PROPERTY\_MTP\_EXT\_OPERATION\_PARAMS** must be specified.

If the MTP driver was able to send the command to the device, the return values will always contain **WPD\_PROPERTY\_MTP\_EXT\_RESPONSE\_CODE**. If the response code indicates success and if the semantics of the command allow for response parameters, **WPD\_PROPERTY\_MTP\_EXT\_RESPONSE\_PARAMS** will also be available.

## Related topics

<dl> <dt>

[**Programming Guide**](programming-guide.md)
</dt> </dl>

 

 




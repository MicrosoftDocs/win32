---
description: Some communications functions can be called for a device by using the EscapeCommFunction function.
ms.assetid: 12b92d4b-04b5-4509-9fad-af23fcfd8857
title: Extended Functions
ms.topic: article
ms.date: 05/31/2018
---

# Extended Functions

Some communications functions can be called for a device by using the [**EscapeCommFunction**](/windows/desktop/api/Winbase/nf-winbase-escapecommfunction) function. This function sends a code to direct the device to perform an extended function. For example, an application can suspend character transmission with the SETBREAK code and resume transmission with the CLRBREAK code. These particular operations can also be started by calling the [**SetCommBreak**](/windows/desktop/api/Winbase/nf-winbase-setcommbreak) and [**ClearCommBreak**](/windows/desktop/api/Winbase/nf-winbase-clearcommbreak) functions. **EscapeCommFunction** can also be used to implement manual modem control. For example, the CLRDTR and SETDTR codes can be used to implement manual DTR (data-terminal-ready) flow control. Note, however, that an error occurs if a process uses **EscapeCommFunction** to manipulate the DTR line when the device has been configured to enable DTR handshaking, or the RTS (request-to-send) line if RTS handshaking is enabled.

The [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) function enables a process to send an extended function code directly to a specified device driver, causing the device to perform a given operation. **DeviceIoControl** gives a device associated with a communications resource capabilities not supported by the standard serial communications functions. It enables an application to configure a device using parameters unique to that device as well as to call any device-specific functions.

 

 

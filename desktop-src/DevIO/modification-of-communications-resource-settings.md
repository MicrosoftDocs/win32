---
description: When the CreateFile function opens a handle to a serial communications resource, the system initializes and configures the resource according to the values set up the last time the resource was opened.
ms.assetid: a39881d8-32af-4846-a2d3-508f1945b666
title: Modification of Communications Resource Settings
ms.topic: article
ms.date: 05/31/2018
---

# Modification of Communications Resource Settings

When the [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea) function opens a handle to a serial communications resource, the system initializes and configures the resource according to the values set up the last time the resource was opened. Preserving the previous settings enables the user to retain the settings specified through a **mode** command when the device is reopened. The values inherited from the previous open operation include the configuration settings of the device control block (a [**DCB**](/windows/desktop/api/Winbase/ns-winbase-dcb) structure) and the time-out values used in I/O operations. If the device has never been opened, it is configured with the system defaults.

To determine the initial configuration of a serial communications resource, a process calls the [**GetCommState**](/windows/desktop/api/Winbase/nf-winbase-getcommstate) function, which fills in a serial port [**DCB**](/windows/desktop/api/Winbase/ns-winbase-dcb) structure with the current configuration settings. To modify this configuration, a process specifies a **DCB** structure in a call to the [**SetCommState**](/windows/desktop/api/Winbase/nf-winbase-setcommstate) function.

Members of the [**DCB**](/windows/desktop/api/Winbase/ns-winbase-dcb) structure specify the configuration settings such as the baud rate, the number of data bits per byte, and the number of stop bits per byte. Other **DCB** members specify special characters and enable parity checking and flow control. When a process needs to modify only a few of these configuration settings, it should first call [**GetCommState**](/windows/desktop/api/Winbase/nf-winbase-getcommstate) to fill in a **DCB** structure with the current configuration. Then the process can adjust the important values in the **DCB** structure and reconfigure the device by calling [**SetCommState**](/windows/desktop/api/Winbase/nf-winbase-setcommstate) and specifying the modified **DCB** structure. This procedure ensures that the unmodified members of the **DCB** structure contain appropriate values. For example, a common error is to configure a device with a **DCB** structure in which the structure's **XonChar** member is equal to the **XoffChar** member.

The [**BuildCommDCB**](/windows/desktop/api/Winbase/nf-winbase-buildcommdcba) function provides another way to modify a [**DCB**](/windows/desktop/api/Winbase/ns-winbase-dcb) structure. **BuildCommDCB** uses a string with the same form as the command-line arguments of the **mode** command to specify the baud rate, parity scheme, number of stop bits, and number of data bits. The remaining members of [**DCB**](/windows/desktop/api/Winbase/ns-winbase-dcb) are not changed by this function, except that the appropriate members are set to disable XON/XOFF and hardware flow control. **BuildCommDCB** only modifies a **DCB** structure; it does not reconfigure the device.

A process can reconfigure a communications resource by using the [**GetCommProperties**](/windows/desktop/api/Winbase/nf-winbase-getcommproperties) function to get information from a device driver about the configuration settings that it supports. The process can use this information to avoid specifying a configuration that is not supported.

The [**SetCommState**](/windows/desktop/api/Winbase/nf-winbase-setcommstate) function reconfigures the communications resource, but it does not affect the internal output and input buffers of the specified driver. The buffers are not flushed, and pending read and write operations are not terminated prematurely.

A process reinitializes a communications resource by using the [**SetupComm**](/windows/desktop/api/Winbase/nf-winbase-setupcomm) function, which performs the following tasks:

-   Terminates pending read and write operations, even if they have not been completed.
-   Discards unread characters and frees the internal output and input buffers of the driver associated with the specified resource.
-   Reallocates the internal output and input buffers.

A process is not required to call [**SetupComm**](/windows/desktop/api/Winbase/nf-winbase-setupcomm). If it does not, the resource's driver initializes the device with the default settings the first time that the communications resource handle is used.

 

 

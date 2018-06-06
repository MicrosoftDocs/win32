---
Description: All user-mode requests are sent to the Microsoft-provided kernel-mode driver GenericUSBFn.sys.
ms.assetid: 27E23570-4897-4E18-90E0-80AE014C4E28
title: User mode services to UFX programming reference
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# User mode services to UFX programming reference

All user-mode requests are sent to the Microsoft-provided kernel-mode driver *GenericUSBFn.sys*. You can create a user-mode service that communicates with *GenericUSBFn.sys* by sending these I/O control code (IOCTL), and *GenericUSBFn.sys* handles kernel-mode communication with the USB function drivers.

These IOCTLs are used for communicating with *GenericUSBFn.sys* from a user-mode service.

## In this section



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>IOCTL_GENERICUSBFN_ACTIVATE_USB_BUS</strong>](/windows/desktop/api/GenericUsbFnIoctl/ni-genericusbfnioctl-ioctl_genericusbfn_activate_usb_bus)<br/></td>
<td>This I/O control code (IOCTL) is sent by a user-mode service or application to notify GenericUSBFn.sys to activate the Universal Serial Bus (USB). Once activated, the bus is prepared to process bus events and handle traffic.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IOCTL_GENERICUSBFN_BUS_EVENT_NOTIFICATION</strong>](/windows/desktop/api/GenericUsbFnIoctl/ni-genericusbfnioctl-ioctl_genericusbfn_bus_event_notification)<br/></td>
<td>This I/O control code (IOCTL) is sent by a user-mode service or application to register for USB event. After this request completes, notifications about events such as a change in the port type or the receipt of a non-standard setup packet can be received. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>IOCTL_GENERICUSBFN_CONTROL_STATUS_HANDSHAKE_IN</strong>](/windows/desktop/api/GenericUsbFnIoctl/ni-genericusbfnioctl-ioctl_genericusbfn_control_status_handshake_in)<br/></td>
<td>This I/O control code (IOCTL) is sent by a user mode service or application to request a zero-length control status handshake on endpoint 0 in the IN direction.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IOCTL_GENERICUSBFN_CONTROL_STATUS_HANDSHAKE_OUT</strong>](/windows/desktop/api/GenericUsbFnIoctl/ni-genericusbfnioctl-ioctl_genericusbfn_control_status_handshake_out)<br/></td>
<td>This I/O control code (IOCTL) is sent by a user-mode service or application to complete a zero-length control status handshake on endpoint 0 in the OUT direction.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IOCTL_GENERICUSBFN_DEACTIVATE_USB_BUS</strong>](/windows/desktop/api/GenericUsbFnIoctl/ni-genericusbfnioctl-ioctl_genericusbfn_deactivate_usb_bus)<br/></td>
<td>This IOCTL code is nevtot supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IOCTL_GENERICUSBFN_GET_CLASS_INFO</strong>](/windows/desktop/api/GenericUsbFnIoctl/ni-genericusbfnioctl-ioctl_genericusbfn_get_class_info)<br/></td>
<td>This I/O control code (IOCTL) is sent by the user-mode service or application to retrieve information about a device's available pipes as configured in the registry. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>IOCTL_GENERICUSBFN_GET_CLASS_INFO_EX</strong>](/windows/desktop/api/GenericUsbFnIoctl/ni-genericusbfnioctl-ioctl_genericusbfn_get_class_info_ex)<br/></td>
<td>This I/O control code (IOCTL) is sent by a user-mode service or application to retrieve information about a device's available pipes as configured in the registry. <br/></td>
</tr>
<tr class="even">
<td>[<strong>IOCTL_GENERICUSBFN_GET_INTERFACE_DESCRIPTOR_SET</strong>](/windows/desktop/api/GenericUsbFnIoctl/ni-genericusbfnioctl-ioctl_genericusbfn_get_interface_descriptor_set)<br/></td>
<td>This I/O control code (IOCTL) is sent by a user-mode service or application to get the entire USB interface descriptor set for a function on the device.
<blockquote>
[!Note]<br />
This IOCTL request does not retrieve the interface descriptor set for the entire device.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="odd">
<td>[<strong>IOCTL_GENERICUSBFN_GET_PIPE_STATE</strong>](/windows/desktop/api/GenericUsbFnIoctl/ni-genericusbfnioctl-ioctl_genericusbfn_get_pipe_state)<br/></td>
<td>This I/O control code (IOCTL) is sent by a user-mode service or application to get the state of the specified USB pipe.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IOCTL_GENERICUSBFN_REGISTER_USB_STRING</strong>](/windows/desktop/api/GenericUsbFnIoctl/ni-genericusbfnioctl-ioctl_genericusbfn_register_usb_string)<br/></td>
<td>This I/O control code (IOCTL) is sent by a user-mode service or application to register a USB string descriptor.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IOCTL_GENERICUSBFN_SET_PIPE_STATE</strong>](/windows/desktop/api/GenericUsbFnIoctl/ni-genericusbfnioctl-ioctl_genericusbfn_set_pipe_state)<br/></td>
<td>This I/O control code (IOCTL) is sent by a user-mode service or application to set the state of the specified USB pipe.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IOCTL_GENERICUSBFN_TRANSFER_IN</strong>](/windows/desktop/api/GenericUsbFnIoctl/ni-genericusbfnioctl-ioctl_genericusbfn_transfer_in)<br/></td>
<td>This I/O control code (IOCTL) is sent by a user-mode service or application to issue an IN direction transfer on the endpoint that corresponds to the specified pipe ID in the input buffer. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>IOCTL_GENERICUSBFN_TRANSFER_IN_APPEND_ZERO_PKT</strong>](/windows/desktop/api/GenericUsbFnIoctl/ni-genericusbfnioctl-ioctl_genericusbfn_transfer_in_append_zero_pkt)<br/></td>
<td>This I/O control code (IOCTL) is sent by a user-mode service or application to issue an IN direction transfer on the endpoint that corresponds to the specified pipe ID in the input buffer.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IOCTL_GENERICUSBFN_TRANSFER_OUT</strong>](/windows/desktop/api/GenericUsbFnIoctl/ni-genericusbfnioctl-ioctl_genericusbfn_transfer_out)<br/></td>
<td>This I/O control code (IOCTL) is sent by a user-mode service or application to issue an OUT direction transfer on the endpoint that corresponds to the specified pipe ID in the input buffer.<br/></td>
</tr>
</tbody>
</table>



 

### Communicating with GenericUSBFn.sys from a user-mode service

The following steps describe how you can define a USB interface service that interacts with *GenericUSBFn.sys* to communicate with the USB function drivers:

1.  On startup, the service listens for the device interface arrival of the interface. The device interface GUID is the InterfaceGUID value that is declared in the registry under the OEM-defined subkey of *HKEY\_LOCAL\_MACHINE\\CurrentControlSet\\Control\\USBFN\\Interfaces*. There are two common methods for listening to device arrival:
    -   Trigger start the service. For more information, see [Service Trigger Events](https://msdn.microsoft.com/library/windows/desktop/dd405513).
    -   Register for device interface arrival. For more information, see the [**CM\_Register\_Notification**](https://msdn.microsoft.com/library/windows/hardware/hh780224) function.
2.  After the interface arrives, the service opens a handle to the device:
    1.  Get the symbolic name for the device by calling the [**CM\_Get\_Device\_Interface\_List**](https://msdn.microsoft.com/library/windows/hardware/ff538463) function. Specify the device interface GUID that is declared in the *InterfaceGUID* value in the registry.
    2.  After you have the symbolic name for the device, open a handle to the device by using **CreateFile**.
3.  The service issues [**IOCTL\_GENERICUSBFN\_GET\_CLASS\_INFO**](/windows/desktop/api/GenericUsbFnIoctl/ni-genericusbfnioctl-ioctl_genericusbfn_get_class_info) to retrieve information about the available pipes, as configured in the registry.
4.  After the service is ready to communicate, it issues [**IOCTL\_GENERICUSBFN\_ACTIVATE\_USB\_BUS**](/windows/desktop/api/GenericUsbFnIoctl/ni-genericusbfnioctl-ioctl_genericusbfn_activate_usb_bus). After all class drivers are activated, the USB function class extension can connect to the host.
5.  To receive USB notifications, the service issues [**IOCTL\_GENERICUSBFN\_BUS\_EVENT\_NOTIFICATION**](/windows/desktop/api/GenericUsbFnIoctl/ni-genericusbfnioctl-ioctl_genericusbfn_bus_event_notification). This IOCTL completes when a new USB event has occurred. Events ([**USBFN\_EVENT**](/windows-hardware/drivers/ddi/content/usbfnbase/ne-usbfnbase-_usbfn_event)) of particular interest include:
    -   **UsbfnEventReset**: This is used to determine the speed of the connected USB device.
    -   **UsbfnEventConfigured**: The service can now issue transfer requests.
    -   **UsbfnEventSetupPacket**: The USB function class extension has received an interface-specific setup packet (`bmRequestType.Type == BMREQUEST_CLASS`). The service should reply to the setup packet by issuing a transfer request in pipe 0, followed by a handshake request ([**IOCTL\_GENERICUSBFN\_CONTROL\_STATUS\_HANDSHAKE\_OUT**](/windows/desktop/api/GenericUsbFnIoctl/ni-genericusbfnioctl-ioctl_genericusbfn_control_status_handshake_out)) in the opposite direction on pipe 0.
6.  After the **UsbfnEventConfigured** event is received, the service can begin issuing transfer requests using [**IOCTL\_GENERICUSBFN\_TRANSFER\_IN**](/windows/desktop/api/GenericUsbFnIoctl/ni-genericusbfnioctl-ioctl_genericusbfn_transfer_in), [**IOCTL\_GENERICUSBFN\_TRANSFER\_IN\_APPEND\_ZERO\_PKT**](/windows/desktop/api/GenericUsbFnIoctl/ni-genericusbfnioctl-ioctl_genericusbfn_transfer_in_append_zero_pkt), and [**IOCTL\_GENERICUSBFN\_TRANSFER\_OUT**](/windows/desktop/api/GenericUsbFnIoctl/ni-genericusbfnioctl-ioctl_genericusbfn_transfer_out).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbref\buses%5D:%20User%20mode%20services%20to%20UFX%20programming%20reference%20%20RELEASE:%20%285/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





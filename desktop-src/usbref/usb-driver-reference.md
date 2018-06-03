---
Description: Programming reference for developing drivers that interact with USB devices, host controllers, connectors.
ms.assetid: F1C90293-BB9A-4864-92FF-6DC13BA2A155
title: USB driver reference
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# USB driver reference

Programming reference for developing drivers that interact with USB devices, host controllers, connectors.

## USB device driver

USB device drivers include:

-   WDM export functions and macros
-   WDF export functions, including WDF USB reference (KMDF and UMDF 2.0) and UMDF 1.x USB reference.
-   USB Device Redirection functions - USB Device Redirection is controlled by the Redirection Policy Manager (RPM). RPM is a kernel-mode export driver that is available in Windows 7. By using RPM, third-party developers can load an alternate driver in place of the original USB device driver. RPM abstracts the redirection functionality provided by Microsoft. One of the clients for RPM is a Windows Virtual PC, a client virtualization solution for Windows 7
-   Callback functions for USB client drivers - These are the callback routines that a USB client can implement.
-   Bus Driver Interface functions for USB Client Drivers - In Windows Vista, and Windows 7, instead of linking directly to Usbd.sys, a USB client driver can query the USB bus driver for an interface. The client driver can then call certain routines associated with the bus driver interface
-   Generic Parent Driver functions - In Windows Vista, the USB Generic Parent Driver (Usbccgp.sys) can query vendor-supplied filter drivers for an interface.
-   I/O control codes for USB device drivers - Windows Driver Model (WDM) clients of the Universal Serial Bus (USB) driver stack communicate to the USB driver stack, by submitting an IRP with major code [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766), and a minor code corresponding to an IOCTL value.
-   Kernel-Mode IOCTLs

The following functions have been deprecated. Do not use.

-   [**USBD\_CalculateUsbBandwidth**](/windows-hardware/drivers/ddi/content/usbdlib/nf-usbdlib-usbd_calculateusbbandwidth)
-   [**USBD\_CreateConfigurationRequest**](/windows-hardware/drivers/ddi/content/usbdlib/nf-usbdlib-usbd_createconfigurationrequest)
-   [**USBD\_Debug\_LogEntry**](https://msdn.microsoft.com/library/windows/hardware/ff539037)
-   [**USBD\_GetUSBDIVersion**](/windows-hardware/drivers/ddi/content/usbdlib/nf-usbdlib-usbd_getusbdiversion)
-   [**USBD\_ParseConfigurationDescriptor**](/windows-hardware/drivers/ddi/content/usbdlib/nf-usbdlib-usbd_parseconfigurationdescriptor)
-   [**USBD\_QueryBusTime**](/windows-hardware/drivers/ddi/content/usbdlib/nf-usbdlib-usbd_querybustime)
-   [**USBD\_RegisterHcFilter**](/windows-hardware/drivers/ddi/content/usbdlib/nf-usbdlib-usbd_registerhcfilter)

The following I/O requests have been deprecated or reserved for internal use. USB client drivers must not use these I/O requests:

-   [**IOCTL\_USB\_DIAG\_IGNORE\_HUBS\_OFF**](/windows-hardware/drivers/ddi/content/Usbioctl/ni-usbioctl-ioctl_usb_diag_ignore_hubs_off)
-   [**IOCTL\_USB\_DIAG\_IGNORE\_HUBS\_ON**](/windows-hardware/drivers/ddi/content/Usbioctl/ni-usbioctl-ioctl_usb_diag_ignore_hubs_on)
-   [**IOCTL\_USB\_DIAGNOSTIC\_MODE\_OFF**](/windows-hardware/drivers/ddi/content/Usbioctl/ni-usbioctl-ioctl_usb_diagnostic_mode_off)
-   [**IOCTL\_USB\_DIAGNOSTIC\_MODE\_ON**](/windows-hardware/drivers/ddi/content/Usbioctl/ni-usbioctl-ioctl_usb_diagnostic_mode_on)
-   [**IOCTL\_USB\_GET\_HUB\_CAPABILITIES**](/windows-hardware/drivers/ddi/content/Usbioctl/ni-usbioctl-ioctl_usb_get_hub_capabilities)
-   [**IOCTL\_USB\_HCD\_DISABLE\_PORT**](/windows-hardware/drivers/ddi/content/Usbioctl/ni-usbioctl-ioctl_usb_hcd_disable_port)
-   [**IOCTL\_USB\_HCD\_ENABLE\_PORT**](/windows-hardware/drivers/ddi/content/usbioctl/ni-usbioctl-ioctl_usb_hcd_enable_port)
-   [**IOCTL\_USB\_HCD\_GET\_STATS\_1**](/windows-hardware/drivers/ddi/content/Usbioctl/ni-usbioctl-ioctl_usb_hcd_get_stats_1)
-   [**IOCTL\_USB\_HCD\_GET\_STATS\_2**](/windows-hardware/drivers/ddi/content/Usbioctl/ni-usbioctl-ioctl_usb_hcd_get_stats_2)
-   [**IOCTL\_USB\_RESET\_HUB**](/windows-hardware/drivers/ddi/content/Usbioctl/ni-usbioctl-ioctl_usb_reset_hub)

## USB dual-role controller

A USB driver for a dual-role controller can behave as a host controller or a function controller depending on the hardware to which it is connected. These controllers are common on mobile devices and allow for connections to PCs, as well as USB peripherals like keyboards and mice. A mobile device can behave as a peripheral when it is connected to a PC, allowing you to transfer files between your PC and the mobile device. In that scenario, the controller on the device operates in the function role. Conversely, the controller can operate in the host role when connected to USB peripherals like storage drives, keyboard, mice.

One of the main responsibilities of a driver for a dual-role controller is to switch between those two roles, tearing down the previous role's device node and loading the device node for the new role. When writing the driver, use the WDF class extension-client driver model. For more information about the WDF class extension-client driver model, see [Ursdevice.h](https://www.bing.com/search?q=Ursdevice.h).

For information about enabling a Windows system for USB dual-role support, see [USB Dual Role Driver Stack Architecture](https://msdn.microsoft.com/library/windows/hardware/dn957036.aspx).

## USB host controller

The USB host controller extension is a system-supplied extension to the Kernel-Mode Driver Framework (KMDF). Within the Microsoft USB Driver Stack Architecture, UCX provides functionality to assist a host controller client driver in managing a USB host controller device. The client driver handles hardware operations and events, power management, and PnP events. UCX serves as an abstracted interface to the rest of the Microsoft USB 3.0 stack, queues requests to the client driver, and performs other tasks.

## USB function class driver to USB function controller

A USB function class driver implements the functionality of a specific interface (or group of interfaces) on the USB device. The class driver handle requests issued by user mode services, or it can forwards requests to USB function class extension (UFX) and its function client driver. Certain class drivers are included in Windows, such as MTP and IpOverUsb. Windows also provides a generic kernel-mode class driver, Generic USBFN (GenericUSBFn.sys). If a particular interface or functionality is not provided by a system-supplied driver, you might need write a function class driver. The class driver may be implemented as a kernel-mode driver by using Windows Driver Frameworks (WDF). Alternatively, you may implement it as a user-mode service. In that case, your class driver must be paired with the system-supplied class driver, Generic USBFN. For example, the MTP class driver runs as a user-mode service that transferring files to and from the device.

## USB function controller client driver

The USB function client driver is responsible for implementing a function controller-specific operations. The client driver communicates with the USB function class extension (UFX) module to handle endpoint data transfers, USB device state changes (reset, suspend, resume), attach/detach detection, port/charger detection. The client driver is also responsible for handling power management, and PnP events.

## USB filter driver for supporting USB chargers

Write a filter driver that supports detection of chargers, if the function controller uses the in-box Synopsys and ChipIdea drivers. If you are writing a client driver for a proprietary function controller, charger/attach detection is integrated in the client driver by implementing [*EVT\_UFX\_DEVICE\_PROPRIETARY\_CHARGER\_SET\_PROPERTY*](/windows-hardware/drivers/ddi/content/Ufxclient/nc-ufxclient-evt_ufx_device_proprietary_charger_set_property), [*EVT\_UFX\_DEVICE\_PROPRIETARY\_CHARGER\_RESET*](/windows-hardware/drivers/ddi/content/Ufxclient/nc-ufxclient-evt_ufx_device_proprietary_charger_reset), and [*EVT\_UFX\_DEVICE\_DETECT\_PROPRIETARY\_CHARGER*](/windows-hardware/drivers/ddi/content/Ufxclient/nc-ufxclient-evt_ufx_device_proprietary_charger_detect).

The USB function stack allows the device, such as a phone or tablet, to charge when connected to a host and USB charger as defined by the [USB Battery Charging (BC) 1.2 specification](http://www.usb.org/developers/docs/devclass_docs/USB_Battery_Charging_1.2.pdf).

-   There are two types of ports that the device can use for charging. The device can charge from a dedicated charging port (DCP) on a charger that shipped with the device. Alternately, the device can from standard downstream ports or charging downstream ports when the device is connected to a PC. Both of those cases are compliant with the USB BC 1.2 specification.
-   Certain chargers do not follow the specification. USB function stack allows the device to charge from those proprietary USB chargers.

To support spec-compliant and proprietary chargers, these operations are required.

-   The device is able to detect when a USB host or charger is attached or detached.
-   The device is able to detect the different USB charging ports as defined by the BC 1.2 spec.
-   For USB chargers that are defined by the BC 1.2 spec, the device charges with the maximum amount of current allowed by the BC 1.2 spec.
-   The device is able to detect proprietary USB chargers.
-   For proprietary USB chargers, determine the maximum amount of current that the device can draw.
-   Notify the operating system about the USB port type that is connected.
-   Prevent the device from pulling current over USB in the OS, even if a USB Host is connected and the device has configured itself with the Host.

Those operations are handled by USB function class extension (UFX)/client driver pair and a filter driver that is loaded as a lower filter in the USB function device stack. The driver manage USB charging starting from USB port detection to notifying the battery stack when it can begin charging and the maximum amount of current the device can draw.

Here is an architectural representation of the device stacks.

![usb charging](images/charger.png)

When a USB port is attached to the device, the client driver gets a notified either by the lower filter driver or an interrupt. At this time, the client driver performs port detection by communicating with the USB hardware and reports the port type to UFX. Alternately, it can request the filter driver. In that case, the filter driver coordinates with the USB hardware to perform USB port detection and returns the detected port type to the client driver and the client driver passes it to UFX.

Based on the port type, UFX determines the maximum amount of current that the device can draw and sends that information to the Charging Aggregation Driver (CAD). CAD validates the information. If the current is valid, CAD sends a request to the battery class driver to start charging up to the specified maximum current. The battery class driver forwards the charging request to the battery miniclass driver for processing. If the charging request specified that a proprietary charger was attached and the battery miniclass handles proprietary chargers, the miniclass driver can attempt to charge with a maximum current that it determines is appropriate. Otherwise, the battery miniclass can only charge up to the maximum current that is specified by CAD.

## USB Type-C connector driver

Windows 10 introduces support for the new USB connector: USB Type-C. You can write a driver for the connector (called the client driver in this section) that communicates with the Microsoft-provided class extension module: UcmCx to handle scenarios related to Type-C connectors such as, which ports support Type-C, which ports support power delivery.

## Emulated USB host controller driver

Windows drivers can present non-USB devices as emulated USB devices. By using the WDF class extension-client driver model, you can write a driver that translates USB-level constructs (reset, data transfers) to the actual underlying bus by using the hardware’s interface. The class extension and the client driver represent *an emulated host controller* with a root hub that is capable of presenting an attached device to the system as an USB device.

In this architecture, the class extension is the Microsoft-provided driver (udecx.sys):

USB device emulation class extension (UdeCx). This is an in-box driver included Windows 10.

The client driver is written by an IHV/OEM. This driver is referred to as the UDE client driver.

The driver pair loads as the FDO in the host controller device stack. The UDE client driver communicates with Udecx by using a set of methods and event callback functions to handle device requests and notify the class extension about various events.

## USB Type-C Port Controller Interface driver

The USB Type-C Port Controller Interface framework extension is a Microsoft-provided driver UcmTcpciCx.sys. This is an in-box driver included in Windows 10, version 1703. The client driver is written by an IHV/OEM. This driver is referred to as the port controller client driver.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbref\buses%5D:%20USB%20driver%20reference%20%20RELEASE:%20%285/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




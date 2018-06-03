---
Description: Plug and Play Extensions (PnP-X) enable a computer system to discover networked devices and to install them on the local system using Plug and Play (PnP).
ms.assetid: d6d158bb-6e81-4ccc-8324-b06dab5d8b9c
title: PnP-X
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PnP-X

\[Function Discovery is available for use in the following versions of Windows: Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008, and Windows Vista. It may be altered or unavailable in subsequent versions.\]

Plug and Play Extensions (PnP-X) enable a computer system to discover networked devices and to install them on the local system using Plug and Play (PnP). For more information about PnP-X, see [Windows Rally](http://go.microsoft.com/fwlink/p/?linkid=158768).

Each PnP-X device has an associated [function instance](function-objects.md). A list of PnP-X function instances is stored in the *PnP-X association database*. If a device has an associated entry marked in the association database and the device is currently online (on the network), the PnP [*devnode*](https://www.bing.com/search?q=*devnode*) for the device is marked *present* on the system, and the associated device is available for use. If a device does not have an associated entry marked in the association database, no PnP *devnode* will exist on the system and the device is not available for use.

## Extending Plug and Play to Network-connected Devices

PnP-X is a set of extensions to Plug and Play in Windows Vista that support network-connected devices. PnP X allows network-connected devices to appear as devices inside Windows and provides an installation experience that is similar to attaching a bus-connected device.

“Discovery” refers to how PnP X determines that a device is present. For bus-connected devices, Plug and Play discovery is done through PCI, USB, and other types of physical bus enumerators. In Windows Vista, PnP-X extends Plug and Plug by using the IP bus enumerator service, which uses networking protocols and the local area network (LAN) connection to determine the presence of DPWS and UPnP-capable devices.

The components of PnP X device association framework allow network-connected devices to be discovered, associated, and installed on a PC client as if they were bus-connected. This framework consists of components such as:

-   Discovery providers, including an SSDP provider and a WS Discovery provider
-   An association UI
-   The IP bus enumerator service

This image shows the relationship between the PnP X components and function discovery. In this figure, PnP X components are represented as rectangles and function discovery categories are represented as circles. All communication is performed through function discovery, which reduces or eliminates the need for new interprocess interfaces. For information about how providers invoke function discovery, see [Function Discovery](fd-portal.md).

![pnpx](https://www.bing.com/search?q=pnpx)

Specification link: [PnP-X: Plug and Play Extensions for Windows](http://msdn.microsoft.com/library/windows/hardware/gg463082.aspx)

### Implementing DPWS Support for PnP-X Devices

DPWS is based on the standard application-to-application communication protocol for most Internet services, to ensure rich discovery, control, and eventing experiences. For a device that implements PnP-X by way of DPWS, the requirements are defined in Web Services specifications.

To incorporate PnP X, the DPWS-capable device must: The user selects the device and chooses to install it. The Plug and Play process for matching INF files is the same as the process for UPnP devices.

-   Support DPWS and Web Services Dynamic Discovery.
-   Be capable of retrieving the metadata for the device and extracting eXtensible markup language (XML) elements. PnP-X: Plug and Play Extensions for Windows is the specification that defines the device metadata XML elements that PnP X requires for device installation.
-   Be capable of creating a series of hardware IDs and compatible IDs from the XML.

WS Discovery manages the exchange of metadata between the device and Windows.

### Implementing UPnP Support for PnP-X Devices

UPnP has been adopted widely for devices that interact in home network A/V scenarios. Adding PnP-X technology advances the capabilities and usability of devices that connect to a Windows PC. To be able to incorporate PnP X capabilities, UPnP-based devices must implement the core UPnP protocols: discovery, descrip¬tion, control, and notifications, including UPnP device metadata mapping. With PnP X, the device installation process for UPnP devices on Windows is as follows:

1.  The Windows Vista PC discovers the device—for example, when a new IP printer is connected to the home network.
2.  The user selects the device in Network Explorer (double-click or right-click and click Install).
3.  IP Bus Enumeration Service creates a physical device object (PDO) for the device.
4.  Plug and Play begins installation of the device.
5.  Plug and Play uses INF files to search the driver store for a matching driver package.
6.  The Found New Hardware Wizard helps the user through the association process.
7.  If the device requires a driver, the Found New Hardware Wizard prompts the user to install the driver.
8.  Windows initializes the device and creates a functional device object (FDO) that stores the device’s property information.

### Implementing Driver Support for PnP-X Devices

Windows Vista includes built-in drivers that can be used for network-connected devices such as a WSD printer and UPnP Content Directory Services media server. If the manufacturer creates a custom driver, it is typically a user-mode component—such as a Windows Sockets application—that exposes APIs to applications.

## Related topics

<dl> <dt>

[PnP-X Association Database Reference](pnp-x-association-database-reference.md)
</dt> </dl>

 

 




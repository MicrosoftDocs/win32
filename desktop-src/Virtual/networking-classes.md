---
title: Networking Classes
description: The networking architecture for virtualization models the physical networking architecture. It uses standard networking objects such as switches, switch ports, and network adapters.
ms.assetid: 'da194bee-fb0d-4ef8-ab25-733a381d42e0'
---

# Networking Classes

The networking architecture for virtualization models the physical networking architecture. It uses standard networking objects such as switches, switch ports, and network adapters.

The following are virtualization WMI classes related to networking.

## In this section



| Topic                                                                                                      | Description                                                                                                                                                                                                                                                          |
|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Msvm\_ActiveConnection**](msvm-activeconnection.md)<br/>                                         | Connects a switch port to the LAN endpoint to which the port is connected.<br/>                                                                                                                                                                                |
| [**Msvm\_BindsTo**](msvm-bindsto.md)<br/>                                                           | An association that establishes a service access point (SAP) as a requester of protocol services from a protocol endpoint.<br/>                                                                                                                                |
| [**Msvm\_DeviceSAPImplementation**](msvm-devicesapimplementation.md)<br/>                           | An association between a service access point (SAP) and how it is implemented.<br/>                                                                                                                                                                            |
| [**Msvm\_DynamicForwardingEntry**](msvm-dynamicforwardingentry.md)<br/>                             | Represents an entry in the forwarding (filtering) database that is associated with the transparent bridging service.<br/>                                                                                                                                      |
| [**Msvm\_EmulatedEthernetPort**](msvm-emulatedethernetport.md)<br/>                                 | Represents an emulated Ethernet adapter.<br/>                                                                                                                                                                                                                  |
| [**Msvm\_EmulatedEthernetPortSettingData**](msvm-emulatedethernetportsettingdata.md)<br/>           | Represents the configured state of an emulated Ethernet adapter.<br/>                                                                                                                                                                                          |
| [**Msvm\_ExternalEthernetPort**](msvm-externalethernetport.md)<br/>                                 | Represents an external Ethernet port (network adapter).<br/>                                                                                                                                                                                                   |
| [**Msvm\_GlobalEthernetPortSAPImplementation**](msvm-globalethernetportsapimplementation.md)<br/>   | An association that connects a LAN endpoint to a global Ethernet port (either an external or internal Ethernet port).<br/>                                                                                                                                     |
| [**Msvm\_HostedAccessPoint**](msvm-hostedaccesspoint.md)<br/>                                       | An association that connects a virtual switch service to a switch port inside of the Microsoft Hyper-V platform.<br/>                                                                                                                                          |
| [**Msvm\_HostedSwitchService**](msvm-hostedswitchservice.md)<br/>                                   | An association that connects a virtual switch service to transparent bridging service.<br/>                                                                                                                                                                    |
| [**Msvm\_InternalEthernetPort**](msvm-internalethernetport.md)<br/>                                 | Represents an internal Ethernet port (network adapter).<br/>                                                                                                                                                                                                   |
| [**Msvm\_NetworkElementSettingData**](msvm-networkelementsettingdata.md)<br/>                       | An association that connects a computer system to a LAN endpoint inside of Hyper-V.<br/>                                                                                                                                                                       |
| [**Msvm\_NetworkJob**](msvm-networkjob.md)<br/>                                                     | Represents a network operation job created by the Network VSP WMI management service.<br/>                                                                                                                                                                     |
| [**Msvm\_SwitchLANEndpoint**](msvm-switchlanendpoint.md)<br/>                                       | Represents the logical connection point for a network adapter.<br/>                                                                                                                                                                                            |
| [**Msvm\_SwitchPort**](msvm-switchport.md)<br/>                                                     | Represents a port on the switch.<br/>                                                                                                                                                                                                                          |
| [**Msvm\_SwitchPortDynamicForwarding**](msvm-switchportdynamicforwarding.md)<br/>                   | Connects a switch port to a dynamic forward entry (learned MAC address).<br/>                                                                                                                                                                                  |
| [**Msvm\_SyntheticEthernetPort**](msvm-syntheticethernetport.md)<br/>                               | Represents a synthetic Ethernet adapter.<br/>                                                                                                                                                                                                                  |
| [**Msvm\_SyntheticEthernetPortSettingData**](msvm-syntheticethernetportsettingdata.md)<br/>         | Represents the configured state of a synthetic Ethernet adapter.<br/>                                                                                                                                                                                          |
| [**Msvm\_TransparentBridgingDynamicForwarding**](msvm-transparentbridgingdynamicforwarding.md)<br/> | Connects a transparent bridging service to a dynamic forward entry (learned MAC address).<br/>                                                                                                                                                                 |
| [**Msvm\_TransparentBridgingService**](msvm-transparentbridgingservice.md)<br/>                     | Serves as a placeholder for the service inside the switch that learns MAC addresses and serves as a bridge between the [**Msvm\_VirtualSwitch**](msvm-virtualswitch.md) and [**Msvm\_DynamicForwardingEntry**](msvm-dynamicforwardingentry.md) classes.<br/> |
| [**Msvm\_VirtualSwitch**](msvm-virtualswitch.md)<br/>                                               | Represents a virtual switch.<br/>                                                                                                                                                                                                                              |
| [**Msvm\_VirtualSwitchManagementService**](msvm-virtualswitchmanagementservice.md)<br/>             | Controls the definition, modification, and destruction of global networking resources such as virtual switches, switch ports, and internal Ethernet ports.<br/>                                                                                                |
| [**Msvm\_VLANEndpoint**](msvm-vlanendpoint.md)<br/>                                                 | Represents the VLAN endpoint of a switch port.<br/>                                                                                                                                                                                                            |
| [**Msvm\_VLANEndpointSettingData**](msvm-vlanendpointsettingdata.md)<br/>                           | Represents the settings for a VLAN endpoint of a switch port.<br/>                                                                                                                                                                                             |
| [**Msvm\_VmLANEndpoint**](msvm-vmlanendpoint.md)<br/>                                               | Represents the logical connection point for a network adapter.<br/>                                                                                                                                                                                            |



 

## Related topics

<dl> <dt>

[Virtualization WMI Classes](virtualization-wmi-classes.md)
</dt> </dl>

 

 






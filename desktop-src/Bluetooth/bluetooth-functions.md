---
title: Bluetooth Functions
description: The functions in this section are used for managing Bluetooth devices and services.
ms.assetid: '5cd4a050-51f3-40f4-b434-be639e109f0f'
keywords: ["Bluetooth, reference, functions"]
---

# Bluetooth Functions

The functions in this section are used for managing Bluetooth devices and services.

Bluetooth is also supported by using the Windows Sockets programming interface. For more information about programming Bluetooth by using the Windows Sockets interface, see [Windows Sockets Support for Bluetooth](windows-sockets-support-for-bluetooth.md).



| Section                                                                                | Content                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BluetoothAuthenticateDevice**](bluetoothauthenticatedevice.md)                     | Sends an authentication request to a remote Bluetooth device.                                                                                                                                 |
| [**BluetoothAuthenticateDeviceEx**](bluetoothauthenticatedeviceex.md)                 | Sends an authentication request to a remote Bluetooth device. Additionally, this function allows for out-of-band data to be passed into the function call for the device being authenticated. |
| [**BluetoothAuthenticateMultipleDevices**](bluetoothauthenticatemultipledevices.md)   | Enables the caller to prompt for multiple devices to be authenticated during a single instance of the Bluetooth Connection Wizard.                                                            |
| [**BluetoothDisplayDeviceProperties**](bluetoothdisplaydeviceproperties.md)           | Invokes the Control Panel device information property sheet.                                                                                                                                  |
| [**BluetoothEnableDiscovery**](bluetoothenablediscovery.md)                           | Changes the discovery state of a local Bluetooth radio or radios.                                                                                                                             |
| [**BluetoothEnableIncomingConnections**](bluetoothenableincomingconnections.md)       | Modifies whether a local Bluetooth radio accepts incoming connections.                                                                                                                        |
| [**BluetoothEnumerateInstalledServices**](bluetoothenumerateinstalledservices.md)     | Enumerates the GUIDs (globally unique identifiers) of the services that are enabled on a Bluetooth device.                                                                                    |
| [**BluetoothFindDeviceClose**](bluetoothfinddeviceclose.md)                           | Closes an enumeration handle that is associated with a device query.                                                                                                                          |
| [**BluetoothFindFirstDevice**](bluetoothfindfirstdevice.md)                           | Begins the enumeration of local Bluetooth devices.                                                                                                                                            |
| [**BluetoothFindFirstRadio**](bluetoothfindfirstradio.md)                             | Begins the enumeration of local Bluetooth radios.                                                                                                                                             |
| [**BluetoothFindNextDevice**](bluetoothfindnextdevice.md)                             | Finds the next Bluetooth device.                                                                                                                                                              |
| [**BluetoothFindNextRadio**](bluetoothfindnextradio.md)                               | Finds the next Bluetooth radio.                                                                                                                                                               |
| [**BluetoothFindRadioClose**](bluetoothfindradioclose.md)                             | Closes the enumeration handle that is associated with finding Bluetooth radios.                                                                                                               |
| [**BluetoothGetDeviceInfo**](bluetoothgetdeviceinfo.md)                               | Retrieves information about a remote Bluetooth device. The Bluetooth device must have been previously identified through a successful device inquiry function call.                           |
| [**BluetoothGetRadioInfo**](bluetoothgetradioinfo.md)                                 | Obtains information about a Bluetooth radio.                                                                                                                                                  |
| [**BluetoothIsConnectable**](bluetoothisconnectable.md)                               | Determines whether a Bluetooth radio or radios is connectable.                                                                                                                                |
| [**BluetoothIsDiscoverable**](bluetoothisdiscoverable.md)                             | Determines whether a Bluetooth radio or radios is discoverable.                                                                                                                               |
| [**BluetoothRegisterForAuthentication**](bluetoothregisterforauthentication.md)       | Registers a callback function that is called when a particular Bluetooth device requests authentication.                                                                                      |
| [**BluetoothRegisterForAuthenticationEx**](bluetoothregisterforauthenticationex.md)   | Registers an application for a pin request, numeric comparison and callback function.                                                                                                         |
| [**BluetoothRemoveDevice**](bluetoothremovedevice.md)                                 | Removes authentication between a Bluetooth device and the computer, purging any cached information about the device.                                                                          |
| [**BluetoothSdpEnumAttributes**](bluetoothsdpenumattributes.md)                       | Enumerates through the SDP record stream and calls the callback function for each attribute in the record.                                                                                    |
| [**BluetoothSdpGetAttributeValue**](bluetoothsdpgetattributevalue.md)                 | Retrieves the attribute value for an attribute identifier.                                                                                                                                    |
| [**BluetoothSdpGetContainerElementData**](bluetoothsdpgetcontainerelementdata.md)     | Iterates over a container stream and returns each element that is contained within the container element.                                                                                     |
| [**BluetoothSdpGetElementData**](bluetoothsdpgetelementdata.md)                       | Retrieves and parses a single element from an SDP stream.                                                                                                                                     |
| [**BluetoothSdpGetString**](bluetoothsdpgetstring.md)                                 | Converts a raw string that is embedded in the SDP record into a Unicode string.                                                                                                               |
| [**BluetoothSelectDevices**](bluetoothselectdevices.md)                               | Enables Bluetooth device selection.                                                                                                                                                           |
| [**BluetoothSelectDevicesFree**](bluetoothselectdevicesfree.md)                       | Frees resources associated with a previous call to the [**BluetoothSelectDevices**](bluetoothselectdevices.md) function.                                                                     |
| [**BluetoothSendAuthenticationResponse**](bluetoothsendauthenticationresponse.md)     | Called when an authentication request to send the passkey response is received.                                                                                                               |
| [**BluetoothSendAuthenticationResponseEx**](bluetoothsendauthenticationresponseex.md) | Called when an authentication request to send the passkey or numeric comparison response is received.                                                                                         |
| [**BluetoothSetLocalServiceInfo**](bluetoothsetlocalserviceinfo.md)                   | Sets local service information for a specific Bluetooth radio.                                                                                                                                |
| [**BluetoothSetServiceState**](bluetoothsetservicestate.md)                           | Enables or disables services for a Bluetooth device.                                                                                                                                          |
| [**BluetoothUnregisterAuthentication**](bluetoothunregisterauthentication.md)         | Removes registration for a callback routine that was previously registered with a call to the [**BluetoothRegisterForAuthentication**](bluetoothregisterforauthentication.md) function.      |
| [**BluetoothUpdateDeviceRecord**](bluetoothupdatedevicerecord.md)                     | Updates the local computer cache about a Bluetooth device.                                                                                                                                    |



 

 

 





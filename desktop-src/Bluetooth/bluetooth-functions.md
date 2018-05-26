---
title: Bluetooth Functions
description: The functions in this section are used for managing Bluetooth devices and services.
ms.assetid: 5cd4a050-51f3-40f4-b434-be639e109f0f
keywords:
- Bluetooth, reference, functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Bluetooth Functions

The functions in this section are used for managing Bluetooth devices and services.

Bluetooth is also supported by using the Windows Sockets programming interface. For more information about programming Bluetooth by using the Windows Sockets interface, see [Windows Sockets Support for Bluetooth](windows-sockets-support-for-bluetooth.md).



| Section                                                                                | Content                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BluetoothAuthenticateDevice**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothauthenticatedevice?branch=master)                     | Sends an authentication request to a remote Bluetooth device.                                                                                                                                 |
| [**BluetoothAuthenticateDeviceEx**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothauthenticatedeviceex?branch=master)                 | Sends an authentication request to a remote Bluetooth device. Additionally, this function allows for out-of-band data to be passed into the function call for the device being authenticated. |
| [**BluetoothAuthenticateMultipleDevices**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothauthenticatemultipledevices?branch=master)   | Enables the caller to prompt for multiple devices to be authenticated during a single instance of the Bluetooth Connection Wizard.                                                            |
| [**BluetoothDisplayDeviceProperties**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothdisplaydeviceproperties?branch=master)           | Invokes the Control Panel device information property sheet.                                                                                                                                  |
| [**BluetoothEnableDiscovery**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothenablediscovery?branch=master)                           | Changes the discovery state of a local Bluetooth radio or radios.                                                                                                                             |
| [**BluetoothEnableIncomingConnections**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothenableincomingconnections?branch=master)       | Modifies whether a local Bluetooth radio accepts incoming connections.                                                                                                                        |
| [**BluetoothEnumerateInstalledServices**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothenumerateinstalledservices?branch=master)     | Enumerates the GUIDs (globally unique identifiers) of the services that are enabled on a Bluetooth device.                                                                                    |
| [**BluetoothFindDeviceClose**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothfinddeviceclose?branch=master)                           | Closes an enumeration handle that is associated with a device query.                                                                                                                          |
| [**BluetoothFindFirstDevice**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothfindfirstdevice?branch=master)                           | Begins the enumeration of local Bluetooth devices.                                                                                                                                            |
| [**BluetoothFindFirstRadio**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothfindfirstradio?branch=master)                             | Begins the enumeration of local Bluetooth radios.                                                                                                                                             |
| [**BluetoothFindNextDevice**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothfindnextdevice?branch=master)                             | Finds the next Bluetooth device.                                                                                                                                                              |
| [**BluetoothFindNextRadio**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothfindnextradio?branch=master)                               | Finds the next Bluetooth radio.                                                                                                                                                               |
| [**BluetoothFindRadioClose**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothfindradioclose?branch=master)                             | Closes the enumeration handle that is associated with finding Bluetooth radios.                                                                                                               |
| [**BluetoothGetDeviceInfo**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothgetdeviceinfo?branch=master)                               | Retrieves information about a remote Bluetooth device. The Bluetooth device must have been previously identified through a successful device inquiry function call.                           |
| [**BluetoothGetRadioInfo**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothgetradioinfo?branch=master)                                 | Obtains information about a Bluetooth radio.                                                                                                                                                  |
| [**BluetoothIsConnectable**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothisconnectable?branch=master)                               | Determines whether a Bluetooth radio or radios is connectable.                                                                                                                                |
| [**BluetoothIsDiscoverable**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothisdiscoverable?branch=master)                             | Determines whether a Bluetooth radio or radios is discoverable.                                                                                                                               |
| [**BluetoothRegisterForAuthentication**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothregisterforauthentication?branch=master)       | Registers a callback function that is called when a particular Bluetooth device requests authentication.                                                                                      |
| [**BluetoothRegisterForAuthenticationEx**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothregisterforauthenticationex?branch=master)   | Registers an application for a pin request, numeric comparison and callback function.                                                                                                         |
| [**BluetoothRemoveDevice**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothremovedevice?branch=master)                                 | Removes authentication between a Bluetooth device and the computer, purging any cached information about the device.                                                                          |
| [**BluetoothSdpEnumAttributes**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothsdpenumattributes?branch=master)                       | Enumerates through the SDP record stream and calls the callback function for each attribute in the record.                                                                                    |
| [**BluetoothSdpGetAttributeValue**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothsdpgetattributevalue?branch=master)                 | Retrieves the attribute value for an attribute identifier.                                                                                                                                    |
| [**BluetoothSdpGetContainerElementData**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothsdpgetcontainerelementdata?branch=master)     | Iterates over a container stream and returns each element that is contained within the container element.                                                                                     |
| [**BluetoothSdpGetElementData**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothsdpgetelementdata?branch=master)                       | Retrieves and parses a single element from an SDP stream.                                                                                                                                     |
| [**BluetoothSdpGetString**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothsdpgetstring?branch=master)                                 | Converts a raw string that is embedded in the SDP record into a Unicode string.                                                                                                               |
| [**BluetoothSelectDevices**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothselectdevices?branch=master)                               | Enables Bluetooth device selection.                                                                                                                                                           |
| [**BluetoothSelectDevicesFree**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothselectdevicesfree?branch=master)                       | Frees resources associated with a previous call to the [**BluetoothSelectDevices**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothselectdevices?branch=master) function.                                                                     |
| [**BluetoothSendAuthenticationResponse**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothsendauthenticationresponse?branch=master)     | Called when an authentication request to send the passkey response is received.                                                                                                               |
| [**BluetoothSendAuthenticationResponseEx**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothsendauthenticationresponseex?branch=master) | Called when an authentication request to send the passkey or numeric comparison response is received.                                                                                         |
| [**BluetoothSetLocalServiceInfo**](/windows/win32/BluetoothAPIs/?branch=master)                   | Sets local service information for a specific Bluetooth radio.                                                                                                                                |
| [**BluetoothSetServiceState**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothsetservicestate?branch=master)                           | Enables or disables services for a Bluetooth device.                                                                                                                                          |
| [**BluetoothUnregisterAuthentication**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothunregisterauthentication?branch=master)         | Removes registration for a callback routine that was previously registered with a call to the [**BluetoothRegisterForAuthentication**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothregisterforauthentication?branch=master) function.      |
| [**BluetoothUpdateDeviceRecord**](/windows/win32/BluetoothAPIs/nf-bluetoothapis-bluetoothupdatedevicerecord?branch=master)                     | Updates the local computer cache about a Bluetooth device.                                                                                                                                    |



 

 

 





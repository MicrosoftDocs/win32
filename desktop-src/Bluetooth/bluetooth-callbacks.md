---
title: Bluetooth Callbacks
description: The Bluetooth callback functions in this section are used in combination with functions that make it possible to manage Bluetooth devices and services.
ms.assetid: a66f88e2-46f7-4e23-9b61-7ee35abec207
ms.topic: article
ms.date: 05/31/2018
---

# Bluetooth Callbacks

The Bluetooth callback functions in this section are used in combination with functions that make it possible to manage Bluetooth devices and services.

Bluetooth is also supported by using the Windows Sockets programming interface. For more information about programming Bluetooth by using the Windows Sockets interface, see [Windows Sockets Support for Bluetooth](windows-sockets-support-for-bluetooth.md).



| Section                                                                                      | Content                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PFN\_AUTHENTICATION\_CALLBACK**](/windows/desktop/api/BluetoothAPIs/nc-bluetoothapis-pfn_authentication_callback)                         | Used in conjunction with the [**BluetoothRegisterForAuthentication**](/windows/desktop/api/BluetoothAPIs/nf-bluetoothapis-bluetoothregisterforauthentication) function.                                                  |
| [**PFN\_AUTHENTICATION\_CALLBACK\_EX**](/windows/desktop/api/BluetoothAPIs/nc-bluetoothapis-pfn_authentication_callback_ex)                  | Used in conjunction with the [**BluetoothRegisterForAuthenticationEx**](/windows/desktop/api/BluetoothAPIs/nf-bluetoothapis-bluetoothregisterforauthenticationex) function.                                              |
| [**PFN\_BLUETOOTH\_ENUM\_ATTRIBUTES\_CALLBACK**](/windows/desktop/api/BluetoothAPIs/nc-bluetoothapis-pfn_bluetooth_enum_attributes_callback) | Called once for each attribute found in the *pSDPStream* parameter that is passed to the [**BluetoothSdpEnumAttributes**](/windows/desktop/api/BluetoothAPIs/nf-bluetoothapis-bluetoothsdpenumattributes) function call. |
| [**PFN\_DEVICE\_CALLBACK**](/windows/desktop/api/BluetoothAPIs/nc-bluetoothapis-pfn_device_callback)                                         | Used in association with selecting Bluetooth devices.                                                                                                                    |



 

 

 





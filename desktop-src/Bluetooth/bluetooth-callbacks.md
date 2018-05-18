---
title: Bluetooth Callbacks
description: The Bluetooth callback functions in this section are used in combination with functions that make it possible to manage Bluetooth devices and services.
ms.assetid: 'a66f88e2-46f7-4e23-9b61-7ee35abec207'
---

# Bluetooth Callbacks

The Bluetooth callback functions in this section are used in combination with functions that make it possible to manage Bluetooth devices and services.

Bluetooth is also supported by using the Windows Sockets programming interface. For more information about programming Bluetooth by using the Windows Sockets interface, see [Windows Sockets Support for Bluetooth](windows-sockets-support-for-bluetooth.md).



| Section                                                                                      | Content                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PFN\_AUTHENTICATION\_CALLBACK**](pfn-authentication-callback.md)                         | Used in conjunction with the [**BluetoothRegisterForAuthentication**](bluetoothregisterforauthentication.md) function.                                                  |
| [**PFN\_AUTHENTICATION\_CALLBACK\_EX**](pfn-authentication-callback-ex.md)                  | Used in conjunction with the [**BluetoothRegisterForAuthenticationEx**](bluetoothregisterforauthenticationex.md) function.                                              |
| [**PFN\_BLUETOOTH\_ENUM\_ATTRIBUTES\_CALLBACK**](pfn-bluetooth-enum-attributes-callback.md) | Called once for each attribute found in the *pSDPStream* parameter that is passed to the [**BluetoothSdpEnumAttributes**](bluetoothsdpenumattributes.md) function call. |
| [**PFN\_DEVICE\_CALLBACK**](pfn-device-callback.md)                                         | Used in association with selecting Bluetooth devices.                                                                                                                    |



 

 

 





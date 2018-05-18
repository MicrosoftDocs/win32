---
title: Bluetooth and WM\_DEVICECHANGE Messages
description: Bluetooth includes specific WM\_DEVICECHANGE messages that enable developers to obtain messages when Bluetooth devices undergo status changes.
ms.assetid: '7dab37a6-63ac-4377-9884-61dd19972433'
---

# Bluetooth and WM\_DEVICECHANGE Messages

Bluetooth includes specific [**WM\_DEVICECHANGE**](https://msdn.microsoft.com/library/windows/desktop/aa363480) messages that enable developers to obtain messages when Bluetooth devices undergo status changes. This topic describes how to receive Bluetooth-specific **WM\_DEVICECHANGE** messages and lists Bluetooth-specific messages.

## Receiving Bluetooth-specific WM\_DEVICECHANGE Messages

To receive [**WM\_DEVICECHANGE**](https://msdn.microsoft.com/library/windows/desktop/aa363480) messages, a handle to the local radio must first be opened. To do this, use one of the following methods:

-   Use the [SetupDiGetClassDevs](http://go.microsoft.com/fwlink/p/?linkid=91493) function with the following parameters: (GUID\_BTHPORT\_DEVICE\_INTERFACE, …, DIGCF\_PRESENT \| DIGCF\_DEVICEINTERFACE), then use the [SetupDiEnumDeviceInterfaces](http://go.microsoft.com/fwlink/p/?linkid=91492), [SetupDiGetDeviceInterfaceDetail](http://go.microsoft.com/fwlink/p/?linkid=91494), [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858), and the [SetupDiDestroyDeviceInfoList](http://go.microsoft.com/fwlink/p/?linkid=91491) functions.
-   Use the [**BluetoothFindFirstRadio**](bluetoothfindfirstradio.md), [**BluetoothFindNextRadio**](bluetoothfindnextradio.md), and [**BluetoothFindRadioClose**](bluetoothfindradioclose.md) functions.

When the Bluetooth radio handle is opened, call the [**RegisterDeviceNotification**](https://msdn.microsoft.com/library/windows/desktop/aa363431) function and register for notifications on the handle using **DBT\_DEVTYP\_HANDLE** as the devicetype. When registered, the following GUIDs are sent, and the [**DEV\_BROADCAST\_HANDLE**](https://msdn.microsoft.com/library/windows/desktop/aa363245)::**dbch\_data** member is the associated buffer.

## Bluetooth-specific Messages

The following table lists Bluetooth-specific [**WM\_DEVICECHANGE**](https://msdn.microsoft.com/library/windows/desktop/aa363480) messages.

| GUID                                   | BUFFER                                                  | Description                                                                                                                                                                                                                                                                                                                                                      |
|----------------------------------------|---------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GUID\_BLUETOOTH\_HCI\_EVENT            | [**BTH\_HCI\_EVENT\_INFO**](bth-hci-event-info.md)     | This message is sent when a remote Bluetooth device connects or disconnects at the ACL level.                                                                                                                                                                                                                                                                    |
| GUID\_BLUETOOTH\_L2CAP\_EVENT          | [**BTH\_L2CAP\_EVENT\_INFO**](bth-l2cap-event-info.md) | This message is sent when an L2CAP channel between the local radio and a remote Bluetooth device has been established or terminated. For L2CAP channels that are multiplexers, such as RFCOMM, this message is only sent when the underlying channel is established, not when each multiplexed channel, such as an RFCOMM channel, is established or terminated. |
| GUID\_BLUETOOTH\_PIN\_REQUEST          | Not applicable.                                         | This message should be ignored by the application. If the application must receive PIN requests, the [**BluetoothRegisterForAuthentication**](bluetoothregisterforauthentication.md) function should be used.                                                                                                                                                   |
| GUID\_BLUETOOTH\_RADIO\_IN\_RANGE      | [**BTH\_RADIO\_IN\_RANGE**](bth-radio-in-range.md)     | This message is sent when any of the following attributes of a remote Bluetooth device has changed: the device has been discovered, the class of device, name, connected state, or device remembered state. This message is also sent when these attributes are set or cleared.                                                                                  |
| GUID\_BLUETOOTH\_RADIO\_OUT\_OF\_RANGE | [**BLUETOOTH\_ADDRESS**](bluetooth-address.md)         | This message is sent when a previously discovered device has not been found after the completion of the last inquiry. This message will not be sent for remembered devices. The **BTH\_ADDRESS** structure is the address of the device that was not found.                                                                                                      |



 

## Related topics

<dl> <dt>

[**BluetoothFindFirstRadio**](bluetoothfindfirstradio.md)
</dt> <dt>

[**BluetoothFindNextRadio**](bluetoothfindnextradio.md)
</dt> <dt>

[**BluetoothFindRadioClose**](bluetoothfindradioclose.md)
</dt> <dt>

[**RegisterDeviceNotification**](https://msdn.microsoft.com/library/windows/desktop/aa363431)
</dt> <dt>

[SetupDiDestroyDeviceInfoList](http://go.microsoft.com/fwlink/p/?linkid=91491)
</dt> <dt>

[SetupDiEnumDeviceInterfaces](http://go.microsoft.com/fwlink/p/?linkid=91492)
</dt> <dt>

[SetupDiGetClassDevs](http://go.microsoft.com/fwlink/p/?linkid=91493)
</dt> <dt>

[**BLUETOOTH\_ADDRESS**](bluetooth-address.md)
</dt> <dt>

[**BTH\_HCI\_EVENT\_INFO**](bth-hci-event-info.md)
</dt> <dt>

[**BTH\_L2CAP\_EVENT\_INFO**](bth-l2cap-event-info.md)
</dt> <dt>

[**BTH\_RADIO\_IN\_RANGE**](bth-radio-in-range.md)
</dt> <dt>

[**DEV\_BROADCAST\_HANDLE**](https://msdn.microsoft.com/library/windows/desktop/aa363245)
</dt> <dt>

[**WM\_DEVICECHANGE**](https://msdn.microsoft.com/library/windows/desktop/aa363480)
</dt> </dl>

 

 





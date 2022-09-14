---
title: Bluetooth and WM_DEVICECHANGE Messages
description: Bluetooth includes specific WM\_DEVICECHANGE messages that enable developers to obtain messages when Bluetooth devices undergo status changes.
ms.assetid: 7dab37a6-63ac-4377-9884-61dd19972433
ms.topic: article
ms.date: 05/31/2018
---

# Bluetooth and WM\_DEVICECHANGE Messages

Bluetooth includes specific [**WM\_DEVICECHANGE**](/windows/desktop/DevIO/wm-devicechange) messages that enable developers to obtain messages when Bluetooth devices undergo status changes. This topic describes how to receive Bluetooth-specific **WM\_DEVICECHANGE** messages and lists Bluetooth-specific messages.

## Receiving Bluetooth-specific WM\_DEVICECHANGE Messages

To receive [**WM\_DEVICECHANGE**](/windows/desktop/DevIO/wm-devicechange) messages, a handle to the local radio must first be opened. To do this, use one of the following methods:

-   Use the [SetupDiGetClassDevs](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdevsw) function with the following parameters: (GUID\_BTHPORT\_DEVICE\_INTERFACE, …, DIGCF\_PRESENT \| DIGCF\_DEVICEINTERFACE), then use the [SetupDiEnumDeviceInterfaces](/windows/win32/api/setupapi/nf-setupapi-setupdienumdeviceinterfaces), [SetupDiGetDeviceInterfaceDetail](https://msdn.microsoft.com/library/ms792901.aspx), [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea), and the [SetupDiDestroyDeviceInfoList](/windows/win32/api/setupapi/nf-setupapi-setupdidestroydeviceinfolist) functions.
-   Use the [**BluetoothFindFirstRadio**](/windows/desktop/api/BluetoothAPIs/nf-bluetoothapis-bluetoothfindfirstradio), [**BluetoothFindNextRadio**](/windows/desktop/api/BluetoothAPIs/nf-bluetoothapis-bluetoothfindnextradio), and [**BluetoothFindRadioClose**](/windows/desktop/api/BluetoothAPIs/nf-bluetoothapis-bluetoothfindradioclose) functions.

When the Bluetooth radio handle is opened, call the [**RegisterDeviceNotification**](/windows/desktop/api/winuser/nf-winuser-registerdevicenotificationa) function and register for notifications on the handle using **DBT\_DEVTYP\_HANDLE** as the devicetype. When registered, the following GUIDs are sent, and the [**DEV\_BROADCAST\_HANDLE**](/windows/desktop/api/dbt/ns-dbt-dev_broadcast_handle)::**dbch\_data** member is the associated buffer.

## Bluetooth-specific Messages

The following table lists Bluetooth-specific [**WM\_DEVICECHANGE**](/windows/desktop/DevIO/wm-devicechange) messages.

| GUID                                   | BUFFER                                                  | Description                                                                                                                                                                                                                                                                                                                                                      |
|----------------------------------------|---------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GUID\_BLUETOOTH\_HCI\_EVENT            | [**BTH\_HCI\_EVENT\_INFO**](/windows/desktop/api/Bthdef/ns-bthdef-bth_hci_event_info)     | This message is sent when a remote Bluetooth device connects or disconnects at the ACL level.                                                                                                                                                                                                                                                                    |
| GUID\_BLUETOOTH\_L2CAP\_EVENT          | [**BTH\_L2CAP\_EVENT\_INFO**](/windows/desktop/api/Bthdef/ns-bthdef-bth_l2cap_event_info) | This message is sent when an L2CAP channel between the local radio and a remote Bluetooth device has been established or terminated. For L2CAP channels that are multiplexers, such as RFCOMM, this message is only sent when the underlying channel is established, not when each multiplexed channel, such as an RFCOMM channel, is established or terminated. |
| GUID\_BLUETOOTH\_PIN\_REQUEST          | Not applicable.                                         | This message should be ignored by the application. If the application must receive PIN requests, the [**BluetoothRegisterForAuthentication**](/windows/desktop/api/BluetoothAPIs/nf-bluetoothapis-bluetoothregisterforauthentication) function should be used.                                                                                                                                                   |
| GUID\_BLUETOOTH\_RADIO\_IN\_RANGE      | [**BTH\_RADIO\_IN\_RANGE**](/windows/desktop/api/Bthdef/ns-bthdef-bth_radio_in_range)     | This message is sent when any of the following attributes of a remote Bluetooth device has changed: the device has been discovered, the class of device, name, connected state, or device remembered state. This message is also sent when these attributes are set or cleared.                                                                                  |
| GUID\_BLUETOOTH\_RADIO\_OUT\_OF\_RANGE | [**BLUETOOTH\_ADDRESS**](/windows/win32/api/bluetoothapis/ns-bluetoothapis-bluetooth_address_struct)         | This message is sent when a previously discovered device has not been found after the completion of the last inquiry. This message will not be sent for remembered devices. The **BTH\_ADDRESS** structure is the address of the device that was not found.                                                                                                      |



 

## Related topics

<dl> <dt>

[**BluetoothFindFirstRadio**](/windows/desktop/api/BluetoothAPIs/nf-bluetoothapis-bluetoothfindfirstradio)
</dt> <dt>

[**BluetoothFindNextRadio**](/windows/desktop/api/BluetoothAPIs/nf-bluetoothapis-bluetoothfindnextradio)
</dt> <dt>

[**BluetoothFindRadioClose**](/windows/desktop/api/BluetoothAPIs/nf-bluetoothapis-bluetoothfindradioclose)
</dt> <dt>

[**RegisterDeviceNotification**](/windows/desktop/api/winuser/nf-winuser-registerdevicenotificationa)
</dt> <dt>

[SetupDiDestroyDeviceInfoList](/windows/win32/api/setupapi/nf-setupapi-setupdidestroydeviceinfolist)
</dt> <dt>

[SetupDiEnumDeviceInterfaces](/windows/win32/api/setupapi/nf-setupapi-setupdienumdeviceinterfaces)
</dt> <dt>

[SetupDiGetClassDevs](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdevsw)
</dt> <dt>

[**BLUETOOTH\_ADDRESS**](/windows/win32/api/bluetoothapis/ns-bluetoothapis-bluetooth_address_struct)
</dt> <dt>

[**BTH\_HCI\_EVENT\_INFO**](/windows/desktop/api/Bthdef/ns-bthdef-bth_hci_event_info)
</dt> <dt>

[**BTH\_L2CAP\_EVENT\_INFO**](/windows/desktop/api/Bthdef/ns-bthdef-bth_l2cap_event_info)
</dt> <dt>

[**BTH\_RADIO\_IN\_RANGE**](/windows/desktop/api/Bthdef/ns-bthdef-bth_radio_in_range)
</dt> <dt>

[**DEV\_BROADCAST\_HANDLE**](/windows/desktop/api/dbt/ns-dbt-dev_broadcast_handle)
</dt> <dt>

[**WM\_DEVICECHANGE**](/windows/desktop/DevIO/wm-devicechange)
</dt> </dl>

 

 
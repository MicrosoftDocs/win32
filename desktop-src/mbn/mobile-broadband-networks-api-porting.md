---
description: This section contains the reference material on porting the deprecated Mobile Broadband Win32 APIs to the equivalent Windows Runtime APIs.
title: Guidelines for porting Mobile Broadband Win32 APIs to Windows Runtime APIs
ms.topic: reference
ms.date: 08/23/2021
---

# Guidelines for porting Mobile Broadband Win32 APIs to Windows Runtime APIs

This table lists equivalent Windows Runtime functionality for the deprecated Mobile Broadband Win32 APIs.

| **IMbnConnection** |  Equivalent Windows Runtime functionality |
| - | - |
| Connect | ConnectivityManager.AcquireConnectionAsync |
| Disconnect | ConnectionSession.Close |
| get\_InterfaceID | MobileBroadbandAccount.NetworkAccountId |
| GetActivationNetworkError | MobileBroadbandNetwork.ActivationNetworkError |
| GetConnectionState | WwanConnectionProfileDetails.GetNetworkRegistrationState |
| GetVoiceCallState | MobileBroadbandNetwork.GetVoiceCallSupport, PhoneCallManager.IsCallActive |
| **IMbnConnectionEvents** | |
| OnConnectComplete | NetworkStateChangeEventDetails.HasNewWwanRegistrationState – After notification, the current registration state can be retrieved from WwanConnectionProfileDetails.GetNetworkRegistrationState. |
| OnConnectStateChange | NetworkStateChangeEventDetails.HasNewWwanRegistrationState – After notification, the current registration state can be retrieved from WwanConnectionProfileDetails.GetNetworkRegistrationState. |
| OnDisconnectComplete | NetworkStateChangeEventDetails.HasNewWwanRegistrationState – After notification, the current registration state can be retrieved from WwanConnectionProfileDetails.GetNetworkRegistrationState. |
| OnVoiceCallStateChange | PhoneCallManager.CallStateChanged |
| **IMbnConnectionProfile** | |
| Delete | ConnectionProfile.TryDeleteAsync |
| GetConnectionProfile | NetworkAdapter.GetConnectedProfileAsync |
| GetConnectionProfiles | NetworkInformation.GetConnectionProfiles |
| **IMbnDeviceService** | |
| CloseCommandSession | MobileBroadbandDeviceServiceCommandSession.CloseSession |
| CloseDataSession | MobileBroadbandDeviceServiceDataSession.CloseSession |
| get\_DeviceServiceID | MobileBroadbandDeviceService.DeviceServiceId |
| OpenCommandSession | MobileBroadbandDeviceService.OpenCommandSession |
| OpenDataSession | MobileBroadbandDeviceService.OpenDataSession |
| QueryCommand | MobileBroadbandDeviceServiceCommandSession.SendQueryCommandAsync |
| QuerySupportedCommands | MobileBroadbandDeviceService.SupportedCommands |
| SetCommand | MobileBroadbandDeviceServiceCommandSession.SendSetCommandAsync |
| WriteData | MobileBroadbandDeviceServiceDataSession.WriteDataAsync |
| **IMbnDeviceServicesContext** | |
| EnumerateDeviceServices | MobileBroadbandDeviceService.SupportedCommands |
| get\_MaxCommandSize | MobileBroadbandModem.MaxDeviceServiceCommandSizeInBytes |
| get\_MaxDataSize | MobileBroadbandModem.MaxDeviceServiceDataSizeInByte |
| GetDeviceService | MobileBroadbandModem.GetDeviceService |
| **IMbnDeviceServicesEvents** | |
| OnReadData | MobileBroadbandDeviceServiceDataSession.DataReceived |
| **IMbnInterface** | |
| get\_InterfaceID | MobileBroadbandAccount.NetworkAccountId |
| GetConnection | ConnectionSession obtained from AcquireConnectionAsync |
| GetHomeProvider | MobileBroadbandModem.GetCurrentConfigurationAsync |
| GetInterfaceCapability | MobileBroadbandAccount.CurrentDeviceInformation |
| GetReadyState | MobileBroadbandDeviceInformation.NetworkDeviceStatus |
| GetSubscriberInformation | MobileBroadbandAccount.CurrentDeviceInformation |
| InEmergencyMode | MobileBroadbandModem.IsInEmergencyCallMode |
| **IMbnInterfaceEvents** | |
| OnEmergencyModeChange | MobileBroadbandModem.IsInEmergencyCallModeChanged |
| OnReadyStateChange | MobileBroadbandNetworkRegistrationStateChange |
| OnSubscriberInformationChange | MobileBroadbandAccountUpdatedEventArgs.HasDeviceInformationChanged |
| **IMbnInterfaceManager** | |
| GetInterface | MobileBroadbandModem.CurrentAccount |
| **IMbnInterfaceManagerEvents** | |
| OnInterfaceArrival | MobileBroadbandAccountWatcher.AccountAdded |
| OnInterfaceRemoval | MobileBroadbandAccountWatcher.Account |
| **IMbnMultiCarrier** | |
| GetCurrentCellularClass | MobileBroadbandDeviceInformation.CellularClass |
| **IMbnMultiCarrierEvents** | |
| OnCurrentCellularClassChange | MobileBroadbandAccountUpdatedEventArgs.HasDeviceInformationChanged |
| **IMbnPin** | |
| Change | MobileBroadbandPin.ChangeAsync |
| Disable | MobileBroadbandPin.DisableAsync |
| Enable | MobileBroadbandPin.EnableAsync |
| Enter | MobileBroadbandPin.EnterAsync |
| get\_PinFormat | MobileBroadbandPin.Format |
| get\_PinLengthMax | MobileBroadbandPin.MaxLength |
| get\_PinLengthMin | MobileBroadbandPin.MaxLength |
| get\_PinMode | MobileBroadbandPin.Enabled |
| get\_PinType | MobileBroadbandPin.Type |
| GetPinManager | MobileBroadbandDeviceInformation.PinManager |
| Unblock | MobileBroadbandPin.UnblockAsync |
| **IMbnPinManager** | |
| GetPin | MobileBroadbandPinManager.GetPin |
| GetPinList | MobileBroadbandPinManager.SupportedPins |
| GetPinState | MobileBroadbandPin.LockState |
| **IMbnPinManagerEvents** | |
| **IMbnRadio** | |
| get\_SoftwareRadioState | Radio.GetRadiosAsync – Radio. State |
| SetSoftwareRadioState | Radio.SetStateAsync |
| **IMbnRadioEvents** | |
| OnRadioStateChange | Radio.StateChanged |
| **IMbnRegistration** | |
| GetAvailableDataClasses | MobileBroadbandDeviceInformation.DataClasses |
| GetCurrentDataClass | MobileBroadbandNetwork.RegisteredDataClass |
| GetPacketAttachNetworkError | MobileBroadbandNetwork.PacketAttachNetworkError |
| GetProviderID | MobileBroadbandNetwork.RegisteredProviderId |
| GetProviderName | MobileBroadbandNetwork.RegisteredProviderName |
| GetRegisterState | MobileBroadbandNetwork.NetworkRegistrationState |
| GetRegistrationNetworkError | MobileBroadbandNetwork.ActivationNetworkError |
| **IMbnRegistrationEvents** | |
| OnPacketServiceStateChange | MobileBroadbandNetworkRegistrationStateChange |
| OnRegisterStateChange | MobileBroadbandNetworkRegistrationStateChange |
| GetSignalStrength | ConnectionProfile.GetSignalBar / MobileBroadbandCellLte.ReferenceSignalReceivedPowerInDBm / MobileBroadbandCellGsm.ReceivedSignalStrengthInDBm |
| **IMbnSignalEvents** | |
| **IMbnSms** | |
| GetSmsConfiguration | SmsDevice2.SmscAddress, SmsDevice2.CellularClass, None for CDMAShortMessageSize and MaxMessageIndex which is not required as public API. |
| SetSmsConfiguration | SmsDevice2.SmscAddress, none of the other parameters are supported |
| SmsSendCdma | SendMessageAndGetResultAsync using CellularClass in ISmsMessageBase |
| SmsSendCdmaPdu | SendMessageAndGetResultAsync using Messagetype and CellularClass in ISmsMessageBase |
| SmsSendPdu | SendMessageAndGetResultAsync using MessageType in ISmsMessageBase |
| **IMbnSmsConfiguration** | |
| get\_ServiceCenterAddress | SmsDevice2.SmscAddress |
| get\_SmsFormat | SmsDevice2.CellularClass |
| put\_ServiceCenterAddress | SmsDevice2.SmscAddress |
| **IMbnSmsEvents** | |
| OnSmsNewClass0Message | SmsMessageRegistration.MessageReceived |
| OnSmsSendComplete | SmsSendMessageResult |
| **IMbnSmsReadMsgPdu** | |
| get\_Message | SmsTextMessage2.Body |
| get\_PduData | SmsTextmessage2.Body |
| **IMbnSmsReadMsgTextCdma** | |
| get\_Address | SmsTextMessage2.From |
| get\_EncodingID | SmsTextMessage2.Encoding |
| get\_Message | SmsTextMessage2.Body |
| get\_Timestamp | SmsTextMessage.2Timestamp |
| **IMbnSubscriberInformation** | |
| get\_SimIccID | MobileBroadbandDeviceInformation.SimIccId |
| get\_SubscriberID | MobileBroadbandDeviceInformation.SubscriberId |
| get\_TelephoneNumbers | MobileBroadbandDeviceInformation.TelephoneNumbers |

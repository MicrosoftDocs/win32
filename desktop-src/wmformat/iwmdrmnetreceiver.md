---
title: IWMDRMNetReceiver interface
description: The IWMDRMNetReceiver interface provides methods needed to use Microsoft Windows Media DRM for Network Devices as a receiver.To obtain an instance of this interface, call IWMDRMProvider CreateObject. Pass IID\_IWMDRMNetReceiver as the riid parameter.
ms.assetid: 29966260-c0aa-4e7e-b827-a872c7429333
keywords:
- IWMDRMNetReceiver interface windows Media Format
- IWMDRMNetReceiver interface windows Media Format , described
topic_type:
- apiref
api_name:
- IWMDRMNetReceiver
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IWMDRMNetReceiver interface

The **IWMDRMNetReceiver** interface provides methods needed to use Microsoft Windows Media DRM for Network Devices as a receiver.

To obtain an instance of this interface, call [**IWMDRMProvider::CreateObject**](iwmdrmprovider-createobject.md). Pass **IID\_IWMDRMNetReceiver** as the *riid* parameter.

## Members

The **IWMDRMNetReceiver** interface inherits from [**IWMDRMEventGenerator**](iwmdrmeventgenerator.md). **IWMDRMNetReceiver** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWMDRMNetReceiver** interface has these methods.



| Method                                                                               | Description                                                                                                                     |
|:-------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------|
| [**GetLicenseChallenge**](iwmdrmnetreceiver-getlicensechallenge.md)                 | Generates a license challenge that is sent to the transmitter when requesting protected content.<br/>                     |
| [**GetRegistrationChallenge**](iwmdrmnetreceiver-getregistrationchallenge.md)       | Generates a registration challenge that is sent to the transmitter when the receiver is registering or revalidating.<br/> |
| [**ProcessLicenseResponse**](iwmdrmnetreceiver-processlicenseresponse.md)           | Processes the license response sent by the transmitter in reply to a license challenge.<br/>                              |
| [**ProcessRegistrationResponse**](iwmdrmnetreceiver-processregistrationresponse.md) | Processes the registration response sent by the transmitter in reply to a registration challenge.<br/>                    |



 

## See also

<dl> <dt>

[**Interfaces**](drm-interfaces.md)
</dt> <dt>

[**IWMDRMEventGenerator**](iwmdrmeventgenerator.md)
</dt> <dt>

[**IWMDRMNetTransmitter Interface**](iwmdrmnettransmitter.md)
</dt> </dl>

 

 






---
title: IWMDRMNetTransmitter interface
description: The IWMDRMNetTransmitter interface provides methods needed to use Windows Media DRM for Network Devices as a transmitter.To obtain an instance of this interface, call IWMDRMProvider CreateObject. Pass IID\_IWMDRMNetTransmitter as the riid parameter.
ms.assetid: e93db52a-8829-4d16-b839-824e34b3e582
keywords:
- IWMDRMNetTransmitter interface windows Media Format
- IWMDRMNetTransmitter interface windows Media Format , described
topic_type:
- apiref
api_name:
- IWMDRMNetTransmitter
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IWMDRMNetTransmitter interface

The **IWMDRMNetTransmitter** interface provides methods needed to use Windows Media DRM for Network Devices as a transmitter.

To obtain an instance of this interface, call [**IWMDRMProvider::CreateObject**](iwmdrmprovider-createobject.md). Pass **IID\_IWMDRMNetTransmitter** as the *riid* parameter.

## Members

The **IWMDRMNetTransmitter** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IWMDRMNetTransmitter** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWMDRMNetTransmitter** interface has these methods.



| Method                                                                        | Description                                                                                                 |
|:------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------|
| [**GetLeafLicenseResponse**](iwmdrmnettransmitter-getleaflicenseresponse.md) | Generates a leaf license response message.<br/>                                                       |
| [**GetRootLicenseResponse**](iwmdrmnettransmitter-getrootlicenseresponse.md) | Generates a root license response message<br/>                                                        |
| [**SetLicenseChallenge**](iwmdrmnettransmitter-setlicensechallenge.md)       | Processes a license challenge sent by a Microsoft Windows Media DRM for Network Devices receiver<br/> |



 

## See also

<dl> <dt>

[**Interfaces**](drm-interfaces.md)
</dt> <dt>

[**IWMDRMNetReceiver Interface**](iwmdrmnetreceiver.md)
</dt> </dl>

 


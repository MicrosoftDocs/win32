---
title: Updating Portable Devices
description: Updating Portable Devices
ms.assetid: 2827e71b-f5e9-4403-9763-043239c4a216
keywords:
- Windows Media Player online stores,updating portable devices
- online stores,updating portable devices
- type 1 online stores,updating portable devices
- Windows Media Player online stores,portable devices
- online stores,portable devices
- type 1 online stores,portable devices
- updating portable devices
- portable devices,updating
- portable devices,Windows Media Player online stores
ms.topic: article
ms.date: 05/31/2018
---

# Updating Portable Devices

Windows Media Player enables users to synchronize digital media content with portable devices. This can include music content purchased or rented from an online store. Under some circumstances, online store providers might want to write code to work on a connected portable device as part of managing content provided by the store. To give the online store plug-in the opportunity to work with a connected device, Windows Media Player calls [IWMPContentPartner::UpdateDevice](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-updatedevice) and provides the canonical name of the portable device. If the plug-in code determines that some work must be done with the connected device, it must immediately return S\_OK from the call to **UpdateDevice** before proceeding to do the work. If there is no work to do, the plug-in should return an error code.

When the plug-in has finished using the device, it must call [IWMPContentPartnerCallback::UpdateDeviceComplete](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartnercallback-updatedevicecomplete) to notify Windows Media Player that the device is available.

## Related topics

<dl> <dt>

[**Programming Guide for Type 1 Online Stores**](programming-guide-for-type-1-online-stores.md)
</dt> </dl>

 

 





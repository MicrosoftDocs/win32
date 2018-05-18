---
title: Type 1 Online Store Plug-in
description: Type 1 Online Store Plug-in
ms.assetid: '3aa74282-522b-4240-8d72-73bd3015abeb'
keywords: ["Windows Media Player online stores,plug-ins", "online stores,plug-ins", "type 1 online stores,plug-ins", "Windows Media Player online stores,IWMPContentPartner interface", "online stores,IWMPContentPartner interface", "type 1 online stores,IWMPContentPartner interface", "plug-ins,Windows Media Player online stores", "plug-ins,online stores", "plug-ins,type 1 online stores", "plug-ins,IWMPContentPartner interface", "Windows Media Player plug-ins,type 1 online stores", "Windows Media Player plug-ins,online stores", "Windows Media Player plug-ins,Windows Media Player online stores", "Windows Media Player plug-ins,IWMPContentPartner interface", "IWMPContentPartner"]
---

# Type 1 Online Store Plug-in

To take advantage of library integration features, type 1 online store providers must create a plug-in that implements the [IWMPContentPartner](iwmpcontentpartner.md) interface. This interface provides the methods that Windows Media Player calls to notify the online store about activities taking place in the Player and to retrieve specific information about online store content, the catalog, or the store itself.

After Windows Media Player instantiates the plug-in, the Player calls [IWMPContentPartner::SetCallback](iwmpcontentpartner-setcallback.md), and provides a pointer to the **IWMPContentPartnerCallback** interface. This interface gives the online store a way to make calls into Windows Media Player to provide status information or to initiate specific processes, such as downloading a music track.

Windows Media Player and the plug-in run in separate processes. The plug-in is an in-process server that runs in the default DLL surrogate, dllhost.exe.

## Related topics

<dl> <dt>

[**About Type 1 Online Stores**](about-type-1-online-stores.md)
</dt> <dt>

[**IWMPContentPartner Interface**](iwmpcontentpartner.md)
</dt> <dt>

[**IWMPContentPartnerCallback Interface**](iwmpcontentpartnercallback.md)
</dt> </dl>

 

 





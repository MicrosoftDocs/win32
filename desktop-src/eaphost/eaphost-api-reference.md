---
title: EAPHost API Reference
description: Learn about EAPHost APIs and their components. See reference information for various API topics, like the EAPHost XML Schema.
ms.assetid: ac2f074f-b525-42a2-8637-c96a08d77714
ms.topic: article
ms.date: 05/31/2018
---

# EAPHost API Reference

The EAPHost APIs are divided into three components: the supplicant APIs, which are directly callable from an EAP-enabled application; the EAP peer method APIs, which manage supplicant requests for a specific EAP authentication type and raise interactive elements on the client; and the EAP authenticator APIS, which perform the server-side authentication of a supplicant.

The latter two API components -- the EAP Peer Method and EAP Authenticator Method APIs -- require custom and conformant implementation in DLLs that expose them to the EAPHost service. They cannot be called directly from application code; instead, they are called by EAPHost (on client side for EAP peer methods, and on the server side for EAP authenticator methods) if the implementation matches the API signatures specified in the corresponding documentation. API implementation specific information is provided on each function reference page.

## EAPHost Registry Settings



| Topic                                                      | Description                                      |
|------------------------------------------------------------|--------------------------------------------------|
| [EAPHost Registry Settings](eaphost-registry-settings.md) | Describes the registry keys consumed by EAPHost. |



 

## EAPHost XML Schema



| Topic                                            | Description                                                                                       |
|--------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [EAPHost and Legacy Schema](eaphost-schemas.md) | Describes the EAPHost schema and legacy schema for creating configuration XML and credential XML. |



 

## Common EAPHost API Reference



| Topic                                                                   | Description                                  |
|-------------------------------------------------------------------------|----------------------------------------------|
| [Common EAPHost API Enumerations](common-eap-host-api-enumerations.md) | Lists constants common to all EAPHost APIs.  |
| [Common EAPHost API Structures](common-eap-host-api-structures.md)     | Lists structures common to all EAPHost APIs. |
| [Common EAPHost API Constants](common-eap-host-error-constants.md)     | Lists constants common to all EAPHost APIs.  |



 

## EAPHost API Reference



| Topic                                                                       | Description                                                                                                                                      |
|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| [EAPHost Supplicant API Reference](eap-host-supplicant-api-reference.md)   | Describes the API elements available to enable supplicant calls to EAPHost.                                                                      |
| [EAPHost Peer Method API Reference](eap-host-peer-method-api-reference.md) | Describes the API elements that must be implemented to create an EAP peer method DLL that can be loaded and called by a client EAPHost.          |
| [EAPHost Authenticator Method APIs](eaphost-authenticator-method-apis.md)  | Describes the API elements that must be implemented to create an EAP authenticator method DLL that can be loaded and called by a server EAPHost. |



 

## Related topics

<dl> <dt>

[About EAPHost](about-eap-host.md)
</dt> <dt>

[Using EAPHost](using-eap-host.md)
</dt> </dl>

 

 





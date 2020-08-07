---
title: Common EAPHost API Structures
description: Learn about common EAPHost API structures. See a list of structures used by all EAPHost technologies.
ms.assetid: f6f3b909-1e89-47f8-853c-c0f3f2414817
ms.topic: article
ms.date: 05/31/2018
---

# Common EAPHost API Structures

The following table lists structures that are common to all EAPHost API technologies.



| Structure                                                                | Description                                                                                                                                                                                                             |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EAP\_ATTRIBUTE**](/windows/desktop/api/eaptypes/ns-eaptypes-eap_attribute)                                  | Contains an EAP attribute.                                                                                                                                                                                              |
| [**EAP\_ATTRIBUTES**](/windows/desktop/api/eaptypes/ns-eaptypes-eap_attributes)                                | Contains an array of EAP attributes.                                                                                                                                                                                    |
| [**EAP\_CONFIG\_INPUT\_FIELD\_ARRAY**](/windows/desktop/api/eaptypes/ns-eaptypes-eap_config_input_field_array) | Contains a set of [**EAP\_CONFIG\_INPUT\_FIELD\_DATA**](/windows/desktop/api/eaptypes/ns-eaptypes-eap_config_input_field_data) structures that collectively contain the user input field data obtained from an EAP Single-Sign-On (SSO) configuration dialog. |
| [**EAP\_CONFIG\_INPUT\_FIELD\_DATA**](/windows/desktop/api/eaptypes/ns-eaptypes-eap_config_input_field_data)   | Contains the data associated with a single input field on a EAP Single-Sign-On (SSO) configuration dialog.                                                                                                              |
| [**EAP\_ERROR**](/windows/desktop/api/eaptypes/ns-eaptypes-eap_error)                                          | Contains data about an error that occurred during an EAPHost operation.                                                                                                                                                 |
| [**EAP\_METHOD\_INFO**](/windows/desktop/api/eaptypes/ns-eaptypes-eap_method_info)                             | Contains specific data for an EAP method.                                                                                                                                                                               |
| [**EAP\_METHOD\_INFO\_EX**](/windows/desktop/api/eaptypes/ns-eaptypes-eap_method_info_ex)                      | Windows Vista with Service Pack 1 (SP1) or later: Contains specific data for an EAP method.                                                                                                                             |
| [**EAP\_METHOD\_INFO\_ARRAY**](/windows/desktop/api/eaptypes/ns-eaptypes-eap_method_info_array)                | Contains information on EAP methods installed on the client computer.                                                                                                                                                   |
| [**EAP\_METHOD\_INFO\_ARRAY\_EX**](/windows/desktop/api/eaptypes/ns-eaptypes-eap_method_info_array_ex)         | Windows Vista with SP1 or later: Contains information about all of the EAP methods installed on the client computer.                                                                                                    |
| [**EAP\_METHOD\_TYPE**](/windows/desktop/api/eaptypes/ns-eaptypes-eap_method_type)                             | Contains type, identification, and author data for an EAP method.                                                                                                                                                       |
| [**EAP\_TYPE**](/windows/desktop/api/eaptypes/ns-eaptypes-eap_type)                                            | Contains type and vendor identification data for an EAP method.                                                                                                                                                         |
| [**EapPacket**](/windows/win32/api/eapmethodtypes/ns-eapmethodtypes-eappacket)                                           | Contains a packet of opaque data sent during an EAP authentication session.                                                                                                                                             |



 

 

 





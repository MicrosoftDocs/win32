---
title: Common EAPHost API Structures
description: The list of structures used by all EAPHost technologies.
ms.assetid: f6f3b909-1e89-47f8-853c-c0f3f2414817
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Common EAPHost API Structures

The following table lists structures that are common to all EAPHost API technologies.



| Structure                                                                | Description                                                                                                                                                                                                             |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EAP\_ATTRIBUTE**](/windows/previous-versions/eaptypes/ns-eaptypes-_eap_attribute?branch=master)                                  | Contains an EAP attribute.                                                                                                                                                                                              |
| [**EAP\_ATTRIBUTES**](/windows/previous-versions/eaptypes/ns-eaptypes-_eap_attributes?branch=master)                                | Contains an array of EAP attributes.                                                                                                                                                                                    |
| [**EAP\_CONFIG\_INPUT\_FIELD\_ARRAY**](/windows/previous-versions/eaptypes/ns-eaptypes-_eap_config_input_field_array?branch=master) | Contains a set of [**EAP\_CONFIG\_INPUT\_FIELD\_DATA**](/windows/previous-versions/eaptypes/ns-eaptypes-_eap_config_input_field_data?branch=master) structures that collectively contain the user input field data obtained from an EAP Single-Sign-On (SSO) configuration dialog. |
| [**EAP\_CONFIG\_INPUT\_FIELD\_DATA**](/windows/previous-versions/eaptypes/ns-eaptypes-_eap_config_input_field_data?branch=master)   | Contains the data associated with a single input field on a EAP Single-Sign-On (SSO) configuration dialog.                                                                                                              |
| [**EAP\_ERROR**](/windows/previous-versions/eaptypes/ns-eaptypes-_eap_error?branch=master)                                          | Contains data about an error that occurred during an EAPHost operation.                                                                                                                                                 |
| [**EAP\_METHOD\_INFO**](/windows/previous-versions/eaptypes/ns-eaptypes-_eap_method_info?branch=master)                             | Contains specific data for an EAP method.                                                                                                                                                                               |
| [**EAP\_METHOD\_INFO\_EX**](/windows/previous-versions/eaptypes/ns-eaptypes-_eap_method_info_ex?branch=master)                      | Windows Vista with Service Pack 1 (SP1) or later: Contains specific data for an EAP method.                                                                                                                             |
| [**EAP\_METHOD\_INFO\_ARRAY**](/windows/previous-versions/eaptypes/ns-eaptypes-_eap_method_info_array?branch=master)                | Contains information on EAP methods installed on the client computer.                                                                                                                                                   |
| [**EAP\_METHOD\_INFO\_ARRAY\_EX**](/windows/previous-versions/eaptypes/ns-eaptypes-_eap_method_info_array_ex?branch=master)         | Windows Vista with SP1 or later: Contains information about all of the EAP methods installed on the client computer.                                                                                                    |
| [**EAP\_METHOD\_TYPE**](/windows/previous-versions/eaptypes/ns-eaptypes-_eap_method_type?branch=master)                             | Contains type, identification, and author data for an EAP method.                                                                                                                                                       |
| [**EAP\_TYPE**](/windows/previous-versions/eaptypes/ns-eaptypes-_eap_type?branch=master)                                            | Contains type and vendor identification data for an EAP method.                                                                                                                                                         |
| [**EapPacket**](/windows/previous-versions/eapmethodtypes/ns-eapmethodtypes-tageappacket?branch=master)                                           | Contains a packet of opaque data sent during an EAP authentication session.                                                                                                                                             |



 

 

 





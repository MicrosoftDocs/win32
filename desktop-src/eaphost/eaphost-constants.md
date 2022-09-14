---
title: EAPHost Constants (Eaptypes.h)
description: View a list of EAPHost constants (Eaptypes.h) used by EAPHost methods and see requirements for their use.
ms.assetid: 56338B98-06E3-4CD3-B1CA-F8F45AA39566
topic_type:
- apiref
api_name:
- EAP_INTERACTIVE_UI_DATA_VERSION
- EAP_CREDENTIAL_VERSION
- EAPHOST_PEER_API_VERSION
- CERTIFICATE_HASH_LENGTH
- MAX_EAP_CONFIG_INPUT_FIELD_LENGTH
- MAX_EAP_CONFIG_INPUT_FIELD_VALUE_LENGTH
- EAP_UI_INPUT_FIELD_PROPS_DEFAULT
- EAP_CONFIG_INPUT_FIELD_PROPS_DEFAULT
- EAP_UI_INPUT_FIELD_PROPS_NON_DISPLAYABLE
- EAP_CONFIG_INPUT_FIELD_PROPS_NON_DISPLAYABLE
- EAP_UI_INPUT_FIELD_PROPS_NON_PERSIST
- EAP_UI_INPUT_FIELD_PROPS_READ_ONLY
api_location:
- eaptypes.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EAPHost Constants

The constants used by EAPHost methods.

<dl> <dt>

<span id="EAP_INTERACTIVE_UI_DATA_VERSION"></span><span id="eap_interactive_ui_data_version"></span>**EAP\_INTERACTIVE\_UI\_DATA\_VERSION**
</dt> <dd> <dl> <dt>

0
</dt> <dt>



The version of the EAP interactive UI data.


</dt> </dl> </dd> <dt>

<span id="EAP_CREDENTIAL_VERSION"></span><span id="eap_credential_version"></span>**EAP\_CREDENTIAL\_VERSION**
</dt> <dd> <dl> <dt>

1
</dt> <dt>



The version of the EAP credentials supplied by the user.


</dt> </dl> </dd> <dt>

<span id="EAPHOST_PEER_API_VERSION"></span><span id="eaphost_peer_api_version"></span>**EAPHOST\_PEER\_API\_VERSION**
</dt> <dd> <dl> <dt>

1
</dt> <dt>



The version of the EAPHost peer API.


</dt> </dl> </dd> <dt>

<span id="CERTIFICATE_HASH_LENGTH"></span><span id="certificate_hash_length"></span>**CERTIFICATE\_HASH\_LENGTH**
</dt> <dd> <dl> <dt>

20
</dt> <dt>



Length of the SHA1 hash of the certificate.


</dt> </dl> </dd> <dt>

<span id="MAX_EAP_CONFIG_INPUT_FIELD_LENGTH"></span><span id="max_eap_config_input_field_length"></span>**MAX\_EAP\_CONFIG\_INPUT\_FIELD\_LENGTH**
</dt> <dd> <dl> <dt>

256
</dt> <dt>



Specifies the maximum supported length of an input field.


</dt> </dl> </dd> <dt>

<span id="MAX_EAP_CONFIG_INPUT_FIELD_VALUE_LENGTH"></span><span id="max_eap_config_input_field_value_length"></span>**MAX\_EAP\_CONFIG\_INPUT\_FIELD\_VALUE\_LENGTH**
</dt> <dd> <dl> <dt>

1024
</dt> <dt>



Specifies the maximum supported length of an input field.


</dt> </dl> </dd> <dt>

<span id="EAP_UI_INPUT_FIELD_PROPS_DEFAULT"></span><span id="eap_ui_input_field_props_default"></span>**EAP\_UI\_INPUT\_FIELD\_PROPS\_DEFAULT**
</dt> <dd> <dl> <dt>

0X00000000 
</dt> <dt>



Windows Vista with SP1 or later: Represents the default property value for input field entries displayed in the UI.


</dt> </dl> </dd> <dt>

<span id="EAP_CONFIG_INPUT_FIELD_PROPS_DEFAULT"></span><span id="eap_config_input_field_props_default"></span>**EAP\_CONFIG\_INPUT\_FIELD\_PROPS\_DEFAULT**
</dt> <dd> <dl> <dt>

0X00000000 
</dt> <dt>



Represents the default property value for configuration input field entries displayed in the UI.


</dt> </dl> </dd> <dt>

<span id="EAP_UI_INPUT_FIELD_PROPS_NON_DISPLAYABLE"></span><span id="eap_ui_input_field_props_non_displayable"></span>**EAP\_UI\_INPUT\_FIELD\_PROPS\_NON\_DISPLAYABLE**
</dt> <dd> <dl> <dt>

0X00000001 
</dt> <dt>



Windows Vista with SP1 or later: Specifies that input field entries will not be displayed in the UI (a password or PIN number, for example).


</dt> </dl> </dd> <dt>

<span id="EAP_CONFIG_INPUT_FIELD_PROPS_NON_DISPLAYABLE"></span><span id="eap_config_input_field_props_non_displayable"></span>**EAP\_CONFIG\_INPUT\_FIELD\_PROPS\_NON\_DISPLAYABLE**
</dt> <dd> <dl> <dt>

0X00000001 
</dt> <dt>



Specifies that configuration input field entries will not be displayed in the UI (a password or PIN number, for example).


</dt> </dl> </dd> <dt>

<span id="EAP_UI_INPUT_FIELD_PROPS_NON_PERSIST"></span><span id="eap_ui_input_field_props_non_persist"></span>**EAP\_UI\_INPUT\_FIELD\_PROPS\_NON\_PERSIST**
</dt> <dd> <dl> <dt>

0X00000002 
</dt> <dt>



Windows Vista with SP1 or later: Indicates that the EAP method will not cache the field data; the supplicant must cache the field data for roaming.


</dt> </dl> </dd> <dt>

<span id="EAP_UI_INPUT_FIELD_PROPS_READ_ONLY"></span><span id="eap_ui_input_field_props_read_only"></span>**EAP\_UI\_INPUT\_FIELD\_PROPS\_READ\_ONLY**
</dt> <dd> <dl> <dt>

0x00000004
</dt> <dt>



Windows Vista with SP1 or later: Indicates that the input field is read-only and cannot be edited.


</dt> </dl> </dd> </dl>

## Requirements



| Role | Minimum supported OS version |
|------|------------------------------|
| Client<br/> | Windows 8 \[desktop apps only\]<br/> |
| Server<br/> | Windows Server 2012 \[desktop apps only\]<br/> |



 

 






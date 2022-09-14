---
title: Identity constants (AppModel.h)
description: Specifies the length of the strings for the package's identity fields.
ms.assetid: C4F81822-B502-4360-AEA4-829F1AB926BF
topic_type:
- apiref
api_name:
- APPLICATION_USER_MODEL_ID_MAX_LENGTH
- APPLICATION_USER_MODEL_ID_MIN_LENGTH
- PACKAGE_ARCHITECTURE_MAX_LENGTH
- PACKAGE_ARCHITECTURE_MIN_LENGTH
- PACKAGE_FAMILY_NAME_MAX_LENGTH
- PACKAGE_FAMILY_NAME_MIN_LENGTH
- PACKAGE_FULL_NAME_MAX_LENGTH
- PACKAGE_FULL_NAME_MIN_LENGTH
- PACKAGE_NAME_MAX_LENGTH
- PACKAGE_NAME_MIN_LENGTH
- PACKAGE_PUBLISHERID_MAX_LENGTH
- PACKAGE_PUBLISHERID_MIN_LENGTH
- PACKAGE_PUBLISHER_MAX_LENGTH
- PACKAGE_PUBLISHER_MIN_LENGTH
- PACKAGE_RELATIVE_APPLICATION_ID_MAX_LENGTH
- PACKAGE_RELATIVE_APPLICATION_ID_MIN_LENGTH
- PACKAGE_RESOURCEID_MAX_LENGTH
- PACKAGE_RESOURCEID_MIN_LENGTH
- PACKAGE_VERSION_MAX_LENGTH
- PACKAGE_VERSION_MIN_LENGTH
api_location:
- AppModel.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Identity constants

Specifies the length of the strings for the package's identity fields. The length is measured in characters and may or may not include space for the NULL terminator.

> [!Note]  
> Constants in the form: **APPLICATION\_USER\_MODEL\_ID\_\*\_LENGTH** and **PACKAGE\_RELATIVE\_APPLICATION\_ID\_\*\_LENGTH** include space for a NULL terminator, but constants in the form: **PACKAGE\_\*\_LENGTH** do not include space for a NULL terminator.

 



| Constant/value                                                                                                                                                                                                                                                                                                   | Description                                                                                                                            |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------|
| <span id="APPLICATION_USER_MODEL_ID_MAX_LENGTH"></span><span id="application_user_model_id_max_length"></span><dl> <dt>**APPLICATION\_USER\_MODEL\_ID\_MAX\_LENGTH**</dt> <dt>130</dt> </dl>                  | The maximum length of the application user model ID. Space is included for the NULL terminator.<br/>                             |
| <span id="APPLICATION_USER_MODEL_ID_MIN_LENGTH"></span><span id="application_user_model_id_min_length"></span><dl> <dt>**APPLICATION\_USER\_MODEL\_ID\_MIN\_LENGTH**</dt> <dt>21</dt> </dl>                   | The minimum length of the application user model ID. Space is included for the NULL terminator.<br/>                             |
| <span id="PACKAGE_ARCHITECTURE_MAX_LENGTH"></span><span id="package_architecture_max_length"></span><dl> <dt>**PACKAGE\_ARCHITECTURE\_MAX\_LENGTH**</dt> <dt>7</dt> </dl>                                     | The maximum length of the architecture. No space included for the NULL terminator.<br/>                                          |
| <span id="PACKAGE_ARCHITECTURE_MIN_LENGTH"></span><span id="package_architecture_min_length"></span><dl> <dt>**PACKAGE\_ARCHITECTURE\_MIN\_LENGTH**</dt> <dt>3</dt> </dl>                                     | The minimum length of the architecture. No space included for the NULL terminator.<br/>                                          |
| <span id="PACKAGE_FAMILY_NAME_MAX_LENGTH"></span><span id="package_family_name_max_length"></span><dl> <dt>**PACKAGE\_FAMILY\_NAME\_MAX\_LENGTH**</dt> <dt>64</dt> </dl>                                      | The maximum length of the family name. No space included for the NULL terminator.<br/>                                           |
| <span id="PACKAGE_FAMILY_NAME_MIN_LENGTH"></span><span id="package_family_name_min_length"></span><dl> <dt>**PACKAGE\_FAMILY\_NAME\_MIN\_LENGTH**</dt> <dt>17</dt> </dl>                                      | The minimum length of the family name. No space included for the NULL terminator.<br/>                                           |
| <span id="PACKAGE_FULL_NAME_MAX_LENGTH"></span><span id="package_full_name_max_length"></span><dl> <dt>**PACKAGE\_FULL\_NAME\_MAX\_LENGTH**</dt> <dt>127</dt> </dl>                                           | The maximum length of the full name. No space included for the NULL terminator.<br/>                                             |
| <span id="PACKAGE_FULL_NAME_MIN_LENGTH"></span><span id="package_full_name_min_length"></span><dl> <dt>**PACKAGE\_FULL\_NAME\_MIN\_LENGTH**</dt> <dt>30</dt> </dl>                                            | The minimum length of the full name. No space included for the NULL terminator.<br/>                                             |
| <span id="PACKAGE_NAME_MAX_LENGTH"></span><span id="package_name_max_length"></span><dl> <dt>**PACKAGE\_NAME\_MAX\_LENGTH**</dt> <dt>50</dt> </dl>                                                            | The maximum length of the name. No space included for the NULL terminator.<br/>                                                  |
| <span id="PACKAGE_NAME_MIN_LENGTH"></span><span id="package_name_min_length"></span><dl> <dt>**PACKAGE\_NAME\_MIN\_LENGTH**</dt> <dt>3</dt> </dl>                                                             | The minimum length of the name. No space included for the NULL terminator.<br/>                                                  |
| <span id="PACKAGE_PUBLISHERID_MAX_LENGTH"></span><span id="package_publisherid_max_length"></span><dl> <dt>**PACKAGE\_PUBLISHERID\_MAX\_LENGTH**</dt> <dt>13</dt> </dl>                                       | The maximum length of the publisher ID. No space included for the NULL terminator.<br/>                                          |
| <span id="PACKAGE_PUBLISHERID_MIN_LENGTH"></span><span id="package_publisherid_min_length"></span><dl> <dt>**PACKAGE\_PUBLISHERID\_MIN\_LENGTH**</dt> <dt>13</dt> </dl>                                       | The minimum length of the publisher ID. No space included for the NULL terminator.<br/>                                          |
| <span id="PACKAGE_PUBLISHER_MAX_LENGTH"></span><span id="package_publisher_max_length"></span><dl> <dt>**PACKAGE\_PUBLISHER\_MAX\_LENGTH**</dt> <dt>8192</dt> </dl>                                           | The maximum length of the publisher. For example, CN=*publisher*. No space included for the NULL terminator.<br/>                |
| <span id="PACKAGE_PUBLISHER_MIN_LENGTH"></span><span id="package_publisher_min_length"></span><dl> <dt>**PACKAGE\_PUBLISHER\_MIN\_LENGTH**</dt> <dt>4</dt> </dl>                                              | The minimum length of the publisher. No space included for the NULL terminator.<br/>                                             |
| <span id="PACKAGE_RELATIVE_APPLICATION_ID_MAX_LENGTH"></span><span id="package_relative_application_id_max_length"></span><dl> <dt>**PACKAGE\_RELATIVE\_APPLICATION\_ID\_MAX\_LENGTH**</dt> <dt>65</dt> </dl> | The maximum length of the package relative application ID. Space is included for the NULL terminator.<br/>                       |
| <span id="PACKAGE_RELATIVE_APPLICATION_ID_MIN_LENGTH"></span><span id="package_relative_application_id_min_length"></span><dl> <dt>**PACKAGE\_RELATIVE\_APPLICATION\_ID\_MIN\_LENGTH**</dt> <dt>2</dt> </dl>  | The minimum length of the package relative application ID. Space is included for the NULL terminator.<br/>                       |
| <span id="PACKAGE_RESOURCEID_MAX_LENGTH"></span><span id="package_resourceid_max_length"></span><dl> <dt>**PACKAGE\_RESOURCEID\_MAX\_LENGTH**</dt> <dt>30</dt> </dl>                                          | The maximum length of the resource ID. No space included for the NULL terminator.<br/>                                           |
| <span id="PACKAGE_RESOURCEID_MIN_LENGTH"></span><span id="package_resourceid_min_length"></span><dl> <dt>**PACKAGE\_RESOURCEID\_MIN\_LENGTH**</dt> <dt>0</dt> </dl>                                           | The minimum length of the resource ID. No space included for the NULL terminator.<br/>                                           |
| <span id="PACKAGE_VERSION_MAX_LENGTH"></span><span id="package_version_max_length"></span><dl> <dt>**PACKAGE\_VERSION\_MAX\_LENGTH**</dt> <dt>23</dt> </dl>                                                   | The maximum length of the version. For example, *xxxxx*.*xxxxx*.*xxxxx*.*xxxxx*. No space included for the NULL terminator/<br/> |
| <span id="PACKAGE_VERSION_MIN_LENGTH"></span><span id="package_version_min_length"></span><dl> <dt>**PACKAGE\_VERSION\_MIN\_LENGTH**</dt> <dt>7</dt> </dl>                                                    | The minimum length of the version. For example, *x*.*x*.*x*.*x*. No space included for the NULL terminator.<br/>                 |



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>AppModel.h</dt> </dl> |



 

 






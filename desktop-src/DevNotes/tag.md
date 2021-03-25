---
description: Identifies an entry in the shim database.
ms.assetid: 'c092592d-a4f4-4b2f-9b03-c07951ed214a'
title: TAG (Exposeenums2managed.h)
ms.topic: article
ms.date: 05/31/2018
---

# TAG

Identifies an entry in the shim database.

The following entries are of type **TAG\_TYPE\_LIST** (0x7000).



| Constant/value                                                                                                                                                                                                                                                             | Description                                                               |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------|
| <span id="TAG_DATABASE"></span><span id="tag_database"></span><dl> <dt>**TAG\_DATABASE**</dt> <dt>(0x1 \| **TAG\_TYPE\_LIST**)</dt> </dl>                               | Database entry.<br/>                                                |
| <span id="TAG_LIBRARY"></span><span id="tag_library"></span><dl> <dt>**TAG\_LIBRARY**</dt> <dt>(0x2 \| **TAG\_TYPE\_LIST**)</dt> </dl>                                  | Library entry.<br/>                                                 |
| <span id="TAG_INEXCLUDE"></span><span id="tag_inexclude"></span><dl> <dt>**TAG\_INEXCLUDE**</dt> <dt>(0x3 \| **TAG\_TYPE\_LIST**)</dt> </dl>                            | Include and exclude entry.<br/>                                     |
| <span id="TAG_SHIM"></span><span id="tag_shim"></span><dl> <dt>**TAG\_SHIM**</dt> <dt>(0x4 \| **TAG\_TYPE\_LIST**)</dt> </dl>                                           | Shim entry that contains the name and purpose information.<br/>     |
| <span id="TAG_PATCH"></span><span id="tag_patch"></span><dl> <dt>**TAG\_PATCH**</dt> <dt>(0x5 \| **TAG\_TYPE\_LIST**)</dt> </dl>                                        | Patch entry that contains the in-memory patching information.<br/>  |
| <span id="TAG_APP"></span><span id="tag_app"></span><dl> <dt>**TAG\_APP**</dt> <dt>(0x6 \| **TAG\_TYPE\_LIST**)</dt> </dl>                                              | Application entry.<br/>                                             |
| <span id="TAG_EXE"></span><span id="tag_exe"></span><dl> <dt>**TAG\_EXE**</dt> <dt>(0x7 \| **TAG\_TYPE\_LIST**)</dt> </dl>                                              | Executable entry.<br/>                                              |
| <span id="TAG_MATCHING_FILE"></span><span id="tag_matching_file"></span><dl> <dt>**TAG\_MATCHING\_FILE**</dt> <dt>(0x8 \| **TAG\_TYPE\_LIST**)</dt> </dl>               | Matching file entry.<br/>                                           |
| <span id="TAG_SHIM_REF"></span><span id="tag_shim_ref"></span><dl> <dt>**TAG\_SHIM\_REF**</dt> <dt>(0x9\| TAG\_TYPE\_LIST)</dt> </dl>                                   | Shim definition entry.<br/>                                         |
| <span id="TAG_PATCH_REF"></span><span id="tag_patch_ref"></span><dl> <dt>**TAG\_PATCH\_REF**</dt> <dt>(0xA \| **TAG\_TYPE\_LIST**)</dt> </dl>                           | Patch definition entry.<br/>                                        |
| <span id="TAG_LAYER"></span><span id="tag_layer"></span><dl> <dt>**TAG\_LAYER**</dt> <dt>(0xB \| **TAG\_TYPE\_LIST**)</dt> </dl>                                        | Layer shim entry.<br/>                                              |
| <span id="TAG_FILE"></span><span id="tag_file"></span><dl> <dt>**TAG\_FILE**</dt> <dt>(0xC \| **TAG\_TYPE\_LIST**)</dt> </dl>                                           | File attribute used in a shim entry.<br/>                           |
| <span id="TAG_APPHELP"></span><span id="tag_apphelp"></span><dl> <dt>**TAG\_APPHELP**</dt> <dt>(0xD \| **TAG\_TYPE\_LIST**)</dt> </dl>                                  | Apphelp information entry.<br/>                                     |
| <span id="TAG_LINK"></span><span id="tag_link"></span><dl> <dt>**TAG\_LINK**</dt> <dt>(0xE \| **TAG\_TYPE\_LIST**)</dt> </dl>                                           | Apphelp online link information entry.<br/>                         |
| <span id="TAG_DATA"></span><span id="tag_data"></span><dl> <dt>**TAG\_DATA**</dt> <dt>(0xF \| **TAG\_TYPE\_LIST**)</dt> </dl>                                           | Name-value mapping entry.<br/>                                      |
| <span id="TAG_MSI_TRANSFORM"></span><span id="tag_msi_transform"></span><dl> <dt>**TAG\_MSI\_TRANSFORM**</dt> <dt>(0x10 \| **TAG\_TYPE\_LIST**)</dt> </dl>              | MSI transformation entry.<br/>                                      |
| <span id="TAG_MSI_TRANSFORM_REF"></span><span id="tag_msi_transform_ref"></span><dl> <dt>**TAG\_MSI\_TRANSFORM\_REF**</dt> <dt>(0x11 \| **TAG\_TYPE\_LIST**)</dt> </dl> | MSI transformation definition entry.<br/>                           |
| <span id="TAG_MSI_PACKAGE"></span><span id="tag_msi_package"></span><dl> <dt>**TAG\_MSI\_PACKAGE**</dt> <dt>(0x12 \| **TAG\_TYPE\_LIST**)</dt> </dl>                    | MSI package entry.<br/>                                             |
| <span id="TAG_FLAG"></span><span id="tag_flag"></span><dl> <dt>**TAG\_FLAG**</dt> <dt>(0x13 \| **TAG\_TYPE\_LIST**)</dt> </dl>                                          | Flag entry.<br/>                                                    |
| <span id="TAG_MSI_CUSTOM_ACTION"></span><span id="tag_msi_custom_action"></span><dl> <dt>**TAG\_MSI\_CUSTOM\_ACTION**</dt> <dt>(0x14 \| **TAG\_TYPE\_LIST**)</dt> </dl> | MSI custom action entry.<br/>                                       |
| <span id="TAG_FLAG_REF"></span><span id="tag_flag_ref"></span><dl> <dt>**TAG\_FLAG\_REF**</dt> <dt>(0x15 \| **TAG\_TYPE\_LIST**)</dt> </dl>                             | Flag definition entry.<br/>                                         |
| <span id="TAG_ACTION"></span><span id="tag_action"></span><dl> <dt>**TAG\_ACTION**</dt> <dt>(0x16 \| **TAG\_TYPE\_LIST**)</dt> </dl>                                    | Unused.<br/>                                                        |
| <span id="TAG_LOOKUP"></span><span id="tag_lookup"></span><dl> <dt>**TAG\_LOOKUP**</dt> <dt>(0x17 \| **TAG\_TYPE\_LIST**)</dt> </dl>                                    | Lookup entry used for lookup in a driver database.<br/>             |
| <span id="TAG_STRINGTABLE"></span><span id="tag_stringtable"></span><dl> <dt>**TAG\_STRINGTABLE**</dt> <dt>(0x801 \| **TAG\_TYPE\_LIST**)</dt> </dl>                    | String table entry.<br/>                                            |
| <span id="TAG_INDEXES"></span><span id="tag_indexes"></span><dl> <dt>**TAG\_INDEXES**</dt> <dt>(0x802 \| **TAG\_TYPE\_LIST**)</dt> </dl>                                | Indexes entry that defines all the indexes in a shim database.<br/> |
| <span id="TAG_INDEX"></span><span id="tag_index"></span><dl> <dt>**TAG\_INDEX**</dt> <dt>(0x803 \| **TAG\_TYPE\_LIST**)</dt> </dl>                                      | Index entry that defines an index in a shim database.<br/>          |



The following entries are of type **TAG\_TYPE\_STRINGREF** (0x6000).



| Constant/value                                                                                                                                                                                                                                                                     | Description                                                                                   |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|
| <span id="TAG_NAME"></span><span id="tag_name"></span><dl> <dt>**TAG\_NAME**</dt> <dt>(0x1 \| **TAG\_TYPE\_STRINGREF**)</dt> </dl>                                              | Name attribute.<br/>                                                                    |
| <span id="TAG_DESCRIPTION"></span><span id="tag_description"></span><dl> <dt>**TAG\_DESCRIPTION**</dt> <dt>(0x2 \| **TAG\_TYPE\_STRINGREF**)</dt> </dl>                         | Description entry.<br/>                                                                 |
| <span id="TAG_MODULE"></span><span id="tag_module"></span><dl> <dt>**TAG\_MODULE**</dt> <dt>(0x3 \| **TAG\_TYPE\_STRINGREF**)</dt> </dl>                                        | Module attribute.<br/>                                                                  |
| <span id="TAG_API"></span><span id="tag_api"></span><dl> <dt>**TAG\_API**</dt> <dt>(0x4 \| **TAG\_TYPE\_STRINGREF**)</dt> </dl>                                                 | API entry.<br/>                                                                         |
| <span id="TAG_VENDOR"></span><span id="tag_vendor"></span><dl> <dt>**TAG\_VENDOR**</dt> <dt>(0x5 \| **TAG\_TYPE\_STRINGREF**)</dt> </dl>                                        | Vendor name attribute.<br/>                                                             |
| <span id="TAG_APP_NAME"></span><span id="tag_app_name"></span><dl> <dt>**TAG\_APP\_NAME**</dt> <dt>(0x6 \| **TAG\_TYPE\_STRINGREF**)</dt> </dl>                                 | Application name attribute that describes an application entry in a shim database.<br/> |
| <span id="TAG_COMMAND_LINE"></span><span id="tag_command_line"></span><dl> <dt>**TAG\_COMMAND\_LINE**</dt> <dt>(0x8 \| **TAG\_TYPE\_STRINGREF**)</dt> </dl>                     | Command line attribute that is used when passing arguments to a shim, for example.<br/> |
| <span id="TAG_COMPANY_NAME"></span><span id="tag_company_name"></span><dl> <dt>**TAG\_COMPANY\_NAME**</dt> <dt>(0x9 \| **TAG\_TYPE\_STRINGREF**)</dt> </dl>                     | Company name attribute.<br/>                                                            |
| <span id="TAG_DLLFILE"></span><span id="tag_dllfile"></span><dl> <dt>**TAG\_DLLFILE**</dt> <dt>(0xA \| **TAG\_TYPE\_STRINGREF**)</dt> </dl>                                     | DLL file attribute for a shim entry.<br/>                                               |
| <span id="TAG_WILDCARD_NAME"></span><span id="tag_wildcard_name"></span><dl> <dt>**TAG\_WILDCARD\_NAME**</dt> <dt>(0xB \| **TAG\_TYPE\_STRINGREF**)</dt> </dl>                  | Wildcard name attribute for an executable entry with a wildcard as the file name.<br/>  |
| <span id="TAG_PRODUCT_NAME"></span><span id="tag_product_name"></span><dl> <dt>**TAG\_PRODUCT\_NAME**</dt> <dt>(0x10 \| **TAG\_TYPE\_STRINGREF**)</dt> </dl>                    | Product name attribute.<br/>                                                            |
| <span id="TAG_PRODUCT_VERSION"></span><span id="tag_product_version"></span><dl> <dt>**TAG\_PRODUCT\_VERSION**</dt> <dt>(0x11 \| **TAG\_TYPE\_STRINGREF**)</dt> </dl>           | Product version attribute.<br/>                                                         |
| <span id="TAG_FILE_DESCRIPTION"></span><span id="tag_file_description"></span><dl> <dt>**TAG\_FILE\_DESCRIPTION**</dt> <dt>(0x12 \| **TAG\_TYPE\_STRINGREF**)</dt> </dl>        | File description attribute.<br/>                                                        |
| <span id="TAG_FILE_VERSION"></span><span id="tag_file_version"></span><dl> <dt>**TAG\_FILE\_VERSION**</dt> <dt>(0x13 \| **TAG\_TYPE\_STRINGREF**)</dt> </dl>                    | File version attribute.<br/>                                                            |
| <span id="TAG_ORIGINAL_FILENAME"></span><span id="tag_original_filename"></span><dl> <dt>**TAG\_ORIGINAL\_FILENAME**</dt> <dt>(0x14 \| **TAG\_TYPE\_STRINGREF**)</dt> </dl>     | Original file name attribute.<br/>                                                      |
| <span id="TAG_INTERNAL_NAME"></span><span id="tag_internal_name"></span><dl> <dt>**TAG\_INTERNAL\_NAME**</dt> <dt>(0x15 \| **TAG\_TYPE\_STRINGREF**)</dt> </dl>                 | Internal file name attribute.<br/>                                                      |
| <span id="TAG_LEGAL_COPYRIGHT"></span><span id="tag_legal_copyright"></span><dl> <dt>**TAG\_LEGAL\_COPYRIGHT**</dt> <dt>(0x16 \| **TAG\_TYPE\_STRINGREF**)</dt> </dl>           | Copyright attribute.<br/>                                                               |
| <span id="TAG_16BIT_DESCRIPTION"></span><span id="tag_16bit_description"></span><dl> <dt>**TAG\_16BIT\_DESCRIPTION**</dt> <dt>(0x17 \| **TAG\_TYPE\_STRINGREF**)</dt> </dl>     | 16-bit description attribute.<br/>                                                      |
| <span id="TAG_APPHELP_DETAILS"></span><span id="tag_apphelp_details"></span><dl> <dt>**TAG\_APPHELP\_DETAILS**</dt> <dt>(0x18 \| **TAG\_TYPE\_STRINGREF**)</dt> </dl>           | Apphelp details message information attribute.<br/>                                     |
| <span id="TAG_LINK_URL"></span><span id="tag_link_url"></span><dl> <dt>**TAG\_LINK\_URL**</dt> <dt>(0x19 \| **TAG\_TYPE\_STRINGREF**)</dt> </dl>                                | Apphelp online link URL attribute.<br/>                                                 |
| <span id="TAG_LINK_TEXT"></span><span id="tag_link_text"></span><dl> <dt>**TAG\_LINK\_TEXT**</dt> <dt>(0x1A \| **TAG\_TYPE\_STRINGREF**)</dt> </dl>                             | Apphelp online link text attribute.<br/>                                                |
| <span id="TAG_APPHELP_TITLE"></span><span id="tag_apphelp_title"></span><dl> <dt>**TAG\_APPHELP\_TITLE**</dt> <dt>(0x1B \| **TAG\_TYPE\_STRINGREF**)</dt> </dl>                 | Apphelp title attribute.<br/>                                                           |
| <span id="TAG_APPHELP_CONTACT"></span><span id="tag_apphelp_contact"></span><dl> <dt>**TAG\_APPHELP\_CONTACT**</dt> <dt>(0x1C \| **TAG\_TYPE\_STRINGREF**)</dt> </dl>           | Apphelp vendor contact attribute.<br/>                                                  |
| <span id="TAG_SXS_MANIFEST"></span><span id="tag_sxs_manifest"></span><dl> <dt>**TAG\_SXS\_MANIFEST**</dt> <dt>(0x1D \| **TAG\_TYPE\_STRINGREF**)</dt> </dl>                    | Side-by-side manifest entry.<br/>                                                       |
| <span id="TAG_DATA_STRING"></span><span id="tag_data_string"></span><dl> <dt>**TAG\_DATA\_STRING**</dt> <dt>(0x1E \| **TAG\_TYPE\_STRINGREF**)</dt> </dl>                       | String attribute for a data entry.<br/>                                                 |
| <span id="TAG_MSI_TRANSFORM_FILE"></span><span id="tag_msi_transform_file"></span><dl> <dt>**TAG\_MSI\_TRANSFORM\_FILE**</dt> <dt>(0x1F \| **TAG\_TYPE\_STRINGREF**)</dt> </dl> | File name attribute of an MSI transformation entry.<br/>                                |
| <span id="TAG_16BIT_MODULE_NAME"></span><span id="tag_16bit_module_name"></span><dl> <dt>**TAG\_16BIT\_MODULE\_NAME**</dt> <dt>(0x20 \| **TAG\_TYPE\_STRINGREF**)</dt> </dl>    | 16-bit module name attribute.<br/>                                                      |
| <span id="TAG_LAYER_DISPLAYNAME"></span><span id="tag_layer_displayname"></span><dl> <dt>**TAG\_LAYER\_DISPLAYNAME**</dt> <dt>(0x21 \| **TAG\_TYPE\_STRINGREF**)</dt> </dl>     | Unused.<br/>                                                                            |
| <span id="TAG_COMPILER_VERSION"></span><span id="tag_compiler_version"></span><dl> <dt>**TAG\_COMPILER\_VERSION**</dt> <dt>(0x22 \| **TAG\_TYPE\_STRINGREF**)</dt> </dl>        | Shim database compiler version.<br/>                                                    |
| <span id="TAG_ACTION_TYPE"></span><span id="tag_action_type"></span><dl> <dt>**TAG\_ACTION\_TYPE**</dt> <dt>(0x23 \| **TAG\_TYPE\_STRINGREF**)</dt> </dl>                       | Unused.<br/>                                                                            |
| <span id="TAG_EXPORT_NAME"></span><span id="tag_export_name"></span><dl> <dt>**TAG\_EXPORT\_NAME**</dt> <dt>(0x24 \| **TAG\_TYPE\_STRINGREF**)</dt> </dl>                       | Export file name attribute.<br/>                                                        |



The following entries are of type **TAG\_TYPE\_DWORD** (0x4000).



| Constant/value                                                                                                                                                                                                                                                                    | Description                                                                                                      |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------|
| <span id="TAG_SIZE"></span><span id="tag_size"></span><dl> <dt>**TAG\_SIZE**</dt> <dt>(0x1 \| **TAG\_TYPE\_DWORD**)</dt> </dl>                                                 | File size attribute.<br/>                                                                                  |
| <span id="TAG_OFFSET"></span><span id="tag_offset"></span><dl> <dt>**TAG\_OFFSET**</dt> <dt>(0x2 \| **TAG\_TYPE\_DWORD**)</dt> </dl>                                           | Unused.<br/>                                                                                               |
| <span id="TAG_CHECKSUM"></span><span id="tag_checksum"></span><dl> <dt>**TAG\_CHECKSUM**</dt> <dt>(0x3 \| **TAG\_TYPE\_DWORD**)</dt> </dl>                                     | File checksum attribute.<br/>                                                                              |
| <span id="TAG_SHIM_TAGID"></span><span id="tag_shim_tagid"></span><dl> <dt>**TAG\_SHIM\_TAGID**</dt> <dt>(0x4 \| **TAG\_TYPE\_DWORD**)</dt> </dl>                              | Shim **TAGID** attribute.<br/>                                                                             |
| <span id="TAG_PATCH_TAGID"></span><span id="tag_patch_tagid"></span><dl> <dt>**TAG\_PATCH\_TAGID**</dt> <dt>(0x5 \| **TAG\_TYPE\_DWORD**)</dt> </dl>                           | Patch **TAGID** attribute.<br/>                                                                            |
| <span id="TAG_MODULE_TYPE"></span><span id="tag_module_type"></span><dl> <dt>**TAG\_MODULE\_TYPE**</dt> <dt>(0x6 \| **TAG\_TYPE\_DWORD**)</dt> </dl>                           | Module type attribute.<br/>                                                                                |
| <span id="TAG_VERDATEHI"></span><span id="tag_verdatehi"></span><dl> <dt>**TAG\_VERDATEHI**</dt> <dt>(0x7 \| **TAG\_TYPE\_DWORD**)</dt> </dl>                                  | High-order portion of the file version date attribute.<br/>                                                |
| <span id="TAG_VERDATELO"></span><span id="tag_verdatelo"></span><dl> <dt>**TAG\_VERDATELO**</dt> <dt>(0x8 \| **TAG\_TYPE\_DWORD**)</dt> </dl>                                  | Low-order portion of the file version date attribute.<br/>                                                 |
| <span id="TAG_VERFILEOS"></span><span id="tag_verfileos"></span><dl> <dt>**TAG\_VERFILEOS**</dt> <dt>(0x9 \| **TAG\_TYPE\_DWORD**)</dt> </dl>                                  | Operating system file version attribute.<br/>                                                              |
| <span id="TAG_VERFILETYPE"></span><span id="tag_verfiletype"></span><dl> <dt>**TAG\_VERFILETYPE**</dt> <dt>(0xA \| **TAG\_TYPE\_DWORD**)</dt> </dl>                            | File type attribute.<br/>                                                                                  |
| <span id="TAG_PE_CHECKSUM"></span><span id="tag_pe_checksum"></span><dl> <dt>**TAG\_PE\_CHECKSUM**</dt> <dt>(0xB \| **TAG\_TYPE\_DWORD**)</dt> </dl>                           | PE file checksum attribute.<br/>                                                                           |
| <span id="TAG_PREVOSMAJORVER"></span><span id="tag_prevosmajorver"></span><dl> <dt>**TAG\_PREVOSMAJORVER**</dt> <dt>(0xC \| **TAG\_TYPE\_DWORD**)</dt> </dl>                   | Major operating system version attribute.<br/>                                                             |
| <span id="TAG_PREVOSMINORVER"></span><span id="tag_prevosminorver"></span><dl> <dt>**TAG\_PREVOSMINORVER**</dt> <dt>(0xD \| **TAG\_TYPE\_DWORD**)</dt> </dl>                   | Minor operating system version attribute.<br/>                                                             |
| <span id="TAG_PREVOSPLATFORMID"></span><span id="tag_prevosplatformid"></span><dl> <dt>**TAG\_PREVOSPLATFORMID**</dt> <dt>(0xE \| **TAG\_TYPE\_DWORD**)</dt> </dl>             | Operating system platform identifier attribute.<br/>                                                       |
| <span id="TAG_PREVOSBUILDNO"></span><span id="tag_prevosbuildno"></span><dl> <dt>**TAG\_PREVOSBUILDNO**</dt> <dt>(0xF \| **TAG\_TYPE\_DWORD**)</dt> </dl>                      | Operating system build number attribute.<br/>                                                              |
| <span id="TAG_PROBLEMSEVERITY"></span><span id="tag_problemseverity"></span><dl> <dt>**TAG\_PROBLEMSEVERITY**</dt> <dt>(0x10 \| **TAG\_TYPE\_DWORD**)</dt> </dl>               | Block attribute of an Apphelp entry. This determines whether the application is hard or soft blocked.<br/> |
| <span id="TAG_LANGID"></span><span id="tag_langid"></span><dl> <dt>**TAG\_LANGID**</dt> <dt>(0x11 \| **TAG\_TYPE\_DWORD**)</dt> </dl>                                          | Language identifier of an Apphelp entry.<br/>                                                              |
| <span id="TAG_VER_LANGUAGE"></span><span id="tag_ver_language"></span><dl> <dt>**TAG\_VER\_LANGUAGE**</dt> <dt>(0x12 \| **TAG\_TYPE\_DWORD**)</dt> </dl>                       | Language version attribute of a file.<br/>                                                                 |
| <span id="TAG_ENGINE"></span><span id="tag_engine"></span><dl> <dt>**TAG\_ENGINE**</dt> <dt>(0x14 \| **TAG\_TYPE\_DWORD**)</dt> </dl>                                          | Unused.<br/>                                                                                               |
| <span id="TAG_HTMLHELPID"></span><span id="tag_htmlhelpid"></span><dl> <dt>**TAG\_HTMLHELPID**</dt> <dt>(0x15 \| **TAG\_TYPE\_DWORD**)</dt> </dl>                              | Help identifier attribute for an Apphelp entry.<br/>                                                       |
| <span id="TAG_INDEX_FLAGS"></span><span id="tag_index_flags"></span><dl> <dt>**TAG\_INDEX\_FLAGS**</dt> <dt>(0x16 \| **TAG\_TYPE\_DWORD**)</dt> </dl>                          | Flags attribute for an index entry.<br/>                                                                   |
| <span id="TAG_FLAGS"></span><span id="tag_flags"></span><dl> <dt>**TAG\_FLAGS**</dt> <dt>(0x17 \| **TAG\_TYPE\_DWORD**)</dt> </dl>                                             | Flags attribute for an Apphelp entry.<br/>                                                                 |
| <span id="TAG_DATA_VALUETYPE"></span><span id="tag_data_valuetype"></span><dl> <dt>**TAG\_DATA\_VALUETYPE**</dt> <dt>(0x18 \| **TAG\_TYPE\_DWORD**)</dt> </dl>                 | Data type attribute for a data entry.<br/>                                                                 |
| <span id="TAG_DATA_DWORD"></span><span id="tag_data_dword"></span><dl> <dt>**TAG\_DATA\_DWORD**</dt> <dt>(0x19 \| **TAG\_TYPE\_DWORD**)</dt> </dl>                             | **DWORD** value attribute for a data entry.<br/>                                                           |
| <span id="TAG_LAYER_TAGID"></span><span id="tag_layer_tagid"></span><dl> <dt>**TAG\_LAYER\_TAGID**</dt> <dt>(0x1A \| **TAG\_TYPE\_DWORD**)</dt> </dl>                          | Layer shim **TAGID** attribute.<br/>                                                                       |
| <span id="TAG_MSI_TRANSFORM_TAGID"></span><span id="tag_msi_transform_tagid"></span><dl> <dt>**TAG\_MSI\_TRANSFORM\_TAGID**</dt> <dt>(0x1B \| **TAG\_TYPE\_DWORD**)</dt> </dl> | MSI transform **TAGID** attribute.<br/>                                                                    |
| <span id="TAG_LINKER_VERSION"></span><span id="tag_linker_version"></span><dl> <dt>**TAG\_LINKER\_VERSION**</dt> <dt>(0x1C \| **TAG\_TYPE\_DWORD**)</dt> </dl>                 | Linker version attribute of a file.<br/>                                                                   |
| <span id="TAG_LINK_DATE"></span><span id="tag_link_date"></span><dl> <dt>**TAG\_LINK\_DATE**</dt> <dt>(0x1D \| **TAG\_TYPE\_DWORD**)</dt> </dl>                                | Link date attribute of a file.<br/>                                                                        |
| <span id="TAG_UPTO_LINK_DATE"></span><span id="tag_upto_link_date"></span><dl> <dt>**TAG\_UPTO\_LINK\_DATE**</dt> <dt>(0x1E \| **TAG\_TYPE\_DWORD**)</dt> </dl>                | Link date attribute of a file. Matching is done up to and including this link date.<br/>                   |
| <span id="TAG_OS_SERVICE_PACK"></span><span id="tag_os_service_pack"></span><dl> <dt>**TAG\_OS\_SERVICE\_PACK**</dt> <dt>(0x1F \| **TAG\_TYPE\_DWORD**)</dt> </dl>             | Operating system service pack attribute for an executable entry.<br/>                                      |
| <span id="TAG_FLAG_TAGID"></span><span id="tag_flag_tagid"></span><dl> <dt>**TAG\_FLAG\_TAGID**</dt> <dt>(0x20 \| **TAG\_TYPE\_DWORD**)</dt> </dl>                             | Flags **TAGID** attribute.<br/>                                                                            |
| <span id="TAG_RUNTIME_PLATFORM"></span><span id="tag_runtime_platform"></span><dl> <dt>**TAG\_RUNTIME\_PLATFORM**</dt> <dt>(0x21 \| **TAG\_TYPE\_DWORD**)</dt> </dl>           | Run-time platform attribute of a file.<br/>                                                                |
| <span id="TAG_OS_SKU"></span><span id="tag_os_sku"></span><dl> <dt>**TAG\_OS\_SKU**</dt> <dt>(0x22 \| **TAG\_TYPE\_DWORD**)</dt> </dl>                                         | Operating system SKU attribute for an executable entry.<br/>                                               |
| <span id="TAG_OS_PLATFORM"></span><span id="tag_os_platform"></span><dl> <dt>**TAG\_OS\_PLATFORM**</dt> <dt>(0x23 \| **TAG\_TYPE\_DWORD**)</dt> </dl>                          | Operating system platform attribute.<br/>                                                                  |
| <span id="TAG_APP_NAME_RC_ID"></span><span id="tag_app_name_rc_id"></span><dl> <dt>**TAG\_APP\_NAME\_RC\_ID**</dt> <dt>(0x24 \| **TAG\_TYPE\_DWORD**)</dt> </dl>               | Application name resource identifier attribute for Apphelp entries.<br/>                                   |
| <span id="TAG_VENDOR_NAME_RC_ID"></span><span id="tag_vendor_name_rc_id"></span><dl> <dt>**TAG\_VENDOR\_NAME\_RC\_ID**</dt> <dt>(0x25 \| **TAG\_TYPE\_DWORD**)</dt> </dl>      | Vendor name resource identifier attribute for Apphelp entries.<br/>                                        |
| <span id="TAG_SUMMARY_MSG_RC_ID"></span><span id="tag_summary_msg_rc_id"></span><dl> <dt>**TAG\_SUMMARY\_MSG\_RC\_ID**</dt> <dt>(0x26 \| **TAG\_TYPE\_DWORD**)</dt> </dl>      | Summary message resource identifier attribute for Apphelp entries.<br/>                                    |
| <span id="TAG_VISTA_SKU"></span><span id="tag_vista_sku"></span><dl> <dt>**TAG\_VISTA\_SKU**</dt> <dt>(0x27 \| **TAG\_TYPE\_DWORD**)</dt> </dl>                                | Windows Vista SKU attribute.<br/>                                                                          |
| <span id="TAG_DESCRIPTION_RC_ID"></span><span id="tag_description_rc_id"></span><dl> <dt>**TAG\_DESCRIPTION\_RC\_ID**</dt> <dt>(0x28 \| **TAG\_TYPE\_DWORD**)</dt> </dl>       | Description resource identifier attribute for Apphelp entries.<br/>                                        |
| <span id="TAG_PARAMETER1_RC_ID"></span><span id="tag_parameter1_rc_id"></span><dl> <dt>**TAG\_PARAMETER1\_RC\_ID**</dt> <dt>(0x29 \| **TAG\_TYPE\_DWORD**)</dt> </dl>          | Parameter1 resource identifier attribute for Apphelp entries.<br/>                                         |
| <span id="TAG_TAGID"></span><span id="tag_tagid"></span><dl> <dt>**TAG\_TAGID**</dt> <dt>(0x801 \| **TAG\_TYPE\_DWORD**)</dt> </dl>                                            | **TAGID** attribute.<br/>                                                                                  |



The following entry is of type **TAG\_TYPE\_STRING** (0x8000).



| Constant/value                                                                                                                                                                                                                                                            | Description                         |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------|
| <span id="TAG_STRINGTABLE_ITEM"></span><span id="tag_stringtable_item"></span><dl> <dt>**TAG\_STRINGTABLE\_ITEM**</dt> <dt>(0x801 \| **TAG\_TYPE\_STRING**)</dt> </dl> | String table item entry.<br/> |



The following entries are of type **TAG\_TYPE\_NULL** (0x1000).



| Constant/value                                                                                                                                                                                                                                                                            | Description                                              |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------|
| <span id="TAG_INCLUDE"></span><span id="tag_include"></span><dl> <dt>**TAG\_INCLUDE**</dt> <dt>(0x1 \| **TAG\_TYPE\_NULL**)</dt> </dl>                                                 | Include list entry.<br/>                           |
| <span id="TAG_GENERAL"></span><span id="tag_general"></span><dl> <dt>**TAG\_GENERAL**</dt> <dt>(0x2 \| **TAG\_TYPE\_NULL**)</dt> </dl>                                                 | General purpose shim entry.<br/>                   |
| <span id="TAG_MATCH_LOGIC_NOT"></span><span id="tag_match_logic_not"></span><dl> <dt>**TAG\_MATCH\_LOGIC\_NOT**</dt> <dt>(0x3 \| **TAG\_TYPE\_NULL**)</dt> </dl>                       | NOT of matching logic entry.<br/>                  |
| <span id="TAG_APPLY_ALL_SHIMS"></span><span id="tag_apply_all_shims"></span><dl> <dt>**TAG\_APPLY\_ALL\_SHIMS**</dt> <dt>(0x4 \| **TAG\_TYPE\_NULL**)</dt> </dl>                       | Unused.<br/>                                       |
| <span id="TAG_USE_SERVICE_PACK_FILES"></span><span id="tag_use_service_pack_files"></span><dl> <dt>**TAG\_USE\_SERVICE\_PACK\_FILES**</dt> <dt>(0x5 \| **TAG\_TYPE\_NULL**)</dt> </dl> | Service pack information for Apphelp entries.<br/> |
| <span id="TAG_MITIGATION_OS"></span><span id="tag_mitigation_os"></span><dl> <dt>**TAG\_MITIGATION\_OS**</dt> <dt>(0x6 \| **TAG\_TYPE\_NULL**)</dt> </dl>                              | Mitigation at operating system scope entry.<br/>   |
| <span id="TAG_BLOCK_UPGRADE"></span><span id="tag_block_upgrade"></span><dl> <dt>**TAG\_BLOCK\_UPGRADE**</dt> <dt>(0x7 \| **TAG\_TYPE\_NULL**)</dt> </dl>                              | Upgrade block entry.<br/>                          |
| <span id="TAG_INCLUDEEXCLUDEDLL"></span><span id="tag_includeexcludedll"></span><dl> <dt>**TAG\_INCLUDEEXCLUDEDLL**</dt> <dt>(0x8 \| **TAG\_TYPE\_NULL**)</dt> </dl>                   | DLL include/exclude entry.<br/>                    |



The following entries are of type **TAG\_TYPE\_QWORD** (0x5000).



| Constant/value                                                                                                                                                                                                                                                                                   | Description                                                                                                    |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------|
| <span id="TAG_TIME"></span><span id="tag_time"></span><dl> <dt>**TAG\_TIME**</dt> <dt>(0x1 \| **TAG\_TYPE\_QWORD**)</dt> </dl>                                                                | Time attribute.<br/>                                                                                     |
| <span id="TAG_BIN_FILE_VERSION"></span><span id="tag_bin_file_version"></span><dl> <dt>**TAG\_BIN\_FILE\_VERSION**</dt> <dt>(0x2 \| **TAG\_TYPE\_QWORD**)</dt> </dl>                          | Bin file version attribute for file entries.<br/>                                                        |
| <span id="TAG_BIN_PRODUCT_VERSION"></span><span id="tag_bin_product_version"></span><dl> <dt>**TAG\_BIN\_PRODUCT\_VERSION**</dt> <dt>(0x3 \| **TAG\_TYPE\_QWORD**)</dt> </dl>                 | Bin product version attribute for file entries.<br/>                                                     |
| <span id="TAG_MODTIME"></span><span id="tag_modtime"></span><dl> <dt>**TAG\_MODTIME**</dt> <dt>(0x4 \| **TAG\_TYPE\_QWORD**)</dt> </dl>                                                       | Unused.<br/>                                                                                             |
| <span id="TAG_FLAG_MASK_KERNEL"></span><span id="tag_flag_mask_kernel"></span><dl> <dt>**TAG\_FLAG\_MASK\_KERNEL**</dt> <dt>(0x5 \| **TAG\_TYPE\_QWORD**)</dt> </dl>                          | Kernel flag mask attribute.<br/>                                                                         |
| <span id="TAG_UPTO_BIN_PRODUCT_VERSION"></span><span id="tag_upto_bin_product_version"></span><dl> <dt>**TAG\_UPTO\_BIN\_PRODUCT\_VERSION**</dt> <dt>(0x6 \| **TAG\_TYPE\_QWORD**)</dt> </dl> | Bin product version attribute of a file. Matching is done up to and including this product version.<br/> |
| <span id="TAG_DATA_QWORD"></span><span id="tag_data_qword"></span><dl> <dt>**TAG\_DATA\_QWORD**</dt> <dt>(0x7 \| **TAG\_TYPE\_QWORD**)</dt> </dl>                                             | **ULONGLONG** value attribute for a data entry.<br/>                                                     |
| <span id="TAG_FLAG_MASK_USER"></span><span id="tag_flag_mask_user"></span><dl> <dt>**TAG\_FLAG\_MASK\_USER**</dt> <dt>(0x8 \| **TAG\_TYPE\_QWORD**)</dt> </dl>                                | User flag mask attribute.<br/>                                                                           |
| <span id="TAG_FLAGS_NTVDM1"></span><span id="tag_flags_ntvdm1"></span><dl> <dt>**TAG\_FLAGS\_NTVDM1**</dt> <dt>(0x9 \| **TAG\_TYPE\_QWORD**)</dt> </dl>                                       | NTVDM1 flag mask attribute.<br/>                                                                         |
| <span id="TAG_FLAGS_NTVDM2"></span><span id="tag_flags_ntvdm2"></span><dl> <dt>**TAG\_FLAGS\_NTVDM2**</dt> <dt>(0xA \| **TAG\_TYPE\_QWORD**)</dt> </dl>                                       | NTVDM2 flag mask attribute.<br/>                                                                         |
| <span id="TAG_FLAGS_NTVDM3"></span><span id="tag_flags_ntvdm3"></span><dl> <dt>**TAG\_FLAGS\_NTVDM3**</dt> <dt>(0xB \| **TAG\_TYPE\_QWORD**)</dt> </dl>                                       | NTVDM3 flag mask attribute.<br/>                                                                         |
| <span id="TAG_FLAG_MASK_SHELL"></span><span id="tag_flag_mask_shell"></span><dl> <dt>**TAG\_FLAG\_MASK\_SHELL**</dt> <dt>(0xC \| **TAG\_TYPE\_QWORD**)</dt> </dl>                             | Shell flag mask attribute.<br/>                                                                          |
| <span id="TAG_UPTO_BIN_FILE_VERSION"></span><span id="tag_upto_bin_file_version"></span><dl> <dt>**TAG\_UPTO\_BIN\_FILE\_VERSION**</dt> <dt>(0xD \| **TAG\_TYPE\_QWORD**)</dt> </dl>          | Bin file version attribute of a file. Matching is done up to and including this file version.<br/>       |
| <span id="TAG_FLAG_MASK_FUSION"></span><span id="tag_flag_mask_fusion"></span><dl> <dt>**TAG\_FLAG\_MASK\_FUSION**</dt> <dt>(0xE \| **TAG\_TYPE\_QWORD**)</dt> </dl>                          | Fusion flag mask attribute.<br/>                                                                         |
| <span id="TAG_FLAG_PROCESSPARAM"></span><span id="tag_flag_processparam"></span><dl> <dt>**TAG\_FLAG\_PROCESSPARAM**</dt> <dt>(0xF \| **TAG\_TYPE\_QWORD**)</dt> </dl>                        | Process param flag attribute.<br/>                                                                       |
| <span id="TAG_FLAG_LUA"></span><span id="tag_flag_lua"></span><dl> <dt>**TAG\_FLAG\_LUA**</dt> <dt>(0x10 \| **TAG\_TYPE\_QWORD**)</dt> </dl>                                                  | LUA flag attribute.<br/>                                                                                 |
| <span id="TAG_FLAG_INSTALL"></span><span id="tag_flag_install"></span><dl> <dt>**TAG\_FLAG\_INSTALL**</dt> <dt>(0x11 \| **TAG\_TYPE\_QWORD**)</dt> </dl>                                      | Install flag attribute.<br/>                                                                             |



The following entries are of type **TAG\_TYPE\_BINARY** (0x9000).



| Constant/value                                                                                                                                                                                                                                                     | Description                                                    |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------|
| <span id="TAG_PATCH_BITS"></span><span id="tag_patch_bits"></span><dl> <dt>**TAG\_PATCH\_BITS**</dt> <dt>(0x2 \| **TAG\_TYPE\_BINARY**)</dt> </dl>              | Patch file bits attribute.<br/>                          |
| <span id="TAG_FILE_BITS"></span><span id="tag_file_bits"></span><dl> <dt>**TAG\_FILE\_BITS**</dt> <dt>(0x3 \| **TAG\_TYPE\_BINARY**)</dt> </dl>                 | File bits attribute.<br/>                                |
| <span id="TAG_EXE_ID"></span><span id="tag_exe_id"></span><dl> <dt>**TAG\_EXE\_ID**</dt> <dt>(0x4 \| **TAG\_TYPE\_BINARY**)</dt> </dl>                          | **GUID** attribute of an executable entry.<br/>          |
| <span id="TAG_DATA_BITS"></span><span id="tag_data_bits"></span><dl> <dt>**TAG\_DATA\_BITS**</dt> <dt>(0x5 \| **TAG\_TYPE\_BINARY**)</dt> </dl>                 | Data bits attribute.<br/>                                |
| <span id="TAG_MSI_PACKAGE_ID"></span><span id="tag_msi_package_id"></span><dl> <dt>**TAG\_MSI\_PACKAGE\_ID**</dt> <dt>(0x6 \| **TAG\_TYPE\_BINARY**)</dt> </dl> | MSI package identifier attribute of an MSI package.<br/> |
| <span id="TAG_DATABASE_ID"></span><span id="tag_database_id"></span><dl> <dt>**TAG\_DATABASE\_ID**</dt> <dt>(0x7 \| **TAG\_TYPE\_BINARY**)</dt> </dl>           | **GUID** attribute of a database.<br/>                   |
| <span id="TAG_INDEX_BITS"></span><span id="tag_index_bits"></span><dl> <dt>**TAG\_INDEX\_BITS**</dt> <dt>(0x801 \| **TAG\_TYPE\_BINARY**)</dt> </dl>            | Index bits attribute.<br/>                               |



The following entries are of type **TAG\_TYPE\_WORD** (0x3000).



| Constant/value                                                                                                                                                                                                                                      | Description                                        |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------|
| <span id="TAG_MATCH_MODE"></span><span id="tag_match_mode"></span><dl> <dt>**TAG\_MATCH\_MODE**</dt> <dt>(0x1 \| **TAG\_TYPE\_WORD**)</dt> </dl> | Match mode attribute.<br/>                   |
| <span id="TAG_TAG"></span><span id="tag_tag"></span><dl> <dt>**TAG\_TAG**</dt> <dt>(0x801 \| **TAG\_TYPE\_WORD**)</dt> </dl>                     | TAG entry.<br/>                              |
| <span id="TAG_INDEX_TAG"></span><span id="tag_index_tag"></span><dl> <dt>**TAG\_INDEX\_TAG**</dt> <dt>(0x802 \| **TAG\_TYPE\_WORD**)</dt> </dl>  | Index TAG attribute for an index entry.<br/> |
| <span id="TAG_INDEX_KEY"></span><span id="tag_index_key"></span><dl> <dt>**TAG\_INDEX\_KEY**</dt> <dt>(0x803 \| **TAG\_TYPE\_WORD**)</dt> </dl>  | Index key attribute for an index entry.<br/> |



## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Exposeenums2managed.h (include Axextendenums.h)</dt> </dl> |



## See also

<dl> <dt>

[TAG Types](tag-types.md)
</dt> <dt>

[**TAGID**](tagid.md)
</dt> <dt>

[**TAGREF**](tagref.md)
</dt> </dl>

 

 





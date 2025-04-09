---
title: Predefined Category Values
description: Predefined Category Values
ms.assetid: 04c0632d-ac64-4081-ba95-c11feb3f40dd
ms.topic: reference
ms.date: 05/31/2018
---

# Predefined Category Values

The following values identify categories implemented by Text Services Framework (TSF).

**GUID_TFCAT_CATEGORY_OF_TIP** specifies the type of text input processor (TIP).

GUIDs for the TIP category. Each category contains TIP classes.

|  Identifier                |
|----------------------------|
| GUID_TFCAT_TIP_KEYBOARD    |
| GUID_TFCAT_TIP_SPEECH      |
| GUID_TFCAT_TIP_HANDWRITING |

GUIDs for the TIP Capability category. Each category contains a Property GUID.

|  Identifier                            |
|----------------------------------------|
| GUID_TFCAT_TIPCAP_SECUREMODE           |
| GUID_TFCAT_TIPCAP_UIELEMENTENABLED     |
| GUID_TFCAT_TIPCAP_INPUTMODECOMPARTMENT |
| GUID_TFCAT_TIPCAP_COMLESS              |
| GUID_TFCAT_TIPCAP_WOW16                |
| GUID_TFCAT_TIPCAP_IMMERSIVESUPPORT     |
| GUID_TFCAT_TIPCAP_SYSTRAYSUPPORT       |

GUIDs for the Property category. Each category contains a Property GUID.

|  Identifier               |
|---------------------------|
| GUID_TFCAT_PROP_AUDIODATA |
| GUID_TFCAT_PROP_INKDATA   |

GUIDs for the Property style.

|  Identifier                        |
|------------------------------------|
| GUID_TFCAT_PROPSTYLE_CUSTOM        |
| GUID_TFCAT_PROPSTYLE_STATIC        |
| GUID_TFCAT_PROPSTYLE_STATICCOMPACT |

GUIDs for the Display Attribute Provider category.

|  Identifier                         |
|-------------------------------------|
| GUID_TFCAT_DISPLAYATTRIBUTEPROVIDER |
| GUID_TFCAT_DISPLAYATTRIBUTEPROPERTY |

## Requirements

**Redistributable:** Requires TSF 1.0 on Windows 2000.

**Header:** Declared in Msctf.idl and Msctf.h.

## Related topics

- [**ITfCategoryMgr::EnumItemsInCategory**](/windows/desktop/api/Msctf/nf-msctf-itfcategorymgr-enumitemsincategory)
- [**ITfCategoryMgr::RegisterCategory**](/windows/desktop/api/Msctf/nf-msctf-itfcategorymgr-registercategory)
- [**ITfInputProcessorProfiles::GetDefaultLanguageProfile**](/windows/desktop/api/Msctf/nf-msctf-itfinputprocessorprofiles-getdefaultlanguageprofile)

 

 





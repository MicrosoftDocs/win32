---
title: Predefined Category Values
description: Predefined Category Values
ms.assetid: 04c0632d-ac64-4081-ba95-c11feb3f40dd
ms.topic: article
ms.date: 05/31/2018
---

# Predefined Category Values

The following values identify categories implemented by Text Services Framework.

**GUID_TFCAT_CATEGORY_OF_TIP** categrorize the types of tips.

GUIDs for the Tips category. Each category contains Tips classes.

|  Identifier                |
|----------------------------|
| GUID_TFCAT_TIP_KEYBOARD    |
| GUID_TFCAT_TIP_SPEECH      |
| GUID_TFCAT_TIP_HANDWRITING |

**Starting Windows 8:** GUIDs for the tip capability category. Each category contains Property GUID.

|  Identifier                            |
|----------------------------------------|
| GUID_TFCAT_TIPCAP_SECUREMODE           |
| GUID_TFCAT_TIPCAP_UIELEMENTENABLED     |
| GUID_TFCAT_TIPCAP_INPUTMODECOMPARTMENT |
| GUID_TFCAT_TIPCAP_COMLESS              |
| GUID_TFCAT_TIPCAP_WOW16                |
| GUID_TFCAT_TIPCAP_IMMERSIVESUPPORT     |
| GUID_TFCAT_TIPCAP_SYSTRAYSUPPORT       |

GUIDs for the property category. Each category contains Property GUID.

|  Identifier               |
|---------------------------|
| GUID_TFCAT_PROP_AUDIODATA |
| GUID_TFCAT_PROP_INKDATA   |

GUIDs for the property style.

|  Identifier                      |
|----------------------------------|
GUID_TFCAT_PROPSTYLE_CUSTOM        |
GUID_TFCAT_PROPSTYLE_STATIC        |
GUID_TFCAT_PROPSTYLE_STATICCOMPACT |

GUIDs for the display attribute provider category.

|  Identifier                         |
|-------------------------------------|
| GUID_TFCAT_DISPLAYATTRIBUTEPROVIDER |
| GUID_TFCAT_DISPLAYATTRIBUTEPROPERTY |

## Requirements

**Redistributable:** Requires TSF 1.0 on Windows 2000.

**Header:** Declared in Msctf.idl and Msctf.h.

## Related topics

<dl> <dt>

[**ITfCategoryMgr::EnumItemsInCategory**](/windows/desktop/api/Msctf/nf-msctf-itfcategorymgr-enumitemsincategory)
</dt> <dt>

[**ITfCategoryMgr::RegisterCategory**](/windows/desktop/api/Msctf/nf-msctf-itfcategorymgr-registercategory)
</dt> <dt>

[**ITfInputProcessorProfiles::GetDefaultLanguageProfile**](/windows/desktop/api/Msctf/nf-msctf-itfinputprocessorprofiles-getdefaultlanguageprofile)
</dt> </dl>

 

 





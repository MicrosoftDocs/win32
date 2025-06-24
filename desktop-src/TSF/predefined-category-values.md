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

The following table shows GUIDs for the TIP category. Each category contains TIP classes.

|  Identifier                | Description                                                                       |
|----------------------------|----------------------------|
| GUID_TFCAT_TIP_KEYBOARD    | Keyboard TIP    |
| GUID_TFCAT_TIP_SPEECH      | Speech TIP    |
| GUID_TFCAT_TIP_HANDWRITING | Handwriting TIP    |

The following table shows GUIDs for the TIP Capability category. Each category contains a Property GUID.

|  Identifier                | Description                                                                       |
|----------------------------|----------------------------|
| GUID_TFCAT_TIPCAP_SECUREMODE           | TIP supports secure mode.  |
| GUID_TFCAT_TIPCAP_UIELEMENTENABLED     | TIP supports the UIElement.     |
| GUID_TFCAT_TIPCAP_INPUTMODECOMPARTMENT | TIP supports input mode compartment.    |
| GUID_TFCAT_TIPCAP_COMLESS              | TIP supports activation without COM.  |
| GUID_TFCAT_TIPCAP_WOW16                | TIP supports activation on 16bit task.    |
| GUID_TFCAT_TIPCAP_IMMERSIVESUPPORT     | TIP supports running properly in a Windows Store app.   |
| GUID_TFCAT_TIPCAP_SYSTRAYSUPPORT       | TIP supports inclusion in the System Tray. This is used for text services that do not set the TF_IPP_CAPS_IMMERSIVESUPPORT flag but are still compatible with the System Tray.    |

The following table shows GUIDs for the Property category. Each category contains a Property GUID.

|  Identifier                | Description                                                                       |
|----------------------------|----------------------------|
| GUID_TFCAT_PROP_AUDIODATA |  TIP audio data associated with text from the speech text service.   |
| GUID_TFCAT_PROP_INKDATA   |   TIP ink data.  |

The following table shows GUIDs for the Property style.

|  Identifier                | Description                                                                       |
|----------------------------|----------------------------|
| GUID_TFCAT_PROPSTYLE_CUSTOM        | A custom property object stores the range information for each range that the property applies to. It does not, however, store the actual data for the property. Instead, a custom property stores an ITfPropertyStore object. The TSF manager uses this object to access and maintain the property data.ITfReadOnlyProperty::GetType returns the GUID_TFCAT_PROPSTYLE_CUSTOM category.    |
| GUID_TFCAT_PROPSTYLE_STATIC        |  A static property object stores the property data with text. It also stores the range of text information for each range that the property applies to. ITfReadOnlyProperty::GetType returns the GUID_TFCAT_PROPSTYLE_STATIC category.   |
| GUID_TFCAT_PROPSTYLE_STATICCOMPACT | A static-compact property object is identical to a static property object except a static-compact property does not store range data. When the range covered by a static-compact property is requested, a range is created for each group of adjacent properties. Static-compact properties are the most efficient way to store properties on a per-character basis. ITfReadOnlyProperty::GetType returns the GUID_TFCAT_PROPSTYLE_STATICCOMPACT category.    |

The following table shows GUIDs for the Display Attribute Provider category.

|  Identifier                | Description                                                                       |
|----------------------------|----------------------------|
| GUID_TFCAT_DISPLAYATTRIBUTEPROVIDER | TIP is a DISPLAYATTRIBUTEPROVIDER.    |
| GUID_TFCAT_DISPLAYATTRIBUTEPROPERTY | TIP is a DISPLAYATTRIBUTEPROPERTY.    |

## Requirements

**Redistributable:** Requires TSF 1.0 on Windows 2000.

**Header:** Declared in Msctf.idl and Msctf.h.

## Related topics

- [**ITfCategoryMgr::EnumItemsInCategory**](/windows/desktop/api/Msctf/nf-msctf-itfcategorymgr-enumitemsincategory)
- [**ITfCategoryMgr::RegisterCategory**](/windows/desktop/api/Msctf/nf-msctf-itfcategorymgr-registercategory)
- [**ITfInputProcessorProfiles::GetDefaultLanguageProfile**](/windows/desktop/api/Msctf/nf-msctf-itfinputprocessorprofiles-getdefaultlanguageprofile)

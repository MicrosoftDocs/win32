---
title: Reserved Property Identifiers
description: Reserved property identifiers cannot be used as property identifiers (ID). Any property identifier (ID) can be used except 0, 1, and any value greater than, or equal to, 0x80000000. These property identifier values are reserved for use by applications.
ms.assetid: d313a7b1-4cac-41f8-ba38-bf9cfaeb9d5c
ms.topic: article
ms.date: 05/31/2018
---

# Reserved Property Identifiers

Reserved property identifiers cannot be used as property identifiers (ID). Any property identifier (ID) can be used except 0, 1, and any value greater than, or equal to, 0x80000000. These property identifier values are reserved for use by applications.

The following table lists the reserved property IDs and the description of what the property ID is reserved for.



| Reserved property ID | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0                    | Reserved for creating an optional [Property Set Display Name Dictionary](property-set-display-name-dictionary.md). This enables property set users to attach meaning to properties, beyond those provided by the type indicator.                                                                                                                                                                                                                                                                                                                                                                |
| 1                    | Reserved as an indicator of the code page (Windows) or Script (Macintosh) to use when interpreting the strings in the property set.<br/> All string values in the property set must be stored with the same code page. The originating operating system value in the property set header (PROPERTYSETHEADER::dwOSVer) determines whether the code page indicator corresponds to a Windows code page or Macintosh script.<br/>                                                                                                                                                        |
| 0x80000000           | Reserved as an indication of the locale for which the property set is written.<br/> The default locale for a property set is the system default locale (LOCALE\_SYSTEM\_DEFAULT). For more information about LOCALE\_SYSTEM\_DEFAULT, see the Win32 APIs. The default is used in the event that the locale indicator does not exist in the property set.<br/>                                                                                                                                                                                                                        |
| 0x80000003           | Reserved as an indicator of property set behaviors. This property ID value is a VT\_UI4 and starts with a **DWORD** data type containing the value VT\_UI4 followed by a **DWORD** indicating property set behavior.<br/> Currently, the only bit in this value that is defined is the low order bit (0x1). If this bit is set, it indicates that property set names, indicated by property ID 0, should be considered case sensitive. If this bit is not set or if the behavior property (ID 0x80000003) does not exist, then the names should be considered case insensitive.<br/> |
| 0xFFFFFFFF           | Reserved for the convenience of programmability. It should never appear in a serialized property set.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |



 

Property identifiers with the high bit set (that is, negative values) are reserved for future use by Microsoft.

Of the reserved properties, those with ID values in the range 0x80000000 to 0xBFFFFFFF are considered read-only by implementations that do not understand their meaning. For example, if an implementation does not understand the meaning of property 0x80000000, it should allow that property to be read but not written or deleted. Such an implementation should allow a property in the range 0xC0000000 to 0xFFFFFFFE to be read, written, or deleted. The Property ID 0xFFFFFFFF is a reserved value and should never appear in a serialized property set.

## Property Set Locale

Applications can choose to either support the locale or use the default behavior. It is recommended that applications allow users to specify a working locale. Such applications should write the user-specified locale identifier to the property. Applications that use the user default locale (LOCALE\_USER\_DEFAULT) should write the user default locale identifier to the property. For more information about LOCALE\_USER\_DEFAULT, see the Win32 API.

> [!Note]  
> If the [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage) interface is used to create a property set, the user default locale is automatically written as the Locale Indicator.

 

Applications should also handle the case of a foreign object, which is one where the locale is not the application locale, the user locale, or the system locale.

The locale indicator property is of type VT\_U14, and therefore consists of a **DWORD** that contains VT\_U14, followed by a **DWORD** containing the Locale Identifier (LCID), as defined in the Win32 API.

## Code Page Indicator

When an application that is not the author of a property set changes a property of type string in the set, it should examine the code page indicator and take one of the following actions:

-   Write the string in the format specified by the code page indicator.
-   Replace and rewrite to change the code page.

If an application cannot recognize this indicator, it should not modify the property. All creators of property sets must write a code page indicator; however, if the code page indicator is not present, the prevailing code page on the reader's computer must be assumed.

> [!Note]  
> If the [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage) interface is used to create a property set, the code page indicator is automatically written.

 

Possible values for the code page are given in the Win32 API (for more information, see the [**GetACP**](/windows/desktop/api/winnls/nf-winnls-getacp) function) and *Inside Macintosh Volume VI*, pages 14-111. (These resources may not be available in some languages and countries.) For example, the code page US ANSI is represented by 0x04E4 (1252 in decimal) while the code page for Unicode is 0x04B0 (1200 in decimal).

It is recommended that the Unicode code page be used when possible, and use VT\_LPWSTR instead of VT\_LPSTR to avoid multibyte <-> Unicode conversions during storage and retrieval. Using the same code page for all property sets is the only way to achieve interoperable property sets on a worldwide basis. In either the Unicode or non-Unicode code page, be aware that the count at the start of a VT\_LPSTR or VT\_BSTR is a **byte** count and not a **character** count. This byte count includes the one or two zero bytes at the end of the string (the **NULL** terminator of the string).

Property ID 1 is a VT\_I2 type and starts with a **DWORD** that contains the value VT\_I2 followed by a **SHORT** that indicates the code page.

 


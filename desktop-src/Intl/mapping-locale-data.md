---
description: NLS includes a number of API functions that your applications can use to map locale data between locale identifiers and locale names, and list neutral locales.
ms.assetid: 01bc261d-dfee-430e-86c9-cfafe82856c8
title: Mapping Locale Data
ms.topic: article
ms.date: 05/31/2018
---

# Mapping Locale Data

NLS includes a number of API functions that your applications can use to map locale data between [locale identifiers](locale-identifiers.md) and [locale names](locale-names.md), and list neutral locales. This topic discusses the use of these functions on Windows Vista and later and on pre-Windows Vista operating systems (sometimes called "downlevel systems").

## Map Locale Data on Windows Vista and Later

NLS provides several locale mapping functions for use by applications that you develop to run on Windows Vista and later. It also includes functions that your applications can use to enumerate neutral locales.

**Use the Standard Conversion Functions for Data Mapping**

To map between a locale name and a locale identifier, your application can call the [**LocaleNameToLCID**](/windows/desktop/api/Winnls/nf-winnls-localenametolcid) function. The application uses [**LCIDToLocaleName**](/windows/desktop/api/Winnls/nf-winnls-lcidtolocalename) to map between a locale identifier and a locale name.

**List Neutral Locales**

To enumerate neutral locales for Windows 7 and later, your application can call [**EnumSystemLocalesEx**](/windows/desktop/api/Winnls/nf-winnls-enumsystemlocalesex) with *dwFlags* set to [**LOCALE\_NEUTRALDATA**](locale-neutraldata.md). It can also use [**GetLocaleInfoEx**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoex) with *LCType* set to [**LOCALE\_INEUTRAL**](locale-ineutral.md).

## Map Locale Data on Pre-Windows Vista Operating Systems

NLS includes a direct-link library (DLL) to use for applications that you develop to run on pre-Windows Vista operating systems. The DLL supports both conversion and listing functions for data mapping.

> [!Note]  
> Applications that only run on Windows Vista and later should not use the downlevel mapping or listing functions.

 

**Use the Downlevel Conversion Functions for Data Mapping**

Your application targeted at a downlevel system can call the [**DownlevelLCIDToLocaleName**](downlevellcidtolocalename.md) function to convert a locale identifier to a locale name. If it needs to convert a locale name to a locale identifier, it should call [**DownlevelLocaleNameToLCID**](downlevellocalenametolcid.md).

**Use the Downlevel Listing Functions to Enumerate Neutral Locales**

Your application should call the [**DownlevelGetParentLocaleLCID**](downlevelgetparentlocalelcid.md) to retrieve the locale identifier of the parent for a locale. If the application needs to get the locale name of the parent for the locale, it should call [**DownlevelGetParentLocaleName**](downlevelgetparentlocalename.md).

## Related topics

<dl> <dt>

[Using National Language Support](using-national-language-support.md)
</dt> <dt>

[Locale Identifiers](locale-identifiers.md)
</dt> <dt>

[Locale Names](locale-names.md)
</dt> </dl>

 

 




---
description: On Windows Vista and later, you can use pseudo-locales for testing the localizability of applications. This topic includes procedures for using pseudo-codes.
ms.assetid: 1eccdbb9-a1bd-443a-a5f6-d64c9e5c87b3
title: Using pseudo-locales for localizability testing
ms.topic: article
ms.date: 07/05/2018
---

# Using pseudo-locales for localizability testing

[Pseudo-locales](pseudo-locales.md) are built in to Windows Vista and later, so that you can access them via National Language Support (NLS) APIs. You can use pseudo-locales to test the [localizability](/windows/uwp/design/globalizing/globalizing-portal) of your applications. This topic includes procedures for using pseudo-codes.

> [!NOTE]
> One task that needs special consideration when it comes to pseudo-locales is enumerating them; whether in your code, or in the regional and language options portion of the Control Panel. More on that later in this topic.

The names of the pseudo-locales are "qps-ploc", "qps-ploca", and "qps-plocm". As of Windows 10, the pseudo-locale "qps-Latn-x-sh" is also available.

## Retrieve information about pseudo-locales

You can use [**GetLocaleInfoEx**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoex) to retrieve information about a pseudo-locale. Pass into the function the name of the particular pseudo-locale (see the list of names above). For example, "qps-plocm" for the mirrored pseudo-locale.

```cpp
wchar_t languageIdentifier[5];
int rc{ ::GetLocaleInfoEx(L"qps-plocm", LOCALE_ILANGUAGE, languageIdentifier, 5) };
```

## Use LocaleNameToLCID with pseudo-locales

You can call the NLS mapping function [**LocaleNameToLCID**](/windows/desktop/api/Winnls/nf-winnls-localenametolcid) with the name of a pseudo-locale.

```cpp
LCID lcid{ ::LocaleNameToLCID(L"qps-plocm", 0) };
```

## Enable pseudo-locales for enumeration

In your application, you can call [**EnumSystemLocalesEx**](/windows/desktop/api/Winnls/nf-winnls-enumsystemlocalesex) to enumerate the locales that the system recognizes. The regional and language options portion of the Control Panel also calls **EnumSystemLocalesEx** to build the list of locales that it displays. However, by default, the four pseudo-locales listed above are not recognized by the system, so they won't be returned by **EnumSystemLocalesEx**. For systems from Windows Vista up to and including Windows 10, version 1709, the solution is to enable pseudo-locales by adding keys to the Windows Registry.

The edits are made under the HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control\\Nls key for the languages installed on the operating system. You can make these settings to enable the pseudo-locales. Each key shown below is the hexadecimal LCID corresponding to the pseudo-locale being enabled. Each value is of type string (REG\_SZ).

```
[HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Nls\Locale]
"00000501"="1" // qps-ploc (Windows Vista and later)
"000005fe"="7" // qps-ploca (Windows Vista and later)
"00000901"="1" // qps-Latn-x-sh (Windows 10 and later)
"000009ff"="d" // qps-plocm (Windows Vista and later)
```

For Windows 10, version 1803, editing the Windows Registry like this has no effect. But you can still call the non-enumerating NLS APIs with the names of the pseudo-locales (see the code examples above) to populate your user interface (UI).

## Related topics

* [Using National Language Support](using-national-language-support.md)
* [Pseudo-Locales](pseudo-locales.md)
* [EnumSystemLocalesEx](/windows/desktop/api/Winnls/nf-winnls-enumsystemlocalesex)
* [GetLocaleInfoEx](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoex)
* [LocaleNameToLCID](/windows/desktop/api/Winnls/nf-winnls-localenametolcid)

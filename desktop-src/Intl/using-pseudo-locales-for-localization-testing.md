---
Description: 'On Windows Vista and later, you can use pseudo-locales for testing the localization of applications. This topic includes procedures for using pseudo-codes.'
ms.assetid: '1eccdbb9-a1bd-443a-a5f6-d64c9e5c87b3'
title: 'Using Pseudo-Locales for Localization Testing'
---

# Using Pseudo-Locales for Localization Testing

On Windows Vista and later, you can use [pseudo-locales](pseudo-locales.md) for testing the localization of applications. This topic includes procedures for using pseudo-codes.

## Enable a Pseudo-Locale

You can enable a pseudo-locale using registry key settings. The settings are made under the HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control\\Nls key for the languages installed on the operating system. You can make the following settings to enable the supported pseudo-locales:


```C++
[HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Nls\Locale]
"00000501"="1"
"000009ff"="d"
"000005fe"="7"
```



## Enumerate Pseudo-Locales

Note that NLS does not automatically enumerate the pseudo-locales or expose them in the regional and language options portion of the Control Panel. They are only enumerable if values are set in the registry. Your application can then call [**EnumSystemLocalesEx**](enumsystemlocalesex.md) to enumerate the locales that the registry recognizes. The values for the locales are all of string (REG\_SZ) type.

## Retrieve Locale Information

The application uses [**GetLocaleInfoEx**](getlocaleinfoex.md) to retrieve information about a pseudo-locale. In the call, the application passes the locale name of the particular pseudo-locale, for example, "qps-mirr" for the mirrored pseudo-locale.

## Use LocaleNameToLCID with Pseudo-Locales

You can use the NLS mapping function [**LocaleNameToLCID**](localenametolcid.md) for pseudo-locales. This function works even if the locales are not enabled, because it does not have to check the registry key for a locale.

## Related topics

<dl> <dt>

[Using National Language Support](using-national-language-support.md)
</dt> <dt>

[Pseudo-Locales](pseudo-locales.md)
</dt> <dt>

[**EnumSystemLocalesEx**](enumsystemlocalesex.md)
</dt> <dt>

[**GetLocaleInfoEx**](getlocaleinfoex.md)
</dt> <dt>

[**LocaleNameToLCID**](localenametolcid.md)
</dt> </dl>

 

 




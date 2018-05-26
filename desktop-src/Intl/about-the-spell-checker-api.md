---
Description: For users worldwide, textual input is part of a modern computing experience, for blogging, commenting, tweeting, instant messaging, or any other kind of text typing. In Windows 8, spell checking is built-in to edit controls.
ms.assetid: ED569D4F-568B-4381-91C3-8EAEDA4DD47C
title: About the Spell Checking API
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# About the Spell Checking API

For users worldwide, textual input is part of a modern computing experience, for blogging, commenting, tweeting, instant messaging, or any other kind of text typing. In Windows 8, spell checking is built-in to edit controls.

Developers can use the spell checking API in their apps to consume available spell checking services. Developers can also create spell checkers that become providers and are integrated into the Windows spell checking framework.

The Spell Checking API is designed for use by professional C/C++ developers of Windows Component Object Model (COM) apps. The Spell Checking API is not supported for use in a Windows or ASP.NET service.

## Versioning

The Spell Checking API is available beginning with the Windows 8 or Windows Server 2012. Future additions to the API will be handled by creating new interfaces that can be determined using [**QueryInterface**](com.iunknown_queryinterface) on the existing ones.

## Interfaces

All interfaces must be released when they are no longer used. All returned (out parameter) **LPWSTR** strings (and **LPOLESTR** items from [**IEnumString**](com.ienumstring)) must be released with [**CoTaskMemFree**](com.cotaskmemfree) when no longer used.

## Error handling

Errors are returned as **HRESULT**s. [**IErrorInfo**](automat.ierrorinfo) and [**ISupportErrorInfo**](automat.isupporterrorinfo) are not supported in this API. Errors are not particularly actionable except for incorrect arguments.

Standard RPC error codes may be returned by any of the API calls because they are out-of-proc. Standard RPC timeouts apply.

## Security

The Spell Checking API may load external code (spell check providers). It will run this code out-of-proc and under a restricted security context.

## Dictionary files

The user-specific dictionaries for a language, which hold the content for the Added, Excluded, and AutoCorrect word lists, are located under %AppData%\\Microsoft\\Spelling\\*&lt;language tag&gt;*. The filenames are default.dic (Added), default.exc (Excluded) and default.acl (AutoCorrect). The files are UTF-16 LE plaintext that must start with the appropriate Byte Order Mark (BOM). Each line contains a word (in the Added and Excluded word lists), or an autocorrect pair with the words separated by a vertical bar ("\|") (in the AutoCorrect word list). Other .dic, .exc, and .acl files present in the directory will be detected by the spell checking service and added to the user word lists. These files are considered to be read-only and are not modified by the spell checking API.

## Installing a spell checking provider

The installation of a spell checking provider must place all the files it uses in a location that allows read access from the SID ([security identifier](security.security_identifiers)) "ALL APPLICATION PACKAGES". Installing it in a folder under "Program Files" works well. Also, the provider must set some keys in the registry for it to appear to the spell checking API. It can be in either the HKEY\_CURRENT\_USER hive or the HKEY\_LOCAL\_MACHINE hive depending on whether it should install only for the current user or all users.


```
Key: <Registry hive>\SOFTWARE\Classes\CLSID\<Server CLSID>
     Default (REG_SZ) = <Name of the provider>

Key: <Registry hive>\SOFTWARE\Classes\CLSID\<Server CLSID>\InprocServer32
     ThreadingModel (REG_SZ) = "Both"

Key: <Registry hive>\SOFTWARE\Classes\CLSID\<Server CLSID>\Version
     Version (REG_SZ) = <Version>

Key: <Registry hive>\SOFTWARE\Microsoft\Spelling\Spellers\<Provider id string>
     CLSID (REG_SZ) = <CLSID of the COM Server that implements the provider>
```



The [spell checking provider sample](http://go.microsoft.com/fwlink/p/?linkid=242819) provides an example of the registration needed to install a provider.

If you are creating new spell checking options for a spell checking provider, see [**IOptionDescription::Id**](/windows/win32/Spellcheck/nf-spellcheck-ioptiondescription-get_id?branch=master) for guidance on naming.

## Related topics

<dl> <dt>

[Spell Checking API Reference](spell-checker-api-reference.md)
</dt> <dt>

[Spell checking client sample](http://go.microsoft.com/fwlink/p/?linkid=242818)
</dt> <dt>

[Spell checking provider sample](http://go.microsoft.com/fwlink/p/?linkid=242819)
</dt> <dt>

[**IOptionDescription::Id**](/windows/win32/Spellcheck/nf-spellcheck-ioptiondescription-get_id?branch=master)
</dt> <dt>

[**IEnumString**](com.ienumstring)
</dt> <dt>

[**QueryInterface**](com.iunknown_queryinterface)
</dt> </dl>

 

 




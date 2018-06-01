---
Description: Language-Specific Registry Entries
ms.assetid: bc03bdfd-55ab-4cc5-96fe-fdf7bf591d9e
title: Language-Specific Registry Entries
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Language-Specific Registry Entries

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Language-specific registry entries contain the word breaker, stemmer, and noise-word list appropriate for a given language. They also contain the HTML error pages returned in response to invalid user and administrator actions.

Language-specific registry entries are found as language-specifier subkeys under the key

**HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\ContentIndex\\Language\\*Language\_Dialect***.

The name of the *Language\_Dialect* key has two parts: the name of the language (*Language*) and the dialect or secondary language (*Dialect*). The combination of language and dialect can have any of the possibilities made using the [**MAKELANGID**](https://www.bing.com/search?q=**MAKELANGID**) macro. For example, if the primary language is French and the dialect (secondary language) is Belgian, the name of the *Language\_Dialect* key is **French\_Belgian**. Although the language-specifier subkeys contain the registry entries appropriate for the language and dialect, the [**Locale**](locale.md) entry contains the actual value that specifies which language and dialect to use.

Each language-specifier subkey can include the following entries. The **ISAPI\*** entries are for the ISAPI implementation under IIS. None of the **ISAPI\*** entries can be overridden by an identically named entry under the [**Catalog**](catalog--property--and-scope-registry-entries.md) subkey for a specific catalog.



| Registry Name                                                  | Short Description                                                           |
|----------------------------------------------------------------|-----------------------------------------------------------------------------|
| [**ISAPIDefaultErrorFile**](isapidefaulterrorfile.md)         | Full virtual path to the generic error template.                            |
| [**ISAPIHTXErrorFile**](isapihtxerrorfile.md)                 | Full virtual path to the HTML error template for HTX errors.                |
| [**ISAPIIDQErrorFile**](isapiidqerrorfile.md)                 | Full virtual path to the Internet Data Query error template for IDQ errors. |
| [**ISAPIRestrictionErrorFile**](isapirestrictionerrorfile.md) | Full virtual path to the query restriction syntax error template.           |
| [**Locale**](locale.md)                                       | Locale identifier (LCID) of language to use.                                |
| [**NoiseFile**](noisefile.md)                                 | File name of the list of noise words to use.                                |
| [**StemmerClass**](stemmerclass.md)                           | Microsoft ActiveX class identifier (CLSID) for the stemming component.      |
| [**StemmerDictionary**](stemmerdictionary.md)                 | File name for the stemming dictionary component of certain locales.         |
| [**WBreakerClass**](wbreakerclass.md)                         | ActiveX CLSID for the word breaker component.                               |



 

 

 




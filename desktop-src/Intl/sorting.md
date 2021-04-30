---
description: For NLS, sorting (also known as &\#0034;collation&\#0034;) is the arrangement of strings.
ms.assetid: 8ca3af60-1ddb-4bfb-8aa6-8db769b3982d
title: Sorting (Internationalization)
ms.topic: article
ms.date: 05/31/2018
---

# Sorting

For NLS, sorting (also known as "collation") is the arrangement of strings. There are two types of sorting:

-   Linguistic sorting. Arranges strings with similar linguistic characteristics into groups (by sorts).
-   Ordinal (non-linguistic) sorting. Arranges the strings in an ordered sequence.

Sorting uses the NLS string comparison functions, such as [CompareString](/windows/win32/api/stringapiset/nf-stringapiset-comparestringw) and [**LCMapString**](/windows/desktop/api/Winnls/nf-winnls-lcmapstringa), or "wrapper" API functions, such as [lstrcmp](/windows/win32/api/winbase/nf-winbase-lstrcmpa), that internally call the NLS string comparison functions.

For details about implementing sorting in your applications, see [Handling Sorting in Your Applications](handling-sorting-in-your-applications.md).

## Related topics

<dl> <dt>

[About National Language Support](about-national-language-support.md)
</dt> <dt>

[Handling Sorting in Your Applications](handling-sorting-in-your-applications.md)
</dt> <dt>

[**CompareString**](/windows/win32/api/stringapiset/nf-stringapiset-comparestringw)
</dt> <dt>

[LCMapString](/windows/desktop/api/Winnls/nf-winnls-lcmapstringa)
</dt> </dl>

 

 

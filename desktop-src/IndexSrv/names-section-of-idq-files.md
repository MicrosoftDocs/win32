---
title: Names Section of .Idq Files
description: Names Section of .Idq Files
ms.assetid: '8d86f599-1e6f-47a8-9ee3-5b42a2400861'
---

# Names Section of .Idq Files

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The names section of the Internet Data Query (.idq) file defines nonstandard column names that can be referred to in the query. The columns refer to properties stored in the property cache, standard file system properties, or Microsoft ActiveX properties that have been created in document files with [**IPropertyStorage**](_stg_ipropertystorage), or in the Office summary and custom properties. The globally unique identifier (GUID) for Office is 0xF29F85E0,0x4FF9,0x1068,0xAB9108002B27B3D9. The following sample defines a few of the ActiveX Summary Information properties:

``` syntax
[Names]
#Property set for ActiveX document properties
DocTitle                                  = F29F85E0-4FF9-1068-AB91-08002B27B3D9 2
DocSubject( DBTYPE_WSTR|DBTYPE_BYREF )     = F29F85E0-4FF9-1068-AB91-08002B27B3D9 3
DocAuthor( DBTYPE_WSTR|DBTYPE_BYREF )      = F29F85E0-4FF9-1068-AB91-08002B27B3D9 4
DocEditTime( VT_FILETIME )                 = F29F85E0-4FF9-1068-AB91-08002B27B3D9 0xa
DocLastPrinted( VT_FILETIME )              = F29F85E0-4FF9-1068-AB91-08002B27B3D9 0xb
DocPageCount( DBTYPE_I4 )                 = F29F85E0-4FF9-1068-AB91-08002B27B3D9 0xe
DocWordCount( DBTYPE_I4 )                 = F29F85E0-4FF9-1068-AB91-08002B27B3D9 0xf
SalesRegion( DBTYPE_WSTR | DBTYPE_BYREF ) = D5CDD505-2E9C-101B-9397-08002B2CF9AE "SalesRegion"
```

Within the section, any blank line, or a line beginning with a number sign (\#) is ignored. Other lines consist of a *friendly name*, optionally followed by a *data type* in parentheses, followed by an equal sign (=), then a GUID identifying the *property set* for the column, followed by either a number or a string giving the PROPID or the *property name*, respectively. If no other data type is provided, **DBTYPE\_WSTR\|DBTYPE\_BYREF** is assumed.

The friendly name is the token in query restrictions, sort specifications, and so on. Multiple friendly names can point to the same property. For example, the friendly name *Author* might be replaced by *Auteur* if an author property is to be shown to a French audience. Friendly names cannot contain spaces or special characters such as angle brackets, equal signs, exclamation points, commas, periods, or asterisks (&gt;=&lt;!,.\*).

The GUID and PROPID/property name is the name of the property within the ActiveX property namespace. See the Microsoft Win32 API for more information on ActiveX properties. The PROPID may be specified as a decimal (base 10) or a hexadecimal (base 16) number. In the latter case, the number must be preceded by 0x. Property names must be enclosed in quotation marks. For example, *"10"* is not the same as *10*.

 

 





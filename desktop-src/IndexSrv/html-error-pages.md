---
Description: HTML Error Pages
ms.assetid: 75972bb2-e23e-4a3b-af6e-b52e260fdac2
title: HTML Error Pages
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# HTML Error Pages

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The first three classes of error (query syntax referring to .idq files only, .idq syntax, and .htx syntax) always generate an HTML error page. The page returned for each class of error is specified in the Language-Specific Registry Settings. Registry keys are under the following path:

```
HKEY_LOCAL_MACHINE\SYSTEM
   SYSTEM
      CurrentControlSet
         Control
            ContentIndex
               Language
                  <language>
```

The keys are:

<dl> <dt>

<span id="ISAPIHTXErrorFile__ISAPIIDQErrorFile__and_ISAPIRestrictionErrorFile"></span><span id="isapihtxerrorfile__isapiidqerrorfile__and_isapirestrictionerrorfile"></span><span id="ISAPIHTXERRORFILE__ISAPIIDQERRORFILE__AND_ISAPIRESTRICTIONERRORFILE"></span>**ISAPIHTXErrorFile**, **ISAPIIDQErrorFile**, and **ISAPIRestrictionErrorFile**
</dt> <dd>

Configures .htx errors, .idq (and .ida) errors, and query syntax errors.

</dd> <dt>

<span id="ISAPIDefaultErrorFile"></span><span id="isapidefaulterrorfile"></span><span id="ISAPIDEFAULTERRORFILE"></span>**ISAPIDefaultErrorFile**
</dt> <dd>

Reports other errors.

</dd> </dl>

These pages are standard, completely customizable .htx pages. The variable *CiErrorMessage* contains a localized string describing the specific error, and *CiErrorNumber* contains the error code.

 

 




---
title: Input Method manager APIs are not supported by Simplified Chinese IME
description: Input Method manager APIs are not supported by Simplified Chinese IME
ms.assetid: 829E1920-8A5C-4DBB-A844-72DA75D58B92
ms.topic: article
ms.date: 05/31/2018
---

# Input Method manager APIs are not supported by Simplified Chinese IME

## Platforms

<dl> Clients - Windows 8.1  
Windows Server 2012 R2  
</dl>

## Description

The following input method manager APIs are not supported by Simplified Chinese IMEs in Windows 8.1:

-   IFECommon interface
-   IFEDictionary interface
-   IFELanguage interface
-   IImePad interface
-   IImePadApplet interface
-   IImeSpecifyApplets interface

## Manifestations

The functions that use those APIs don’t work with Simplified Chinese IME.

## Solution

Applications must be designed so that users can complete the desired task without using the specified API.

## Resources

-   [Input Method Manager Interfaces](https://msdn.microsoft.com/library/windows/desktop/hh851805(v=vs.85).aspx)
-   [IFECommon](https://msdn.microsoft.com/library/windows/desktop/hh851760(v=vs.85).aspx)
-   [IFECommon interface](https://msdn.microsoft.com/library/windows/desktop/hh851760(v=vs.85).aspx)
-   [IFEDictionary interface](https://msdn.microsoft.com/library/windows/desktop/hh851765(v=vs.85).aspx)
-   [IFELanguage](https://msdn.microsoft.com/library/windows/desktop/hh851778(v=vs.85).aspx)
-   [IImePad](https://msdn.microsoft.com/library/windows/desktop/hh851784(v=vs.85).aspx)
-   [IImePadApplet](https://msdn.microsoft.com/library/windows/desktop/hh851785(v=vs.85).aspx)
-   [IimePlugInDictDictionaryList](https://msdn.microsoft.com/library/windows/desktop/hh851792(v=vs.85).aspx)
-   [IImeSpecifyApplets](https://msdn.microsoft.com/library/windows/desktop/hh851795(v=vs.85).aspx)

 

 





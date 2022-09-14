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

-   [Input Method Manager Interfaces](../intl/input-method-manager-interfaces.md)
-   [IFECommon](/windows/win32/api/msime/nn-msime-ifecommon)
-   [IFECommon interface](/windows/win32/api/msime/nn-msime-ifecommon)
-   [IFEDictionary interface](/windows/win32/api/msime/nn-msime-ifedictionary)
-   [IFELanguage](/windows/win32/api/msime/nn-msime-ifelanguage)
-   [IImePad](/windows/win32/api/imepad/nn-imepad-iimepad)
-   [IImePadApplet](/windows/win32/api/imepad/nn-imepad-iimepadapplet)
-   [IimePlugInDictDictionaryList](/windows/win32/api/msimeapi/nn-msimeapi-iimeplugindictdictionarylist)
-   [IImeSpecifyApplets](/windows/win32/api/imepad/nn-imepad-iimespecifyapplets)

 

 
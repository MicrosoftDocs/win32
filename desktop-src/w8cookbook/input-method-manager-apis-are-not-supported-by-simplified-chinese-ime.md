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

-   [Input Method Manager Interfaces](https://go.microsoft.com/fwlink/p/?LinkId=325304)
-   [IFECommon](https://go.microsoft.com/fwlink/p/?LinkId=325305)
-   [IFECommon interface](https://go.microsoft.com/fwlink/p/?LinkId=325305)
-   [IFEDictionary interface](https://go.microsoft.com/fwlink/p/?LinkId=325308)
-   [IFELanguage](https://go.microsoft.com/fwlink/p/?LinkId=325309)
-   [IImePad](https://go.microsoft.com/fwlink/p/?LinkId=325310)
-   [IImePadApplet](https://go.microsoft.com/fwlink/p/?LinkId=325311)
-   [IimePlugInDictDictionaryList](https://go.microsoft.com/fwlink/p/?LinkId=325312)
-   [IImeSpecifyApplets](https://go.microsoft.com/fwlink/p/?LinkId=325313)

 

 





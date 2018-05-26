---
title: Input Method manager APIs are not supported by Simplified Chinese IME
description: Input Method manager APIs are not supported by Simplified Chinese IME
ms.assetid: 829E1920-8A5C-4DBB-A844-72DA75D58B92
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

-   [Input Method Manager Interfaces](http://go.microsoft.com/fwlink/p/?LinkId=325304)
-   [IFECommon](http://go.microsoft.com/fwlink/p/?LinkId=325305)
-   [IFECommon interface](http://go.microsoft.com/fwlink/p/?LinkId=325305)
-   [IFEDictionary interface](http://go.microsoft.com/fwlink/p/?LinkId=325308)
-   [IFELanguage](http://go.microsoft.com/fwlink/p/?LinkId=325309)
-   [IImePad](http://go.microsoft.com/fwlink/p/?LinkId=325310)
-   [IImePadApplet](http://go.microsoft.com/fwlink/p/?LinkId=325311)
-   [IimePlugInDictDictionaryList](http://go.microsoft.com/fwlink/p/?LinkId=325312)
-   [IImeSpecifyApplets](http://go.microsoft.com/fwlink/p/?LinkId=325313)

 

 





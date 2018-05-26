---
Description: This section describes the IMM interfaces.
ms.assetid: 25092F1D-0B54-4E5E-AC9E-F8F3A0181482
title: Input Method Manager Interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Input Method Manager Interfaces

This section describes the IMM interfaces.



| Interface                                                            | Description                                                                                                                                    |
|----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IFECommon**](/windows/win32/Msime/nn-msime-ifecommon?branch=master)                                       | Provides IME-related services that are common for different languages.                                                                         |
| [**IFEDictionary**](/windows/win32/Msime/nn-msime-ifedictionary?branch=master)                               | Allows clients to access a Microsoft IME user dictionary.                                                                                      |
| [**IFELanguage**](/windows/win32/Msime/nn-msime-ifelanguage?branch=master)                                   | Provides language processing services using the Microsoft IME.                                                                                 |
| [**IImePad**](/windows/win32/Imepad/nn-imepad-iimepad?branch=master)                                           | Inserts text into apps from IMEPadApplets that implement the [**IImePadApplet**](/windows/win32/Imepad/nn-imepad-iimepadapplet?branch=master) interface.                                 |
| [**IImePadApplet**](/windows/win32/Imepad/nn-imepad-iimepadapplet?branch=master)                               | Inputs strings into apps through the [**IImePad**](/windows/win32/Imepad/nn-imepad-iimepad?branch=master) interface.                                                                     |
| [**IImePlugInDictDictionaryList**](/windows/win32/Msimeapi/nn-msimeapi-iimeplugindictdictionarylist?branch=master) | Provides access to the list of IME plug-in dictionaries.                                                                                       |
| [**IImeSpecifyApplets**](/windows/win32/Imepad/nn-imepad-iimespecifyapplets?branch=master)                     | Specifies methods called from the [**IImePad**](/windows/win32/Imepad/nn-imepad-iimepad?branch=master) interface object to emulate the [**IImePadApplet**](/windows/win32/Imepad/nn-imepad-iimepadapplet?branch=master) interface. |



 

 

 




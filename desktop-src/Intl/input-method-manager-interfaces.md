---
description: This section describes the IMM interfaces.
ms.assetid: 25092F1D-0B54-4E5E-AC9E-F8F3A0181482
title: Input Method Manager Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Input Method Manager Interfaces

This section describes the IMM interfaces.



| Interface                                                            | Description                                                                                                                                    |
|----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IFECommon**](/windows/desktop/api/Msime/nn-msime-ifecommon)                                       | Provides IME-related services that are common for different languages.                                                                         |
| [**IFEDictionary**](/windows/desktop/api/Msime/nn-msime-ifedictionary)                               | Allows clients to access a Microsoft IME user dictionary.                                                                                      |
| [**IFELanguage**](/windows/desktop/api/Msime/nn-msime-ifelanguage)                                   | Provides language processing services using the Microsoft IME.                                                                                 |
| [**IImePad**](/windows/desktop/api/Imepad/nn-imepad-iimepad)                                           | Inserts text into apps from IMEPadApplets that implement the [**IImePadApplet**](/windows/desktop/api/Imepad/nn-imepad-iimepadapplet) interface.                                 |
| [**IImePadApplet**](/windows/desktop/api/Imepad/nn-imepad-iimepadapplet)                               | Inputs strings into apps through the [**IImePad**](/windows/desktop/api/Imepad/nn-imepad-iimepad) interface.                                                                     |
| [**IImePlugInDictDictionaryList**](/windows/desktop/api/Msimeapi/nn-msimeapi-iimeplugindictdictionarylist) | Provides access to the list of IME plug-in dictionaries.                                                                                       |
| [**IImeSpecifyApplets**](/windows/desktop/api/Imepad/nn-imepad-iimespecifyapplets)                     | Specifies methods called from the [**IImePad**](/windows/desktop/api/Imepad/nn-imepad-iimepad) interface object to emulate the [**IImePadApplet**](/windows/desktop/api/Imepad/nn-imepad-iimepadapplet) interface. |



 

 

 




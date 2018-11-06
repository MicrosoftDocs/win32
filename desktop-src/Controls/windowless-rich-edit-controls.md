---
title: Windowless Rich Edit Controls
description: This section contains information about the programming elements used with windowless rich edit controls.
ms.assetid: 'vs|controls|~\controls\richedit\windowlessricheditcontrols.htm'
ms.topic: article
ms.date: 05/31/2018
---

# Windowless Rich Edit Controls

This section contains information about the programming elements used with windowless rich edit controls. The Component Object Model (COM) defines a set of interfaces to support windowless objects. Windowless objects can enter the in-place active state without having their own window, but rather use the window of their container. Consequently, a windowless object uses fewer system resources and gives better performance through faster activation and deactivation. In addition, windowless objects can be nonrectangular and transparent.

### Overviews



| Topic                                                                          | Contents                                                                                                                                                                                                     |
|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [About Windowless Rich Edit Controls](about-windowless-rich-edit-controls.md) | A windowless rich edit control, also known as a text services object, is an object that provides the functionality of a [rich edit control](rich-edit-controls.md) without providing the window.<br/> |



 

### Functions



| Topic                                            | Contents                                                                                                                                                                                                                                                             |
|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateTextServices**](/windows/desktop/api/Textserv/nf-textserv-createtextservices) | The [**CreateTextServices**](/windows/desktop/api/Textserv/nf-textserv-createtextservices) function creates an instance of a text services object. The text services object supports a variety of interfaces, including [**ITextServices**](/windows/desktop/api/Textserv/nl-textserv-itextservices) and the Text Object Model (TOM).<br/> |



 

### Interfaces



| Topic                                  | Contents                                                                                                                |
|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [**ITextHost**](/windows/desktop/api/Textserv/nl-textserv-itexthost)         | The [**ITextHost**](/windows/desktop/api/Textserv/nl-textserv-itexthost) interface is used by a text services object to obtain text host services.<br/> |
| [**ITextServices**](/windows/desktop/api/Textserv/nl-textserv-itextservices) | Extends the TOM to provide extra functionality for windowless operation.<br/>                                     |



 

 

 






---
title: Text Object Model
description: This section contains information about the programming elements used with the Text Object Model (TOM).
ms.assetid: 'vs|controls|~\controls\richedit\textobjectmodel.htm'
ms.topic: article
ms.date: 05/31/2018
---

# Text Object Model

This section contains information about the programming elements used with the Text Object Model (TOM).

The TOM defines a substantial set of text manipulation interfaces. Text solutions such as Microsoft Word and rich edit controls support the TOM feature set. TOM was greatly influenced by WordBasic (the programming language used for Word) and it is easy to use from Microsoft Visual Basic for Applications (VBA). This compatibility has several advantages:

-   Code can migrate fairly easily from one solution to another.
-   One language can be used to share text information between different text engines.
-   It reduces the need for documentation and code compared to the separate low-level Component Object Model (COM) and VBA interfaces.

However, it can be less efficient for C/C++ purposes than the use of more general lower level COM interfaces.

TOM is a straightforward set of interfaces to implement for its primary text solutions, Word and rich edit controls. However, for applications that place minor emphasis on text, it is better to provide TOM interfaces by transferring the text to an edit control that supports TOM. Since rich edit controls ship with Microsoft operating systems, they are the standard means of obtaining TOM functionality.

### Overviews



| Topic                                                          | Contents                                                                                                                                                                                                         |
|----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [About Text Object Model](about-text-object-model.md)         | The top-level Text Object Model (TOM) object is defined by the [**ITextDocument**](/windows/desktop/api/Tom/nn-tom-itextdocument) interface, which has methods for creating and retrieving objects lower in the object hierarchy.<br/> |
| [Using The Text Object Model](using-the-text-object-model.md) | The code samples in this document show various aspects of using the Text Object Model (TOM).<br/>                                                                                                          |



 

### Interfaces




| Topic | Contents | 
|-------|----------|
| <a href="/windows/desktop/api/Tom/nn-tom-itextdocument"><strong>ITextDocument</strong></a> | The <a href="/windows/desktop/api/Tom/nn-tom-itextdocument"><strong>ITextDocument</strong></a> interface is the TOM top-level interface, which retrieves the active selection and range objects for any story in the document whether active or not. It enables the application to:<ul><li>Open and save documents.</li><li>Control undo behavior and screen updating.</li><li>Find a range from a screen position.</li><li>Get an <a href="/windows/desktop/api/Tom/nn-tom-itextstoryranges"><strong>ITextStoryRanges</strong></a> story enumerator.</li></ul><br /><strong>When to Implement</strong><br /> Applications typically do not implement the <a href="/windows/desktop/api/Tom/nn-tom-itextdocument"><strong>ITextDocument</strong></a> interface. Microsoft text solutions, such as rich edit controls, implement <strong>ITextDocument</strong> as part of their TOM implementation. <br /><strong>When to Use</strong><br /> Applications can retrieve an <a href="/windows/desktop/api/Tom/nn-tom-itextdocument"><strong>ITextDocument</strong></a> pointer from a rich edit control. To do this, send an <a href="em-getoleinterface.md"><strong>EM_GETOLEINTERFACE</strong></a> message to retrieve an <a href="/windows/desktop/api/Richole/nn-richole-iricheditole"><strong>IRichEditOle</strong></a> object from a rich edit control. Then, call the object's <a href="/windows/desktop/api/unknwn/nf-unknwn-iunknown-queryinterface(q)"><strong>IUnknown::QueryInterface</strong></a> method to retrieve an <strong>ITextDocument</strong> pointer.<br /> | 
| <a href="/windows/desktop/api/Tom/nn-tom-itextfont"><strong>ITextFont</strong></a> | TOM rich text-range attributes are accessed through a pair of dual interfaces, <a href="/windows/desktop/api/Tom/nn-tom-itextfont"><strong>ITextFont</strong></a> and <a href="/windows/desktop/api/Tom/nn-tom-itextpara"><strong>ITextPara</strong></a>.<br /> | 
| <a href="/windows/desktop/api/Tom/nn-tom-itextpara"><strong>ITextPara</strong></a> | TOM rich text-range attributes are accessed through a pair of dual interfaces, <a href="/windows/desktop/api/Tom/nn-tom-itextfont"><strong>ITextFont</strong></a> and <a href="/windows/desktop/api/Tom/nn-tom-itextpara"><strong>ITextPara</strong></a>.<br /> | 
| <a href="/windows/desktop/api/Tom/nn-tom-itextrange"><strong>ITextRange</strong></a> | The <a href="/windows/desktop/api/Tom/nn-tom-itextrange"><strong>ITextRange</strong></a> objects are powerful editing and data-binding tools that allow a program to select text in a story and then examine or change that text.<br /> | 
| <a href="/windows/desktop/api/Tom/nn-tom-itextselection"><strong>ITextSelection</strong></a> | A text selection is a text range with selection highlighting.<br /> | 
| <a href="/windows/desktop/api/Tom/nn-tom-itextstoryranges"><strong>ITextStoryRanges</strong></a> | The purpose of the <a href="/windows/desktop/api/Tom/nn-tom-itextstoryranges"><strong>ITextStoryRanges</strong></a> interface is to enumerate the stories in an <a href="/windows/desktop/api/Tom/nn-tom-itextdocument"><strong>ITextDocument</strong></a>.<br /> | 




 

 


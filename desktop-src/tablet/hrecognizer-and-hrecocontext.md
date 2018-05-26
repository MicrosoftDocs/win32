---
Description: You reference an ink recognizer with an HRECOGNIZER handle and a recognizer context as an HRECOCONTEXT handle.A recognizer dynamic-link library (DLL) can implement recognizers for more than one language.
ms.assetid: 23002d02-cf8f-489b-a50f-4a18ac091825
title: HRECOGNIZER and HRECOCONTEXT
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HRECOGNIZER and HRECOCONTEXT

You reference an ink recognizer with an [HRECOGNIZER](hrecognizer-handle.md) handle and a recognizer context as an [HRECOCONTEXT](hrecocontext-handle.md) handle.

A recognizer dynamic-link library (DLL) can implement recognizers for more than one language. If so, each language is selected by a CLSID that is passed in when creating the [**IInkRecognizer**](/windows/win32/msinkaut/nn-msinkaut-iinkrecognizer?branch=master) object in the application. In addition, a recognizer DLL can create multiple recognizer handles when it is loaded, one or more for each language recognized.

A recognizer context is created to represent the event of recognizing a specific piece of ink. When the context is created, the associated recognizer objects handle is passed to the [**CreateContext**](/windows/win32/recapis/nf-recapis-createcontext?branch=master) function. This associates the language with the recognizer context.

A recognizer context may represent the recognition of all the ink in the body of an email, the ink of a single field within an application, or a single line of text written in the Tablet PC Input Panel. The volume of ink in a single recognizer context may vary from a single stroke to a whole page or more.

The recognizer context is defined by the settings of:

-   The recognition guide.
-   Any factoids.
-   Any flags.
-   The text context.
-   Any word list.
-   The character Autocomplete mode.

The handle for the recognizer context is passed to all functions that use these settings. Changing a setting changes the recognizer context.

The application may use several contexts to recognize ink from different parts of the screen. An individual context can recognize multiple lines of text. However, an individual context cannot process two paragraphs written side by side, such as multiple columns in a newspaper article.

To recognize new ink, create a new context. As an alternative, use the [**CloneContext**](/windows/win32/recapis/nf-recapis-clonecontext?branch=master) function to make a copy of a context that does not have the ink and results, or the [**ResetContext**](/windows/win32/recapis/nf-recapis-resetcontext?branch=master) function to clear a context of its ink and results. With these approaches, an ink application can reuse a context.

## Related topics

<dl> <dt>

[**SetGuide Function**](/windows/win32/recapis/nf-recapis-setguide?branch=master)
</dt> <dt>

[**GetGuide Function**](/windows/win32/recapis/nf-recapis-getguide?branch=master)
</dt> <dt>

[**SetFactoid Function**](/windows/win32/recapis/nf-recapis-setfactoid?branch=master)
</dt> <dt>

[**SetFlags Function**](/windows/win32/recapis/nf-recapis-setflags?branch=master)
</dt> <dt>

[**SetEnabledUnicodeRanges Function**](/windows/win32/recapis/nf-recapis-setenabledunicoderanges?branch=master)
</dt> <dt>

[**GetEnabledUnicodeRanges Function**](/windows/win32/recapis/nf-recapis-getenabledunicoderanges?branch=master)
</dt> <dt>

[**SetCACMode Function**](/windows/win32/recapis/nf-recapis-setcacmode?branch=master)
</dt> <dt>

[**SetTextContext Function**](/windows/win32/recapis/nf-recapis-settextcontext?branch=master)
</dt> <dt>

[**SetWordList Function**](/windows/win32/recapis/nf-recapis-setwordlist?branch=master)
</dt> </dl>

 

 




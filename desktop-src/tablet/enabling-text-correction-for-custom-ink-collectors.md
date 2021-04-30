---
description: Microsoft Tablet PC Input Panel is a powerful tool for entering handwritten text with a pen and correcting text without the use of a keyboard.
ms.assetid: c45ac1b5-7713-4bcb-a130-4692cff99aa2
title: Enabling Text Correction for Custom Ink Collectors
ms.topic: article
ms.date: 05/31/2018
---

# Enabling Text Correction for Custom Ink Collectors

Microsoft Tablet PC Input Panel is a powerful tool for entering handwritten text with a pen and correcting text without the use of a keyboard. When using Input Panel, a user enters text by handwriting onto Input Panel's inking surfaces, which causes Input Panel to recognize the user's handwriting as text. Once the text has been recognized, the user taps Insert on Input Panel to insert the text into an application or document. Prior to inserting the text, a user has access to a set of correction tools in Input Panel. These include the selection of an alternative recognition result, the ability to rewrite a single character, or even to scratch-out the entire word and rewrite. These correction tools enable a user to correct both recognition errors and human errors.

Once the text entered using Input Panel is in the document, users have access to the same correction functionality that is available prior to insertion in Windows [Text Services Framework](/windows/desktop/TSF/text-services-framework)-based and Text Services-enabled applications. Starting in Microsoft Windows XP Service Pack 2 Tablet PC Edition all Rich Edit applications are Text Services-enabled by default, and starting in Windows Vista, HTML applications are Text Services-enabled by default. In-document correction is only available in Text Service based and enabled applications; this is because Input Panel is dependent on Text Service's capability to store associated text properties, including ink objects and recognition alternates, in order to provide in-document correction.

![tablet pc input panel with text correction](images/a0dced5e-16de-410b-965f-5d97d297cee5.jpg)

There are, however, numerous scenarios, including correcting speech recognition or correcting typed text on the go, that do not start with text entry using Input Panel but in which in-document correction can be extremely useful for Tablet PC users. A prime example is in applications that provide custom inking surfaces for entering text using a pen. Custom inking surfaces are a great way for applications to provide uniquely tailored functionality specific to the text entry tasks of each application. Additionally, custom inking surfaces provide a fully integrated Tablet PC user experience, which makes it clear the pen is a first class input device in applications that contain them. However, applications that provide custom inking surfaces may not allow or may not be able to provide the same level of correction support that is available from Input Panel in-document correction.

![custom ink collector](images/b6797b12-dda6-44c4-87f4-570fe0c23f3a.jpg)

Text Services based or enabled applications in which in-document correction is useful for correction of text not entered using Input Panel are able to use Input Panel's [**IHandWrittenTextInsertion**](/windows/desktop/api/peninputpanel/nn-peninputpanel-ihandwrittentextinsertion) API ([Microsoft.TextInput.HandwrittenTextInsertion](/previous-versions/ms573516(v=vs.100)) class in managed code)to enable in-document correction for text entered by other means. In this way, applications can cheaply add powerful correction support to their custom inking surfaces or other text entry scenarios, and round out their Tablet PC text entry story. The Input Panel IHandWrittenTextInsertion API is included as part of the Windows Vista operating system and as part of the Tablet Platform SDK version 1.9 or newer. Both a .NET and COM based version of the API are included. Enabling in-document correction for text not entered using Input Panel is supported on Windows Vista and newer. In-document correction is only available for Latin languages and is unable to display any character outside the Latin character set.

## How to Use the HandwrittenTextInsertion API in an Application

The required changes to an application in order to integrate Input Panel in-document correction for text not entered using Input Panel and using the [**IHandWrittenTextInsertion**](/windows/desktop/api/peninputpanel/nn-peninputpanel-ihandwrittentextinsertion) API are straightforward. All of the application's custom text entry code remains unchanged except for the last step. At the point at which text entered using a custom inking surface, speech recognition, or other means is to be displayed in a text services enabled text field, the application sends the text to the **IHandWrittenTextInsertion** interface instead of sending it directly to the text field. The Input Panel programmability component then handles inserting the text into both the text field and the Text Services backing-store. When adding the text to the Text Services backing-store, the Input Panel programmability component handles setting the text properties that are required by Input Panel for in-document correction to be enabled for that text.

The following section walks through this process in detail for a C++ application using the COM version of the [**IHandWrittenTextInsertion**](/windows/desktop/api/peninputpanel/nn-peninputpanel-ihandwrittentextinsertion) API. There are notes anywhere the steps for using the .NET Framework version of the API in C\# differ for the using COM version in C++. The managed **HandwrittenTextInsertion** API includes a single COM interface, **IHandwrittenTextInsertion**. The definition for this interface is located in PenInputPanel.h and PenInputPanel\_i.c.

First, the application should use the [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) function to produce an instance of [**IHandWrittenTextInsertion**](/windows/desktop/api/peninputpanel/nn-peninputpanel-ihandwrittentextinsertion) with class id **CLSID\_HandwrittenTextInsertion**. Note that the creation of a **CLSID\_HandwrittenTextInsertion** object will succeed only after a window is created and given focus, because until then the Text Services backing-store is not activated. Additionally, if tiptsf.dll is not present on the system, the **CoCreateInstance** function fails and returns **REGDB\_E\_CLASSNOTREG**, indicating that Input Panel in-document correction is not supported on the system. At this point the application should proceed without trying to enable Input Panel in-document correction. The instance of **HandwrittenTextInsertion** must be accessible from the application's code that handles inserting text into a text field.

> [!Note]  
> When working with the .NET Framework version of the API, the application should add a using statement to allow access to the [Microsoft.Ink.TextInput](/previous-versions/dotnet/netframework-3.5/ms581554(v=vs.90)) namespace and then create the object directly.

 

Second, the application's code that is responsible for inserting text into a text field must be altered so that it no longer inserts text into a text field directly, but calls one or the other of [**IHandwrittenTextInsertion**](/windows/desktop/api/peninputpanel/nn-peninputpanel-ihandwrittentextinsertion)'s two insertion methods instead. Whether the applications should choose to call [**InsertRecognitionResultsArray**](/windows/desktop/api/peninputpanel/nf-peninputpanel-ihandwrittentextinsertion-insertrecognitionresultsarray) or [**InsertRecognitionResults**](/windows/desktop/api/peninputpanel/nf-peninputpanel-ihandwrittentextinsertion-insertinkrecognitionresult) depends on whether the application has the recognition alternates for the text stored as an array or as an [**IInkRecognitionResult**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkrecognitionresult) object.

> [!Note]  
> When working in managed code, the corresponding recognition object consumed by InsertRecognitionResultsArray is [RecognitionResult](/previous-versions/ms552537(v=vs.100)). Both methods consume the following three parameters:

 

-   *alternates* Is a two dimensional collection of strings, stored either as an array of arrays or as an [**IInkRecognitionResult**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkrecognitionresult) (or [RecognitionResult](/previous-versions/ms552537(v=vs.100))) object. If the alternates are stored as an array of arrays, then it should be passed as a safe array pointer. Each entry in the top level array is a list of alternates for a single word in the insertion. The entry at position zero in the sub-arrays of alternates is the text that is inserted into the text field. The additional alternates (indices 1 through n in each sub-array) are stored in the Text Services backing-store and offered to the user as choices as part of in-document correction. If alternates are not included, then the user sees 'No suggestion' in place of the list of alternates. If an insertion contains multiple words with spaces between them, then each space must be included as an entry in the top level array.
-   *language* The Input Language [LCID](/previous-versions/ms221397(v=vs.71)) that corresponds to the text contained in the *alternates* parameter. In the case in which the contents of *alternates* was generated by a handwriting or speech recognizer, this is also the [**Languages**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizer-get_languages) property associated with the recognizer used.
-   *fLatticeContainsAutoSpacingInformation* A flag indicating whether the text contained in the *alternates* parameter was generated by a recognizer with auto-spacing enabled. If auto-spacing was enabled, then the flag should be set to **TRUE**. If auto-spacing was disabled, then the flag should be set to **FALSE**. In the case in which the contents of *alternates* was generated by a recognizer that does not support auto-spacing, or was not generated by a recognizer at all, then the flag should be set to **FALSE**.

Input Panel's programmability model is able to insert the text in the document or application from the position of the system caret.

Both methods return **S\_OK** if the insertion succeeds. They return **E\_NOINTERFACE** if the application is not Text Services based or enabled, and **E\_INVALIDARG** if *alternates* is improperly formatted or inaccessible. They may also return **E\_OUTOFMEMORY** if there is not enough memory available on the system, or **E\_FAIL** after a catastrophic failure such as the Text Services Framework not being enabled.

### Conclusion

Enabling Input Panel in-document correction for text not entered using Input Panel is a cheap and easy way for a Text Services based or enabled application to supplement a custom inking or input method with powerful pen-based correction functionality. On Windows Vista, all Rich Edit and Trident applications are Text Services enabled. While integrated inking surfaces are a great option for adding a custom Tablet PC user experience to an application, they only support half of text entry if they do not include correction capabilities. In-document correction provides users with the other half of the story by adding the ability to swap a selection for a recognition alternate, or to rewrite part or all of the selection.

## Related topics

<dl> <dt>

[Programming the Text Input Panel](programming-the-text-input-panel.md)
</dt> </dl>

 

 

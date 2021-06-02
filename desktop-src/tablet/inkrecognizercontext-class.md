---
description: Enables the ability to perform ink recognition, retrieve the recognition result, and retrieve alternates. The InkRecognizerContext enables the various recognizer that are installed on a system to use ink recognition to process input appropriately.
ms.assetid: 2b39fd32-831d-4606-8600-b52aaa7ed882
title: InkRecognizerContext class (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- InkRecognizerContext
- InkRecognizerContext.IInkRecognizerContext
api_type: 
- COM
api_location: 
- InkObj.dll
- InkObj.dll.dll
---

# InkRecognizerContext class

Enables the ability to perform ink recognition, retrieve the recognition result, and retrieve alternates. The **InkRecognizerContext** enables the various recognizer that are installed on a system to use ink recognition to process input appropriately.

**InkRecognizerContext** has these types of members:

-   [Events](#events)
-   [Interfaces](#interfaces)
-   [Methods](#methods)
-   [Properties](#properties)

### Events

The **InkRecognizerContext** class has these events.



| Event                                                                               | Description                                                                                                                                                                                            |
|:------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Recognition**](inkrecognizercontext-recognition.md)                             | Occurs when the InkRecognizerContext has generated results from the BackgroundRecognize method.<br/>                                                                                             |
| [**RecognitionWithAlternates**](inkrecognizercontext-recognitionwithalternates.md) | Occurs when the **InkRecognizerContext** has generated results after calling the [**BackgroundRecognizeWithAlternates**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-backgroundrecognizewithalternates) method<br/> |



 

### Interfaces

The **InkRecognizerContext** class defines these interfaces.



| Interface                 | Description                                                                    |
|:--------------------------|:-------------------------------------------------------------------------------|
| **IInkRecognizerContext** | This object implements the **IInkRecognizerContext** COM interface.<br/> |



 

### Methods

The **InkRecognizerContext** class has these methods.



| Method                                                                                              | Description                                                                                                                                                                                                                                            |
|:----------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BackgroundRecognize**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-backgroundrecognize)                             | Specifies that the recognizer should recognize the associated strokes and fire a [**Recognition**](inkrecognizercontext-recognition.md) event when recognition is complete.<br/>                                                                |
| [**BackgroundRecognizeWithAlternates**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-backgroundrecognizewithalternates) | Specifies that the recognizer should recognize the associated strokes and fire a [**RecognitionWithAlternates**](inkrecognizercontext-recognitionwithalternates.md) event when recognition is complete.<br/>                                    |
| [**Clone**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-clone)                                                                      | Creates a duplicate **InkRecognizerContext**.<br/>                                                                                                                                                                                               |
| [**EndInkInput**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-endinkinput)                                             | Ends ink input to the **InkRecognizerContext**.<br/>                                                                                                                                                                                             |
| [**IsStringSupported**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-isstringsupported)                                 | Indicates whether the system dictionary, user dictionary, or [**word list**](inkwordlist-class.md) contain a specified string.<br/>                                                                                                             |
| [**Recognize**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-recognize)                                                 | Performs recognition on an [**InkStrokes**](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) collection and returns recognition results.<br/>                                                                                                                          |
| [**StopBackgroundRecognition**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-stopbackgroundrecognition)                 | Ends background recognition that was started with a call to [**BackgroundRecognize**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-backgroundrecognize) or [**BackgroundRecognizeWithAlternates**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-backgroundrecognizewithalternates).<br/> |



 

### Properties

The **InkRecognizerContext** class has these properties.



| Property                                                                                   | Access type           | Description                                                                                                                                                |
|:-------------------------------------------------------------------------------------------|:----------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CharacterAutoCompletion**](/windows/win32/api/msinkaut/nf-msinkaut-iinkrecognizercontext-get_characterautocompletionmode)<br/> | Read/write<br/> | Gets or sets the character Autocomplete mode, which determines when characters or words are recognized.<br/>                                         |
| [**Factoid**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-get_factoid)<br/>                                 | Read/write<br/> | Gets or sets the string name of the factoid used by the **InkRecognizerContext** object.<br/>                                                        |
| [**Guide**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-get_guide)<br/>                                     | Read/write<br/> | Gets or sets the [**InkRecognizerGuide**](inkrecognizerguide-class.md) to use for ink input.<br/>                                                   |
| [**PrefixText**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-get_prefixtext)<br/>                           | Read/write<br/> | Gets or sets the characters that come before the [**InkStrokes**](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) collection in the **InkRecognizerContext** object.<br/> |
| [**RecognitionFlags**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-get_recognitionflags)<br/>               | Read/write<br/> | Gets or sets the flags that specify how the recognizer interprets the ink and determines the result string.<br/>                                     |
| [**Recognizer**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-get_recognizer)<br/>                           | Read/write<br/> | Gets or sets the [**IInkRecognizer**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkrecognizer) object used by the **InkRecognizerContext** object.<br/>                                   |
| [**Strokes**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-get_strokes)<br/>                                 | Read/write<br/> | Gets or sets the [**InkStrokes**](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) collection associated with the **InkRecognizerContext** object.<br/>                    |
| [**SuffixText**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-get_suffixtext)<br/>                           | Read/write<br/> | Gets or sets the characters that come after the [**InkStrokes**](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) collection in the **InkRecognizerContext** object.<br/>  |
| [**WordList**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-get_wordlist)<br/>                               | Read/write<br/> | Gets or sets the [**InkWordList**](inkwordlist-class.md) object that is used to improve the recognition results.<br/>                               |



 

## Remarks

This object can be instantiated by calling the [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) method in C++.

There are two types of recognition: background (asynchronous) or foreground (synchronous). Background recognition is started by a call to the [**BackgroundRecognize**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-backgroundrecognize) or [**BackgroundRecognizeWithAlternates**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-backgroundrecognizewithalternates) methods, occurs on a background thread, and reports results to the application through an event mechanism. Foreground recognition does not return until all recognition is completed, thus making recognition results available to the calling thread without listening for the recognition event.

Ink is processed continuously in the background. If an [**IInkStrokeDisp**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) is added to the [InkStrokes](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) collection to which the **InkRecognizerContext** refers, then the **IInkStrokeDisp** is then recognized immediately. See remarks in the [**EndInkInput**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-endinkinput) method topic for more details.

All recognition occurs through a recognizer context. The context defines the settings for a single recognition session. It receives the ink that must be recognized and defines the constraints on the ink input and on the recognition output. The constraints that can be set on the context include the language, the dictionary, and grammar that is being used.

> [!Note]  
> Setting properties other than the [**Strokes**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-get_strokes) or [**CharacterAutoCompletion**](/windows/win32/api/msinkaut/nf-msinkaut-iinkrecognizercontext-get_characterautocompletionmode) properties succeeds only if the [InkStrokes](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) collection is **NULL**. You must set the other properties before you attach the InkStrokes collection to the **InkRecognizerContext**, or you must set the InkStrokes collection to **NULL** and then set the other properties. If you set the InkStrokes collection to **NULL** and then set the other properties, you may have to reattach the InkStrokes collection. This is because the recognition starts right after you assign the InkStrokes to the **InkRecognizerContext**. When a call is made to [**Recognize Method \[InkRecognizeContext Class\]**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-recognize) or [**BackgroundRecognize**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-backgroundrecognize), call results might be available already.

 

To improve your application's performance, dispose of your **InkRecognizerContext** object when it is no longer needed.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl>                               |



## See also

<dl> <dt>

[**IInkRecognizer Interface**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkrecognizer)
</dt> <dt>

[InkStrokes Collection](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85))
</dt> </dl>

 


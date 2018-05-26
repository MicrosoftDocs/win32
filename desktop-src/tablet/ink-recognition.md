---
Description: Not all applications require the use of recognition, but because most applications were designed with text as their primary data type, the ability to convert ink into text is very valuable.
ms.assetid: 70d25839-6ddd-40db-8891-92da074d17b0
title: Ink Recognition
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Ink Recognition

Not all applications require the use of recognition, but because most applications were designed with text as their primary data type, the ability to convert ink into text is very valuable. You can use the recognition features of the Tablet PC platform API to query for information about the recognition engines that are available, such as what languages they recognize. You can then send a [**Strokes**](/windows/win32/msinkaut/?branch=master) collection from an [**Ink**](/windows/win32/msinkaut/?branch=master) object to a recognition engine and have it return a [**RecognitionResult**](/windows/win32/msinkaut/nn-msinkaut-iinkrecognitionresult?branch=master) object.

## RecognizerContext Object

A [**RecognizerContext**](/windows/win32/msinkaut/?branch=master) object is the instantiation of a given recognizer. The **RecognizerContext** object enables you to recognize a given collection of strokes synchronously or asynchronously. When recognizing asynchronously, the **RecognizerContext** object returns the [**RecognitionResult**](/windows/win32/msinkaut/nn-msinkaut-iinkrecognitionresult?branch=master) object in an event callback to the application.

## Recognizers and Recognizer Objects

A single Tablet PC may have one or more recognizers available. You can query the recognizer's collection to determine which recognizer to use. A recognizer provides specific information about its capabilities such as the language it can recognize and the manufacturer.

To determine whether at least one recognizer is installed, instantiate an [**InkRecognizerContext**](/windows/win32/msinkaut/?branch=master) object as shown in the following C++ and C\# code examples. If a recognizer is not present, this call to [**CoCreateInstance**](https://msdn.microsoft.com/library/windows/desktop/ms686615) fails.


```C++
CComPtr<IInkRecognizerContext> g_pIInkRecoContext;
hr = CoCreateInstance(CLSID_InkRecognizerContext, 
      NULL, CLSCTX_INPROC_SERVER,
      IID_IInkRecognizerContext, 
(void **) &amp;g_pIInkRecoContext);
if (FAILED(hr)) 
{
      ::MessageBox(NULL, TEXT("No recognizers installed.\nExiting."), 
      gc_szAppName, MB_ICONERROR);
      return -1;
}
```




```CSharp
try
{
  Recognizers recos = new Recognizers();//Check for recognizer.
  Recognizer defReco = recos.GetDefaultRecognizer();
  recoContext = defReco.CreateRecognizerContext();
}
catch
{
  MessageBox.Show("No recognizers installed.");
}
```



## RecognitionResult and RecognitionAlternate Objects

The results of the recognition are returned in a [**RecognitionResult**](/windows/win32/msinkaut/nn-msinkaut-iinkrecognitionresult?branch=master) object. The results contain a best result string in the [TopString](frlrfMicrosoftInkRecognitionResultClassTopStringTopic) property, as well as a collection of alternative results in a [**RecognitionAlternates**](/windows/win32/msinkaut/nn-msinkaut-iinkrecognitionalternates?branch=master) collection. The **RecognitionResult** object can be persisted with the original [**Strokes**](/windows/win32/msinkaut/?branch=master) collection from which it was generated.

## RecognizerGuide Structure

The recognizer guide can consist of rows and columns, and gives the recognizer a better context in which to perform recognition. For example, you can draw horizontal lines on a user's screen, almost like a ruled piece of paper, that show where handwriting should occur (this type of guide would consist only of rows, and no columns). If a user writes on the lines, instead of some arbitrary space, recognition accuracy improves.

The following illustration shows a [**RecognizerGuide**](/windows/win32/msinkaut/?branch=master) structure with two lines for input.

![illustration showing two-line recognizer guide](images/9791100b-8279-4dd0-823f-0a38a0308a74.jpg)

The following illustration shows a [**RecognizerGuide**](/windows/win32/msinkaut/?branch=master) structure with four columns and three rows.

![illustration showing three-by-four recognizer guide](images/d1bbf2d3-9653-49d7-bf48-c1b26645074c.jpg)

For more information about using the [**RecognizerGuide**](/windows/win32/msinkaut/?branch=master) structure, see the **RecognizerGuide** reference topic.

 

 




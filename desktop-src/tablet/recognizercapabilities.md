---
description: Specifies the attributes of an IInkAnalysisRecognizer.
ms.assetid: 'e9577d83-0212-4f2f-88d7-e9153ec9fae5'
title: RecognizerCapabilities enumeration (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- InkAnalysisRecognizerCapabilities
api_type: 
- HeaderDef
api_location: 
- IACom.h
---

# RecognizerCapabilities enumeration

Specifies the attributes of an [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md).

## Syntax


```C++
typedef enum RecognizerCapabilities { 
  RC_None                            = 0,
  RC_DoNotCare                       = 0x1,
  RC_Object                          = 0x2,
  RC_FreeInput                       = 0x4,
  RC_LinedInput                      = 0x8,
  RC_BoxedInput                      = 0x10,
  RC_CharacterAutoCompletionInput    = 0x20,
  RC_RightAndDown                    = 0x40,
  RC_LeftAndDown                     = 0x80,
  RC_DownAndLeft                     = 0x100,
  RC_DownAndRight                    = 0x200,
  RC_ArbitraryAngle                  = 0x400,
  RC_Lattice                         = 0x800,
  RC_AdviseInkChange                 = 0x1000,
  RC_StrokeReorder                   = 0x2000,
  RC_Personalizable                  = 0x4000,
  RC_PrefersArbitraryAngle           = 0x8000,
  RC_PrefersParagraphBreaking        = 0x10000,
  RC_PrefersSegmentationRecognition  = 0x20000
} InkAnalysisRecognizerCapabilities;
```



## Constants

<dl> <dt>

<span id="RC_None"></span><span id="rc_none"></span><span id="RC_NONE"></span>**RC\_None**
</dt> <dd>

No capabilities specified.

</dd> <dt>

<span id="RC_DoNotCare"></span><span id="rc_donotcare"></span><span id="RC_DONOTCARE"></span>**RC\_DoNotCare**
</dt> <dd>

Ignores all other flags that are set.

</dd> <dt>

<span id="RC_Object"></span><span id="rc_object"></span><span id="RC_OBJECT"></span>**RC\_Object**
</dt> <dd>

Supports object recognition; otherwise, recognizes only text.

</dd> <dt>

<span id="RC_FreeInput"></span><span id="rc_freeinput"></span><span id="RC_FREEINPUT"></span>**RC\_FreeInput**
</dt> <dd>

Supports free input, where ink is entered without the use of a recognition guide, such as a line or a box.

</dd> <dt>

<span id="RC_LinedInput"></span><span id="rc_linedinput"></span><span id="RC_LINEDINPUT"></span>**RC\_LinedInput**
</dt> <dd>

Supports lined input, which is similar to writing on lined paper.

</dd> <dt>

<span id="RC_BoxedInput"></span><span id="rc_boxedinput"></span><span id="RC_BOXEDINPUT"></span>**RC\_BoxedInput**
</dt> <dd>

Supports boxed input, where each character or word is entered in a box.

</dd> <dt>

<span id="RC_CharacterAutoCompletionInput"></span><span id="rc_characterautocompletioninput"></span><span id="RC_CHARACTERAUTOCOMPLETIONINPUT"></span>**RC\_CharacterAutoCompletionInput**
</dt> <dd>

Supports character Autocomplete. Recognizers that support character Autocomplete require boxed input.

</dd> <dt>

<span id="RC_RightAndDown"></span><span id="rc_rightanddown"></span><span id="RC_RIGHTANDDOWN"></span>**RC\_RightAndDown**
</dt> <dd>

Supports handwriting input in right and down order, such as in western languages and some East Asian languages.

</dd> <dt>

<span id="RC_LeftAndDown"></span><span id="rc_leftanddown"></span><span id="RC_LEFTANDDOWN"></span>**RC\_LeftAndDown**
</dt> <dd>

Supports handwriting input in left and down order, such as in Hebrew and Arabic languages.

</dd> <dt>

<span id="RC_DownAndLeft"></span><span id="rc_downandleft"></span><span id="RC_DOWNANDLEFT"></span>**RC\_DownAndLeft**
</dt> <dd>

Supports handwriting input in down and left order, such as in some East Asian languages.

</dd> <dt>

<span id="RC_DownAndRight"></span><span id="rc_downandright"></span><span id="RC_DOWNANDRIGHT"></span>**RC\_DownAndRight**
</dt> <dd>

Supports handwriting input in down and right order, such as in some East Asian languages.

</dd> <dt>

<span id="RC_ArbitraryAngle"></span><span id="rc_arbitraryangle"></span><span id="RC_ARBITRARYANGLE"></span>**RC\_ArbitraryAngle**
</dt> <dd>

Supports text written at arbitrary angles.

</dd> <dt>

<span id="RC_Lattice"></span><span id="rc_lattice"></span><span id="RC_LATTICE"></span>**RC\_Lattice**
</dt> <dd>

Supports returning a lattice as an alternative a string for handwriting recognition results.

</dd> <dt>

<span id="RC_AdviseInkChange"></span><span id="rc_adviseinkchange"></span><span id="RC_ADVISEINKCHANGE"></span>**RC\_AdviseInkChange**
</dt> <dd>

Supports interrupting background recognition, such as when the ink has changed.

</dd> <dt>

<span id="RC_StrokeReorder"></span><span id="rc_strokereorder"></span><span id="RC_STROKEREORDER"></span>**RC\_StrokeReorder**
</dt> <dd>

Supports that stroke order, spatial and temporal, is handled as part of the recognition operation. The [**IInkAnalyzer**](iinkanalyzer.md) does not reorder strokes before sending ink to the [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md).

</dd> <dt>

<span id="RC_Personalizable"></span><span id="rc_personalizable"></span><span id="RC_PERSONALIZABLE"></span>**RC\_Personalizable**
</dt> <dd>

Supports personalized handwriting, where the recognizer improves recognition when exposed to the same handwriting over time.

</dd> <dt>

<span id="RC_PrefersArbitraryAngle"></span><span id="rc_prefersarbitraryangle"></span><span id="RC_PREFERSARBITRARYANGLE"></span>**RC\_PrefersArbitraryAngle**
</dt> <dd>

The [**IInkAnalyzer**](iinkanalyzer.md) need not rotate the handwriting to a horizontal orientation before sending the ink to the [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md).

</dd> <dt>

<span id="RC_PrefersParagraphBreaking"></span><span id="rc_prefersparagraphbreaking"></span><span id="RC_PREFERSPARAGRAPHBREAKING"></span>**RC\_PrefersParagraphBreaking**
</dt> <dd>

The [**IInkAnalyzer**](iinkanalyzer.md) should send entire paragraphs of ink to the [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md), allowing the **IInkAnalysisRecognizer** to do the line breaking and word (or character) breaking.

</dd> <dt>

<span id="RC_PrefersSegmentationRecognition"></span><span id="rc_preferssegmentationrecognition"></span><span id="RC_PREFERSSEGMENTATIONRECOGNITION"></span>**RC\_PrefersSegmentationRecognition**
</dt> <dd>

Recognizes only one word or character per recognition operation. The [**IInkAnalyzer**](iinkanalyzer.md) performs segmentation on the handwriting and sends only one segment at a time to the [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md).

</dd> </dl>

## Remarks

This enumeration allows a bitwise combination of its member values. Use this enumeration to find an installed ink recognizer that supports the attributes you need.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |



## See also

<dl> <dt>

[**IInkAnalysisRecognizer::GetCapabilities**](iinkanalysisrecognizer-getcapabilities.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 





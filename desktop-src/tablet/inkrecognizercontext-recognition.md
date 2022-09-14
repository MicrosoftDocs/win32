---
description: Occurs when the InkRecognizerContext has generated results from the BackgroundRecognize method.
ms.assetid: 0cc319af-cd0b-4089-928b-cae6c86f6f61
title: InkRecognizerContext.Recognition event (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkRecognizerContext.Recognition event

Occurs when the [**InkRecognizerContext**](inkrecognizercontext-class.md) has generated results from the [**BackgroundRecognize**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-backgroundrecognize) method.

## Syntax


```C++
void Recognition(
  [in] BSTR                 RecognizedString,
  [in] VARIANT              CustomData,
  [in] InkRecognitionStatus RecognitionStatus
);
```



## Parameters

<dl> <dt>

*RecognizedString* \[in\]
</dt> <dd>

The recognition result text with the highest confidence.

For more information about the BSTR data type, see the [Using the COM Library](using-the-com-library.md).

</dd> <dt>

*CustomData* \[in\]
</dt> <dd>

The object that contains the custom data for the recognition result.

For more information about the VARIANT structure, see the [Using the COM Library](using-the-com-library.md).

</dd> <dt>

*RecognitionStatus* \[in\]
</dt> <dd>

The recognition status as of the most recent recognition result.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

The behavior of the application programming interface (API) is unpredictable if you try to gain access to the original [**InkRecognizerContext**](inkrecognizercontext-class.md) object from the recognition event handler. Do not attempt to do this. Instead, if you need to do this, create a flag and set it in the [Recognition](ink-recognition.md) event handler. Then you can poll that flag to determine when to change the **InkRecognizerContext** properties outside of the event handler.

This event method is defined in the \_IInkEvents interface. The \_IInkEvents interface implements the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface with an identifier of DISPID\_IRERecognition.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl>                               |



## See also

<dl> <dt>

[**InkRecognizerContext Class**](inkrecognizercontext-class.md)
</dt> <dt>

[**BackgroundRecognize Method**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-backgroundrecognize)
</dt> <dt>

[**InkRecognitionStatus Enumeration**](/windows/desktop/api/msinkaut/ne-msinkaut-inkrecognitionstatus)
</dt> <dt>

[**Recognize Method**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-recognize)
</dt> <dt>

[**IInkRecognitionResult Interface**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkrecognitionresult)
</dt> </dl>

 


---
Description: Occurs when the InkEdit control gets results manually from a call to the InkEditRecognize method or automatically after the recognition timeout fires.
ms.assetid: 09618be0-fe49-494f-940f-79ff8352097e
title: InkEdit.RecognitionResult event
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# InkEdit.RecognitionResult event

Occurs when the [InkEdit](inkedit-control-reference.md) control gets results manually from a call to the [**InkEdit::Recognize**](/windows/win32/inked/?branch=master) method or automatically after the recognition timeout fires.

## Syntax


```C++
void RecognitionResult(
  [in] IInkRecognitionResult *RecognitionResult
);
```



## Parameters

<dl> <dt>

*RecognitionResult* \[in\]
</dt> <dd>

An [**IInkRecognitionResult**](/windows/win32/msinkaut/nn-msinkaut-iinkrecognitionresult?branch=master) object that contains the result of the recognition.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event method is defined in the **\_IInkEditEvents** interface. The **\_IInkEditEvents** interface implements the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface with an identifier of DISPID\_IeeRecognitionResult.

## Requirements



|                                     |                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>Inked.h (also requires inked\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkEd.dll</dt> </dl>                          |



## See also

<dl> <dt>

[InkEdit](inkedit-control-reference.md)
</dt> <dt>

[**Recognize Method \[InkEdit Control\]**](/windows/win32/inked/?branch=master)
</dt> </dl>

 

 





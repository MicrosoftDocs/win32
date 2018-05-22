---
Description: 'Occurs when the current selection of text in the InkEdit control has changed or the insertion point has moved.'
ms.assetid: '14ddffe7-bdfe-4a35-82c7-b3401b5b720c'
title: 'InkEdit.SelChange event'
---

# InkEdit.SelChange event

Occurs when the current selection of text in the [InkEdit](inkedit-control-reference.md) control has changed or the insertion point has moved.

## Syntax


```C++
void SelChange();
```



## Parameters

This event has no parameters.

## Return value

This event does not return a value.

## Remarks

You can use the **SelChange** event to check the various properties that give information about the current selection (such as [**SelBold**](inkedit-selbold.md)) so you can update buttons in a toolbar, for example.

## Requirements



|                                     |                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>Inked.h (also requires inked\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkEd.dll</dt> </dl>                          |



## See also

<dl> <dt>

[InkEdit](inkedit-control-reference.md)
</dt> </dl>

 

 





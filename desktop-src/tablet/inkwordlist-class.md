---
Description: Represents a list of words that can be used to improve the recognition result.
ms.assetid: d189fd13-ec69-45dc-8be4-fea48f337636
title: InkWordList class (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- InkWordList
- InkWordList.IInkWordList
api_type: 
- COM
api_location: 
- InkObj.dll
- InkObj.dll.dll
---

# InkWordList class

Represents a list of words that can be used to improve the recognition result.

**InkWordList** has these types of members:

-   [Interfaces](#interfaces)
-   [Methods](#methods)

### Interfaces

The **InkWordList** class defines these interfaces.



| Interface        | Description                                                           |
|:-----------------|:----------------------------------------------------------------------|
| **IInkWordList** | This object implements the **IInkWordList** COM interface.<br/> |



 

### Methods

The **InkWordList** class has these methods.



| Method                                       | Description                                                             |
|:---------------------------------------------|:------------------------------------------------------------------------|
| [**AddWord**](https://msdn.microsoft.com/en-us/library/ms702462(v=VS.85).aspx)       | Adds a single word to the **InkWordList**.<br/>                   |
| [**Merge**](https://msdn.microsoft.com/en-us/library/ms700650(v=VS.85).aspx)           | Merges another **InkWordList** to into this **InkWordList**.<br/> |
| [**RemoveWord**](https://msdn.microsoft.com/en-us/library/ms701127(v=VS.85).aspx) | Removes a single word from a **InkWordList**.<br/>                |



 

## Remarks

This object can be instantiated by calling the [**CoCreateInstance**](https://docs.microsoft.com/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) method in C++.

## Requirements



|                                     |                                                                                                                     |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl>                               |



## See also

<dl> <dt>

[**WordList Property**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-get_wordlist)
</dt> <dt>

[Factoid Constants](factoid-constants.md)
</dt> <dt>

[**InkRecognizerContext Class**](inkrecognizercontext-class.md)
</dt> </dl>

 

 





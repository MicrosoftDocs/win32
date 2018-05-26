---
Description: An HRECOCONTEXT handle is used to add ink to the context, perform ink recognition (synchronously or asynchronously), retrieve the recognition result, and retrieve alternates.
ms.assetid: 509188e2-28af-4915-bc76-ee451133398f
title: HRECOCONTEXT Handle
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HRECOCONTEXT Handle

An **HRECOCONTEXT** handle is used to add ink to the context, perform ink recognition (synchronously or asynchronously), retrieve the recognition result, and retrieve alternates.

The primary reason for having recognizer context handles is to differentiate between ink inputs. For example, you can create an application with two windows, the user being able to ink in either window. You do not want to have the ink of the first window mixed up with the ink of the second window when you ask the recognizer to recognize the ink of one of the windows. In this kind of application, you create two recognizer contexts (one for each window) and you add strokes coming into window 1 into recognizer context 1 and strokes from window 2 into recognizer context 2. To return recognition results, call process on recognizer context 1 or recognizer context 2 depending on whether you want the results for window 1 or 2.

The recognizer context handle can be anything you want. But typically it is an index in a global array of structures. The structures may contain all the strokes that have been entered and all the variables that the recognizer uses for that particular piece of ink (for example, your internal lattice structure, or the current state of recognition). One structure may contain all the information the recognizer needs and uses for one particular piece of ink.

To get an **HRECOCONTEXT** handle, call the [**CreateContext**](/windows/win32/recapis/nf-recapis-createcontext?branch=master) function.


```C++
typedef HANDLE HRECOCONTEXT;
```



## Remarks

The following are the **HRECOCONTEXT** functions



| Function                                                            | Description                                                                                                                                                                                                                                                 |
|---------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddStroke**](/windows/win32/recapis/nf-recapis-addstroke?branch=master)                                      | Adds an ink stroke to the recognizer context.<br/>                                                                                                                                                                                                    |
| [**AdviseInkChange**](/windows/win32/recapis/nf-recapis-adviseinkchange?branch=master)                          | Stops the recognizer from processing ink because a new stroke is being added or deleted.<br/>                                                                                                                                                         |
| [**CloneContext**](/windows/win32/recapis/nf-recapis-clonecontext?branch=master)                                | Creates a recognizer context that contains the same settings as the original. The new recognizer context does not include the ink or recognition results of the original.<br/>                                                                        |
| [**EndInkInput**](/windows/win32/msinkaut/?branch=master)             | Indicates that no more ink will be added to the context.<br/>                                                                                                                                                                                         |
| [**GetAlternateList**](/windows/win32/recapis/?branch=master)                        | Returns a list of alternates for the best result string.<br/>                                                                                                                                                                                         |
| [**GetBestAlternate**](/windows/win32/recapis/?branch=master)                        | Returns an [HRECOALT Handle](hrecoalt-handle.md) pointer for the best result alternate.<br/>                                                                                                                                                         |
| [**GetBestResultString**](/windows/win32/recapis/nf-recapis-getbestresultstring?branch=master)                  | Returns the best result string.<br/>                                                                                                                                                                                                                  |
| [**GetContextPropertyList**](/windows/win32/recapis/nf-recapis-getcontextpropertylist?branch=master)            | Returns a list of properties the recognizer supports.<br/>                                                                                                                                                                                            |
| [**GetContextPropertyValue**](/windows/win32/recapis/nf-recapis-getcontextpropertyvalue?branch=master)          | Returns a specified property value from the recognizer context.<br/>                                                                                                                                                                                  |
| [**GetEnabledUnicodeRanges**](/windows/win32/recapis/nf-recapis-getenabledunicoderanges?branch=master)          | Returns a list of Unicode point ranges enabled on the context.<br/>                                                                                                                                                                                   |
| [**GetGuide**](/windows/win32/recapis/nf-recapis-getguide?branch=master)                                        | Returns the guide used for boxed or lined input.<br/>                                                                                                                                                                                                 |
| [**GetLatticePtr**](/windows/win32/recapis/nf-recapis-getlatticeptr?branch=master)                              | Returns a pointer to the lattice for the current results.<br/>                                                                                                                                                                                        |
| [**IsStringSupported**](/windows/win32/msinkaut/?branch=master) | Returns a value that indicates whether a word, date, time, number, or other text that is passed in is contained in the dictionary.<br/>                                                                                                               |
| [**Process**](/windows/win32/recapis/nf-recapis-process?branch=master)                                          | Performs ink recognition synchronously.<br/>                                                                                                                                                                                                          |
| [**ResetContext**](/windows/win32/recapis/nf-recapis-resetcontext?branch=master)                                | Deletes the current ink and recognition results from the context.<br/>                                                                                                                                                                                |
| [**SetCACMode**](/windows/win32/recapis/nf-recapis-setcacmode?branch=master)                                    | Specifies character Autocomplete mode for character or word recognition.<br/>                                                                                                                                                                         |
| [**SetContextPropertyValue**](/windows/win32/recapis/nf-recapis-setcontextpropertyvalue?branch=master)          | Adds a property to the recognizer context. If a property already exists, its value is modified.<br/>                                                                                                                                                  |
| [**SetEnabledUnicodeRanges**](/windows/win32/recapis/nf-recapis-setenabledunicoderanges?branch=master)          | Enables one or more Unicode point ranges on the context.<br/>                                                                                                                                                                                         |
| [**SetFactoid**](/windows/win32/recapis/nf-recapis-setfactoid?branch=master)                                    | Sets the factoid a recognizer uses to constrain its search for the result.<br/>                                                                                                                                                                       |
| [**SetFlags**](/windows/win32/recapis/nf-recapis-setflags?branch=master)                                        | Sets how the recognizer interprets the ink and determines the result string.<br/>                                                                                                                                                                     |
| [**SetGuide**](/windows/win32/recapis/nf-recapis-setguide?branch=master)                                        | Sets the guide to use for boxed or lined input.<br/>                                                                                                                                                                                                  |
| [**SetTextContext**](/windows/win32/recapis/nf-recapis-settextcontext?branch=master)                            | Provides the text strings that come before and after the text contained in the recognizer context. For recognizers of East Asian characters, the [**SetTextContext**](/windows/win32/recapis/nf-recapis-settextcontext?branch=master) function provides characters rather than text strings.<br/> |
| [**SetWordList**](/windows/win32/recapis/nf-recapis-setwordlist?branch=master)                                  | Sets the word list for the current recognizer context to recognize.<br/>                                                                                                                                                                              |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                        |
| Minimum supported server<br/> | None supported<br/>                                                            |
| Header<br/>                   | <dl> <dt>Recapis.h</dt> </dl> |



 

 





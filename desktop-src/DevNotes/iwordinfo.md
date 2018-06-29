---
Description: The IWordInfo interface is a Japanese-specific language resource component. The object parses text and identifies individual words, returning either the words in the string or returns the dictionary (root) forms of the words in the text of the string.
ms.assetid: 760d9c78-d564-40a2-b2e4-d538c32361ed
title: IWordInfo interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWordInfo
- IWordInfo.BreakText
api_type: 
- COM
api_location: 
- Msir3jp.dll
---

# IWordInfo interface

\[This interface is obsolete and is not supported on Windows Vista.\]

The **IWordInfo** interface is a Japanese-specific language resource component. The object parses text and identifies individual words, returning either the words in the string or returns the dictionary (root) forms of the words in the text of the string.

## Members

The **IWordInfo** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/en-us/library/ms680509(v=VS.85).aspx) interface. **IWordInfo** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWordInfo** interface has these methods.



| Method        | Description                                                                                                                                 |
|:--------------|:--------------------------------------------------------------------------------------------------------------------------------------------|
| **BreakText** | Parses text to identify words and provides the results to the [WordSink](Http://go.microsoft.com/fwlink/p/?linkid=85323) object.<br/> |



 

## Remarks

This interface is used to retrieve Japanese word breaks or dictionary forms for the text to be analyzed. The dictionary form of a word is the uninflected form of the word.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| End of client support<br/>    | Windows XP<br/>                                                                  |
| End of server support<br/>    | Windows Server 2003<br/>                                                         |
| DLL<br/>                      | <dl> <dt>Msir3jp.dll</dt> </dl> |



## See also

<dl> <dt>

[**WordInfo**](wordinfo-coclass.md)
</dt> <dt>

[WordSink](Http://go.microsoft.com/fwlink/p/?linkid=85323)
</dt> </dl>

 

 





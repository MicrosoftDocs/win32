---
Description: 'An HRECOGNIZER handle is used to create a recognizer context, retrieve the recognizer''s attributes and properties, and determine which packet properties the recognizer requires to perform recognition.'
ms.assetid: '1fc1901e-8c4d-4ef1-8c38-52d46ce10a48'
title: HRECOGNIZER Handle
---

# HRECOGNIZER Handle

An **HRECOGNIZER** handle is used to create a recognizer context, retrieve the recognizer's attributes and properties, and determine which packet properties the recognizer requires to perform recognition.


```C++
typedef HANDLE HRECOGNIZER;
```



## Remarks

The following functions use an **HRECOGNIZER**.



| Function                                                               | Description                                                                                        |
|------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| [**CreateRecognizer**](createrecognizer.md)                           | Creates a recognizer.<br/>                                                                   |
| [**DestroyRecognizer**](destroyrecognizer.md)                         | Destroys a recognizer.<br/>                                                                  |
| [**GetRecoAttributes**](getrecoattributes.md)                         | Returns the attributes of the recognizer.<br/>                                               |
| [**CreateContext**](createcontext.md)                                 | Creates a recognizer context.<br/>                                                           |
| [**DestroyContext**](destroycontext.md)                               | Destroys a recognizer context.<br/>                                                          |
| [**DestroyRecognizer**](destroyrecognizer.md)                         | Destroys a recognizer.<br/>                                                                  |
| [**GetAllRecognizers**](getallrecognizers.md)                         | Gets all recognizers.<br/>                                                                   |
| [**GetResultPropertyList**](getresultpropertylist.md)                 | Retrieves a list of properties the recognizer can return for a result range.<br/>            |
| [**GetPreferredPacketDescription**](getpreferredpacketdescription.md) | Retrieves a packet description that contains the packet properties the recognizer uses.<br/> |
| [**GetUnicodeRanges**](getunicoderanges.md)                           | Retrieves the ranges of Unicode points that the recognizer supports.<br/>                    |
| [**LoadCachedAttributes**](loadcachedattributes.md)                   | Loads the cached attributes of a recognizer.<br/>                                            |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                        |
| Minimum supported server<br/> | None supported<br/>                                                            |
| Header<br/>                   | <dl> <dt>Recapis.h</dt> </dl> |



 

 





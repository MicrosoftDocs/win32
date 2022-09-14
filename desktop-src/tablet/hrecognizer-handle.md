---
description: An HRECOGNIZER handle is used to create a recognizer context, retrieve the recognizer's attributes and properties, and determine which packet properties the recognizer requires to perform recognition.
ms.assetid: 1fc1901e-8c4d-4ef1-8c38-52d46ce10a48
title: HRECOGNIZER Handle (Recapis.h)
ms.topic: reference
ms.date: 05/31/2018
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
| [**CreateRecognizer**](/windows/desktop/api/recapis/nf-recapis-createrecognizer)                           | Creates a recognizer.<br/>                                                                   |
| [**DestroyRecognizer**](/windows/desktop/api/recapis/nf-recapis-destroyrecognizer)                         | Destroys a recognizer.<br/>                                                                  |
| [**GetRecoAttributes**](/windows/desktop/api/recapis/nf-recapis-getrecoattributes)                         | Returns the attributes of the recognizer.<br/>                                               |
| [**CreateContext**](/windows/desktop/api/recapis/nf-recapis-createcontext)                                 | Creates a recognizer context.<br/>                                                           |
| [**DestroyContext**](/windows/desktop/api/recapis/nf-recapis-destroycontext)                               | Destroys a recognizer context.<br/>                                                          |
| [**GetAllRecognizers**](/windows/desktop/api/recapis/nf-recapis-getallrecognizers)                         | Gets all recognizers.<br/>                                                                   |
| [**GetResultPropertyList**](/windows/desktop/api/recapis/nf-recapis-getresultpropertylist)                 | Retrieves a list of properties the recognizer can return for a result range.<br/>            |
| [**GetPreferredPacketDescription**](/windows/desktop/api/recapis/nf-recapis-getpreferredpacketdescription) | Retrieves a packet description that contains the packet properties the recognizer uses.<br/> |
| [**GetUnicodeRanges**](/windows/desktop/api/recapis/nf-recapis-getunicoderanges)                           | Retrieves the ranges of Unicode points that the recognizer supports.<br/>                    |
| [**LoadCachedAttributes**](/windows/desktop/api/recapis/nf-recapis-loadcachedattributes)                   | Loads the cached attributes of a recognizer.<br/>                                            |



 

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                        |
| Minimum supported server<br/> | None supported<br/>                                                            |
| Header<br/>                   | <dl> <dt>Recapis.h</dt> </dl> |



 

 





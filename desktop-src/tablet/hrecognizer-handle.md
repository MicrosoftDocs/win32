---
Description: An HRECOGNIZER handle is used to create a recognizer context, retrieve the recognizers attributes and properties, and determine which packet properties the recognizer requires to perform recognition.
ms.assetid: 1fc1901e-8c4d-4ef1-8c38-52d46ce10a48
title: HRECOGNIZER Handle
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
| [**CreateRecognizer**](/windows/win32/recapis/nf-recapis-createrecognizer?branch=master)                           | Creates a recognizer.<br/>                                                                   |
| [**DestroyRecognizer**](/windows/win32/recapis/nf-recapis-destroyrecognizer?branch=master)                         | Destroys a recognizer.<br/>                                                                  |
| [**GetRecoAttributes**](/windows/win32/recapis/nf-recapis-getrecoattributes?branch=master)                         | Returns the attributes of the recognizer.<br/>                                               |
| [**CreateContext**](/windows/win32/recapis/nf-recapis-createcontext?branch=master)                                 | Creates a recognizer context.<br/>                                                           |
| [**DestroyContext**](/windows/win32/recapis/nf-recapis-destroycontext?branch=master)                               | Destroys a recognizer context.<br/>                                                          |
| [**DestroyRecognizer**](/windows/win32/recapis/nf-recapis-destroyrecognizer?branch=master)                         | Destroys a recognizer.<br/>                                                                  |
| [**GetAllRecognizers**](/windows/win32/recapis/nf-recapis-getallrecognizers?branch=master)                         | Gets all recognizers.<br/>                                                                   |
| [**GetResultPropertyList**](/windows/win32/recapis/nf-recapis-getresultpropertylist?branch=master)                 | Retrieves a list of properties the recognizer can return for a result range.<br/>            |
| [**GetPreferredPacketDescription**](/windows/win32/recapis/nf-recapis-getpreferredpacketdescription?branch=master) | Retrieves a packet description that contains the packet properties the recognizer uses.<br/> |
| [**GetUnicodeRanges**](/windows/win32/recapis/nf-recapis-getunicoderanges?branch=master)                           | Retrieves the ranges of Unicode points that the recognizer supports.<br/>                    |
| [**LoadCachedAttributes**](/windows/win32/recapis/nf-recapis-loadcachedattributes?branch=master)                   | Loads the cached attributes of a recognizer.<br/>                                            |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                        |
| Minimum supported server<br/> | None supported<br/>                                                            |
| Header<br/>                   | <dl> <dt>Recapis.h</dt> </dl> |



 

 





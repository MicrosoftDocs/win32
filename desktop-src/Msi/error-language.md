---
Description: The read-only Language property of the Error object returns the LANGID of the current error.
ms.assetid: f47cad5d-8e76-4210-b1ab-377d2d05379e
title: Error.Language property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Error.Language property

The read-only **Language** property of the [**Error**](error-object.md) object returns the **LANGID** of the current error.

This property is read-only.

## Syntax


```JScript
propVal = Error.Language
```



## Property value

## Remarks

The value of the **Language** property is -1 unless the error is of type msmErrorLanguageUnsupported or msmErrorLanguageFailed. You can determine the type of error by calling the [**Type**](error-type.md) property of the [**Error**](error-object.md) object.

### C++

See [**get\_Language Function (Error Object)**](https://msdn.microsoft.com/en-us/library/Aa369252(v=VS.85).aspx).

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 1.0 or later<br/>                                                    |
| Header<br/>  | <dl> <dt>Mergemod.h</dt> </dl>   |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl> |



 

 





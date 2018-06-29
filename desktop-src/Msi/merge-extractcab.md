---
Description: The ExtractCAB method of the Merge object extracts the embedded .cab file from a module and saves it as the specified file. The installer creates this file if it does not already exist and overwritten if it does exist.
ms.assetid: 3f794dac-6eeb-4c1e-8c23-c9d7384f650f
title: Merge.ExtractCAB method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Merge.ExtractCAB
- IMsmMerge.ExtractCAB
api_type: 
- COM
api_location: 
- Mergemod.dll
---

# Merge.ExtractCAB method

The **ExtractCAB** method of the [**Merge**](merge-object.md) object extracts the embedded .cab file from a module and saves it as the specified file. The installer creates this file if it does not already exist and overwritten if it does exist.

## Syntax


```JScript
Merge.ExtractCAB(
  FileName
)
```



## Parameters

<dl> <dt>

*FileName* 
</dt> <dd>

The fully qualified destination file.

</dd> </dl>

## Return value

This method does not return a value.

## C++

See [**ExtractCAB**](https://msdn.microsoft.com/en-us/library/Aa369269(v=VS.85).aspx) function.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | Mergemod.dll 1.0 or later<br/>                                                    |
| Header<br/>  | <dl> <dt>Mergemod.h</dt> </dl>   |
| DLL<br/>     | <dl> <dt>Mergemod.dll</dt> </dl> |



 

 





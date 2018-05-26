---
title: WcsCheckColors function
description: Determines whether the colors in an array are within the output gamut of a specified WCS color transform.
ms.assetid: 01b452bf-4352-4b83-863b-e9eb76121fdd
keywords:
- WcsCheckColors function Windows Color System
topic_type:
- apiref
api_name:
- WcsCheckColors
api_location:
- mscms.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WcsCheckColors function

Determines whether the colors in an array are within the output gamut of a specified WCS color transform.

## Syntax


```C++
BOOL WINAPI WcsCheckColors(
  _In_  HTRANSFORM    hColorTransform,
  _In_  DWORD         nColors,
  _In_  DWORD         nInputChannels,
  _In_  COLORDATATYPE cdtInput,
  _In_  DWORD         cbInput,
  _In_                pInputData,
  _Out_ PBYTE         paResult
);
```



## Parameters

<dl> <dt>

*hColorTransform* \[in\]
</dt> <dd>

A handle to the specified WCS color transform.

</dd> <dt>

*nColors* \[in\]
</dt> <dd>

The number of elements in the array pointed to by *pInputData* and *paResult*.

</dd> <dt>

*nInputChannels* \[in\]
</dt> <dd>

The number of channels per element in the array pointed to by *pInputData*.

</dd> <dt>

*cdtInput* \[in\]
</dt> <dd>

The input COLORDATATYPE color data type.

</dd> <dt>

*cbInput* \[in\]
</dt> <dd>

The buffer size of *pInputData*.

</dd> <dt>

*pInputData* \[in\]
</dt> <dd>

A pointer to an array of input colors. Colors in this array correspond to the color space of the source profile. The size of the buffer for this array will be the number of bytes indicated by *cbInput*.

</dd> <dt>

*paResult* \[out\]
</dt> <dd>

A pointer to an array of *nColors* bytes that receives the results of the test.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Remarks

If the input and the output color data types are not compatible with the color transform, this function will convert the input color data as required.

This function fails if you use an International Color Consortium (ICC) transform is used.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Mscms.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mscms.dll</dt> </dl> |



## See also

<dl> <dt>

[Basic Color Management Concepts](basic-color-management-concepts.md)
</dt> <dt>

[Windows Color System Schemas and Algorithms](windows-color-system-schemas-and-algorithms.md)
</dt> <dt>

[Functions](functions.md)
</dt> </dl>

 

 






---
title: WcsTranslateColors function
description: Translates an array of colors from the source color space to the destination color space as defined by a color transform.
ms.assetid: e7053c70-5b32-4d33-983c-a4c9c14a0d1b
keywords:
- WcsTranslateColors function Windows Color System
topic_type:
- apiref
api_name:
- WcsTranslateColors
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

# WcsTranslateColors function

Translates an array of colors from the source color space to the destination color space as defined by a color transform.

## Syntax


```C++
BOOL WINAPI WcsTranslateColors(
  _In_  HTRANSFORM    hColorTransform,
  _In_  DWORD         nColors,
  _In_  DWORD         nInputChannels,
  _In_  COLORDATATYPE cdtInput,
  _In_  DWORD         cbInput,
  _In_  PVOID         pInputData,
  _In_  DWORD         nOutputChannels,
  _In_  COLORDATATYPE cdtOutput,
  _In_  DWORD         cbOutput,
  _Out_ PVOID         pOutputData
);
```



## Parameters

<dl> <dt>

*hColorTransform* \[in\]
</dt> <dd>

A handle for the WCS color transform.

</dd> <dt>

*nColors* \[in\]
</dt> <dd>

The number of elements in the array to which *pInputData* and *pOutputData* point.

</dd> <dt>

*nInputChannels* \[in\]
</dt> <dd>

The number of channels per element in the array to which *pInputData* points.

</dd> <dt>

*cdtInput* \[in\]
</dt> <dd>

The input [**COLORDATATYPE**](colordatatype.md) color data type.

</dd> <dt>

*cbInput* \[in\]
</dt> <dd>

The buffer size, in bytes, of *pInputData*.

</dd> <dt>

*pInputData* \[in\]
</dt> <dd>

A pointer to an array of input colors. The size of the buffer for this array, in bytes, is the **DWORD** value of *cbInput*.

</dd> <dt>

*nOutputChannels* \[in\]
</dt> <dd>

The number of channels per element in the array to which *pOutputData* points.

</dd> <dt>

*cdtOutput* \[in\]
</dt> <dd>

The [**COLORDATATYPE**](colordatatype.md) output that specified the color data type.

</dd> <dt>

*cbOutput* \[in\]
</dt> <dd>

The buffer size, in bytes, of *pOutputData*.

</dd> <dt>

*pOutputData* \[out\]
</dt> <dd>

A pointer to an array of colors that receives the results of the color translation.The size of the buffer for this array, in bytes, is the **DWORD** value of *cbOutput*.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Remarks

If the input and the output color data types are not compatible with the color transform, this function fails. This function will fail if an ICC transform is used.

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

 

 






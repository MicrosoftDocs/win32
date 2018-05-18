---
Description: 'The WcsTranslateColors function translates an array of colors from the source color space to the destination color space as defined by a color transform.'
ms.assetid: '99843150-9e27-4f09-a3ba-5ff87d3f1c88'
title: WcsTranslateColors function
---

# WcsTranslateColors function

The `WcsTranslateColors` function translates an array of colors from the source color space to the destination color space as defined by a color transform.

## Syntax


```C++
BOOL WcsTranslateColors(
  _In_  HTRANSFORM    hColorTransform,
  _In_  DWORD         nColors,
  _In_  DWORD         nInputChannels,
  _In_  COLORDATATYPE cdtInput,
  _In_  DWORD         cbInput,
  _In_  PVOID         pInputData,
  _In_  DWORD         nOutputChannels,
  _In_  COLORDATATYPE cdtOutput,
  _In_  DWORD         cbOutput,
  _Out_ PVOID         pOutputData
);
```



## Parameters

<dl> <dt>

*hColorTransform* \[in\]
</dt> <dd>

A handle to the WCS color transform to use.

</dd> <dt>

*nColors* \[in\]
</dt> <dd>

The number of elements in the array pointed to by *pInputData* and *pOutputData*.

</dd> <dt>

*nInputChannels* \[in\]
</dt> <dd>

The number of channels per element in the array pointed to by *pInputData*.

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

A pointer to an array of input colors.

</dd> <dt>

*nOutputChannels* \[in\]
</dt> <dd>

The number of channels per element in the array pointed to by *pOutputData*.

</dd> <dt>

*cdtOutput* \[in\]
</dt> <dd>

The output [**COLORDATATYPE**](colordatatype.md) color data type.

</dd> <dt>

*cbOutput* \[in\]
</dt> <dd>

The buffer size, in bytes, of *pOutputData*.

</dd> <dt>

*pOutputData* \[out\]
</dt> <dd>

A pointer to an array of colors that receives the results of the color translation.

</dd> </dl>

## 

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError** (described in the Microsoft Windows SDK documentation).

This function will fail if an ICC transform is used.

## Remarks

If the input and the output color data types are not compatible with the color transform, this function will fail.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Included in Windows Vista and later.<br/>                                                                                         |
| Header<br/>          | <dl> <dt>Icm.h</dt> </dl>                                                        |
| Library<br/>         | <dl> <dt>Mscms.lib</dt> </dl>                                                    |
| DLL<br/>             | <dl> <dt>Mscms.dll</dt> </dl>                                                    |



## See also

<dl> <dt>

[**COLORDATATYPE**](colordatatype.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20WcsTranslateColors%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")






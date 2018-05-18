---
Description: 'The WcsCheckColors function determines whether the colors in an array lie within the output gamut of a specified WCS color transform.'
ms.assetid: '1254b0d4-cb72-4171-b09d-f0bca58a137a'
title: WcsCheckColors function
---

# WcsCheckColors function

The `WcsCheckColors` function determines whether the colors in an array lie within the output gamut of a specified WCS color transform.

## Syntax


```C++
BOOL WcsCheckColors(
  _In_  HTRANSFORM    hColorTransform,
  _In_  DWORD         nColors,
  _In_  DWORD         nInputChannels,
  _In_  COLORDATATYPE cdtInput,
  _In_  DWORD         cbInput,
  _In_  PVOID         pInputData,
  _Out_ PBYTE         paResult
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

A pointer to an array of input colors. Colors in this array correspond to the color space of the source profile.

</dd> <dt>

*paResult* \[out\]
</dt> <dd>

A pointer to an array of *nColors* bytes that receives the results of the test.

</dd> </dl>

## 

If this function succeeds, the return value is **TRUE**.

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError** (described in the Microsoft Windows SDK documentation).

## Remarks

If the input and the output color data types are not compatible with the color transform, this function will convert the input color data as required.

This function will fail if an ICC transform is used.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Included in Windows Vista and later.<br/>                                                                                         |
| Header<br/>          | <dl> <dt>Icm.h</dt> </dl>                                                        |
| Library<br/>         | <dl> <dt>Mscms.lib</dt> </dl>                                                    |
| DLL<br/>             | <dl> <dt>Mscms.dll</dt> </dl>                                                    |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20WcsCheckColors%20function%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





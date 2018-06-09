---
Description: The SetInputData method sets the data to send to the printer.
ms.assetid: 8db7b5cd-b03f-4973-8711-8ac022bfb2b5
title: IBidiRequest::SetInputData method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IBidiRequest::SetInputData method

The **SetInputData** method sets the data to send to the printer.

## Syntax


```C++
HRESULT SetInputData(
  [in] const DWORD dwType,
  [in] const BYTE  *pData,
  [in] const UINT  uSize
);
```



## Parameters

<dl> <dt>

*dwType* \[in\]
</dt> <dd>

The type of data to be sent. This parameter can be one of the following values.



| Value                                                                                                                                                   | Meaning                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| <span id="BIDI_NULL"></span><span id="bidi_null"></span><dl> <dt>**BIDI\_NULL**</dt> </dl>       | No data.<br/>                                          |
| <span id="BIDI_INT"></span><span id="bidi_int"></span><dl> <dt>**BIDI\_INT**</dt> </dl>          | Integer data.<br/>                                     |
| <span id="BIDI_FLOAT"></span><span id="bidi_float"></span><dl> <dt>**BIDI\_FLOAT**</dt> </dl>    | Floating-point number.<br/>                            |
| <span id="BIDI_BOOL"></span><span id="bidi_bool"></span><dl> <dt>**BIDI\_BOOL**</dt> </dl>       | **TRUE** or **FALSE**.<br/>                            |
| <span id="BIDI_STRING"></span><span id="bidi_string"></span><dl> <dt>**BIDI\_STRING**</dt> </dl> | Unicode character string.<br/>                         |
| <span id="BIDI_TEXT"></span><span id="bidi_text"></span><dl> <dt>**BIDI\_TEXT**</dt> </dl>       | Non-localizable Unicode string.<br/>                   |
| <span id="BIDI_ENUM"></span><span id="bidi_enum"></span><dl> <dt>**BIDI\_ENUM**</dt> </dl>       | Enumeration data in the form of a Unicode string.<br/> |
| <span id="BIDI_BLOB"></span><span id="bidi_blob"></span><dl> <dt>**BIDI\_BLOB**</dt> </dl>       | Binary data.<br/>                                      |



 

</dd> <dt>

*pData* \[in\]
</dt> <dd>

A pointer to the byte array that contains the data. For example, if *dwType* is BIDI\_BOOL, *pData* points to a buffer that contains a Boolean value and if *dwType* is BIDI\_BLOB, *pData* points to a buffer that contains the binary data.

</dd> <dt>

*uSize* \[in\]
</dt> <dd>

Size, in bytes, of the byte array specified by *pData*.

</dd> </dl>

## Return value

The method returns one of the following values. For more information about COM error codes, see [Error Handling](15f3ae3e-1794-4948-a7aa-6309a703364b).



| Value                                                                                            | Description                                                                        |
|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>             | The operation was successfully carried out.<br/>                             |
| <dl> <dt>**E\_HANDLE**</dt> </dl>         | The interface handle was invalid.<br/>                                       |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>     | The type of the data was not consistent with its size.<br/>                  |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>    | Memory allocation failed.<br/>                                               |
| <dl> <dt>**None of the above**</dt> </dl> | The **HRESULT** contains an error code corresponding to the last error.<br/> |



 

## Remarks

If an application calls **SetInputData** more than once, only the value of the last call will be set.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                         |
| Target platform<br/>          | <dl> <dt>Desktop</dt> </dl>     |
| Header<br/>                   | <dl> <dt>Bidispl.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Bidispl.dll</dt> </dl> |



## See also

<dl> <dt>

[Bidirectional Communication Interfaces](bidirectional-communication-interfaces.md)
</dt> <dt>

[Bidirectional Communication Schema](https://www.bing.com/search?q=Bidirectional+Communication+Schema)
</dt> <dt>

[**IBidiRequest**](ibidirequest.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IBidiRequest::SetInputData%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")






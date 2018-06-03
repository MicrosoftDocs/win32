---
Description: The GetOutputData method gets the specified output data coming back from the printer.
ms.assetid: 0757dbc2-850b-4267-9339-b87591f85767
title: IBidiRequest::GetOutputData method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IBidiRequest::GetOutputData method

The **GetOutputData** method gets the specified output data coming back from the printer.

## Syntax


```C++
HRESULT GetOutputData(
  [in]  const DWORD  dwIndex,
  [out]       LPWSTR *ppszSchema,
  [out]       DWORD  *pdwType,
  [out]       BYTE   **ppData,
  [out]       ULONG  *uSize
);
```



## Parameters

<dl> <dt>

*dwIndex* \[in\]
</dt> <dd>

A zero-based index of the output data that is requested. For more information, see Remarks.

</dd> <dt>

*ppszSchema* \[out\]
</dt> <dd>

A pointer to a NULL-terminated string that receives the schema string. The caller must call the [**CoTaskMemFree**](https://www.bing.com/search?q=**CoTaskMemFree**) function to free this pointer.

</dd> <dt>

*pdwType* \[out\]
</dt> <dd>

A pointer to a variable that receives the type of the output data. This parameter can be one of the following values.



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

*ppData* \[out\]
</dt> <dd>

A pointer to the variable that receives a pointer to the byte array containing the output data. The buffer is allocated by the COM interface to store the output data. The caller is responsible for calling [**CoTaskMemFree**](https://www.bing.com/search?q=**CoTaskMemFree**) to free the buffer.

</dd> <dt>

*uSize* \[out\]
</dt> <dd>

A pointer to a variable that receives the size of the byte array specified by \*\*ppData.

</dd> </dl>

## Return value

The method returns one of the following values. For more information about COM error codes, see [Error Handling](https://www.bing.com/search?q=Error Handling).



| Return code                                                                                      | Description                                                                                           |
|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>             | The operation was successfully carried out.<br/>                                                |
| <dl> <dt>**E\_HANDLE**</dt> </dl>         | The interface handle was invalid.<br/>                                                          |
| <dl> <dt>**E\_POINTER**</dt> </dl>        | At least one of the pointer variable parameters did not reference a valid memory location.<br/> |
| <dl> <dt>**None of the above**</dt> </dl> | The **HRESULT** contains an error code corresponding to the last error.<br/>                    |



 

## Remarks

A single bidi request can have multiple results. The application calls [**GetEnumCount**](ibidirequest-ibidirequest--getenumcount.md) to get the number of results from the bidi request.

If an application calls **GetOutputData** with the same index twice, the interface allocates two different buffers and thus the application must free both buffers.

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

[Bidirectional Communication Schema](https://www.bing.com/search?q=Bidirectional Communication Schema)
</dt> <dt>

[**IBidiRequest**](ibidirequest.md)
</dt> <dt>

[**GetEnumCount**](ibidirequest-ibidirequest--getenumcount.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IBidiRequest::GetOutputData%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")






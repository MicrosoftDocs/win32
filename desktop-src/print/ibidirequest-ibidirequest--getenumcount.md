---
Description: 'The GetEnumCount method gets the number of output results from the bidi request.'
ms.assetid: '4c857ff4-02c1-487b-bdb0-44d62a4cf4a1'
title: 'IBidiRequest::GetEnumCount method'
---

# IBidiRequest::GetEnumCount method

The **GetEnumCount** method gets the number of output results from the bidi request.

## Syntax


```C++
HRESULT GetEnumCount(
  [out] DWORD *pdwTotal
);
```



## Parameters

<dl> <dt>

*pdwTotal* \[out\]
</dt> <dd>

A pointer to a variable that receives the number of output results.

</dd> </dl>

## Return value

The method returns one of the following values. For more information about COM error codes, see [Error Handling](_com_error_handling).



| Value                                                                                            | Description                                                                        |
|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>             | The method was successful.<br/>                                              |
| <dl> <dt>**E\_HANDLE**</dt> </dl>         | The interface handle was invalid.<br/>                                       |
| <dl> <dt>**E\_POINTER**</dt> </dl>        | The *pdwTotal* parameter did not point to a valid memory location.<br/>      |
| <dl> <dt>**None of the above**</dt> </dl> | The **HRESULT** contains an error code corresponding to the last error.<br/> |



 

## Remarks

A single bidi request can have multiple results. After calling **GetEnumCount**, the application can call [**GetOutputData**](ibidirequest-ibidirequest--getoutputdata.md) to select a particular result.

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

[Bidirectional Communication Schema](print.bidirectional_communication_schema)
</dt> <dt>

[**IBidiRequest**](ibidirequest.md)
</dt> <dt>

[**GetOutputData**](ibidirequest-ibidirequest--getoutputdata.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IBidiRequest::GetEnumCount%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")






---
Description: The SendRecvXMLString method sends a bidirectional printer communication request and receives the response as Unicode strings formatted in accordance with the Bidirectional Communication Schemas.
ms.assetid: 7d61402e-e248-4770-a828-9c266e528115
title: IBidiSpl2SendRecvXMLString method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IBidiSpl2::SendRecvXMLString method

The **SendRecvXMLString** method sends a bidirectional printer communication request and receives the response as Unicode strings formatted in accordance with the [Bidirectional Communication Schemas](print.bidirectional_communication_schema).

## Syntax


```C++
HRESULT SendRecvXMLString(
  [in]  BSTR bstrRequest,
  [out] BSTR *pbstrResponse
);
```



## Parameters

<dl> <dt>

*bstrRequest* \[in\]
</dt> <dd>

The bidi communication request as a Unicode string that complies with one of the [Bidirectional Communication Schemas](print.bidirectional_communication_schema).

</dd> <dt>

*pbstrResponse* \[out\]
</dt> <dd>

A pointer to the printer's response as a Unicode string that complies with one of the [Bidirectional Communication Schemas](print.bidirectional_communication_schema).

</dd> </dl>

## Return value

The method returns one of the following values.



| Value                                                                                            | Description                                                                           |
|--------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>             | The operation was successful.<br/>                                              |
| <dl> <dt>**E\_HANDLE**</dt> </dl>         | The interface handle is invalid.<br/>                                           |
| <dl> <dt>**None of the above**</dt> </dl> | The **HRESULT** contains an error code that corresponds to the last error.<br/> |



 

Note that the **HRESULT** may contain a system error code that is defined in [Bidi Error Codes](print.bidi_error_codes).

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Target platform<br/>          | <dl> <dt>Desktop</dt> </dl>     |
| Header<br/>                   | <dl> <dt>Bidispl.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Bidispl.dll</dt> </dl> |



## See also

<dl> <dt>

[**IBidiSpl2**](ibidispl2.md)
</dt> <dt>

[Bidirectional Communication Interfaces](bidirectional-communication-interfaces.md)
</dt> <dt>

[Print Spooler Components](print.print_spooler_components)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IBidiSpl2::SendRecvXMLString%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")






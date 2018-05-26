---
Description: The SendRecv method sends a bidi request to the printer.
ms.assetid: 0c91abd0-5e49-4e23-a50f-9d1dacf9d868
title: IBidiSplSendRecv method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IBidiSpl::SendRecv method

The **SendRecv** method sends a bidi request to the printer.

## Syntax


```C++
HRESULT SendRecv(
  [in] const LPCWSTR      pszAction,
  [in]       IBidiRequest *pRequest
);
```



## Parameters

<dl> <dt>

*pszAction* \[in\]
</dt> <dd>

A pointer to a NULL-terminated string that specifies the action for this bidi request. It can be one of the following constants.



| Constant                          | Value              | Meaning                                                                                                            |
|-----------------------------------|--------------------|--------------------------------------------------------------------------------------------------------------------|
| BIDI\_ACTION\_ENUM\_SCHEMA        | L"EnumSchema"      | Enumerate the schema. The returned data will be a list of schema that the port monitor or print provider supports. |
| BIDI\_ACTION\_GET                 | L"Get"             | Get the value of a specified schema.                                                                               |
| BIDI\_ACTION\_GET\_ALL            | L"GetAll"          | Get the values of all child nodes of the specified schema.                                                         |
| BIDI\_ACTION\_SET                 | L"Set"             | Set a value of the schema.                                                                                         |
| BIDI\_ACTION\_GET\_WITH\_ARGUMENT | L"GetWithArgument" | Request the bidi schema value using the data set as input argument.                                                |



 

</dd> <dt>

*pRequest* \[in\]
</dt> <dd>

A pointer to a single bidi request.

</dd> </dl>

## Return value

The method returns one of the following values.



| Value                                                                                            | Description                                                                        |
|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>             | The operation was successfully carried out.<br/>                             |
| <dl> <dt>**E\_HANDLE**</dt> </dl>         | The interface handle was invalid.<br/>                                       |
| <dl> <dt>**None of the above**</dt> </dl> | The **HRESULT** contains an error code corresponding to the last error.<br/> |



 

Note that the **HRESULT** may contain a system error code defined in [Bidi Error Codes](print.bidi_error_codes).

## Remarks

The BIDI\_ACTION\_\* values are case insensitive strings.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>     |
| Header<br/>          | <dl> <dt>Bidispl.h</dt> </dl>   |
| DLL<br/>             | <dl> <dt>Bidispl.dll</dt> </dl> |



## See also

<dl> <dt>

[**IBidiSpl**](ibidispl.md)
</dt> <dt>

[Bidirectional Communication Interfaces](bidirectional-communication-interfaces.md)
</dt> <dt>

[Bidirectional Communication Schema](print.bidirectional_communication_schema)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IBidiSpl::SendRecv%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")






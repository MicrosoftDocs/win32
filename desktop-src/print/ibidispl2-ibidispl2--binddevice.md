---
Description: The BindDevice method binds a printer to a bidirectional printer communication (bidi communication) request. This method is similar to the OpenPrinter function.
ms.assetid: c5bd238d-4b85-4463-aa73-ff3a7798ccff
title: IBidiSpl2::BindDevice method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IBidiSpl2::BindDevice method

The **BindDevice** method binds a printer to a bidirectional printer communication (bidi communication) request. This method is similar to the [**OpenPrinter**](https://www.bing.com/search?q=**OpenPrinter**) function.

## Syntax


```C++
HRESULT BindDevice(
  [in] const LPCWSTR pszDeviceName,
  [in] const DWORD   dwAccess
);
```



## Parameters

<dl> <dt>

*pszDeviceName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that contains the name of the printer or print server. If **NULL**, this parameter indicates the local print server.

</dd> <dt>

*dwAccess* \[in\]
</dt> <dd>

The access privileges for the printer. This parameter can be one of the following values.



| Value                                                                                                                                                                                              | Meaning                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="BIDI_ACCESS_ADMINISTRATOR"></span><span id="bidi_access_administrator"></span><dl> <dt>**BIDI\_ACCESS\_ADMINISTRATOR**</dt> </dl> | Permits users to perform all administrative tasks and basic printing operations except for SYNCHRONIZE. This is the same as PRINTER\_ALL\_ACCESS in [**OpenPrinter**](https://www.bing.com/search?q=**OpenPrinter**).<br/> |
| <span id="BIDI_ACCESS_USER"></span><span id="bidi_access_user"></span><dl> <dt>**BIDI\_ACCESS\_USER**</dt> </dl>                            | Permits users to perform basic printing operations. This is the same as PRINTER\_ACCESS\_USE in [**OpenPrinter**](https://www.bing.com/search?q=**OpenPrinter**).<br/>                                                     |



 

</dd> </dl>

## Return value

The method returns one of the following values.



| Return code                                                                                      | Description                                                                           |
|--------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>             | The operation was successful.<br/>                                              |
| <dl> <dt>**E\_HANDLE**</dt> </dl>         | The interface handle is invalid.<br/>                                           |
| <dl> <dt>**None of the above**</dt> </dl> | The **HRESULT** contains an error code that corresponds to the last error.<br/> |



 

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

[Bidirectional Communication Schema](https://www.bing.com/search?q=Bidirectional+Communication+Schema)
</dt> <dt>

[Print Spooler Components](https://www.bing.com/search?q=Print+Spooler+Components)
</dt> <dt>

[**OpenPrinter**](https://www.bing.com/search?q=**OpenPrinter**)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IBidiSpl2::BindDevice%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")






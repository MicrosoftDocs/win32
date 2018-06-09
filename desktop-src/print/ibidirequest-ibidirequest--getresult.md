---
Description: The GetResult method tells whether the bidi request was successful.
ms.assetid: d3d37fd2-b3fa-4664-ba4b-c355197d9b40
title: IBidiRequest::GetResult method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IBidiRequest::GetResult method

The **GetResult** method tells whether the bidi request was successful.

## Syntax


```C++
HRESULT GetResult(
  [out] HRESULT *phr
);
```



## Parameters

<dl> <dt>

*phr* \[out\]
</dt> <dd>

Pointer to a variable that specifies the status of the bidi request.

</dd> </dl>

## Return value

The method returns one of the following values. For more information about COM error codes, see [Error Handling](15f3ae3e-1794-4948-a7aa-6309a703364b).



| Value                                                                                            | Description                                                                                           |
|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>             | The operation was successfully carried out.<br/>                                                |
| <dl> <dt>**E\_HANDLE**</dt> </dl>         | The interface handle was invalid.<br/>                                                          |
| <dl> <dt>**E\_POINTER**</dt> </dl>        | At least one of the pointer variable parameters did not reference a valid memory location.<br/> |
| <dl> <dt>**None of the above**</dt> </dl> | The **HRESULT** contains an error code corresponding to the last error.<br/>                    |



 

Note that the return value indicates whether the method was successful. It does not indicate what happened to the bidi request.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IBidiRequest::GetResult%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")






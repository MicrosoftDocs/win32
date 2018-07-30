---
Description: The Next method gets the next specified number of elements in the enumeration sequence. This method is hidden from Visual Basic and scripting languages.
ms.assetid: bd94f592-ac6f-48b7-8190-352a5e18f224
title: IEnumParticipant::Next method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IEnumParticipant::Next method

\[**Next** is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **Next** method gets the next specified number of elements in the enumeration sequence. This method is hidden from Visual Basic and scripting languages.

## Syntax


```C++
);
```



## Parameters

<dl> <dt>

*celt* \[in\]
</dt> <dd>

Number of elements requested.

</dd> <dt>

*ppElements* \[out\]
</dt> <dd>

Pointer to [**ITAgentHandler**](https://msdn.microsoft.com/en-us/library/Aa380394(v=VS.85).aspx) interfaces.

</dd> <dt>

*pceltFetched* \[out\]
</dt> <dd>

Pointer to number of elements actually supplied. May be **NULL** if *celt* is one.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method returned *celt* number of elements.<br/>           |
| <dl> <dt>**S\_FALSE**</dt> </dl>       | Number of elements remaining was less than *celt*.<br/>   |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | The *ppElements* parameter is not a valid pointer.<br/>   |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/> |



 

## Remarks

TAPI calls the [**AddRef**](https://msdn.microsoft.com/en-us/library/ms691379(v=VS.85).aspx) method on the [**ITAgentHandler**](https://msdn.microsoft.com/en-us/library/Aa380394(v=VS.85).aspx) interface returned by **IEnumParticipant::Next**. The application must call [**Release**](https://msdn.microsoft.com/en-us/library/ms682317(v=VS.85).aspx) on the **ITAgentHandler** interface to free resources associated with it.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Confpriv.h</dt> </dl> |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Tapi3.dll</dt> </dl>  |



## See also

<dl> <dt>

[**IEnumParticipant**](ienumparticipant.md)
</dt> <dt>

[**ITParticipant**](itparticipant.md)
</dt> </dl>

 

 





---
description: The Clone method creates another enumerator that contains the same enumeration state as the current one. This method is hidden from Visual Basic and scripting languages.
ms.assetid: 551e0ddc-7ebf-4fc2-a155-0c9ee2f406d4
title: IEnumParticipant::Clone method (Confpriv.h)
ms.topic: reference
ms.date: 05/31/2018
---

# IEnumParticipant::Clone method

\[**Clone** is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **Clone** method creates another enumerator that contains the same enumeration state as the current one. This method is hidden from Visual Basic and scripting languages.

## Syntax


```C++
HRESULT Clone(
  [out] IEnumParticipant **ppEnum
);
```



## Parameters

<dl> <dt>

*ppEnum* \[out\]
</dt> <dd>

Pointer to new [**IEnumParticipant**](ienumparticipant.md) interface.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                    |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | The *ppEnum* parameter is not a valid pointer.<br/>       |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/> |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl>  | Failed for unknown reasons.<br/>                          |



 

## Remarks

TAPI calls the [**AddRef**](/windows/win32/api/unknwn/nf-unknwn-iunknown-addref) method on the [**IEnumParticipant**](ienumparticipant.md) interface returned by **IEnumParticipant::Clone**. The application must call [**Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) on the **IEnumParticipant** interface to free resources associated with it.

## Requirements



| Requirement | Value |
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

 


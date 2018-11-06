---
Description: The get\_LocalParticipantTypedInfo method gets participant information, such as e-mail name or geographical location.
ms.assetid: 46bb70a7-7dc9-463d-8416-737122412750
title: ITLocalParticipant::get_LocalParticipantTypedInfo method
ms.topic: article
ms.date: 05/31/2018
---

# ITLocalParticipant::get\_LocalParticipantTypedInfo method

The **get\_LocalParticipantTypedInfo** method gets participant information, such as e-mail name or geographical location.

## Syntax


```C++
);
```



## Parameters

<dl> <dt>

*InfoType* \[in\]
</dt> <dd>

[**PARTICIPANT\_TYPED\_INFO**](participant-typed-info.md) identifier of type of information required.

</dd> <dt>

*ppInfo* \[out\]
</dt> <dd>

Pointer to a **BSTR** that will contain the required information following a successful return of the method.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The application must use [SysFreeString](https://msdn.microsoft.com/en-us/library/ms221481(v=VS.71).aspx) to free the memory allocated for the *ppInfo* parameter.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Confpriv.h</dt> </dl> |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Tapi3.dll</dt> </dl>  |



## See also

<dl> <dt>

[**ITLocalParticipant**](itlocalparticipant.md)
</dt> <dt>

[**PARTICIPANT\_TYPED\_INFO**](participant-typed-info.md)
</dt> </dl>

 

 





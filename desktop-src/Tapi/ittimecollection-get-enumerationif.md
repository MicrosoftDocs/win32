---
description: The get\_EnumerationIf method returns the IEnumTime enumeration interface that enumerates ITTime.
ms.assetid: 31f6fa94-d047-4c53-96ae-8dd7e66a4e33
title: ITTimeCollection::get_EnumerationIf method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITTimeCollection::get\_EnumerationIf method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **get\_EnumerationIf** method returns the [**IEnumTime**](ienumtime.md) enumeration interface that enumerates [**ITTime**](ittime.md).

## Syntax


```C++
HRESULT get_EnumerationIf(
  [out] IEnumTime **pVal
);
```



## Parameters

<dl> <dt>

*pVal* \[out\]
</dt> <dd>

Pointer to the [**IEnumTime**](ienumtime.md) interface.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                         | Meaning                                                         |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                    |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | The *pVal* parameter is not a valid pointer.<br/>         |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Unspecified error.<br/>                                   |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | This method is not yet implemented.<br/>                  |



 

## Remarks

This method is interchangeable with [**get\_\_NewEnum**](ittimecollection-get--newenum.md) except that it returns [**IEnumTime**](ienumtime.md) instead of **IUnknown**.

TAPI calls the **AddRef** method on the [**IEnumTime**](ienumtime.md) interface returned by **ITTimeCollection::get\_EnumerationIf**. The application must call **Release** on the [**IEnumTime**](ienumtime.md) interface to free resources associated with it.

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



## See also

<dl> <dt>

[**IEnumTime**](ienumtime.md)
</dt> <dt>

[**ITTimeCollection**](ittimecollection.md)
</dt> <dt>

[**ITTime**](ittime.md)
</dt> </dl>

 

 





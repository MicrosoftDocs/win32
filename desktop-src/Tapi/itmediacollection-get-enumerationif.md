---
description: The get\_EnumerationIf method gets a pointer to a media enumeration interface.
ms.assetid: d5f1e10f-e5ad-45e6-a5ec-024905603012
title: ITMediaCollection::get_EnumerationIf method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITMediaCollection::get\_EnumerationIf method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **get\_EnumerationIf** method gets a pointer to a media enumeration interface.

## Syntax


```C++
HRESULT get_EnumerationIf(
  [out] IEnumMedia **pVal
);
```



## Parameters

<dl> <dt>

*pVal* \[out\]
</dt> <dd>

Pointer to the [**IEnumMedia**](ienummedia.md) interface for the desired item.

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

This method is interchangeable with [**get\_\_NewEnum**](itmediacollection-get--newenum.md) except that it returns [**IEnumMedia**](ienummedia.md) instead of **IUnknown**.

TAPI calls the **AddRef** method on the [**IEnumMedia**](ienummedia.md) interface returned by **ITMediaCollection::get\_Enumerationlf**. The application must call **Release** on the **IEnumMedia** interface to free resources associated with it.

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



## See also

<dl> <dt>

[**IEnumMedia**](ienummedia.md)
</dt> <dt>

[**ITMediaCollection**](itmediacollection.md)
</dt> </dl>

 

 





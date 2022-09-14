---
description: The Create method creates a new ITTime component.
ms.assetid: dee50454-8358-4898-b098-2de51505b658
title: ITTimeCollection::Create method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITTimeCollection::Create method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **Create** method creates a new [**ITTime**](ittime.md) component.

## Syntax


```C++
HRESULT Create(
  [in]  LONG   Index,
  [out] ITTime **ppTime
);
```



## Parameters

<dl> <dt>

*Index* \[in\]
</dt> <dd>

Index of the item to create. (The index array is one-based.)

</dd> <dt>

*ppTime* \[out\]
</dt> <dd>

Pointer to the b component created.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                         | Meaning                                                         |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                    |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | The *ppTime* parameter is not a valid pointer.<br/>       |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *Index* parameter is not valid.<br/>                  |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Unspecified error.<br/>                                   |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | This method is not yet implemented.<br/>                  |



 

## Remarks

TAPI calls the **AddRef** method on the [**ITTime**](ittime.md) interface returned by **ITTimeCollection::Create**. The application must call **Release** on the v interface to free resources associated with it.

This function may send data over the wire in unencrypted form; therefore, someone eavesdropping on the network may be able to read the data. The security risk of sending the data in clear text should be considered before using this method.

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



## See also

<dl> <dt>

[**ITTimeCollection**](ittimecollection.md)
</dt> <dt>

[**ITTime**](ittime.md)
</dt> </dl>

 

 





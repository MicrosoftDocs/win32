---
description: The EnumerateStreams method enumerates streams currently with the participants. This method is provided for C and C++ applications. Automation client applications, such as those written in Visual Basic, must use the get\_Streams method.
ms.assetid: 69db198d-fb4c-482b-bf49-5c636ac2f86b
title: ITParticipant::EnumerateStreams method (Ipmsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITParticipant::EnumerateStreams method

\[**EnumerateStreams**is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **EnumerateStreams** method enumerates streams currently with the participants. This method is provided for C and C++ applications. Automation client applications, such as those written in Visual Basic, must use the [**get\_Streams**](itparticipant-get-streams.md) method.

## Syntax


```C++
HRESULT EnumerateStreams(
  [out] IEnumStream **ppEnumStream
);
```



## Parameters

<dl> <dt>

*ppEnumStream* \[out\]
</dt> <dd>

Pointer to [**IEnumStream**](/windows/desktop/api/tapi3if/nn-tapi3if-ienumstream) interface pointer.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                     | Meaning                                                         |
|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | Method succeeded.<br/>                                    |
| <dl> <dt>**E\_POINTER**</dt> </dl> | The *ppEnumStream* parameter is not a valid pointer.<br/> |



 

## Remarks

TAPI calls the **AddRef** method on the [**IEnumStream**](/windows/desktop/api/tapi3if/nn-tapi3if-ienumstream) interface returned by **ITParticipant::EnumerateStreams**. The application must call **Release** on the **IEnumStream** interface to free resources associated with it.

## Requirements



| Requirement | Value |
|-------------------------|--------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                |
| Header<br/>       | <dl> <dt>Ipmsp.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>  |
| DLL<br/>          | <dl> <dt>Tapi3.dll</dt> </dl> |



## See also

<dl> <dt>

[**ITParticipant**](itparticipant.md)
</dt> <dt>

[**get\_Streams**](itparticipant-get-streams.md)
</dt> <dt>

[**IEnumStream**](/windows/desktop/api/tapi3if/nn-tapi3if-ienumstream)
</dt> </dl>

 

 





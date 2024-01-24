---
description: The get\_Streams method creates a collection of streams associated with the current participant.
ms.assetid: 9ab05b14-8ef8-4e7f-b598-05795011e35d
title: ITParticipant::get_Streams method (Ipmsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITParticipant::get\_Streams method

\[**get\_Streams** is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **get\_Streams** method creates a collection of streams associated with the current participant. This method is provided for Automation client applications, such as those written in Visual Basic. C and C++ applications must use the [**EnumerateStreams**](itparticipant-enumeratestreams.md) method.

## Syntax


```C++
HRESULT get_Streams(
  [out] VARIANT *pVariant
);
```



## Parameters

<dl> <dt>

*pVariant* \[out\]
</dt> <dd>

Pointer to **VARIANT** containing an [**ITCollection**](/windows/desktop/api/tapi3if/nn-tapi3if-itcollection) of [**ITStream**](/windows/win32/api/tapi3if/nn-tapi3if-itstream) interface pointers.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                         | Meaning                                                         |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                    |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | The *pVariant* parameter is not a valid pointer.<br/>     |



 

## Remarks

TAPI calls the **AddRef** method on the [**ITStream**](/windows/win32/api/tapi3if/nn-tapi3if-itstream) interface returned by **ITParticipant::get\_Streams**. The application must call **Release** on the **ITStream** interface to free resources associated with it.

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

[**EnumerateStreams**](itparticipant-enumeratestreams.md)
</dt> <dt>

[**IEnumStream**](/windows/desktop/api/tapi3if/nn-tapi3if-ienumstream)
</dt> <dt>

[**ITCollection**](/windows/desktop/api/tapi3if/nn-tapi3if-itcollection)
</dt> <dt>

[**ITStream**](/windows/win32/api/tapi3if/nn-tapi3if-itstream)
</dt> </dl>

 


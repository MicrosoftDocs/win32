---
description: The get\_LoopbackMode method gets the multicast loopback mode.
ms.assetid: 2499c108-f70b-4afe-aa2b-2376c95b84bd
title: IMulticastControl::get_LoopbackMode method (Confpriv.h)
ms.topic: reference
ms.date: 05/31/2018
---

# IMulticastControl::get\_LoopbackMode method

\[**get\_LoopbackMode** is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **get\_LoopbackMode** method gets the multicast loopback mode.

## Syntax


```C++
HRESULT get_LoopbackMode(
  [out] MULTICAST_LOOPBACK_MODE *pMode
);
```



## Parameters

<dl> <dt>

*pMode* \[out\]
</dt> <dd>

Pointer to the [**MULTICAST\_LOOPBACK\_MODE**](multicast-loopback-mode.md) descriptor of the current loopback mode.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                        | Meaning                                        |
|----------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Method succeeded.<br/>                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The *pMode* parameter is not valid.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Confpriv.h</dt> </dl> |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Tapi3.dll</dt> </dl>  |



## See also

<dl> <dt>

[**IMulticastControl**](imulticastcontrol.md)
</dt> </dl>

 

 





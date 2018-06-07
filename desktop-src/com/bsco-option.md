---
title: BSCO\_OPTION enumeration
description: Specifies the callback notifications that the client wants from the moniker.
ms.assetid: 82ca0285-5a03-40ab-b244-72e853e2a14a
keywords:
- BSCO_OPTION enumeration COM
topic_type:
- apiref
api_name:
- BSCO_OPTION
api_type:
- NA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# BSCO\_OPTION enumeration

Specifies the callback notifications that the client wants from the moniker. Simple clients of [**IMoniker::BindToStorage**](/windows/desktop/api/ObjIdl/nf-objidl-imoniker-bindtostorage) that want nothing but the data bits need specify only BSCO\_ONDATAAVAILABLE.

## Syntax


```C++
typedef enum  { 
  BSCO_ONSTARTBINDING     = 0x00000001,
  BSCO_GETPRIORITY        = 0x00000002,
  BSCO_ONLOWRESOURCE      = 0x00000004,
  BSCO_ONPROGRESS         = 0x00000008,
  BSCO_ONSTOPBINDING      = 0x00000010,
  BSCO_GETBINDINFO        = 0x00000020,
  BSCO_ONDATAAVAILABLE    = 0x00000040,
  BSCO_ONOBJECTAVAILABLE  = 0x00000080,
  BSCO_ALLONIBSC          = 0x000000FF,
  BSCO_ALLONIBDGSITE      = 0x0000001F
} BSCO_OPTION;
```



## Constants

<dl> <dt>

<span id="BSCO_ONSTARTBINDING"></span><span id="bsco_onstartbinding"></span>**BSCO\_ONSTARTBINDING**
</dt> <dd>

The client would like to receive the [**OnStartBinding**](75a6432d-d3c6-4010-85fe-355278d86cbb) callback.

</dd> <dt>

<span id="BSCO_GETPRIORITY"></span><span id="bsco_getpriority"></span>**BSCO\_GETPRIORITY**
</dt> <dd>

The client would like to receive the [**GetPriority**](22ebe288-6bed-45ed-9818-5097bc70b6b9) callback.

</dd> <dt>

<span id="BSCO_ONLOWRESOURCE"></span><span id="bsco_onlowresource"></span>**BSCO\_ONLOWRESOURCE**
</dt> <dd>

The client would like to receive the [**OnLowResource**](55977a98-9757-4697-bc4c-a4533fc55576) callback.

</dd> <dt>

<span id="BSCO_ONPROGRESS"></span><span id="bsco_onprogress"></span>**BSCO\_ONPROGRESS**
</dt> <dd>

The client would like to receive the [**OnProgress**](c6541dd3-8095-481a-a2d5-08acaba91aad) callback.

</dd> <dt>

<span id="BSCO_ONSTOPBINDING"></span><span id="bsco_onstopbinding"></span>**BSCO\_ONSTOPBINDING**
</dt> <dd>

The client would like to receive the [**OnStopBinding**](921b8c09-ca1d-41e5-91e2-7495fcbc539a) callback.

</dd> <dt>

<span id="BSCO_GETBINDINFO"></span><span id="bsco_getbindinfo"></span>**BSCO\_GETBINDINFO**
</dt> <dd>

The client would like to receive the [**GetBindInfo**](a402c6a2-bae3-4874-8fc9-67d04b67687e) callback.

</dd> <dt>

<span id="BSCO_ONDATAAVAILABLE"></span><span id="bsco_ondataavailable"></span>**BSCO\_ONDATAAVAILABLE**
</dt> <dd>

The client would like to receive the [**OnDataAvailable**](9755eda0-4d33-49e1-9bdd-f50a906e826f) callback.

</dd> <dt>

<span id="BSCO_ONOBJECTAVAILABLE"></span><span id="bsco_onobjectavailable"></span>**BSCO\_ONOBJECTAVAILABLE**
</dt> <dd>

The client would like to receive the [**OnObjectAvailable**](d225d7f0-69eb-4359-88a4-17c9ea9e7be4) callback.

</dd> <dt>

<span id="BSCO_ALLONIBSC"></span><span id="bsco_allonibsc"></span>**BSCO\_ALLONIBSC**
</dt> <dd>

The client would like to receive all callbacks.

</dd> <dt>

<span id="BSCO_ALLONIBDGSITE"></span><span id="bsco_allonibdgsite"></span>**BSCO\_ALLONIBDGSITE**
</dt> <dd>

The client would like to receive all callbacks.

</dd> </dl>

## Remarks

A client of a binding operation provides values from the **BSCO\_OPTION** enumeration when calling the [**RegisterBindStatusCallback**](https://www.bing.com/search?q=**RegisterBindStatusCallback**) function to register the client's [**IBindStatusCallback**](https://www.bing.com/search?q=**IBindStatusCallback**) interface.

## Requirements



|                                     |                                                            |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

[**IBindStatusCallback**](https://www.bing.com/search?q=**IBindStatusCallback**)
</dt> <dt>

[**RegisterBindStatusCallback**](https://www.bing.com/search?q=**RegisterBindStatusCallback**)
</dt> </dl>

 

 






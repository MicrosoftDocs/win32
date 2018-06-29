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
api_location: 
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

The client would like to receive the [**OnStartBinding**](https://www.bing.com/search?q=**OnStartBinding**) callback.

</dd> <dt>

<span id="BSCO_GETPRIORITY"></span><span id="bsco_getpriority"></span>**BSCO\_GETPRIORITY**
</dt> <dd>

The client would like to receive the [**GetPriority**](https://www.bing.com/search?q=**GetPriority**) callback.

</dd> <dt>

<span id="BSCO_ONLOWRESOURCE"></span><span id="bsco_onlowresource"></span>**BSCO\_ONLOWRESOURCE**
</dt> <dd>

The client would like to receive the [**OnLowResource**](https://www.bing.com/search?q=**OnLowResource**) callback.

</dd> <dt>

<span id="BSCO_ONPROGRESS"></span><span id="bsco_onprogress"></span>**BSCO\_ONPROGRESS**
</dt> <dd>

The client would like to receive the [**OnProgress**](https://www.bing.com/search?q=**OnProgress**) callback.

</dd> <dt>

<span id="BSCO_ONSTOPBINDING"></span><span id="bsco_onstopbinding"></span>**BSCO\_ONSTOPBINDING**
</dt> <dd>

The client would like to receive the [**OnStopBinding**](https://www.bing.com/search?q=**OnStopBinding**) callback.

</dd> <dt>

<span id="BSCO_GETBINDINFO"></span><span id="bsco_getbindinfo"></span>**BSCO\_GETBINDINFO**
</dt> <dd>

The client would like to receive the [**GetBindInfo**](https://www.bing.com/search?q=**GetBindInfo**) callback.

</dd> <dt>

<span id="BSCO_ONDATAAVAILABLE"></span><span id="bsco_ondataavailable"></span>**BSCO\_ONDATAAVAILABLE**
</dt> <dd>

The client would like to receive the [**OnDataAvailable**](https://www.bing.com/search?q=**OnDataAvailable**) callback.

</dd> <dt>

<span id="BSCO_ONOBJECTAVAILABLE"></span><span id="bsco_onobjectavailable"></span>**BSCO\_ONOBJECTAVAILABLE**
</dt> <dd>

The client would like to receive the [**OnObjectAvailable**](https://www.bing.com/search?q=**OnObjectAvailable**) callback.

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

 

 






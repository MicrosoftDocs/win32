---
description: "Learn more about: JetGetSessionParameter Function"
title: JetGetSessionParameter Function
TOCTitle: JetGetSessionParameter Function
ms:assetid: 36fbcc06-a72d-4bfb-976b-1b705487732a
ms:mtpsurl: https://msdn.microsoft.com/library/JJ835039(v=EXCHG.10)
ms:contentKeyID: 49894661
ms.date: 04/11/2016
ms.topic: reference
dev_langs:
- c++
api_name: 
- JetGetSessionParameter
topic_type: 
- apiref
- kbArticle
api_type: 
- DLLExport
api_location: 
- ESENT.DLL
ROBOTS: INDEX,FOLLOW

---

# JetGetSessionParameter Function


_**Applies to:** Windows | Windows Server_

The **JetGetSessionParameter** function reads the session parameter for the given session.

The **JetGetSessionParameter** function was introduced in the Windows 8 operating system.

``` c++
JET_ERR JET_API JetGetSessionParameter (
  __in_opt      JET_SESID sesid,
  __in          unsigned long sesparamid,
  __out_cap_post_count_(cbParamMax, *pcbParamActual)  void* pvParam,
  __in          unsigned long cbParamMax,
  __out_opt_    unsigned long pcbParamActual
);
```

### Parameters

*sesid*

The session to use for this call.

When specified, the specified instance is ignored and the instance associated with the session will be used.

*sesparamid*

The ID of the session parameter to set.

*pvParam*

Data in this session parameter.

*cbParamMax*

The maximum size of the data set in this session parameter.

*pcbParamActual*

The actual size of the data set in this session parameter.

### Return value

On success, the output buffer appropriate for the requested session parameter will be set to the value of that session parameter.

On failure, the state of the output buffers will be undefined.

#### Remarks

The session parameter is used for the lifetime of the session or until the value is reset.

#### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows 8.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2012.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Library</strong></p> | <p>Use ESENT.lib.</p> | 
| <p><strong>DLL</strong></p> | <p>Requires ESENT.dll.</p> | 



#### See also

[JET_API_PTR](./jet-api-ptr.md)  
[JET_ERR](./jet-err.md)  
[JET_INSTANCE](./jet-instance.md)  
[JET_SESID](./jet-sesid.md)  
[JetCreateInstance](./jetcreateinstance-function.md)  
[JetInit](./jetinit-function.md)  
[JetSetSystemParameter](./jetsetsystemparameter-function.md)  
[JetStopService](./jetstopservice-function.md)  
[System Parameters](./extensible-storage-engine-system-parameters.md)

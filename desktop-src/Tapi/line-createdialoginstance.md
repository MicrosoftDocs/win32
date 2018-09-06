---
Description: The TSPI LINE\_CREATEDIALOGINSTANCE message causes TAPI to create an association between the service provider and an instance of the TUISPI\_providerGenericDialog function executing in the context of the application.
ms.assetid: 5a7e34bc-1dc3-40c4-b07e-de5b88cbcd75
title: LINE_CREATEDIALOGINSTANCE message
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LINE\_CREATEDIALOGINSTANCE message

The TSPI **LINE\_CREATEDIALOGINSTANCE** message causes TAPI to create an association between the service provider and an instance of the [**TUISPI\_providerGenericDialog**](https://msdn.microsoft.com/en-us/library/ms725982(v=VS.85).aspx) function executing in the context of the application that invoked the asynchronous TSPI function identified by the *dwRequestID* parameter of the [**TUISPICREATEDIALOGINSTANCEPARAMS**](https://msdn.microsoft.com/en-us/library/ms725972(v=VS.85).aspx) structure pointed to by *lpTUISPICreateDialogInstanceParams*.


```C++
            
```



## Parameters

<dl> <dt>

*hProvider* 
</dt> <dd>

The ProviderHandle supplied to the service provider as a parameter to [**TSPI\_providerEnumDevices**](https://msdn.microsoft.com/en-us/library/ms725957(v=VS.85).aspx).

</dd> <dt>

*lpTUISPICreateDialogInstanceParams* 
</dt> <dd>

Pointer to a [**TUISPICREATEDIALOGINSTANCEPARAMS**](https://msdn.microsoft.com/en-us/library/ms725972(v=VS.85).aspx) structure.

</dd> </dl>

## Requirements



|                         |                                                                                   |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tspi.h</dt> </dl> |



## See also

<dl> <dt>

[**TSPI\_providerEnumDevices**](https://msdn.microsoft.com/en-us/library/ms725957(v=VS.85).aspx)
</dt> <dt>

[**TUISPICREATEDIALOGINSTANCEPARAMS**](https://msdn.microsoft.com/en-us/library/ms725972(v=VS.85).aspx)
</dt> </dl>

 

 





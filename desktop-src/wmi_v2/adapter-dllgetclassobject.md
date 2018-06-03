---
title: Adapter\_DllGetClassObject function
description: Retrieves an interface pointer that a provider can use to communicate with the specified class object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7ada3434-9274-46a7-b56d-f6281b732efe
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Adapter_DllGetClassObject function Windows Management Infrastructure (MI)
topic_type:
- apiref
api_name:
- Adapter_DllGetClassObject
api_location:
- WmiToMi.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Adapter\_DllGetClassObject function

Retrieves an interface pointer that a provider can use to communicate with the specified class object. The interface exposes the [**DllGetClassObject**](https://msdn.microsoft.com/library/windows/desktop/ms680760) function to the provider. The [**CoGetClassObject**](https://msdn.microsoft.com/library/windows/desktop/ms684007) function locates, and if necessary, dynamically loads the executable code that is required by this operation.

> \[!Important\]  
> This function is only used by generated code and should not be used by developers.

 

## Syntax


```C++
STDAPI Adapter_DllGetClassObject(
  _In_  CLSID          supportedClassIds,
  _In_  MI_MainFuncPtr fpMain,
  _In_  REFCLSID       rclsid,
  _In_  REFIID         riid,
  _Out_ PVOID          *ppv
);
```



## Parameters

<dl> <dt>

*supportedClassIds* \[in\]
</dt> <dd>

The **CLSID** that identifies the class object.

</dd> <dt>

*fpMain* \[in\]
</dt> <dd>

A pointer to the entry function that retrieves the class object.

</dd> <dt>

*rclsid* \[in\]
</dt> <dd>

The **CLSID** that identifies the class object.

</dd> <dt>

*riid* \[in\]
</dt> <dd>

A reference to the identifier of the interface that the provider is to use to communicate with the class object. Usually this value is set to **IID\_IClassFactory**, which is defined in the OLE headers as the interface identifier for [**IClassFactory**](https://msdn.microsoft.com/library/windows/desktop/ms694364). However, the other interface identifiers defined in the OLE header files are also valid. The interface identifiers are defined in the OLE header files as **IID\_*interfacename***, where *interfacename* is the name of the interface.

</dd> <dt>

*ppv* \[out\]
</dt> <dd>

The address of the pointer variable that receives the interface pointer requested in the riid *parameter*. If this function returns successfully, the *ppv* parameter will contain the requested interface pointer.

</dd> </dl>

## Return value

This function returns one of the following values:

<dl> <dt>


</dt> <dd>

CO\_E\_APPDIDNTREG

The executable was launched, but it did not register the class object (and it may have shut down).

</dd> <dt>


</dt> <dd>

CO\_E\_APPNOTFOUND

The executable file was not found (**CLSCTX\_LOCAL\_SERVER** only).

</dd> <dt>


</dt> <dd>

CO\_E\_DLLNOTFOUND

Either the in-process DLL or handler DLL was not found.

</dd> <dt>


</dt> <dd>

CO\_E\_ERRORINDLL

There is an error in the executable image.

</dd> <dt>


</dt> <dd>

E\_ACCESSDENIED

There was a general access failure on load.

</dd> <dt>


</dt> <dd>

E\_NOINTERFACE

Either the object pointed to by *ppv* does not support the interface identified by *riid*, or the [**QueryInterface**](https://msdn.microsoft.com/library/windows/desktop/ms682521) operation on the class object returned **E\_NOINTERFACE**.

</dd> <dt>


</dt> <dd>

REGDB\_E\_CLASSNOTREG

The **CLSID** is not properly registered. This error can also indicate that the *dwClsContext* value specified in the [**CoCreateInstance**](https://msdn.microsoft.com/library/windows/desktop/ms686615) or [**CoCreateInstanceEx**](https://msdn.microsoft.com/library/windows/desktop/ms680701) function is not in the registry.

</dd> <dt>


</dt> <dd>

REGDB\_E\_READREGDB

There was an error reading the registration database.

</dd> <dt>


</dt> <dd>

S\_OK

The location and connection to the specified class object was successful.

</dd> <dt>


</dt> <dd>

WBEM\_E\_INVALID\_PARAMETER

The value for *supportedClassId* is not included in *rclisid*.

</dd> <dt>


</dt> <dd>

WBEM\_E\_NOT\_SUPPORTED

The thread model of the DLL is registered as single-threaded apartment (STA), which is not supported by the MI framework.

</dd> <dt>


</dt> <dd>

WBEM\_E\_OUT\_OF\_MEMORY

There was not enough memory for the operation.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| DLL<br/>                      | <dl> <dt>WmiToMi.dll</dt> </dl> |



## See also

<dl> <dt>

[Adapter Functions](adapter-functions.md)
</dt> </dl>

 

 






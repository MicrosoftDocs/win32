---
description: Gets the interface ID of an agile reference to an object.
ms.assetid: 627A7EE4-CFEF-47F6-BA99-51BEB78C5D55
title: IAgileReference::Resolve method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAgileReference.Resolve
api_type: 
- COM
api_location: 
- objidl.h
---

# IAgileReference::Resolve method

Gets the interface ID of an agile reference to an object.

## Syntax


```C++
HRESULT Resolve(
  [in]          REFIID riid,
  [out, retval] void   **ppvObjectReference
);
```



## Parameters

<dl> <dt>

*riid* \[in\]
</dt> <dd>

The interface ID of the interface to be retrieved from the agile reference. It is not required to be the same as the registered interface.

</dd> <dt>

*ppvObjectReference* \[out, retval\]
</dt> <dd>

On successful completion, \**ppvObjectReference* is a pointer to the interface specified by *riid*.

</dd> </dl>

## Return value

This method can return one of these values.



| Return value                                                                              | Description                                                                    |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>          | The method completed successfully.<br/>                                  |
| <dl> <dt>E\_NOINTERFACE</dt> </dl> | The requested interface isn't implemented on the registered object.<br/> |



 

## Remarks

Call the [**RoGetAgileReference**](/windows/desktop/api/ComBaseApi/nf-combaseapi-rogetagilereference) function to create an agile reference to an object. Call the **Resolve** method to localize the object into the apartment in which **Resolve** is called.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps \| UWP apps\]<br/>            |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps \| UWP apps\]<br/> |



## See also

<dl> <dt>

[**IAgileReference**](/windows/desktop/api/objidl/nn-objidl-iagilereference)
</dt> <dt>

[**RoGetAgileReference**](/windows/desktop/api/ComBaseApi/nf-combaseapi-rogetagilereference)
</dt> </dl>

 

 





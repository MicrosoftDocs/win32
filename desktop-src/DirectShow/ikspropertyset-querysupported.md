---
description: The QuerySupported method determines whether an object supports a specified property set.
ms.assetid: eda0325c-dba4-4d9f-81e2-7fd67d5b9873
title: IKsPropertySet::QuerySupported method (Ks.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IKsPropertySet.QuerySupported
api_type: 
- COM
api_location: 
- Strmiids.lib
- Strmiids.dll
---

# IKsPropertySet::QuerySupported method

The `QuerySupported` method determines whether an object supports a specified property set.

## Syntax


```C++
HRESULT QuerySupported(
  [in]  REFGUID guidPropSet,
  [in]  DWORD   dwPropID,
  [out] DWORD   *pTypeSupport
);
```



## Parameters

<dl> <dt>

*guidPropSet* \[in\]
</dt> <dd>

Property set GUID.

</dd> <dt>

*dwPropID* \[in\]
</dt> <dd>

Identifier of the property within the property set.

</dd> <dt>

*pTypeSupport* \[out\]
</dt> <dd>

Pointer to a value in which to store flags indicating the support provided by the driver. Supported flags include the following.



| Value                    | Description                                                                                            |
|--------------------------|--------------------------------------------------------------------------------------------------------|
| KSPROPERTY\_SUPPORT\_GET | You can retrieve the property by calling the [**IKsPropertySet::Get**](ikspropertyset-get.md) method. |
| KSPROPERTY\_SUPPORT\_SET | You can change the property by calling [**IKsPropertySet::Set**](ikspropertyset-set.md).              |



 

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following.



| Return code                                                                                              | Description                                                                     |
|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                     | The specified property set and property ID combination is supported.<br/> |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>                | Property set is not supported.<br/>                                       |
| <dl> <dt>**E\_PROP\_ID\_UNSUPPORTED**</dt> </dl>  | Property ID is not supported for the specified property set.<br/>         |
| <dl> <dt>**E\_PROP\_SET\_UNSUPPORTED**</dt> </dl> | Property set is not supported.<br/>                                       |



 

## Remarks

> [!Note]  
> Another interface by this name exists in the dsound.h header file. The two interfaces are not compatible. The **IKsControl** interface, documented in the DirectShow DDK, is now the recommended interface for passing property sets between WDM drivers and user mode components.

 

You must include Ks.h before Ksproxy.h.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                             |
| Header<br/>                   | <dl> <dt>Ks.h; </dt> <dt>Ksproxy.h</dt> </dl> |
| Library<br/>                  | <dl> <dt>Strmiids.lib</dt> </dl>                                                          |



## See also

<dl> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> <dt>

[**IKsPropertySet Interface**](ikspropertyset.md)
</dt> <dt>

[Property Sets](property-sets.md)
</dt> </dl>

 

 





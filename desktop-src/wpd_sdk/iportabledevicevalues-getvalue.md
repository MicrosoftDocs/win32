---
description: The GetValue method retrieves a PROPVARIANT value specified by a key.
ms.assetid: 927844f5-8f57-4596-ae0d-c67b8011ca87
title: IPortableDeviceValues::GetValue method (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPortableDeviceValues.GetValue
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IPortableDeviceValues::GetValue method

The **GetValue** method retrieves a **PROPVARIANT** value specified by a key.

## Syntax


```C++
HRESULT GetValue(
  [in]  REFPROPERTYKEY key,
  [out] PROPVARIANT    *pValue
);
```



## Parameters

<dl> <dt>

*key* \[in\]
</dt> <dd>

A **REFPROPERTYKEY** key that specifies the item to retrieve.

</dd> <dt>

*pValue* \[out\]
</dt> <dd>

Pointer to the retrieved **PROPVARIANT** value. The caller must release the memory by calling **PropVariantClear** when done with it.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                                            | Description                                                          |
|------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                                   | The method succeeded.<br/>                                     |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_NOT\_FOUND)**</dt> </dl> | The property specified by *key* is not in the collection.<br/> |



 

## Remarks

When the VARTYPE for *pValue* is VT\_VECTOR or VT\_UI1, retrieving a **NULL** or zero-sized buffer is not supported. For example, neither pValue.caub.pElems = **NULL** nor pValue.caub.cElems = 0 are allowed.

This method can be used to retrieve a value of any type from the collection. However, if you know the value type in advance, use one of the specialized retrieval methods of this interface to avoid the overhead of working with PROPVARIANT values directly.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>PortableDeviceTypes.h</dt> </dl>   |
| Library<br/> | <dl> <dt>PortableDeviceGUIDs.lib</dt> </dl> |



## See also

<dl> <dt>

[**IPortableDeviceValues Interface**](iportabledevicevalues.md)
</dt> <dt>

[**IPortableDeviceValues::RemoveValue**](iportabledevicevalues-removevalue.md)
</dt> <dt>

[**IPortableDeviceValues::SetValue**](iportabledevicevalues-setvalue.md)
</dt> </dl>

 

 





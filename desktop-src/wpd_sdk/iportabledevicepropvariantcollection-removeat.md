---
description: IPortableDevicePropVariantCollection::RemoveAt method - The RemoveAt method removes the element stored at the location specified by the given index.
ms.assetid: cfee2454-5103-48ce-b9f7-1f76f5c18b6d
title: IPortableDevicePropVariantCollection::RemoveAt method (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPortableDevicePropVariantCollection.RemoveAt
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IPortableDevicePropVariantCollection::RemoveAt method

The **RemoveAt** method removes the element stored at the location specified by the given index.

## Syntax


```C++
HRESULT RemoveAt(
  [in] const DWORD dwIndex
);
```



## Parameters

<dl> <dt>

*dwIndex* \[in\]
</dt> <dd>

Specifies the index of the element to be removed.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                  | Description                                      |
|----------------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The method succeeded.<br/>                 |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The specified index was out of range.<br/> |



 

## Remarks

You must specify a zero-based index.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>PortableDeviceTypes.h</dt> </dl>   |
| Library<br/> | <dl> <dt>PortableDeviceGUIDs.lib</dt> </dl> |



## See also

<dl> <dt>

[**IPortableDevicePropVariantCollection Interface**](iportabledevicepropvariantcollection.md)
</dt> </dl>

 

 





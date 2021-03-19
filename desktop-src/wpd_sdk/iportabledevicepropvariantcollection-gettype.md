---
description: The GetType method retrieves the data type of the items in the collection.
ms.assetid: 2e389090-74ef-47af-9490-a4820d925246
title: IPortableDevicePropVariantCollection::GetType method (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPortableDevicePropVariantCollection.GetType
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IPortableDevicePropVariantCollection::GetType method

The **GetType** method retrieves the data type of the items in the collection.

## Syntax


```C++
HRESULT GetType(
  [out] VARTYPE *pvt
);
```



## Parameters

<dl> <dt>

*pvt* \[out\]
</dt> <dd>

A Platform SDK **VARTYPE** enumeration value that indicates the data type of all the items in the collection.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                               | Description                                          |
|-------------------------------------------------------------------------------------------|------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The method succeeded.<br/>                     |
| <dl> <dt>**E\_POINTER**</dt> </dl> | A required pointer argument was **NULL**.<br/> |



 

## Remarks

All items that are stored in an **IPortableDevicePropVariantCollection** are the same type.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>PortableDeviceTypes.h</dt> </dl>   |
| Library<br/> | <dl> <dt>PortableDeviceGUIDs.lib</dt> </dl> |



## See also

<dl> <dt>

[**IPortableDevicePropVariantCollection Interface**](iportabledevicepropvariantcollection.md)
</dt> </dl>

 

 





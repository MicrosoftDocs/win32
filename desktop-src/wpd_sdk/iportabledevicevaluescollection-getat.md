---
description: The GetAt method retrieves an item from the collection by a zero-based index.
ms.assetid: b219b052-a74b-466a-a2ee-d2e9c466f393
title: IPortableDeviceValuesCollection::GetAt method (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPortableDeviceValuesCollection.GetAt
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IPortableDeviceValuesCollection::GetAt method

The **GetAt** method retrieves an item from the collection by a zero-based index.

## Syntax


```C++
HRESULT GetAt(
  [in]  const DWORD                 dwIndex,
  [out]       IPortableDeviceValues **ppValues
);
```



## Parameters

<dl> <dt>

*dwIndex* \[in\]
</dt> <dd>

**DWORD** that specifies a zero-based index in the collection.

</dd> <dt>

*ppValues* \[out\]
</dt> <dd>

Address of a variable that receives a pointer to an [**IPortableDeviceValues**](iportabledevicevalues.md) interface from the collection. The caller is responsible for calling **Release** on this interface when done with it.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                  | Description                                                                      |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The method succeeded.<br/>                                                 |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The zero-based index that was passed in was out of range.<br/>             |
| <dl> <dt>**E\_POINTER**</dt> </dl>    | A required pointer argument was **NULL**.<br/>                             |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl> | The collection contains a **NULL** **IPortableDeviceValues** pointer.<br/> |



 

## Remarks

Any changes that are made to values in the retrieved interface will be made to the version stored in the collection.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>PortableDeviceTypes.h</dt> </dl>   |
| Library<br/> | <dl> <dt>PortableDeviceGUIDs.lib</dt> </dl> |



## See also

<dl> <dt>

[**IPortableDeviceValuesCollection Interface**](iportabledevicevaluescollection.md)
</dt> </dl>

 

 





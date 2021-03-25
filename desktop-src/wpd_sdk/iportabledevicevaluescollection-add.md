---
description: The Add method adds an item to the collection.
ms.assetid: 3b06abc4-f0ab-4b02-b3a7-360615f86a2a
title: IPortableDeviceValuesCollection::Add method (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPortableDeviceValuesCollection.Add
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IPortableDeviceValuesCollection::Add method

The **Add** method adds an item to the collection.

## Syntax


```C++
HRESULT Add(
  [in] IPortableDeviceValues *pValues
);
```



## Parameters

<dl> <dt>

*pValues* \[in\]
</dt> <dd>

Pointer to an **IPortableDeviceValues** interface to add to the collection. The interface is not actually copied, but **AddRef** is called on it.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                   | Description                                                                         |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | The method succeeded.<br/>                                                    |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | There is not enough memory available to add the value to the collection.<br/> |



 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>PortableDeviceTypes.h</dt> </dl>   |
| Library<br/> | <dl> <dt>PortableDeviceGUIDs.lib</dt> </dl> |



## See also

<dl> <dt>

[**IPortableDeviceValuesCollection Interface**](iportabledevicevaluescollection.md)
</dt> </dl>

 

 





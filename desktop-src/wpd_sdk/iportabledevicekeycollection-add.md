---
description: The Add method adds a property key to the collection.
ms.assetid: 640ef1c4-2843-48dd-a30a-9a2ef9de35b9
title: IPortableDeviceKeyCollection::Add method (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPortableDeviceKeyCollection.Add
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IPortableDeviceKeyCollection::Add method

The **Add** method adds a property key to the collection.

## Syntax


```C++
HRESULT Add(
  [in] REFPROPERTYKEY Key
);
```



## Parameters

<dl> <dt>

*Key* \[in\]
</dt> <dd>

A **REFPROPERTYKEY** to add to the collection. This method copies the key to the collection, so you can release the local variable after calling this method.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                   | Description                                                                       |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | The method succeeded.<br/>                                                  |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | There is not enough memory available to add the key to the collection.<br/> |



 

## Examples

For an example of how to use this method, see [Retrieving Properties for a Single Object](retrieving-properties-for-a-single-object.md).

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>PortableDeviceTypes.h</dt> </dl>   |
| Library<br/> | <dl> <dt>PortableDeviceGUIDs.lib</dt> </dl> |



## See also

<dl> <dt>

[**IPortableDeviceKeyCollection Interface**](iportabledevicekeycollection.md)
</dt> <dt>

[Retrieving Content-Object Properties](retrieving-content-object-properties.md)
</dt> <dt>

[Retrieving Properties for a Single Object](retrieving-properties-for-a-single-object.md)
</dt> <dt>

[Retrieving the Rendering Capabilities Supported by a Device](retrieving-the-rendering-capabilities-supported-by-a-device.md)
</dt> </dl>

 

 





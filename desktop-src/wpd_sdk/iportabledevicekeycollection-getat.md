---
description: The GetAt method retrieves a PROPERTYKEY from the collection by index.
ms.assetid: 9a3c5c28-39b4-4d53-a8d7-0f5a0d4d89ad
title: IPortableDeviceKeyCollection::GetAt method (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPortableDeviceKeyCollection.GetAt
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IPortableDeviceKeyCollection::GetAt method

The **GetAt** method retrieves a **PROPERTYKEY** from the collection by index.

## Syntax


```C++
HRESULT GetAt(
  [in]  const DWORD       dwIndex,
  [out]       PROPERTYKEY *pKey
);
```



## Parameters

<dl> <dt>

*dwIndex* \[in\]
</dt> <dd>

**DWORD** that contains the index of the key to be retrieved.

</dd> <dt>

*pKey* \[out\]
</dt> <dd>

Pointer to a **PROPERTYKEY** object.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                  | Description                                          |
|----------------------------------------------------------------------------------------------|------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The method succeeded.<br/>                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The index passed in was out of range.<br/>     |
| <dl> <dt>**E\_POINTER**</dt> </dl>    | A required pointer argument was **NULL**.<br/> |



 

## Examples

For an example of how to use this method, see [Retrieving Supported Service Events](retrieving-supported-events.md).

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>PortableDeviceTypes.h</dt> </dl>   |
| Library<br/> | <dl> <dt>PortableDeviceGUIDs.lib</dt> </dl> |



## See also

<dl> <dt>

[**IPortableDeviceKeyCollection Interface**](iportabledevicekeycollection.md)
</dt> <dt>

[Retrieving Supported Service Events](retrieving-supported-events.md)
</dt> <dt>

[Retrieving Supported Service Methods](retrieving-supported-methods.md)
</dt> </dl>

 

 





---
description: IPortableDeviceValuesCollection::GetCount method - The GetCount method retrieves the number of items in the collection.
ms.assetid: c7b80a54-9e74-42d9-9155-cfcb2a92d324
title: IPortableDeviceValuesCollection::GetCount method (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPortableDeviceValuesCollection.GetCount
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IPortableDeviceValuesCollection::GetCount method

The **GetCount** method retrieves the number of items in the collection.

## Syntax


```C++
HRESULT GetCount(
  [in] DWORD *pcElems
);
```



## Parameters

<dl> <dt>

*pcElems* \[in\]
</dt> <dd>

Pointer to a **DWORD** that contains the number of **IPortableDeviceValues** interfaces in the collection.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                               | Description                                          |
|-------------------------------------------------------------------------------------------|------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The method succeeded.<br/>                     |
| <dl> <dt>**E\_POINTER**</dt> </dl> | A required pointer argument was **NULL**.<br/> |



 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>PortableDeviceTypes.h</dt> </dl>   |
| Library<br/> | <dl> <dt>PortableDeviceGUIDs.lib</dt> </dl> |



## See also

<dl> <dt>

[**IPortableDeviceValuesCollection Interface**](iportabledevicevaluescollection.md)
</dt> </dl>

 

 





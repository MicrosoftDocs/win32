---
description: IPortableDeviceValues::GetCount method - The GetCount method retrieves the number of items in the collection.
ms.assetid: 89266483-4211-43d2-a306-68c70f1e7026
title: IPortableDeviceValues::GetCount method (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPortableDeviceValues.GetCount
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IPortableDeviceValues::GetCount method

The **GetCount** method retrieves the number of items in the collection.

## Syntax


```C++
HRESULT GetCount(
  [in] DWORD *pcelt
);
```



## Parameters

<dl> <dt>

*pcelt* \[in\]
</dt> <dd>

Pointer to a **DWORD** that contains the number of items in the collection.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>PortableDeviceTypes.h</dt> </dl>   |
| Library<br/> | <dl> <dt>PortableDeviceGUIDs.lib</dt> </dl> |



## See also

<dl> <dt>

[**IPortableDeviceValues Interface**](iportabledevicevalues.md)
</dt> </dl>

 

 





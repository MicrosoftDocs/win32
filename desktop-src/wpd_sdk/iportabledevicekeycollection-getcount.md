---
Description: 'The GetCount method retrieves the number of keys in this collection.'
ms.assetid: '963f514e-3e0f-4334-ac29-6de7cc8aa336'
title: 'IPortableDeviceKeyCollection::GetCount method'
---

# IPortableDeviceKeyCollection::GetCount method

The **GetCount** method retrieves the number of keys in this collection.

## Syntax


```C++
HRESULT GetCount(
  [in] DWORD *pcElems
);
```



## Parameters

<dl> <dt>

*pcElems* \[in\]
</dt> <dd>

Pointer to a **DWORD** that contains the number of keys in the collection.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                               | Description                                          |
|-------------------------------------------------------------------------------------------|------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The method succeeded.<br/>                     |
| <dl> <dt>**E\_POINTER**</dt> </dl> | A required pointer argument was **NULL**.<br/> |



 

## Examples

For an example of how to use this method, see [Retrieving Supported Service Events](retrieving-supported-events.md).

## Requirements



|                    |                                                                                                    |
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

 

 





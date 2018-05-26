---
Description: The GetIPortableDeviceKeyCollectionValue method retrieves an IPortableDeviceKeyCollection value (type VT\_UNKNOWN) specified by a key.
ms.assetid: 131c8e05-9224-4db4-bdf6-0fd9c563e049
title: IPortableDeviceValuesGetIPortableDeviceKeyCollectionValue method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPortableDeviceValues::GetIPortableDeviceKeyCollectionValue method

The **GetIPortableDeviceKeyCollectionValue** method retrieves an **IPortableDeviceKeyCollection** value (type VT\_UNKNOWN) specified by a key.

## Syntax


```C++
HRESULT GetIPortableDeviceKeyCollectionValue(
  [in]  REFPROPERTYKEY               key,
  [out] IPortableDeviceKeyCollection **ppValue
);
```



## Parameters

<dl> <dt>

*key* \[in\]
</dt> <dd>

A **REFPROPERTYKEY** key that specifies the item to retrieve.

</dd> <dt>

*ppValue* \[out\]
</dt> <dd>

Pointer to the retrieved [**IPortableDeviceKeyCollection**](iportabledevicekeycollection.md) interface pointer. The caller is responsible for calling **Release** on the retrieved interface.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                                            | Description                                                                                      |
|------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                                   | The method succeeded.<br/>                                                                 |
| <dl> <dt>**DISP\_E\_TYPEMISMATCH**</dt> </dl>                   | The property specified by *key* is not an **IPortableDeviceKeyCollection** interface.<br/> |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_NOT\_FOUND)**</dt> </dl> | The property specified by *key* is not in the collection.<br/>                             |



 

## Examples

For an example of how to use this method, see [Retrieving Supported Service Events](retrieving-supported-events.md).

## Requirements



|                    |                                                                                                    |
|--------------------|----------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>PortableDeviceTypes.h</dt> </dl>   |
| Library<br/> | <dl> <dt>PortableDeviceGUIDs.lib</dt> </dl> |



## See also

<dl> <dt>

[**IPortableDeviceValues Interface**](iportabledevicevalues.md)
</dt> <dt>

[**IPortableDeviceValues::SetIPortableDeviceKeyCollectionValue**](iportabledevicevalues-setiportabledevicekeycollectionvalue.md)
</dt> <dt>

[Retrieving Supported Service Events](retrieving-supported-events.md)
</dt> <dt>

[Retrieving Supported Service Methods](retrieving-supported-methods.md)
</dt> </dl>

 

 





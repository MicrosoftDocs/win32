---
Description: The RemoveValue method removes an item from the collection.
ms.assetid: 864c23ee-5a4e-4e06-add0-f6aef5562430
title: IPortableDeviceValuesRemoveValue method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPortableDeviceValues::RemoveValue method

The **RemoveValue** method removes an item from the collection.

## Syntax


```C++
HRESULT RemoveValue(
  [in] REFPROPERTYKEY key
);
```



## Parameters

<dl> <dt>

*key* \[in\]
</dt> <dd>

A **REFPROPERTYKEY** that specifies the item to remove.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Requirements



|                    |                                                                                                    |
|--------------------|----------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>PortableDeviceTypes.h</dt> </dl>   |
| Library<br/> | <dl> <dt>PortableDeviceGUIDs.lib</dt> </dl> |



## See also

<dl> <dt>

[**IPortableDeviceValues Interface**](iportabledevicevalues.md)
</dt> <dt>

[**IPortableDeviceValues::GetValue**](iportabledevicevalues-getvalue.md)
</dt> <dt>

[**IPortableDeviceValues::SetValue**](iportabledevicevalues-setvalue.md)
</dt> </dl>

 

 





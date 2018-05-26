---
Description: The SetUnsignedLargeIntegerValue method adds a new ULONGLONG value (type VT\_UI8) or overwrites an existing one.
ms.assetid: 64874b86-7bf1-407a-8fff-a2c07c22f0cb
title: IPortableDeviceValuesSetUnsignedLargeIntegerValue method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPortableDeviceValues::SetUnsignedLargeIntegerValue method

The **SetUnsignedLargeIntegerValue** method adds a new **ULONGLONG** value (type VT\_UI8) or overwrites an existing one.

## Syntax


```C++
HRESULT SetUnsignedLargeIntegerValue(
  [in]       REFPROPERTYKEY key,
  [in] const ULONGLONG      Value
);
```



## Parameters

<dl> <dt>

*key* \[in\]
</dt> <dd>

A **REFPROPERTYKEY** that specifies the item to create or overwrite.

</dd> <dt>

*Value* \[in\]
</dt> <dd>

A **ULONGLONG** that specifies the new value.

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

[Adding a Resource to an Object](adding-a-resource-to-an-object.md)
</dt> <dt>

[**IPortableDeviceValues Interface**](iportabledevicevalues.md)
</dt> <dt>

[**IPortableDeviceValues::GetUnsignedLargeIntegerValue**](iportabledevicevalues-getunsignedlargeintegervalue.md)
</dt> </dl>

 

 





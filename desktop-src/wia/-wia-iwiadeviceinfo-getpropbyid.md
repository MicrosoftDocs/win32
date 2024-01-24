---
description: The GetPropById method of the DeviceInfo object uses a device property's ID to return its value.
ms.assetid: 9c68e6af-446c-4750-89e6-70862b23b296
title: DeviceInfo.GetPropById method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DeviceInfo.GetPropById
api_type: 
- COM
api_location: 
- Wiascr.dll
---

# DeviceInfo.GetPropById method

The **GetPropById** method of the [**DeviceInfo**](-wia-deviceinfo.md) object uses a device property's ID to return its value.

## Syntax


```JScript
retVal = DeviceInfo.GetPropById(
  Id
)
```



## Parameters

<dl> <dt>

*Id* \[in\]
</dt> <dd>

Type: **[WiaDeviceInfoPropertyId](-wia-wiadeviceinfopropertyid.md)**

Specifies the ID of the property.

</dd> </dl>

## Return value

Type: **VARIANT**

This method returns the value of the property specified by *Id*.

## Remarks

Use this method to find the value of a device property from its ID. For a list of property IDs, see [WIA Property Constant Definitions](-wia-wia-property-constant-definitions.md). For information about Windows Image Acquisition (WIA) properties themselves, see [WIA Property Constants](-wia-wia-property-constants.md).

For Microsoft Visual Basic applications, add a reference to "Windows Image Acquisition 1.01 Type Library". This following constants defined in that file are valid for this method:

``` syntax
const DeviceID = 2
const Manufacturer = 3
const Description = 4
const Type = 5
const Port = 6
const Name = 7
const Server = 8
const RemoteDevID = 9
const UIClassID = 10
```

## Examples

The following example demonstrates the use of the **GetPropById** method to retrieve a property value.


```JScript
<SCRIPT LANGUAGE="VBScript">
const WIA_DIP_DEV_TYPE = 5
Dim objWia
Dim objDeviceInfoCollection
Dim objDeviceInfo
Dim PropValue
 
Set objWIA = CreateObject("Wia.Script")
 
Set objDeviceInfoCollection = objWia.Devices
 
For Each objDeviceInfo In objDeviceInfoCollection
    PropValue = objDeviceInfo.GetPropById(WIA_DIP_DEV_TYPE)
Next
</SCRIPT>
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Wiascr.dll (version 4.90 or later)</dt> </dl> |



 

 





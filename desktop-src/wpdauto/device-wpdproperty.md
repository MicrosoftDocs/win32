---
title: Device.WpdProperty property
description: The WpdProperty gets or sets the value of a device property.
ms.assetid: 3351e16c-dce2-465e-b9cc-01f0df81118b
keywords:
- WpdProperty property WPD Automation
- WpdProperty property WPD Automation , Device object
- Device object WPD Automation , WpdProperty property
topic_type:
- apiref
api_name:
- Device.WpdProperty
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Device.WpdProperty property

The **WpdProperty** gets or sets the value of a device property.

This property is read/write.

## Syntax


```JScript
strWpdProperty = Device.WpdProperty
Device.WpdProperty = strWpdProperty
```



## Property value

String that is the name of a property on the device.

## Remarks

The following table shows the mapping between WPD PROPERTYKEYs and their equivalent WPD Automation names. The **Device.WpdProperty** property uses the WPD Automation property name on the right that corresponds to a WPD PROPERTYKEY on the left. For example, the WPD-defined property WPD\_DEVICE\_MANUFACTURER is accessed by using the corresponding WPD Automation property name, like this: `deviceObject.DeviceManufacturer`

For a complete list of WPD PROPERTYKEYs and their corresponding WPD Automation names, see [**Names for WPD PROPERTYKEYs**](names-for-wpd-propertykeys.md).



| WPD PROPERTYKEY                        | WPD Automation Name         |
|----------------------------------------|-----------------------------|
| WPD\_OBJECT\_ID                        | ObjectId                    |
| WPD\_OBJECT\_NAME                      | ObjectName                  |
| WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID    | ObjectPersistentUniqueId    |
| WPD\_OBJECT\_FORMAT                    | ObjectFormat                |
| WPD\_FUNCTIONAL\_OBJECT\_CATEGORY      | FunctionalObjectCategory    |
| WPD\_DEVICE\_FIRMWARE\_VERSION         | DeviceFirmwareVersion       |
| WPD\_DEVICE\_MANUFACTURER              | DeviceManufacturer          |
| WPD\_DEVICE\_MODEL                     | DeviceModel                 |
| WPD\_DEVICE\_SERIAL\_NUMBER            | DeviceSerialNumber          |
| WPD\_DEVICE\_POWER\_LEVEL              | DevicePowerLevel            |
| WPD\_DEVICE\_POWER\_SOURCE             | DevicePowerSource           |
| WPD\_DEVICE\_PROTOCOL                  | DeviceProtocol              |
| WPD\_DEVICE\_SUPPORTS\_NON\_CONSUMABLE | DeviceSupportsNonConsumable |
| WPD\_DEVICE\_FRIENDLY\_NAME            | DeviceFriendlyName          |
| WPD\_DEVICE\_TYPE                      | DeviceType                  |
| WPD\_DEVICE\_NETWORK\_IDENTIFIER       | DeviceNetworkIdentifier     |



 

## Examples

The following JScript example uses ***WpdProperty*** to obtain the name, model, and manufacturer of the device.


```JScript
var name = deviceObject.ObjectName;
var manufacturer = deviceObject.DeviceManufacturer;
var model = deviceObject.DeviceModel;
```



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Device Object**](device-object.md)
</dt> </dl>

 

 






---
title: Assigning and Getting Object Properties
description: The main objects in the WPD Automation object model are the Device object, the Service object and the Storage object.
ms.assetid: 'c8b56bc1-c25d-4cf0-92c7-bad2fb7df52c'
---

# Assigning and Getting Object Properties

The main objects in the WPD Automation object model are the [**Device**](device-object.md) object, the [**Service**](service-object.md) object and the [**Storage**](storage-object.md) object. These objects provide access to the full set of properties that have been defined for the particular device, service, or storage that they represent.

The following table shows the mapping between WPD PROPERTYKEYs and the equivalent WPD Automation names for the Device object properties. For example, the WPD-defined property WPD\_DEVICE\_MANUFACTURER is accessed by using the corresponding WPD Automation property name: `deviceObject.DeviceManufacturer`

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



 

## Assigning and Getting Object Properties

The following HTML and JScript example demonstrates how to get the property values of a device and display them. In this example, deviceObject represents a WPD Device object injected into the scripting environment through the command **window.external**. The Device object properties **DeviceFriendlyName**, **DeviceManufacturer**, **DeviceModel**, and **DeviceFirmwareVersion** are all WPD Automation names that correspond to WPD PROPERTYKEYs.


```JScript
<html>
<head>
<script language="jscript" type="text/jscript">    

function GetDeviceProperties()
{
    var deviceObject = window.external;

    nameDiv.childNodes[0].nodeValue = deviceObject.DeviceFriendlyName;
    manufacturerDiv.childNodes[0].nodeValue = deviceObject.DeviceManufacturer;
    modelDiv.childNodes[0].nodeValue = deviceObject.DeviceModel;
    firmwareDiv.childNodes[0].nodeValue = deviceObject.DeviceFirmwareVersion;
}   
</script>

</head>
<body >
Device Name = <div id="nameDiv">?</div>
Device Manufacturer = <div id="manufacturerDiv">?</div>
Device Model = <div id="modelDiv">?</div>
Firmware = <div id="firmwareDiv">?</div>
</body>
</html>
```



## Assigning and Getting Binary Array Properties

Some object properties may contain binary arrays in which each element of the array represents a byte. The array supports a length property that returns the number of elements (bytes) in the array. It also supports a zero-based numeric index that can be used to get or set bytes in the array. Setting a particular byte modifies the array, but does not modify the binary property.

To update a binary property on an object, assign the array to the object's property, as shown in the following example.


```JScript
wpdObject.SomeWritableBinaryProperty = updatedArray;
```



The following JScript example shows how to get and set a binary array as an object property.


```JScript
// Getting a binary array as an object property.
var binaryArray = wpdObject.SomeBinaryProperty;
var strBytes = "";

for (i=0; i < binaryArray.length; i++)
{
    strBytes += binaryArray [i];
}

// Setting a binary array as an object property.
var newArray = new Array();

for (i=0; i < 10; i++)
{
    newArray[i] = i;
}

wpdObject.SomeWritableBinaryProperty = newArray;
```



## Further Examples

For further examples of assigning and getting object properties, see the reference pages for [**Device.wpdProperty**](device-wpdproperty.md), [**Service.wpdProperty**](service-serviceproperty.md), [**Service.AbstractServices**](service-abstractservices.md), [**Service.ServiceProperty**](service-serviceproperty.md), and [**Storage.WpdProperty**](storage-wpdproperty.md).

## Related topics

<dl> <dt>

[**Device Object**](device-object.md)
</dt> <dt>

[**Service Object**](service-object.md)
</dt> <dt>

[**Storage Object**](storage-object.md)
</dt> <dt>

[**WPDObject**](wpdobject.md)
</dt> <dt>

[WPD Automation Programming Guide](wpd-automation-programming-guide.md)
</dt> </dl>

 

 





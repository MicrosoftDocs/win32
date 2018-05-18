---
title: Device.GetServicesByType method
description: The GetServicesByType method returns a collection of services for the specified service type.
ms.assetid: 'b6f9f5bc-70f7-4f62-a817-828a2b7cf758'
keywords: ["GetServicesByType method WPD Automation", "GetServicesByType method WPD Automation , Device object", "Device object WPD Automation , GetServicesByType method"]
topic_type:
- apiref
api_name:
- Device.GetServicesByType
api_type:
- COM
---

# Device.GetServicesByType method

The **GetServicesByType** method returns a collection of services for the specified service type.

## Syntax


```JScript
retVal = Device.GetServicesByType(
  ServiceTypeGUID
)
```



## Parameters

<dl> <dt>

*ServiceTypeGUID* 
</dt> <dd>

GUID in string form that uniquely identifies the service type. The format of the string must be "{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}".

</dd> </dl>

## Return value

Returns a **servicesCollection** object that contains all of the available services for the specified service type.

## Remarks

For a full list of service type GUIDs, download the [Windows Portable Device Enabling Kit](http://go.microsoft.com/fwlink/p/?linkid=144353).

## Examples

The following JScript example uses the **GetServicesByType** method to retrieve a collection of "Contacts" services on a device, and then enumerates them.


```JScript
// Retrieve a collection of Contacts services by using a ServiceTypeGUID.        
var contactsServices = deviceObject.GetServicesByType("{D0EACE0E-707D-4106-8D38-4F60E6A9F8E}");

// Enumerate all of the Contacts services.
for (i=0; i < contactsServices.Count; i++)
{
    var aContactsService = contactsServices[i];
}
```



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Device Object**](device-object.md)
</dt> <dt>

[**servicesCollection Object**](servicescollection-object.md)
</dt> </dl>

 

 






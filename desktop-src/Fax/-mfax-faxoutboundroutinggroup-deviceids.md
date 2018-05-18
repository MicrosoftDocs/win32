---
Description: 'The DeviceIds property retrieves the ordered collection of device IDs that participate in the outbound routing group. The order of the devices in the collection determines the relative order in which available devices send outgoing transmissions.'
ms.assetid: '46046834-2098-49b5-9514-b87356fcc4cb'
title: 'FaxOutboundRoutingGroup.DeviceIds property'
---

# FaxOutboundRoutingGroup.DeviceIds property

The **DeviceIds** property retrieves the ordered collection of device IDs that participate in the outbound routing group. The order of the devices in the collection determines the relative order in which available devices send outgoing transmissions.

This property is read-only.

## Syntax


```VB
Property DeviceIds As FaxDeviceIds
```



## Property value

A [**FaxDeviceIds**](-mfax-faxdeviceids.md) object.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-managing-outbound-routing-groups.md)
</dt> <dt>

[**FaxOutboundRoutingGroup**](-mfax-faxoutboundroutinggroup.md)
</dt> <dt>

[**IFaxOutboundRoutingGroup**](-mfax-faxoutboundroutinggroup-cpp.md)
</dt> </dl>

 

 





---
Description: The SetOrder method changes the order of a device in the ordered FaxDeviceIds collection.
ms.assetid: 02b4bc41-7c7c-4c4d-a2dc-e86fec6aaa19
title: FaxDeviceIds.SetOrder method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FaxDeviceIds.SetOrder method

The **SetOrder** method changes the order of a device in the ordered [**FaxDeviceIds**](-mfax-faxdeviceids.md) collection.

## Syntax


```VB
FaxDeviceIds.SetOrder( _
  ByVal lDeviceId As Long, _
  ByVal lNewOrder As Long _
) As Long
```



## Parameters

<dl> <dt>

*lDeviceId* \[in\]
</dt> <dd>

Type: **Long**

Specifies the device ID of the device whose order you want to change.

</dd> <dt>

*lNewOrder* \[in\]
</dt> <dd>

Type: **Long**

Specifies the new position of the device in the order.

</dd> </dl>

## Remarks

You identify the device with its device ID, and then choose a new place for it in the order. If you move the device closer to the top of the order, the devices below that position in the order will drop down to accommodate the change. If you move the device closer to the bottom of the order, the devices above that position in the order will move up to fill the gap caused by the change.

In a fax device group, the relative order of the devices within the group is significant. When the fax service initiates an outgoing job, it attempts to select the first fax device in the device group. If that device is not available, the service selects the next available device that follows in rank order, and so on. For more information, see [Fax Device Groups](-mfax-fax-device-groups.md).

To use this method, a user must have the [****farMANAGE\_CONFIG****](/previous-versions/windows/desktop/api/FaxComex/ne-faxcomex-fax_access_rights_enum) access right.

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

[**FaxDeviceIds**](-mfax-faxdeviceids.md)
</dt> <dt>

[**IFaxDeviceIds**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxdeviceids)
</dt> </dl>

 

 





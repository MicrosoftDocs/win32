---
Description: 'The Add method adds a fax device to the FaxDeviceIds collection, using the device''s ID.'
ms.assetid: '22cd030d-1444-4605-8935-cd19d9392720'
title: 'FaxDeviceIds.Add method'
---

# FaxDeviceIds.Add method

The **Add** method adds a fax device to the [**FaxDeviceIds**](-mfax-faxdeviceids.md) collection, using the device's ID.

## Syntax


```VB
FaxDeviceIds.Add( _
  ByVal lDeviceId As Long _
) As Long
```



## Parameters

<dl> <dt>

*lDeviceId* \[in\]
</dt> <dd>

Type: **Long**

A **Long** value that specifies the ID of the fax device to add to the collection.

</dd> </dl>

## Remarks

This method can also return remote procedure call (RPC) return values. For more information, see [RPC Return Values](http://msdn.microsoft.com/library/en-us/rpc/rpc/rpc_return_values.asp).

> [!Note]  
> You cannot add devices to the special **All Devices** routing group. Also, you can only add valid device IDs. You can obtain the valid ID of a device in the [**FaxDeviceIds**](-mfax-faxdeviceids.md) collection through the [**Id**](-mfax-faxdevice-id-vb.md) property.

 

To use this method, a user must have the [****farMANAGE\_CONFIG****](-mfax-fax-access-rights-enum.md) access right.

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

[**IFaxDeviceIds**](-mfax-faxdeviceids-cpp.md)
</dt> </dl>

 

 





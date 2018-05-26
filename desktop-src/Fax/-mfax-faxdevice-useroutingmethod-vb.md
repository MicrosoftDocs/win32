---
Description: The UseRoutingMethod method adds an inbound fax routing method to or removes a fax routing method (FaxInboundRoutingMethod) from the list of routing methods associated with the fax device.
ms.assetid: 1ad0f032-3410-47d0-a197-fa1330552173
title: FaxDevice.UseRoutingMethod method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxDevice.UseRoutingMethod method

The **UseRoutingMethod** method adds an inbound fax routing method to or removes a fax routing method ([**FaxInboundRoutingMethod**](-mfax-faxinboundroutingmethod.md)) from the list of routing methods associated with the fax device.

## Syntax


```VB
FaxDevice.UseRoutingMethod( _
  ByVal bstrMethodGUID As String, _
  ByVal bUse As Boolean _
) As Long
```



## Parameters

<dl> <dt>

*bstrMethodGUID* \[in\]
</dt> <dd>

Type: **String**

Specifies a null-terminated string that uniquely identifies the fax routing method to add or remove.

</dd> <dt>

*bUse* \[in\]
</dt> <dd>

Type: **Boolean**

Specifies a Boolean value. If this parameter is equal to **True**, the method adds the fax routing method to the list of inbound methods associated with the fax device. If you set this parameter to **False**, the method removes the routing method from the list.

</dd> </dl>

## Remarks

To use this method, a user must have the [****farMANAGE\_CONFIG****](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access right.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[Visual Basic Example](-mfax-managing-the-fax-device-collection.md)
</dt> <dt>

[**FaxDevice**](-mfax-faxdevice.md)
</dt> <dt>

[**IFaxDevice**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxdevice?branch=master)
</dt> </dl>

 

 





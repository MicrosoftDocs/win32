---
title: MSFT\_TargetPortal class
description: Represents a target portal.
ms.assetid: 27412123-730E-4AD4-9899-049CB9528CCB
keywords:
- MSFT_TargetPortal class Windows Storage Management API
- MSFT_TargetPortal class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_TargetPortal
- MSFT_TargetPortal.IPv4Address
- MSFT_TargetPortal.IPv6Address
- MSFT_TargetPortal.SubnetMask
- MSFT_TargetPortal.PortNumber
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_TargetPortal class

Represents a target portal.

A target portal is an endpoint that is used by IP-based storage networks, such as iSCSI. It provides to initiators the IP addresses where they can discover target ports.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_TargetPortal : MSFT_StorageObject
{
  String IPv4Address;
  String IPv6Address;
  String SubnetMask;
  UInt32 PortNumber;
};
```

## Members

The **MSFT\_TargetPortal** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_TargetPortal** class has these properties.

<dl> <dt>

**IPv4Address**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The IPv4 address that the target portal uses.

</dd> <dt>

**IPv6Address**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The IPv6 address that the target portal uses.

</dd> <dt>

**PortNumber**
</dt> <dd> <dl> <dt>

Data type: **UInt32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The port number that is used by the target portal.

</dd> <dt>

**SubnetMask**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The subnet mask for the IPv4 address of the target portal, if a subnet mask is defined.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageObject**](msft-storageobject.md)
</dt> </dl>

 

 






---
description: Represents per-interface IP-HTTPs configuration settings.
ms.assetid: 14ce0ade-3c93-4244-b9fb-d91a3e2eb1ef
title: MSFT\_NetIpHTTPsState class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetIpHTTPsState
- MSFT_NetIpHTTPsState.ManagedElement
- MSFT_NetIpHTTPsState.SettingData
- MSFT_NetIpHTTPsState.InterfaceStatus
- MSFT_NetIpHTTPsState.LastErrorCode
api_type: 
- DllExport
api_location: 
- NetTtCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetIpHTTPsState class

Represents per-interface IP-HTTPs configuration settings.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetTtCim")]
class MSFT_NetIpHTTPsState : CIM_ElementSettingData
{
  MSFT_NetIPInterface       REF ManagedElement;
  MSFT_Net6to4Configuration REF SettingData;
  string                        InterfaceStatus;
  uint32                        LastErrorCode;
};
```

## Members

The **MSFT\_NetIpHTTPsState** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetIpHTTPsState** class has these properties.

<dl> <dt>

**InterfaceStatus**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the status of the IP-HTTPs interface.

</dd> <dt>

**LastErrorCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the error code for the last error that occurred for the IP-HTTPs interface.

</dd> <dt>

**ManagedElement**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetIPInterface**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override** ("ManagedElement")
</dt> </dl>

Defines the IP interface of the association.

</dd> <dt>

**SettingData**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_Net6to4Configuration**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override** ("SettingData")
</dt> </dl>

Defines the global 6to4 settings.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCIMV2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTtCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTtCim.dll</dt> </dl> |



 

 





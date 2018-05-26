---
title: Create method of the MSFT\_NetRoute class
description: Creates a TCP/IP route.
audience: developer
ms.assetid: a1578fd3-e9d8-41b6-bf06-a07b692e7295
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Create method
- Create method, MSFT_NetRoute class
- MSFT_NetRoute class, Create method
topic_type:
- apiref
api_name:
- MSFT_NetRoute.Create
api_location:
- VPNClientPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Create method of the MSFT\_NetRoute class

Creates a TCP/IP route.

## Syntax


```mof
uint32 Create(
  [in]  uint32        InterfaceIndex,
  [in]  string        InterfaceAlias,
  [in]  string        DestinationPrefix,
  [in]  uint8         Publish,
  [in]  uint16        RouteMetric,
  [in]  datetime      ValidLifetime,
  [in]  datetime      PreferredLifetime,
  [in]  uint16        AddressFamily,
  [in]  string        PolicyStore,
  [in]  boolean       PassThru,
  [out] MSFT_NetRoute CmdletOutput
);
```



## Parameters

<dl> <dt>

*InterfaceIndex* \[in\]
</dt> <dd>

The user-friendly interface index.

</dd> <dt>

*InterfaceAlias* \[in\]
</dt> <dd>

The user-friendly interface name.

</dd> <dt>

*DestinationPrefix* \[in\]
</dt> <dd>

The destination prefix.

</dd> <dt>

*Publish* \[in\]
</dt> <dd>

One of the following values:

<dt>

<span id="No"></span><span id="no"></span><span id="NO"></span>

<span id="No"></span><span id="no"></span><span id="NO"></span>**No** (0)


</dt> <dd>

Not advertised in Route Advertisements. This is the default.

</dd> <dt>

<span id="Age"></span><span id="age"></span><span id="AGE"></span>

<span id="Age"></span><span id="age"></span><span id="AGE"></span>**Age** (1)


</dt> <dd>

Advertised in Route Advertisements with a finite lifetime.

</dd> <dt>

<span id="Yes"></span><span id="yes"></span><span id="YES"></span>

<span id="Yes"></span><span id="yes"></span><span id="YES"></span>**Yes** (2)


</dt> <dd>

Advertised in Route Advertisements with an infinite lifetime.

</dd> </dl> </dd> <dt>

*RouteMetric* \[in\]
</dt> <dd>

Metric of the route being added.

</dd> <dt>

*ValidLifetime* \[in\]
</dt> <dd>

Lifetime over which the route is valid. The default value is infinite.

</dd> <dt>

*PreferredLifetime* \[in\]
</dt> <dd>

Lifetime over which the route is preferred. The default value is infinite.

</dd> <dt>

*AddressFamily* \[in\]
</dt> <dd>

Indicates whether the address family for this route is v4 or v6.

<dt>

2
</dt> <dd>

v4

</dd> <dt>

23
</dt> <dd>

v6

</dd> </dl> </dd> <dt>

*PolicyStore* \[in\]
</dt> <dd>

Path to the group policy object that should be modified by this method.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**true** to return the current instance in the *CmdletOutput* parameter. The default is **false**.

</dd> <dt>

*CmdletOutput* \[out\]
</dt> <dd>

On return, contains an instance of the current object. This parameter returns a value only if *PassThru* is set to true.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\Client<br/>                                          |
| MOF<br/>                      | <dl> <dt>VPNClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VPNClientPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_NetRoute**](msft-netroute-vpnclientpsprovider.md)
</dt> </dl>

 

 






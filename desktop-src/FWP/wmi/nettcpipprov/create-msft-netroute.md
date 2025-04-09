---
description: Create an IP route.
ms.assetid: 06dfd275-25f9-48bc-8361-87ab1c905c17
title: Create method of the MSFT\_NetRoute class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- kbSyntax
api_name: 
api_type: 
api_location: 
---

# Create method of the MSFT\_NetRoute class

Create an IP route.

## Syntax


```mof
uint32 Create(
  [in]  uint32        InterfaceIndex,
  [in]  string        InterfaceAlias,
  [in]  string        DestinationPrefix,
  [in]  string        NextHop,
  [in]  uint8         Publish,
  [in]  uint16        RouteMetric,
  [in]  uint16        Protocol,
  [in]  datetime      ValidLifetime,
  [in]  datetime      PreferredLifetime,
  [in]  string        PolicyStore,
  [in]  uint16        AddressFamily,
  [in]  boolean       PassThru,
  [out] MSFT_NetRoute CmdletOutput[]
);
```



## Parameters

<dl> <dt>

*InterfaceIndex* \[in\]
</dt> <dd>

The interface index of the route.

</dd> <dt>

*InterfaceAlias* \[in\]
</dt> <dd>

The interface alias of the route.

</dd> <dt>

*DestinationPrefix* \[in\]
</dt> <dd>

The destination prefix of the route.

</dd> <dt>

*NextHop* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*Publish* \[in\]
</dt> <dd>

The value that indicates how to advertise the route. This parameter can contain one of the following values.



| Value                                                                        | Meaning                                                 |
|------------------------------------------------------------------------------|---------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | Do not advertise the route.<br/>                  |
| <dl> <dt>1</dt> </dl> | Advertise the route for a specific interval.<br/> |
| <dl> <dt>2</dt> </dl> | Advertise the route indefinitely.<br/>            |



 

</dd> <dt>

*RouteMetric* \[in\]
</dt> <dd>

The route metric.

</dd> <dt>

*Protocol* \[in\]
</dt> <dd>

TBD

**Windows 8 and Windows Server 2012:** This parameter is not supported before Windows 8.1 and Windows Server 2012 R2.

</dd> <dt>

*ValidLifetime* \[in\]
</dt> <dd>

The valid end time of the lifetime of the route. The default value for this parameter is infinite.

</dd> <dt>

*PreferredLifetime* \[in\]
</dt> <dd>

The preferred end time of the lifetime of the route. The default value for this parameter is infinite

</dd> <dt>

*PolicyStore* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*AddressFamily* \[in\]
</dt> <dd>

A value that indicates whether the route uses the IPv4 or IPv6 address family. This parameter can contain one of the following values.



| Value                                                                         | Meaning         |
|-------------------------------------------------------------------------------|-----------------|
| <dl> <dt>2</dt> </dl>  | IPv4<br/> |
| <dl> <dt>23</dt> </dl> | IPv6<br/> |



 

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

A value that indicates whether the *MSFT\_NetRoute* parameter returns an object.

</dd> <dt>

*CmdletOutput* \[out\]
</dt> <dd>

The [**MSFT\_NetRoute**](msft-netroute.md) object that receives the new route.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTCPIP.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTCPIP.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_NetRoute**](msft-netroute.md)
</dt> </dl>

 

 





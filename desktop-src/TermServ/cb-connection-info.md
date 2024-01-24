---
title: CB_CONNECTION_INFO structure (Cbclient.h)
description: Contains information about an incoming connection request.
ms.assetid: BA908425-3B68-40AA-B1E3-153D6873EF2C
ms.tgt_platform: multiple
keywords:
- CB_CONNECTION_INFO structure Remote Desktop Services
- PCB_CONNECTION_INFO structure pointer Remote Desktop Services
topic_type:
- apiref
api_name:
- CB_CONNECTION_INFO
api_location:
- Cbclient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_CONNECTION\_INFO structure

Contains information about an incoming connection request. This structure is used with the [**IConnectionBrokerClient::GetTargetInfo**](iconnectionbrokerclient-gettargetinfo.md) method.

## Syntax


```C++
typedef struct {
  WCHAR            UserName[CB_USERNAME_LENGTH];
  WCHAR            Domain[CB_DOMAINNAME_LENGTH];
  WCHAR            InitialProgram[CB_INITAPP_LENGTH];
  CB_RESOURCE_TYPE Resource;
  WCHAR            PluginName[CB_PLUGINNAME_LENGTH];
  WCHAR            FarmName[CB_FARMNAME_LENGTH];
  DWORD            dwVendorInfoLength;
  PBYTE            pVendorSpecificInfo;
} CB_CONNECTION_INFO, *PCB_CONNECTION_INFO;
```



## Members

<dl> <dt>

**UserName**
</dt> <dd>

The name of the user requesting a session.

</dd> <dt>

**Domain**
</dt> <dd>

The name of the domain that **UserName** is a member of.

</dd> <dt>

**InitialProgram**
</dt> <dd>

The fully qualified path and file name of the initial program that is started when the session is started. Set this member to an empty string if no initial program should be started.

</dd> <dt>

**Resource**
</dt> <dd>

A value of the [**CB\_RESOURCE\_TYPE**](cb-resource-type.md) enumeration that specifies the type of resource that the incoming connection is connecting to. If the **PluginName** member is **NULL**, this member is used to by the Remote Desktop Connection Broker to determine which plug-in to invoke for determining the target computer.

</dd> <dt>

**PluginName**
</dt> <dd>

The name of the plug-in to invoke to determine the target computer. If this parameter is **NULL**, the **Resource** member is used to determine which plug-in to invoke.

</dd> <dt>

**FarmName**
</dt> <dd>

The name of the farm that contains the computers, one of which will be the target computer where the connection will be redirected.

</dd> <dt>

**dwVendorInfoLength**
</dt> <dd>

This member is reserved for future use.

</dd> <dt>

**pVendorSpecificInfo**
</dt> <dd>

This member is reserved for future use.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                        |
| Header<br/>                   | <dl> <dt>Cbclient.h</dt> </dl> |



## See also

<dl> <dt>

[**IConnectionBrokerClient::GetTargetInfo**](iconnectionbrokerclient-gettargetinfo.md)
</dt> </dl>

 

 






---
title: Win32_RDSHServer class
description: Manages a Remote Desktop Session Host (RDSH) server.
ms.assetid: 2c2840d2-16aa-484a-979b-6dbb1a08bbcf
ms.tgt_platform: multiple
keywords:
- Win32_RDSHServer class Remote Desktop Services
- Win32_RDSHServer class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_RDSHServer
- Win32_RDSHServer.Name
- Win32_RDSHServer.ConnectionBroker
- Win32_RDSHServer.CollectionAlias
- Win32_RDSHServer.ServerState
api_location:
- RDMS.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_RDSHServer class

Manages a Remote Desktop Session Host (RDSH) server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("Win32_RDManagement_Prov"), AMENDMENT]
class Win32_RDSHServer
{
  string Name;
  string ConnectionBroker;
  string CollectionAlias;
  uint32 ServerState;
};
```

## Members

The **Win32\_RDSHServer** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_RDSHServer** class has these methods.



| Method                                                                          | Description                                                                                                                                                                       |
|:--------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetInt32Property**](getint32property-win32-rdshserver.md)                   | Retrieves an integer property value of a **Win32\_RDSHServer** object.<br/>                                                                                                 |
| [**GetPendingStartServerList**](win32-rdshserver-getpendingstartserverlist.md) | Retrieves a list of server waiting to start.<br/>                                                                                                                           |
| [**GetStringProperty**](getstringproperty-win32-rdshserver.md)                 | Retrieves a string property value of a **Win32\_RDSHServer** object.<br/>                                                                                                   |
| [**SetInt32Property**](setint32property-win32-rdshserver.md)                   | Updates an integer property value of a **Win32\_RDSHServer** object.<br/>                                                                                                   |
| [**SetStringProperty**](setstringproperty-win32-rdshserver.md)                 | Updates a string property value of a **Win32\_RDSHServer** object.<br/>                                                                                                     |
| [**TestAndSetState**](win32-rdshserver-testandsetstate.md)                     | Compares the current state to the specified comparand; if the two match, the state is set to a new value. Regardless of the match, the current state is also returned.<br/> |



 

### Properties

The **Win32\_RDSHServer** class has these properties.

<dl> <dt>

**CollectionAlias**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**optional**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

Gets and sets the alias to the RDSH collection to which the RDSH server is assigned.

</dd> <dt>

**ConnectionBroker**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets the name of the Remote Desktop Connection Broker (RDCB) that manages user access to the RDSH server.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Gets and sets the name of the RDSH server.

</dd> <dt>

**ServerState**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**optional**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

Describes the state of the server. Any value other than **TARGET\_RUNNING** (3) is reserved and should be consider an invalid state.

The possible values are.

<dt>

<span id="TARGET_UNKNOWN"></span><span id="target_unknown"></span>

**TARGET\_UNKNOWN** (1)


</dt> <dd></dd> <dt>

<span id="TARGET_RUNNING"></span><span id="target_running"></span>

**TARGET\_RUNNING** (3)


</dt> <dd></dd> <dt>

<span id="TARGET_INVALID"></span><span id="target_invalid"></span>

**TARGET\_INVALID** (8)


</dt> <dd></dd> <dt>

<span id="TARGET_STARTING"></span><span id="target_starting"></span>

**TARGET\_STARTING** (9)


</dt> <dd></dd> <dt>

<span id="TARGET_STOPPING"></span><span id="target_stopping"></span>

**TARGET\_STOPPING** (10)


</dt> <dd></dd> </dl>

**Windows Server 2012 R2 and Windows Server 2012:** This property is unavailable prior to Windows Server 2016.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\cimv2\\rdms<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>         |



## See also

<dl> <dt>

[Remote Desktop Management Services Provider](rdms-api-reference.md)
</dt> </dl>

 


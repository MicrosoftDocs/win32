---
description: Represents the global 6to4 configuration shared across all 6to4 interfaces.
ms.assetid: af6506d6-bbd6-4c12-b018-a34b45fbd22d
title: MSFT\_Net6to4Configuration class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_Net6to4Configuration
- MSFT_Net6to4Configuration.PolicyStore
- MSFT_Net6to4Configuration.State
- MSFT_Net6to4Configuration.ResolutionInterval
- MSFT_Net6to4Configuration.RelayName
- MSFT_Net6to4Configuration.RelayState
api_type: 
- DllExport
api_location: 
- NetTtCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_Net6to4Configuration class

Represents the global 6to4 configuration shared across all 6to4 interfaces.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetTtCim")]
class MSFT_Net6to4Configuration : MSFT_NetSettingData
{
  string PolicyStore;
  uint32 State;
  uint32 ResolutionInterval;
  string RelayName;
  uint32 RelayState;
};
```

## Members

The **MSFT\_Net6to4Configuration** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_Net6to4Configuration** class has these methods.



| Method                                                                       | Description                                                            |
|:-----------------------------------------------------------------------------|:-----------------------------------------------------------------------|
| [**GetConfig**](/previous-versions/windows/desktop/raserverpsprov/getconfigurationversion-ps-remoteaccesslocal) | Obtains the configuration given the specified policy store.<br/> |
| [**Reset**](reset-msft-net6to4configuration.md)                             | Resets the 6to4 configuration.<br/>                              |



 

### Properties

The **MSFT\_Net6to4Configuration** class has these properties.

<dl> <dt>

**PolicyStore**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the store from which to retrieve the 6to4 configuration policy.

</dd> <dt>

**RelayName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the name of the 6to4 relay.

</dd> <dt>

**RelayState**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Describes the state of the relay name resolution using one of the following values:

<dl> <dt>

<span id="default_"></span><span id="DEFAULT_"></span>**default** (0)
</dt> <dt>

<span id="automatic_"></span><span id="AUTOMATIC_"></span>**automatic** (1)
</dt> <dt>

<span id="enabled_"></span><span id="ENABLED_"></span>**enabled** (2)
</dt> <dt>

<span id="disabled_"></span><span id="DISABLED_"></span>**disabled** (3 )
</dt> </dl>

</dd> <dt>

**ResolutionInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the resolution interval in minutes.

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the 6to4 service state using one of the following values:

<dl> <dt>

<span id="default_"></span><span id="DEFAULT_"></span>**default** (0)
</dt> <dt>

<span id="automatic_"></span><span id="AUTOMATIC_"></span>**automatic** (1)
</dt> <dt>

<span id="enabled_"></span><span id="ENABLED_"></span>**enabled** (2)
</dt> <dt>

<span id="disabled_"></span><span id="DISABLED_"></span>**disabled** (3 )
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCIMV2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTtCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTtCim.dll</dt> </dl> |



 


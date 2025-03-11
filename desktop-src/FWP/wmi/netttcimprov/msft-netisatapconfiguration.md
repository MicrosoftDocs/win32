---
description: Represents global ISATAP Configuration shared across all ISATAP interfaces.
ms.assetid: 35f5dd82-58db-47d1-b5ca-6d4b5f88fc03
title: MSFT\_NetISATAPConfiguration class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetISATAPConfiguration
- MSFT_NetISATAPConfiguration.PolicyStore
- MSFT_NetISATAPConfiguration.State
- MSFT_NetISATAPConfiguration.Router
- MSFT_NetISATAPConfiguration.ResolutionState
- MSFT_NetISATAPConfiguration.ResolutionInterval
api_type: 
- DllExport
api_location: 
- NetTtCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetISATAPConfiguration class

Represents global ISATAP Configuration shared across all ISATAP interfaces.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetTtCim")]
class MSFT_NetISATAPConfiguration : MSFT_NetSettingData
{
  string PolicyStore;
  uint32 State;
  string Router;
  uint32 ResolutionState;
  uint32 ResolutionInterval;
};
```

## Members

The **MSFT\_NetISATAPConfiguration** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_NetISATAPConfiguration** class has these methods.



| Method                                                                       | Description                                                            |
|:-----------------------------------------------------------------------------|:-----------------------------------------------------------------------|
| [**GetConfig**](/previous-versions/windows/desktop/raserverpsprov/getconfigurationversion-ps-remoteaccesslocal) | Obtains the configuration given the specified policy store.<br/> |



 

### Properties

The **MSFT\_NetISATAPConfiguration** class has these properties.

<dl> <dt>

**PolicyStore**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the store from which to retrieve the ISATAP configuration policy.

</dd> <dt>

**ResolutionInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the resolution interval in minutes.

</dd> <dt>

**ResolutionState**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the state of the ISATAP resolution using one of the following values:

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

**Router**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the name of the ISATAP router.

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Describes the ISATAP service state using one of the following values:

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



 


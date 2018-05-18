---
title: MSFT\_FSRMFMJAction class
description: Represents a file management job action object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f396e2cb-cfe0-4b4f-bd01-7814a83fb133'
ms.prod: 'windows-server-dev'
ms.technology: 'file-server-resource-manager'
ms.tgt_platform: multiple
keywords: ["MSFT_FSRMFMJAction class File Server Resource Manager", "MSFT_FSRMFMJAction class File Server Resource Manager , described"]
topic_type:
- apiref
api_name:
- MSFT_FSRMFMJAction
- MSFT_FSRMFMJAction.Type
- MSFT_FSRMFMJAction.ExpirationFolder
- MSFT_FSRMFMJAction.RMSFolderOwner
- MSFT_FSRMFMJAction.RMSFullControlUser
- MSFT_FSRMFMJAction.RMSReadUser
- MSFT_FSRMFMJAction.RMSWriteUser
- MSFT_FSRMFMJAction.RMSTemplate
- MSFT_FSRMFMJAction.Command
- MSFT_FSRMFMJAction.WorkingDirectory
- MSFT_FSRMFMJAction.CommandParameters
- MSFT_FSRMFMJAction.SecurityLevel
api_location:
- SrmSvc.dll
api_type:
- DllExport
---

# MSFT\_FSRMFMJAction class

Represents a file management job action object.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("FSRMWmiProvider")]
class MSFT_FSRMFMJAction
{
  uint32  Type;
  string  ExpirationFolder;
  boolean RMSFolderOwner;
  string  RMSFullControlUser[] = {};
  string  RMSReadUser[] = {};
  string  RMSWriteUser[] = {};
  string  RMSTemplate = "";
  string  Command;
  string  WorkingDirectory = "";
  string  CommandParameters = "";
  uint32  SecurityLevel = 2;
};
```

## Members

The **MSFT\_FSRMFMJAction** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_FSRMFMJAction** class has these methods.



| Method                                                          | Description                                                |
|:----------------------------------------------------------------|:-----------------------------------------------------------|
| [**CreateFMJAction**](msft-fsrmfmjaction-createfmjaction.md)   | Creates a new **MSFT\_FSRMFMJAction** instance.<br/> |
| [**EnumRmsTemplates**](msft-fsrmfmjaction-enumrmstemplates.md) | Enumerates the available RMS templates.<br/>         |



 

### Properties

The **MSFT\_FSRMFMJAction** class has these properties.

<dl> <dt>

**Command**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A string that refers to a valid executable file. Must not exceed the length of **MAX\_PATH** (260). Required.

This property is only valid when the **Type** property is 2 (Custom).

</dd> <dt>

**CommandParameters**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A string up to 10KB in size. The default value is an empty string. Optional.

This property is required when the **Type** property is 2 (Custom). See the [**Arguments**](ifsrmactioncommand-arguments.md) property of [**IFsrmActionCommand**](ifsrmactioncommand.md).

</dd> <dt>

**ExpirationFolder**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A string representing a path to a local or remote folder. Optional. Size must not exceed the value of **MAX\_PATH** (260).

This property is only valid when the **Type** property is 1 (Expiration).

</dd> <dt>

**RMSFolderOwner**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Add the **FolderOwner** to the full control list if **True**. Has no effect if no **FolderOwner** is available for the file.

This property is only valid when the **Type** property is 3 (RMS) and the **RMSTemplate** property is not specified.

</dd> <dt>

**RMSFullControlUser**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array of user email addresses to provide with full control. Each string must be less than 1KB in size. This parameter is optional. The default value is an empty list.

This property is required when the **Type** property is 3 (RMS) and the **RMSTemplate** property is empty or not specified.

</dd> <dt>

**RMSReadUser**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

A list of user email addresses to provide with read access. Each string must be less than 1KB in size. This parameter is optional. The default value is an empty list.

This property is only valid when the **Type** property is 3 (RMS) and the **RMSTemplate** property is empty or not specified.

</dd> <dt>

**RMSTemplate**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of an RMS template. Must be fewer than 1000 characters. This parameter is optional. The default value is an empty string.

This property is required the **Type** property is 3 (RMS) and the **RMSFullControlUser** property is empty or not specified. If this property is specified then the **RMSFolderOwner**, **RMSFullControlUser**, **RMSReadUser**, and **RMSWriteUser** properties must not be specified.

</dd> <dt>

**RMSWriteUser**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

A list of user email addresses to provide with write access. Each string must be less than 1KB in size. This parameter is optional. The default value is an empty list.

This property is only valid when the **Type** property is 3 (RMS) and the **RMSTemplate** property is empty or not specified.

</dd> <dt>

**SecurityLevel**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The account under which the executable program or script will be run. This property is only valid when the **Type** property is 2 (Custom). The default value is 2 (LocalService). See the [**FsrmAccountType**](fsrmaccounttype.md) enumeration.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (0)


</dt> <dd>

The security level is not specified.

</dd> <dt>

<span id="NetworkService"></span><span id="networkservice"></span><span id="NETWORKSERVICE"></span>

<span id="NetworkService"></span><span id="networkservice"></span><span id="NETWORKSERVICE"></span>**NetworkService** (1)


</dt> <dd>

The action is run in the context of the [NetworkService Account](https://msdn.microsoft.com/library/windows/desktop/ms684272).

</dd> <dt>

<span id="LocalService"></span><span id="localservice"></span><span id="LOCALSERVICE"></span>

<span id="LocalService"></span><span id="localservice"></span><span id="LOCALSERVICE"></span>**LocalService** (2)


</dt> <dd>

The action is run in the context of the [LocalService Account](https://msdn.microsoft.com/library/windows/desktop/ms684188).

</dd> <dt>

<span id="LocalSystem"></span><span id="localsystem"></span><span id="LOCALSYSTEM"></span>

<span id="LocalSystem"></span><span id="localsystem"></span><span id="LOCALSYSTEM"></span>**LocalSystem** (3)


</dt> <dd>

The action is run in the context of the [LocalSystem Account](https://msdn.microsoft.com/library/windows/desktop/ms684190).

</dd> </dl>

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the type of the action. Not all types support all properties. Properties that are not supported must be cleared if the **Type** property value is changed. See the Remarks section for a table that shows which properties are supported for each type.

<dt>

<span id="Expiration"></span><span id="expiration"></span><span id="EXPIRATION"></span>

<span id="Expiration"></span><span id="expiration"></span><span id="EXPIRATION"></span>**Expiration** (1)


</dt> <dd>

The action is an expiration action.

</dd> <dt>

<span id="Custom"></span><span id="custom"></span><span id="CUSTOM"></span>

<span id="Custom"></span><span id="custom"></span><span id="CUSTOM"></span>**Custom** (2)


</dt> <dd>

The action is a custom action.

</dd> <dt>

<span id="RMS"></span><span id="rms"></span>

<span id="RMS"></span><span id="rms"></span>**RMS** (3)


</dt> <dd>

The action is a Rights Managed Services (RMS) action.

</dd> </dl>

</dd> <dt>

**WorkingDirectory**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A string that refers to a valid path to a folder. The length must not exceed **MAX\_PATH** (260). Remote paths are not supported. The default value is an empty string.

This property is only valid when the **Type** property is 2 (Custom). See the [**WorkingDirectory**](ifsrmactioncommand-workingdirectory.md) property of [**IFsrmActionCommand**](ifsrmactioncommand.md).

</dd> </dl>

## Remarks

Not all action types support every property in the class. The table below indicates which properties in this class are supported by each action type in the **Type** property.



| Property/Type          | Expiration (1) | Custom (2) | RMS (3) |
|------------------------|----------------|------------|---------|
| **ExpirationFolder**   | Yes            | No         | No      |
| **RMSFolderOwner**     | No             | No         | Yes     |
| **RMSFullControlUser** | No             | No         | Yes     |
| **RMSReadUser**        | No             | No         | Yes     |
| **RMSWriteUser**       | No             | No         | Yes     |
| **RMSTemplate**        | No             | Yes        | Yes     |
| **Command**            | No             | Yes        | No      |
| **WorkingDirectory**   | No             | Yes        | No      |
| **Parameters**         | No             | Yes        | No      |
| **SecurityLevel**      | No             | Yes        | No      |



 

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\FSRM<br/>                                                 |
| MOF<br/>                      | <dl> <dt>MSFT\_FSRM.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SrmSvc.dll</dt> </dl>     |



## See also

<dl> <dt>

[FSRM WMI Classes](fsrm-wmi-classes.md)
</dt> </dl>

 

 






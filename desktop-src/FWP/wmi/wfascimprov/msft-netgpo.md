---
description: This class does not have any instances. It is used to manage locally-cached Group Policy Objects.
ms.assetid: 827f9188-6115-4dd7-b3f0-678025ec6635
title: MSFT\_NetGPO class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetGPO
- MSFT_NetGPO.InstanceID
- MSFT_NetGPO.Caption
- MSFT_NetGPO.Description
- MSFT_NetGPO.ElementName
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetGPO class

This class does not have any instances. It is used to manage locally-cached Group Policy Objects.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetGPO : CIM_SettingData
{
  string InstanceID;
  string Caption;
  string Description;
  string ElementName;
};
```

## Members

The **MSFT\_NetGPO** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_NetGPO** class has these methods.



| Method                           | Description                                           |
|:---------------------------------|:------------------------------------------------------|
| [**Open**](open-msft-netgpo.md) | Read a GPO, and cache results locally<br/>      |
| [**Save**](save-msft-netgpo.md) | Write the local cached GPO info back to AD<br/> |



 

### Properties

The **MSFT\_NetGPO** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Used in CimInstance.ToString(). A short string for describing this instance when debugging.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This field is ignored.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that uniquely identifies this instance within the PolicyStore.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



 

 





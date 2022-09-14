---
title: Win32_RDSHCollection class
description: Manages a collection of Remote Desktop Session Hosts.
ms.assetid: 7800bf2e-9497-4e41-aed9-b318748dd83f
ms.tgt_platform: multiple
keywords:
- Win32_RDSHCollection class Remote Desktop Services
- Win32_RDSHCollection class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_RDSHCollection
- Win32_RDSHCollection.Alias
- Win32_RDSHCollection.Name
- Win32_RDSHCollection.Description
- Win32_RDSHCollection.Type
api_location:
- RDMS.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_RDSHCollection class

Manages a collection of Remote Desktop Session Hosts.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("Win32_RDManagement_Prov"), AMENDMENT]
class Win32_RDSHCollection
{
  string Alias;
  string Name;
  string Description;
  uint32 Type;
};
```

## Members

The **Win32\_RDSHCollection** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_RDSHCollection** class has these methods.



| Method                                                                      | Description                                                                                                                                                                                            |
|:----------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetInt32Property**](getint32property-win32-rdshcollection.md)           | Retrieves an integer property value of a **Win32\_RDSHCollection** object.<br/>                                                                                                                  |
| [**GetStringProperty**](getstringproperty-win32-rdshcollection.md)         | Retrieves a string property value of a **Win32\_RDSHCollection** object.<br/>                                                                                                                    |
| [**KeyValueCompareAndSet**](win32-rdshcollection-keyvaluecompareandset.md) | Compares the specified key in the collection with a comparand; if they match, the key is set to a new value. If the key does not exist, the method will insert the key into the collection.<br/> |
| [**KeyValueDelete**](win32-rdshcollection-keyvaluedelete.md)               | Deletes the specified key (and associated value) from the collection.<br/>                                                                                                                       |
| [**KeyValueGet**](win32-rdshcollection-keyvalueget.md)                     | Retrieves the value associated with the specified key in the collection.<br/>                                                                                                                    |
| [**SetInt32Property**](setint32property-win32-rdshcollection.md)           | Updates an integer property value of a **Win32\_RDSHCollection** object.<br/>                                                                                                                    |
| [**SetStringProperty**](setstringproperty-win32-rdshcollection.md)         | Updates a string property value of a **Win32\_RDSHCollection** object.<br/>                                                                                                                      |



 

### Properties

The **Win32\_RDSHCollection** class has these properties.

<dl> <dt>

**Alias**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Gets and sets the alias of the collection.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**optional**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

Gets and sets the description of the collection.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets the name of the collection.

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**Windows Server 2012 R2 and Windows Server 2012:** This property is unavailable prior to Windows Server 2016.

The type of collection.

<dt>

<span id="Regular"></span><span id="regular"></span><span id="REGULAR"></span>

<span id="Regular"></span><span id="regular"></span><span id="REGULAR"></span>**Regular** (0)


</dt> <dd></dd> <dt>



 (2)


</dt> <dd>

Reserved

</dd> <dt>



 (3)


</dt> <dd>

Reserved

</dd> <dt>

<span id="ManualPersonal"></span><span id="manualpersonal"></span><span id="MANUALPERSONAL"></span>

<span id="ManualPersonal"></span><span id="manualpersonal"></span><span id="MANUALPERSONAL"></span>**ManualPersonal** (4)


</dt> <dd></dd> <dt>

<span id="AutoPersonal"></span><span id="autopersonal"></span><span id="AUTOPERSONAL"></span>

<span id="AutoPersonal"></span><span id="autopersonal"></span><span id="AUTOPERSONAL"></span>**AutoPersonal** (5)


</dt> <dd></dd> </dl>

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

 


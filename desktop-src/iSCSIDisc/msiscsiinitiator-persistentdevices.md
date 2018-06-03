---
Description: This MSIscsiInitiator\_PersistentDevices structure contains path information associated with a persistent device.
ms.assetid: 9e48d87f-8781-48d7-8def-7d412a5fe24b
title: MSIscsiInitiator\_PersistentDevices class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSIscsiInitiator\_PersistentDevices class

This **MSIscsiInitiator\_PersistentDevices** structure contains path information associated with a persistent device.

## Syntax

``` syntax
class MSIscsiInitiator_PersistentDevices
{
  string DevicePath;
};
```

## Members

The **MSIscsiInitiator\_PersistentDevices** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSIscsiInitiator\_PersistentDevices** class has these properties.

<dl> <dt>

**DevicePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

A unique key DevicePath

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Namespace<br/>                | Root\\WMI<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>Iscsidsc.mof</dt> </dl> |



 

 





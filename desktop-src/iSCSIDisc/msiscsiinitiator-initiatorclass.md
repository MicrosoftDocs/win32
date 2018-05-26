---
Description: The MSIscsiInitiator\_InitiatorClass structure contains the name of the Initiator.
ms.assetid: ee59c722-d286-4713-a359-6efebdba61f3
title: MSIscsiInitiator\_InitiatorClass class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSIscsiInitiator\_InitiatorClass class

The **MSIscsiInitiator\_InitiatorClass** structure contains the name of the Initiator.

## Syntax

``` syntax
class MSIscsiInitiator_InitiatorClass
{
  string InitiatorName;
};
```

## Members

The **MSIscsiInitiator\_InitiatorClass** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSIscsiInitiator\_InitiatorClass** class has these properties.

<dl> <dt>

**InitiatorName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the Initiator.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Namespace<br/>                | Root\\WMI<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>Iscsidsc.mof</dt> </dl> |



 

 





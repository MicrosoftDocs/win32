---
title: Windows Mail Miscellaneous Reference
description: This documentation provides miscellaneous-related information about the set of interfaces for objects related to Windows Mail (formerly Outlook Express).
ms.assetid: 1d524739-c26f-4fd9-92c3-3085112bf57f
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Windows Mail Miscellaneous Reference

This documentation provides miscellaneous-related information about the set of interfaces for objects related to Windows Mail (formerly Outlook Express).

New applications should not use this set of interfaces and schemas. These interfaces and schemas exist for backward compatibility with legacy applications. These interfaces and schemas will be unavailable in the future.

### Interfaces



| Topic                                         | Contents                                                                                                                                                                                      |
|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IOEActions**](oe-ioeactions.md)           | Do not use. If the criteria are met, the methods of the [**IOEActions**](oe-ioeactions.md) interface handle the actions.<br/>                                                          |
| [**IOECriteria**](oe-ioecriteria.md)         | Do not use. The [**IOECriteria**](oe-ioecriteria.md) interface represents criteria used for rules and actions.<br/>                                                                    |
| [**IOEEnumRules**](oe-ioeenumrules.md)       | Do not use. The [**IOEEnumRules**](oe-ioeenumrules.md) interface represents a collection of [**IOERule**](oe-ioerule.md) objects. <br/>                                               |
| [**IOEExecRules**](oe-ioeexecrules.md)       | Do not use. The methods of the [**IOEExecRules**](oe-ioeexecrules.md) interface execute rules when certain criteria are met.<br/>                                                      |
| [**IOERule**](oe-ioerule.md)                 | Do not use. The [**IOERule**](oe-ioerule.md) interface represents a message rule.<br/>                                                                                                 |
| [**IOERulesManager**](oe-ioerulesmanager.md) | Do not use. The methods of the [**IOERulesManager**](oe-ioerulesmanager.md) interface manage message rules. <br/>                                                                      |
| [**IOutlookExpress**](oe-ioutlookexpress.md) | Do not use. Represents the application object.<br/>                                                                                                                                     |
| [**IStoreFolder**](oe-istorefolder.md)       | Do not use. Interface to an Windows Mail storage folder object. Using this interface, you can create, enumerate, and modify messages.<br/>                                              |
| [**IStoreNamespace**](oe-istorenamespace.md) | Do not use. Interface to an Windows Mail storage namespace object. Using this interface, you can create, enumerate, and modify message folders, as well as copy and move messages.<br/> |



 

### Objects



| Topic                                             | Contents                                                                                                                                                                                                                           |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**OEActions**](oe-oeactionsobject.md)           | Do not use. The [**OEActions**](oe-oeactionsobject.md) object implements the [**IOEActions**](oe-ioeactions.md) and [IPersistStream](http://msdn.microsoft.com/library/com/htm/cmi_n2p_02b1.asp) interfaces.<br/>    |
| [**OECriteria**](oe-oecriteriaobject.md)         | Do not use. The [**OECriteria**](oe-oecriteriaobject.md) object implements the [**IOECriteria**](oe-ioecriteria.md) and [IPersistStream](http://msdn.microsoft.com/library/com/htm/cmi_n2p_02b1.asp) interfaces<br/> |
| [**OEEnumRules**](oe-oeenumrulesobject.md)       | Do not use. The [**OEEnumRules**](oe-oeenumrulesobject.md) object implements the [**IOEEnumRules**](oe-ioeenumrules.md) interface. It represents an enumeration of message rules. <br/>                                    |
| [**OEExecRules**](oe-oeexecrulesobject.md)       | Do not use. The [**OEExecRules**](oe-oeexecrulesobject.md) object implements the [**IOEExecRules**](oe-ioeexecrules.md) interface.<br/>                                                                                    |
| [**OERule**](oe-oeruleobject.md)                 | Do not use. The [**OERule**](oe-oeruleobject.md) object implements the [**IOERule**](oe-ioerule.md) interface. It represents a message rule. <br/>                                                                         |
| [**OERulesManager**](oe-oerulesmanagerobject.md) | Do not use. The [**OERulesManager**](oe-oerulesmanagerobject.md) object implements the [**IOERulesManager**](oe-ioerulesmanager.md) interface. It manages message rules. <br/>                                             |



 

### Enums



| Topic                                           | Contents                                                                                        |
|-------------------------------------------------|-------------------------------------------------------------------------------------------------|
| [**ACT\_TYPE**](oe-act-type.md)                | Do not use. Specifies action types.<br/>                                                  |
| [**CRIT\_LOGIC**](oe-crit-logic.md)            | Do not use. Specifies criteria logic.<br/>                                                |
| [**CRIT\_TYPE**](oe-crit-type.md)              | Do not use. Specifies criteria types.<br/>                                                |
| [**FOLDERNOTIFYTYPE**](oe-foldernotifytype.md) | Do not use. Defined as part of [**IStoreNamespace**](oe-istorenamespace.md).<br/>        |
| [**RULE\_PROP**](oe-rule-prop.md)              | Do not use. Identifies the various properties of message rules.<br/>                      |
| [**RULE\_TYPE**](oe-rule-type.md)              | Do not use. Identifies types of rules. <br/>                                              |
| [**SPECIALFOLDER**](oe-specialfolder.md)       | Do not use. Contains constants that specify special message folders in Windows Mail.<br/> |



 

### Structures



| Topic                                       | Contents                                                  |
|---------------------------------------------|-----------------------------------------------------------|
| [**ACT\_ITEM**](oe-act-item.md)            | Do not use. <br/>                                   |
| [**CRIT\_ITEM**](oe-crit-item.md)          | Do not use. <br/>                                   |
| [**FOLDERNOTIFYEX**](oe-foldernotifyex.md) | Do not use. <br/>                                   |
| [**FOLDERPROPS**](oe-folderprops.md)       | Do not use. Defines message folder properties.<br/> |
| [**MESSAGEIDLIST**](oe-messageidlist.md)   | Do not use. Specifies a list of messages.<br/>      |
| [**MESSAGEPROPS**](oe-messageprops.md)     | Do not use. Defines message properties.<br/>        |
| [**RULEINFO**](oe-ruleinfo.md)             | Do not use. Contains a rule.<br/>                   |



 

### Constants



| Topic                                                 | Contents                                                                             |
|-------------------------------------------------------|--------------------------------------------------------------------------------------|
| [**Message State Flags**](oe-message-state-flags.md) | Do not use. Message state flag values that can be set and their meaning. <br/> |



 

 

 






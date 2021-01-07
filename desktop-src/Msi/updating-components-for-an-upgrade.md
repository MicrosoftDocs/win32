---
description: By design, users of the fictitious MNP2000 product should never use upgraded files such as Baseba01.txt.
ms.assetid: 5aca7ff5-c09f-4d00-b319-2b89550686ab
title: Updating Components for an Upgrade
ms.topic: article
ms.date: 05/31/2018
---

# Updating Components for an Upgrade

By design, users of the fictitious MNP2000 product should never use upgraded files such as Baseba01.txt. Therefore the updated files are by definition incompatible with the original product and Windows Installer components, such as Baseball, containing these files must be assigned new component codes. New files, such as Opera01.txt, are introduced as a part of a new component with a unique component code. Because the original product and upgrade use the same Notepad component, the component code of this component is unchanged. For more information about when component code must be changed, see [Changing the Component Code](changing-the-component-code.md).

Use Orca or another database editor to enter the following data into the [Component table](component-table.md) of MNP2001.msi. Do not reuse the GUIDs shown below in the ComponentId column in your sample.

[Component Table](component-table.md)



| Component  | ComponentId                            | Directory\_ | Attributes | Condition | Keypath      |
|------------|----------------------------------------|-------------|------------|-----------|--------------|
| Baseball   | {2951190A-6AF8-4D7F-AA16-D256405C277A} | SPORTDIR    | 2          |           | Baseba01.txt |
| Basketball | {E1AAB6B0-FEC6-4F18-B765-3B05A81CEACB} | SPORTDIR    | 2          |           | Basket01.txt |
| Concert    | {C28C5064-AA84-4431-AC69-FC1321DF18AF} | ARTSDIR     | 2          |           | Concer01.txt |
| Dance      | {1AC2B14D-D5F4-4642-9F7A-EE81BF59B3E2} | ARTSDIR     | 2          |           | Dance01.txt  |
| Opera      | {C2DABF7E-1EF6-458D-84B1-AAC1127CED26} | ARTSDIR     | 2          |           | Opera01.txt  |
| Football   | {92AA30F4-7AC5-4DFA-801E-988CF3DAA4DC} | SPORTDIR    | 2          |           | Footba01.txt |
| Help       | {AD10EB50-33C1-11D3-91D6-00C04FD70856} | NOTEPADDIR  | 2          |           | Help.txt     |
| January    | {E90CD0E6-ED8D-4F88-B000-27BD2B482C6C} | MONDIR      | 2          |           | Janua01.txt  |
| NewYears   | {1EEF8C53-F7C0-405C-8FE3-2B0FE54B0114} | HOLDIR      | 2          |           | NewYea01.txt |
| Memorial   | {BA81ACF7-4D43-424F-93B0-8845A2DF1C02} | HOLDIR      | 2          |           | Memori01.txt |
| Notepad    | {19BED232-30AB-11D3-91D3-00C04FD70856} | NOTEPADDIR  | 2          |           | Redpark.exe  |



 

[Continue](updating-features-for-an-upgrade.md)

 

 




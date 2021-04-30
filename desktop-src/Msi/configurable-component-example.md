---
description: This example allows the module consumer to independently configure an edit control, the checksum attribute, and the compressed attribute.
ms.assetid: f0500856-18d0-45e5-992a-57e01fb2cca5
title: Configurable Component Example
ms.topic: article
ms.date: 05/31/2018
---

# Configurable Component Example

In this example, the following ModuleConfiguration and ModuleSubstitution tables allows the module consumer to independently configure the Password attribute for an edit control, the checksum attribute for a file, and the compressed attribute for the same file.

[ModuleSubstitution Table](modulesubstitution-table.md)



| Table   | Row           | Column     | Value                        |
|---------|---------------|------------|------------------------------|
| Control | Dialog1;Edit1 | Attributes | \[=Password\]                |
| File    | File1         | Attributes | \[=Checksum\]\[=Compressed\] |



 

[ModuleConfiguration Table](moduleconfiguration-table.md)



| Name       | Format   | Type | ContextData                              | DefaultValue | Attributes | DisplayName | Description |
|------------|----------|------|------------------------------------------|--------------|------------|-------------|-------------|
| Password   | Bitfield |      | 2097152;True=2097152;False=0             | 0            | 0          |             |             |
| Checksum   | Bitfield |      | 1024;Checksum=1024;No Checksum=0         | 0            | 0          |             |             |
| Compressed | Bitfield |      | 24576;Compressed=16384;Uncompressed=8192 | 8192         | 0          |             |             |



 

 

 




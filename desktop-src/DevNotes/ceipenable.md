---
description: HKLM\\Software\\Microsoft\\SQMClient\\Windows\\CEIPEnable.
ms.assetid: 68ba8219-7ed2-44a9-9fd5-f6dfa57891c0
title: CEIPEnable
ms.topic: article
ms.date: 05/31/2018
---

# CEIPEnable

**HKLM\\Software\\Microsoft\\SQMClient\\Windows\\CEIPEnable**



| Data type  | Range                     | Default value |
|------------|---------------------------|---------------|
| REG\_DWORD | 0 (disable) or 1 (enable) | 0             |



 

## Description

Enables the Windows Customer Experience Improvement program.

## Change Method

To change the value of this entry, in Control Panel, select **System and Maintenance**, followed by **Problem Reports and Solutions**. Click **Customer Experience Improvement Settings** from the See Also section.

## Activation Method

Changes made to this entry are effective immediately. Enabling this registry key causes the Windows Customer Experience Improvement Program to be enabled for the entire computer. Disabling this registry key causes the Windows Customer Experience Improvement Program to be disabled for the entire computer.

This entry can be superseded by a Group Policy setting on systems that support Group Policy. While the Windows Customer Experience Improvement Program CEIP Enable Group Policy setting is enabled, the system ignores this entry. The configuration of this policy setting is stored in the **Policies** section under **HKLM\\Software\\Policies\\Microsoft\\SQMClient\\Windows\\CEIPEnable**.

 

 




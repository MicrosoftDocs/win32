---
title: Count Property
description: Count Property
ms.assetid: 'a0375aa9-495d-47be-a3f7-4d5987688555'
---

# Count Property

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns a Long integer (read-only property) that specifies the count of [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441) objects in the [**Commands**](https://msdn.microsoft.com/library/windows/desktop/ms695971) collection.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").Commands.Count**

</dd> </dl>

## Remarks

**Count** includes only the number of [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441) objects you define in your [**Commands**](https://msdn.microsoft.com/library/windows/desktop/ms695971) collection. Server or other client entries are not included.

 

 





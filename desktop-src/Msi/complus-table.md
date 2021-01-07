---
description: The Complus table contains information needed to install COM+ applications.
ms.assetid: 0c9a7469-5959-45ad-b84d-6cfd3e169ff6
title: Complus Table
ms.topic: article
ms.date: 05/31/2018
---

# Complus Table

The Complus table contains information needed to install COM+ applications.

The Complus table has the following columns.



| Column      | Type                         | Key | Nullable |
|-------------|------------------------------|-----|----------|
| Component\_ | [Identifier](identifier.md) | Y   | N        |
| ExpType     | [Integer](integer.md)       | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Component_"></span><span id="component_"></span><span id="COMPONENT_"></span>Component\_
</dt> <dd>

An external key into the first column of the [Component table](component-table.md). This is the component that contains the COM+ application.

</dd> <dt>

<span id="ExpType"></span><span id="exptype"></span><span id="EXPTYPE"></span>ExpType
</dt> <dd>

Export flags used during the generation of the .msi file. For more information see the COM+ documentation in the Microsoft Windows Software Development Kit (SDK).

</dd> </dl>

## Remarks

See the [RegisterComPlus action](registercomplus-action.md) and [UnregisterComPlus action](unregistercomplus-action.md).

See [Installing a COM+ Application with the Windows Installer](installing-a-com--application-with-the-windows-installer.md).

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE32](ice32.md)  
[ICE66](ice66.md)  
</dl>

 

 




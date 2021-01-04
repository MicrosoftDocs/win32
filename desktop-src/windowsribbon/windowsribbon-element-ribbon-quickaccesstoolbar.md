---
title: Ribbon.QuickAccessToolbar property
description: Represents a container for the Quick Access Toolbar (QAT).
ms.assetid: 8a873a48-4f8b-439d-acad-7da2081fbf40
keywords:
- Ribbon.QuickAccessToolbar property Windows Ribbon
topic_type:
- apiref
api_name:
- Ribbon.QuickAccessToolbar
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Ribbon.QuickAccessToolbar property

Represents a container for the Quick Access Toolbar (QAT).

## Usage

``` syntax
<Ribbon.QuickAccessToolbar>
  child elements
</Ribbon.QuickAccessToolbar>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                                           | Description                                    |
|-----------------------------------------------------------------------------------|------------------------------------------------|
| [**QuickAccessToolbar**](windowsribbon-element-quickaccesstoolbar.md)<br/> | Must occur exactly once<br/> <br/> |



## Parent elements



| Element                                                   |
|-----------------------------------------------------------|
| [**Ribbon**](windowsribbon-element-ribbon.md)<br/> |



## Remarks

Required.

May occur one or more times for each [**Ribbon**](windowsribbon-element-ribbon.md).

## Examples

The following example demonstrates the basic markup for the **Ribbon.QuickAccessToolbar** element.


```XML
      <Ribbon.QuickAccessToolbar>
        <QuickAccessToolbar CommandName="cmdQAT"
                            CustomizeCommandName="cmdCustomizeQAT">
          <QuickAccessToolbar.ApplicationDefaults>
            <Button CommandName="cmdButton1"/>
            <ToggleButton CommandName="cmdMinimize"
                          ApplicationDefaults.IsChecked="false"/>
          </QuickAccessToolbar.ApplicationDefaults>
        </QuickAccessToolbar>
      </Ribbon.QuickAccessToolbar>
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 






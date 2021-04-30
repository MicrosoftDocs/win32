---
description: The SFGAO flag values of the Shell attributes for an item can be tested to determine whether the verb should be enabled or disabled.
ms.assetid: 3A539A9D-DB6B-4E3D-AD26-D5309BECEBB1
title: How to Use Item Attributes
ms.topic: article
ms.date: 05/31/2018
---

# How to Use Item Attributes

The [**SFGAO**](sfgao.md) flag values of the Shell attributes for an item can be tested to determine whether the verb should be enabled or disabled.

To use this attribute feature, add the following **REG\_DWORD** values under the verb:

## Instructions

### Step 1:

The AttributeMask value specifies the [**SFGAO**](sfgao.md) value of the bit values of the mask to test with.

### Step 2:

The AttributeValue value specifies the [**SFGAO**](sfgao.md) value of the bits that are tested.

### Step 3:

The ImpliedSelectionModel specifies zero for item verbs, or nonzero for verbs on the background shortcut menu.

## Remarks

In the following example registry entry, the AttributeMask is set to [**SFGAO\_READONLY**](sfgao.md) (0x40000).

```
HKEY_CLASSES_ROOT
   txtfile
      Shell
         test.verb2
            AttributeMask = 0x40000
            AttributeValue = 0x0
            ImpliedSelectionModel = 0x0
            command
               (Default) = %SystemRoot%\system32\notepad.exe %1
```

 

 




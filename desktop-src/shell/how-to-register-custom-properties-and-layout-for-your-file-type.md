---
description: After you understand the Search Result mode, the Browse mode, and the layout patterns, you can register a custom property list for your file type.To register a custom property list and layout pattern for your file type, follow these steps.
ms.assetid: 29B863B3-E5FD-4E0A-B76B-4AFE5A6A76E3
title: How to Register Custom Properties and Layout for Your File Type
ms.topic: article
ms.date: 05/31/2018
---

# How to Register Custom Properties and Layout for Your File Type

After you understand the Search Result mode, the Browse mode, and the layout patterns, you can register a custom property list for your file type.

To register a custom property list and layout pattern for your file type, follow these steps.

## Instructions

### Step 1:

Choose from the four layout patterns: Alpha, Beta, Gamma, or Delta.

### Step 2:

Consider the following formatting rules, which apply equally to all four layout patterns:

- Property 1 is always displayed in a larger font size. The large font size usually used for the item name, but can also be used for the anchor or other item property.
- Property 4 is intended for excerpts in the Alpha, Beta, and Gamma layout patterns. This property is allotted more space in those patterns and is displayed in a gray font color, as opposed to black like the other properties, to help it stand out.
- The pixel measurements below are in relative pixels, and the size includes the icon/thumbnail to the left of the properties and the space between the icon/thumbnail and the selection rectangle.
- Most properties have a minimum display size. Therefore, they will not appear if there is not enough space for them at a particular view size. The minimum size is usually 100 pixels wide.
- Each layout pattern defines the number of rows and the number of properties in each row.

### Step 3:

Decide which properties you want to display in the layout, and which property you want to display in each location. When deciding which property to display in each position in the layout, consider the typical length of the property, its importance to the user, and whether it should be dropped when the window size is too small to contain all properties.

### Step 4:

Register a layout pattern and a property list for your file type or item type by adding the following keys under the ProgID registry key for the file type or item (in this example, for the .xyz file type).

```
HKEY_CLASSES_ROOT\*
   Contoso.xyzfile
      (ContentViewModeForBrowse) = <Layout pattern name (Alpha, Beta, Delta, or Gamma)>
      (ContentViewModeForSearch) = <Layout pattern name (Alpha, Beta, Delta, or Gamma)>
      (ContentViewModeLayoutPatternForBrowse) = <PropertyList>
      (ContentViewModeLayoutPatternForSearch) = <PropertyList>
```

### Step 5:

Observe the following formatting guidelines for registering properties:

- Each registration starts with `prop:`
- Each property requires the full property name.
- Properties are separated by a semicolon with no space.
- Properties are displayed in the order defined by the selected layout pattern.
- `~` indicates that the property label should not be displayed.
- `~System.LayoutPattern.PlaceHolder` should be used if you want to leave blank a property that is specified in the layout pattern.

The following sample registry key illustrates these formatting guidelines.

```
HKEY_CLASSES_ROOT\
   Kind.Document
      (ContentViewModeForBrowse) = <PropertyList>
```

Possible values for (ContentViewModeForBrowse) include the following: `prop:~System.ItemNameDisplay;System.Author;System.LayoutPattern.Placeholder;System.Keywords;System.DateModified;~System.Size`

 

 



